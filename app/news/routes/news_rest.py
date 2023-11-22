from fastapi import APIRouter, Depends

NewsRouter = APIRouter(
    prefix="/news",
    tags=["News"],
)


@NewsRouter.get("/")
def get_ads():
    return "pass"


@NewsRouter.post("/")
def add_ads():
    return "pass"


@NewsRouter.put("/{id}")
def update_ads():
    return "pass"


@NewsRouter.delete("/{id}")
def delete_ads():
    return "pass"
