from fastapi import APIRouter, Depends

MailerRouter = APIRouter(
    prefix="/mailer",
    tags=["Mailer"],
)


@MailerRouter.get("/")
def get_ads():
    return "pass"


@MailerRouter.post("/")
def add_ads():
    return "pass"


@MailerRouter.put("/{id}")
def update_ads():
    return "pass"


@MailerRouter.delete("/{id}")
def delete_ads():
    return "pass"
