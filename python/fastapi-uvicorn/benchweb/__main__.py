from __future__ import annotations

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root() -> str:
    return "Hello, world!"


def main() -> None:
    from os import cpu_count

    from uvicorn import run as uvicorn_run

    uvicorn_run(
        "benchweb.__main__:app",
        host="0.0.0.0",
        port=5150,
        workers=cpu_count(),
        log_level="warning",
    )


if __name__ == "__main__":
    main()
