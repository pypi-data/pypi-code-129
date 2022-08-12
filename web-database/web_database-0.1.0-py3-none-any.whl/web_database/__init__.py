__version__ = '0.1.0'

import json
import os
from os import listdir
from os.path import isfile
  
def getFiles():
  return [f for f in listdir() if isfile(f)]

def read_db(db):
    # Opening JSON file
    with open(db, 'r') as openfile:

        # Reading from json file
        return json.loads(openfile.read())


def write_db(db, dictionary):
    # Serializing json
    json_object = json.dumps(dictionary, indent=len(dictionary.keys()))

    # Writing to sample.json
    with open(db, 'w') as outfile:
        outfile.write(json_object)


def create_db(name):
    try:
        with open(name + ".json", 'x', encoding='utf-8') as f:
            write_db(name + ".json", {
              
            })
    except:
        raise Exception("This database allready exists.")


class DB:
    def __init__(self, database):
        if database + ".json" not in getFiles():
            raise Exception(
                "This database doesn't exist. Use create_db to create a database."
            )
        self.database = database + ".json"

    def change_db(self, new_db):
        self.database = new_db + ".json"

    def write(self, key, value):
        current = self.read()
        current[key] = value
        write_db(self.database, current)

    def read(self):
        return read_db(self.database)

    def remove(self, key):
        content = self.read()
        try:
            del content[key]
        except:
            raise Exception("Nonexistent key.")
        write_db(self.database, content)

    def delete(self):
        os.remove(self.database)
        self.database = ""