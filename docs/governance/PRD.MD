# 开门十件事（The Daily Ten）— 产品需求说明（PRD）

## 1. 项目定位

- **目标**：为同事提供可在线浏览的站点，使用 **Streamlit** 部署，集中展示 `docs/assets` 目录下全部口播稿 Markdown。
- **公开仓库**：[The-Daily-Ten](https://github.com/AiroGriefwind/The-Daily-Ten)

## 2. 内容与顺序

- **来源**：`docs/assets/*.md`（十篇主题稿）。
- **固定展示顺序**（不得按文件名排序打乱）：
  1. 柴 → 2. 米 → 3. 油 → 4. 盐 → 5. 酱 → 6. 醋 → 7. 茶 → 8. 糖 → 9. 酒 → 10. 辣椒  
- **对应文件名**：`chai-firewood.md`、`mi-rice.md`、`you-oil.md`、`yan-salt.md`、`jiang-sauce.md`、`cu-vinegar.md`、`cha-tea.md`、`tang-sugar.md`、`jiu-alcohol.md`、`lajiao-chili.md`。

## 3. 功能需求（Streamlit 站点）

| 需求 | 说明 |
|------|------|
| 首页筛选 | 提供选择器（如 `selectbox`），让用户从上述十篇中选一篇。 |
| 双板块 | **左栏**：文案（口播稿，即从文稿开头到「## 歷史事實」标题之前的全部内容）。**右栏**：历史事实验证（从「## 歷史事實」标题起的区块）。 |
| 可点击 URL | 历史事实区块内所有 `http(s)://` 链接须可在页面中点击打开；已为 Markdown `[文字](url)` 的保持不变；裸露 URL 需自动转为可点击链接。 |

说明：**不在** Streamlit 页面内嵌入 GitHub 仓库入口；协作方通过本文「公开仓库」一节获取仓库地址即可。

## 4. 文稿结构约定（解析依赖）

- 每篇须包含二级标题 **`## 歷史事實`**（当前文稿为繁体），作为「文案」与「历史事实」的分界；若将来使用简体等别名，须在应用代码中维护别名列表。
- 「文案部分」建议维持 **`## 文案部分（粵語口播…）`** 等现有格式，便于人工阅读（程序以「歷史事實」标题为切分点）。

## 5. 技术栈与入口

- **本地运行**：`streamlit run streamlit_app.py`
- **依赖**：根目录 `requirements.txt`（至少包含 `streamlit`）。
- **线上部署**：可使用 [Streamlit Community Cloud](https://streamlit.io/cloud) 等，绑定本仓库并指定主文件为 `streamlit_app.py`。

## 6. 治理与协作

- **PRD（本文件）**：记录当前共识需求；需求变更时更新本文。
- **PROGRESS（`docs/governance/PROGRESS.MD`）**：**每次 push 前**，将自上次 push 以来的进度与变更摘要写入该文件，便于 LLM 与同事在编程前快速上手。
- **建议工作流**：新会话或新任务开始前，先阅读 `PRD.MD` 与 `PROGRESS.MD`。

## 7. 非目标（当前版本）

- 不强制账号、权限或后台编辑器；内容以 Git 管理 Markdown 为主。
- 不承诺多语言 UI（界面以中文为主，与文稿一致即可）。
