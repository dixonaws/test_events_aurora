import json
import boto3
from user import User

str_aws_region = "eu-west-1"
str_kinesis_firehose_stream = "test_events_aurora" # todo: get stream name from secure string store
int_users_to_put = 100000

firehose = boto3.client('firehose')

# todo: implement backoff logic
for user in User().generate(int_users_to_put):  # generate int_users_to_put users
	print(user)
	response = firehose.put_record(
		DeliveryStreamName=str_kinesis_firehose_stream,
		Record={
			"Data": json.dumps(user)
		}
	)



