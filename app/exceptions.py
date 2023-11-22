from fastapi import HTTPException


class NPaaSException(HTTPException):
    def __init__(self, status_code: int, msg: str, err: Exception = None):
        self.status_code = status_code
        self.msg = msg
        self.error = err


class CredentialsExistException(HTTPException):
    def __init__(self, err: Exception = None):
        self.status_code = 400
        self.msg = "Credentials Already Exists"
        self.error = err


class CredentialsNotFoundException(HTTPException):
    def __init__(self, err: Exception = None):
        self.status_code = 204
        self.msg = "No Credentials Found"
        self.error = err


class InvalidPayloadException(HTTPException):
    def __init__(self, err: Exception = None):
        self.status_code = 400
        self.msg = "Invalid Payload"
        self.error = err


class InvalidNewsException(HTTPException):
    def __init__(self, err: Exception = None):
        self.status_code = 400
        self.msg = "Invalid News"
        self.error = err


class LoginRequiredException(HTTPException):
    def __init__(self, err: Exception = None):
        self.status_code = 401
        self.msg = "Unauthorized Entry"
        self.error = err
