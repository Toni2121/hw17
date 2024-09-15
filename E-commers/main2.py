import sqlite_lib2

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT COUNT(*)
        FROM ecomm e
''')
customer_count = answer[0][0]
print(f"Amount of customers: {customer_count}")

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT AVG(e.age)
        FROM ecomm e
''')
customer_count = answer[0][0]
print(f"Average age of Customers: {customer_count}")

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT COUNT(*)
        FROM ecomm e
    WHERE gender LIKE "male"
''')
customer_count = answer[0][0]
print(f"Male Customers: {customer_count}")

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT COUNT(*)
        FROM ecomm e
    WHERE gender LIKE "female"
''')
customer_count = answer[0][0]
print(f"Female Customers: {customer_count}")

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT AVG("items purchased")
        FROM ecomm e
    WHERE gender LIKE "male"
''')
customer_count = answer[0][0]
print(f"Male average items per order: {customer_count}")

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT AVG("items purchased")
        FROM ecomm e
    WHERE gender LIKE "female"
''')
customer_count = answer[0][0]
print(f"Female average items per order: {customer_count}")

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT COUNT(DISTINCT "membership type")
        FROM ecomm e
''')
customer_count = answer[0][0]
print(f"Membership types: {customer_count}")

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT COUNT(city)
        FROM ecomm e
    WHERE city LIKE "New York"
''')
customer_count = answer[0][0]
print(f"Amount of customers from NY: {customer_count}")

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT City, COUNT(*)
        FROM ecomm
    GROUP BY City
    ORDER BY COUNT(*) DESC
''')
for row in answer:
    city, count = row
    print(f"Number of customers in {city}: {count}")

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT "total spend"
        FROM ecomm e
    WHERE gender LIKE "Male"
''')
total = 0
for i in answer:
    total += i[0]
print(f"Male total spend: {total}")

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT "total spend"
        FROM ecomm e
    WHERE gender LIKE "Female"
''')
total = 0
for i in answer:
    total += i[0]
print(f"Female total spend: {total}")

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT "customer id"
        FROM ecomm e
    ORDER BY "items purchased" DESC
    LIMIT 3
''')
print(f"Customers who purchased the most items: {answer}")

sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
answer = sqlite_lib2.run_query_select('''
    SELECT "customer id"
        FROM ecomm e
    ORDER BY "items purchased"
    LIMIT 3
''')
print(f"Customers who purchased the least items: {answer}")


def members_count():
    sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
    gold = sqlite_lib2.run_query_select('''
        SELECT count(*)
            FROM ecomm e
        WHERE "membership type" LIKE "gold"
    ''')

    sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
    silver = sqlite_lib2.run_query_select('''
            SELECT count(*)
                FROM ecomm e
            WHERE "membership type" LIKE "silver"
        ''')

    sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')
    bronze = sqlite_lib2.run_query_select('''
            SELECT count(*)
                FROM ecomm e
            WHERE "membership type" LIKE "bronze"
        ''')
    if membership_type.lower() == "gold":
        return gold[0][0]
    if membership_type.lower() == "silver":
        return silver[0][0]
    if membership_type.lower() == "bronze":
        return bronze[0][0]


membership_type = input("please enter the desired membership type: ")
print(members_count())
members_count()
