import sys
from b_aws_s3_backup.exceptions.s3_bucket_not_found import S3BucketNotFound
from b_aws_s3_backup.color_print import cprint
from b_aws_s3_backup.cli_actions.base_cli_actions import get_all_buckets, ask_y_n_question
from b_aws_s3_backup.s3_actions.download_s3_bucket import DownloadS3Bucket
from b_aws_s3_backup.print_colors import PrintColors


def main():
    try:
        bucket_names = [sys.argv[1]]
    except IndexError:
        bucket_names = get_all_buckets()
        bucket_names_readable = '\n'.join(bucket_names)
        question = f'Are you sure you want to backup all these s3 buckets?:\n{bucket_names_readable}\n[y/n]: '

        if not ask_y_n_question(question):
            return

    for bucket_name in bucket_names:
        try:
            DownloadS3Bucket().download(bucket_name)
        except S3BucketNotFound as ex:
            cprint(PrintColors.FAIL, repr(ex))
