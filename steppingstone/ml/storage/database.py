from pymongo import MongoClient


class Storage(object):

    def __init__(self, dbname):
        self.hostname = 'localhost'
        self.dbname = dbname
        self.port = '27017'

    def put_all(self, coll, cdict_list):
        client = MongoClient('{}:{}'.format(self.hostname, self.port))
        db = client[self.dbname]
        coll = db.coll
        return coll.insert_many(cdict_list)

    def get_one(self, coll, sdict):
        client = MongoClient('{}:{}'.format(self.hostname, self.port))
        db = client[self.dbname]
        coll = db.coll
        result = coll.find_one(sdict)
        return result

