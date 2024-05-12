import json

def export_to_csv():
  with open("/Users/deepakdas/InterviewKickStart/InterviewKickStart-1/utilities/data.json") as f:
    list1 = []
    data = json.loads(f.read())
    temp = data[0]
    header_items = []
    list1.append(get_headers(temp, header_items))
    #print(list1)
    for record in data:
      linedata = []
      extract_data(record, linedata)
      list1.append(linedata)
  import csv
  with open('/Users/deepakdas/InterviewKickStart/InterviewKickStart-1/utilities/output1.csv', 'w') as output_file:
    writer = csv.writer(output_file)
    for line in list1:
      writer.writerow(line)
      




def get_headers(temp,header_items):
  for val in temp:
      if isinstance(temp[val], dict):
        header_items.append(val)
        get_headers(temp[val],header_items)
      else:
        header_items.append(val)
  return header_items

def extract_data(obj,currentdata):
  for val in obj:
      if isinstance(obj[val], dict):
        currentdata.append("")
        extract_data(obj[val],currentdata)
      else:
        currentdata.append(obj[val])
  return currentdata

export_to_csv()