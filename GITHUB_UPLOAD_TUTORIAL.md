# 本地文件上传到 GitHub 的详细教程

这是一份给零基础学习者准备的 GitHub 上传教程。

你可以把它理解成一句最核心的话：

先保存文件，再 `git add`，再 `git commit`，最后 `git push`。

---

## 一、先理解 4 个最重要的动作

### 1. 保存

保存的意思是：

- 你在编辑器里改了内容
- 按 `Ctrl + S`
- 文件真正写进了本地磁盘

如果你没有保存，那么 Git 看不到你最新改了什么。

### 2. `git add`

`git add` 的意思是：

- 把这次改动放进“准备提交”的区域

你可以把它理解成：

“我先把这次要上传的内容装进一个包裹里。”

### 3. `git commit`

`git commit` 的意思是：

- 在本地生成一次版本记录

你可以把它理解成：

“我给这次改动拍了一个快照，并写了一句说明。”

### 4. `git push`

`git push` 的意思是：

- 把本地的提交上传到 GitHub

你可以把它理解成：

“把我本地已经打包好的版本，发到 GitHub 仓库里。”

---

## 二、你必须先知道的一件事

GitHub 早就不支持用账号密码直接做 Git 推送了。

也就是说：

- 不能再用 GitHub 登录密码直接 `git push`
- 现在通常用的是：
  - `HTTPS + Git Credential Manager`
  - `SSH`
  - `Personal Access Token`

最适合新手的是：

- `HTTPS + Git Credential Manager`

---

## 三、最常用的日常上传流程

如果你的仓库已经和 GitHub 连好了，以后通常只用这几步。

### 第 1 步：进入项目文件夹

```powershell
cd "D:\桌面\py测试"
```

如果你是别的项目，就进入别的目录。

### 第 2 步：先看当前状态

```powershell
git status
```

这一步的作用是：

- 看看你改了哪些文件
- 看看有没有还没提交的内容

如果看到很多红字或绿字，不用怕，那只是 Git 在告诉你哪些文件变了。

### 第 3 步：把改动加入暂存区

```powershell
git add .
```

这里的 `.` 意思是：

- 当前目录下所有改动都加入

如果你只想加某一个文件，也可以这样写：

```powershell
git add README.md
```

### 第 4 步：生成一次本地提交

```powershell
git commit -m "更新学习资料"
```

这句话里的：

- `-m` 表示后面要跟一条提交说明

你可以把 `"更新学习资料"` 改成别的，比如：

```powershell
git commit -m "Add day 002 notes"
git commit -m "Fix unit 001 examples"
git commit -m "Update study log"
```

### 第 5 步：上传到 GitHub

如果你的分支是 `master`：

```powershell
git push origin master
```

如果你的分支是 `main`：

```powershell
git push origin main
```

### 第 6 步：确认成功

```powershell
git status
```

如果工作区干净，通常会看到类似意思：

```text
nothing to commit, working tree clean
```

这说明：

- 本地已经没有未提交改动

然后你再去 GitHub 网页看最新文件有没有更新。

---

## 四、如何查看自己当前是 `main` 还是 `master`

运行：

```powershell
git branch --show-current
```

如果输出是：

```text
master
```

那你上传时就用：

```powershell
git push origin master
```

如果输出是：

```text
main
```

那你上传时就用：

```powershell
git push origin main
```

---

## 五、第一次从零开始上传一个本地项目

如果某个文件夹还没有和 GitHub 绑定，就按下面一步一步做。

### 第 1 步：先去 GitHub 网站创建仓库

你需要先在 GitHub 网页上创建一个新仓库。

建议这样做：

- 填仓库名
- 选择公开或私有
- 如果你已经有本地项目，最好不要勾选初始化 `README`、`.gitignore`、`LICENSE`

为什么？

因为这样更容易避免第一次推送冲突。

### 第 2 步：进入本地项目目录

```powershell
cd "D:\你的项目文件夹"
```

### 第 3 步：初始化 Git

```powershell
git init
```

这一步的意思是：

- 告诉 Git：“这个文件夹以后要归你管理了。”

### 第 4 步：设置 Git 用户信息

```powershell
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的GitHub邮箱"
```

这一步是给提交记录标注作者身份。

你可以检查是否设置成功：

```powershell
git config --global user.name
git config --global user.email
```

### 第 5 步：加入全部文件

```powershell
git add .
```

### 第 6 步：做第一次提交

```powershell
git commit -m "Initial commit"
```

### 第 7 步：把分支名改成 `main`

