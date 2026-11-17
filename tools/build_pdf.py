#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成《文明重启手册》整本 PDF（中文 / 英文）。

流程：mkdocs.yml（或 mkdocs-en.yml）的 nav → 按顺序读 md → python-markdown → weasyprint → PDF
输出：dist/reboot-manual-zh-v{ver}.pdf 与 dist/reboot-manual-en-v{ver}.pdf

用法：
    ~/aging-manual-book/.venv/bin/python tools/build_pdf.py [--lang zh|en|both]
"""
from __future__ import annotations

import argparse
import datetime
import os
import re
import sys

import markdown
import yaml
from weasyprint import CSS, HTML

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LANGS = {
    "zh": dict(
        cfg="mkdocs.yml", root="book", out="reboot-manual-zh",
        title="文明重启手册", sub="工业文明断档之后，怎么从一块石头重新走到电",
        toc="目 录", font_body='"Noto Serif SC","Noto Serif CJK SC",serif',
        font_head='"Noto Sans SC","Noto Sans CJK SC",sans-serif',
        lang="zh-Hans", disclaimer=(
            "本 PDF 与线上版本同源，内容为公开出版物，CC BY-NC-SA 4.0：可自由阅读、转载、改编，"
            "须署名、非商业、同样方式共享。<br>修订以新版发布；发现问题请提 issue：github.com/Jweokk/civilization-restart-manual"),
        running="文明重启手册",
    ),
    "en": dict(
        cfg="mkdocs-en.yml", root="book-en", out="reboot-manual-en",
        title="The Civilization Restart Manual",
        sub="From a single stone back to electricity",
        toc="Contents", font_body='"Noto Serif SC","Noto Serif CJK SC",serif',
        font_head='"Noto Sans SC","Noto Sans CJK SC",sans-serif',
        lang="en", disclaimer=(
            "This PDF shares its source with the online edition. CC BY-NC-SA 4.0: read, repost and adapt freely, "
            "with attribution, non-commercially, under the same licence.<br>Corrections ship with the next edition: "
            "github.com/Jweokk/civilization-restart-manual"),
        running="The Civilization Restart Manual",
    ),
}

CSS_TEXT = """
@page {
  size: A4;
  margin: 17mm 16mm 18mm 16mm;
  @top-center { content: "%(running)s"; font: 8pt %(head)s; color: #888; }
  @bottom-center { content: counter(page); font: 8.5pt %(body)s; color: #555; }
}
@page cover { margin: 0; @top-center { content: none } @bottom-center { content: none } }
html { font-family: %(body)s; font-size: 9.8pt; line-height: 1.62; color: #111; }
body { margin: 0; hyphens: auto; }
.cover { page: cover; height: 297mm; padding: 62mm 24mm 0 24mm; box-sizing: border-box;
         background: #f7f5ef; text-align: center; }
.cover h1 { font-family: %(head)s; font-size: 34pt; margin: 0 0 10mm 0; letter-spacing: 2px; }
.cover .sub { font-size: 12pt; color: #444; line-height: 1.8; }
.cover .meta { position: absolute; bottom: 30mm; left: 24mm; right: 24mm;
               font-size: 8.5pt; color: #666; line-height: 1.7; text-align: left; }
.toc { page-break-after: always; }
.toc h1 { font-family: %(head)s; font-size: 18pt; margin: 0 0 6mm 0; }
.toc ul { list-style: none; padding: 0; margin: 0; }
.toc li { margin: 0; }
.toc .part { font-family: %(head)s; font-weight: 700; font-size: 10.5pt; margin: 4.2mm 0 1mm 0; }
.toc .ch { font-size: 9.4pt; padding-left: 4mm; }
.toc a { color: #111; text-decoration: none; }
.toc a::after { content: leader('.') target-counter(attr(href), page); color: #666; }
section.doc { page-break-before: always; }
section.doc h1 { font-family: %(head)s; font-size: 19pt; line-height: 1.35; margin: 0 0 7mm 0;
                 padding-bottom: 3mm; border-bottom: 1.2px solid #ccd; }
h2 { font-family: %(head)s; font-size: 13pt; margin: 7mm 0 2.5mm 0; page-break-after: avoid; }
h3 { font-family: %(head)s; font-size: 11pt; margin: 5mm 0 2mm 0; page-break-after: avoid; }
h4 { font-family: %(head)s; font-size: 10pt; margin: 4mm 0 1.5mm 0; page-break-after: avoid; }
p { margin: 0 0 2.6mm 0; text-align: justify; }
ul, ol { margin: 0 0 2.6mm 0; padding-left: 6mm; }
li { margin: 0 0 1.2mm 0; }
strong { font-weight: 700; }
table { width: 100%%; border-collapse: collapse; margin: 2mm 0 3.6mm 0;
        font-size: 8.6pt; page-break-inside: auto; }
th, td { border: 0.5px solid #bbb; padding: 1.3mm 1.6mm; vertical-align: top; text-align: left; }
th { background: #efeee8; font-family: %(head)s; font-weight: 700; }
tr { page-break-inside: avoid; }
blockquote { margin: 3mm 0; padding: 2mm 0 2mm 4mm; border-left: 2px solid #ccd; color: #333;
             font-size: 9.3pt; }
code, pre { font-family: "Noto Sans Mono", monospace; font-size: 8.4pt; }
pre { background: #f6f6f3; padding: 2.5mm; border: 0.5px solid #ddd; white-space: pre-wrap;
      page-break-inside: avoid; }
hr { border: none; border-top: 0.6px solid #ddd; margin: 4mm 0; }
.small { font-size: 8.4pt; color: #666; }
"""


def load_nav(cfg_path):
    cfg = yaml.safe_load(open(cfg_path, encoding="utf-8"))
    items, part = [], None
    for entry in cfg.get("nav", []):
        for label, target in entry.items():
            if isinstance(target, list):
                part = label
                items.append(("part", label, None))
                for e in target:
                    for lab, tg in e.items():
                        items.append(("ch", lab, tg))
            else:
                items.append(("ch", label, target))
    return items


def md_to_html(text):
    return markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html"],
        output_format="html5",
    )


def strip_first_h1(md_text):
    return re.sub(r"^#\s+.*?\n", "", md_text, count=1, flags=re.M)


def build(lang, version):
    M = LANGS[lang]
    root = os.path.join(BASE, M["root"])
    nav = load_nav(os.path.join(BASE, M["cfg"]))
    today = datetime.date.today().isoformat()

    slug = lambda i: f"doc{i}"
    toc_rows, body = [], []
    i = 0
    for kind, label, target in nav:
        if kind == "part":
            toc_rows.append(f'<li class="part">{label}</li>')
            continue
        path = os.path.join(root, target)
        if not os.path.exists(path):
            print("  ! missing", target, file=sys.stderr)
            continue
        md = strip_first_h1(open(path, encoding="utf-8").read())
        body.append(f'<section class="doc" id="{slug(i)}"><h1>{label}</h1>{md_to_html(md)}</section>')
        toc_rows.append(f'<li class="ch"><a href="#{slug(i)}">{label}</a></li>')
        i += 1

    cover = f"""<div class="cover">
  <h1>{M['title']}</h1>
  <div class="sub">{M['sub']}</div>
  <div class="meta">v{version} · {today} · Jweokk<br>{M['disclaimer']}</div>
</div>"""
    toc = f'<div class="toc"><h1>{M["toc"]}</h1><ul>{"".join(toc_rows)}</ul></div>'
    html = f"<html lang=\"{M['lang']}\"><body>{cover}{toc}{''.join(body)}</body></html>"

    css = CSS(string=CSS_TEXT % dict(running=M["running"], head=M["font_head"], body=M["font_body"]))
    outdir = os.path.join(BASE, "dist")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f"{M['out']}-v{version}.pdf")
    HTML(string=html, base_url=root).write_pdf(out, stylesheets=[css])
    size = os.path.getsize(out) / 1e6
    print(f"{lang}: {len(body)} docs → {out}  ({size:.1f} MB)")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="both", choices=["zh", "en", "both"])
    a = ap.parse_args()
    version = open(os.path.join(BASE, "VERSION"), encoding="utf-8").read().strip()
    langs = ["zh", "en"] if a.lang == "both" else [a.lang]
    for lg in langs:
        build(lg, version)


if __name__ == "__main__":
    main()
