
# 准备工作 + 微信读书自动翻页教程
## iOS
### 工具
* Mac
* Xcode
* Python3、pip3

### 安装WebDriverAgent
1. git clone https://github.com/facebook/WebDriverAgent.git
2. ./Scripts/bootstrap.sh
3. 打开`WebDriverAgent.xcodeproj`，设置好开发者apple id
4. Product -> **Test**，在手机上运行，在手机上打开一下刚安装的没有图标的WebDriverAgent，会自动关闭，然后在Xcode控制台会输出ServerURL: http://x.x.x.x:8100
5. brew install imobiledevice
6. iproxy 8100 8100
7. 浏览器访问`http://localhost:8100/status`看到json就说明运行成功

### 安装python-wda
```
pip3 install --pre facebook-wda
```

### 执行
以微信读书为例。在微信读书中打开一本书，然后终端执行：

```
git clone https://github.com/huowenxuan/weread_auto
cd weread_auto
python3 ios.py
```

## Android
### 工具
* Python3、pip3

### 安装uiautomator
```
pip3 install uiautomator
```

### 执行
在微信读书中打开一本书，然后终端执行：

```
git clone https://github.com/huowenxuan/weread_auto
cd weread_auto
python3 android.py
```

# 趣头条小视频自动上拉（仅限android）
打开趣头条app，点击小视频tab