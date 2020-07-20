# tdemail
使用python发送邮件

## 内容列表

- [背景](#背景)
- [安装](#安装)
- [使用说明](#使用说明)
- [使用许可](#使用许可)

## 背景
笔者长期从事大数据开发工作，日常工作长需要将数据结果以文件附件的形式发送给业务人员，面临以下问题：
1. 需求较多时一天可能需要发送多封邮件，多次下载附件到开发机，然后使用邮件客户端或网页版邮箱发送邮件，非常繁琐
2. 有些需求需要每天定时发送邮件，这就要求配置一个定时任务，手动发送邮件已经不能满足需求

基于以上问题，笔者基于python开发了一个邮件发送工具，可以方便的解决以上问题。

## 安装
适用于python2和python3，无需安装，下载修改发送邮箱和密码后直接使用。


## 使用说明
```python
python tdemail.py params
```
参数说明：
```bash
:param receiver: 收件人
:param [acc]: 抄送人
:param subject: 邮件主题
:param content: 邮件内容
:param [attachment]: 邮件附件
```

### 示例
示例1：
```python
python tdemail.py -r tiangx@tangdou.com -s 测试邮件主题 -c 测试邮件内容 -t rawlog.sql 
```
示例2：
```python
# 如果邮件标题或邮件内容中包含空格或换行符，请以单引号包裹，如：
python tdemail.py -r tiangx@tangdou.com -s '测试 这是一个 测试啊？' -c '测试
b
d
com
内容' -t y.txt
```

## 使用许可

[MIT](LICENSE) © MuChen