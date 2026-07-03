#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新药品列表covered状态 - 2026-06-22批次（139-143）"""

import json
import os

os.chdir("/app/data/所有对话/主对话/蓝培医疗文章")

# 5个已覆盖的药品
covered_drugs = [
    "博舒替尼片 Bosuvi",
    "博舒替尼片 BONITAR",
    "依普利酮片 EPLECARD",
    "依普利酮片 EPTUS",
    "依普利酮片 EXENTA",
]

with open('药品列表.json', 'r', encoding='utf-8') as f:
    drugs = json.load(f)

updated_count = 0
for drug in drugs:
    if drug['name'] in covered_drugs and not drug.get('covered'):
        drug['covered'] = True
        updated_count += 1
        print(f"  ✓ {drug['name']} -> covered=true")

print(f"\n更新 {updated_count} 个药品")

with open('药品列表.json', 'w', encoding='utf-8') as f:
    json.dump(drugs, f, ensure_ascii=False, indent=2)

# 验证
total = len(drugs)
covered = sum(1 for d in drugs if d.get('covered'))
print(f"当前进度: covered={covered}/{total}")