```powershell
git branch -M main
```

这一步的意思是：

- 把当前主分支统一命名成 `main`

### 第 8 步：连接远程 GitHub 仓库

```powershell
git remote add origin https://github.com/你的用户名/你的仓库名.git
```

这句话里的：

- `origin` 是远程仓库的默认名字
- 后面的 URL 是你的 GitHub 仓库地址

### 第 9 步：第一次上传

```powershell
git push -u origin main
```

这里的 `-u` 很重要，意思是：

- 把当前本地分支和远程分支建立默认关联

以后你就可以直接用：

```powershell
git push
```

---

## 六、如何查看远程仓库地址

运行：

```powershell
git remote -v
```

你会看到类似：

```text
origin  https://github.com/你的用户名/你的仓库名.git (fetch)
origin  https://github.com/你的用户名/你的仓库名.git (push)
```

意思是：

- 这个本地仓库已经连接到了 GitHub 上的某个仓库

---

## 七、如果远程仓库地址配错了怎么办

先查看：

```powershell
git remote -v
```

如果地址不对，就改掉：

```powershell
git remote set-url origin https://github.com/你的用户名/你的仓库名.git
```

然后再检查一次：

```powershell
git remote -v
```

---

## 八、Windows 上最适合新手的登录方式

最适合你的方式通常是：

- 安装 `Git for Windows`
- 使用 `HTTPS`
- 让 `Git Credential Manager` 帮你完成认证

常见流程是：

1. 你执行 `git push`
2. 系统弹出浏览器登录 GitHub
3. 你在网页里授权
4. 以后这台电脑通常就不用反复登录

这也是为什么很多时候你没有手动输入密码，也能推送成功。

---

## 九、如果它让你输入用户名和密码，应该怎么办

这时要特别注意：

### 用户名怎么填

如果提示输入：

```text
Username for 'https://github.com':
```

这里填：

- 你的 GitHub 用户名

### 密码怎么填

如果提示输入：

```text
Password for 'https://github.com':
```

这里不要填 GitHub 网站登录密码。

正确做法通常是：

- 用浏览器授权登录
- 或者填 `Personal Access Token`

---

## 十、什么是 Personal Access Token

你可以把它理解成：

- GitHub 给你发的一把专门用于命令行操作的“钥匙”

它不是普通密码。

如果你必须自己创建 Token，大概这样做：

1. 打开 GitHub
2. 进入 `Settings`
3. 进入 `Developer settings`
4. 打开 `Personal access tokens`
5. 建议选 `Fine-grained tokens`
6. 新建一个 token
7. 指定它能访问哪个仓库
8. 给它内容读写权限
9. 生成后复制并保存

要特别注意：

- Token 只会显示一次
- 不要发给别人
- 不要放进代码文件
- 不要提交到 GitHub

---

## 十一、怎么看自己到底有没有上传成功

你可以从 3 个地方确认。

### 方法 1：看命令行

执行完 `git push` 后，如果没有报错，而且有类似上传完成的信息，通常就是成功了。

### 方法 2：看本地状态

```powershell
git status
```

如果状态干净，说明本地没有还没提交的内容。

### 方法 3：看 GitHub 网页

打开你的仓库主页，检查：

- 最新提交信息有没有变化
- 文件内容有没有更新
- 时间是不是刚刚那次提交

---

## 十二、最常见的几种情况

### 情况 1：文件改了，但是 Git 没反应

先检查你是不是没保存。

做法：

1. 回到编辑器
2. 按 `Ctrl + S`
3. 再运行：

```powershell
git status
```

如果还是没反应，说明你可能改的不是这个仓库里的文件。

### 情况 2：`git status` 显示工作区干净

这说明：

- 你没有新改动
- 或者你改了但没保存
- 或者你已经提交过了

### 情况 3：只想上传一个文件

可以这样：

```powershell
git add study_logs/day001.md
git commit -m "Update day001 log"
git push
```

### 情况 4：想上传全部改动

```powershell
git add .
git commit -m "Update files"
git push
```

---

## 十三、常见报错和解决方法

### 1. `nothing to commit, working tree clean`

意思：

- 没有可以提交的新改动

原因通常是：

- 你没改文件
- 你改了但没保存
- 你已经提交完了

### 2. `remote origin already exists`

意思：

- 远程仓库已经配置过了

不要重复 `git remote add origin ...`

应该改成：

```powershell
git remote -v
git remote set-url origin https://github.com/你的用户名/你的仓库名.git
```

### 3. `Authentication failed`

