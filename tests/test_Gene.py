from unittest import TestCase
from unittest.mock import patch, call, Mock
from src.Gene import Gene
from src.Transcript import Transcript, NotAValidTranscript

class TestGene(TestCase):
    # could be done without the build method, by mocking Transcript.__new__, Transcript.__init__, and Gene.__eq__
    @patch.object(Transcript, "build", side_effect=["T1", "T2", "T3", "T4", "T5", "T6"])
    def test____get_transcripts___all_six_transcripts_are_valid(self, build_mock):
        dummy_gene = Gene("plasmid", 0, 0)
        transcripts = dummy_gene._get_transcripts()
        build_mock.assert_has_calls([
            call(dummy_gene, True, 0),
            call(dummy_gene, True, 1),
            call(dummy_gene, True, 2),
            call(dummy_gene, False, 0),
            call(dummy_gene, False, 1),
            call(dummy_gene, False, 2),
        ], any_order=True)
        self.assertEqual(transcripts, ["T1", "T2", "T3", "T4", "T5", "T6"])

    @patch.object(Transcript, "build", side_effect=["T1", NotAValidTranscript, NotAValidTranscript, "T4", "T5", NotAValidTranscript])
    def test____get_transcripts___3_valid_3_invalid(self, build_mock):
        dummy_gene = Gene("plasmid", 0, 0)
        transcripts = dummy_gene._get_transcripts()
        build_mock.assert_has_calls([
            call(dummy_gene, True, 0),
            call(dummy_gene, True, 1),
            call(dummy_gene, True, 2),
            call(dummy_gene, False, 0),
            call(dummy_gene, False, 1),
            call(dummy_gene, False, 2),
        ], any_order=True)
        self.assertEqual(transcripts, ["T1", "T4", "T5"])


    @patch.object(Gene, "_get_transcripts", return_value=[])
    def test___is_expressed___no_transcripts_are_valid___not_expressed(self, *uninteresting_mocks):
        dummy_gene = Gene("plasmid", 0, 0)
        self.assertFalse(dummy_gene.is_expressed())

    @patch.object(Gene, "_get_transcripts", return_value=[Mock(has_PTC=Mock(return_value=True)),
                                                          Mock(has_PTC=Mock(return_value=True)),
                                                          Mock(has_PTC=Mock(return_value=True))])
    def test___is_expressed___3_transcripts___all_have_PTC___not_expressed(self, *uninteresting_mocks):
        dummy_gene = Gene("plasmid", 0, 0)
        self.assertFalse(dummy_gene.is_expressed())

    @patch.object(Gene, "_get_transcripts", return_value=[Mock(has_PTC=Mock(return_value=True)),
                                                          Mock(has_PTC=Mock(return_value=True)),
                                                          Mock(has_PTC=Mock(return_value=False))])
    def test___is_expressed___3_transcripts___one_does_not_have_PTC___expressed(self, *uninteresting_mocks):
        dummy_gene = Gene("plasmid", 0, 0)
        self.assertTrue(dummy_gene.is_expressed())