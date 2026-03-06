# Troubleshooting

## 1. 提示没有 Flask

处理方式：

```bash
pip install -r requirements.txt
```

## 2. 浏览器打不开页面

检查顺序：

1. 确认终端里 Flask 还在运行
2. 确认地址是 `http://127.0.0.1:5000`
3. 看终端有没有报错

## 3. 页面文字变了但样式没变

常见原因：

- 没刷新浏览器
- CSS 文件路径不对

检查点：

- `base.html` 里是否用了 `url_for('static', filename='style.css')`

## 4. 改代码后没生效

处理方式：

- 先保存文件
- 再刷新浏览器
- 如果还不行，重启 Flask
