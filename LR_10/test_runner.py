# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import unittest
import calc
import utest_test_calc

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(utest_test_calc.CalcTest))

runner = unittest.TestSuite()
runner.run(calcTestSuite)

