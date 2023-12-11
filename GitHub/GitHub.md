# GitHub Desktop

把程式碼丟到 GitHub 上面

## 所需程式 or 環境

- [Git](https://git-scm.com/downloads)
    裝 git 是避免桌面版有沒辦法排解的問題，同時這是最常用的工具
- [GitHub Desktop](https://desktop.github.com/)
    最容易上手的工具，但有些問題沒辦法只靠桌面版解決

## 建立 Repositories

> 需要按的地方會用粉色框框標示

1. 我們要到自己的 repositories 介面新增一個新的 repository。

![GitHub repositories](/GitHub/imgs/github-repositories.png)

2. 再來是設定 repository 的名字，可以選擇要 public 還是 private，差別就是別人看不看得到，最後就按下 create。

![GitHub create repositories](/GitHub/imgs/github-create-repository.png)

3. 創建完會像這個畫面

![GitHub my repository](/GitHub/imgs/github-my-repository.png)

## 把檔案推上去

這邊會有兩個方法，一個是 git command，一個是 GitHub desktop

### Git command

1. `git init`
    初始化 git 資料夾，告訴電腦這個資料夾要跟 git 有關了
2. `git remote add https://github.com/<username>/<repository name>.git`
    新增遠端的連結，總該讓電腦知道目的地吧
3. `git branch -M main`
    重新命名分支，原先初始化的 branch 是 master，但因為[有一些原因](https://www.ithome.com.tw/news/140094)所以要重新命名成 main
4. `git add .`
    告訴電腦所有這個資料夾變動的檔案都要新增上去
5. `git commit -m "commit message"`
    在自己電腦還有遠端註解一個變動訊息，總是要讓自己知道做了甚麼變動吧
6. `git push -u origin main`
    把檔案推到 main 分支上

> 備註：可以用 `git status` 看有哪些做了改動！

### GitHub desktop

1. 與遠端建立連線

![GitHub desktop init](/GitHub/imgs/github-desktop-init.png)

> 如果電腦上完全沒有任何要上傳的檔案直接按右邊的 your repositories 或是新增一個新的 repository

2. 選擇電腦上的路徑

![GitHub desktop add local repository](/GitHub/imgs/github-desktop-add-local-repository.png)

選完之後就直接 add repository，加完之後應該會長這樣！

![GitHub desktop repository](/GitHub/imgs/github-desktop-repository.png)

> [!NOTE]
> 你可能會發現為甚麼分支是 master，然後我找不到地方改 branch name 欸！？
> 這就是 git command 和桌面版的差別，常常有一些進階操作做不了。

沒關係，這個問題晚點處理，我們先 commit 訊息，在左下角的地方打上你要的 commit 訊息。

> [!IMPORTANT]  
> 所有檔案變更都會在這裡顯示，新增、修改、刪除都會需要 commit。
> 但 commit 和 push 都會是重複的動作，先 commit 再 push。

![GitHub desktop commit](/GitHub/imgs/github-desktop-commit.png)

再來就是推上去！

![GitHub desktop push](/GitHub/imgs/github-desktop-push.png)

回到你的 repository 網頁頁面，推上去了！

![GitHub result but not rename branch](/GitHub/imgs/github-result-unrename-branch.png)

再來的步驟可有可無，但通常我們會重新命名 branch name

![Github rename branch](/GitHub/imgs/github-rename-branch1.png)
![Github rename branch](/GitHub/imgs/github-rename-branch2.png)

再來我們把 branch name 改成 `main`，然後按下 `Rename branch`！

![Github rename branch](/GitHub/imgs/github-rename-branch3.png)

我們成功改 branch 名稱了！

![Github rename branch](/GitHub/imgs/github-rename-branch4.png)