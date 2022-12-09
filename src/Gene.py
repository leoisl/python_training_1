from src.DNASequence import DNASequence
from src.Transcript import Transcript, NotAValidTranscript
from src.Plasmid import Plasmid
from typing import List
from constants import promoter_sequence, terminator_sequence


class Gene:
    def __init__(self, plasmid: Plasmid, start_pos: int, end_pos: int):
        self._plasmid = plasmid
        self._start_pos = start_pos
        self._end_pos = end_pos
        self._coding_sequence_start_pos = start_pos + len(promoter_sequence)
        self._coding_sequence_end_pos = end_pos - len(terminator_sequence)
        self._coding_sequence = DNASequence(plasmid.get_record().get_sequence()[
                                            self._coding_sequence_start_pos:self._coding_sequence_end_pos])

    def get_coding_sequence(self) -> DNASequence:
        return self._coding_sequence

    def __eq__(self, other):
        return (self._plasmid, self._start_pos, self._end_pos) == (other._plasmid, other._start_pos, other._end_pos)

    def __str__(self):
        return f"{self._plasmid}[{self._start_pos}:{self._end_pos}]"

    def _get_transcripts(self) -> List[Transcript]:
        transcripts = []
        for reverse in [True, False]:
            for frame in [0, 1, 2]:
                try:
                    transcript = Transcript(self, reverse, frame)
                    transcripts.append(transcript)
                except NotAValidTranscript:
                    pass
        return transcripts

    def is_expressed(self) -> bool:
        transcripts = self._get_transcripts()
        for transcript in transcripts:
            if not transcript.has_PTC():
                return True
        return False
