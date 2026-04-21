"""
開門十件事 — Markdown 瀏覽（Streamlit）
從 docs/assets 按固定順序載入十篇內容，分「文案」與「歷史事實驗證」兩欄展示。
"""

from __future__ import annotations

import io
import re
import zipfile
from pathlib import Path

import streamlit as st

# 柴、米、油、鹽、醬、醋、茶、糖、酒、辣椒（介面用字：繁體）
ASSET_ORDER: list[tuple[str, str]] = [
    ("chai-firewood.md", "柴"),
    ("mi-rice.md", "米"),
    ("you-oil.md", "油"),
    ("yan-salt.md", "鹽"),
    ("jiang-sauce.md", "醬"),
    ("cu-vinegar.md", "醋"),
    ("cha-tea.md", "茶"),
    ("tang-sugar.md", "糖"),
    ("jiu-alcohol.md", "酒"),
    ("lajiao-chili.md", "辣椒"),
]

HISTORY_HEADING = "## 歷史事實"
# 若文稿標題改寫，在此擴展別名
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
    """將未被 `[]()` 包裹的 http(s) 轉成可點擊的 Markdown 連結。"""

    def repl(m: re.Match[str]) -> str:
        url = m.group(1)
        tail = ""
        while url and url[-1] in ".,;:!?)」』\"'":
            tail = url[-1] + tail
            url = url[:-1]
        return f"[{url}]({url}){tail}"

    return _BARE_URL.sub(repl, md)


def _article_raw_bytes(filename: str) -> bytes | None:
    path = _assets_dir() / filename
    if not path.is_file():
        return None
    return path.read_bytes()


def _zip_all_articles() -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for fn, _ in ASSET_ORDER:
            raw = _article_raw_bytes(fn)
            if raw is not None:
                zf.writestr(fn, raw)
    buf.seek(0)
    return buf.getvalue()


@st.cache_data(show_spinner=False)
def load_article(filename: str) -> tuple[str, str]:
    path = _assets_dir() / filename
    if not path.is_file():
        return f"找不到檔案：`{filename}`", ""
    raw = path.read_text(encoding="utf-8")
    copy_part, hist_part = _split_copy_and_history(raw)
    return copy_part, linkify_bare_urls(hist_part)


def main() -> None:
    st.set_page_config(
        page_title="開門十件事",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.title("開門十件事")

    labels = [f"{label}（{fn}）" for fn, label in ASSET_ORDER]
    choice_idx = st.selectbox(
        "篩選：選擇一篇",
        range(len(ASSET_ORDER)),
        format_func=lambda i: labels[i],
        key="article_pick",
    )

    filename, _ = ASSET_ORDER[choice_idx]
    one_bytes = _article_raw_bytes(filename)
    col_dl1, col_dl2 = st.columns(2)
    with col_dl1:
        st.download_button(
            label="下載本篇",
            data=one_bytes if one_bytes is not None else b"",
            file_name=filename,
            mime="text/markdown; charset=utf-8",
            disabled=one_bytes is None,
            key="dl_one",
        )
    with col_dl2:
        st.download_button(
            label="下載全部",
            data=_zip_all_articles(),
            file_name="開門十件事_全部文稿.zip",
            mime="application/zip",
            key="dl_all",
        )

    copy_md, hist_md = load_article(filename)

    st.divider()

    left, right = st.columns(2, gap="large")

    with left:
        st.subheader("文案")
        if copy_md:
            st.markdown(copy_md)
        else:
            st.info("此檔案暫無文案區塊。")

    with right:
        st.subheader("歷史事實驗證")
        if hist_md:
            st.markdown(hist_md)
        else:
            st.info("未偵測到「## 歷史事實」標題；請檢查 Markdown 結構。")


if __name__ == "__main__":
    main()
