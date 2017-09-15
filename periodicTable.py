import json

#pt_json = open('PeriodicTable.json', 'r')
#pt = json.load(pt_json)

#new_pt = {}

#for key in pt['elements']:
#    new_pt[key['symbol']] = key

#with open('newPeriodicTable.json', 'w') as fp:
#    json.dump(new_pt, fp)
    
pt_json2 = open('newPeriodicTable.json', 'r')
pt2 = json.load(pt_json2)

print(pt2['As'])
