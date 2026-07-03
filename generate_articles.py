#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成蓝培医疗药品文章HTML"""

import os
import re

# 药品数据
drugs = [
    {
        "name": "尼拉帕利阿比特龙片",
        "brand": "Nizela",
        "generic": "Niraparib/Abiraterone",
        "category": "前列腺癌",
        "pinyin": "nizela",
        "filename": "news-021-nizela.html",
        "seo_title": "尼拉帕利阿比特龙片用法用量 | BRCA突变前列腺癌靶向药",
        "seo_desc": "尼拉帕利阿比特龙片用法用量详解，适用于BRCA突变的转移性去势抵抗性前列腺癌。含原研药与仿制药价格参考，专业全球医疗资源咨询。",
        "seo_keywords": "尼拉帕利阿比特龙片,用法用量,BRCA突变,前列腺癌,靶向药,阿比特龙仿制药",
        "indications": """
            <h2>适应症</h2>
            <p>本品联合泼尼松或泼尼松龙用于携带胚系和/或体系BRCA基因突变的转移性去势抵抗性前列腺癌成人患者（mCRPC）。</p>
            <div class="info-box">
                <p><strong>重要提示：</strong>使用前需进行BRCA基因检测确认存在BRCA突变。</p>
            </div>
        """,
        "dosage": """
            <h2>用法用量</h2>
            <h3>推荐剂量</h3>
            <p>本品的推荐剂量为<strong>200mg尼拉帕利/1000mg醋酸阿比特龙</strong>，每日一次口服，联合每日10mg泼尼松或泼尼松龙给药，直至疾病进展或出现不可耐受的毒性。</p>
            
            <h3>服药方式</h3>
            <ul>
                <li><strong>空腹服用</strong>：本品必须在餐后至少2小时服用，且在服用本品后至少1小时内不得进食</li>
                <li>用水送服，请勿切开、碾碎或咀嚼</li>
                <li>接受本品治疗的患者应同时接受促性腺激素释放激素（GnRH）类似物治疗，或进行过双侧睾丸切除术</li>
            </ul>
            
            <h3>漏服处理</h3>
            <p>如果出现漏服，应指导患者尽快在当天补服，次日仍按正常计划服药。</p>
        """,
        "side_effects": """
            <h2>常见不良反应</h2>
            <ul>
                <li><strong>血液系统</strong>：贫血、血小板减少、中性粒细胞减少</li>
                <li><strong>胃肠道</strong>：恶心、呕吐、便秘、腹泻</li>
                <li><strong>其他</strong>：疲劳乏力、食欲下降、高血压、水肿、皮疹</li>
            </ul>
            <div class="warning-box">
                <p><strong>严重警告：</strong>可能出现骨髓增生异常综合征/急性髓系白血病（MDS/AML），需定期监测血常规。</p>
            </div>
        """,
        "precautions": """
            <h2>注意事项</h2>
            <ul>
                <li>必须在有抗肿瘤药物使用经验的医生指导下使用</li>
                <li>治疗前需进行BRCA基因突变检测</li>
                <li>定期监测血常规、肝肾功能、血压</li>
                <li>避免与强效CYP3A4抑制剂或诱导剂同时使用</li>
                <li>孕妇及哺乳期禁用</li>
            </ul>
        """,
        "price_table": """
            <tr><td>原研药</td><td>泽倍珂（西安杨森）</td><td>中国</td><td>咨询获取报价</td></tr>
            <tr><td>仿制药</td><td>其他地区版本</td><td>海外</td><td>咨询获取报价</td></tr>
        """
    },
    {
        "name": "奥德昔巴特胶囊",
        "brand": "Odxibat",
        "generic": "Odevixibat",
        "category": "综合药品",
        "pinyin": "odxibat",
        "filename": "news-022-odxibat.html",
        "seo_title": "奥德昔巴特胶囊用法用量 | PFIC胆汁淤积性肝病靶向药",
        "seo_desc": "奥德昔巴特胶囊用法用量详解，适用于进行性家族性肝内胆汁淤积症(PFIC)和Alagille综合征。含原研药与仿制药价格参考，专业全球医疗资源咨询。",
        "seo_keywords": "奥德昔巴特,用法用量,PFIC,胆汁淤积,Alagille综合征,Bylvay",
        "indications": """
            <h2>适应症</h2>
            <p>奥德昔巴特适用于以下胆汁淤积性肝病相关瘙痒症状：</p>
            <ul>
                <li><strong>PFIC（进行性家族性肝内胆汁淤积症）</strong>：适用于3个月及以上确诊为PFIC的患儿</li>
                <li><strong>Alagille综合征（ALGS）</strong>：适用于12个月及以上因ALGS引发胆汁淤积性瘙痒的患者</li>
            </ul>
            <div class="info-box">
                <p><strong>作用机制：</strong>通过抑制回肠胆汁酸转运蛋白（IBAT），减少肠道内胆汁酸重吸收，降低血清胆汁酸水平，从而缓解瘙痒症状。</p>
            </div>
        """,
        "dosage": """
            <h2>用法用量</h2>
            <h3>PFIC患者（3个月以上）</h3>
            <ul>
                <li><strong>初始剂量</strong>：40μg/kg，每日早晨随餐口服1次</li>
                <li><strong>剂量调整</strong>：若持续治疗3个月后瘙痒未缓解，可每3个月增加剂量1次，每次增加40μg/kg</li>
                <li><strong>最大剂量</strong>：120μg/kg/日，且每日总剂量不超过6mg</li>
            </ul>
            
            <h3>Alagille综合征患者（12个月及以上）</h3>
            <ul>
                <li><strong>推荐剂量</strong>：120μg/kg，每日早晨随餐口服1次</li>
            </ul>
            
            <h3>服药方式</h3>
            <p>每日晨起随餐口服1次；可打开胶囊或将微丸混入食物或液体中服用。</p>
        """,
        "side_effects": """
            <h2>常见不良反应</h2>
            <ul>
                <li><strong>消化系统</strong>：腹泻、腹痛、呕吐（多为轻度至中度）</li>
                <li><strong>代谢/营养</strong>：血清转氨酶轻度升高</li>
                <li><strong>皮肤反应</strong>：皮疹、瘙痒加重（罕见）</li>
                <li><strong>其他</strong>：发热、头痛（发生率较低）</li>
            </ul>
            <div class="warning-box">
                <p><strong>重点监测：</strong>可能出现脂溶性维生素（A、D、E、K）缺乏，建议定期监测并补充。</p>
            </div>
        """,
        "precautions": """
            <h2>注意事项</h2>
            <ul>
                <li>需在专业医师指导下使用</li>
                <li>治疗前需评估肝功能、血清胆汁酸水平及营养状况</li>
                <li>定期监测肝功能指标、胆汁酸水平和脂溶性维生素水平</li>
                <li>避免与胆汁酸螯合剂（如考来烯胺）同服，需间隔≥4小时</li>
                <li>避免突然停药，需在医生指导下逐步减量</li>
                <li>孕妇及哺乳期禁用</li>
            </ul>
        """,
        "price_table": """
            <tr><td>原研药</td><td>Bylvay（蓓尔唯）</td><td>美国/欧盟</td><td>咨询获取报价</td></tr>
            <tr><td>仿制药</td><td>其他地区版本</td><td>海外</td><td>咨询获取报价</td></tr>
        """
    },
    {
        "name": "奥拉帕利片",
        "brand": "Olieni",
        "generic": "Olaparib",
        "category": "前列腺癌",
        "pinyin": "olieni",
        "filename": "news-023-olieni.html",
        "seo_title": "奥拉帕利片用法用量 | BRCA突变前列腺癌PARP抑制剂",
        "seo_desc": "奥拉帕利片用法用量详解，适用于携带BRCA突变的转移性去势抵抗性前列腺癌。作为PARP抑制剂，为前列腺癌患者提供精准靶向治疗方案。",
        "seo_keywords": "奥拉帕利片,用法用量,BRCA突变,前列腺癌,PARP抑制剂,利普卓",
        "indications": """
            <h2>适应症</h2>
            <p>奥拉帕利适用于携带胚系或体细胞BRCA突变的转移性去势抵抗性前列腺癌（mCRPC）患者：</p>
            <ul>
                <li>适用于既往治疗（包括一种新型内分泌药物）失败的mCRPC成人患者</li>
                <li>可作为单药或与阿比特龙联合使用</li>
            </ul>
            <div class="info-box">
                <p><strong>作用机制：</strong>奥拉帕利是聚ADP核糖聚合酶（PARP）抑制剂，通过抑制PARP酶活性，干扰肿瘤细胞DNA修复，导致合成致死。</p>
            </div>
        """,
        "dosage": """
            <h2>用法用量</h2>
            <h3>推荐剂量</h3>
            <ul>
                <li><strong>单药治疗</strong>：300mg（2片150mg片剂），每日2次，相当于每日总剂量为600mg</li>
                <li><strong>联合阿比特龙</strong>：奥拉帕利300mg每日2次 + 阿比特龙1000mg每日1次 + 泼尼松5mg每日2次</li>
            </ul>
            
            <h3>服药方式</h3>
            <ul>
                <li>整片吞服，不应咀嚼、压碎、溶解或掰断</li>
                <li>进餐或空腹时均可服用</li>
                <li>每次服药间隔约12小时</li>
                <li>接受治疗的患者应同时接受GnRH类似物治疗，或已进行双侧睾丸切除术</li>
            </ul>
            
            <h3>剂量调整</h3>
            <ul>
                <li>首次减量：250mg，每日2次（500mg/日）</li>
                <li>再次减量：200mg，每日2次（400mg/日）</li>
            </ul>
        """,
        "side_effects": """
            <h2>常见不良反应</h2>
            <ul>
                <li><strong>常见</strong>（≥10%）：恶心、疲乏、贫血、呕吐、腹泻、食欲下降、头痛</li>
                <li><strong>≥3级不良反应</strong>：贫血（16%）、中性粒细胞减少症（5%）、疲乏/乏力（5%）</li>
            </ul>
            <div class="warning-box">
                <p><strong>严重警告：</strong>可能出现骨髓增生异常综合征/急性髓系白血病（MDS/AML），需定期监测血常规。</p>
            </div>
        """,
        "precautions": """
            <h2>注意事项</h2>
            <ul>
                <li>必须在有肿瘤治疗经验的医生指导下使用</li>
                <li>治疗前需进行BRCA基因突变检测</li>
                <li>定期监测血常规、肝肾功能</li>
                <li>避免食用西柚、酸橙及其果汁（含CYP3A4抑制剂）</li>
                <li>避免与强效CYP3A4抑制剂或诱导剂同时使用</li>
                <li>孕妇及哺乳期禁用</li>
            </ul>
        """,
        "price_table": """
            <tr><td>原研药</td><td>利普卓（阿斯利康）</td><td>英国/美国</td><td>咨询获取报价</td></tr>
            <tr><td>仿制药</td><td>其他地区版本</td><td>海外</td><td>咨询获取报价</td></tr>
        """
    },
    {
        "name": "甲磺酸奥希替尼片",
        "brand": "Osiem",
        "generic": "Osimertinib",
        "category": "肺癌",
        "pinyin": "osiem",
        "filename": "news-024-osiem.html",
        "seo_title": "甲磺酸奥希替尼片用法用量 | EGFR突变非小细胞肺癌靶向药",
        "seo_desc": "甲磺酸奥希替尼片用法用量详解，适用于EGFR突变的非小细胞肺癌。作为第三代EGFR-TKI，为肺癌患者提供显著生存获益。",
        "seo_keywords": "奥希替尼,甲磺酸奥希替尼,用法用量,EGFR突变,肺癌,T790M",
        "indications": """
            <h2>适应症</h2>
            <p>甲磺酸奥希替尼片适用于：</p>
            <ul>
                <li><strong>一线治疗</strong>：具有表皮生长因子受体（EGFR）外显子19缺失或外显子21（L858R）置换突变的局部晚期或转移性非小细胞肺癌（NSCLC）成人患者</li>
                <li><strong>二线治疗</strong>：既往经EGFR酪氨酸激酶抑制剂（TKI）治疗时或治疗后出现疾病进展，并且经检测确认存在EGFR T790M突变阳性的局部晚期或转移性NSCLC成人患者</li>
                <li><strong>III期不可切除NSCLC</strong>：接受含铂放化疗期间或之后未出现疾病进展的EGFR突变患者</li>
            </ul>
            <div class="info-box">
                <p><strong>创新突破：</strong>奥希替尼是全球首个获批EGFR突变III期不可切除NSCLC人群根治性放化疗后维持治疗的靶向药，中位无进展生存期（PFS）超过3年。</p>
            </div>
        """,
        "dosage": """
            <h2>用法用量</h2>
            <h3>推荐剂量</h3>
            <p>本品的推荐剂量为<strong>每日80mg</strong>，直至疾病进展或出现无法耐受的毒性。</p>
            
            <h3>服药方式</h3>
            <ul>
                <li>整片和水送服，不应压碎、掰断或咀嚼</li>
                <li>每日相同时间服用，进餐或空腹时服用均可</li>
                <li>如漏服本品1次，应补服，除非下次服药时间在12小时以内</li>
            </ul>
            
            <h3>剂量调整</h3>
            <p>根据患者个体的安全性和耐受性，可暂停用药或减量。如需减量，剂量应减至<strong>40mg，每日1次</strong>。</p>
        """,
        "side_effects": """
            <h2>常见不良反应</h2>
            <ul>
                <li><strong>皮肤反应</strong>：皮疹、腹泻、甲沟炎、皮肤干燥</li>
                <li><strong>消化系统</strong>：恶心、食欲下降、便秘</li>
                <li><strong>其他</strong>：疲乏、头痛、QTc间期延长</li>
            </ul>
            <div class="warning-box">
                <p><strong>心脏监测：</strong>可能出现左心室射血分数（LVEF）下降，治疗前及治疗中需监测心功能。</p>
            </div>
        """,
        "precautions": """
            <h2>注意事项</h2>
            <ul>
                <li>必须在有抗肿瘤治疗经验的医生指导下使用</li>
                <li>使用前需明确EGFR突变状态（经充分验证的检测方法确认）</li>
                <li>定期监测心功能（LVEF）</li>
                <li>轻度肝功能损害患者慎用，中重度肝功能损害患者不建议使用</li>
                <li>重度或终末期肾功能损害患者慎用</li>
                <li>孕妇及哺乳期禁用</li>
            </ul>
        """,
        "price_table": """
            <tr><td>原研药</td><td>泰瑞沙（阿斯利康）</td><td>英国/美国</td><td>咨询获取报价</td></tr>
            <tr><td>仿制药</td><td>其他地区版本</td><td>海外</td><td>咨询获取报价</td></tr>
        """
    },
    {
        "name": "哌柏西利片",
        "brand": "Parcini",
        "generic": "Palbociclib",
        "category": "乳腺癌",
        "pinyin": "parcini",
        "filename": "news-025-parcini.html",
        "seo_title": "哌柏西利片用法用量 | HR+/HER2-乳腺癌CDK4/6抑制剂",
        "seo_desc": "哌柏西利片用法用量详解，适用于激素受体阳性(HR+)人表皮生长因子受体2阴性(HER2-)的局部晚期或转移性乳腺癌。作为CDK4/6抑制剂一线治疗药物。",
        "seo_keywords": "哌柏西利片,用法用量,乳腺癌,CDK4/6抑制剂,HR+乳腺癌,Ibrance",
        "indications": """
            <h2>适应症</h2>
            <p>哌柏西利片适用于激素受体（HR）阳性、人表皮生长因子受体2（HER2）阴性的局部晚期或转移性乳腺癌：</p>
            <ul>
                <li>应与芳香化酶抑制剂（如来曲唑）联合使用，作为绝经后女性患者的初始内分泌治疗</li>
                <li>可与氟维司群联合用于既往接受过内分泌治疗的患者的后续治疗</li>
            </ul>
            <div class="info-box">
                <p><strong>临床获益：</strong>哌柏西利联合来曲唑一线治疗，中位无进展生存期（PFS）长达24.8个月，显著优于来曲唑单药的14.5个月。</p>
            </div>
        """,
        "dosage": """
            <h2>用法用量</h2>
            <h3>推荐剂量</h3>
            <p>本品的推荐剂量为<strong>125mg/日</strong>，连续服用21天，之后停药7天，<strong>28天为一个治疗周期</strong>。</p>
            
            <h3>服药方式</h3>
            <ul>
                <li>片剂可与食物同服或空腹服用</li>
                <li>胶囊剂型应与食物同服（确保暴露量一致）</li>
                <li>每日相同时间服用</li>
                <li>应整片吞服，不应咀嚼或压碎</li>
            </ul>
            
            <h3>剂量调整</h3>
            <p>如出现不良反应，可暂停用药或减量。首次减量至100mg/日，再次减量至75mg/日。</p>
        """,
        "side_effects": """
            <h2>常见不良反应</h2>
            <ul>
                <li><strong>血液系统</strong>：中性粒细胞减少（最常见）、白细胞减少、贫血、血小板减少</li>
                <li><strong>其他</strong>：疲乏、感染、恶心、口腔炎、脱发、皮疹</li>
            </ul>
            <div class="info-box">
                <p><strong>温馨提示：</strong>哌柏西利片剂与胶囊剂安全性相当，但片剂可与质子泵抑制剂（PPI）联用，不影响疗效。</p>
            </div>
            <div class="warning-box">
                <p><strong>重要监测：</strong>中性粒细胞减少大多发生在治疗的前2-3个月内，中位缓解时间为7天。</p>
            </div>
        """,
        "precautions": """
            <h2>注意事项</h2>
            <ul>
                <li>必须在有肿瘤治疗经验的医生指导下使用</li>
                <li>治疗前需检测血常规，治疗期间需定期监测</li>
                <li>出现严重中性粒细胞减少时需暂停用药或减量</li>
                <li>避免与强效CYP3A4抑制剂或诱导剂同时使用</li>
                <li>肝肾功能损害患者需谨慎使用</li>
                <li>孕妇及哺乳期禁用</li>
            </ul>
        """,
        "price_table": """
            <tr><td>原研药</td><td>Ibrance（辉瑞）</td><td>美国</td><td>咨询获取报价</td></tr>
            <tr><td>仿制药</td><td>其他地区版本</td><td>海外</td><td>咨询获取报价</td></tr>
        """
    }
]

