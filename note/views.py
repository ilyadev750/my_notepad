from django.core.cache import cache
from .tasks import create_new_note, update_current_note
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render, redirect
from .functions import (
    prepare_data_for_form,
    add_info_in_session,
    extract_data_from_object,
    get_queryset_from_db,
    reset_session
)
from .forms import AnonymousNoteForm, UserCreateNoteForm, UserUpdateNoteForm
from .models import Note


def anonymous_note(request, *args, **kwargs):
    data = prepare_data_for_form(request)
    form = AnonymousNoteForm(data)

    if request.method == "POST":
        form = AnonymousNoteForm(request.POST)
        request = add_info_in_session(form, request)

        if "login" in request.POST:
            return redirect("login")

        elif "register" in request.POST:
            return redirect("registration")

    context = {"form": form}
    return render(request, "note/note.html", context)


def get_user_notes(request, *args, **kwargs):
    username = request.user.username

    if request.user.is_authenticated:
        cache_key = username
        user_notes = cache.get(cache_key)

        if not user_notes:
            q = Q(username_id__username=username)
            user_notes = (
                Note.objects.select_related('username_id')
                .filter(q)
                .order_by('-update')
                )
            cache.set(cache_key, user_notes, timeout=10)

        context = {
            "user_objects": user_notes,
            "username": username,
            }
        return render(request, "note/all_user_notes.html", context)

    return redirect('home')


def new_user_note(request, *args, **kwargs):
    if request.user.is_authenticated:

        data = prepare_data_for_form(request)
        form = UserCreateNoteForm(data)

        if request.method == "POST":
            form = UserCreateNoteForm(request.POST)
            if form.is_valid():
                create_new_note.delay(form.cleaned_data, request.user.username)
                reset_session(request)
                return redirect('success', 'created')

        context = {
            "form": form,
            "username": request.user.username
            }

        return render(request, "note/note.html", context)

    return redirect('home')


def update_user_note(request, *args, **kwargs):
    username = request.user.username

    if request.user.is_authenticated:
        current_note_object = cache.get(kwargs["slug"])

        if not current_note_object:
            current_note_object = get_queryset_from_db(
                username, kwargs["slug"]
                )
            if not current_note_object:
                return redirect('get_user_notes', username)
            current_note_object = current_note_object[0]
            cache.set(kwargs["slug"], current_note_object, timeout=100)

        data = extract_data_from_object(current_note_object)
        form = UserUpdateNoteForm(data)
        if request.method == "POST":
            form = UserUpdateNoteForm(request.POST)
            if form.is_valid():
                update_current_note.delay(
                    form.cleaned_data, username, kwargs["slug"]
                    )
                return redirect('success', 'updated')

        context = {
            "form": form,
            "username": request.user.username,
            "slug": current_note_object.slug
            }

        return render(request, "note/note.html", context)

    return redirect('home')


def delete_user_note(request, *args, **kwargs):
    if request.user.is_authenticated:

        q1 = Q(username_id__username=kwargs['username'])
        q2 = Q(slug=kwargs["slug"])

        current_user_object = (
            Note.objects.select_related('username_id')
            .get(q1 & q2)
            )
        current_user_object.delete()

        cache.delete(kwargs['username'])
        return redirect("get_user_notes", kwargs['username'])

    return redirect('home')


def success(request, message):
    get_user_notes = reverse("get_user_notes", args=[request.user.username])

    if message == 'created':
        message = 'New note is created!'

    elif message == 'updated':
        message = 'Chosen note is updated!'

    context = {
        'get_user_notes': get_user_notes,
        'message': message
        }

    return render(request, 'note/success.html', context)
