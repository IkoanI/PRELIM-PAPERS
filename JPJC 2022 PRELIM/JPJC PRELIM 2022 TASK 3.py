#Task 3.1
import pymongo, json
client = pymongo.MongoClient("localhost", 27017)
db = client.get_database("StyleTheory")
db.drop_collection("Rental")
coll = db.get_collection("Rental")

with open("RENTAL.JSON") as f:
    data = json.load(f)
    coll.insert_many(data)

#Task 3.2
while(True):
    print("Style Theory")
    print("Option 1 – Insert new rental")
    print("Option 2 – Update existing rental")
    print("Option 3 – Quit")
    option = input("Enter your option (1, 2, or 3): ")

    if option == '1':
        catalogueNumber = int(input("Enter catalogue number: "))
        brand = input("Enter brand: ")
        category = input("Enter category: ")
        rental = int(input("Enter rental fee: "))
        email = input("Enter customer's email: ")
        startDate = input("Enter start date: ")
        endDate = input("Enter end date: ")

        if category.lower() == 'apparel':
            size = int(input("Enter size: "))
            coll.insert_one({'catalogueNumber': catalogueNumber, \
                             'brand': brand, \
                             'category': category.lower(), \
                             'rental': rental, \
                             'size': size, \
                             'email': email, \
                             'startDate': startDate, \
                             'endDate': endDate})

        elif category.lower() == 'bag':
            coll.insert_one({'catalogueNumber': catalogueNumber, \
                             'brand': brand, \
                             'category': category.lower(), \
                             'rental': rental, \
                             'email': email, \
                             'startDate': startDate, \
                             'endDate': endDate})
            

    elif option == '2':
        catalogueNumber = int(input("Enter catalogue number: "))
        startDate = input("Enter start date: ")
        endDate = input("Enter new end date: ")
        query = {"$and" : [{"catalogueNumber" : catalogueNumber}, {'startDate': startDate}]}
        newValue = {"$set" : {"endDate": endDate}}
        coll.update_one(query, newValue)

    elif option == "3":
        break

    else:
        print("Invalid input, please try again")


#Task 3.3
from datetime import date
def display_all(coll):
    result = coll.find()
    print("Catalogue Number | Brand | Category | Rental Fee | Size | " + \
          "Customer Email | Start Date | End Date | Total Amount Payable")
    for item in result:
        catalogueNumber = item["catalogueNumber"]
        brand = item["brand"]
        category = item["category"]
        rental = item["rental"]
        size = "NA"
        if category == "apparel":
            size = item["size"]
        email = item["email"]
        startDate = item["startDate"]
        endDate = item["endDate"]
        f_date = date(int(startDate[:4]), int(startDate[5:7]), int(startDate[8:10]))
        l_date = date(int(endDate[:4]), int(endDate[5:7]), int(endDate[8:10]))
        delta = l_date - f_date
        daysRented = delta.days
        amtPayable = rental * daysRented
        print(f"{catalogueNumber} {brand} {category} {rental} {size} {email} {startDate} {endDate} {amtPayable}")

display_all(coll)   
client.close()

        
