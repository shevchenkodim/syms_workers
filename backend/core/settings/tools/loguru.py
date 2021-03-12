import sys
from loguru import logger
from core.settings import DEBUG, BASE_DIR

LOG_PATH = BASE_DIR / 'core/log'

LOGURU_CONFIG = {
    'handlers': [
        {
            'sink': sys.stdout,
            'format':
                "<g>{time:DD-MM-YYYY HH:mm:ss}</g> "
                "<r>|</r> "
                "<lvl>{level}</lvl> "
                "<r>|</r> "
                "<c>{name}</c>"
                "<r>:</r>"
                "<c>{function}</c>"
                "<r>:</r>"
                "<c>{line}</c> "
                "<r>-</r> "
                "<lvl>{message}</lvl> "
                "<lvl>{exception}</lvl>",
            'colorize': True
        },
        {
            'sink': LOG_PATH / 'Auth.log',
            'delay': True,
            'serialize': True,
            'rotation': '10 MB',
            'compression': 'zip',
            'format': '{auth_message}',
            'filter': lambda record: record['extra']['name'] == 'auth_message',
        },
    ],
    'extra': {
        'name': 'default'
    }

}

if not DEBUG:
    logger.configure(**LOGURU_CONFIG)

# if you want async logging.
# enqueue=True
# await logger.complete()

# Fully descriptive exceptions with better-exceptions
# backtrace=True, diagnose=True

# Structured logging as needed. Serialized JSON
# serialize=True

# You can contextualize your logger messages
# logger.add("file.log", format="{extra[ip]} {extra[user]} {message}")
# context_logger = logger.bind(ip="192.168.0.1", user="someone")
# context_logger.info("Contextualize your logger easily")

# Finally, the patch() method allows dynamic values to be attached to the record dict of each new message
# logger.add(sys.stderr, format="{extra[utc]} {message}")
# logger = logger.patch(lambda record: record["extra"].update(utc=datetime.now()))
