local_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {'simple': {'format': '%(asctime)-20s : [thread - %(threadName)s] [%(levelname)-3s] : %(message)s'}},
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout',
        }
    },
    'root': {'level': 'INFO', 'handlers': ['console']},
}

main_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'class': 'lib_logging.formatters.CustomJsonFormatter',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout',
        }
    },
    'root': {'level': 'INFO', 'handlers': ['console']},
}
