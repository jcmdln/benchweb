from __future__ import annotations

from litestar import Litestar, get


@get("/")
async def index() -> str:
    return "Hello, world!"


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


app = Litestar([index, get_book])


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
