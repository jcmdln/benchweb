.POSIX:

all: build

bench:
	@make bench -C blacksheep-uvicorn
	@make bench -C fastapi-uvicorn
	@make bench -C flask-bjoern

build:
	@make build -C blacksheep-uvicorn
	@make build -C fastapi-uvicorn
	@make build -C flask-bjoern

clean:
	@make clean -C blacksheep-uvicorn
	@make clean -C fastapi-uvicorn
	@make clean -C flask-bjoern
