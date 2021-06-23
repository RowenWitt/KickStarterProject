# import pandas as pd
# import numpy as np
import json, jsonlines
from os import listdir
from os.path import isfile, join


def iter_dir(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

base_path = 'Data/Kickstarter'
files = iter_dir(base_path)

def process_obj(obj):
    del obj['table_id']
    del obj['robot_id']
    del obj['data']['photo']
    del obj['data']['disable_communication']
    del obj['data']['currency_trailing_code']
    del obj['data']['creator']['avatar']
    del obj['data']['creator']['urls']
    if('location' in obj['data'].keys()):
        del obj['data']['location']['urls']
    del obj['data']['category']['color']
    del obj['data']['category']['urls']
    del obj['data']['profile']['show_feature_image']
    del obj['data']['profile']['background_image_opacity']
    del obj['data']['profile']['should_show_feature_image_section']
    del obj['data']['profile']['feature_image_attributes']
    del obj['data']['urls']
    del obj['data']['source_url']

    return obj


# @TODO: load multiline json the correct way
# see https://stackoverflow.com/a/34463368/15697805pip
box = []
for i in range(len(files)):
    file = files[i]
    print('{}/{}'.format(i+1, len(files)))
    with jsonlines.open(join(base_path, file)) as f:
        t = 0
        for i in f:
            t += 1
            if(t % 10000 == 0):
                print(f'iteration {t} successful') 
            box.append(process_obj(i))

with open('listKick.json', 'w') as fp:
    json.dump(box, fp)


