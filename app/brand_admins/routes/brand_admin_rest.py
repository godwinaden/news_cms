from fastapi import APIRouter, Depends

AdminRouter = APIRouter(
    prefix="/brdAdmin",
    tags=["Brand Admin"],
)


@AdminRouter.get("/")
def get_ads():
    return "pass"


@AdminRouter.post("/")
def add_ads():
    return "pass"


@AdminRouter.put("/{id}")
def update_ads():
    return "pass"


@AdminRouter.delete("/{id}")
def delete_ads():
    return "pass"
