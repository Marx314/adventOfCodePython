from unittest import TestCase
from src.Day9 import Day9


class Day9Test(TestCase):
    def setUp(self):
        self.day = Day9()

    def tearDown(self):
        pass

    def test_sample_case(self):
        instructions = [
            'London to Dublin = 464',
            'London to Belfast = 518',
            'Dublin to Belfast = 141',
        ]
        self.assertEqual(605, self.day.calc(instructions))

    def test_problem(self):
        instructions = [
            'Faerun to Norrath = 129',
            'Faerun to Tristram = 58',
            'Faerun to AlphaCentauri = 13',
            'Faerun to Arbre = 24',
            'Faerun to Snowdin = 60',
            'Faerun to Tambi = 71',
            'Faerun to Straylight = 67',
            'Norrath to Tristram = 142',
            'Norrath to AlphaCentauri = 15',
            'Norrath to Arbre = 135',
            'Norrath to Snowdin = 75',
            'Norrath to Tambi = 82',
            'Norrath to Straylight = 54',
            'Tristram to AlphaCentauri = 118',
            'Tristram to Arbre = 122',
            'Tristram to Snowdin = 103',
            'Tristram to Tambi = 49',
            'Tristram to Straylight = 97',
            'AlphaCentauri to Arbre = 116',
            'AlphaCentauri to Snowdin = 12',
            'AlphaCentauri to Tambi = 18',
            'AlphaCentauri to Straylight = 91',
            'Arbre to Snowdin = 129',
            'Arbre to Tambi = 53',
            'Arbre to Straylight = 40',
            'Snowdin to Tambi = 15',
            'Snowdin to Straylight = 99',
            'Tambi to Straylight = 70']
        self.assertEqual(207, self.day.calc(instructions))
        self.assertEqual(804, self.day.calc(instructions, max))
