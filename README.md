# EroCoolSpider

[EroCool 漫画图集网站](https://zha.erocool.me/) 爬虫

+ 支持列表页爬取和详情页爬取

+ 所有爬取的图集将位于 `Gallery` 文件夹下的对应名称的文件夹内，`meta.json` 中保存的是图集的元信息，如标签、图片数、图片源链接等

+ 支持链接输入或通过启动参数传入爬取链接

+ `BatchDownload.py` 可以自动多进程批量下载列表页内容

+ `CollectCover.py` 可以提取已下载图集的封面至 `Cover` 文件夹（默认为图集已下载图片的第一张）

+ `OpenGallery.py` 可以打开指定名称的图集（而避免使用让人厌烦的 Windows 搜索功能）

+ `.bat` 文件为已封装的启动命令，各文件和对应功能见下表：

|            文件名             |        功能        |
|:-----------------------------:|:------------------:|
|          `start.bat`          |   无参数启动爬虫   |
|       `start_batch.bat`       |  启动列表批量下载  |
| `start_language_Chinese.bat`  |    爬取中文图集    |
| `start_language_English.bat`  |    爬取英文图集    |
| `start_language_Japanese.bat` |    爬取日文图集    |
|      `start_latest.bat`       |    爬取最新图集    |
|     `start_rank_day.bat`      |  爬取每日排行图集  |
|      `collect_cover.bat`      |    提取图集封面    |
|      `open_gallery.bat`       | 打开指定名称的图集 |

### 注意  
由于 BeautifulSoup 中使用了 `lxml` 解析，未安装相关库可能导致 “获取网页原始信息错误！” 的异常报错，请先安装 [相关库](https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) 再进行爬取

*由于网站地址变化不定，请在爬取失败时提交 issue 或发送邮件到 Voidmatrix@qq.com 通知作者*