意思：

- 登录认证失败

常见原因：

- 你填了 GitHub 网站密码
- 旧凭据缓存错了
- Token 失效了

解决方向：

- 改用浏览器授权登录
- 或清理 Windows 凭据管理器里的旧 GitHub 凭据
- 然后重新 `git push`

### 4. `non-fast-forward`

意思：

- 远程仓库比你本地更新
- 你不能直接把本地版本硬推上去

通常先同步远程，再推送：

```powershell
git pull --rebase origin main
git push origin main
```

如果你当前分支是 `master`，就把 `main` 换成 `master`。

### 5. `src refspec main does not match any`

意思通常是：

- 你当前并没有 `main` 这个分支

先查一下：

```powershell
git branch --show-current
```

如果显示的是 `master`，那就推：

```powershell
git push origin master
```

---

## 十四、你这个仓库以后最常用的命令

你现在这个项目以后最常用的就是下面这几句：

```powershell
cd "D:\桌面\py测试"
git status
git add .
git commit -m "更新教学资料"
git push origin master
```

如果以后分支改成 `main`，就把最后一行改成：

```powershell
git push origin main
```

---

## 十五、最短记忆版

### 第一次上传

```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用户名/你的仓库名.git
git push -u origin main
```

### 以后日常上传

```powershell
git add .
git commit -m "本次修改说明"
git push
```

---

## 十六、给零基础学习者的建议

一开始不要追求一次记住所有命令。

你只要先牢牢记住这一条：

1. 改文件
2. 保存
3. `git status`
4. `git add .`
5. `git commit -m "说明"`
6. `git push`

只要你能把这 6 步反复练熟，就已经足够完成大部分日常上传任务。

---

## 十七、你的常用检查命令

### 查看状态

```powershell
git status
```

### 查看当前分支

```powershell
git branch --show-current
```

### 查看远程仓库地址

```powershell
git remote -v
```

### 查看最新一次提交

```powershell
git log --oneline -1
```

---

## 十八、一句话总结

本地上传到 GitHub 的完整流程就是：

保存文件 -> `git add` -> `git commit` -> `git push`

如果失败，就检查：

- 有没有保存
- 分支名是不是对的
- 远程地址是不是对的
- 登录认证是不是正常

---

## 十九、如果要上传另一个项目，应该怎么做

这要分成几种情况。

### 情况 1：另一个项目是全新的本地文件夹，还没有连 GitHub

假设你的另一个项目在：

```powershell
D:\另一个项目
```

那么可以这样做：

```powershell
cd "D:\另一个项目"
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用户名/你的新仓库名.git
git push -u origin main
```

这套命令的意思是：

1. 进入项目目录
2. 让 Git 开始管理这个文件夹
3. 把全部文件加入暂存区
4. 生成第一次提交
5. 把主分支命名成 `main`
6. 连接 GitHub 上的新仓库
7. 第一次推送到 GitHub

### 情况 2：另一个项目本地已经是 Git 仓库，但还没有连远程

先进入项目目录：

```powershell
cd "D:\另一个项目"
```

然后检查：

```powershell
git status
git remote -v
```

如果 `git remote -v` 没有输出，说明这个项目还没有连接 GitHub。

这时可以继续：

```powershell
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用户名/你的新仓库名.git
git push -u origin main
```

### 情况 3：另一个项目已经连了远程，但远程地址是错的

不要重新 `git init`。

先看当前远程：

```powershell
git remote -v
```

如果地址不对，就改掉：

```powershell
git remote set-url origin https://github.com/你的用户名/正确的仓库名.git
```

然后推送：

```powershell
git push -u origin main
```

如果你的当前分支不是 `main`，先检查：

```powershell
git branch --show-current
```

如果输出的是 `master`，就改成：

```powershell
git push -u origin master
```

### 情况 4：这个项目已经正常连着 GitHub，只是想继续上传新改动

那就最简单，只要：

```powershell
cd "D:\另一个项目"
git status
git add .
git commit -m "更新内容"
git push
```

### 一个很重要的原则

一个本地项目目录，通常对应一个 GitHub 仓库。

不要把两个完全不同的项目混在同一个仓库里上传。

也不要在一个 Git 仓库里面再随便套另一个独立 Git 仓库，除非你明确知道自己在做什么。

### 另一个项目的最实用模板

以后你拿到任何一个新项目，如果它还没上传过 GitHub，可以直接套下面这组命令：

```powershell
cd "D:\项目路径"
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用户名/仓库名.git
git push -u origin main
```
