# 简要
    weibo_spider2.0在原来weibo_spider基础上【修改】：
    1、支持url获取、分析、图形获重试功能；由于一次性大量访问会导致后续出现网络问题，retry几次就ok
    2、由于短时间频繁访问和下载，处理几千张图片之后可能cookie原因而暂时无法访问（过几个小时又ok),所以对于访问失败的页面进行保存，提供后续继续下载
    3、本地磁盘有限，添加shell脚本支持镜像备份到服务器
    4、支持多个微博一次性批量下载
    5、异常捕获
## 微博爬虫weibo_spider2.0

    *说明：
        修改自己的微博账户cookie替代xxx，如cookie = {"Cookie": "xxx"}
    *执行脚步:
        #正常情况下：      sh *.sh
        #检查微博名配置：  sh *.sh 1      
        #如果存在异常执行：sh *.sh 2
    *效果如下：
        liaohw@lhw-ubuntu:~/python$ sh lftp.sh
        -------------------1/1 begining...
        ---------------- Loading...
        @微博名 :<2043123631> 总共页数: 132
        ***********下载信息
        －－－－－爬虫准备Page－－－－－
        －－－－－爬虫准备就绪
        。。。
        。。。【省略】
        。。。
        －－－－－抓取页面:P101/132－－－－－
        URL => http://weibo.cn/u/2043123631?filter=1&page=101
        正在文字爬取...
         89 : 痘痘爆发时，千万别用手挤、用暗疮针挑，不然时间一长，痘印、痘坑、痘疤会夹杂在一起爆发，用再多的药物都难治好了，整张脸算是毁了。分享个去痘淡印的方法，摆脱痘印脸，其实很简单，赶紧学起来!http://t.cn/RGs94U3
         90 : 今天真被自己从鼻子上撕下来的超大一片黑头恶心到了，不弄不知道，原来鼻子上有这么多脏东西啊，都吓死宝宝了[吃惊][吃惊]http://t.cn/RGsanu2 秒拍视频
         91 : 优雅美
         92 : 【高级灰】北欧风格家居。
         93 : 酷酷暗黑风格的游戏杂志编辑的家。
         94 : 终于没有烦人的黑头了，真爽，还给男朋友试了[哈哈][哈哈]http://t.cn/RGkm5Q2 秒拍视频
         95 : 北欧の夏，简单不失精致。
         96 : 【Soft rock 建面100㎡混搭两居室】这是一个将美式、工业、北欧等元素结合的一套混搭作品，东方与西方的优雅邂逅，怀旧和自然贯穿整个设计。辰佑设计
         97 : 轻柔水蓝色+明亮典雅白，惬意乡村。
         98 : 小浴室的收纳
        正在图片信息爬取...
         －G获取Page101 的图片信息: http://ww1.sinaimg.cn/large/79c797afjw1f26g3yhah6j20c8096dgi.jpg
         －G获取Page101 的图片信息: http://ww3.sinaimg.cn/large/79c797afjw1f26g3yo95jj20c809mdgs.jpg
         －G获取Page101 的图片信息: http://ww3.sinaimg.cn/large/79c797afjw1f26g3yjk5vj20c80ic3zm.jpg
        。。。
        。。。【省略】
        。。。
        －－－－－抓取页面:P109/132－－－－－
        URL => http://weibo.cn/u/2043123631?filter=1&page=109
        [访问失败,将重试!]－－ retry 1 time
        [访问失败,将重试!]－－ retry 2 time
        [重试成功!!!]－－ retry ok
        正在文字爬取...
         169 : 照着视频里的方法做，真的可以看到有半厘米长的黑头被拔出来！！[震惊][震惊]http://t.cn/RGnWCkP 秒拍视频
         170 : 【130㎡《绿影流光》实木简美风】家，有时候是幸福的归宿，有时候是喜悦的空间，有时候更是能给自己一份惊喜和情怀！设计：阿墨（上辑）
         171 : 【实用面积40平极致利用，做你想不到】厨房？好小！餐厅？没有！卫生间？only one！可是在卧室里面！经过设计师的巧手改造，开放式厨房虽然有益于减少阻隔，扩大空间，但中餐油烟颇重，并不是所有人都适用~请谨慎参考！by 80设计
         172 : 没有什么比现在脸上没有一颗痘印的感觉更好的了，坚持的这段时间，还是没有白费的，真心推荐：http://t.cn/RGEnoij 秒拍视频
         173 : 闺蜜跟着这视频做，拔出来一大片黑头，看得我整个人都不好了[吐]http://t.cn/RGE8UYm 秒拍视频
         174 : 【北欧文艺范】简约雅致的居室风格，摒弃了繁杂无用的设计，看似平淡，实则耐人寻味。配上拼色地板，更是让空间显得灵动、精致。@大自然整体家装 全屋整体家装为你打造环保文艺的北欧风家居。
         175 : 【杭州温莎郡 简约小复式】业主的话：曾经许诺在30岁前努力能有属于自己的房子, 车子。庆幸的是当这一切变成现实的同时，还有了一个可爱的孩子，虽然不是豪宅豪车，但终于有了一个完整的家...[心]by.力设计
         176 : 美式风格教你打造一个治愈系客厅。
         177 : 【哈巴涅拉---酒红与姜黄的偶然相遇】建筑面积：89㎡；户型：三室两厅；风格：简约美式， 业主非常喜欢大胆，色彩分明，又有温馨感的设计。cr.见图
         178 : 别以为挤出痘痘里面的白色颗粒就完事了，大错特错！这样只会留下难看的痘印和深深的痘坑，今天来教大家一种不伤皮肤去痘淡印方法。一起来学学！http://t.cn/RGRrSCu
        正在图片信息爬取...
        [访问失败,将重试!]－－ retry 1 time
        [访问失败,将重试!]－－ retry 2 time
        [访问失败,将重试!]－－ retry 3 time
        [访问失败,将重试!]－－ retry 4 time
        [重试成功!!!]－－ retry ok
        [JPG地址错误,将重试!]－－ retry 1 time
        [JPG地址错误,将重试!]－－ retry 2 time
        [JPG地址错误,将重试!]－－ retry 3 time
        [重试成功!!!]－－ retry ok
         －G获取Page109 的图片信息: http://ww4.sinaimg.cn/large/79c797afjw1f1sk42k7y8j20i30c1q6d.jpg
        。。。
        。。。【省略】
        。。。
        -第1224张图片 正在下载...
        -第1225张图片 正在下载...
        -第1226张图片 正在下载...
        -第1227张图片 正在下载...
        －－－－－结果－－－－－
        + 微博图片爬取完毕，共1227张，保存路径/home/liaohw/python/2043123631_时尚家居SHOW
        ......................run ending......................





