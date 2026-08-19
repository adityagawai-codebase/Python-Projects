import json
from pathlib import Path

#Locaion for JSON database
database = Path(__file__).parent / "data" / "Bank_data.json"

#create data folder if doesn't exist 
database.parent.mkdir(parents=True, exist_ok=True)

def save_data(data):

  #save python dictionary into JSON file
  with open(database, "w") as f:
    json.dump(data, f, indent=4)

def load_data():

  #check wheather database file exits
  if database.exists():

    with open(database, "r") as f:
      content = f.read()

    #If file empty
    if not content.strip():
      return{
         "customers": [],
          "accounts": [],
          "transactions": []
      }

    #Convert JSON data into python dictionary
    return json.loads(content)

  # If database doesn't exist
  return {
        "customers": [],
        "accounts": [],
        "transactions": []
    }