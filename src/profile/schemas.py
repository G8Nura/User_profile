from pydantic import BaseModel
from datetime import date
from typing import Optional

class ProfileBase(BaseModel):
    full_name: str
    photo_url: Optional[str] = None
    birth_date: Optional[date] = None
    locality_id: Optional[int] = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class ProfileResponse(ProfileBase):
    id: int
    locality: Optional["LocalityResponse"] = None  
    class Config:
        from_attributes = True


from src.localities.schemas import LocalityResponse
ProfileResponse.update_forward_refs()
