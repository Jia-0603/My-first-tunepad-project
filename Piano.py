def guitar_melody():
    # Beats 1-2:
    playNote(60, beats=1)    # C4
    playNote(64, beats=0.5)  # E4
    playNote(67, beats=0.5)  # G4
    
    # Beats 3-4:
    playNote(69, beats=0.5)  # A4
    playNote(67, beats=0.5)  # G4
    playNote(64, beats=1)    # E4
    
    # Beats 5-6:
    playNote(60, beats=0.5)  # C4
    playNote(57, beats=0.5)  # A3
    playNote(60, beats=1)    # C4
    
    # Beats 7-8: Finishing Motif (Short and Powerful)
    playNote(64, beats=0.5)  # E4
    playNote(60, beats=0.5)  # C4

# Repeat three times
for _ in range(3):
    guitar_melody()
