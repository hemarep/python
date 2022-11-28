import boto3
import  os

boto3.setup_default_session(profile_name='hema_mac')
s3_client = boto3.client('s3')

def download_s3_file(p_s3_bucket_name, p_s3_folder, p_s3_file_name, p_local_download_folder_file):
    l_s3_file_path_name = p_s3_folder + "/" + p_s3_file_name
    s3_client.download_file(p_s3_bucket_name, l_s3_file_path_name, p_local_download_folder_file)

def upload_my_file(p_s3_bucket_name, p_s3_folder, p_local_folder_file_to_upload, p_upload_file_name):
    l_s3_file_name = p_s3_folder + "/" + p_upload_file_name
    s3_client.upload_file(p_local_folder_file_to_upload,p_s3_bucket_name,l_s3_file_name)

def downloadDirectoryFroms3(bucketName, remoteDirectoryName):
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucketName)
    for obj in bucket.objects.filter(Prefix = remoteDirectoryName):
        print(obj)
        if not os.path.exists(os.path.dirname(obj.key)):
            os.makedirs(os.path.dirname(obj.key))
        bucket.download_file(obj.key, obj.key) # save to same path

def main():
    l_s3_bucket_c = 'pythonoct2022'
    l_s3_data_folder = 'incoming/'
    l_s3_scripts_folder = 'scripts/db'
    l_file_name = 'usa_cities_new_col_hema.csv'

    #download_s3_file(l_s3_bucket_c,l_s3_data_folder,l_file_name,"usa_cities_new_col_hema.csv")
    # upload_my_file(l_s3_bucket_c, l_s3_data_folder,
    #                 "//Users//arun//pycharmprojects//python/csv/sample.txt",
    #                 'sample.csv')

    downloadDirectoryFroms3(l_s3_bucket_c,l_s3_data_folder)


if __name__ == '__main__': main()