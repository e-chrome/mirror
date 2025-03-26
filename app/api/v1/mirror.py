import logging
from datetime import datetime

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, JSONResponse

from app.middleware import verify_token

router = APIRouter()


@router.get('/home', response_class=HTMLResponse)
async def web_interface(request: Request, _=Depends(verify_token)):
    return request.app.state.templates.TemplateResponse(
        'home.html', {'request': request, 'requests': list(reversed(request.app.state.request_history))}
    )


@router.api_route('/{path:path}', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
async def mirror(request: Request, path: str, _=Depends(verify_token)):
    try:
        body = await request.body()
        body_text = body.decode('utf-8')
    except UnicodeDecodeError:
        body_text = '[binary data]'

    request_data = {
        'timestamp': datetime.now().isoformat(),
        'method': request.method,
        'path': path,
        'headers': dict(request.headers),
        'cookies': request.cookies,
        'query_params': dict(request.query_params),
        'http_version': request.scope.get('http_version'),
        'client': {
            'host': request.client.host,
            'port': request.client.port,
        },
        'body': body_text,
        'fingerprint': {
            'ip': request.client.host,
            'user_agent': request.headers.get('user-agent', ''),
        },
    }

    request.app.state.request_history.append(request_data)
    logging.info(f'New request: {request.method} {path}')

    return JSONResponse(content=request_data)
