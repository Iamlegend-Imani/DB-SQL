import sqlite3
# Connecting to our database


def connectiontodb(db_name='../northwind_small.sqlite3'):
    conn = sqlite3.connect(db_name)
    return conn
# Executing our read queries


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

'''
Queries
'''
'''
PART 2
'''
# What are the ten most expensive items (per unit price) in the database?
# SELECT ProductName
expensive_items = '''
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
'''
# What is the average age of an employee at the time of their hiring?
avg_hire_age = '''
SELECT AVG(HireDate - BirthDate) AS INTEGER
FROM Employee;
'''
# How does the average age of employee at hire vary by city?
avg_age_by_city = '''
SELECT AVG(HireDate - BirthDate) AS INTEGER, City
FROM Employee GROUP BY City;
'''
'''
PART 3
'''
# What are the ten most expensive items in the database and their suppliers?
# SELECT ProductName, CompanyName
ten_most_expensive = '''
SELECT
ProductName AS Products,
UnitPrice AS Price,
CompanyName As Company
FROM Product
JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;
'''
# What is the largest category (by number of unique products in it)?
largest_category = '''
SELECT CategoryName,
COUNT(CategoryId) AS CategoryId
FROM Product
Join Category
ON Product.CategoryId = Category.Id
GROUP BY CategoryId
Order BY CategoryId DESC
LIMIT 1;
'''
# Who's the employee with the most territories?
most_territories = '''
SELECT
LastName,
FirstName,
COUNT(EmployeeId) AS "Territories"
FROM Employee
JOIN EmployeeTerritory
ON Employee.Id = EmployeeTerritory.EmployeeId
GROUP BY EmployeeId
ORDER BY Territories DESC
LIMIT 1
'''
# Fetching outputs for ease of grading
if __name__ == "__main__":
    conn = connectiontodb()
    curse = conn.cursor()
    ten_items = execute_query(curse, expensive_items)
    print('Ten Most Expensive Items: ', ten_items)
    age_hiring = execute_query(curse, avg_hire_age)
    print('Average Age of Employee at Hiring: ', age_hiring)
    age_city = execute_query(curse, avg_age_by_city)
    print('Average Age Employee Hire by City: ', age_city)
    items_supplier = execute_query(curse, ten_most_expensive)
    print('Ten Most Expensive Items & Suppliers: ', items_supplier)
    large_cat = execute_query(curse, largest_category)
    print('Largest Category by Number of Unique Products: ', large_cat)
    most_terr = execute_query(curse, most_territories)
    print('Employee with most Territory: ', most_terr)
