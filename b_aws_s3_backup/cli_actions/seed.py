import sys

from b_aws_s3_backup.s3_actions.seed_s3_bucket import SeedS3Bucket


def main():
    bucket_name = sys.argv[1]
    SeedS3Bucket().seed(bucket_name, 100)
