

from genmidi import Midi
from music import NoteSeq

seq1 = NoteSeq('C D E')
seq2 = NoteSeq('F G A')
midi = Midi()
midi.seq_notes(seq1)
midi.seq_notes(seq2)
midi.write('foo.mid')