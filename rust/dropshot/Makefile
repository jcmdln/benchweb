.POSIX:

all: build bench

bench: run
	@sleep 5
	@go-wrk -d 30 http://localhost:5150
	@pkill -9 --full rust-dropshot
	@sleep 5

build:
	cargo build --release

clean:
	cargo clean

run:
	@./target/release/rust-dropshot &
