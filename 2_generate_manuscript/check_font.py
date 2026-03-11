from fontTools.ttLib import TTFont

<<<<<<< HEAD
font = TTFont(r"D:\NTUT\AI\Font-Project\01-1_generate_paper-main\2_generate_manuscript\NotoSansTC-ExtraLight.ttf")
=======
#font = TTFont(r"D:\NTUT\AI\Font-Project\01-1_generate_paper-main\2_generate_manuscript\NotoSansTC-ExtraLight.ttf")
font = TTFont(r"D:\NTUT\AI\Font-Project\01-1_generate_paper-main\2_generate_manuscript\GenSekiGothic-M.ttc")
>>>>>>> d1e4a67 (updata)

# 檢查是否在字型的映射表中
char = 39658
if char in font.getBestCmap():
    print("字型有收錄這個字")
else:
    print("字型真的沒這個字，警告是正確的")