from pyslideshare2 import pyslideshare
import pprint
import json
import os

def read_config():
    config_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(config_path, 'config.json'), 'r') as f:
        return json.load(f)


config = read_config()
api = pyslideshare.pyslideshare(config, verbose=True)
slideshow = api.get_slideshow_by_url(config['init_url'])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(slideshow)


