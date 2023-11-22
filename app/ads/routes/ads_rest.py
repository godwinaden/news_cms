from typing import List

from app.ads.repos.ads_repo import AdsRepo
from app.ads.routes.ads_metrics_rest import AdsMetricsRouter
from app.ads.routes.ads_type_rest import AdsTypeRouter
from app.ads.schemas.ads_request import AdsSchema
from app.ads.schemas.ads_response import AdsDisplaySchema
from fastapi import APIRouter, Depends, Request

AdsRouter = APIRouter(
    prefix="/ads",
    tags=["Adverts"],
)

AdsRouter.include_router(AdsMetricsRouter)
AdsRouter.include_router(AdsTypeRouter)


@AdsRouter.post("/",
                status_code=200,
                description="This endpoint creates a new ads"
                )
def add_ads(request: Request, repo: AdsRepo = Depends(AdsRepo)):
    return repo.create(request)


@AdsRouter.put("/{id}")
def update_ads():
    return "pass"


@AdsRouter.delete("/{id}")
def delete_ads():
    return "pass"


@AdsRouter.get("/{brand_id}",
               status_code=200,
               response_model=List[AdsDisplaySchema],
               description="This endpoint gets all active ads belonging to a npaas"
                           " brand for display on their platform for their subscribers to see"
               )
def get_ads(request: Request, brand_id: str, repo: AdsRepo = Depends(AdsRepo)):
    return repo.display_active_ads(brand_id)
