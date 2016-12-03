from unittest import TestCase

from src.Year2015.Day19 import Day19


class Day19Test(TestCase):
    def setUp(self):
        self.day = Day19()

    def simple_puzzle(self):
        return '''H => HO
H => OH
O => HH

HOH'''

    def simple_puzzle_part2(self):
        return '''e => H
e => O
H => HO
H => OH
O => HH'''

    def test_simple_part2(self):
        self.assertEqual(3, self.day.minimal_step_to(self.simple_puzzle_part2(), expected_molecule='HOH'))

    def test_simple_part2_hohoho(self):
        self.assertEqual(6, self.day.minimal_step_to(self.simple_puzzle_part2(), expected_molecule='HOHOHO'))

    def test_simple_puzzle_give_four(self):
        self.assertEqual(4, self.day.possibilities(self.simple_puzzle()))

    # TODO(marx314) : 19 part 2!
    # def test_puzzle_step2(self):
    #    self.assertEqual(6, self.day.minimal_step_to_puzzle(self.puzzle()))

    # def test_puzzle_give_four(self):
    #    self.assertEquals(576, self.day.possibilities(self.puzzle()))

    def puzzle(self):
        return '''Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'''
