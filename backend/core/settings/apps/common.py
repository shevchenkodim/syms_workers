from core.settings import (
    INSTALLED_APPS,
)

INSTALLED_APPS.append('common.apps.common')

AUTH_USER_MODEL = 'common.User'
