.POSIX:

DURATION=10s
RATE=1000/s

all: build

bench: run
	@sleep 3
	@echo "GET http://0.0.0.0:5150/" | vegeta attack -duration="$(DURATION)" -rate="$(RATE)" | vegeta report
	@pkill go-net-http

build:
	@go build

run:
	@./go-net-http &
