from app.ads.repos.ads_repo import AdsRepo
from fastapi import APIRouter, Depends

AdsMetricsRouter = APIRouter(
    prefix="/metrics",
    tags=["Ads Metrics"],
)


@AdsMetricsRouter.get("/")
def get_ads():
    return "pass"


@AdsMetricsRouter.post("/")
def add_ads():
    return AdsRepo().create()


@AdsMetricsRouter.put("/{id}")
def update_ads():
    return "pass"


@AdsMetricsRouter.delete("/{id}")
def delete_ads():
    return "pass"
