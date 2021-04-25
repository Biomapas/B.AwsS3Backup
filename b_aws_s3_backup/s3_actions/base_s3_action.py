import boto3


class BaseS3Action:
    def __init__(self):
        self.client = boto3.client('s3')

    @classmethod
    def default_directory(cls, bucket_name: str) -> str:
        return f'./backups/{bucket_name}'
