from typing import Any, Dict, List, Optional
from pathlib import Path

from b_aws_s3_backup.exceptions.s3_bucket_not_found import S3BucketNotFound

from b_aws_s3_backup.color_print import cprint
from b_aws_s3_backup.s3_actions.base_s3_action import BaseS3Action
from b_aws_s3_backup.print_colors import PrintColors


class DownloadS3Bucket(BaseS3Action):
    def download(self, bucket_name: str, download_dir: Optional[str] = None) -> None:
        """
        Downloads a whole S3 bucket to a specified download dir.
        """
        # Ensure that the download directory is available.
        download_dir = download_dir or self.default_directory(bucket_name)
        download_dir = Path(download_dir)
        download_dir.mkdir(parents=True, exist_ok=True)

        continuation_token = None

        cprint(PrintColors.OKBLUE, f'Downloading {bucket_name} bucket files...')

        while True:
            keys: List[str] = []
            dirs: List[str] = []

            kwargs = dict(Bucket=bucket_name)
            if continuation_token:
                kwargs['ContinuationToken'] = continuation_token

            try:
                response: Dict[Any, Any] = self.client.list_objects_v2(**kwargs)
            except self.client.exceptions.NoSuchBucket:
                cprint(PrintColors.FAIL, 'S3 bucket not found!')
                raise S3BucketNotFound()

            items: List[Dict[Any, Any]] = response.get('Contents') or []
            count: int = response.get('KeyCount') or len(items)
            continuation_token = response.get('NextContinuationToken')

            if count == 0:
                break

            # Extract which items are files and which are directories.
            for i in items:
                key = i.get('Key')
                if key[-1] != '/':
                    keys.append(key)
                else:
                    dirs.append(key)

            # Create directories locally to represent same S3 structure.
            for d in dirs:
                directory = Path(f'{download_dir}/{d}')
                cprint(PrintColors.OKBLUE, f'Creating directory {str(directory)}...')
                directory.mkdir(parents=True, exist_ok=True)

            # Download all files to created directories.
            for key in keys:
                file_path = Path(f'{download_dir}/{key}')
                file_path.parent.mkdir(parents=True, exist_ok=True)
                cprint(PrintColors.OKBLUE, f'Downloading file {file_path}...')
                self.client.download_file(bucket_name, key, str(file_path))

            if not continuation_token:
                break

        cprint(PrintColors.OKGREEN, 'Successfully finished download operation.')
