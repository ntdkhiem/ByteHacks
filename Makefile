web-console:
	@docker-compose exec stjk python manage.py shell
db-seed:
	@docker-compose exec stjk python manage.py create_user byte@hacks.com 1234
db-console:
	@docker-compose exec users_db psql --username=stjk --dbname=stjk_bytehacks