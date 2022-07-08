from datetime import date, timedelta
import requests


class Student:
    """
    A Student class as a base for method testing
    """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        # The underscore that prepends the first-name and last-name above means Read Only
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        # the start and end dates use the today method of the date library. The end date does not account for leap years
        self.naughty_list = False
    
    @property  # a decorator since the method is a means of getting data only
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
        #  returns a composite of the first_name and the second_name
    
    def alert_santa(self):
        self.naughty_list = True
        #  if called, this method will set the attribute of naughty_list on an instantiated class to True, from its default value of False

    @property
    # these decorators are necessary for getting tests that test these methods to pass. @property is used for methods that produce data from attributes of the class
    def email_address(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"
        # if called, this method will return a student's email address, in the format of first_name.last_name@email.com

    
    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)
    #if called, this method will apply and extension to the student's end date, and the caller must supply a value for days

    
    def course_schedule(self):
        response = requests.get(f'http://company.com/course-schedule/{self._last_name}/{self._first_name}')
        # response makes a call to a fictional API for a student's schedule, passing in the student's last name and first name to the URL to retrieve the correct response

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request"

        # This was built prior to any tests being written, and those tests cannot test both outcomes - i.e a successful request and a failed request
        # mocking allows tests of both outcomes

