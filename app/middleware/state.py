from collections import deque
from typing import Deque, Optional

from fastapi.templating import Jinja2Templates

from config import Settings


class AppState:
    def __init__(self):
        self.config: Optional[Settings] = None
        self.request_history: Deque[dict[str, any]] = deque(maxlen=100)
        self.templates: Optional[Jinja2Templates] = None
