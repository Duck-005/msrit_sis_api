from pydantic import BaseModel

class Data(BaseModel):
    usn : str = None
    section: str = None
    photo: str = None
    name: str = None
    sem: str = None
    lastUpdated: str = None
    courseData: list = None