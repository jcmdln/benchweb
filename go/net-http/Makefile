.POSIX:

CPUS=1
DURATION=10s
RATE=1000/s

all: build bench

bench: run
	@sleep 5
	@echo "GET http://0.0.0.0:5150/" | vegeta -cpus=$(CPUS) attack -duration="$(DURATION)" -rate="$(RATE)" | vegeta report
	@pkill -9 --full go-net-http
	@sleep 5

build:
	go build

clean:
	go clean

run:
	@./go-net-http &
