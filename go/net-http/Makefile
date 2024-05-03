.POSIX:

all: build bench

bench: run
	@sleep 5
	@go-wrk -d 30 http://localhost:5150
	@pkill -9 --full go-net-http
	@sleep 5

build:
	go build

clean:
	go clean

run:
	@./go-net-http &
