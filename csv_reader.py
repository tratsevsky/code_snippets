#################################
## CSV Module
## Readind CSV Files
#################################

###CSV File - (airtravel.csv) - attached to this lecture
# "Month", "1958", "1959", "1960"
# "JAN",  340,  360,  417
# "FEB",  318,  342,  391
# "MAR",  362,  406,  419
# "APR",  348,  396,  461
# "MAY",  363,  420,  472
# "JUN",  435,  472,  535
# "JUL",  491,  548,  622
# "AUG",  505,  559,  606
# "SEP",  404,  463,  508
# "OCT",  359,  407,  461
# "NOV",  310,  362,  390
# "DEC",  337,  405,  432

import csv

with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    year_1958 = dict()
    for row in reader:
        year_1958[row[0]] = row[1]

    # print(year_1958)

    max_1958 = max(year_1958.values())

    # print(max_1958)

    for k, v in year_1958.items():
        if max_1958 == v:
            print(f'Busiest month in 1958:{k}, Flights:{v.strip()}')

print(csv.list_dialects())
