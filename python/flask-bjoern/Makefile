.POSIX:

all: build bench

bench: run
	@sleep 5
	@go-wrk -d 30 http://localhost:5150
	@pkill -9 --full benchweb
	@sleep 5

build:
	pdm sync --only-keep -G main

clean:
	rm -fr .venv/

run:
	@pdm run benchweb &
