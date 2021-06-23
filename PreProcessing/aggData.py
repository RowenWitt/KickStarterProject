import json

files = ['listKick1.json', 'listKick2.json', 'listKick3.json']

def process_Smaller(imp):
    if 'location' in imp['data'].keys():
        del imp['data']['location']['id']
        del imp['data']['location']['name']
        del imp['data']['location']['slug']
        del imp['data']['location']['displayable_name']
        del imp['data']['location']['localized_name']
        del imp['data']['location']['state']
        del imp['data']['location']['is_root']
        del imp['data']['location']['expanded_country']
    del imp['data']['category']['name']
    if 'analytics_name' in imp['data']['category'].keys():
        del imp['data']['category']['analytics_name']
    del imp['data']['category']['position']
    if 'parent_id' in imp['data']['category'].keys():
        del imp['data']['category']['parent_id']
    if 'parent_name' in imp['data']['category'].keys():
        del imp['data']['category']['parent_name']
    del imp['data']['profile']['id']
    del imp['data']['profile']['project_id']
    del imp['data']['profile']['name']
    del imp['data']['profile']['blurb']
    del imp['data']['profile']['background_color']
    del imp['data']['profile']['text_color']
    del imp['data']['profile']['link_background_color']
    del imp['data']['profile']['link_text_color']
    del imp['data']['profile']['link_text']
    del imp['data']['profile']['link_url']
    del imp['data']['spotlight']

    return imp

data = []
for f in files:
    print(f'file {f}')
    with open(f, 'r') as fp:
        o = 0
        for lines in json.load(fp):
            o += 1
            if(o % 10000 == 0):
                print(f'iteration {o} successful')
            data.append(process_Smaller(lines))

with open('listKick.json', 'w') as fp:
    json.dump(data, fp)