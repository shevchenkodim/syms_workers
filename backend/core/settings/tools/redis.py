from core.settings import env

REDIS_DB = env.int('REDIS_DB', 0)
REDIS_HOST = env.str('REDIS_HOST', '')
REDIS_PORT = env.int('REDIS_PORT', '')
REDIS_USER = env.str('REDIS_USER', '')
REDIS_PASSWORD = env.str('REDIS_PASSWORD', '')
