#!bin/bash
# sh tdemail.sh tiangx@tangdou.com tiangx2@tangdou.com 测试邮件主题 测试邮件内容 rawlog.sql

receiver=$2
acc=$4
subject=$6
content=$8
attachment=${10}

echo "receiver:${receiver}"
echo "acc:${acc}"
echo "subject:${subject}"
echo "content:${content}"
echo "attachment:${attachment}"

result1=`python params_validate.py -r ${receiver} -a ${acc} -s ${subject} -c ${content} -t ${attachment}`
echo ${result1}
if [ -n ${attachment} ]; then
    python txt2csv.py ${attachment} && python tdemail.py -r ${receiver} -a ${acc} -s ${subject} -c ${content} -t ${attachment}
else
    python tdemail.py -r ${receiver} -a ${acc} -s ${subject} -c ${content}
fi
