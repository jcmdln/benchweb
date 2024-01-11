.POSIX:

all: build

bench:
	@make bench -C go
	@make bench -C python

build:
	@make build -C go
	@make build -C python
