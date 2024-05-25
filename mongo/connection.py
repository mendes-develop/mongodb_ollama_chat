from pymongo import MongoClient, ReturnDocument
import os

from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator

from typing_extensions import Annotated, Literal

from bson import ObjectId
# from pymongo import ReturnDocument

from typing import Optional, List
# from pydantic import BaseModel, EmailStr, Field, ConfigDict, OptionalDict
# from bson import ObjectId

URL = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

print(URL, DB_NAME)

client = MongoClient(URL)
db = client[DB_NAME]

# User collection
USER = db["Business"]


PyObjectId = Annotated[str, BeforeValidator(str)]

# create business model here


# class Address:  # Assuming you have a separate Address model
    # ... define your Address model properties here ...

# class Business(BaseModel):
#     """
#     Represents a business entity.
#     """
#     id: Optional[ObjectId] = Field(alias="_id", default=None)
#     # user: ObjectId = Field(...)  # Assuming you have a way to reference the user
#     name: str = Field(...)
#     description: Optional[str] = None
#     picture: Optional[str] = None
#     email: EmailStr = Field(...)
#     phone: Optional[str] = None
#     website: Optional[str] = None
#     stripeAccountId: Optional[str] = None
#     # address: Optional[Address] = None
#     hoursOfOperation: Optional[dict] = None  # Placeholder for HoursOfOperation type
#     # products: List[ObjectId] = Field(default_factory=list)  # Assuming product references are stored as ObjectIds
#     # categories: List[ObjectId] = Field(default_factory=list)  # Assuming category references are stored as ObjectIds
#     # menus: List[ObjectId] = Field(default_factory=list)  # Assuming menu references are stored as ObjectIds
#     employees: List[ObjectId] = Field(default_factory=list)  # Assuming employee references are stored as ObjectIds
#     employeesPending: List[ObjectId] = Field(default_factory=list)  # Assuming session references are stored as ObjectIds
#     country: str = Literal["BR", "US"]
#     taxRate: float = Field(default=0.0)
    # created_date: datetime.datetime = Field(default_factory=datetime.datetime.now)

# Find a document with a specific ID (replace with your desired criteria)
