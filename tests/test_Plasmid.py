from unittest import TestCase
from unittest.mock import patch
from src.FastaRecord import FastaRecord
from src.DNASequence import DNASequence
from src.Plasmid import Plasmid
from src.Gene import Gene
from src.constants import terminator_sequence

class TestPlasmid(TestCase):
    def setUp(self) -> None:
        self.record = FastaRecord(">record", DNASequence(
            "ACCGTAGGTTGGCAGTCAGTCAGCATCTACTGTTTGCAGTTTTTCGTCTGCTTTTGTCTCTGCTGCTGTCGTTTAAAAA")
        )
        self.plasmid = Plasmid(self.record)

    def test___constructor(self):
        self.assertEqual(self.plasmid._record, self.record)

    def test____find_promoter___just_before_promoter___finds_promoter(self):
        actual_promoter_pos = self.plasmid._find_promoter(4)
        expected_promoter_pos = 5
        self.assertEqual(actual_promoter_pos, expected_promoter_pos)

    def test____find_promoter___just_on_promoter___finds_promoter(self):
        actual_promoter_pos = self.plasmid._find_promoter(5)
        expected_promoter_pos = 5
        self.assertEqual(actual_promoter_pos, expected_promoter_pos)

    def test____find_promoter___just_after_promoter___does_not_find_promoter(self):
        actual_promoter_pos = self.plasmid._find_promoter(6)
        expected_promoter_pos = -1
        self.assertEqual(actual_promoter_pos, expected_promoter_pos)

    def test____find_promoter___just_after_promoter___finds_next_promoter(self):
        record = FastaRecord(">record", DNASequence(
            "ACCGTAGGTTGGCAGTCAGTCAGCATCTACTGTTTGCAGTTTTTCGTCTGCTTTTGTCTCTGCTGCTGTCGTTTAAAAAAGGTTGGCAGTCAGTCAGCATCTACTGTTTGCAG")
                                  )
        plasmid = Plasmid(record)
        actual_promoter_pos = plasmid._find_promoter(6)
        expected_promoter_pos = 79
        self.assertEqual(actual_promoter_pos, expected_promoter_pos)

    def test___get_genes___single_gene(self):
        actual_genes = self.plasmid.get_genes()
        expected_genes = [Gene(self.plasmid, 5, 74)]
        self.assertEqual(actual_genes, expected_genes)

    @patch.object(Plasmid, "_find_promoter", side_effect=[15, -1])
    @patch.object(Plasmid, "_find_terminator", side_effect=[500, -1])
    def test___get_genes___1_promoter_1_terminator___1_gene(self, *mocks):
        dummy_plasmid = Plasmid(None)
        actual_genes = dummy_plasmid.get_genes()
        expected_genes = [Gene(dummy_plasmid, 15, 500+len(terminator_sequence))]
        self.assertEqual(actual_genes, expected_genes)

    @patch.object(Plasmid, "_find_promoter", side_effect=[-1])
    @patch.object(Plasmid, "_find_terminator", side_effect=[-1])
    def test___get_genes___0_promoter_0_terminator___no_genes(self, *mocks):
        dummy_plasmid = Plasmid(None)
        actual_genes = dummy_plasmid.get_genes()
        expected_genes = []
        self.assertEqual(actual_genes, expected_genes)

    @patch.object(Plasmid, "_find_promoter", side_effect=[15, -1])
    @patch.object(Plasmid, "_find_terminator", side_effect=[-1])
    def test___get_genes___1_promoter_0_terminator___no_genes(self, *mocks):
        dummy_plasmid = Plasmid(None)
        actual_genes = dummy_plasmid.get_genes()
        expected_genes = []
        self.assertEqual(actual_genes, expected_genes)

    @patch.object(Plasmid, "_find_promoter", side_effect=[15, 100, -1])
    @patch.object(Plasmid, "_find_terminator", side_effect=[-1])
    def test___get_genes___2_promoter_0_terminator___no_genes(self, *mocks):
        dummy_plasmid = Plasmid(None)
        actual_genes = dummy_plasmid.get_genes()
        expected_genes = []
        self.assertEqual(actual_genes, expected_genes)

    @patch.object(Plasmid, "_find_promoter", side_effect=[-1])
    @patch.object(Plasmid, "_find_terminator", side_effect=[50, -1])
    def test___get_genes___0_promoter_1_terminator___no_genes(self, *mocks):
        dummy_plasmid = Plasmid(None)
        actual_genes = dummy_plasmid.get_genes()
        expected_genes = []
        self.assertEqual(actual_genes, expected_genes)

    @patch.object(Plasmid, "_find_promoter", side_effect=[-1])
    @patch.object(Plasmid, "_find_terminator", side_effect=[50, 200, -1])
    def test___get_genes___0_promoter_2_terminator___no_genes(self, *mocks):
        dummy_plasmid = Plasmid(None)
        actual_genes = dummy_plasmid.get_genes()
        expected_genes = []
        self.assertEqual(actual_genes, expected_genes)

    @patch.object(Plasmid, "_find_promoter", side_effect=[15, 50, -1])
    @patch.object(Plasmid, "_find_terminator", side_effect=[500, -1])
    def test___get_genes___2_promoter_1_terminator___case_1___1_gene(self, *mocks):
        dummy_plasmid = Plasmid(None)
        actual_genes = dummy_plasmid.get_genes()
        expected_genes = [Gene(dummy_plasmid, 15, 500 + len(terminator_sequence))]
        self.assertEqual(actual_genes, expected_genes)

    @patch.object(Plasmid, "_find_promoter", side_effect=[15, 1000, -1])
    @patch.object(Plasmid, "_find_terminator", side_effect=[500, -1])
    def test___get_genes___2_promoter_1_terminator___case_2___1_gene(self, *mocks):
        dummy_plasmid = Plasmid(None)
        actual_genes = dummy_plasmid.get_genes()
        expected_genes = [Gene(dummy_plasmid, 15, 500 + len(terminator_sequence))]
        self.assertEqual(actual_genes, expected_genes)

    @patch.object(Plasmid, "_find_promoter", side_effect=[15, -1])
    @patch.object(Plasmid, "_find_terminator", side_effect=[500, 1000, -1])
    def test___get_genes___1_promoter_2_terminator___case_1___1_gene(self, *mocks):
        dummy_plasmid = Plasmid(None)
        actual_genes = dummy_plasmid.get_genes()
        expected_genes = [Gene(dummy_plasmid, 15, 500 + len(terminator_sequence))]
        self.assertEqual(actual_genes, expected_genes)

    # TODO: why this test fails?
    # @patch.object(Plasmid, "_find_promoter", side_effect=[15, -1])
    # @patch.object(Plasmid, "_find_terminator", side_effect=[5, 1000, -1])
    # def test___get_genes___1_promoter_2_terminator___case_2___1_gene(self, *mocks):
    #     dummy_plasmid = Plasmid(None)
    #     actual_genes = dummy_plasmid.get_genes()
    #     expected_genes = [Gene(dummy_plasmid, 15, 1000 + len(terminator_sequence))]
    #     self.assertEqual(actual_genes, expected_genes)
