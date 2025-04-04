# networkx
存放一些network的内容


## 常规操作

### 导出环境
```
uv export --format requirements-txt > requirements.txt
```
### 更新文档
```
mkdocs serve # 预览
mkdocs gh-deploy -d ../.temp # 同步到github网站
```

### 运行测试并同步到测试服务
```
uv run pytest --html=/Users/zhaoxuefeng/GitHub/aiworker/html/networkx.html
```
