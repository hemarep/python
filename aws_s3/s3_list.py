import boto3
from botocore.exceptions import ClientError

boto3.setup_default_session(profile_name='hema_mac')
s3_client = boto3.client('s3')
s3 = boto3.resource('s3')
l_s3_bucket = 'pythonoct2022'

print(s3_client.list_objects(Bucket=l_s3_bucket)['Contents'])

#printing all objects in the bucket CLIENT LEVEL (low level objects)
for key in s3_client.list_objects(Bucket=l_s3_bucket)['Contents']:
   print(key['Key'])

print("#printing all objects in the bucket RESOURCE LEVEL (high level objects)")
l_s3_bucket_resource = s3.Bucket(l_s3_bucket)
for file in l_s3_bucket_resource.objects.all():
   print(file.key)


###tried from boto3 docs
##not working
##for bucket in l_s3_bucket.all():
#    print(bucket.key)
