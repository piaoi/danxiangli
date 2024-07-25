**python编写一个脚本，每天新建一个文件夹，以年月日为文件夹分层目录，每天10点爬取https://xialiu.cn/api/dan/网站的图片保存到本地，图片以日期命名**
实现这个，我们需要分成几个步骤：

每天创建一个以当前日期为分层目录的文件夹。
定时任务每天10点执行。
爬取网站 https://xialiu.cn/api/dan/ 的图片。
将图片保存到本地的相应文件夹。
首先，我们可以使用 os 模块创建目录，使用 requests 模块来发送 HTTP 请求，并使用 schedule 模块来设置定时任务。
**脚本说明：**
create_directory 函数会根据当前日期创建一个目录。
fetch_and_save_image 函数会从指定的API地址获取图片的URL，然后下载并保存图片到本地的相应目录。
使用 schedule 模块设置每天10点执行 job 函数。
脚本会在无限循环中等待任务的执行。
请确保在运行此脚本前安装了所需的库：pip install requests schedule
fetch_and_save_image 函数中的请求现在假设 API 返回的响应中直接包含图片数据，而不是 JSON 格式。
检查响应头中的 Content-Type 是否为 image/jpeg，以确保下载的是 JPEG 格式的图片。
生成图片文件名时使用当前时间的小时、分钟和秒作为文件名的一部分，以确保每次下载的图片文件名唯一。
fetch_and_save_image 函数中的图片文件名现在使用当前日期（例如，2023-07-24.jpg）命名。
其他部分保持不变，确保每天创建相应的目录并下载和保存图片。
