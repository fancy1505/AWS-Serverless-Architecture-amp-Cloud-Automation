import boto3
from datetime import datetime, timezone, timedelta

# Initialize S3 client
s3 = boto3.client('s3')

# Replace with your actual S3 bucket name
BUCKET_NAME = 'your-bucket-name'

def lambda_handler(event, context):

    # Define 1-day threshold
    days = 1
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)

    # List objects in the bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    # Check if bucket contains files
    if 'Contents' not in response:
        print("Bucket is empty")
        return

    # Loop through files
    for obj in response['Contents']:
        key = obj['Key']
        last_modified = obj['LastModified']

        # Compare file date with cutoff date
        if last_modified < cutoff_date:
            print(f"Deleting file: {key}")

            # Delete old file
            s3.delete_object(
                Bucket=BUCKET_NAME,
                Key=key
            )

    print("Cleanup completed")
