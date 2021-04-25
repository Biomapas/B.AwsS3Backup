import json
import os
from typing import Optional
from os import listdir
from os.path import isfile, join

from b_aws_s3_backup.exceptions.backup_not_found import BackupNotFound

from b_aws_s3_backup.color_print import cprint
from b_aws_s3_backup.s3_actions.base_s3_action import BaseS3Action
from b_aws_s3_backup.print_colors import PrintColors


class UploadDb(BaseS3Action):
    def upload(self, bucket_name: str, backups_dir: Optional[str] = None) -> None:
        backups_dir = backups_dir or self.default_directory(bucket_name)

        file_paths = []
        for root, subdirs, files in os.walk(backups_dir):
            for file in files:
                file_paths.append(os.path.join(root, file))

        if len(file_paths) < 1:
            cprint(PrintColors.FAIL, f'Directory ({backups_dir}) does not contain any backup files!')
            raise BackupNotFound()

        for file in file_paths:
            self.client.upload_file(
                Filename=file,
                Bucket=bucket_name,
                Key=file
            )

            cprint(
                PrintColors.OKGREEN,
                f'Successfully uploaded restore data ({file}).'
            )

        cprint(PrintColors.OKGREEN, 'Successfully restored the S3 bucket.')
