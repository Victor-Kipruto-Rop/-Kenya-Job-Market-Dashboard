import boto3, json
from datetime import date

s3 = boto3.client("s3", endpoint_url="http://localhost:9000",
                  aws_access_key_id="minioadmin", aws_secret_access_key="minioadmin")

def upload_raw(jobs: list):
    key = f"raw/jobs_{date.today().isoformat()}.json"
    s3.put_object(Bucket="job-market", Key=key, Body=json.dumps(jobs).encode())
    print(f"Uploaded {len(jobs)} jobs to s3://job-market/{key}")
