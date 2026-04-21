# 进度记录（每次 push 前更新）

> 约定：每次 **push 前** 在顶部新增一节，简述「自上次 push 以来」的变更与状态。

---

## 2026-04-21（自 `4aecf66` 以来）

### 已完成

- Streamlit **全部界面用字**改为**繁体中文**（标题、筛选、分栏标题、提示信息；篇章标签为鹽／醬等繁体）。
- 筛选器下方新增 **下載本篇**、**下載全部** 两个下载按钮（本篇为当前选中的 `docs/assets` 原始 `.md`；全部为十篇 zip，默认文件名 `開門十件事_全部文稿.zip`，包内文件名与仓库一致）。
- **`docs/governance/PRD.MD`**：补充「下载」与「界面繁体」需求条目。

---

## 2026-04-21（自 `3b9c79b` 以来）

### 已完成

- Streamlit 页：移除副标题说明「供同事在线浏览：口播文案与历史事实验证对照」。
- Streamlit 页：移除顶部「GitHub 仓库（The-Daily-Ten）」链接区块；筛选器单独占满顶栏区域。
- **`docs/governance/PRD.MD`**：同步删除「页面须展示 GitHub 仓库入口」的产品要求，避免与实现不一致。

---

## 2026-04-21（自 `ec23b47` initialzing repo 以来）

### 已完成

- 新增 **Streamlit** 应用 `streamlit_app.py`：按「柴→米→油→盐→酱→醋→茶→糖→酒→辣椒」顺序加载 `docs/assets` 下十篇 `.md`。
- 首页 **筛选器**（`selectbox`）切换篇章；主区 **双栏**：左「文案」、右「历史事实验证」；以文稿中的 `## 歷史事實` 为分界解析。
- 历史区块对 **裸露 http(s) URL** 做自动链转写，与已有 Markdown 链接并存，保证可点击。
- 新增 `requirements.txt`（声明 `streamlit` 依赖）。
- 撰写 **`docs/governance/PRD.MD`**（需求总览）并建立本 **`PROGRESS.MD`** 的首条进度。

### 后续 / 部署

- 若要公网访问，需将仓库部署到 Streamlit Cloud（或同类托管），入口指定 `streamlit_app.py`，并安装 `requirements.txt` 中的依赖。

### 同次迭代补充

- 添加根目录 `.gitignore`（忽略 `__pycache__` 等），避免本地运行 Streamlit 时产生缓存文件被误提交。
