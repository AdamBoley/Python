import unittest
from student import Student
from datetime import date, timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):
    
    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Smith')
        # this is an instance variable, so all further use of student must be replaced with self.student

    def tearDown(self):
        print('tearDown')
        # the tearDown method is not necessary here, and is included with a print statement to show where it is called
        # when this test file is run, the setUp method is run before each test method, and the tearDown method is run after each test method
        # This repeats for as many test methods as there are
        # the setUpClass and tearDownClass methods are run once, and are used in cases where we want to set up a database, run tests on it and then destroy it

    @classmethod
    def setUpClass(cls):
        print('setUpClass')
        # when run, we can see that setUpClass is run once at the beginning of the tests

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        # when run, we can see that tearDownClass is run once at the end of the tests

    def test_full_name_method(self):
        # student = Student('John', 'Smith')
        # creates an instance of the imported Student class, with first name of John, last name of Smith
        # this is currently unused, since student is now instantiated at the top of the test class in the setUp method
        # This necessitates the use of the self. prior to each use of student
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Smith')
        # calls the full_name method of the student variable, which should be an instance of the Student class with first name John and second name Smith
        # the test checks whether the output of the full_name function when called on this instance returns John Smith, which it should

    
    def test_alert_santa(self):
        # student = Student('John', 'Smith')
        # creates an instance of the imported Student class, with first name of John, last name of Smith
        # this is currently unused, since student is now instantiated at the top of the test class in the setUp method
        # This necessitates the use of the self. prior to each use of student
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)
        # rather than looking for a return statement, this test merely checks to see if the value of naughty_list in the instantiated class student is True
        # without an alert_santa method / function in the Student class, this test will fail with an attribute error, since no such method exists
        # with such a method that works as intended, this test passes
    

    def test_email_address_method(self):
        # student = Student('John', 'Smith')
        # creates an instance of the imported Student class, with first name of John, last name of Smith
        # this is currently unused, since student is now instantiated at the top of the test class in the setUp method
        # This necessitates the use of the self. prior to each use of student
        print('test_email_address')
        self.assertEqual(self.student.email_address, 'john.smith@email.com')
        # this test requires that the email_address method of the Student class have the @property decorator

    def test_apply_extension(self):
        print('test_apply_extension')
        old_end_date = self.student.end_date  # fixes the current old_end_date
        extension = 30
        self.student.apply_extension(extension)  # calls apply_extension function with an argument of 30 days
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=extension))  # checks to see if the new value of end_date is equal to the old value + an extension period

    
    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
        # mocked_get is an object
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "success"
            # note that ok and text are properties from the course_schedule method, so we can give them mock values

            schedule = self.student.course_schedule()
            # calls the student_course method of the the instantiated student class
            self.assertEqual(schedule, "success")
            # schedule should be "success", as course_schedule() will return text, which is set to "success" per the mocked_get above 


    def test_course_schedule_failure(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False
            # note that lack of mocked_get.return_value.text, since a failed request in the method will not return response.text, but rather a custom string

            schedule = self.student.course_schedule()
            # calls the student_course() method

            self.assertEqual(schedule, "Something went wrong with the request")
            # checks whether schedule and the string are the same
            # they should be since student_course() will return that string if the reponse.ok = False, i.e the request fails


if __name__ == '__main__':
    unittest.main()



