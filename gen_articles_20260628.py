import json
import re
from datetime import datetime

# 药品数据
drugs_data = [
    {
        "name": "非布司他片",
        "brand": "Intas",
        "pinyin": "febutax",
        "seq": 140,
        "category": "痛风/高尿酸血症",
        "indication": "用于痛风患者的高尿酸血症的长期治疗",
        "dosage": "起始剂量：40 mg，每日一次；2周后若血清尿酸未降至6 mg/dL以下，可增至80 mg，每日一次；严重肾功能损害患者限40 mg，每日一次",
        "feature": "新型非嘌呤类黄嘌呤氧化酶抑制剂，降酸效果强于别嘌醇；可空腹或餐后服用，食物不影响吸收",
        "price": "约180元/盒（30片装80mg）"
    },
    {
        "name": "吡非尼酮片",
        "brand": "Pirfenex",
        "pinyin": "pirfenex",
        "seq": 141,
        "category": "肺纤维化",
        "indication": "用于治疗特发性肺纤维化（IPF）",
        "dosage": "起始剂量：200 mg，每日3次（每日600 mg），随餐服用；此后逐步递增，第3周起每次400 mg，每日3次（每日1200 mg）维持",
        "feature": "多靶点抗纤维化药物，可抑制成纤维细胞增殖和胶原合成；需随餐服用以减少胃肠道反应",
        "price": "约650元/盒（Natco 100片装）"
    },
    {
        "name": "尼达尼布胶囊",
        "brand": "NINDEV",
        "pinyin": "nindev",
        "seq": 142,
        "category": "肺纤维化",
        "indication": "用于治疗特发性肺纤维化（IPF）及其他慢性纤维化间质性肺病",
        "dosage": "推荐剂量：150 mg，每日两次，间隔约12小时（如早、晚各一次）；轻度过量肝功能损害患者可调整至100 mg，每日两次；整粒吞服，不可咀嚼或压碎",
        "feature": "小分子酪氨酸激酶抑制剂，同时抑制多种生长因子受体；固定剂量方案，服用方便",
        "price": "约2800元/盒（CIPLA 60粒装）"
    },
    {
        "name": "尼达尼布胶囊",
        "brand": "Nindanib",
        "pinyin": "nindanib",
        "seq": 143,
        "category": "肺纤维化",
        "indication": "用于治疗特发性肺纤维化（IPF）及系统性硬化症相关间质性肺病",
        "dosage": "推荐剂量：150 mg，每日两次，间隔约12小时；根据耐受性可调整至100 mg，每日两次；中重度肝功能损害患者禁用",
        "feature": "SUN Pharma生产的尼达尼布版本，与原研OFEV具有相同的活性成分和疗效",
        "price": "约2600元/盒（SUN 60粒装）"
    },
    {
        "name": "地拉罗司口服混悬片",
        "brand": "DEFRIJET",
        "pinyin": "defrijet",
        "seq": 144,
        "category": "铁过载",
        "indication": "用于治疗2岁及以上患者因输血导致的慢性铁过载",
        "dosage": "起始剂量：20 mg/kg体重，每日一次（输血铁过载）；或10 mg/kg体重，每日一次（NDT综合征）；空腹服用，在每日相同时间；根据血清铁蛋白水平每月调整剂量",
        "feature": "一日一次口服铁螯合剂，使用方便；可溶解于水或果汁中服用；需定期监测肾功能",
        "price": "约1200元/盒（Glenmark 30片装）"
    }
]

# HTML模板
html_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 蓝培医疗</title>
    <style>
        body {{ font-family: "PingFang SC", "Microsoft YaHei", sans-serif; line-height: 1.8; max-width: 900px; margin: 0 auto; padding: 20px; color: #333; }}
        h1 {{ color: #1e3a5f; border-bottom: 2px solid #f97316; padding-bottom: 10px; }}
        h2 {{ color: #2d5a87; margin-top: 25px; }}
        .meta {{ color: #888; font-size: 14px; margin-bottom: 20px; }}
        .drug-header {{ background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 20px; border-radius: 10px; margin-bottom: 20px; }}
        .drug-name {{ font-size: 24px; color: #1e3a5f; font-weight: bold; }}
        .drug-brand {{ color: #f97316; font-size: 16px; margin-top: 5px; }}
        .section {{ margin: 20px 0; }}
        .dosage-box {{ background: #fff3e0; padding: 15px; border-left: 4px solid #f97316; margin: 15px 0; }}
        .feature-box {{ background: #e3f2fd; padding: 15px; border-left: 4px solid #2196f3; }}
        .price {{ color: #f97316; font-weight: bold; }}
        .back-link {{ display: inline-block; margin-top: 20px; color: #1e3a5f; text-decoration: none; }}
        .back-link:hover {{ text-decoration: underline; }}
        .consult-box {{ background: #f0f4f8; padding: 20px; border-radius: 8px; margin-top: 30px; text-align: center; }}
        .consult-box h3 {{ color: #1e3a5f; margin-top: 0; }}
    </style>
</head>
<body>
    <div class="drug-header">
        <div class="drug-name">{name}</div>
        <div class="drug-brand">品牌：{brand}</div>
    </div>
    
    <div class="meta">发布日期：{date} | 分类：{category}</div>
    
    <h2>药品简介</h2>
    <p>{indication}</p>
    
    <h2>用法用量</h2>
    <div class="dosage-box">
        <p><strong>推荐剂量：</strong>{dosage}</p>
    </div>
    
    <h2>产品特点</h2>
    <div class="feature-box">
        <p>{feature}</p>
    </div>
    
    <h2>参考价格</h2>
    <p class="price">{price}</p>
    
    <div class="consult-box">
        <h3>获取更多用药信息</h3>
        <p>想了解更多关于{name}的用药信息、价格或获取渠道？</p>
        <p>WhatsApp咨询：<a href="https://wa.me/639685838435">+63 968 583 8435</a></p>
        <p>微信咨询：17844531559</p>
    </div>
    
    <a href="news.html" class="back-link">← 返回资讯列表</a>
</body>
</html>'''

# 公众号TXT模板
txt_template = '''【{name}（{brand}）用药指南】

{name}是用于治疗{category}的海外合规药品。以下为您详细介绍：

【适应症】
{indication}

【用法用量】
起始剂量：{dosage}

【产品特点】
{feature}

【参考价格】
{price}

想了解更多用药信息或获取渠道，可通过以下方式联系我们：

• WhatsApp：+63 968 583 8435
• 微信：17844531559

---
蓝培医疗 | 帮助患者获取全球优质医疗资源
'''

# 生成文件
today = datetime.now().strftime('%Y-%m-%d')

for drug in drugs_data:
    # HTML文件
    html_content = html_template.format(
        title=drug["name"],
        name=drug["name"],
        brand=drug["brand"],
        date=today,
        category=drug["category"],
        indication=drug["indication"],
        dosage=drug["dosage"],
        feature=drug["feature"],
        price=drug["price"]
    )
    
    html_file = f'news-{drug["seq"]:03d}-{drug["pinyin"]}.html'
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f'已生成: {html_file}')
    
    # TXT文件
    txt_content = txt_template.format(
        name=drug["name"],
        brand=drug["brand"],
        category=drug["category"],
        indication=drug["indication"],
        dosage=drug["dosage"],
        feature=drug["feature"],
        price=drug["price"]
    )
    
    txt_file = f'news-{drug["seq"]:03d}-{drug["pinyin"]}.txt'
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(txt_content)
    print(f'已生成: {txt_file}')

print(f'\\n共生成 {len(drugs_data) * 2} 个文件')
