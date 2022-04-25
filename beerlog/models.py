from sqlmodel import SQLModel, Field
from sqlmodel import select
from datetime import datetime
from typing import Optional
from pydantic import validator


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0


    @validator("flavor", "image", "cost")
    def validade_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

try:
    brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=8, cost=10)
except RuntimeError:
    print("Zica de mais")