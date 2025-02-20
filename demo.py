from fontTools.ttLib import TTFont
import requests

# 下载字体文件
font_url = "https://img.bosszhipin.com/static/file/2023/3kovsijnt11693967587313.woff2"  # 替换为实际的字体文件 URL
font_data = requests.get(font_url).content
with open("font.woff", "wb") as f:
    f.write(font_data)
font = TTFont('font.woff')
# 获取字符映射表
cmap = font.getBestCmap()
print("字符映射表:", cmap)

salary_text = "-K"

for code, char in cmap.items():
    print(f"{code:04x}: {char}")
    salary_text = salary_text.replace(chr(code), char)


print("解析后的薪资范围:", salary_text)