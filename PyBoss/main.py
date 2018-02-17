# main.py for PyBoss

import csv
import os

#Need to update csv file name below, which I don't consider a "major re-write".
emp_data_csv = 'employee_data2.csv'

cleaned_emp_data_csv = os.path.join('cleaned_' + emp_data_csv)

employee_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(emp_data_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip headers
    next(csvreader)

    for row in csvreader:

        employee_id.append(row[0])

        name = row[1].split(" ")
        first_name.append(name[0])
        last_name.append(name[1])

        split_dob = row[2].split("-")
        dob.append(split_dob[1] + "/" + split_dob[2] + "/" + split_dob[0])

        new_ssn = row[3].split("-")
        ssn.append("***-**-"+new_ssn[2])

        abbrev = us_state_abbrev[row[4]]
        state.append(abbrev)
       
cleaned_data = zip(employee_id, first_name, last_name, dob, ssn, state)

with open(cleaned_emp_data_csv, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    
    for row in cleaned_data:
        csvwriter.writerow(row)