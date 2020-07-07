# 手机端自动触摸工具

## 准备工作 + 读书APP自动翻页教程
### iOS
#### 工具
* Mac
* Xcode
* Python3、pip3

#### 安装WebDriverAgent
1. git clone https://github.com/facebook/WebDriverAgent.git
2. ./Scripts/bootstrap.sh
3. 打开`WebDriverAgent.xcodeproj`，在Xcode中设置好开发者apple id
4. 在Xcode中，Product -> **Test**，在手机上运行，在手机上打开一下刚安装的没有图标的WebDriverAgent，会自动关闭，然后在Xcode控制台会输出ServerURL: http://x.x.x.x:8100
5. brew install imobiledevice
6. iproxy 8100 8100
7. 浏览器访问`http://localhost:8100/status`看到json就说明运行成功

#### 安装python-wda
```
pip3 install --pre facebook-wda
```

#### 执行
以微信读书为例。在微信读书中打开一本书，然后终端执行：

```
git clone https://github.com/huowenxuan/auto_touch
cd auto_touch
python3 read_ios.py
```

### Android
#### 工具
* Python3、pip3

#### 安装uiautomator
```
pip3 install -U uiautomator2
```

#### 执行
在读书APP中打开一本书，然后终端执行：

```
git clone https://github.com/huowenxuan/auto_touch
cd auto_touch
```

如果通过USB控制，需要进入开发者选项，打开USB调试，执行：

```
python3 read_android.py
```

如果通过WIFI控制，需要电脑和手机连接同一WIFI，在文件名后添加手机的ip地址

```
python3 read_android.py x.x.x.x
```

## 趣头条小视频自动上拉（仅限android）
打开趣头条app，点击小视频tab，执行：

```
python3 qutoutiao_android.py
```
