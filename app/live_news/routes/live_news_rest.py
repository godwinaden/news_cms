from fastapi import APIRouter, Depends

LiveNewsRouter = APIRouter(
    prefix="/live_news",
    tags=["Live News"],
)


@LiveNewsRouter.get("/")
def get_ads():
    return "pass"


@LiveNewsRouter.post("/")
def add_ads():
    return "pass"


@LiveNewsRouter.put("/{id}")
def update_ads():
    return "pass"


@LiveNewsRouter.delete("/{id}")
def delete_ads():
    return "pass"
