# B.AwsS3Backup

A python based package that allows you to back up, restore, and seed S3 buckets.

### Description

Sometimes you want to make a small modification to your S3 bucket, however it usually requires
destruction of the bucket itself. This library allows you to do those small modifications without 
any headache. You can easily backup all your data to your local computer, delete the bucket, create
a new one with desired modifications, and then simply restore it!

### Remarks

[Biomapas](https://biomapas.com) aims to modernise life-science 
industry by sharing its IT knowledge with other companies and 
the community. This is an open source library intended to be used 
by anyone. Improvements and pull requests are welcome.

### Related technology

- Python 3
- S3
- Boto3

### Assumptions

The project assumes the following:

- You have basic knowledge in python programming.
- You have basic knowledge in S3.

### Useful sources

- Read more S3:<br>
https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html

### Install

The project is built and uploaded to PyPi. Install it by using pip.

```
pip install b_aws_s3_backup
```

Or directly install it through source.

```
pip install .
```

### Usage & Examples

The library uses boto3 AWS SDK for interacting with AWS environment. Hence,
environmental credentials (such as `aws_access_key_id`, `aws_secret_access_key`, and `region_name`)
are required.

The library exposes cli commands. Read more about them down below.

##### s3seed

Seeds your S3 bucket with random data.

```shell
> s3seed BucketName
```

##### s3back

Backups your whole bucket(s).

```shell
# Single bucket.
> s3back BucketName

# All buckets.
> s3back 
```

##### s3rest

Restores your whole bucket(s).

```shell
# Single bucket.
> s3rest BucketName

# All bucket.
> s3rest
```

### Testing

This project currently has no tests.

### Contribution

Found a bug? Want to add or suggest a new feature?<br>
Contributions of any kind are gladly welcome. You may contact us 
directly, create a pull-request or an issue in github platform.
Lets modernize the world together.
