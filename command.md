docker volume prune
docker volume ls
docker system prune



pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker-compose up -d --build
docker-compose down -v
docker exec -it django python manage.py createsuperuser

