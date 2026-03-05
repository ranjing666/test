# 单元 064 参考答案：React Hooks 与表单

这一份用来对照思路和结构。建议先自己做，再回来比对。

## 文件：`App.tsx`

```tsx
import { useState } from "react";
import "./styles.css";

export default function App() {
  const [done, setDone] = useState(false);

  return (
    <main className="app">
      <h1>React Hooks 与表单</h1>
      <p>Status: {done ? "done" : "in progress"}</p>
      <button onClick={() => setDone(!done)}>Toggle</button>
    </main>
  );
}
```

## 文件：`styles.css`

```css
.app {
  padding: 24px;
  font-family: "Microsoft YaHei", sans-serif;
}
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 064 starter pack"
git push
```
