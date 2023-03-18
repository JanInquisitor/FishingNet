from typing import Optional

import flask
from flask import Request


class ViewModelBase:
    def __int__(self):
        self.requests: Request = flask.request
        self.error: Optional[str] = None
