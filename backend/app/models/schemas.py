from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")

class RegionBase(BaseModel):
    region_name: str
    zone_head: str
    created_at: datetime = Field(default_factory=datetime.now)

class Region(RegionBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    class Config:
        json_encoders = {ObjectId: str}

class EmployeeBase(BaseModel):
    employee_code: str
    name: str
    email: str
    phone: str
    designation: str
    department: str
    region_id: PyObjectId
    active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)
    created_by: str = "admin"
    updated_at: datetime = Field(default_factory=datetime.now)
    updated_by: str = "manager"

class Employee(EmployeeBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    class Config:
        json_encoders = {ObjectId: str}

class ProductBase(BaseModel):
    product_code: str
    product_name: str
    product_type: str
    brand: str
    price: float
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Product(ProductBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    class Config:
        json_encoders = {ObjectId: str}

class SaleBase(BaseModel):
    employee_id: PyObjectId
    product_id: PyObjectId
    region_id: PyObjectId
    quantity: int
    total_amount: float
    sale_date: datetime
    created_at: datetime = Field(default_factory=datetime.now)

class Sale(SaleBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    class Config:
        json_encoders = {ObjectId: str}

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    chart_type: str
    x_field: str
    y_field: str
    title: str
    data: List[Dict[str, Any]]
