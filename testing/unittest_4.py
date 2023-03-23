# unit tests can also check to see if certain exceptions are raised
# this is done via the assertRaises test case
# we can also check to see if warnings are raised

import unittest
import alerts
# alerts.py is a companion file


class SystemAlertTests(unittest.TestCase):

    def test_power_outage_alert(self):
        self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)
        # we pass 3 arguments to assertRaises - the error that is raised, the function and any function arguments

    def test_water_level_warning(self):
        self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)
        # we pass 3 arguments to assertWarns - the warning, the function and any function arguments


unittest.main()
# both tests should pass