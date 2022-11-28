import csv
#from lib2to3.pgen2.token import NEWLINE

"""
with open('usa_cities.csv', 'r') as file:
    csv_data = csv.reader(file)     
    print(csv_data)
    next(csv_data)
#    for row in csv_data:
#      print(row)
    
    with open('usa_cities_new.csv', 'w',newline='') as new_file:
        usa_cities_writer = csv.writer(new_file,delimiter='\t')
        print(usa_cities_writer)
        print(type(usa_cities_writer))
        for row in csv_data:
            usa_cities_writer.writerow(row)
"""

## DictWriter Method
with open('usa_cities.csv', 'r') as file:
    csv_data = csv.DictReader(file)
    
    with open('usa_cities_new_dict.csv', 'w',newline='') as new_file:
        #fieldnames = ['LatD','LatM', 'LatS', 'NS', 'LonD','LonM', 'LonS', 'EW', 'City', 'State']
        fieldnames = {'LatD':'LatD_new',
        'LatM':'LatM_new', 
        'LatS':'LatS_new', 
        'NS':'NS_new', 
        'LonD':'LonD_new',
        'LonM':'LonM_new', 
        'LonS':'LonS_new', 
        'EW':'EW_new', 
        'City':'City_new', 
        'State':'State_new'}
        
        usa_cities_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        #usa_cities_writer.writeheader()
        usa_cities_writer.writerow(fieldnames)

        for row in csv_data:
            if row:
                usa_cities_writer.writerow(row)

