from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        from_attributes = True
        populate_by_name = True
        orm_model = True
