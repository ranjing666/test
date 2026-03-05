# 单元 025 参考答案：CSS 布局与响应式

这一份用来对照思路和结构。建议先自己做，再回来比对。

## 文件：`index.html`

```html
<section class="card">
  <h1>CSS 布局与响应式</h1>
  <p>这个页面已经有基础结构和样式。</p>
</section>
```

## 文件：`style.css`

```css
body {
  margin: 0;
  padding: 32px;
  background: linear-gradient(180deg, #f4f6fb, #e9eef8);
  font-family: "Microsoft YaHei", sans-serif;
}

.card {
  max-width: 560px;
  margin: 0 auto;
  padding: 24px;
  background: white;
  border-radius: 18px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
}
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 025 starter pack"
git push
```
