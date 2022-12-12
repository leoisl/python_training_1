from src.DNASequence import DNASequence
from src.ProteinSequence import ProteinSequence
from unittest.mock import patch
from unittest import TestCase

class TestProteinSequence(TestCase):
    def test___constructor___0_nts___0_aa(self):
        actual = ProteinSequence(DNASequence(""))
        expected = ""
        self.assertEqual(str(actual), expected)

    def test___constructor___1_nts___0_aa(self):
        actual = ProteinSequence(DNASequence("A"))
        expected = ""
        self.assertEqual(str(actual), expected)

    def test___constructor___2_nts___0_aa(self):
        actual = ProteinSequence(DNASequence("AC"))
        expected = ""
        self.assertEqual(str(actual), expected)

    def test___constructor___3_nts___1_aa(self):
        actual = ProteinSequence(DNASequence("ACT"))
        expected = "T"
        self.assertEqual(str(actual), expected)

    def test___constructor___4_nts___1_aa(self):
        actual = ProteinSequence(DNASequence("ACTG"))
        expected = "T"
        self.assertEqual(str(actual), expected)

    def test___constructor___5_nts___1_aa(self):
        actual = ProteinSequence(DNASequence("ACTGG"))
        expected = "T"
        self.assertEqual(str(actual), expected)

    def test___constructor___6_nts___2_aa(self):
        actual = ProteinSequence(DNASequence("ACTGGC"))
        expected = "TG"
        self.assertEqual(str(actual), expected)

    def test___constructor___complex(self):
        actual = ProteinSequence(DNASequence("TGGTATCGATCATTATCTAGTCAGTCGTAGTCAGCGATGCAT"))
        expected = "WYRSLSSQS_SAMH"
        self.assertEqual(str(actual), expected)

    @patch.object(ProteinSequence, "_translate", return_value="MPYYRPPP_")
    def test___get_first_pos_of_aminoacid___not_found(self, translate_mock):
        sequence = ProteinSequence(DNASequence("hello!"))
        actual_pos = sequence.get_first_pos_of_aminoacid("I")
        expected_pos = -1
        translate_mock.assert_called_once_with("hello!")
        self.assertEqual(actual_pos, expected_pos)

    @patch.object(ProteinSequence, "_translate", return_value="MPYYRPPP_")
    def test___get_first_pos_of_aminoacid___found(self, translate_mock):
        sequence = ProteinSequence(DNASequence(""))
        actual_pos = sequence.get_first_pos_of_aminoacid("P")
        expected_pos = 1
        self.assertEqual(actual_pos, expected_pos)

    @patch.object(ProteinSequence, "_translate", return_value="MPYYRPPP_")
    def test___get_first_pos_of_aminoacid___last_aminoacid___found(self, translate_mock):
        sequence = ProteinSequence(DNASequence(""))
        actual_pos = sequence.get_first_pos_of_aminoacid("_")
        expected_pos = 8
        self.assertEqual(actual_pos, expected_pos)

    @patch.object(ProteinSequence, "_translate", return_value="MPYYRPPP_")
    def test___get_last_pos_of_aminoacid___not_found(self, translate_mock):
        sequence = ProteinSequence(DNASequence(""))
        actual_pos = sequence.get_last_pos_of_aminoacid("I")
        expected_pos = -1
        self.assertEqual(actual_pos, expected_pos)

    @patch.object(ProteinSequence, "_translate", return_value="MPYYRPPP_")
    def test___get_last_pos_of_aminoacid___found(self, translate_mock):
        sequence = ProteinSequence(DNASequence(""))
        actual_pos = sequence.get_last_pos_of_aminoacid("P")
        expected_pos = 7
        self.assertEqual(actual_pos, expected_pos)

    @patch.object(ProteinSequence, "_translate", return_value="MPYYRPPP_")
    def test___get_last_pos_of_aminoacid___first_aminoacid___found(self, translate_mock):
        sequence = ProteinSequence(DNASequence(""))
        actual_pos = sequence.get_last_pos_of_aminoacid("M")
        expected_pos = 0
        self.assertEqual(actual_pos, expected_pos)

