from typing import List

import boto3

from b_aws_s3_backup.color_print import cprint
from b_aws_s3_backup.print_colors import PrintColors


def get_all_buckets() -> List[str]:
    buckets = boto3.client('s3').list_buckets()['Buckets']
    return [bucket['Name'] for bucket in buckets]


def ask_y_n_question(question: str) -> bool:
    ans = input(question)

    if ans.lower() == 'n':
        cprint(PrintColors.FAIL, 'Aborted by user.')
        return False
    elif ans.lower() != 'y':
        cprint(PrintColors.FAIL, 'Unsupported answer.')
        return False

    return True
