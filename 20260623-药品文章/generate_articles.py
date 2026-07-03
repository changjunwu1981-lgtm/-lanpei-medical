#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成5篇药品用法用量文章
"""
import os
import json

# 读取模板
TEMPLATE_PATH = '/app/data/所有对话/主对话/蓝培医疗文章/news/article-template.html'
OUTPUT_DIR = '/app/data/所有对话/主对话/蓝培医疗文章/20260623-药品文章'
DRUGS_JSON = '/app/data/所有对话/主对话/蓝培医疗文章/药品列表.json'

with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

# 修正模板：所有 13037856968 替换为 17844531559
template = template.replace('13037856968', '17844531559')

with open(DRUGS_JSON, 'r', encoding='utf-8') as f:
    drugs = json.load(f)

covered_count = sum(1 for d in drugs if d.get('covered') == True)
uncovered = [d for d in drugs if d.get('covered') == False][:5]


# 起始序号 = 已存在文件最大序号 + 1 = 144（避免与news-140~143冲突）
START_IDX = 144

# ============ 1. 非布司他片 Febuxostat (Intas) ============
drug1 = {
    'idx': START_IDX,  # 144
    'name': '非布司他片',
    'generic': '非布司他 (Febuxostat)',
    'brand': 'Feburic / 优立通 (Intas 印度版)',
    'category': '痛风 / 高尿酸血症',
    'category_label': '痛风用药',
    'filename': 'news-144-febuxostat.html',
}

content1 = """
<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品简介</h2>
<p>非布司他（Febuxostat）是一种新型<strong>非嘌呤类选择性黄嘌呤氧化酶（XO）抑制剂</strong>，通过抑制尿酸合成路径中的关键酶，有效降低血尿酸浓度。该药由日本帝人制药研发，2009年获FDA批准用于临床，是20世纪80年代以来首个通过抑制尿酸合成机制治疗痛风的新药。原研品商品名为<strong>Feburic/优立通</strong>，已在全球60多个国家上市。该药尤其适合<strong>别嘌醇（Allopurinol）治疗失败或不耐受</strong>的痛风患者，为这部分人群提供了更优选择。</p>

<h2><i class="fas fa-crosshairs mr-2 text-orange-500"></i>适应症</h2>
<div class="info-box">
<ul class="list-disc list-inside space-y-2">
<li><strong>痛风患者高尿酸血症的长期治疗</strong>：适用于成年痛风患者持续性高尿酸血症（血尿酸≥6mg/dL或360μmol/L）</li>
<li><strong>仅用于别嘌醇不耐受、治疗失败或不适合的患者</strong>：FDA对非布司他有限制使用要求，不作为一线</li>
<li><strong>不推荐用于无症状高尿酸血症</strong></li>
</ul>
</div>

<h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
<h3>推荐剂量</h3>
<ul>
<li><strong>起始剂量</strong>：40mg，口服，每日1次</li>
<li><strong>维持剂量</strong>：40mg或80mg，每日1次</li>
<li><strong>剂量调整</strong>：治疗2周后检测血尿酸，若未达到目标值（&lt;6mg/dL）可增至80mg/日</li>
</ul>

<h3>特殊人群剂量</h3>
<ul>
<li><strong>严重肾功能不全</strong>（肌酐清除率&lt;30mL/min）：每日剂量<strong>不应超过40mg</strong></li>
<li><strong>轻中度肾功能不全</strong>（CrCl 30-89mL/min）：无需调整剂量</li>
<li><strong>轻中度肝功能不全</strong>（Child-Pugh A/B级）：无需调整剂量</li>
<li><strong>重度肝功能不全</strong>：慎用，无充分研究数据</li>
<li><strong>老年人</strong>：无需调整剂量，但需监测不良反应</li>
<li><strong>儿童（&lt;18岁）</strong>：安全性尚未确立，不推荐</li>
</ul>

<h3>服用方法</h3>
<ul>
<li>口服给药，<strong>餐前餐后均可</strong>，无需随餐服用</li>
<li>建议<strong>固定时间</strong>每日一次服用</li>
<li>整片吞服，<strong>不可掰开或咀嚼</strong></li>
<li>足量饮水（建议每日≥2000ml）有助于尿酸排泄</li>
</ul>

<h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>重要注意事项</h2>
<div class="warning-box">
<strong>痛风发作预防</strong>：开始治疗初期，因血尿酸急剧下降可能诱发痛风急性发作。医生通常会同时开具<strong>小剂量秋水仙碱或非甾体抗炎药（NSAIDs）</strong>预防发作，预防用药可持续<strong>最长6个月</strong>。若治疗期间出现痛风发作，<strong>无需停用</strong>非布司他。
</div>

