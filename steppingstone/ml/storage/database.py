from pymongo import MongoClient


class Storage(object):

    def __init__(self, dbname):
        self.hostname = 'localhost'
        #self.weights = 'tag-weights'
        self.port = '27017'

    def createDB(self):
        client = MongoClient('{}:{}'.format(self.hostname, self.port))
        db = client[self.dbname]
        return db

    def put_all(self, db, coll, cdict):
        coll = db.coll
        return coll.insert_one(cdict)

    def get_one(self, conn, sdict):
        return conn.find_one(sdict)
