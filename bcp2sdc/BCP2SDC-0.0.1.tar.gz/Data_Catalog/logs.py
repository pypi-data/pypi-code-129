import logging
from datetime import datetime
from pydoc import doc
import pymongo




date = datetime.now().strftime("%d_%m_%Y")
now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

logging.basicConfig(filename=f"C://Users//hp//Documents//Logs//log_{date}",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p'
                    )

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

conn = pymongo.MongoClient("mongodb://localhost:27017")
#Accessing the DB
mydb = conn['Data_Catalog']
mycol = mydb["Logs"]

def debug(msg):
    logger.debug(msg)
    doc={
            "Evénement":msg,
            "Type de l'événement":"DEBUG",
            "Date et heure":now
            
        }
    mycol.insert_one(doc)
    
    
def info(msg):
    logger.info(msg)
    doc={
            "Evénement":msg,
            "Type de l'événement":"INFO",
            "Date et heure":now
            
        }
    mycol.insert_one(doc)

def warning(msg):
    logger.warning(msg)
    doc={
            "Evénement":msg,
            "Type de l'événement":"WARNING",
            "Date et heure":now
            
        }
    mycol.insert_one(doc)

def error(msg):
    logger.error(msg)
    doc={
            "Evénement":msg,
            "Type de l'événement":"ERROR",
            "Date et heure":now
            
        }
    mycol.insert_one(doc)

def critical(msg):
    logger.critical(msg)
    doc={
            "Evénement":msg,
            "Type de l'événement":"CRITICAL",
            "Date et heure":now
            
        }
    mycol.insert_one(doc)

