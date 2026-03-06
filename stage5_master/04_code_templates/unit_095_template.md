# 单元 095 起步模板：面试总复习

这一份不是最终答案，而是一个可以继续补、继续改的起步包。

## 文件：`schema.sql`

```sql
CREATE TABLE items (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT
);
```

## 文件：`query.sql`

```sql
SELECT id, name
FROM items
ORDER BY id DESC;
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 095 starter pack"
git push
```
