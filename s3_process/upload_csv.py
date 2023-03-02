from dotenv import load_dotenv
import boto3

load_dotenv()
client = boto3.client('s3')

Filename = 'test_data/sample.csv'
Bucket = 'm1gp-mishima'
Key = 'test.csv'
client.upload_file(Filename, Bucket, Key)
