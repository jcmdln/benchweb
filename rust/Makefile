.POSIX:

all: build bench

bench:
	@make bench -C axum
	@make bench -C dropshot

build:
	@make build -C axum
	@make build -C dropshot

clean:
	@make clean -C axum
	@make clean -C dropshot
