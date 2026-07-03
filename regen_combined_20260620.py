#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重新生成all-articles-combined.txt(包含全部5篇HTML+5篇gzh)"""
import os

WORK_DIR = "/app/data/所有对话/主对话/蓝培医疗文章"
output_dir = os.path.join(WORK_DIR, "2026-06-20")

# 5篇药品的元数据
articles = [
    {'num': '129', 'slug': 'obeticholic-obetohep', 'name': '奥贝胆酸片Obetohep', 'brand': 'Alkem(Cadila Healthcare)', 'indication': 'PBC原发性胆汁性胆管炎'},
    {'num': '130', 'slug': 'valganciclovir-virofil', 'name': '缬更昔洛韦片VIROFIL', 'brand': 'Cadila Healthcare', 'indication': 'CMV巨细胞病毒感染/移植后预防'},
    {'num': '131', 'slug': 'valganciclovir-vagacyte', 'name': '缬更昔洛韦片VAGACYTE', 'brand': 'Panacea Biotec', 'indication': 'CMV巨细胞病毒感染/移植后预防'},
    {'num': '132', 'slug': 'valganciclovir-valgacel', 'name': '缬更昔洛韦片VALGACEL', 'brand': 'Sun Pharma', 'indication': 'CMV巨细胞病毒感染/移植后预防'},
    {'num': '133', 'slug': 'valganciclovir-valgan', 'name': '缬更昔洛韦片Valgan', 'brand': 'Cipla', 'indication': 'CMV巨细胞病毒感染/移植后预防'},
]

# 头部说明
header = '''<!-- 蓝培医疗药品文章合并文件 - 2026-06-20 - 5篇 -->
<!-- 编号:129-133 主题:奥贝胆酸 + 缬更昔洛韦(4家印度厂商) -->
<!-- 联系:微信/电话 17844531559 | WhatsApp +639685838435 -->
<!-- 生成时间:2026-06-20 -->
<!-- 用途:公众号版(规避敏感词:仿制药→海外版本/经济版,代购→咨询渠道) -->

================================================================================
本次5篇药品明细
================================================================================

| 编号 | 药品名 | 厂家 | 适应症 |
|------|--------|------|--------|
'''

for a in articles:
    header += f"| {a['num']} | {a['name']} | {a['brand']} | {a['indication']} |\n"

header += "\n文件构成:\n"
header += "  • 网站版HTML (5个,用于蓝培医疗网站药闻速递分类):\n"
for a in articles:
    header += f"    - news-{a['num']}-{a['slug']}.html\n"
header += "  • 公众号版TXT (5个,用于微信公众号发布):\n"
for a in articles:
    header += f"    - gzh-{a['num']}-{a['slug']}.txt\n"

header += '''
药品列表进度:已covered=129/426(本次新增5个)
下一批起始序号:134
网站地址:https://lanpeimed.com
'''

# 合并内容
content_parts = [header]
content_parts.append("\n" + "="*80)
content_parts.append("【第一部分:网站版HTML - 5篇】")
content_parts.append("="*80 + "\n")

for a in articles:
    html_path = os.path.join(WORK_DIR, f"news-{a['num']}-{a['slug']}.html")
    if os.path.exists(html_path) and os.path.getsize(html_path) > 0:
        content_parts.append(f"\n{'='*80}")
        content_parts.append(f"<!-- 网站版HTML: news-{a['num']}-{a['slug']}.html -->")
        content_parts.append(f"{'='*80}\n")
        with open(html_path, 'r', encoding='utf-8') as f:
            content_parts.append(f.read())
    else:
        content_parts.append(f"\n<!-- 警告:news-{a['num']}-{a['slug']}.html 不存在或为空 -->")

content_parts.append("\n\n" + "="*80)
content_parts.append("【第二部分:公众号版TXT - 5篇】")
content_parts.append("="*80 + "\n")

for a in articles:
    gzh_path = os.path.join(output_dir, f"gzh-{a['num']}-{a['slug']}.txt")
    if os.path.exists(gzh_path) and os.path.getsize(gzh_path) > 0:
        content_parts.append(f"\n{'-'*80}")
        with open(gzh_path, 'r', encoding='utf-8') as f:
            content_parts.append(f.read())
    else:
        content_parts.append(f"\n<!-- 警告:gzh-{a['num']}-{a['slug']}.txt 不存在或为空 -->")

content_parts.append("\n" + "="*80)
content_parts.append("【合并文件结束】")
content_parts.append("="*80 + "\n")

# 写入文件
combined_path = os.path.join(WORK_DIR, "all-articles-combined.txt")
with open(combined_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(content_parts))

print(f"✅ 已重新生成合并文件: {combined_path}")
print(f"   大小: {os.path.getsize(combined_path)} bytes")

# 验证内容完整性
with open(combined_path, 'r', encoding='utf-8') as f:
    combined_content = f.read()
print(f"\n📊 内容验证:")
for a in articles:
    html_marker = f"网站版HTML: news-{a['num']}-{a['slug']}.html"
    gzh_marker = f"news-{a['num']}-{a['slug']}-gzh.txt"
    html_ok = html_marker in combined_content
    gzh_ok = gzh_marker in combined_content
    print(f"  news-{a['num']}: HTML={'✓' if html_ok else '✗'}  GZH={'✓' if gzh_ok else '✗'}")
