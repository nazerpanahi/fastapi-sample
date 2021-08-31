from sentry_sdk import init

from config import settings

sentry_app = None
if settings.SENTRY_DSN is not None and isinstance(settings.SENTRY_DSN, str) and len(settings.SENTRY_DSN.strip()) > 0:
    sentry_app = init(dsn=settings.SENTRY_DSN, traces_sample_rate=1.0)
