from datetime import datetime

import google.cloud.exceptions
from app.ads.schemas.ads_request import AdsSchema
from app.ads.schemas.ads_response import AdsDisplaySchema
from app.config import get_settings
from google.cloud.firestore_v1 import FieldFilter
from fastapi import Request


class AdsRepo:

    def __init__(self):
        self.settings = get_settings()
        self.col = self.settings.db.collection("ads")

    def create(self, request: Request):
        doc_ref = self.col.document()
        ads = AdsSchema(
            brand_name=request.get("brand_name"),
            npaas_brand_id=request.get("npaas_brand_id"),
            active=False,
            type_id=request.get("type_id"),
            description=request.get("description"),
            days_used=0,
            title=request.get("title"),
            duration_in_days=0,
            media_url=request.get("media_url"),
            media_type=request.get("media_type"),
            paid=request.get("paid"),
            created_on=datetime.now(),
            updated_on=datetime.now(),
            goto_url=request.get("goto_url")
        )
        doc_ref.set(ads.model_dump(mode='python'))
        return {"ads": "Ads was added successfully."}

    def display_active_ads(self, brand_id: str):
        result = []
        ads = (
            self.col
            .where(filter=FieldFilter("brand_id", "==", brand_id))
            .where(filter=FieldFilter("active", "==", True))
            .get()
        )
        if not ads:
            return None
        for ad in ads:
            result.append(AdsDisplaySchema.model_validate(ad.to_dict()))
        return result

    def delete(self, ad_id: str) -> bool:
        ads = self.col.document(ad_id).delete()
        if not ads:
            return False
        else:
            return True

    def update(self, ad_id: str, new_update: dict) -> bool | None:
        try:
            ads = self.col.document(ad_id).set(new_update)
            if not ads:
                return False
            else:
                return True
        except google.cloud.exceptions.NotFound:
            return None
        except:
            return None
