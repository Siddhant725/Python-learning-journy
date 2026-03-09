import json
data_from_internet='{"name":"Siddhant","hours":42,"rate":30}'
user_dict=json.loads(data_from_internet)

print(f"data processed for {user_dict['name']}: Total${user_dict['hours'] * user_dict['rate']}")