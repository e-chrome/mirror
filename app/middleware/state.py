from typing import Optional

from fastapi.templating import Jinja2Templates

from app.tools import LimitedSizeDict
from config import Settings


class AppState:
    def __init__(self):
        self.config: Optional[Settings] = None
        self.request_history: Optional[LimitedSizeDict] = None
        self.templates: Optional[Jinja2Templates] = None
