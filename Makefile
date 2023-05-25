up:
	docker compose up --build -d

down:
	docker compose down

start:
	docker compose start

stop:
	docker compose stop

build:
	docker compose build

vol:
	docker volume create db