import ddddocr

def getCode():
    ocr = ddddocr.DdddOcr()
    with open('./code_png/code.png', 'rb') as f:  # 打开图片
        img_bytes = f.read()  # 读取图片
    res = ocr.classification(img_bytes)  # 识别
    return res