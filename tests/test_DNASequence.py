from unittest import TestCase
from src.DNASequence import DNASequence

class TestDNASequence(TestCase):
    def test___constructor___ACGT_sequence___ok(self):
        actual_sequence = DNASequence("ACGT")
        expected_sequence = "ACGT"

        self.assertEqual(expected_sequence, str(actual_sequence))

    def test___get_rc___empty_sequence(self):
        source = DNASequence("")
        actual = source.get_rc()
        expected = DNASequence("")
        self.assertEqual(actual, expected)

    def test___get_rc___one_base(self):
        source = DNASequence("A")
        actual = source.get_rc()
        expected = DNASequence("T")
        self.assertEqual(actual, expected)

    def test___get_rc___long(self):
        source = DNASequence("AGGGGTCACA")
        actual = source.get_rc()
        expected = DNASequence("TGTGACCCCT")
        self.assertEqual(actual, expected)

    def test___shift___zero_shift(self):
        source = DNASequence("ACGTTGCA")
        actual = source.shift(0)
        expected = DNASequence("ACGTTGCA")
        self.assertEqual(actual, expected)

    def test___shift___one_shift(self):
        source = DNASequence("ACGTTGCA")
        actual = source.shift(1)
        expected = DNASequence("CGTTGCA")
        self.assertEqual(actual, expected)

    def test___shift___two_shift(self):
        source = DNASequence("ACGTTGCA")
        actual = source.shift(2)
        expected = DNASequence("GTTGCA")
        self.assertEqual(actual, expected)

    def test___shift___six_shift(self):
        source = DNASequence("ACGTTGCA")
        actual = source.shift(6)
        expected = DNASequence("CA")
        self.assertEqual(actual, expected)