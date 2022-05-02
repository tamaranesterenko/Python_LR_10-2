# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import unittest
import calc
import utest_test_calc

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(utest_test_calc.CalcBasicTests))
calcTestSuite.addTest(unittest.makeSuite(utest_test_calc.CalcExTests))
print("count of tests: " + str(calcTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)