<div class="warning-box">
<strong>心血管事件风险</strong>：2019年FDA黑框警告——非布司他可能增加<strong>心血管死亡风险</strong>。有心脏病史、心肌梗死、中风、心绞痛等患者需<strong>严密监测</strong>，出现胸痛、呼吸急促、心跳异常、一侧肢体无力、突发剧烈头痛等症状<strong>应立即就医</strong>。
</div>

<ul>
<li><strong>肝毒性</strong>：用药前及用药期间<strong>定期监测肝功能</strong>（ALT/AST/胆红素）。若ALT超过参考范围上限3倍以上，应中止服药并查明原因</li>
<li><strong>严重皮肤反应</strong>：罕见但严重，包括Stevens-Johnson综合征（SJS）、中毒性表皮坏死松解症（TEN）。一旦怀疑应立即停药</li>
<li><strong>禁忌</strong>：正在接受<strong>硫唑嘌呤、巯嘌呤</strong>治疗的患者禁用（严重相互作用！）</li>
<li><strong>孕妇</strong>：FDA妊娠分级C级，仅利大于弊时使用</li>
<li><strong>哺乳期</strong>：不推荐</li>
<li><strong>生活方式</strong>：限制高嘌呤食物（动物内脏、海鲜、浓肉汤），严格戒酒尤其是啤酒</li>
</ul>

<h2><i class="fas fa-prescription-bottle-alt mr-2 text-orange-500"></i>规格与保存</h2>
<ul>
<li><strong>规格</strong>：片剂，40mg/片、80mg/片</li>
<li><strong>包装</strong>：印度Intas版常见30片/盒</li>
<li><strong>保存</strong>：密封，阴凉干燥处保存（&lt;25°C），避光防潮</li>
</ul>
"""

price_rows1 = """
<tr><td>原研药</td><td>Feburic（非布司他）</td><td>日本帝人 / Astellas / 优立通</td><td>由实际咨询为准</td></tr>
<tr><td>仿制版</td><td>非布司他片（Intas）</td><td>印度Intas</td><td>由实际咨询为准</td></tr>
"""


# ============ 2. 吡非尼酮片 Pirfenex (Natco) ============
drug2 = {
    'idx': START_IDX + 1,  # 145
    'name': '吡非尼酮片',
    'generic': '吡非尼酮 (Pirfenidone)',
    'brand': 'Pirfenex / 艾思瑞',
    'category': '特发性肺纤维化（IPF）',
    'category_label': '肺纤维化用药',
    'filename': 'news-145-pirfenidone.html',
}

content2 = """
<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品简介</h2>
<p>吡非尼酮（Pirfenidone）是一种具有<strong>抗纤维化、抗炎和抗氧化</strong>多重作用的广谱口服小分子药物，是全球第一个、也是中国CSCO指南推荐用于<strong>特发性肺纤维化（IPF）</strong>的一线治疗药物。该药由日本盐野义制药（Shionogi）原研，2014年FDA批准用于IPF治疗，商品名为<strong>Esbriet</strong>。中国同类产品名为<strong>艾思瑞</strong>。吡非尼酮通过抑制转化生长因子β（TGF-β）等致纤维化因子的产生，<strong>延缓IPF患者用力肺活量（FVC）的下降速率</strong>，改善生活质量、延长生存时间，但<strong>不能治愈该疾病</strong>。印度Natco与Cipla等厂家生产仿制版Pirfenex（200mg/片）已获批上市。</p>

<h2><i class="fas fa-crosshairs mr-2 text-orange-500"></i>适应症</h2>
<div class="info-box">
<ul class="list-disc list-inside space-y-2">
<li><strong>轻至中度特发性肺纤维化（IPF）</strong>：确诊IPF且FVC%≥50%的成人患者</li>
<li><strong>进行性纤维化性间质性肺疾病（PF-ILD）</strong>：在专科医生评估后使用</li>
<li><strong>慢性过敏性肺炎（CHP）</strong>等纤维化性肺病</li>
</ul>
</div>

<h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
<h3>推荐剂量（剂量滴定）</h3>
<p>为减少胃肠道反应和光敏反应等不良反应，<strong>必须采用剂量递增法</strong>逐步达到维持剂量。Pirfenex规格为200mg/片：</p>
<ul>
<li><strong>第1-7天</strong>：每次200mg（1片），每日3次（共<strong>600mg/日</strong>），<strong>餐后服用</strong></li>
<li><strong>第8-14天</strong>：每次400mg（2片），每日3次（共<strong>1200mg/日</strong>）</li>
<li><strong>第15天起（维持剂量）</strong>：每次600mg（3片），每日3次（共<strong>1800mg/日</strong>）</li>
</ul>
<p>注：欧美及日本上市的Esbriet规格为267mg/片，剂量递增方案按801mg→1602mg→2403mg/日执行，请<strong>以药品实际规格与医生处方为准</strong>。</p>

