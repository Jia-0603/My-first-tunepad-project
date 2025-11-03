def guitar_melody():
    # 第1-2拍：
    playNote(60, beats=1)    # C4
    playNote(64, beats=0.5)  # E4
    playNote(67, beats=0.5)  # G4
    
    # 第3-4拍：
    playNote(69, beats=0.5)  # A4
    playNote(67, beats=0.5)  # G4
    playNote(64, beats=1)    # E4
    
    # 第5-6
    playNote(60, beats=0.5)  # C4
    playNote(57, beats=0.5)  # A3
    playNote(60, beats=1)    # C4
    
    # 第7-8拍：收尾动机（短促有力）
    playNote(64, beats=0.5)  # E4
    playNote(60, beats=0.5)  # C4

# 循环3次
for _ in range(3):
    guitar_melody()
