import boto3
from botocore.exceptions import NoCredentialsError
import hashlib

class S3Uploader:
    def __init__(self, aws_access_key_id, aws_secret_access_key, bucket_name, region_name='us-west-1'):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )
        self.bucket_name = bucket_name

    def upload_image(self, file_path, object_name=None):
        if object_name is None:
            object_name = file_path

        # Calculate the hash of the file
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        file_hash = hasher.hexdigest()

        # Assign the hash value to object_name
        object_name = file_hash
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, object_name)
            url = f"https://{self.bucket_name}.s3.amazonaws.com/{object_name}"
            return url
        except FileNotFoundError:
            print("The file was not found")
            return None
        except NoCredentialsError:
            print("Credentials not available")
            return None

# Example usage:
# uploader = S3Uploader('your_access_key_id', 'your_secret_access_key', 'your_bucket_name')
# url = uploader.upload_image('/path/to/your/image.jpg')
# print(url)