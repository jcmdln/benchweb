.POSIX:

all: build bench

bench:
	@make bench -C blacksheep-uvicorn
	@make bench -C fastapi-uvicorn
	@make bench -C flask-bjoern
	@make bench -C flask-gunicorn
	@make bench -C litestar-uvicorn

build:
	@make build -C blacksheep-uvicorn
	@make build -C fastapi-uvicorn
	@make build -C flask-bjoern
	@make build -C flask-gunicorn
	@make build -C litestar-uvicorn

clean:
	@make clean -C blacksheep-uvicorn
	@make clean -C fastapi-uvicorn
	@make clean -C flask-bjoern
	@make clean -C flask-gunicorn
	@make clean -C litestar-uvicorn
