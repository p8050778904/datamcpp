import asyncio
from datetime import datetime, timedelta
import random
import sys
import os
from bson import ObjectId

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from backend.app.database.mongodb import connect_to_mongo, close_mongo_connection, get_database

async def seed_data():
    await connect_to_mongo()
    db = get_database()

    # Clear existing data
    await db.regions.delete_many({})
    await db.employees.delete_many({})
    await db.products.delete_many({})
    await db.sales.delete_many({})

    print("Cleaning up old data...")

    # 1. Regions
    regions_data = [
        {"region_name": "South", "zone_head": "Mr. Kumar", "created_at": datetime.now()},
        {"region_name": "West", "zone_head": "Ms. Priya", "created_at": datetime.now()},
        {"region_name": "North", "zone_head": "Mr. Singh", "created_at": datetime.now()},
        {"region_name": "East", "zone_head": "Ms. Chatterjee", "created_at": datetime.now()}
    ]
    regions_inserted = await db.regions.insert_many(regions_data)
    region_ids = regions_inserted.inserted_ids
    region_map = {regions_data[i]["region_name"]: region_ids[i] for i in range(len(regions_data))}

    # 2. Products (Croma Style)
    products_data = [
        {"product_code": "P001", "product_name": "iPhone 15 Pro", "product_type": "Mobile", "brand": "Apple", "price": 120000},
        {"product_code": "P002", "product_name": "Samsung S24 Ultra", "product_type": "Mobile", "brand": "Samsung", "price": 110000},
        {"product_code": "P003", "product_name": "MacBook Air M3", "product_type": "Laptop", "brand": "Apple", "price": 95000},
        {"product_code": "P004", "product_name": "Dell XPS 13", "product_type": "Laptop", "brand": "Dell", "price": 85000},
        {"product_code": "P005", "product_name": "Sony 55-inch 4K TV", "product_type": "TV", "brand": "Sony", "price": 65000},
        {"product_code": "P006", "product_name": "LG Front Load Washer", "product_type": "Appliances", "brand": "LG", "price": 45000},
        {"product_code": "P007", "product_name": "Bose QuietComfort", "product_type": "Audio", "brand": "Bose", "price": 25000},
        {"product_code": "P008", "product_name": "iPad Pro 11", "product_type": "Tablet", "brand": "Apple", "price": 70000},
    ]
    for p in products_data:
        p["created_at"] = datetime.now()
        p["updated_at"] = datetime.now()
    products_inserted = await db.products.insert_many(products_data)
    product_ids = products_inserted.inserted_ids

    # 3. Employees
    designations = ["Sales Executive", "Senior Sales", "Store Manager"]
    departments = ["Retail Sales", "Customer Support", "Inventory"]
    employees_data = []
    names = ["Rahul Sharma", "Anjali Gupta", "Vikram Singh", "Sanya Iyer", "Amit Patel", "Deepa Mehra", "Karan Johar", "Neha Kapoor"]
    
    for i, name in enumerate(names):
        reg_id = random.choice(region_ids)
        employees_data.append({
            "employee_code": f"EMP{100+i}",
            "name": name,
            "email": f"{name.lower().replace(' ', '.')}@croma.com",
            "phone": f"98765432{10+i}",
            "designation": random.choice(designations),
            "department": random.choice(departments),
            "region_id": reg_id,
            "active": True if i < 7 else False, # 1 inactive for testing
            "created_at": datetime.now(),
            "created_by": "admin",
            "updated_at": datetime.now(),
            "updated_by": "manager"
        })
    employees_inserted = await db.employees.insert_many(employees_data)
    employee_ids = employees_inserted.inserted_ids

    # 4. Sales (Central Collection)
    sales_data = []
    for _ in range(150):
        emp_id = random.choice(employee_ids)
        prod_id = random.choice(product_ids)
        
        # Get employee's region
        emp_doc = await db.employees.find_one({"_id": emp_id})
        reg_id = emp_doc["region_id"]
        
        # Get product price
        prod_doc = await db.products.find_one({"_id": prod_id})
        price = prod_doc["price"]
        
        qty = random.randint(1, 3)
        sales_data.append({
            "employee_id": emp_id,
            "product_id": prod_id,
            "region_id": reg_id,
            "quantity": qty,
            "total_amount": qty * price,
            "sale_date": datetime.now() - timedelta(days=random.randint(0, 180)),
            "created_at": datetime.now()
        })
    await db.sales.insert_many(sales_data)

    # 5. Indexes
    print("Creating indexes...")
    await db.employees.create_index("email", unique=True)
    await db.employees.create_index("region_id")
    await db.employees.create_index("active")
    
    await db.sales.create_index("employee_id")
    await db.sales.create_index("product_id")
    await db.sales.create_index("region_id")
    await db.sales.create_index("sale_date")
    await db.sales.create_index("total_amount")
    
    await db.products.create_index("brand")
    await db.products.create_index("product_type")
    
    await db.regions.create_index("region_name")

    print("Database seeded with Croma Retail Model successfully!")
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(seed_data())
