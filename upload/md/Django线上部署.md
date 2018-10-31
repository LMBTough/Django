#Django线上部署

标签（空格分隔）： Django

---

如果没有指定DEBUG=True， 系统不会自动实现路由功能，需要手动指定。
通常部署线上Django项目为了安全起见，部署DEBUG=False

---
##原先的静态文件部署：
```
STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR, 'static')
```
##现在的静态文件部署
```
STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR, 'static_u')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
###STATIC_ROOT 是集中包括所有Django应用static文件夹和STATICFILES_DIRS静态文件的存储地方。

```./manage.py collectstatic```
###执行上面代码可以在部署上线之前把所有之前静态文件夹里面的内容复制到STATIC_ROOT中

---

##手动部署路由
在原来的urls.py中加入静态文件的配置文件
```
from django.conf import settings
url(r'^static/(?P<path>.*)$', django.views.static.serve,{'document_root': settings.STATIC_ROOT})
```