# 读取模板
with open("news/article-template.html", "r", encoding="utf-8") as f:
    template = f.read()

# 生成每个药品的HTML文件
for drug in drugs:
    content = template
    
    # 替换占位符
    content = content.replace("{{DRUG_NAME}}", drug["name"])
    content = content.replace("{{GENERIC_NAME}}", drug["generic"])
    content = content.replace("{{BRAND_NAME}}", drug["brand"])
    content = content.replace("{{CATEGORY}}", drug["category"])
    content = content.replace("{{CATEGORY_KEY}}", "tab_drug")
    content = content.replace("{{CATEGORY_LABEL}}", "药闻速递")
    
    # SEO
    content = content.replace("{{DRUG_NAME}}用法用量 - 蓝培医疗新闻资讯", drug["seo_title"])
    content = content.replace('meta name="description" content="{{DRUG_NAME}}用法用量详解', f'meta name="description" content="{drug["seo_desc"]}')
    content = content.replace("{{DRUG_NAME}},{{DRUG_NAME}}用法用量,{{DRUG_NAME}}价格,{{GENERIC_NAME}}仿制药,{{BRAND_NAME}}", drug["seo_keywords"])
    
    # 文章内容
    article_content = drug["indications"] + drug["dosage"] + drug["side_effects"] + drug["precautions"]
    content = content.replace("<!-- ARTICLE_CONTENT_PLACEHOLDER -->", article_content)
    
    # 价格表
    content = content.replace("<!-- PRICE_ROWS_PLACEHOLDER -->", drug["price_table"])
    
    # 文件名
    content = content.replace("{{ARTICLE_FILENAME}}", drug["filename"])
    
    # 写文件到根目录
    output_path = drug["filename"]
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Generated: {output_path}")

print("\nAll articles generated successfully!")
