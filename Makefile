.POSIX:

all: build

bench:
	@make bench -C go
	@make bench -C python
	@make bench -C rust

build:
	@make build -C go
	@make build -C python
	@make build -C rust

clean:
	@make clean -C go
	@make clean -C python
	@make clean -C rust
