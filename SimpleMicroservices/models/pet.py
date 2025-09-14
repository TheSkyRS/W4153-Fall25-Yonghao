# pet.py
from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, date
from pydantic import BaseModel, Field

from .owner import OwnerRead


class PetBase(BaseModel):
    name: str = Field(
        ...,
        description="Pet's given name.",
        json_schema_extra={"example": "Buddy"},
    )
    species: str = Field(
        ...,
        description="Type of animal.",
        json_schema_extra={"example": "Dog"},
    )
    breed: Optional[str] = Field(
        None,
        description="Specific breed if applicable.",
        json_schema_extra={"example": "Golden Retriever"},
    )
    birth_date: Optional[date] = Field(
        None,
        description="Date of birth (YYYY-MM-DD).",
        json_schema_extra={"example": "2020-05-10"},
    )
    color: Optional[str] = Field(
        None,
        description="Primary color of the pet.",
        json_schema_extra={"example": "Golden"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Buddy",
                    "species": "Dog",
                    "breed": "Golden Retriever",
                    "birth_date": "2020-05-10",
                    "color": "Golden",
                }
            ]
        }
    }


class PetCreate(PetBase):
    """Creation payload for a Pet."""
    owner_id: UUID = Field(
        ...,
        description="The Owner ID this pet belongs to.",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Whiskers",
                    "species": "Cat",
                    "breed": "Siamese",
                    "birth_date": "2021-07-04",
                    "color": "Cream",
                    "owner_id": "99999999-9999-4999-8999-999999999999",
                }
            ]
        }
    }


class PetUpdate(BaseModel):
    """Partial update for a Pet; supply only fields to change."""
    name: Optional[str] = Field(None, json_schema_extra={"example": "Max"})
    species: Optional[str] = Field(None, json_schema_extra={"example": "Dog"})
    breed: Optional[str] = Field(None, json_schema_extra={"example": "Labrador"})
    birth_date: Optional[date] = Field(None, json_schema_extra={"example": "2019-12-25"})
    color: Optional[str] = Field(None, json_schema_extra={"example": "Black"})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "Max"},
                {"breed": "Labrador", "color": "Black"},
            ]
        }
    }


class PetRead(PetBase):
    """Server representation returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Pet ID.",
        json_schema_extra={"example": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"},
    )
    owner: Optional[OwnerRead] = Field(
        None,
        description="The Owner record this pet belongs to.",
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )