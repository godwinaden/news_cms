from fastapi import APIRouter, Depends

SubscriptionRouter = APIRouter(
    prefix="/subscriptions",
    tags=["Subscriptions"],
)


@SubscriptionRouter.get("/")
def get_ads():
    return "pass"


@SubscriptionRouter.post("/")
def add_ads():
    return "pass"


@SubscriptionRouter.put("/{id}")
def update_ads():
    return "pass"


@SubscriptionRouter.delete("/{id}")
def delete_ads():
    return "pass"
