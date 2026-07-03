#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全gzh-129文件(原文件0字节)"""
import os

WORK_DIR = "/app/data/所有对话/主对话/蓝培医疗文章"
output_dir = os.path.join(WORK_DIR, "2026-06-20")
os.makedirs(output_dir, exist_ok=True)

GZH_TPL = '''<!-- FILE: news-{num}-{slug}-gzh.txt -->
【{drug_name}】用法用量详解 | {subtitle_short}

🔹什么是{drug_short}？

{drug_desc}

🔹适应症

{indications_text}

🔹用法用量

{dosage_text}

🔹价格参考

{price_text}

*参考价格,实际以咨询为准

🔹注意事项

⚠️ {warning_text}

📞 专业咨询
蓝培医疗帮您了解{drug_short}的全球用药渠道,合规获取全球优质医疗资源。

微信咨询:17844531559
电话:17844531559
WhatsApp:+639685838435

---
免责声明:本文仅供信息参考,不构成医疗建议。药品为处方药,请务必在专业医生指导下使用。如有用药需求,请先咨询主治医生。
'''

article = {
    'num': '129',
    'slug': 'obeticholic-obetohep',
    'drug_name': '奥贝胆酸片 Obetohep',
    'drug_short': '奥贝胆酸',
    'subtitle_short': 'PBC原发性胆汁性胆管炎二线靶向治疗',
    'drug_desc': '全球首个获批的法尼醇X受体(FXR)激动剂,印度Alkem仿制版Obetohep,成分与原研Ocaliva基本一致。作为PBC二线治疗选择,通过激活FXR调节胆汁酸代谢、抑制CYP7A1减少胆汁酸合成、促进胆汁排泄,改善胆汁淤积。',
    'indications_text': '• 适用于对熊去氧胆酸(UDCA)应答不足或不耐受的原发性胆汁性胆管炎(PBC)成人患者\n• 可与UDCA联合使用,也可单药治疗UDCA不耐受者\n• 仅限无肝硬化或代偿期肝硬化无门静脉高压证据的患者使用;失代偿期肝硬化禁用',
    'dosage_text': '• 起始剂量5mg,每日一次,口服\n• 治疗3个月后评估ALP和总胆红素:若应答不佳且耐受良好,可增至10mg/天(最大剂量)\n• 可与食物同服或空腹服用;与胆汁酸结合树脂(考来烯胺)合用需间隔至少4小时',
    'price_text': '• 原研药Ocaliva(Intercept):5mg×30片美国约4881美元/盒(约3.5万元);10mg×30片约5200美元/盒\n• 海外经济版(Alkem/Glenmark/Sun/Lupin等多家印度药企):价格约每盒数百至一千多元人民币,经济性显著',
    'warning_text': '奥贝胆酸:瘙痒(发生率高达68%)为最常见副作用,剂量依赖性;失代偿期肝硬化患者禁用(FDA黑框警告);需定期监测肝功能、ALP、胆红素;妊娠期/哺乳期禁用;出现肝功能失代偿征象(黄疸加深、腹水、肝性脑病)立即停药'
}

content = GZH_TPL.format(**article)
filepath = os.path.join(output_dir, f"gzh-{article['num']}-{article['slug']}.txt")
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# 验证
print(f"✅ 已重新生成: {filepath}")
print(f"   大小: {os.path.getsize(filepath)} bytes")
