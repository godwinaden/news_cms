from app.ads.repos.ads_repo import AdsRepo
from fastapi import APIRouter, Depends

AdsTypeRouter = APIRouter(
    prefix="/type",
    tags=["Ads Type"],
)


@AdsTypeRouter.get("/")
def get_ads():
    return "pass"


@AdsTypeRouter.post("/")
def add_ads():
    return AdsRepo().create()


@AdsTypeRouter.put("/{id}")
def update_ads():
    return "pass"


@AdsTypeRouter.delete("/{id}")
def delete_ads():
    return "pass"
