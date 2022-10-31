import csv
"""
with open('usa_cities.csv','r') as f:
    csv_data = csv.reader(f)
    print(csv_data)
    next(csv_data)
    for row in csv_data:
        print(row)

    with open('usa_cities_new.csv','w') as fw:
        usa_city_new_data = csv.writer(fw,delimiter='\t')
        for row in csv_data:
            print(row)
            usa_city_new_data.writerow(row)
  """
# DictWriter Method
with open('usa_cities.csv', 'r') as file:
    csv_data = csv.DictReader(file)
    # for row in csv_data:
    #     print(row)
    # print(type(csv_data))

    with open('usa_cities_new_dict.csv', 'w') as new_file:
        fieldnames = {'LatD':'VA_LatD',
                      'LatM':'VA_LatM',
                      'LatS':'VA_LatS',
                      'NS':'VA_NS',
                      'LonD':'VA_LonD',
                      'LonM':'VA_LonM',
                      'LonS':'VA_LonS',
                      'EW':'VA_EW',
                      'City':'VA_City',
                      'State':'VA_State'}

        usa_cities_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='-')
        #usa_cities_writer.writeheader()
        usa_cities_writer.writerow(fieldnames)
        for row in csv_data:
            #print(row)
            if row:
                #print(row['State'])
                if (row['State'].strip(' '))=='VA':
                    usa_cities_writer.writerow(row)

