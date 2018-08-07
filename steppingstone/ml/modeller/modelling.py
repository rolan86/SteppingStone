import json

from steppingstone import conf
from steppingstone.ml.storage.database import Storage


class Modeller(object):

    def get_tags(self):
        with open('../data/quotes.json') as js:
            data = json.loads(js.read())
            return list(
                set([item for sublist in data for item in sublist['tags']])
            )

    def add_weights(self):
        all_tags = self.get_tags()
        weighted_tags = {}
        only_tags = {}
        weighted_tags_list = []
        for tag in all_tags:
            entry = input("Enter weight between 0 - 5 for {} ".format(tag))
            if not isinstance(entry, int):
                done = raw_input("Are you done adding weights? y/n ")
                if done == 'y':
                    break
            if not only_tags.get(tag):
                weighted_tags = {}
                only_tags[tag] = entry
                weighted_tags['tag'] = tag
                weighted_tags['weight'] = entry
                weighted_tags_list.append(weighted_tags)
        with open('../data/weights.json', 'w') as js:
            data = js.write(json.dumps(weighted_tags_list))
        storage = Storage('tag-weights')
        storage.put_all('weights', weighted_tags_list)

    def get_weights(self, tag_dict):
        storage = Storage('tag-weights')
        result = storage.get_one('weights', tag_dict)
        return result.get('weight')
