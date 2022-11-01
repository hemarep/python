import csv
import boto3

boto3.setup_default_session(profile_name='hema_mac')
s3_client = boto3.client('s3')

with open('usa_cities.csv', 'r') as file:
    csv_data = csv.DictReader(file)

    with open('usa_cities_new_dict_only_VA.csv', 'w', newline='') as new_file:
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

        usa_cities_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        #usa_cities_writer.writeheader()
        usa_cities_writer.writerow(fieldnames)
        for row in csv_data:
            if row:
                #print(row['State'])
                if (row['State'].strip(' '))=='VA':
                    usa_cities_writer.writerow(row)

    s3_client.upload_file('usa_cities_new_dict_only_VA.csv', 'pythonoct2022', 'Only_VA_On_The_Fly_Hema.csv')