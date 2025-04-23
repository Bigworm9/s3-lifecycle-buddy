import boto3
import subprocess
import json
import time
import uuid

# Config
bucket_name = "my-s3-bucket-lifestyle-buddy-jfp"
region = "us-east-1"
lifecycle_file = "lifecycle_policy.json"

def create_bucket():
    if region == "us-east-1":
        subprocess.run([
            "aws", "s3api", "create-bucket",
            "--bucket", bucket_name
        ])
    else:
        subprocess.run([
            "aws", "s3api", "create-bucket",
            "--bucket", bucket_name,
            "--region", region,
            "--create-bucket-configuration", f"LocationConstraint={region}"
        ])
    print(f"[+] Bucket {bucket_name} created.")


def apply_lifecycle_policy():
    lifecycle_config = {
        "Rules": [
            {
                "ID": "AutoDeleteOldObjects",
                "Prefix": "",
                "Status": "Enabled",
                "Expiration": {
                    "Days": 1
                }
            }
        ]
    }

    subprocess.run([
        "aws", "s3api", "put-bucket-lifecycle-configuration",
        "--bucket", bucket_name,
        "--lifecycle-configuration", json.dumps(lifecycle_config)
    ])
    print(f"[+] Lifecycle policy applied to {bucket_name}.")

def upload_test_file():
    with open("test_upload.txt", "w") as f:
        f.write("This is a test file.")
    subprocess.run([
        "aws", "s3", "cp", "test_upload.txt", f"s3://{bucket_name}/"
    ])
    print("[+] Test file uploaded.")

def cleanup():
    subprocess.run([
        "aws", "s3", "rb", f"s3://{bucket_name}", "--force"
    ])
    print(f"[x] Bucket {bucket_name} deleted.")

if __name__ == "__main__":
    create_bucket()
    apply_lifecycle_policy()
    upload_test_file()
    time.sleep(2)
    cleanup()
