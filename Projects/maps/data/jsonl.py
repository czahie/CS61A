"""A wrapper around Python's json module to parse newline-delimited json.

>>> all_reviews = load(open('reviews.json'))
>>> dump(all_reviews, open('reviews_copy.json', 'w'))
>>> all_reviews == load(open('reviews_copy.json'))
True
"""

from json import loads, dumps

def load(fp, **kw):
    return [loads(obj, **kw) for obj in fp]

def dump(objs, fp, **kw):
    for obj in objs:
        fp.write(dumps(obj, **kw))
        fp.write('\n')
