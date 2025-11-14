'''
# writing to CSV


import csv
	
# field names
FC=int(input("DO you want to use the default(AE PLUGINS) or create new fields?")or 0)
if FC==0:
    fields = ['Name', 'Issue', 'record', 'comment',' ']

	
# data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'],
		['Sanchit', 'COE', '2', '9.1'],
		['Aditya', 'IT', '2', '9.3'],
		['Sagar', 'SE', '1', '9.5'],
		['Prateek', 'MCE', '3', '7.8'],
		['Sahil', 'EP', '2', '9.1']]
	
# name of csv file
filename = "university_records.csv"
	
# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
		
	# writing the fields
	csvwriter.writerow(fields)
		
	# writing the data rows
	csvwriter.writerows(rows)
'''


import csv

# default AE plugin CSV fields
fields = ['Plugin Name', 'Issue', 'Version', 'Comment']

rows = []

print("Enter AE plugin records. Type 'q' at any time to stop.\n")

while True:
    name = input("Plugin Name: ")
    if name.lower() == 'q':
        break

    issue = input("Issue (e.g. Missing, Outdated): ")
    version = input("Version: ")
    comment = input("Comment: ")

    rows.append([name, issue, version, comment])
    print("Record added.\n")

filename = "ae_plugins.csv"

with open(filename, "w", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields)
    csv_writer.writerows(rows)

print("CSV file created:", filename)
