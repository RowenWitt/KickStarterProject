import json
import pickle
import datetime

f = 'listKick.json'

# Getting id, blurb, state from listKick0.json 
def selectXY(imp):
	unid = imp['data']['id']
	launched = imp['data']['launched_at']
	deadline = imp['data']['deadline']
	timeline = (datetime.datetime.fromtimestamp(deadline) - datetime.datetime.fromtimestamp(launched)).days
	goal = imp['data']['goal']
	xrate = imp['data']['static_usd_rate']
	goalUSD = goal * xrate
	category = imp['data']['category']['slug']
	text = imp['data']['blurb']  # need to grab description not blurb
	state = imp['data']['state']

	row = [unid, timeline, goalUSD, category, text, state]
	return row

def viewJson(imp):  # Actually make into real function later
	print(json.dumps(a[0], indent=4))


XY = []
with open(f, 'r') as fp:
	raw = json.load(fp)
	for o in range(len(raw)):
		if(o % 10000 ==0 ):
			print('iteration {}/{} successful'.format(o, len(raw)))
		XY.append(selectXY(raw[o]))
		o += 1


with open('kickXY.pkl', 'wb') as p:
	pickle.dump(XY, p)