#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并5篇网站版HTML + 5篇公众号版txt为1个txt文件"""
import os

OUT_DIR = "./蓝培医疗文章/news-batch/2026-06-14"
HTML_DIR = "./蓝培医疗文章"
DRUGS = [
    ("094", "pirfeni", "吡非尼酮"),
    ("095", "sora", "甲苯磺酸索拉非尼片"),
    ("096", "ribo", "琥珀酸瑞波西利片"),
    ("097", "dasa", "达沙替尼片"),
    ("098", "stir", "司替戊醇"),
]

# 合并文件
combined_path = os.path.join(OUT_DIR, "蓝培医疗文章代码-2026-06-14.txt")
with open(combined_path, 'w', encoding='utf-8') as out:
    out.write("=" * 60 + "\n")
    out.write("蓝培医疗药品文章合并文件 - 2026-06-14\n")
    out.write("序号：094-098（5篇）\n")
    out.write("=" * 60 + "\n\n")
    
    for num, pinyin, name in DRUGS:
        # 网站版HTML
        html_filename = f"news-{num}-{pinyin}.html"
        html_path = os.path.join(HTML_DIR, html_filename)
        if os.path.exists(html_path):
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            out.write("\n" + "=" * 60 + "\n")
            out.write(f"=== 网站版HTML: {html_filename} - {name} ===\n")
            out.write("=" * 60 + "\n")
            out.write(html_content)
            out.write("\n")
        
        # 公众号版txt
        gzh_filename = f"gzh-{num}-{pinyin}.txt"
        gzh_path = os.path.join(OUT_DIR, gzh_filename)
        if os.path.exists(gzh_path):
            with open(gzh_path, 'r', encoding='utf-8') as f:
                gzh_content = f.read()
            out.write("\n" + "=" * 60 + "\n")
            out.write(f"=== 公众号版: {gzh_filename} - {name} ===\n")
            out.write("=" * 60 + "\n")
            out.write(gzh_content)
            out.write("\n")

print(f"✅ 合并文件: {combined_path}")
print(f"   文件大小: {os.path.getsize(combined_path)} bytes")
