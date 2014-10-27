from pyslideshare2 import pyslideshare
import pprint
import json
import os
from sets import Set

def read_config():
    config_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(config_path, 'config.json'), 'r') as f:
        return json.load(f)

def process_slideshow(slideshow, tags):
    cnt = 0
    for tag in slideshow['Tags']['Tag']:
        tags.add(tag['value'])
        cnt += 1
    print "=== added %d new tags.." % cnt

pp = None
config = read_config()
limit_per_tag = 2
tags_limit = 2
api = pyslideshare.pyslideshare(config, verbose=True)
slideshow = api.get_slideshow_by_url(config['init_url'], detailed=1)
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(slideshow)
tags = Set()
for tag in slideshow['Slideshow']['Tags']['Tag']:
    tags.add(tag['value'])

it = 0
while tags:
    tag = tags.pop()
    print "=== processing tag: %s" % tag
    response = api.get_slideshows_by_tag(tag=tag, limit=limit_per_tag, detailed=1)
    for slideshow in response['Tag']['Slideshow']:
        pp = pprint.PrettyPrinter(indent=4)
        process_slideshow(slideshow, tags)
    if it == tags_limit:
        break
    else:
        it = it + 1



