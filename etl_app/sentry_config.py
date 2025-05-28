import sentry_sdk
import os
from dotenv import load_dotenv
load_dotenv()


def init_sentry():
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        send_default_pii=True,
    )
