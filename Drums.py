from tune import *

def short_drum_beat():
    
    playNote(24, beats=0.5)  
    playNote(30, beats=0.5)  
    
    
    playNote(26, beats=0.5)  
    playNote(33, beats=0.5)  
    playNote(30, beats=0.5)  
    
    
    playNote(24, beats=0.5)
    playNote(30, beats=0.5)
    
    
    playNote(30, beats=0.5)

# Repeat 2 times (total 16 beats)
for _ in range(2):
    short_drum_beat()

