from functools import wraps
from fastapi import Request
from app.exceptions import LoginRequiredException


def login_required(func):
    @wraps(func)
    def wrapper(request: Request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise LoginRequiredException()
        return func(request, *args, **kwargs)

    return wrapper
