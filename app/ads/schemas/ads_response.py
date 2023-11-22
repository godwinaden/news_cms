from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AdsEditSchema(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True)

    id: str
    media_type: str
    goto_url: str
    media_url: str
    npaas_brand_id: str


class AdsDisplaySchema(AdsEditSchema):
    npaas_brand_id: str