<h3>服用方法</h3>
<ul>
<li><strong>必须餐后服用</strong>（空腹时血药浓度会明显升高，不良反应风险增大）</li>
<li>整片<strong>吞服，勿掰开、压碎或咀嚼</strong></li>
<li>每天3次（早/午/晚），保持固定的服药时间</li>
<li>每日总剂量<strong>不可超过2400mg/日</strong></li>
</ul>

<h3>特殊人群</h3>
<ul>
<li><strong>轻中度肝功能不全</strong>（Child-Pugh A/B）：无需调整剂量，需加强监测</li>
<li><strong>重度肝功能不全</strong>（Child-Pugh C）：<strong>禁用</strong></li>
<li><strong>轻中度肾功能不全</strong>：无需调整剂量</li>
<li><strong>重度肾功能不全</strong>（CrCl&lt;30mL/min）或透析患者：<strong>慎用</strong></li>
<li><strong>老年患者</strong>：≥65岁无需调整剂量，但生理功能下降需<strong>慎用</strong></li>
<li><strong>儿童/青少年</strong>：安全性数据不足，<strong>不推荐</strong></li>
</ul>

<h3>中断后重启</h3>
<ul>
<li>中断治疗<strong>≥14天</strong>：需<strong>重新从初始剂量滴定</strong></li>
<li>中断治疗<strong>&lt;14天</strong>：可直接恢复之前的维持剂量</li>
</ul>

<h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>重要注意事项</h2>
<div class="warning-box">
<strong>肝毒性监测</strong>：本品可能引起严重肝损伤。<strong>治疗前6个月每月监测1次肝功能</strong>（ALT/AST/胆红素），之后每3个月监测1次。ALT/AST≥3倍ULN需减量，≥5倍ULN应<strong>停药并保肝治疗</strong>。
</div>

<div class="warning-box">
<strong>光敏反应预防</strong>：吡非尼酮可显著增加皮肤对阳光和紫外线的敏感性，长期暴露可能增加<strong>皮肤癌</strong>风险。用药期间需采取<strong>严格防晒措施</strong>：每天涂抹SPF50+防晒霜、穿长袖衣裤、戴宽边帽、避免正午阳光直射。出现皮疹、瘙痒及时联系医生。
</div>

<ul>
<li><strong>胃肠道反应</strong>（恶心、呕吐、腹泻、食欲下降）：发生率30-50%。餐后服用、分次少量进食、避免油腻食物可缓解</li>
<li><strong>绝对禁忌</strong>：对吡非尼酮过敏者；中重度肝病患者；妊娠及哺乳期；需服用氟伏沙明者</li>
<li><strong>药物相互作用</strong>：
<ul>
<li>禁用强效CYP1A2抑制剂（<strong>氟伏沙明、依诺沙星</strong>）——可使吡非尼酮血药浓度升高4-7倍</li>
<li>慎用中效CYP1A2抑制剂（环丙沙星）——联用需减量至534mg×3/日</li>
<li>避免CYP1A2诱导剂（利福平、卡马西平、苯妥英钠）——降低疗效</li>
</ul>
</li>
<li><strong>吸烟</strong>：烟草多环芳烃诱导CYP1A2，使血药浓度降低50%以上——<strong>用药期间必须戒烟</strong></li>
<li><strong>驾驶/机械操作</strong>：可能出现头晕、嗜睡，避免从事相关活动</li>
</ul>

