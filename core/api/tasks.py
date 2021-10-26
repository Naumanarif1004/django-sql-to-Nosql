from celery import shared_task
import collections
from pymongo import MongoClient
from django.conf import settings as c

@shared_task
def ConvertDBRowsToJson(rows,colnames,db_name):
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        for col in range(len(colnames)):
            if colnames[col] == 'id':
                d["_id"] = row[col]
            else:
                d[colnames[col]] = row[col]
        objects_list.append(d)

    #store data in a document-oriented form in mongodb
    client = MongoClient(c.MONGO_CREDENTIALS)
    db = client[db_name]
    coll_name = "{}_collection".format(db_name)
    collection = db[coll_name]
    collection.insert_many(objects_list)
    client.close()
