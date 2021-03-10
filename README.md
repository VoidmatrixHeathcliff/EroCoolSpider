# EroCoolSpider

[EroCool 漫画图集网站](https://zha.erocool.me/) 爬虫

+ 支持列表页爬取和详情页爬取

+ 所有爬取的图集将位于 `Gallery` 文件夹下的对应名称的文件夹内，`meta.json` 中保存的是图集的元信息，如标签、图片数、图片源链接等

+ 支持链接输入或通过启动参数传入爬取链接

+ `.bat` 文件为已封装的启动命令，各文件和对应功能见下表：

    |            文件名             |       功能       |
    |:-----------------------------:|:----------------:|
    |          `start.bat`          |  无参数启动爬虫  |
    | `start_language_Chinese.bat`  |   爬取中文图集   |
    | `start_language_English.bat`  |   爬取英文图集   |
    | `start_language_English.bat`  |   爬取英文图集   |
    | `start_language_Japanese.bat` |   爬取日文图集   |
    |      `start_latest.bat`       |   爬取最新图集   |
    |     `start_rank_day.bat`      | 爬取每日排行图集 |

*由于网站地址变化不定，请在爬取失败时提交 issue 或发送邮件到 Voidmatrix@qq.com 通知作者*