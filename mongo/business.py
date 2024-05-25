from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from bson import ObjectId

# class Address:  # Assuming you have a separate Address model
    # ... define your Address model properties here ...

class Business(BaseModel):
    """
    Represents a business entity.
    """
    id: Optional[ObjectId] = Field(alias="_id", default=None)
    user: ObjectId = Field(...)  # Assuming you have a way to reference the user
    name: str = Field(...)
    description: Optional[str] = None
    picture: Optional[str] = None
    email: EmailStr = Field(...)
    phone: Optional[str] = None
    website: Optional[str] = None
    stripeAccountId: Optional[str] = None
    # address: Optional[Address] = None
    hoursOfOperation: Optional[dict] = None  # Placeholder for HoursOfOperation type
    products: List[ObjectId] = Field(default_factory=list)  # Assuming product references are stored as ObjectIds
    categories: List[ObjectId] = Field(default_factory=list)  # Assuming category references are stored as ObjectIds
    menus: List[ObjectId] = Field(default_factory=list)  # Assuming menu references are stored as ObjectIds
    employees: List[ObjectId] = Field(default_factory=list)  # Assuming employee references are stored as ObjectIds
    employeesPending: List[ObjectId] = Field(default_factory=list)  # Assuming session references are stored as ObjectIds
    # country: str = "BR"
    taxRate: float = Field(default=0.0)
    # created_date: datetime.datetime = Field(default_factory=datetime.datetime.now)
    embeding: List[int] = Field(default_factory=list)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}  # Encode ObjectId to string for JSON serialization

# Using MongoClient
# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")
# db = client["your_database_name"]
# collection = db["businesses"]

# # Example usage
# business = Business(name="My Business", email="info@mybusiness.com", ...)
# collection.insert_one(business.dict(exclude_unset=True))  # Insert into MongoDB

# ... (other operations using Business model)
