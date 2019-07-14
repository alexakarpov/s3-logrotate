#!/usr/bin/python3

import boto3, sys

if len(sys.argv) != 3:
    print("Usage: rotate <bucket> <prefix>")
    sys.exit(1)

client = boto3.client('s3')
bucket = sys.argv[1]
prefix = sys.argv[2]

res = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
print(res)

if res['KeyCount'] == 0:
    print("No keys found for prefix provided")
    sys.exit(0)

files = res['Contents']
file_count = len(files)
print("Found " + str(file_count) + " S3 files")

earliest = min(files, key=lambda k: k['LastModified'])

if (file_count < 3):
    print("Would delete %s if count was more than 3" % earliest['Key'])
else:
    print("Deleting " + str(earliest['Key']))
    client.delete_object(Bucket=bucket, Key=earliest['Key'])
