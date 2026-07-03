#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
合并5篇HTML + 5篇公众号txt到1个txt文件
- 附件必须是代码（HTML注释标记文件名），不能有说明文字
"""
import os

ROOT = '/app/data/所有对话/主对话/蓝培医疗文章'
OUT_DIR = os.path.join(ROOT, '20260623-药品文章')

html_files = [
    'news-144-febuxostat.html',
    'news-145-pirfenidone.html',
    'news-146-nintedanib-cipla.html',
    'news-147-nintedanib-sun.html',
    'news-148-deferasirox.html',
]

wechat_files = [
    'wechat-news-144-febuxostat.txt',
    'wechat-news-145-pirfenidone.txt',
    'wechat-news-146-nintedanib-cipla.txt',
    'wechat-news-147-nintedanib-sun.txt',
    'wechat-news-148-deferasirox.txt',
]

output_path = os.path.join(OUT_DIR, '20260623-药品文章合并.txt')

with open(output_path, 'w', encoding='utf-8') as out:
    # 第一部分：5个网站版HTML
    for filename in html_files:
        path = os.path.join(ROOT, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        out.write(f'<!-- {filename} -->\n')
        out.write(content)
        out.write('\n')

    # 分隔
    out.write('\n\n')

    # 第二部分：5个公众号版txt
    for filename in wechat_files:
        path = os.path.join(OUT_DIR, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        out.write(f'<!-- {filename} -->\n')
        out.write(content)
        out.write('\n\n')

print(f"已生成合并文件: {output_path}")
print(f"大小: {os.path.getsize(output_path)} 字节")
