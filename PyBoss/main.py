# main.py for PyBoss

import csv

csvpath1 = 'employee_data1.csv'
#csvpath2 = 'employee_data2.csv'

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

with open(csvpath1, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:

        employee_id.append(row[0])

        name = row[1].split(" ")
        first_name = name.append(name[0])
        last_name = name.append(name[1])

        new_dob = row[2].split("-")
        dob.append(new_dob[1]+"/"+new_dob[2]+"/"+new_dob[0]

        new_ssn = row[3].split("-")
        ssn.append("***-**"+new_ssn[2])

        state = us_state_abbrev[row[4]]

cleaned_csv = zip(employee_id, first_name, last_name, dob, ssn, state)
print(cleaned_csv)


#make this work for 2 files... and keep going. And copy in the csv files to local directory

#look at web_solved.py?

#TODO: export to csv


