# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import unittest
import utest_test_calc

testCases = []
testCases.append(utest_test_calc.CalcBasicTests)
testCases.append(utest_test_calc.CalcExTests)

testLoad = unittest.TestLoader()

suites = []
for tc in testCases:
    suites.append(testLoad.loadTestsFromTestCase(tc))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)

