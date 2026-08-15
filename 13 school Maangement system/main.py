import json
from abc import ABC, abstractmethod
import pathlib as path

database = "school_data.json"

data = {
    "students": [],
    "teachers": [],}

if path(database).exists():
  with open(database, "r") as f:
    content = f.read()

    if content:
      data = json.loads(content)


class Person(ABcC):

  @abstractmethod
  def get_roles(self):
    pass


  @abstractmethod
  def register(self):
    pass

  @abstractmethod
  def view_details(self):
    pass

  @staticmethod
  def validate_email(email):
     if "@" in email and "." in email:
        return True
     else:
        return False


