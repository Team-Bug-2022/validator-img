from pydantic import BaseModel

class RequestModel(BaseModel):
  urlImageOld: str
  urlImageNew: str

class ResponseModel(BaseModel):
  match : bool