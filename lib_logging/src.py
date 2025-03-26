from logging import config as logging_config

from lib_logging.configs import local_config, main_config
from lib_logging.enums import EnvEnum


def init_logging(environment: EnvEnum = EnvEnum.LOCAL, config: dict = main_config) -> dict:
    """
    Функция для инициализации логирования cогласно формату, лежащего в корне проекта.
    Для локального окружения логи будут писаться в дефолтном формате, для других окружений будет
    использован json-формат логов.

    Логирование следует инициализировать перед запуском сервиса, в случае сервисов на fastapi
    следует передавать сгенерированный конфиг в unicorn
    """

    if environment == EnvEnum.LOCAL:
        config = local_config

    logging_config.dictConfig(config)

    return config
