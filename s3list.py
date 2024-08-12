import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
def list_files_in_bucket (bucket_name):
	s3 = boto3.client('s3')
        # List objects in the specified bucket
	response = s3.list_objects_v2(Bucket=bucket_name)
        
        # Check if the bucket contains objects
	if 'Contents' in response:
		print(f"Files in bucket '{bucket_name}':")
		for obj in response['Contents']:
			print(f" - {obj['Key']}")
	else:
		print(f"The bucket '{bucket_name}' is empty or does not contain any objects.")
		
bucket_name= 'bucket9312'
list_files_in_bucket(bucket_name)
