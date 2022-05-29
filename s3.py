import boto3

s3_client = boto3.client(service_name='s3', region_name='us-east-1',
                         aws_access_key_id='AKIASITP24H6OMEJIVO7',
                         aws_secret_access_key='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')


# s3_client.download_file("lab2-pavliuk", "data_USD.csv", "data_USD_from_S3.csv")



s3_client.upload_file("data_USD.csv", "lab2-pavliuk", "(this file on s3 server)data_USD.csv")









