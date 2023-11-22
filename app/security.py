from fastapi import Security
from fastapi.security.api_key import APIKeyHeader
from app.exceptions import NPaaSException
from app.credential.repos.key_repo import KeyRepo

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)


async def validate_public_key(api_token: str = Security(api_key_header)):
    if api_token:
        app_name, public_key = api_token.split(" ", 1)
        return KeyRepo.verify_token(app_name=app_name, public_key=public_key)
    else:
        raise NPaaSException(
            status_code=403,
            msg="No authorization found"
        )
