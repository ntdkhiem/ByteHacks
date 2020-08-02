db-seed:
	@docker-compose exec stjk python manage.py create_user ntd@gmail.com hello
db-console:
	@docker-compose exec db psql --username=stjk --dbname=stjk_bytehacks