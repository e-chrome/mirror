from collections import deque

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from app.api import api_router
from app.exceptions import internal_server_error
from app.middleware import AppState
from config import config


def create_app():
    app = FastAPI(title='Mirror Service')
    app.include_router(api_router)
    app.state = AppState()

    # Инициализация состояния приложения
    app.state.config = config
    app.state.request_history = deque(maxlen=100)
    app.state.templates = Jinja2Templates(directory='templates')

    app.add_exception_handler(Exception, internal_server_error)

    return app
