import json
data = {"name" : "Alice", "age" : 30 , "city" : "kampala" }

json_string = json.dumps(data)

with open("data.json", "w") as file:
    json.dump(data, file)
    