<h2><i class="fas fa-prescription-bottle-alt mr-2 text-orange-500"></i>规格与保存</h2>
<ul>
<li><strong>规格</strong>：200mg/片，150片/盒（印度版Pirfenex）</li>
<li><strong>保存</strong>：密封，&lt;25°C干燥处保存</li>
<li><strong>避免</strong>：受潮、避光、儿童不可触及</li>
</ul>
"""

price_rows2 = """
<tr><td>原研药</td><td>Esbriet（吡非尼酮）</td><td>日本盐野义（Shionogi）/ 罗氏（部分市场）</td><td>由实际咨询为准</td></tr>
<tr><td>中国同类</td><td>艾思瑞</td><td>北京康蒂尼</td><td>由实际咨询为准</td></tr>
<tr><td>仿制版</td><td>Pirfenex（吡非尼酮）</td><td>印度Natco / Cipla</td><td>由实际咨询为准</td></tr>
"""


# ============ 3. 尼达尼布胶囊 NINDEV (CIPLA) ============
drug3 = {
    'idx': START_IDX + 2,  # 146
    'name': '尼达尼布胶囊',
    'generic': '尼达尼布 (Nintedanib)',
    'brand': 'Nintib / Ofev（维加特）',
    'category': '特发性肺纤维化（IPF）',
    'category_label': '肺纤维化用药',
    'filename': 'news-146-nintedanib-cipla.html',
}

content3 = """
<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品简介</h2>
<p>尼达尼布（Nintedanib）是一种口服小分子<strong>三重血管激酶抑制剂（triple angiokinase inhibitor）</strong>，通过抑制VEGFR、FGFR、PDGFR等多种酪氨酸激酶活性，<strong>减缓肺纤维化进程</strong>。该药由德国勃林格殷格翰（Boehringer Ingelheim）原研，商品名为<strong>Ofev（维加特）</strong>，2014年FDA批准用于特发性肺纤维化（IPF）。印度Cipla生产仿制版<strong>Nintib（100mg/150mg胶囊）</strong>于2020年上市，是全球首个进入临床的尼达尼布仿制药之一。Nintib主要用于治疗<strong>IPF、具有进行性表型的慢性纤维化性间质性肺疾病（PF-ILD）以及系统性硬化症相关间质性肺疾病（SSc-ILD）</strong>，可显著降低FVC年下降率，是目前IPF抗纤维化治疗的<strong>一线核心药物</strong>。</p>

<h2><i class="fas fa-crosshairs mr-2 text-orange-500"></i>适应症</h2>
<div class="info-box">
<ul class="list-disc list-inside space-y-2">
<li><strong>特发性肺纤维化（IPF）</strong>：成人IPF的一线治疗</li>
<li><strong>具有进行性表型的慢性纤维化性间质性肺疾病（PF-ILD）</strong></li>
<li><strong>系统性硬化症相关间质性肺疾病（SSc-ILD）</strong></li>
<li><strong>非小细胞肺癌（NSCLC）</strong>：联合多西他赛用于腺癌二线治疗（特定基因型）</li>
</ul>
</div>

<h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
<h3>推荐剂量</h3>
<ul>
<li><strong>标准剂量</strong>：<strong>150mg，每日2次</strong>（早晚各一次，间隔约12小时）</li>
<li><strong>IPF、PF-ILD、SSc-ILD</strong>：每次150mg bid，与餐同服</li>
<li><strong>NSCLC（联合多西他赛）</strong>：每次200mg bid，治疗第2-21天服用</li>
</ul>

<h3>剂量调整</h3>
<ul>
<li>如不能耐受（腹泻、肝酶升高、恶心等），可<strong>减量至100mg bid</strong></li>
<li>减量后仍不能耐受，应<strong>暂停治疗</strong>，症状缓解后考虑重启</li>
<li><strong>不可自行减量或停药</strong>，须严格遵医嘱</li>
</ul>

<h3>服用方法</h3>
<ul>
<li><strong>必须与餐同服</strong>（减少胃肠道反应）</li>
<li>整粒胶囊<strong>吞服，勿压碎、咀嚼或打开</strong></li>
<li>每天固定时间服药，维持稳定的血药浓度</li>
<li>每日总剂量<strong>不可超过300mg</strong></li>
</ul>

<h3>特殊人群</h3>
<ul>
<li><strong>轻中度肝功能不全</strong>（Child-Pugh A）：慎用，建议密切监测肝功能</li>
<li><strong>重度肝功能不全</strong>（Child-Pugh B/C）：<strong>禁用</strong>，数据不足</li>
<li><strong>轻度肾功能不全</strong>：无需调整剂量</li>
<li><strong>中重度肾功能不全</strong>或透析：<strong>慎用</strong></li>
<li><strong>老年人</strong>（≥65岁）：无需调整剂量，但需监测</li>
<li><strong>儿童/青少年</strong>（&lt;18岁）：不推荐</li>
<li><strong>妊娠期</strong>：<strong>禁用</strong>（动物实验显示生殖毒性）</li>
<li><strong>哺乳期</strong>：用药期间停止哺乳</li>
</ul>

<h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>重要注意事项</h2>
<div class="warning-box">
<strong>腹泻管理</strong>：腹泻是<strong>最常见</strong>的不良反应（发生率&gt;60%）。<strong>首剂即可发生</strong>。处理方法：①足量饮水（≥2L/日）；②症状轻微可用洛哌丁胺对症；③严重（≥3次/日）应联系医生考虑<strong>减量至100mg bid</strong>；④配合益生菌、低脂低纤维饮食。
</div>

