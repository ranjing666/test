# 单元 068 参考答案：TypeScript 入门

这一份用来对照思路和结构。建议先自己做，再回来比对。

## 文件：`main.ts`

```ts
type StudyTask = {
  title: string;
  done: boolean;
};

const currentTask: StudyTask = {
  title: "TypeScript 入门",
  done: true,
};

function formatTask(task: StudyTask): string {
  return `${task.title} - ${task.done ? "done" : "not done"}`;
}

console.log(formatTask(currentTask));
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 068 starter pack"
git push
```
