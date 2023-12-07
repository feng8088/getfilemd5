![CSDN图标](https://github.com/feng8088/getfilemd5/blob/main/1688.png)

这是使用Python3开发的一个小功能，用于获取文件的MD5。
一般的应用场景就是用来对比两个文件的MD5是否一致，用来确保手上的文件与原始文件是否为同一个文件。
本身代码文件很小才2KB，加了UI界面以及打包成exe，集成了Python3运行环境。
所以成品的exe文件有8M之外。

源代码已开源,大家可以自行学习研究，如有问题可在github反馈，我不一定及时会看到。
个人也是边学习边开发，不一定完全好用或达到您的要求。
但也许能给您一点启发或思路，您可以完善为自己的版本。

打包方式如下
```
pip install pyinstaller
pyinstaller -Fw .\exe版.py
```
