# 进度记录（每次 push 前更新）

> 约定：每次 **push 前** 在顶部新增一节，简述「自上次 push 以来」的变更与状态。

---

## 2026-04-21（自 `ec23b47` initialzing repo 以来）

### 已完成

- 新增 **Streamlit** 应用 `streamlit_app.py`：按「柴→米→油→盐→酱→醋→茶→糖→酒→辣椒」顺序加载 `docs/assets` 下十篇 `.md`。
- 首页 **筛选器**（`selectbox`）切换篇章；主区 **双栏**：左「文案」、右「历史事实验证」；以文稿中的 `## 歷史事實` 为分界解析。
- 历史区块对 **裸露 http(s) URL** 做自动链转写，与已有 Markdown 链接并存，保证可点击。
- 页面提供可点击的 **GitHub 仓库** 链接：[The-Daily-Ten](https://github.com/AiroGriefwind/The-Daily-Ten)。
- 新增 `requirements.txt`（声明 `streamlit` 依赖）。
- 撰写 **`docs/governance/PRD.MD`**（需求总览）并建立本 **`PROGRESS.MD`** 的首条进度。

### 后续 / 部署

- 若要公网访问，需将仓库部署到 Streamlit Cloud（或同类托管），入口指定 `streamlit_app.py`，并安装 `requirements.txt` 中的依赖。
