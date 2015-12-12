from unittest import TestCase
from src.Day9 import Day9


class Day9Test(TestCase):
    def setUp(self):
        self.day = Day9()

    def tearDown(self):
        pass

    def test_sample_case(self):
        instructions = 'London to Dublin = 464\n' \
                       'London to Belfast = 518\n' \
                       'Dublin to Belfast = 141'
        self.assertEqual(605, self.day.calc(instructions))

    def test_puzzle(self):
        self.assertEqual(207, self.day.calc(self.puzzle()))
        self.assertEqual(804, self.day.calc(self.puzzle(), method=max))

    def puzzle(self):
        return 'Faerun to Norrath = 129\n' \
               'Faerun to Tristram = 58\n' \
               'Faerun to AlphaCentauri = 13\n' \
               'Faerun to Arbre = 24\n' \
               'Faerun to Snowdin = 60\n' \
               'Faerun to Tambi = 71\n' \
               'Faerun to Straylight = 67\n' \
               'Norrath to Tristram = 142\n' \
               'Norrath to AlphaCentauri = 15\n' \
               'Norrath to Arbre = 135\n' \
               'Norrath to Snowdin = 75\n' \
               'Norrath to Tambi = 82\n' \
               'Norrath to Straylight = 54\n' \
               'Tristram to AlphaCentauri = 118\n' \
               'Tristram to Arbre = 122\n' \
               'Tristram to Snowdin = 103\n' \
               'Tristram to Tambi = 49\n' \
               'Tristram to Straylight = 97\n' \
               'AlphaCentauri to Arbre = 116\n' \
               'AlphaCentauri to Snowdin = 12\n' \
               'AlphaCentauri to Tambi = 18\n' \
               'AlphaCentauri to Straylight = 91\n' \
               'Arbre to Snowdin = 129\n' \
               'Arbre to Tambi = 53\n' \
               'Arbre to Straylight = 40\n' \
               'Snowdin to Tambi = 15\n' \
               'Snowdin to Straylight = 99\n' \
               'Tambi to Straylight = 70'
