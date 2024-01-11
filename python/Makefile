.POSIX:

ATTACK_RATE="1000/s"

all: build

bench:
	@make bench -C blacksheep
	@make bench -C fastapi

build:
	@make build -C blacksheep
	@make build -C fastapi
