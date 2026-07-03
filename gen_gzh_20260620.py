#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成公众号版txt文章 + 合并邮件附件txt - 2026-06-20"""

import os

WORK_DIR = "/app/data/所有对话/主对话/蓝培医疗文章"
output_dir = os.path.join(WORK_DIR, "2026-06-20")
os.makedirs(output_dir, exist_ok=True)

# 公众号版文章 - 规避敏感词:仿制药→海外版本/经济版,代购→咨询渠道
# 文末引导加微信17844531559
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

# ============ 5篇公众号文章 ============
articles = [
    {
        'num': '129',
        'slug': 'obeticholic-obetohep',
        'drug_name': '奥贝胆酸片 Obetohep',
        'drug_short': '奥贝胆酸',
        'subtitle_short': 'PBC原发性胆汁性胆管炎二线靶向治疗',
        'drug_desc': '''全球首个获批的法尼醇X受体(FXR)激动剂,印度Alkem仿制版Obetohep,成分与原研Ocaliva基本一致。作为PBC二线治疗选择,通过激活FXR调节胆汁酸代谢、抑制CYP7A1减少胆汁酸合成、促进胆汁排泄,改善胆汁淤积。''',
        'indications_text': '''• 适用于对熊去氧胆酸(UDCA)应答不足或不耐受的原发性胆汁性胆管炎(PBC)成人患者
• 可与UDCA联合使用,也可单药治疗UDCA不耐受者
• 仅限无肝硬化或代偿期肝硬化无门静脉高压证据的患者使用;失代偿期肝硬化禁用''',
        'dosage_text': '''• 起始剂量5mg,每日一次,口服
• 治疗3个月后评估ALP和总胆红素:若应答不佳且耐受良好,可增至10mg/天(最大剂量)
• 可与食物同服或空腹服用;与胆汁酸结合树脂(考来烯胺)合用需间隔至少4小时''',
        'price_text': '''• 原研药Ocaliva(Intercept):5mg×30片美国约4881美元/盒(约3.5万元);10mg×30片约5200美元/盒
• 海外经济版(Alkem/Glenmark/Sun/Lupin等多家印度药企):价格约每盒数百至一千多元人民币,经济性显著''',
        'warning_text': '''奥贝胆酸:瘙痒(发生率高达68%)为最常见副作用,剂量依赖性;失代偿期肝硬化患者禁用(FDA黑框警告);需定期监测肝功能、ALP、胆红素;妊娠期/哺乳期禁用;出现肝功能失代偿征象(黄疸加深、腹水、肝性脑病)立即停药'''
    },
    {
        'num': '130',
        'slug': 'valganciclovir-virofil',
        'drug_name': '缬更昔洛韦片 VIROFIL',
        'drug_short': '缬更昔洛韦',
        'subtitle_short': '抗CMV巨细胞病毒感染治疗与移植后预防',
        'drug_desc': '''更昔洛韦(Ganciclovir)的L-缬氨酰酯前体药物,印度Cadila仿制版VIROFIL,经印度药品监管机构批准上市。口服后经肝/肠酯酶迅速水解为活性更昔洛韦,生物利用度约60%,远高于更昔洛韦胶囊;原研药Roche Valcyte万赛维已在100多个国家获批。具有潜在致畸性、致癌性和生殖毒性。''',
        'indications_text': '''• 治疗AIDS(获得性免疫缺陷综合征)患者CMV(巨细胞病毒)视网膜炎
• 预防高危实体器官移植(肾移植、心脏移植、肾-胰腺联合移植)患者CMV疾病
• 儿童:从出生至18岁、接受CMV血清阳性供体器官移植后的预防用药''',
        'dosage_text': '''• CMV视网膜炎诱导治疗:900mg(2片),每日2次,口服,持续21天
• 维持治疗:900mg(2片),每日1次,口服
• 肾移植后预防:900mg,每日1次,移植后10天内开始,持续至200天
• 心脏/肾-胰腺移植预防:900mg,每日1次,移植后10天内开始,持续至100天
• 建议随餐服用以提高生物利用度''',
        'price_text': '''• 原研药Valcyte万赛维(Roche):450mg×60片美国约5000-7000美元/盒(约3.6-5万元)
• 海外经济版(Cipla/Panacea/Cadila等多家印度药企):Valgan(Cipla)450mg×4片/盒约1500印度卢比(约120-130元),VAGACYTE(Panacea)450mg×2片/盒约60元,经济性显著(约原研1/30至1/100)''',
        'warning_text': '''缬更昔洛韦:严重骨髓抑制(中性粒细胞减少发生率15-25%、血小板减少、贫血)是最主要风险;妊娠期绝对禁用(可能导致胎儿严重出生缺陷);基于动物数据可能致癌、影响生育;用药期间及停药后90天内严格避孕;操作药片前后用肥皂水洗手,不可掰开/压碎'''
    },
    {
        'num': '131',
        'slug': 'valganciclovir-vagacyte',
        'drug_name': '缬更昔洛韦片 VAGACYTE',
        'drug_short': '缬更昔洛韦',
        'subtitle_short': '抗CMV巨细胞病毒感染治疗与移植后预防',
        'drug_desc': '''更昔洛韦的L-缬氨酰酯前体药物,印度Panacea Biotec(移植领域专业公司)仿制版VAGACYTE,成分与原研Valcyte一致,在印度移植科应用广泛。口服后经酯酶水解为更昔洛韦,生物利用度约60%。''',
        'indications_text': '''• 治疗AIDS患者CMV(巨细胞病毒)视网膜炎
• 预防高危实体器官移植(肾移植、心脏移植、肾-胰腺联合移植)患者CMV疾病
• 儿童:接受CMV血清阳性供体器官移植后的预防用药''',
        'dosage_text': '''• CMV视网膜炎诱导治疗:900mg(2片),每日2次,口服,持续21天
• 维持治疗:900mg(2片),每日1次,口服
• 肾移植后预防:900mg,每日1次,移植后10天内开始,持续至200天
• 心脏/肾-胰腺移植预防:900mg,每日1次,移植后10天内开始,持续至100天
• 建议随餐服用以提高生物利用度''',
        'price_text': '''• 原研药Valcyte万赛维(Roche):450mg×60片美国约5000-7000美元/盒(约3.6-5万元)
• 海外经济版(印度多家):VAGACYTE(Panacea)450mg×2片/盒MRP约682.50印度卢比(约60元),Valgan(Cipla)450mg×4片/盒约1500印度卢比(约120-130元);经济性显著(约原研1/30至1/100)''',
        'warning_text': '''缬更昔洛韦:严重骨髓抑制(中性粒细胞减少15-25%、血小板减少、贫血)是最主要风险;妊娠期绝对禁用(可能导致胎儿严重出生缺陷);基于动物数据可能致癌、影响生育;用药期间及停药后90天内严格避孕;操作药片前后用肥皂水洗手,不可掰开/压碎'''
    },
    {
        'num': '132',
        'slug': 'valganciclovir-valgacel',
        'drug_name': '缬更昔洛韦片 VALGACEL',
        'drug_short': '缬更昔洛韦',
        'subtitle_short': '抗CMV巨细胞病毒感染治疗与移植后预防',
        'drug_desc': '''更昔洛韦的L-缬氨酰酯前体药物,印度Sun Pharma(全球第四大仿制药公司)仿制版VALGACEL,成分与原研Valcyte基本一致,经印度药品监管机构批准上市。作为全球CMV治疗与移植预防的主流仿制选择。''',
        'indications_text': '''• 治疗AIDS患者CMV(巨细胞病毒)视网膜炎
• 预防高危实体器官移植(肾移植、心脏移植、肾-胰腺联合移植)患者CMV疾病
• 儿童:接受CMV血清阳性供体器官移植后的预防用药''',
        'dosage_text': '''• CMV视网膜炎诱导治疗:900mg(2片),每日2次,口服,持续21天
• 维持治疗:900mg(2片),每日1次,口服
• 肾移植后预防:900mg,每日1次,移植后10天内开始,持续至200天
• 心脏/肾-胰腺移植预防:900mg,每日1次,移植后10天内开始,持续至100天
• 建议随餐服用以提高生物利用度''',
        'price_text': '''• 原研药Valcyte万赛维(Roche):450mg×60片美国约5000-7000美元/盒(约3.6-5万元)
• 海外经济版(印度多家):Valgan(Cipla)450mg×4片/盒约1500印度卢比(约120-130元),VAGACYTE(Panacea)450mg×2片/盒约60元;经济性显著(约原研1/30至1/100)''',
        'warning_text': '''缬更昔洛韦:严重骨髓抑制(中性粒细胞减少15-25%、血小板减少、贫血)是最主要风险;妊娠期绝对禁用(可能导致胎儿严重出生缺陷);基于动物数据可能致癌、影响生育;用药期间及停药后90天内严格避孕;操作药片前后用肥皂水洗手,不可掰开/压碎'''
    },
    {
        'num': '133',
        'slug': 'valganciclovir-valgan',
        'drug_name': '缬更昔洛韦片 Valgan',
        'drug_short': '缬更昔洛韦',
        'subtitle_short': '抗CMV巨细胞病毒感染治疗与移植后预防',
        'drug_desc': '''更昔洛韦的L-缬氨酰酯前体药物,印度Cipla(印度第二大制药企业,全球抗病毒仿制药主要供应商之一)仿制版Valgan,成分与原研Valcyte基本一致,在全球抗HIV/抗病毒仿制市场占据重要地位。''',
        'indications_text': '''• 治疗AIDS患者CMV(巨细胞病毒)视网膜炎
• 预防高危实体器官移植(肾移植、心脏移植、肾-胰腺联合移植)患者CMV疾病
• 儿童:接受CMV血清阳性供体器官移植后的预防用药''',
        'dosage_text': '''• CMV视网膜炎诱导治疗:900mg(2片),每日2次,口服,持续21天
• 维持治疗:900mg(2片),每日1次,口服
• 肾移植后预防:900mg,每日1次,移植后10天内开始,持续至200天
• 心脏/肾-胰腺移植预防:900mg,每日1次,移植后10天内开始,持续至100天
• 建议随餐服用以提高生物利用度''',
        'price_text': '''• 原研药Valcyte万赛维(Roche):450mg×60片美国约5000-7000美元/盒(约3.6-5万元)
• 海外经济版(Cipla/Panacea/Cadila等多家印度药企):Valgan(Cipla)450mg×4片/盒约1500印度卢比(约120-130元),VAGACYTE(Panacea)450mg×2片/盒约60元;经济性显著(约原研1/30至1/100)''',
        'warning_text': '''缬更昔洛韦:严重骨髓抑制(中性粒细胞减少15-25%、血小板减少、贫血)是最主要风险;妊娠期绝对禁用(可能导致胎儿严重出生缺陷);基于动物数据可能致癌、影响生育;用药期间及停药后90天内严格避孕;操作药片前后用肥皂水洗手,不可掰开/压碎'''
    },
]

