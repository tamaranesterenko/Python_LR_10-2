# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


import unittest
import workers


class WorkersTests(unittest.TestCase):
    def test_select_all_4_rows(self):
        testlist = [
            {
                'surname': 'Nesterenko',
                'name': 'Tamara',
                'zodiac': 'Oven',
                'year': '2022'
            },
            {
                'surname': 'Sviridova',
                'name': 'Oksana',
                'zodiac': 'Pyba',
                'year': '2012'
             },
            {
                'surname': 'Ovechkin',
                'name': 'Daniil',
                'zodiac': 'Strilech',
                'year': '2012'
             }
        ]
        self.assertListEqual(workers.select_all('test_workers.db'), testlist)

    def test_select_by_type(self):
        ans = [
            {
                'surname': 'Nesterenko',
                'name': 'Tamara',
                'zodiac': 'Oven',
                'year': '2022'
             }
        ]
        self.assertListEqual(
            workers.select_by_period('test_workers.db', 2022), ans
        )

    def test_select_all_after_adding(self):
        surname = "Ivanova"
        name = "Valentina"
        zodiac = "Deva"
        year = 2010
        workers.add_worker('test_flights.db', surname, name, zodiac, year)
        testlist = [
            {
                'surname': 'Nesterenko',
                'name': 'Tamara',
                'zodiac': 'Oven',
                'year': '2022'
            },
            {
                'surname': 'Sviridova',
                'name': 'Oksana',
                'zodiac': 'Pyba',
                'year': '2012'
             },
            {
                'surname': 'Ovechkin',
                'name': 'Daniil',
                'zodiac': 'Strilech',
                'year': '2012'
             },
            {
                'surname': 'Ivanova',
                'name': 'Valentina',
                'zodiac': 'Deva',
                'year': '2010'
            }
        ]
        self.assertListEqual(workers.select_all('test_workers.db'), testlist)
