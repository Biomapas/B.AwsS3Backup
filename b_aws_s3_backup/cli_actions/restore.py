import sys

from b_aws_s3_backup.cli_actions.base_cli_actions import ask_y_n_question, get_all_buckets
from b_aws_s3_backup.color_print import cprint
from b_aws_s3_backup.s3_actions.upload_s3 import UploadDb
from b_aws_s3_backup.exceptions.backup_not_found import BackupNotFound
from b_aws_s3_backup.exceptions.s3_bucket_not_found import S3BucketNotFound
from b_aws_s3_backup.print_colors import PrintColors


def main():
    try:
        bucket_names = [sys.argv[1]]
    except IndexError:
        bucket_names = get_all_buckets()
        bucket_names_readable = '\n'.join(bucket_names)
        question = f'Are you sure you want to restore all these s3 buckets?:\n{bucket_names_readable}\n[y/n]: '

        if not ask_y_n_question(question):
            return

    for bucket_name in bucket_names:
        try:
            UploadDb().upload(bucket_name)
        except (S3BucketNotFound, BackupNotFound) as ex:
            cprint(PrintColors.FAIL, repr(ex))