# 生成每篇公众号版txt
gzh_files = []
for a in articles:
    content = GZH_TPL.format(**a)
    filename = f"gzh-{a['num']}-{a['slug']}.txt"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    gzh_files.append(filepath)
    print(f"生成公众号版: {filename}")

# ============ 合并5篇网站版HTML + 5篇公众号版txt为1个txt文件 ============
combined_filename = "蓝培医疗-药品文章代码-2026-06-20.txt"
combined_path = os.path.join(WORK_DIR, combined_filename)

with open(combined_path, 'w', encoding='utf-8') as combined:
    # 头部说明
    combined.write(f"<!-- 蓝培医疗药品文章合并文件 - 2026-06-20 - 5篇 -->\n")
    combined.write(f"<!-- 编号:129-133 主题:奥贝胆酸 + 缬更昔洛韦(4家印度厂商) -->\n")
    combined.write(f"<!-- 联系:微信/电话 17844531559 | WhatsApp +639685838435 -->\n")
    combined.write(f"<!-- 生成时间:2026-06-20 -->\n\n")

    # 5篇网站版HTML
    for d in articles:
        combined.write(f"\n\n{'='*80}\n")
        combined.write(f"<!-- 网站版HTML: news-{d['num']}-{d['slug']}.html -->\n")
        combined.write(f"{'='*80}\n\n")
        html_filepath = os.path.join(WORK_DIR, f"news-{d['num']}-{d['slug']}.html")
        with open(html_filepath, 'r', encoding='utf-8') as f:
            combined.write(f.read())
        combined.write(f"\n\n<!-- END news-{d['num']}-{d['slug']}.html -->\n")

    # 5篇公众号版txt
    for a in articles:
        combined.write(f"\n\n{'='*80}\n")
        combined.write(f"<!-- 公众号版TXT: gzh-{a['num']}-{a['slug']}.txt -->\n")
        combined.write(f"{'='*80}\n\n")
        gzh_filepath = os.path.join(output_dir, f"gzh-{a['num']}-{a['slug']}.txt")
        with open(gzh_filepath, 'r', encoding='utf-8') as f:
            combined.write(f.read())
        combined.write(f"\n\n<!-- END gzh-{a['num']}-{a['slug']}.txt -->\n")

print(f"\n合并文件: {combined_path}")
print(f"文件大小: {os.path.getsize(combined_path)} bytes")
