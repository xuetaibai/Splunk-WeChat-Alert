# Splunk-WeChat-Alert  
splunk微信告警脚本   
### 功能介绍  
用于将splunk告警信息推送到微信企业号  
### 安装使用  
#### 环境要求  
1. 需要注册微信企业号  
[点击注册](https://qy.weixin.qq.com/)   
#### 使用  
1. 下载  
```shell
git clone https://github.com/XWJR-Ops/Splunk-WeChat-Alert.git
```
2. 复制脚本到执行位置  
```shell
cd Splunk-WeChat-Alert
cp splunk.sh splunk.py /opt/splunk/bin/scripts
chown splunk.splunk /opt/splunk/bin/scripts/splunk*
chmod 755 /opt/splunk/bin/scripts/splunk*
```
3. splunk创建告警  
splunk创建告警时，触发操作选择运行脚本，脚本名称**splunk.sh**


