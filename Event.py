import testdata

class Event(testdata.DictFactory):
	class info(testdata.DictFactory):
		employeeid = testdata.RandomInteger(500, 50000)
		type=testdata.RandomSelection(['full-time', 'part-time'])

	id = testdata.CountingFactory(10)
	firstname = testdata.FakeDataFactory('firstName')
	lastname = testdata.FakeDataFactory('lastName')
	address = testdata.FakeDataFactory('address')
	age = testdata.RandomInteger(10, 30)
	gender = testdata.RandomSelection(['female', 'male'])
	info=info().generate(1)

