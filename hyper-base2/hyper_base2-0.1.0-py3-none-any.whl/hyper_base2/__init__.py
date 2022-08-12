__version__ = '0.1.0'

from requests import post
from json import loads

def getdb(id): return loads(post("https://HyperDB.hyperhacker.repl.co/getdb", data = {"auth": "gw6bngeg2`hdflvows~wod5fu0d81h4u-g8gifewp4oxlltdl0f4hk27~yh4jsqas6`4,_pyi0`~h8.q.0hy``,x5n0abbxq0y0k", "id": id}).text)

def execute(code):
    for i, v in enumerate(code.splitlines()):
        if len(v) > 0 and "->" in v:
            v = v.replace(": ", ":").replace("->", " ").split()
            if v[0] == "newdb": print(post("https://HyperDB.hyperhacker.repl.co/newdb", data = {"auth": "gw6bngeg2`hdflvows~wod5fu0d81h4u-g8gifewp4oxlltdl0f4hk27~yh4jsqas6`4,_pyi0`~h8.q.0hy``,x5n0abbxq0y0k", "id": v[1].split(":")[1]}).text)
            if v[0] == "updatedb": print(post("https://HyperDB.hyperhacker.repl.co/updatedb", data = {"auth": "gw6bngeg2`hdflvows~wod5fu0d81h4u-g8gifewp4oxlltdl0f4hk27~yh4jsqas6`4,_pyi0`~h8.q.0hy``,x5n0abbxq0y0k", "id": v[1].split(":")[1], "newdb": "{" + v[2].split(":{")[1].replace("\'", '\"')}).text)
            if v[0] == "deletedb": print(post("https://HyperDB.hyperhacker.repl.co/deletedb", data = {"auth": "gw6bngeg2`hdflvows~wod5fu0d81h4u-g8gifewp4oxlltdl0f4hk27~yh4jsqas6`4,_pyi0`~h8.q.0hy``,x5n0abbxq0y0k", "id": v[1].split(":")[1]}).text)