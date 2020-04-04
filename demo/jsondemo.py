import json

conf='{"scheduleConf":[{"index":1,"type":0},{"index":2,"type":0},{"index":3,"type":0},{"index":5,"type":1},{"index":6,"type":1},{"index":7,"type":1},{"index":8,"type":1},{"index":9,"type":2},{"index":9,"type":2}],"stageConf":[{"stage":1,"trainCampId":187},{"stage":2,"trainCampId":188},{"stage":3,"trainCampId":189}]}'

conf_js = json.loads(conf)

print(conf)
print(conf_js)
print(json.dumps(conf_js.get('scheduleConf')))
print(json.dumps(conf_js.get('scheduleConf'), separators=(',', ':')))

for c in conf_js.get('stageConf'):
    print(c)
    if 'trainCampId' in c:
        print(c.get('stage'),c.get('trainCampId'))