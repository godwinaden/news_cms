from datetime import datetime
from typing import Optional

from app.config import get_settings
from google.cloud.firestore_v1 import FieldFilter
from pydantic import BaseModel, field_validator, ConfigDict

settings = get_settings()
db = settings.db


class AdsSchema(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True)

    id: Optional[str]
    title: str
    type_id: str
    active: Optional[bool]
    created_on: datetime
    paid: float
    duration_in_days: int
    days_used: int
    media_type: str
    goto_url: str
    brand_name: str
    description: Optional[str]
    media_url: str
    npaas_brand_id: str
    updated_on: datetime


class AdsTypeSchema(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True)

    id: Optional[str]
    name: str
    cost: float
    total_duration_in_days: int
    currency: str
    description: str

    @staticmethod
    def from_dict(source: dict):
        if source.keys().__contains__("id"):
            raise ValueError("Wrong source: source has no id")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cost": self
        }

    def __repr__(self):
        return f"AdsType(\
                    name={self.name}, \
                    id={self.id}, \
                    cost={self.cost}, \
                    description={self.description}, \
                    currency={self.currency}\
                )"

    @field_validator("name")
    def validate_name(cls, v, values, **kwargs):
        q = db.collection("ads_types").where(filter=FieldFilter("name", "==", v)).get()
        if len(q) > 0:
            raise ValueError("The ads type name already exists.")
        else:
            return v


class AdsMetricsSchema(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True)

    id: Optional[str]
    ads_id: str
    clicks: int
    impressions: int
    cost_per_day: float
    total_used: int = 0
