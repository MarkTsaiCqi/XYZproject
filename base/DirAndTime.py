import time,os
from datetime import datetime
import config


# 获取当前的日期
def getCurrentDate():
    timeTup = time.localtime()
    currentDate = str(timeTup.tm_year)+"_"+str(timeTup.tm_mon)+"_"+str(timeTup.tm_mday)
    return currentDate

# 获取当前时间
def getCurrentTime():
    timeStr = datetime.now()
    nowTime = timeStr.strftime('%H-%M-%S')
    return nowTime

# 创建截图存放的目录
def createCurrentDateDir():
    dirName = os.path.join(config.DIR_PATH+"\screenshots\\", getCurrentDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    return dirName

if __name__=="__main__":
    print(getCurrentTime())
