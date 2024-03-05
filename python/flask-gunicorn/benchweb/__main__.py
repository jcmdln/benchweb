from __future__ import annotations

from flask import Flask
from gunicorn.app.base import BaseApplication

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def main() -> None:
    from os import cpu_count

    StandaloneApplication(
        app,
        {
            "bind": "127.0.0.1:5150",
            "loglevel": "error",
            "workers": cpu_count(),
        },
    ).run()


if __name__ == "__main__":
    main()
