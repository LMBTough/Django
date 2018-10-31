# MARKDOWN转换成HTML以及高亮代码

标签（空格分隔）： HTML

---

## 首先是转换成html代码
```
<script type="text/javascript" src="{%static '/showdown/dist/showdown.min.js'%}"></script>
```
把id为middle元素中的内容转换
```
<script>
            var text = document.getElementById("middle").innerHTML;
            console.log(text);
            var converter = new showdown.Converter();
            var html = converter.makeHtml(text);
            document.getElementById("middle").innerHTML = html;
</script>
```
## 其次是高亮代码
导入包
```
<link type="text/css" rel="stylesheet" href="/static/highlight/styles/color-brewer.css">
<script type="text/javascript" src="{%static 'jquery-1.11.3.js'%}"></script>
```
执行初始化
```
<script>
hljs.initHighlightingOnLoad();
</script>
```
---
##淡入效果
```
#middle{
    width: 50%;
    position:relative;
    top: 100px;
    margin:auto;
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
    animation: fade-in 2s;
    -webkit-animation: fade-in 1.5s;
    /*test*/
    /*background-color: darkorange;*/
}
@keyframes fade-in {
    0% {opacity: 0; top: 0px;}/*初始状态 透明度为0*/
    40% {opacity: 0;}/*过渡状态 透明度为0*/
    100% {opacity: 1;}/*结束状态 透明度为1*/
}
@-webkit-keyframes fade-in {/*针对webkit内核*/
    0% {opacity: 0;
        top: 0px;}
    40% {opacity: 0;}
    100% {opacity: 1;}
}
```



