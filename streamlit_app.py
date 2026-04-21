"""
开门十件事 — Markdown 浏览（Streamlit）
从 docs/assets 按固定顺序加载十篇内容，分「文案」与「历史事实验证」两栏展示。
"""

from __future__ import annotations

import re
from pathlib import Path

import streamlit as st

# 柴、米、油、盐、酱、醋、茶、糖、酒、辣椒（与文稿标题用字一致：盐/酱 等）
ASSET_ORDER: list[tuple[str, str]] = [
    ("chai-firewood.md", "柴"),
    ("mi-rice.md", "米"),
    ("you-oil.md", "油"),
    ("yan-salt.md", "盐"),
    ("jiang-sauce.md", "酱"),
    ("cu-vinegar.md", "醋"),
    ("cha-tea.md", "茶"),
    ("tang-sugar.md", "糖"),
    ("jiu-alcohol.md", "酒"),
    ("lajiao-chili.md", "辣椒"),
]

HISTORY_HEADING = "## 歷史事實"
# 若文稿标题改写，在此扩展别名
HISTORY_ALIASES = ("## 历史事实", "## 歷史事實驗證", "## 历史事实验证")


def _assets_dir() -> Path:
    return Path(__file__).resolve().parent / "docs" / "assets"


def _split_copy_and_history(raw: str) -> tuple[str, str]:
    text = raw.replace("\r\n", "\n")
    cut = -1
    for alias in (HISTORY_HEADING,) + HISTORY_ALIASES:
        idx = text.find(alias)
        if idx != -1:
            cut = idx
            break
    if cut == -1:
        return text.strip(), ""
    return text[:cut].strip(), text[cut:].strip()


_BARE_URL = re.compile(r"(?<!\]\()((?:https?://)[^\s\]<>`]+)")


def linkify_bare_urls(md: str) -> str:
    """将未被 `[]()` 包裹的 http(s) 转为可点击的 Markdown 链接。"""

    def repl(m: re.Match[str]) -> str:
        url = m.group(1)
        tail = ""
        while url and url[-1] in ".,;:!?)」』\"'":
            tail = url[-1] + tail
            url = url[:-1]
        return f"[{url}]({url}){tail}"

    return _BARE_URL.sub(repl, md)


@st.cache_data(show_spinner=False)
def load_article(filename: str) -> tuple[str, str]:
    path = _assets_dir() / filename
    if not path.is_file():
        return f"找不到文件：`{filename}`", ""
    raw = path.read_text(encoding="utf-8")
    copy_part, hist_part = _split_copy_and_history(raw)
    return copy_part, linkify_bare_urls(hist_part)


def main() -> None:
    st.set_page_config(
        page_title="开门十件事",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.title("开门十件事")

    labels = [f"{label}（{fn}）" for fn, label in ASSET_ORDER]
    choice_idx = st.selectbox(
        "筛选：选择一篇",
        range(len(ASSET_ORDER)),
        format_func=lambda i: labels[i],
        key="article_pick",
    )

    filename, _ = ASSET_ORDER[choice_idx]
    copy_md, hist_md = load_article(filename)

    st.divider()

    left, right = st.columns(2, gap="large")

    with left:
        st.subheader("文案")
        if copy_md:
            st.markdown(copy_md)
        else:
            st.info("此文件暂无文案区块。")

    with right:
        st.subheader("历史事实验证")
        if hist_md:
            st.markdown(hist_md)
        else:
            st.info("未检测到「## 歷史事實」标题；请检查 Markdown 结构。")


if __name__ == "__main__":
    main()
