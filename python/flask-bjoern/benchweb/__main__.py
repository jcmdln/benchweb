from __future__ import annotations

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


def main() -> None:
    from bjoern import run as bjoern_run

    bjoern_run(app, "127.0.0.1", 5150)


if __name__ == "__main__":
    main()
