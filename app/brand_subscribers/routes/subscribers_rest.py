from fastapi import APIRouter, Depends

SubscriberRouter = APIRouter(
    prefix="/subscribers",
    tags=["Subscribers"],
)


@SubscriberRouter.get("/")
def get_ads():
    return "pass"


@SubscriberRouter.post("/")
def add_ads():
    return "pass"


@SubscriberRouter.put("/{id}")
def update_ads():
    return "pass"


@SubscriberRouter.delete("/{id}")
def delete_ads():
    return "pass"
