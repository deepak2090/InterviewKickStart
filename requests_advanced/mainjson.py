import json

# Specify the relative file path to data.json
file_path = "/Users/deepakdas/InterviewKickStart/InterviewKickStart-1/requests_advanced/data.json"

# Open the file and load its contents
with open(file_path, "r") as json_file:
    data = json.load(json_file)

# Access the JSON data
print(data)
