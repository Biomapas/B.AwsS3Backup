import os
import random
import uuid

from b_aws_s3_backup.color_print import cprint
from b_aws_s3_backup.print_colors import PrintColors
from b_aws_s3_backup.s3_actions.base_s3_action import BaseS3Action


class SeedS3Bucket(BaseS3Action):
    def seed(self, s3_bucket_name: str, data_count: int) -> None:
        cprint(PrintColors.OKBLUE, f'Seeding {s3_bucket_name} bucket with {data_count} random files...')

        for index in range(data_count):
            key = f'{self.random_directory()}chunk{index}'
            self.client.put_object(
                Bucket=s3_bucket_name,
                Key=key,
                Body=self.random_bytes()
            )

            cprint(
                PrintColors.OKGREEN,
                f'({index + 1}/{data_count}) Successfully seeded S3 bucket with {key} file.'
            )

        cprint(PrintColors.OKGREEN, 'Successfully seeded the S3 bucket.')

    @classmethod
    def random_bytes(cls) -> bytes:
        return os.urandom(1000)

    @classmethod
    def random_directory(cls) -> str:
        return random.choice([
            '',
            'a/',
            'a/test/',
            'a/dir/subdir/',
            'b/c/d/e/f/g/h/',
            'c/rand/stuff/',
            f'd/{uuid.uuid4()}/',
            f'e/{uuid.uuid4()}/',
            f'e/{uuid.uuid4()}/{uuid.uuid4()}/{uuid.uuid4()}/'
        ])
