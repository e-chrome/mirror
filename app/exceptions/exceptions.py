import logging

from fastapi.responses import JSONResponse
from starlette import status


async def internal_server_error(_, exc: Exception) -> JSONResponse:
    logging.error(exc)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={'code': 500, 'msg': 'Internal Server Error'}
    )
