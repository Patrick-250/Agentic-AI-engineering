from pydantic import BaseModel
from typing import Optional


class Creator(BaseModel):
  username:str
  display_name:str
  bio:Optional[str]=None
  profile_pic_url:Optional[str]=None
  email:str

creator=Creator(username="tyrumanzi",display_name=25,email="askmehow@gmail.com")
print(creator)
