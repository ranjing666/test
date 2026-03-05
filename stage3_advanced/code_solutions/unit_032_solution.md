# 单元 032 参考答案：SQL 与 SQLite 基础

这一份用来对照思路和结构。建议先自己做，再回来比对。

## 文件：`schema.sql`

```sql
CREATE TABLE items (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT
);

INSERT INTO items (name, description)
VALUES ('Notebook', 'study notes'), ('Task', 'daily work');
```

## 文件：`query.sql`

```sql
SELECT id, name
FROM items
WHERE name IS NOT NULL
ORDER BY id DESC;
```

## 使用说明

1. 先手敲一遍，不要直接复制。
2. 跑起来或读一遍输出，再改一个小地方。
3. 卡住时回到单元讲义和工作簿。

## 建议提交

```bash
git add .
git commit -m "Work on unit 032 starter pack"
git push
```