<div class="warning-box">
<strong>肝毒性监测</strong>：治疗前、治疗前3个月<strong>每月监测</strong>ALT/AST/胆红素，之后定期复查。肝酶显著升高（≥3×ULN伴症状或≥5×ULN）应<strong>减量或停药</strong>。
</div>

<ul>
<li><strong>出血风险</strong>：因抑制VEGFR可能影响血管生成，<strong>有出血倾向或正在抗凝治疗者慎用</strong></li>
<li><strong>胃肠道穿孔</strong>：罕见但严重，近期有腹部手术史者慎用</li>
<li><strong>动脉血栓栓塞</strong>：有心血管疾病史者需谨慎</li>
<li><strong>伤口愈合</strong>：术前<strong>至少停药28天</strong>，术后评估恢复情况再考虑重启</li>
<li><strong>绝对禁忌</strong>：对尼达尼布、花生或大豆过敏者；孕妇</li>
<li><strong>药物相互作用</strong>：
<ul>
<li>强效P-gp和CYP3A4抑制剂（酮康唑、红霉素）会增加尼达尼布暴露——需密切监测</li>
<li>强效P-gp诱导剂（利福平、卡马西平、苯妥英钠）会降低疗效</li>
<li>抗凝药（华法林、肝素）联用可能增加出血风险</li>
</ul>
</li>
<li><strong>避孕</strong>：治疗期间及停药后至少3个月内<strong>采取有效避孕措施</strong></li>
</ul>

<h2><i class="fas fa-prescription-bottle-alt mr-2 text-orange-500"></i>规格与保存</h2>
<ul>
<li><strong>规格</strong>：软胶囊，100mg/粒、150mg/粒</li>
<li><strong>包装</strong>：印度Cipla版Nintib：100mg×30粒/瓶、150mg×30粒/瓶</li>
<li><strong>保存</strong>：&lt;25°C，避光密封保存，<strong>不可冷冻</strong></li>
<li><strong>开瓶后</strong>：应密封置于原包装内防潮</li>
</ul>
"""

price_rows3 = """
<tr><td>原研药</td><td>Ofev（维加特，尼达尼布）</td><td>德国勃林格殷格翰（Boehringer Ingelheim）</td><td>由实际咨询为准</td></tr>
<tr><td>仿制版</td><td>Nintib（尼达尼布）</td><td>印度Cipla</td><td>由实际咨询为准</td></tr>
"""


# ============ 4. 尼达尼布胶囊 Nindanib (SUN) ============
drug4 = {
    'idx': START_IDX + 3,  # 147
    'name': '尼达尼布胶囊',
    'generic': '尼达尼布 (Nintedanib)',
    'brand': 'Nindanib / Ofev（维加特）',
    'category': '特发性肺纤维化（IPF）',
    'category_label': '肺纤维化用药',
    'filename': 'news-147-nintedanib-sun.html',
}

content4 = """
<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品简介</h2>
<p>尼达尼布（Nintedanib）是一种口服小分子<strong>三重血管激酶抑制剂</strong>，通过抑制VEGFR、FGFR、PDGFR等多种酪氨酸激酶活性，<strong>减缓肺纤维化进程</strong>。原研品为德国勃林格殷格翰的<strong>Ofev（维加特）</strong>，2014年获FDA批准用于治疗<strong>特发性肺纤维化（IPF）</strong>，后陆续扩展至具有进行性表型的慢性纤维化性间质性肺疾病（PF-ILD）、系统性硬化症相关间质性肺疾病（SSc-ILD），并在非小细胞肺癌（NSCLC）联合多西他赛方案中应用。印度<strong>Sun Pharma</strong>等厂家生产仿制版<strong>Nindanib（150mg软胶囊）</strong>，通过WHO-GMP认证，全球供应，为IPF患者提供高性价比的治疗选择。Nindanib与原研Ofev<strong>生物等效</strong>，临床应用广泛。</p>

<h2><i class="fas fa-crosshairs mr-2 text-orange-500"></i>适应症</h2>
<div class="info-box">
<ul class="list-disc list-inside space-y-2">
<li><strong>特发性肺纤维化（IPF）</strong>：成人IPF的一线治疗</li>
<li><strong>具有进行性表型的慢性纤维化性间质性肺疾病（PF-ILD）</strong></li>
<li><strong>系统性硬化症相关间质性肺疾病（SSc-ILD）</strong></li>
<li><strong>非小细胞肺癌（NSCLC）</strong>：联合多西他赛用于腺癌二线治疗</li>
</ul>
</div>

