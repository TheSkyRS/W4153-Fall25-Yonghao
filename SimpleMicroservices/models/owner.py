# owner.py
from __future__ import annotations

from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr

from .address import AddressBase


class OwnerBase(BaseModel):
    first_name: str = Field(
        ...,
        description="Owner given name.",
        json_schema_extra={"example": "Ada"},
    )
    last_name: str = Field(
        ...,
        description="Owner family name.",
        json_schema_extra={"example": "Lovelace"},
    )
    email: EmailStr = Field(
        ...,
        description="Primary email address.",
        json_schema_extra={"example": "ada@example.com"},
    )
    phone: Optional[str] = Field(
        None,
        description="Contact phone number in any reasonable format.",
        json_schema_extra={"example": "+1-317-555-0123"},
    )
    government_id: Optional[str] = Field(
        None,
        description="Optional government-issued ID or number.",
        json_schema_extra={"example": "NY-123-456-789"},
    )

    # Embed addresses (each with persistent ID)
    addresses: List[AddressBase] = Field(
        default_factory=list,
        description="Addresses linked to this person (each carries a persistent Address ID).",
        json_schema_extra={
            "example": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "street": "123 Main St",
                    "city": "London",
                    "state": None,
                    "postal_code": "SW1A 1AA",
                    "country": "UK",
                }
            ]
        },
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Leslie",
                    "last_name": "Knope",
                    "email": "leslie.knope@example.com",
                    "phone": "+1-317-555-0123",
                    "government_id": "NY-123-456-789",
                    "addresses": [
                        {
                            "id": "550e8400-e29b-41d4-a716-446655440000",
                            "street": "123 Main St",
                            "city": "London",
                            "state": None,
                            "postal_code": "SW1A 1AA",
                            "country": "UK",
                        }
                    ],
                }
            ]
        }
    }


class OwnerCreate(OwnerBase):
    """Creation payload for an Owner."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "April",
                    "last_name": "Ludgate",
                    "email": "april@example.com",
                    "phone": "+1-317-555-0987",
                    "government_id": None,
                    "addresses": [],
                }
            ]
        }
    }


class OwnerUpdate(BaseModel):
    """Partial update for an Owner; supply only fields to change."""
    first_name: Optional[str] = Field(None, json_schema_extra={"example": "Ann"})
    last_name: Optional[str] = Field(None, json_schema_extra={"example": "Perkins"})
    email: Optional[EmailStr] = Field(None, json_schema_extra={"example": "ann.perkins@example.com"})
    phone: Optional[str] = Field(None, json_schema_extra={"example": "+1-317-555-0000"})
    government_id: Optional[str] = Field(None, json_schema_extra={"example": "CA-987-654-321"})
    addresses: Optional[List[AddressBase]] = Field(
        None,
        description="Replace the entire set of addresses with this list.",
        json_schema_extra={
            "example": [
                {
                    "id": "bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb",
                    "street": "10 Downing St",
                    "city": "London",
                    "state": None,
                    "postal_code": "SW1A 2AA",
                    "country": "UK",
                }
            ]
        },
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"first_name": "Ann", "last_name": "Perkins"},
                {"phone": "+1-317-555-0000"},
                {
                    "addresses": [
                        {
                            "id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
                            "street": "742 Evergreen Terrace",
                            "city": "Springfield",
                            "state": "IL",
                            "postal_code": "62704",
                            "country": "USA",
                        }
                    ]
                },
            ]
        }
    }


class OwnerRead(OwnerBase):
    """Server representation returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Owner ID.",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
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

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Leslie",
                    "last_name": "Knope",
                    "email": "leslie.knope@example.com",
                    "phone": "+1-317-555-0123",
                    "government_id": "NY-123-456-789",
                    "addresses": [
                        {
                            "id": "550e8400-e29b-41d4-a716-446655440000",
                            "street": "123 Main St",
                            "city": "London",
                            "state": None,
                            "postal_code": "SW1A 1AA",
                            "country": "UK",
                        }
                    ],
                    "created_at": "2025-01-15T10:20:30Z",
                    "updated_at": "2025-01-16T12:00:00Z",
                }
            ]
        }
    }