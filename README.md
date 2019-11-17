# python_web
django record

20191101

重新创建了一个仓库，用于Django小组学习的提交。

安装虚拟环境，使用pycharm将Django工程选定为虚拟环境。用pycharm管理虚拟环境和非虚拟环境很方便。

关于git的使用。自己其实以前就是用的很简单的方法，直接将远程仓库clone下来。昨天自己折腾了一下，又是本地建新仓库，采用git remote add , 又是git fetch, 发现如果本地有东西，远程有东西，这样会冲突，比较麻烦，没必要折腾。不过折腾一番的话也使得自己对这个东西较以前有了更近一步的认识，也有所得。

20191117

将网站部署到pythonanywhere上。

1.在pythonanywhere上注册一个账号。

2.然后在pythonanywhere上运行一个bash控制台，和本机电脑一样的操作。

3.将网站部署到服务器上，需要将部署的网址添加到ALLOWED_HOSTS中，在Django工程的setting.py中添加

4.将GitHub上的Django的仓库克隆下来。

5.在pythonanywhere创建一个python的虚拟环境。

6.环境创建完成之后，创建数据库，收集静态文件。python manage.py collectstatic

7.以上一系列操作完成之后，返回主界面，添加一个web app，在弹出来的选项中选择自己配置，选择虚拟环境安装的Python版本。然后在弹出来的界面中虚拟环境的那一项中配置上虚拟环境的路径

8.配置 WSGI 文件

```
import os
import sys

path = '/home/<your-username>/my-first-blog'  # use your own username here
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
```

其中path的路径填上Django工程的路径

重新加载之后，然后访问<http://<your-user-name>.pythonanywhere.com/>

就可以看到你的网页了，如果成功的话。没有出现的话，根据弹出来的提示，看具体的报错信息进行调试。

9.配置静态文件的路径。这样访问Django自带的后台的时候，就会有样式了。

