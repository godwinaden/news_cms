from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from app.utils import log
from app import exceptions


def npaas_exception_handler(request: Request, exc: exceptions.NPaaSException | HTTPException):
	base_error_message = f"Execution Failed: {request.method}: {request.url}"
	msg = f"{base_error_message}. Detail: {exc.msg}"
	log(msg=msg, level=40, exc=exc.error)
	return JSONResponse(status_code=exc.status_code, content={"message": msg})


def credential_exception_handler(request: Request, exc: exceptions.CredentialsExistException):
	npaas_exception_handler(request, exc)


def no_credential_exception_handler(request: Request, exc: exceptions.CredentialsNotFoundException):
	npaas_exception_handler(request, exc)


def invalid_payload_handler(request: Request, exc: exceptions.InvalidPayloadException):
	npaas_exception_handler(request, exc)


def invalid_request_handler(request: Request, exc: exceptions.InvalidNewsException):
	npaas_exception_handler(request, exc)


def login_needed_handler(request: Request, exc: exceptions.LoginRequiredException):
	npaas_exception_handler(request, exc)
