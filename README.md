# zutNet

中原工学院校园网的快速连接方式，基于Python

## 使用步骤

0.连接校园网
1.按要求填写信息  
2.运行Python文件（使用时请关闭代理）  
3.登录成功  

## 编译为exe

安装pyinstaller

```sh
pip install pyinstaller
```

在当前目录下运行

```sh
pyinstaller --onefile login_script.py
```

点击 dist 文件夹中的 login_script.exe 文件即可运行

## 说明

仅在本人电脑上测试过，可成功运行，有问题请提issues
