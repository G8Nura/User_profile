from pydantic import BaseModel

class LocalityBase(BaseModel):
    country_name: str
    city_name: str


class LocalityCreate(LocalityBase):
    pass 


class LocalityUpdate(LocalityBase):
    pass 


class LocalityResponse(LocalityBase):
    id: int 

    class Config:
        from_attributes = True