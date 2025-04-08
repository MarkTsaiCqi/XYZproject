import os
import base64
import time
import ddddocr
from selenium import webdriver


# js获取canvas里面的图片，并且保存,返回图片地址
def down_verification_image(dirver, canvas_class):
    # 获取当前父亲目录，AutomatedTesdDemo
    mypath = os.path.dirname((os.path.abspath(__file__)))
    timename = time.strftime("%Y-%m-%d-%H%M%S")
    js = 'return document.getElementById("{}").toDataURL("image/png");'.format(canvas_class)
    image_data = dirver.execute_script(js)      # 执行js代码得到图片数据
    image_base64 = image_data.split(",")[1]      # 获得base64编码的图片信息
    image_bytes = base64.b64decode(image_base64)  # 将base64转为bytes类型
    image_png="{}\\{}.png".format(mypath, timename)
    with open(image_png, "wb") as f:
        f.write(image_bytes)
    return image_png



# 验证码识别返回数字
def verification(img2path):
    ocr = ddddocr.DdddOcr()
    with open(img2path, 'rb') as f:
        img_bytes = f.read()
    result = ocr.classification(img_bytes)
    os.remove(img2path)
    return result


if __name__ == '__main__':
    pass
    # browser = webdriver.Chrome(executable_path='chromedriver')
    # browser.get("https://test.zyzntech.com/#/login?redirect=%2Fdashboard")
    # imgpaht = down_verification_image("verifyCanvas")
    # asd = verification(imgpaht)
    # print(asd)
    # time.sleep(10)
