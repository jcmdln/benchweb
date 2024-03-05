.POSIX:

all: build bench

bench:
	@make bench -C fiber
	@make bench -C net-http

build:
	@make build -C fiber
	@make build -C net-http

clean:
	@make clean -C fiber
	@make clean -C net-http
