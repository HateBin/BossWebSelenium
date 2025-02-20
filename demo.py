


cmap = {
    '': '1',
    '': '2',
    '': '3',
    '': '4',
    '': '5',
    '': '6',
    '': '7',
    '': '8',
    '': '9',
    '': '0',
 }

salary_text = "-K"

for code, char in cmap.items():
    salary_text = salary_text.replace(code, char)


print("解析后的薪资范围:", salary_text)