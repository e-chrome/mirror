import logging
from typing import Optional

from fastapi import Header, HTTPException, Request


def verify_token(
    request: Request,
    x_token: Optional[str] = Header(None),
):
    expected_token = request.app.state.config.TOKEN
    if x_token != expected_token:
        logging.warning(f'Invalid token attempt: {x_token}')
        raise HTTPException(status_code=403, detail='Invalid token')
    return True
