# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import unittest
import utest_test_calc

testLoad = unittest.TestLoader()

suites = testLoad.loadTestsFromModule(utest_test_calc)

testResult = unittest.TestResult()

runner = unittest.TextTestRunner(verbosity=1)
runner.run(suites)
print("errors")
print(len(testResult.errors))
print("failures")
print(len(testResult.failures))
print("skipped")
print(len(testResult.skipped))
print("testsRun")
print(testResult.testsRun)



