import os
import requests
from datetime import datetime
import schedule
import time

def create_directory():
    # 获取当前日期
    today = datetime.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    
    # 创建以年月日为分层目录的文件夹
    directory = os.path.join(year, month, day)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return directory

def fetch_and_save_image():
    # 创建目录
    directory = create_directory()
    
    # 发送HTTP请求获取图片
    url = "https://xialiu.cn/api/dan/"
    response = requests.get(url)
    
    if response.status_code == 200:
        # 假设API返回的响应中直接是图片数据
        if response.headers['Content-Type'] == 'image/jpeg':
            # 构建图片文件名，以当前日期命名
            image_name = datetime.now().strftime("%Y-%m-%d") + ".jpg"
            image_path = os.path.join(directory, image_name)
            
            # 保存图片到本地文件夹
            with open(image_path, 'wb') as file:
                file.write(response.content)
            print(f"Image saved to {image_path}")
        else:
            print("Response is not in JPEG format")
    else:
        print("Failed to fetch image")

def job():
    fetch_and_save_image()

# 设置定时任务每天10点执行
schedule.every().day.at("08:04").do(job)

print("Scheduler started. Waiting for next scheduled task...")

# 保持脚本运行
while True:
    schedule.run_pending()
    time.sleep(1)
