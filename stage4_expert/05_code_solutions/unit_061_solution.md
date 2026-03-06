# 单元 061 参考答案：Node、npm 与前端工具链

这一份用来对照思路和结构。建议先自己做，再回来比对。

## 文件：`package.json`

```json
{
  "name": "study-finished-example",
  "private": true,
  "scripts": {
    "dev": "vite"
  }
}
```

## 文件：`main.js`

```javascript
const currentTime = new Date().toLocaleTimeString();
console.log(`Task finished at ${currentTime}`);
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 061 starter pack"
git push
```
