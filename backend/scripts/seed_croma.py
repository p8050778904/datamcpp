import asyncio
import os
import sys
from datetime import datetime
from bson import ObjectId

# Add the project root to sys.path to allow imports from backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from backend.app.database.mongodb import connect_to_mongo, get_database, close_mongo_connection

async def seed_data():
    await connect_to_mongo()
    db = get_database()

    # Drop collections to clear everything including indexes if necessary
    await db.regions.drop()
    await db.products.drop()
    await db.employees.drop()
    await db.sales.drop()

    print("Dropped collections.")

    # Regions
    regions = [
        { "_id": ObjectId("65a000000000000000000001"), "region_name": "South", "zone_head": "Mr. Kumar", "created_at": datetime(2025, 1, 1) },
        { "_id": ObjectId("65a000000000000000000002"), "region_name": "West", "zone_head": "Ms. Mehta", "created_at": datetime(2025, 1, 1) },
        { "_id": ObjectId("65a000000000000000000003"), "region_name": "North", "zone_head": "Mr. Singh", "created_at": datetime(2025, 1, 1) },
        { "_id": ObjectId("65a000000000000000000004"), "region_name": "East", "zone_head": "Mr. Das", "created_at": datetime(2025, 1, 1) }
    ]
    await db.regions.insert_many(regions)
    print(f"Inserted {len(regions)} regions.")

    # Products
    products = [
        { "_id": ObjectId("67c000000000000000000001"), "product_code": "P001", "product_name": "iPhone 15", "product_type": "Mobile", "brand": "Apple", "price": 80000 },
        { "_id": ObjectId("67c000000000000000000002"), "product_code": "P002", "product_name": "MacBook Air M2", "product_type": "Laptop", "brand": "Apple", "price": 120000 },
        { "_id": ObjectId("67c000000000000000000003"), "product_code": "P003", "product_name": "iPad Pro", "product_type": "Tablet", "brand": "Apple", "price": 90000 },
        { "_id": ObjectId("67c000000000000000000004"), "product_code": "P004", "product_name": "Samsung Galaxy S24", "product_type": "Mobile", "brand": "Samsung", "price": 75000 },
        { "_id": ObjectId("67c000000000000000000005"), "product_code": "P005", "product_name": "Samsung Galaxy Book", "product_type": "Laptop", "brand": "Samsung", "price": 95000 },
        { "_id": ObjectId("67c000000000000000000006"), "product_code": "P006", "product_name": "Samsung Galaxy Tab S9", "product_type": "Tablet", "brand": "Samsung", "price": 70000 },
        { "_id": ObjectId("67c000000000000000000007"), "product_code": "P007", "product_name": "Dell XPS 13", "product_type": "Laptop", "brand": "Dell", "price": 110000 },
        { "_id": ObjectId("67c000000000000000000008"), "product_code": "P008", "product_name": "Dell Inspiron 15", "product_type": "Laptop", "brand": "Dell", "price": 70000 },
        { "_id": ObjectId("67c000000000000000000009"), "product_code": "P009", "product_name": "HP Spectre x360", "product_type": "Laptop", "brand": "HP", "price": 105000 },
        { "_id": ObjectId("67c000000000000000000010"), "product_code": "P010", "product_name": "HP Pavilion", "product_type": "Laptop", "brand": "HP", "price": 65000 },
        { "_id": ObjectId("67c000000000000000000011"), "product_code": "P011", "product_name": "Lenovo ThinkPad X1", "product_type": "Laptop", "brand": "Lenovo", "price": 115000 },
        { "_id": ObjectId("67c000000000000000000012"), "product_code": "P012", "product_name": "Lenovo Tab P12", "product_type": "Tablet", "brand": "Lenovo", "price": 50000 },
        { "_id": ObjectId("67c000000000000000000013"), "product_code": "P013", "product_name": "OnePlus 12", "product_type": "Mobile", "brand": "OnePlus", "price": 60000 },
        { "_id": ObjectId("67c000000000000000000014"), "product_code": "P014", "product_name": "OnePlus Pad", "product_type": "Tablet", "brand": "OnePlus", "price": 45000 },
        { "_id": ObjectId("67c000000000000000000015"), "product_code": "P015", "product_name": "Asus ROG Laptop", "product_type": "Laptop", "brand": "Asus", "price": 130000 },
        { "_id": ObjectId("67c000000000000000000016"), "product_code": "P016", "product_name": "Asus Zenbook", "product_type": "Laptop", "brand": "Asus", "price": 90000 },
        { "_id": ObjectId("67c000000000000000000017"), "product_code": "P017", "product_name": "Acer Aspire 7", "product_type": "Laptop", "brand": "Acer", "price": 75000 },
        { "_id": ObjectId("67c000000000000000000018"), "product_code": "P018", "product_name": "Acer Iconia Tab", "product_type": "Tablet", "brand": "Acer", "price": 40000 },
        { "_id": ObjectId("67c000000000000000000019"), "product_code": "P019", "product_name": "Google Pixel 8", "product_type": "Mobile", "brand": "Google", "price": 70000 },
        { "_id": ObjectId("67c000000000000000000020"), "product_code": "P020", "product_name": "Microsoft Surface Laptop", "product_type": "Laptop", "brand": "Microsoft", "price": 125000 }
    ]
    await db.products.insert_many(products)
    print(f"Inserted {len(products)} products.")

    # Employees
    employees = [
        { "_id": ObjectId("66b000000000000000000001"), "employee_code": "EMP001", "name": "Rahul Sharma", "region_id": ObjectId("65a000000000000000000001"), "active": True },
        { "_id": ObjectId("66b000000000000000000002"), "employee_code": "EMP002", "name": "Priya Nair", "region_id": ObjectId("65a000000000000000000001"), "active": True },
        { "_id": ObjectId("66b000000000000000000003"), "employee_code": "EMP003", "name": "Arjun Reddy", "region_id": ObjectId("65a000000000000000000001"), "active": False },
        { "_id": ObjectId("66b000000000000000000004"), "employee_code": "EMP004", "name": "Sneha Iyer", "region_id": ObjectId("65a000000000000000000001"), "active": True },
        { "_id": ObjectId("66b000000000000000000005"), "employee_code": "EMP005", "name": "Karthik Rao", "region_id": ObjectId("65a000000000000000000001"), "active": True },
        { "_id": ObjectId("66b000000000000000000006"), "employee_code": "EMP006", "name": "Amit Shah", "region_id": ObjectId("65a000000000000000000002"), "active": True },
        { "_id": ObjectId("66b000000000000000000007"), "employee_code": "EMP007", "name": "Neha Patel", "region_id": ObjectId("65a000000000000000000002"), "active": True },
        { "_id": ObjectId("66b000000000000000000008"), "employee_code": "EMP008", "name": "Rohan Desai", "region_id": ObjectId("65a000000000000000000002"), "active": False },
        { "_id": ObjectId("66b000000000000000000009"), "employee_code": "EMP009", "name": "Meera Joshi", "region_id": ObjectId("65a000000000000000000002"), "active": True },
        { "_id": ObjectId("66b000000000000000000010"), "employee_code": "EMP010", "name": "Vikram Malhotra", "region_id": ObjectId("65a000000000000000000002"), "active": True },
        { "_id": ObjectId("66b000000000000000000011"), "employee_code": "EMP011", "name": "Raj Singh", "region_id": ObjectId("65a000000000000000000003"), "active": True },
        { "_id": ObjectId("66b000000000000000000012"), "employee_code": "EMP012", "name": "Anjali Verma", "region_id": ObjectId("65a000000000000000000003"), "active": True },
        { "_id": ObjectId("66b000000000000000000013"), "employee_code": "EMP013", "name": "Deepak Yadav", "region_id": ObjectId("65a000000000000000000003"), "active": False },
        { "_id": ObjectId("66b000000000000000000014"), "employee_code": "EMP014", "name": "Pooja Kapoor", "region_id": ObjectId("65a000000000000000000003"), "active": True },
        { "_id": ObjectId("66b000000000000000000015"), "employee_code": "EMP015", "name": "Sanjay Kumar", "region_id": ObjectId("65a000000000000000000003"), "active": True },
        { "_id": ObjectId("66b000000000000000000016"), "employee_code": "EMP016", "name": "Subhash Das", "region_id": ObjectId("65a000000000000000000004"), "active": True },
        { "_id": ObjectId("66b000000000000000000017"), "employee_code": "EMP017", "name": "Ritika Sen", "region_id": ObjectId("65a000000000000000000004"), "active": True },
        { "_id": ObjectId("66b000000000000000000018"), "employee_code": "EMP018", "name": "Aman Roy", "region_id": ObjectId("65a000000000000000000004"), "active": False },
        { "_id": ObjectId("66b000000000000000000019"), "employee_code": "EMP019", "name": "Tina Paul", "region_id": ObjectId("65a000000000000000000004"), "active": True },
        { "_id": ObjectId("66b000000000000000000020"), "employee_code": "EMP020", "name": "Rahul Bose", "region_id": ObjectId("65a000000000000000000004"), "active": True }
    ]
    
    # Try inserting employees individually to find the exact error
    inserted_count = 0
    for emp in employees:
        try:
            await db.employees.insert_one(emp)
            inserted_count += 1
        except Exception as e:
            print(f"Failed to insert employee {emp['employee_code']}: {e}")
            if hasattr(e, 'details'):
                print(f"Details: {e.details}")
    
    print(f"Inserted {inserted_count} employees.")

    # Sales
    sales = [
        {
            "sale_date": datetime(2025, 1, 1),
            "region_id": ObjectId("65a000000000000000000001"),
            "employee_id": ObjectId("66b000000000000000000001"),
            "total_quantity": 3,
            "total_amount": 270000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000001"), "quantity": 1, "amount": 80000 },
                { "product_id": ObjectId("67c000000000000000000002"), "quantity": 1, "amount": 120000 },
                { "product_id": ObjectId("67c000000000000000000012"), "quantity": 1, "amount": 70000 }
            ],
            "created_at": datetime(2025, 1, 1)
        },
        {
            "sale_date": datetime(2025, 1, 3),
            "region_id": ObjectId("65a000000000000000000002"),
            "employee_id": ObjectId("66b000000000000000000006"),
            "total_quantity": 4,
            "total_amount": 325000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000004"), "quantity": 2, "amount": 150000 },
                { "product_id": ObjectId("67c000000000000000000009"), "quantity": 1, "amount": 105000 },
                { "product_id": ObjectId("67c000000000000000000018"), "quantity": 1, "amount": 70000 }
            ],
            "created_at": datetime(2025, 1, 3)
        },
        {
            "sale_date": datetime(2025, 1, 5),
            "region_id": ObjectId("65a000000000000000000003"),
            "employee_id": ObjectId("66b000000000000000000011"),
            "total_quantity": 5,
            "total_amount": 420000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000005"), "quantity": 2, "amount": 190000 },
                { "product_id": ObjectId("67c000000000000000000003"), "quantity": 1, "amount": 90000 },
                { "product_id": ObjectId("67c000000000000000000008"), "quantity": 1, "amount": 70000 },
                { "product_id": ObjectId("67c000000000000000000014"), "quantity": 1, "amount": 70000 }
            ],
            "created_at": datetime(2025, 1, 5)
        },
        {
            "sale_date": datetime(2025, 1, 7),
            "region_id": ObjectId("65a000000000000000000004"),
            "employee_id": ObjectId("66b000000000000000000016"),
            "total_quantity": 4,
            "total_amount": 335000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000015"), "quantity": 1, "amount": 130000 },
                { "product_id": ObjectId("67c000000000000000000010"), "quantity": 1, "amount": 65000 },
                { "product_id": ObjectId("67c000000000000000000019"), "quantity": 2, "amount": 140000 }
            ],
            "created_at": datetime(2025, 1, 7)
        },
        {
            "sale_date": datetime(2025, 1, 10),
            "region_id": ObjectId("65a000000000000000000001"),
            "employee_id": ObjectId("66b000000000000000000004"),
            "total_quantity": 6,
            "total_amount": 505000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000002"), "quantity": 2, "amount": 240000 },
                { "product_id": ObjectId("67c000000000000000000001"), "quantity": 2, "amount": 160000 },
                { "product_id": ObjectId("67c000000000000000000006"), "quantity": 2, "amount": 105000 }
            ],
            "created_at": datetime(2025, 1, 10)
        },
        {
            "sale_date": datetime(2025, 1, 12),
            "region_id": ObjectId("65a000000000000000000002"),
            "employee_id": ObjectId("66b000000000000000000009"),
            "total_quantity": 5,
            "total_amount": 420000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000011"), "quantity": 2, "amount": 230000 },
                { "product_id": ObjectId("67c000000000000000000004"), "quantity": 2, "amount": 150000 },
                { "product_id": ObjectId("67c000000000000000000018"), "quantity": 1, "amount": 40000 }
            ],
            "created_at": datetime(2025, 1, 12)
        },
        {
            "sale_date": datetime(2025, 1, 15),
            "region_id": ObjectId("65a000000000000000000003"),
            "employee_id": ObjectId("66b000000000000000000012"),
            "total_quantity": 4,
            "total_amount": 330000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000008"), "quantity": 2, "amount": 140000 },
                { "product_id": ObjectId("67c000000000000000000003"), "quantity": 1, "amount": 90000 },
                { "product_id": ObjectId("67c000000000000000000017"), "quantity": 1, "amount": 100000 }
            ],
            "created_at": datetime(2025, 1, 15)
        },
        {
            "sale_date": datetime(2025, 1, 18),
            "region_id": ObjectId("65a000000000000000000004"),
            "employee_id": ObjectId("66b000000000000000000017"),
            "total_quantity": 3,
            "total_amount": 290000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000020"), "quantity": 1, "amount": 125000 },
                { "product_id": ObjectId("67c000000000000000000009"), "quantity": 1, "amount": 105000 },
                { "product_id": ObjectId("67c000000000000000000013"), "quantity": 1, "amount": 60000 }
            ],
            "created_at": datetime(2025, 1, 18)
        },
        {
            "sale_date": datetime(2025, 1, 20),
            "region_id": ObjectId("65a000000000000000000001"),
            "employee_id": ObjectId("66b000000000000000000002"),
            "total_quantity": 4,
            "total_amount": 310000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000001"), "quantity": 1, "amount": 80000 },
                { "product_id": ObjectId("67c000000000000000000005"), "quantity": 1, "amount": 95000 },
                { "product_id": ObjectId("67c000000000000000000007"), "quantity": 1, "amount": 85000 },
                { "product_id": ObjectId("67c000000000000000000012"), "quantity": 1, "amount": 50000 }
            ],
            "created_at": datetime(2025, 1, 20)
        },
        {
            "sale_date": datetime(2025, 1, 22),
            "region_id": ObjectId("65a000000000000000000002"),
            "employee_id": ObjectId("66b000000000000000000003"),
            "total_quantity": 3,
            "total_amount": 260000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000002"), "quantity": 1, "amount": 120000 },
                { "product_id": ObjectId("67c000000000000000000004"), "quantity": 1, "amount": 75000 },
                { "product_id": ObjectId("67c000000000000000000018"), "quantity": 1, "amount": 65000 }
            ],
            "created_at": datetime(2025, 1, 22)
        },
        {
            "sale_date": datetime(2025, 1, 25),
            "region_id": ObjectId("65a000000000000000000003"),
            "employee_id": ObjectId("66b000000000000000000005"),
            "total_quantity": 5,
            "total_amount": 445000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000015"), "quantity": 2, "amount": 260000 },
                { "product_id": ObjectId("67c000000000000000000001"), "quantity": 1, "amount": 80000 },
                { "product_id": ObjectId("67c000000000000000000012"), "quantity": 2, "amount": 105000 }
            ],
            "created_at": datetime(2025, 1, 25)
        },
        {
            "sale_date": datetime(2025, 1, 28),
            "region_id": ObjectId("65a000000000000000000004"),
            "employee_id": ObjectId("66b000000000000000000008"),
            "total_quantity": 4,
            "total_amount": 350000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000011"), "quantity": 1, "amount": 115000 },
                { "product_id": ObjectId("67c000000000000000000009"), "quantity": 1, "amount": 105000 },
                { "product_id": ObjectId("67c000000000000000000004"), "quantity": 1, "amount": 75000 },
                { "product_id": ObjectId("67c000000000000000000013"), "quantity": 1, "amount": 55000 }
            ],
            "created_at": datetime(2025, 1, 28)
        },
        {
            "sale_date": datetime(2025, 2, 1),
            "region_id": ObjectId("65a000000000000000000001"),
            "employee_id": ObjectId("66b000000000000000000007"),
            "total_quantity": 3,
            "total_amount": 250000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000003"), "quantity": 1, "amount": 90000 },
                { "product_id": ObjectId("67c000000000000000000006"), "quantity": 1, "amount": 55000 },
                { "product_id": ObjectId("67c000000000000000000015"), "quantity": 1, "amount": 105000 }
            ],
            "created_at": datetime(2025, 2, 1)
        },
        {
            "sale_date": datetime(2025, 2, 3),
            "region_id": ObjectId("65a000000000000000000002"),
            "employee_id": ObjectId("66b000000000000000000010"),
            "total_quantity": 4,
            "total_amount": 340000,
            "product_breakdown": [
                { "product_id": ObjectId("67c000000000000000000016"), "quantity": 1, "amount": 90000 },
                { "product_id": ObjectId("67c000000000000000000011"), "quantity": 1, "amount": 115000 },
                { "product_id": ObjectId("67c000000000000000000004"), "quantity": 1, "amount": 75000 },
                { "product_id": ObjectId("67c000000000000000000017"), "quantity": 1, "amount": 60000 }
            ],
            "created_at": datetime(2025, 2, 3)
        }
    ]
    await db.sales.insert_many(sales)
    print(f"Inserted {len(sales)} sales.")

    await close_mongo_connection()
    print("Seeding completed.")

if __name__ == "__main__":
    asyncio.run(seed_data())
