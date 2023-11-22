import time
from typing import Optional

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from app.config import get_settings

durations: list = []
settings = get_settings()


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        log(msg="{name:<30} started".format(name=func.__name__), level=20)
        result = func(*args, **kwargs)
        duration = "{name:<30} finished in {elapsed:.2f} seconds".format(
            name=func.__name__, elapsed=time.perf_counter() - start
        )
        log(msg=duration, level=20)
        durations.append(duration)
        return result

    return wrapper


def log(msg: str, level: int = 20, exc: Optional[Exception] = None):
    settings.logger.log(level=level, msg=msg, exc_info=exc)


def generate_hash(credl_raw):
    ph = PasswordHasher()
    return ph.hash(credl_raw)


def verify_hash(credl_hashed, credl_raw):
    ph = PasswordHasher()
    verified: bool = False
    msg = "verified Successfully."
    try:
        verified = ph.verify(credl_hashed, credl_raw)
    except VerifyMismatchError as v:
        msg = f"Invalid Credential. {repr(v)}"
    except Exception as e:
        msg = f"Unexpected Error: \n{e}"
    return verified, msg
