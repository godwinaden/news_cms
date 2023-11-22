from fastapi import APIRouter, Depends

BrandRouter = APIRouter(
    prefix="/brands",
    tags=["Brands"],
)


@BrandRouter.get("/")
def get_ads():
    return "pass"


@BrandRouter.post("/")
def add_ads():
    return "pass"


@BrandRouter.put("/{id}")
def update_ads():
    return "pass"


@BrandRouter.delete("/{id}")
def delete_ads():
    return "pass"