<h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
<h3>推荐剂量</h3>
<ul>
<li><strong>标准剂量</strong>：<strong>150mg，每日2次</strong>（早晚各一次，间隔约12小时）</li>
<li>IPF、PF-ILD、SSc-ILD：每次150mg bid</li>
<li>NSCLC：每次200mg bid（第2-21天，28天一周期）</li>
</ul>

<h3>剂量调整</h3>
<ul>
<li>不耐受：可<strong>减量至100mg bid</strong></li>
<li>仍不能耐受：暂停治疗，症状缓解后重启</li>
<li><strong>不可自行调整</strong>，须遵医嘱</li>
</ul>

<h3>服用方法</h3>
<ul>
<li><strong>必须与餐同服</strong>，减少胃肠道反应</li>
<li>整粒<strong>吞服，勿压碎、咀嚼</strong></li>
<li>每日总剂量<strong>不可超过300mg</strong></li>
</ul>

<h3>特殊人群</h3>
<ul>
<li><strong>轻中度肝功能不全</strong>（Child-Pugh A）：慎用，加强监测</li>
<li><strong>重度肝功能不全</strong>：<strong>禁用</strong></li>
<li><strong>轻度肾功能不全</strong>：无需调整剂量</li>
<li><strong>中重度肾功能不全</strong>/透析：慎用</li>
<li><strong>老年人</strong>（≥65岁）：无需调整剂量</li>
<li><strong>儿童/青少年</strong>：不推荐</li>
<li><strong>妊娠期</strong>：<strong>禁用</strong></li>
<li><strong>哺乳期</strong>：用药期间停止哺乳</li>
</ul>

<h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>重要注意事项</h2>
<div class="warning-box">
<strong>腹泻管理</strong>：腹泻是<strong>最常见</strong>的不良反应（&gt;60%），首剂即可出现。①足量饮水；②轻症可用洛哌丁胺对症；③严重时医生可能减量至100mg bid；④低脂低纤维饮食可缓解。
</div>

<div class="warning-box">
<strong>肝毒性监测</strong>：前3个月<strong>每月</strong>监测ALT/AST/胆红素，之后定期复查。肝酶≥3×ULN伴症状或≥5×ULN应<strong>减量或停药</strong>。
</div>

<ul>
<li><strong>出血风险</strong>：抗凝治疗者慎用</li>
<li><strong>胃肠道穿孔</strong>：近期有腹部手术史者慎用</li>
<li><strong>伤口愈合</strong>：术前<strong>至少停药28天</strong></li>
<li><strong>绝对禁忌</strong>：对尼达尼布、花生或大豆过敏者；孕妇</li>
<li><strong>药物相互作用</strong>：
<ul>
<li>强效P-gp和CYP3A4抑制剂（酮康唑、红霉素）增加暴露</li>
<li>强效P-gp诱导剂（利福平、卡马西平）降低疗效</li>
<li>与抗凝药联用增加出血风险</li>
</ul>
</li>
<li><strong>避孕</strong>：治疗期间及停药后至少3个月内有效避孕</li>
</ul>

<h2><i class="fas fa-prescription-bottle-alt mr-2 text-orange-500"></i>规格与保存</h2>
<ul>
<li><strong>规格</strong>：软胶囊，100mg/粒、150mg/粒</li>
<li><strong>包装</strong>：印度Sun版Nindanib：150mg×10粒/盒或30粒装</li>
<li><strong>保存</strong>：&lt;25°C，避光密封，<strong>不可冷冻</strong></li>
</ul>
"""

price_rows4 = """
<tr><td>原研药</td><td>Ofev（维加特，尼达尼布）</td><td>德国勃林格殷格翰</td><td>由实际咨询为准</td></tr>
<tr><td>仿制版</td><td>Nindanib（尼达尼布）</td><td>印度Sun Pharma</td><td>由实际咨询为准</td></tr>
<tr><td>仿制版</td><td>Nintib（尼达尼布）</td><td>印度Cipla</td><td>由实际咨询为准</td></tr>
"""


# ============ 5. 地拉罗司口服混悬片 DEFRIJET (Glenmark) ============
drug5 = {
    'idx': START_IDX + 4,  # 148
    'name': '地拉罗司口服混悬片',
    'generic': '地拉罗司 (Deferasirox)',
    'brand': 'Defrijet / Exjade（恩瑞格）',
    'category': '慢性铁过载',
    'category_label': '祛铁用药',
    'filename': 'news-148-deferasirox.html',
}

content5 = """
<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品简介</h2>
<p>地拉罗司（Deferasirox）是一种<strong>口服铁螯合剂</strong>，通过与体内过量铁离子结合形成稳定的螯合物，经粪便排出体外，从而降低体内铁负荷。该药由诺华（Novartis）原研，商品名为<strong>Exjade（恩瑞格）</strong>，2005年获FDA批准用于临床，是<strong>第一个也是目前应用最广的口服祛铁药物</strong>。印度Glenmark等多家厂家生产仿制版<strong>Defrijet</strong>，已通过WHO-GMP和DCGI认证。地拉罗司主要用于治疗<strong>输血依赖型地中海贫血、骨髓增生异常综合征（MDS）等长期输血导致的慢性铁过载</strong>，以及<strong>非输血依赖性地中海贫血综合征（NTDT）</strong>患者的慢性铁过载。中国国家药品监督管理局于2024年6月批准<strong>地拉罗司颗粒（文帝平®）</strong>在国内上市，是国内首个且唯一获批治疗铁过载的颗粒剂。</p>

