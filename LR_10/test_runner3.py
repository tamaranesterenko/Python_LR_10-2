# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import unittest
import utest_test_calc

testLoad = unittest.TestLoader()

suites = testLoad.loadTestsFromModule(utest_test_calc)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suites)

