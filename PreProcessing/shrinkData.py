import json


f = 'listKick.json'

def process_Smallest(imp):
    del imp['data']['slug']
    del imp['data']['country']
    del imp['data']['staff_pick']
    del imp['data']['is_starrable']
    del imp['data']['country_displayable_name']
    del imp['data']['currency_symbol']

    if 'slug' in imp['data']['creator'].keys():
        del imp['data']['creator']['slug']
    del imp['data']['creator']['id']
    del imp['data']['creator']['is_registered']
    if 'is_email_verified' in imp['data']['creator'].keys():
        del imp['data']['creator']['is_email_verified']
    del imp['data']['creator']['chosen_currency']
    del imp['data']['creator']['is_superbacker']

    if 'background_image_attributes' in imp['data']['profile'].keys():
        del imp['data']['profile']['background_image_attributes']

    return imp

data = []
with open(f, 'r') as fp:
    raw = json.load(fp)
    for o in range(len(raw)):
        if(o % 10000 == 0):
            print('iteration {} successful'.format(o))

        data.append(process_Smallest(raw[o]))

with open('listKick0.json', 'w') as fp:
    json.dump(data, fp)