<h2><i class="fas fa-crosshairs mr-2 text-orange-500"></i>适应症</h2>
<div class="info-box">
<ul class="list-disc list-inside space-y-2">
<li><strong>输血依赖型慢性铁过载</strong>：2岁及以上患者因频繁输血（每月浓缩红细胞≥7mL/kg）所致</li>
<li><strong>其他输血依赖性疾病</strong>（如MDS、再生障碍性贫血、镰状细胞病等）所致铁过载</li>
<li><strong>非输血依赖性地中海贫血综合征（NTDT）</strong>：10岁及以上患者的慢性铁过载</li>
</ul>
</div>

<h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
<h3>推荐剂量</h3>
<ul>
<li><strong>输血依赖型铁过载（TDT）</strong>：
<ul>
<li>起始剂量：<strong>14mg/kg/日</strong>，口服，每日1次</li>
<li>每月接受&lt;7mL/kg浓缩红细胞者：起始可考虑<strong>7mg/kg/日</strong></li>
<li>每月接受&gt;14mL/kg者：起始可考虑<strong>21mg/kg/日</strong></li>
</ul>
</li>
<li><strong>非输血依赖型地中海贫血综合征（NTDT）</strong>：
<ul>
<li>起始剂量：<strong>7mg/kg/日</strong>，口服，每日1次</li>
<li>基线肝铁浓度（LIC）&gt;15mg Fe/g干重者，4周后可考虑<strong>增至20mg/kg/日</strong></li>
<li><strong>最大剂量不超过20mg/kg/日</strong></li>
</ul>
</li>
</ul>

<h3>剂量调整（基于血清铁蛋白）</h3>
<ul>
<li>治疗中每月监测血清铁蛋白，根据变化每3-6个月调整剂量</li>
<li>铁蛋白&lt;300μg/L：<strong>暂停治疗</strong>，并检测LIC</li>
<li>LIC&lt;3mg Fe/g干重：<strong>中断治疗</strong>，持续监测</li>
</ul>

<h3>服用方法</h3>
<ul>
<li><strong>空腹服用</strong>，餐前<strong>至少30分钟</strong>，最好每日固定时间</li>
<li><strong>不可咀嚼或整片吞服</strong>，需先分散</li>
<li>将片剂投入<strong>水、橙汁或苹果汁</strong>中搅拌至形成均匀混悬液后立即饮服
<ul>
<li>剂量&lt;1g：用约<strong>100mL（3.5盎司）</strong>液体</li>
<li>剂量≥1g：用约<strong>200mL（7盎司）</strong>液体</li>
</ul>
</li>
<li>饮服后用少量液体冲洗容器一并饮下，确保服完全量</li>
<li><strong>不可与含铝抗酸药同时服用</strong>（会降低吸收）</li>
</ul>

<h3>特殊人群</h3>
<ul>
<li><strong>eGFR&gt;60 mL/min/1.73m²</strong>：按推荐剂量</li>
<li><strong>eGFR 40-60 mL/min/1.73m²</strong>：<strong>减量50%</strong>，密切监测</li>
<li><strong>eGFR&lt;40 mL/min/1.73m²</strong>：<strong>禁用</strong></li>
<li><strong>重度肝功能不全</strong>：慎用</li>
<li><strong>儿童（2-17岁）</strong>：剂量与成人一致，按体重计算并随生长调整</li>
<li><strong>老年人</strong>：不良反应风险增加，密切监测</li>
<li><strong>孕妇</strong>：仅利大于弊时使用</li>
</ul>

