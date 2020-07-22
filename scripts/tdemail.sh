#!bin/bash

# sh tdemail.sh -r tiangx@tangdou.com --acc tiangx2@tangdou.com -s 测试主题 -c 测试内容 -t a.csv
acc='-1'
attachment='-1'

ARGS=`getopt -o hvr:a:s:c:t: --long help,version,receiver:,acc:,subject:,content:attachment: -- "$@"`
if [ $? != 0 ] ; then echo "Terminating..." >&2 ; exit 1 ; fi
eval set -- "$ARGS"
while true;do
    case "$1" in
        -r|--receiver)
            echo "-r | --receiver"
            receiver=$2
            shift 2
            ;;
        -a|--acc)
            echo "-a | --acc"
            acc=$2
            shift 2
            ;;
        -s|--subject)
            echo "-s | --subject"
            subject=$2
            shift 2
            ;;
        -c|--content)
            echo "-c | --content"
            content=$2
            shift 2
            ;;
        -t|--attachment)
            echo "-t | --attachment"
            attachment=$2
            shift 2
            ;;
        --)
            shift
            break
            ;;
        *)
            echo "未知的属性:{$1}"
            exit 1
            ;;
    esac
done

echo "receiver:${receiver}"
echo "acc:${acc}"
echo "subject:${subject}"
echo "content:${content}"
echo "attachment:${attachment}"

# 验证必传参数
if [ -z ${receiver} ] || [ -z ${subject} ] || [ -z ${content} ]; then
    echo "Error! Required Parameter:-r <receiver> -s <subject> -c <content>"
    exit 1
fi

# attachment参数不为空
if [ -n ${attachment} ] && [ "-1" != ${attachment} ]; then
    python txt2csv.py ${attachment} && python tdemail.py -r ${receiver} -a ${acc} -s ${subject} -c ${content} -t ${attachment}
else
    python tdemail.py -r ${receiver} -a ${acc} -s ${subject} -c ${content} -t ${attachment}
fi