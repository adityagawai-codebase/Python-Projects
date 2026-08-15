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


