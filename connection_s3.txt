import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError  
def connect_s3(): 
	try:
		s3 = boto3.client('s3') #initializes client for s3 operation
		response = s3.list_buckets() # it is used to retrieve a list of all buckets in AWS
		print("Connected to S3 successfully.")
		print("Buckets available:")
		for bucket in response['Buckets']:
			print(f" - {bucket['Name']}")
		return s3
	except NoCredentialsError:
		print("No credentials available. Please configure your AWS credentials.")
	except PartialCredentialsError:
		print("Incomplete credentials provided. Please check your AWS credentials configuration.")
	except ClientError as e:
		print(f"Client error occurred: {e}") #Catches errors specific to AWS Service requests.
	except Exception as e:
		print(f"An unexpected error occurred: {e}") # Catches any other unexpected error
s3_client = connect_s3() 

