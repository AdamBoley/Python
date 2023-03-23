# Expected Failures

# there may be cases, where we expect a test to fail
# we may be testing a feature with a known bug, and the test triggers that bug
# or the test is designed to fail
# if this were the case, the failure would mark the results
# we could skip the test
# however, unittest allows us to mark tests as expected failures
# this means that they actually pass in the report

import unittest
import feedback


class CustomerFeedbackTests(unittest.TestCase):

    @unittest.expectedFailure
    def test_survey_form(self):
        self.assertEqual(feedback.issue_survey(), 'Success')
    # feedback.issue_servey raises a custom FormError
    # as we know this, we can expect the test to fail
    # the decorator is how we mark tests as one we expect to fail

    def test_complaint_form(self):
        self.assertEqual(feedback.log_customer_complaint(), 'Success')


unittest.main()
