import json


class Modeller(object):

    def get_tags(self):
        with open('../../../quotes.json') as js:
            data = json.loads(js.read())
            return list(
                set([item for sublist in data for item in sublist['tags']])
            )

    def add_weights(self):
        pass
