from fastapi import APIRouter, Depends

CredentialRouter = APIRouter(
    prefix="/credentials",
    tags=["Credentials"],
)


@CredentialRouter.get("/")
def get_ads():
    return "pass"


@CredentialRouter.post("/")
def add_ads():
    return "pass"


@CredentialRouter.put("/{id}")
def update_ads():
    return "pass"


@CredentialRouter.delete("/{id}")
def delete_ads():
    return "pass"
