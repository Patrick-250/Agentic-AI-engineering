from pydantic import BaseModel,Field
from typing import Optional


class Creator(BaseModel):
  username:str=Field(max_length=20,min_length=4)
  display_name:str=Field(max_length=10,min_length=4)
  bio:Optional[str]=None
  profile_pic_url:Optional[str]=None
  email:str

creator=Creator(username="tyrumanzi",display_name="Rumanzi",email="askmehow@gmail.com")
print(creator)


