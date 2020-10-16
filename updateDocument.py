# Method prompts user-input to identify business ID in MongoDB database "city" 
# in the collection "inspections".  User is then prompted to select which value of 
# the document to modify and update in the database. 

import json 
from bson import json_util
from pymongo import MongoClient

#Connect to MongoClient, database and collection
client = MongoClient('localhost', 27017)
db = client.city
coll = db['inspections']

#Method to update a document in MongoDB
def update_one():
    try: 
        businessID = input('Enter business ID without quotation marks: ')
        
        
        db.inspections.find_one(
                {
                    "id" : businessID ,
                   
                }
            )
        print("\nBusiness found successfully!")
        print(coll.find_one({"id": businessID}))
        
        user_input = input('\nChoose the numbered attribute to update: 1. ID, 2. Business Name, 3. Inspection Date,4. Inspection Result ')
        
        # elif statement to update attribute per user request
        if user_input == 1:
          newID = input('Please enter new business ID: ')
          
          db.inspections.insert({"id" : newID})
          
          print("Business ID has been updated!")
          
        elif user_input == 2: 
          newName = input('Please enter new business name in quotation marks: ')
          
          db.inspections.insert({"business_name" : newName})
          
          print("Business name has been updated!")
          
        elif user_input == 3: 
          newDate = input('Please enter new inspection date in quotation marks: ')
          
          db.inspections.insert({"date" : newDate})
          
          print("Inspection date has been updated!")
          
        elif user_input == 4: 
          newResult = input('Please enter new inspection result in quotation marks: ')
          
          db.inspections.insert({"result" : newResult})
          
          print("Inspection result has been updated!")
          
        else: 
          print("Please select options 1-4, please try again.")
        
        
    except Exception as exception:
        print("Exception: {}".format(type(exception).__name__))
        print("Exception message: Use quotation marks and/or check spelling.")
        
update_one()
