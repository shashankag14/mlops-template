from pydantic import BaseModel


class Survival(BaseModel):
    name: str
    api_version: str
    model_version: str
