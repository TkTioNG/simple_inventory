build:
	docker compose -f docker-compose.local.yml build

up:
	docker compose -f docker-compose.local.yml up

django:
	docker compose -f docker-compose.local.yml exec django bash
