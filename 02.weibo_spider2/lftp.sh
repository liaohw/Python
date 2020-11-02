#!/bin/csh

# 可以自己修改：
# ftp_ip，用于将本地下载的所有微博图片上传到服务器保存
# USER_ARRAY，用于需要爬取得微博列表，可自行添加
#正常情况下：      sh *.sh
#检查微博名配置：  sh *.sh 1      
#如果存在异常执行：sh *.sh 2

ftp_ip=10.10.xx.xx
ftp_user=liaohw
ftp_passwd=liaohw

ftp_file()
{
        echo "lftp $1 -> $2"
        # lftp
lftp $ftp_ip << EOF
user $ftp_user $ftp_passwd
cd $2
mirror -R $1
exit
EOF
        echo "--------------------rm -rf $1/*"
        rm -rf $1/*
}

ori_path=/home/liaohw/python/weibo_img
dst_path=/data02/usergrp/liaohw/python

############## 装修 图片#####################
# 时尚家居SHOW —— 2043123631
# DIY设计我的家 —— zmqd
# 新居生活馆 —— homekoo2011
# 性感工头 —— 5699464812
# 土巴兔 —— to8to
# 微博房产家居 —— 5524359949
# 家居丶时尚 —— 2714376390
# 一起装修网 —— 17house
# 热家居 —— 2625738240
# 创意家居装修设计 —— starinfo
# 土拨鼠装修网   —— tobosu
# 小户型装修罗曼史   —— 5745465827
# 我的装修日记本   —— 5745465793
# 小户型家居设计   —— moranjia
# 家居装修创意设计   —— 2165286784
#############################################

USER_ARRAY=(
2043123631
# zmqd
# homekoo2011
# 5699464812
# to8to
# 5524359949
# 2714376390
# 17house
# 2625738240
# starinfo
# tobosu
# 5745465827
# 5745465793
# moranjia
# 2165286784
)

array_Count=${#USER_ARRAY[@]}
i_Count=0

# 0下载， 1检查， 2从新下载0里失败的页数
check_flag=0
if [ $# -eq 1 ];then
        check_flag=$1
fi

while [ $i_Count -lt $array_Count ];do
        echo "-------------------$[i_Count+1]/$array_Count begining..."
        weibo_name=${USER_ARRAY[i_Count]}
        i_Count=$[i_Count+1]

        if [ $check_flag -eq 2 ];then
                echo "---------------- ReLoading..."
                # 重新下载之前失败的页数
                redo_file=`find . -name "$weibo_name.redo"`
                if [ $redo_file ];then
                        echo "$weibo_name [need redo]"
                        cat $redo_file
                        python weibo_spider.py $weibo_name $check_flag 
                else
                        echo "$weibo_name [continue]"
                        continue
                fi
        else
                echo "---------------- Loading..."
                # 正常下载或检查
                python weibo_spider.py $weibo_name $check_flag 
        fi

        redo_file=`find . -name "$weibo_name.redo"`
        if [ $redo_file ]; then
                continue
        elif [ $check_flag -eq 1 ]; then
                continue
        else
                echo "-------------------mv ${USER_ARRAY}_* $ori_path"
                `ls | grep $weibo_name | xargs -i mv {} $ori_path`

                if [ `ls -l $ori_path | wc -l` -gt 1 ];then
                        ftp_file $ori_path $dst_path
                else
                        echo "--------------------where is ?"
                        sleep 1
                fi
        fi

        echo "-------------------$[i_Count]/$array_Count ending..."
done

echo "......................run ending......................"

