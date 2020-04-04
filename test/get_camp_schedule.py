import json

str = '{"courseId":720,"scheduleConf":[{"index":1,"type":0},{"index":2,"type":0},{"index":3,"type":0},{"index":6,"type":1},{"index":7,"type":1},{"index":8,"type":1},{"index":9,"type":1},{"index":10,"type":2},{"index":10,"type":2}],"stageConf":[{"newTrainCampId":334,"stage":1,"trainCampId":293},{"newTrainCampId":335,"stage":2,"trainCampId":294},{"newTrainCampId":336,"stage":3,"trainCampId":295}]}'

str_json = json.loads(str)
max_index = max([x['index'] for x in str_json['scheduleConf']])
print(max_index)

type_schedule = {}
print(str_json['scheduleConf'])
for x in str_json['scheduleConf']:
    print(x['type'], x['index'])
    type_schedule.setdefault(x['type'], [x['index']])
    type_schedule[x['type']].append(x['index'])

print(type_schedule)
