#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并5个HTML + 5个公众号txt为1个txt文件 - 2026-06-22批次（139-143）"""

import os
os.chdir("/app/data/所有对话/主对话/蓝培医疗文章")

# 5个HTML文件
html_files = [
    "news-139-bosuvi.html",
    "news-140-bonitar.html",
    "news-141-eplecard.html",
    "news-142-eptus.html",
    "news-143-exenta.html",
]

# 5个公众号文件
gzh_files = [
    "gzh-139-bosuvi.txt",
    "gzh-140-bonitar.txt",
    "gzh-141-eplecard.txt",
    "gzh-142-eptus.txt",
    "gzh-143-exenta.txt",
]

# 合并
combined = ""
combined += "=" * 60 + "\n"
combined += "蓝培医疗-每日药品文章生成 - 2026-06-22\n"
combined += "=" * 60 + "\n\n"

combined += "=" * 60 + "\n"
combined += "第一部分：网站版HTML文件 (5个)\n"
combined += "=" * 60 + "\n\n"

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    combined += f"<!-- FILE: {f} -->\n{content}\n\n"

combined += "\n\n"
combined += "=" * 60 + "\n"
combined += "第二部分：公众号版TXT文件 (5个)\n"
combined += "=" * 60 + "\n\n"

for f in gzh_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    combined += f"<!-- FILE: {f} -->\n{content}\n\n"

with open("蓝培医疗-药品文章代码-2026-06-22.txt", "w", encoding="utf-8") as f:
    f.write(combined)

print(f"合并文件生成完毕: 蓝培医疗-药品文章代码-2026-06-22.txt ({len(combined)} 字符)")
