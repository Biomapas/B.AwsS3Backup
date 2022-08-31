import os
from typing import Optional, List, Dict

from b_aws_s3_backup.color_print import cprint
from b_aws_s3_backup.exceptions.backup_not_found import BackupNotFound
from b_aws_s3_backup.print_colors import PrintColors
from b_aws_s3_backup.s3_actions.base_s3_action import BaseS3Action


class UploadS3(BaseS3Action):
    def upload(self, bucket_name: str, backups_dir: Optional[str] = None) -> None:
        backups_dir = backups_dir or self.default_directory(bucket_name)

        upload_files: List[Dict[str, str]] = []
        for root, subdirs, files in os.walk(backups_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_key = file_path.replace(backups_dir, '')
                if file_key.startswith('/'):
                    file_key = file_key[1:]

                upload_files.append({
                    "file_path": file_path,
                    "file_key": file_key
                })

        if len(upload_files) < 1:
            cprint(PrintColors.FAIL, f'Directory ({backups_dir}) does not contain any backup files!')
            raise BackupNotFound()

        for file in upload_files:
            self.client.upload_file(
                Filename=file['file_path'],
                Bucket=bucket_name,
                Key=file['file_key']
            )

            cprint(
                PrintColors.OKGREEN,
                f'Successfully uploaded restore data ({file}).'
            )

        cprint(PrintColors.OKGREEN, 'Successfully restored the S3 bucket.')
