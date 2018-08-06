import json

#from steppingstone import conf
from steppingstone.ml.storage.database import Storage


class Modeller(object):

    def get_tags(self):
        with open('../../../quotes.json') as js:
            data = json.loads(js.read())
            return list(
                set([item for sublist in data for item in sublist['tags']])
            )

    def add_weights(self):
        all_tags = self.get_tags()
        weighted_tags = {}
        for tag in all_tags:
            entry = input("Enter weight between 0 - 5 for {} ".format(tag))
            if not isinstance(entry, int):
                done = raw_input("Are you done adding weights? y/n")
                if done == 'y':
                    break
            if not weighted_tags.get(tag):
                weighted_tags[tag] = entry
        with open('../../../weights.json', 'w') as js:
            data = js.write(json.dumps(weighted_tags))

