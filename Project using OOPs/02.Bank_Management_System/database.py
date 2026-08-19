import json
from pathlib import Path

database = Path(__file__).parent/"data"/"bank_data.json"

data = {
  "Customers":[],
  "Accounts": [],
  "Transactions":[]
}

def save_data(data):

  with open(database,"w") as f:
    json.dump(data, f, indent=4)


def load_data():

  if database.exists():
    with open(database, "r") as f:
      data = json.load(f)

      return data

  return {
    "Customers":[],
    "Accounts":[],
    "Transactions":[]
  }