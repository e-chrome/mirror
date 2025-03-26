import logging

import uvicorn

from config import config
from lib_logging import EnvEnum, get_app_version, init_logging

if __name__ == '__main__':
    logging_config = init_logging(config.ENVIRONMENT)
    logging.info(f'Service started. Version: {get_app_version()}')

    uvicorn.run(
        'app.main:create_app',
        host=config.HOST,
        port=config.PORT,
        reload=config.ENVIRONMENT == EnvEnum.LOCAL,
        log_config=logging_config,
        factory=True,
    )
