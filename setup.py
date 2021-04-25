from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

with open('VERSION') as file:
    VERSION = file.read()
    VERSION = ''.join(VERSION.split())

setup(
    name='b_aws_s3_backup',
    version=VERSION,
    license='Apache License 2.0',
    packages=find_packages(exclude=['venv', 'b_aws_s3_backup_test']),
    entry_points={
        'console_scripts': [
            's3back=b_aws_s3_backup.cli_actions.backup:main',
            's3rest=b_aws_s3_backup.cli_actions.restore:main',
            's3seed=b_aws_s3_backup.cli_actions.seed:main',
        ],
    },
    description=('S3.'),
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'boto3',
        'b-continuous-subprocess>=0.3.2,<1.0.0',
    ],
    author='Laimonas Sutkus',
    author_email='laimonas.sutkus@biomapas.com',
    keywords='S3',
    url='https://github.com/biomapas/B.AwsS3Backup.git',
)
