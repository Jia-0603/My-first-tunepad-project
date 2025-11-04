def guitar_melody():
    # Beats 1-2: C major tonic C4 (60)
    playNote(60, beats=1)    # C4
    playNote(64, beats=0.5)  # E4
    playNote(67, beats=0.5)  # G4
    
    # Beats 3-4: Staccato + Return to the main note (to increase melodic undulation)
    playNote(69, beats=0.5)  # A4
    playNote(67, beats=0.5)  # G4
    playNote(64, beats=1)    # E4
    
    # Beats 5-6: Descending scale (smooth transition)
    playNote(60, beats=0.5)  # C4
    playNote(57, beats=0.5)  # A3
    playNote(60, beats=1)    # C4   
    
    playNote(64, beats=0.5)  # E4（
    playNote(60, beats=0.5)  # C4

# Repeat three times (a total of 24 beats, suitable for drum beat loop)
for _ in range(3):
    guitar_melody()
