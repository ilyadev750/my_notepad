from django.http import HttpResponse
from django.shortcuts import render, redirect
from .functions import (
    prepare_data_for_form,
    add_info_in_new_object_and_session,
    add_info_in_session,
    extract_data_from_object,
    add_info_in_current_object_and_session,
    make_pdf,
)
from .forms import AnonymousNoteForm, UserCreateNoteForm, UserUpdateNoteForm
from django.contrib.auth.models import User
from .models import Note


def anonymous_note(request, *args, **kwargs):
    data = prepare_data_for_form(request)
    form = AnonymousNoteForm(data)

    if request.method == "POST":
        form = AnonymousNoteForm(request.POST)
        request = add_info_in_session(form, request)

        if "login" in request.POST:  # separate login and register
            return redirect("login")

        elif "register" in request.POST:  # separate login and register
            return redirect("register")

        elif "download" in request.POST:
            pdf = make_pdf(request)
            return HttpResponse(pdf, content_type="application/pdf")

    context = {"form": form}
    return render(request, "note/note.html", context)


def get_user_notes(request, *args, **kwargs):
    if request.user.is_authenticated:
        user_id = (User.objects.get(username=request.user.username)).id
        user_objects = Note.objects.filter(username_id=user_id)
        context = {
            "user_objects": user_objects,
            "username": request.user.username
            }
        return render(request, "note/all_user_notes.html", context)


def new_user_note(request, *args, **kwargs):
    request.session["title"] = ""
    request.session["content"] = ""

    if request.user.is_authenticated:
        data = prepare_data_for_form(request)
        form = UserCreateNoteForm(data)

        if request.method == "POST":
            form = UserCreateNoteForm(request.POST)
            empty_obj = Note()
            if form.is_valid():
                filled_obj, request = add_info_in_new_object_and_session(
                    empty_obj, form, request
                )

                if "save" in request.POST:
                    filled_obj.save()
                    return redirect("get_user_notes", request.user.username)

                elif "download" in request.POST:
                    pdf = make_pdf(request)
                    return HttpResponse(pdf, content_type="application/pdf")

        context = {
            "form": form,
            "username": request.user.username
            }
        return render(request, "note/note.html", context)


def update_user_note(request, *args, **kwargs):
    if request.user.is_authenticated:
        user_id = (User.objects.get(username=kwargs['username'])).id
        current_user_object = Note.objects.get(
            username_id=user_id, slug=kwargs["slug"]
        )
        data = extract_data_from_object(current_user_object)
        form = UserUpdateNoteForm(data)
        if request.method == "POST":
            form = UserUpdateNoteForm(request.POST)
            if form.is_valid():
                current_user_object,
                request = add_info_in_current_object_and_session(
                    current_user_object, form, request
                )

            if "save" in request.POST:
                current_user_object.save()
                return redirect("get_user_notes", request.user.username)

            elif "download" in request.POST:
                pdf = make_pdf(request)
                return HttpResponse(pdf, content_type="application/pdf")

        context = {
            "form": form,
            "username": request.user.username,
            "slug": current_user_object.slug
            }
        return render(request, "note/note.html", context)


def delete_user_note(request, *args, **kwargs):
    if request.user.is_authenticated:
        user_id = (User.objects.get(username=kwargs['username'])).id
        current_user_object = Note.objects.get(
            username_id=user_id, slug=kwargs["slug"]
        )
        current_user_object.delete()
        return redirect("get_user_notes", request.user.username)
