#!/usr/bin/env python

from dotenv import load_dotenv
import boto3

load_dotenv()
Bucket = 'm1gp-mishima'
Key = 'test.csv'

s3 = boto3.resource('s3')
s3.Bucket(Bucket).download_file(Filename=Key, Key=Key)
