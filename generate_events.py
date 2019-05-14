import json
import boto3
import testdata


class User(testdata.DictFactory):
	id = testdata.CountingFactory(10)
	firstname = testdata.FakeDataFactory('firstName')
	lastname = testdata.FakeDataFactory('lastName')
	address = testdata.FakeDataFactory('address')
	age = testdata.RandomInteger(10, 30)
	gender = testdata.RandomSelection(['female', 'male'])


str_aws_region = "eu-west-1"
str_kinesis_firehose_stream = "test_events_aurora" # todo: get stream name from secure string store
int_users_to_put = 100000

firehose = boto3.client('firehose')

# todo: create a record with complex JSON
# todo: implement backoff logic
for user in User().generate(int_users_to_put):  # generate int_users_to_put users
	response = firehose.put_record(
		DeliveryStreamName=str_kinesis_firehose_stream,
		Record={
			"Data": json.dumps(user)
		}
	)

	print(response)


