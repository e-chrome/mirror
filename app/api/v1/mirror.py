import logging
import uuid
from datetime import datetime

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, JSONResponse

from app.middleware import verify_token

router = APIRouter()


@router.get('/home', response_class=HTMLResponse)
async def home(request: Request, _=Depends(verify_token)):
    reqs = [
        r for r in reversed(request.app.state.request_history.values()) if r['client']['host'] == request.client.host
    ]
    return request.app.state.templates.TemplateResponse('home.html', {'request': request, 'requests': reqs})


@router.api_route('/{path:path}', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
async def mirror(request: Request, path: str, _=Depends(verify_token)):
    try:
        body = await request.body()
        body_text = body.decode('utf-8')
    except UnicodeDecodeError:
        body_text = '[binary data]'
    req_uuid = str(uuid.uuid4())
    request_data = {
        'uuid': req_uuid,
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

    request.app.state.request_history[req_uuid] = request_data
    logging.info(f'New request: {request.method} {path}')

    return JSONResponse(content=request_data)