<h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>重要注意事项</h2>
<div class="warning-box">
<strong>黑框警告：肾/肝功能衰竭、胃肠道出血</strong>：地拉罗司可能引起<strong>急性肾损伤（包括肾衰竭需透析）</strong>、<strong>肝毒性（包括肝衰竭）</strong>、<strong>胃肠道出血</strong>等严重甚至致命的不良反应。治疗前需<strong>重复检测</strong>血清肌酐、肝功能；治疗中<strong>每月监测</strong>肾肝功能和血常规；铁蛋白监测避免<strong>过度螯合</strong>。
</div>

<ul>
<li><strong>治疗前检查</strong>：
<ul>
<li>血清肌酐（重复2次取基线）+ eGFR</li>
<li>尿常规及血清电解质（评估肾小管功能）</li>
<li>ALT/AST/胆红素</li>
<li>血清铁蛋白</li>
<li>基线听力、眼科检查（避免感音性听力下降、晶状体混浊）</li>
</ul>
</li>
<li><strong>常见不良反应</strong>（&gt;5%）：腹泻、呕吐、恶心、腹痛、皮疹、血清肌酐升高</li>
<li><strong>严重皮肤反应</strong>：Stevens-Johnson综合征（SJS）、中毒性表皮坏死松解症（TEN）、DRESS综合征——疑似即<strong>永久停药</strong></li>
<li><strong>骨髓抑制</strong>：中性粒细胞减少、粒细胞缺乏、贫血加重、血小板减少——每月监测血常规</li>
<li><strong>绝对禁忌</strong>：eGFR&lt;40；一般状况差；高危MDS；晚期恶性肿瘤；血小板&lt;50×10⁹/L；已知过敏</li>
<li><strong>药物相互作用</strong>：
<ul>
<li>不可与含铝抗酸药、其他铁螯合剂（去铁胺、去铁酮）联用</li>
<li>慎用可能致溃疡或出血的药物（NSAIDs、糖皮质激素、口服抗凝药）</li>
<li>强效UDP-葡萄糖醛酸转移酶（UGT）诱导剂（利福平）可降低地拉罗司疗效</li>
</ul>
</li>
<li><strong>儿童/青少年</strong>：剂量同成人，但需<strong>随体重变化调整</strong></li>
</ul>

<h2><i class="fas fa-prescription-bottle-alt mr-2 text-orange-500"></i>规格与保存</h2>
<ul>
<li><strong>规格</strong>：片剂（口服混悬用），125mg/片、250mg/片、500mg/片</li>
<li><strong>中国文帝平®颗粒</strong>：180mg/袋、360mg/袋（适合儿童）</li>
<li><strong>包装</strong>：印度Glenmark版Defrijet：30片/盒</li>
<li><strong>保存</strong>：密封，&lt;30°C干燥处保存</li>
</ul>
"""

price_rows5 = """
<tr><td>原研药</td><td>Exjade（恩瑞格，地拉罗司）</td><td>瑞士诺华（Novartis）</td><td>由实际咨询为准</td></tr>
<tr><td>中国新剂型</td><td>文帝平®（地拉罗司颗粒）</td><td>西藏奥斯必秀医药</td><td>由实际咨询为准</td></tr>
<tr><td>仿制版</td><td>Defrijet（地拉罗司）</td><td>印度Glenmark</td><td>由实际咨询为准</td></tr>
"""


# 全部文章配置
all_drugs = [
    (drug1, content1, price_rows1),
    (drug2, content2, price_rows2),
    (drug3, content3, price_rows3),
    (drug4, content4, price_rows4),
    (drug5, content5, price_rows5),
]

# 生成每篇文章
os.makedirs(OUTPUT_DIR, exist_ok=True)

for drug, content, price_rows in all_drugs:
    html = template

    # 替换元数据占位符
    html = html.replace('{{DRUG_NAME}}', drug['name'])
    html = html.replace('{{GENERIC_NAME}}', drug['generic'])
    html = html.replace('{{BRAND_NAME}}', drug['brand'])
    html = html.replace('{{CATEGORY}}', drug['category'])
    html = html.replace('{{CATEGORY_LABEL}}', drug['category_label'])
    html = html.replace('{{CATEGORY_KEY}}', 'tab_drug')
    html = html.replace('{{ARTICLE_FILENAME}}', drug['filename'])
    html = html.replace('{{ARTICLE_CONTENT_PLACEHOLDER}}', content)
    html = html.replace('{{PRICE_ROWS_PLACEHOLDER}}', price_rows)

    # 保存文件 - 文章放根目录
    output_path = os.path.join('/app/data/所有对话/主对话/蓝培医疗文章', drug['filename'])
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"已生成: {drug['filename']} - {drug['name']} ({drug['brand']})")

print()
print("全部5篇文章已生成！")
print(f"输出目录: {OUTPUT_DIR}")
