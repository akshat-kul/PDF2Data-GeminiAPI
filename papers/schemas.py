from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from config.schemas import Params, Section

class SamplePaper(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    title: str
    type: str
    time: int
    marks: int
    params: Params  
    tags: List[str]
    chapters: List[str]
    sections: List[Section] 

    @classmethod
    def from_mongo(cls, document: dict):
        """Converts MongoDB's ObjectId to string when returning data."""
        document["_id"] = str(document["_id"]) if "_id" in document else None
        return cls(**document)

    def to_mongo(self):
        """Converts the model to a dict, ensuring _id is an ObjectId for MongoDB."""
        data = self.model_dump(by_alias=True)
        if data["_id"] is None:
            del data["_id"]
        else:
            data["_id"] = ObjectId(data["_id"])  # Convert _id to ObjectId
        return data