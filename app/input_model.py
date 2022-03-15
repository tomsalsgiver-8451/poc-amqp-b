from pydantic import BaseModel


# Generic input model
class InputModel(BaseModel):
    message: str
