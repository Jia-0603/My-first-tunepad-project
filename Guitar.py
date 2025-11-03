def guitar_melody():
    # 第1-2拍：C大调主音C4（60）
    playNote(60, beats=1)    # C4
    playNote(64, beats=0.5)  # E4
    playNote(67, beats=0.5)  # G4
    
    # 第3-4拍：小跳音+回主音（增加旋律起伏）
    playNote(69, beats=0.5)  # A4
    playNote(67, beats=0.5)  # G4
    playNote(64, beats=1)    # E4
    
    # 第5-6拍：下行音阶（流畅衔接）
    playNote(60, beats=0.5)  # C4
    playNote(57, beats=0.5)  # A3
    playNote(60, beats=1)    # C4   
    
    playNote(64, beats=0.5)  # E4（
    playNote(60, beats=0.5)  # C4

# 循环3次（共24拍，适配鼓点循环）
for _ in range(3):
    guitar_melody()
