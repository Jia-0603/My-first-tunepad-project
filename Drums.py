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

# 循环2次（共16拍）
for _ in range(2):
    short_drum_beat()

