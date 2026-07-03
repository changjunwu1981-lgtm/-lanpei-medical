#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成5篇药品用法用量文章（序号 149-153）
- 序号从149开始（已covered 144个，文件最大序号148，避免冲突）
- 5个未覆盖药品：DEFRATAJ, Regonat, COMTRIPSY, ZAFIMOVE, RELGIN
"""
import os

TEMPLATE_PATH = '/app/data/所有对话/主对话/蓝培医疗文章/news-148-deferasirox.html'
OUTPUT_DIR = '/app/data/所有对话/主对话/蓝培医疗文章'

with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    base = f.read()

# 修正：把硬编码的"祛铁用药"统一为"药闻速递"
base = base.replace('祛铁用药', '药闻速递')

START_IDX = 149

# ============ 1. 地拉罗司分散片 DEFRATAJ (MANKIND) ============
content1 = """
<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品简介</h2>
<p>地拉罗司（Deferasirox）是一种<strong>口服活性铁螯合剂</strong>，能高度选择性地与三价铁（Fe³⁺）结合，形成稳定的 2:1 复合物并主要经粪便排出体外。它对锌、铜的亲和力低，不会引起这两种金属的持续血清浓度降低。地拉罗司由诺华（Novartis）原研，商品名为 <strong>Exjade / Jadenu（恩瑞格）</strong>，2005 年获 FDA 批准，是目前临床应用最广泛的口服铁螯合剂之一。DEFRATAJ 是印度 Mankind Pharma 生产的印度经济版（125/250/500 mg 分散片），与原研品生物等效，是广大地中海贫血、骨髓增生异常综合征（MDS）、镰状细胞病等长期输血患者长期治疗的经济选择。</p>

<h2><i class="fas fa-crosshairs mr-2 text-orange-500"></i>适应症</h2>
<div class="info-box">
<ul class="list-disc list-inside space-y-2">
<li><strong>输血依赖性慢性铁过载</strong>：2 岁及以上、经常输血（≥7 mL/kg/月浓缩红细胞）的患者</li>
<li><strong>非输血依赖性地中海贫血综合征（NTDT）</strong>：10 岁及以上、肝铁浓度（LIC）≥5 mg Fe/g 干重 且 血清铁蛋白＞300 µg/L 的患者</li>
<li>其他长期输血导致的慢性铁过载（如 MDS、镰状细胞病、再生障碍性贫血等）</li>
</ul>
</div>

<h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
<h3>推荐起始剂量（按适应症区分）</h3>
<ul>
<li><strong>输血依赖性铁过载（≥2岁）</strong>：起始 <strong>20 mg/kg/日</strong>，每日 1 次口服（空腹或与清淡饮食同服均可）</li>
<li><strong>输血量大的患者</strong>（>14 mL/kg/月红细胞，约＞4 单位/月）：可考虑 <strong>30 mg/kg/日</strong> 起始</li>
<li><strong>输血量小的患者</strong>（<7 mL/kg/月红细胞，约＜2 单位/月）：可考虑 <strong>10 mg/kg/日</strong> 起始</li>
<li><strong>非输血依赖性地中海贫血（NTDT）</strong>：起始 <strong>10 mg/kg/日</strong></li>
</ul>

<h3>剂量调整</h3>
<ul>
<li><strong>监测频率</strong>：每月监测血清铁蛋白，每 3-6 个月依据趋势调整剂量</li>
<li><strong>调整步长</strong>：每次 5-10 mg/kg，根据个体反应与治疗目标（维持或减低铁负荷）</li>
<li><strong>目标范围</strong>：血清铁蛋白控制在 500-1000 µg/L</li>
<li><strong>最大剂量</strong>：分散片 40 mg/kg/日（不可超量）</li>
<li><strong>减停时机</strong>：铁蛋白持续＜500 µg/L 时考虑暂停治疗，避免过度螯合</li>
</ul>

<h3>服用方法</h3>
<ul>
<li>空腹或与<strong>清淡饮食</strong>同服（高脂餐会显著增加吸收）</li>
<li>分散片须<strong>整片吞服</strong>或碾碎后混入软食（酸奶/苹果泥）立即服用，<strong>不可贮存后补服</strong></li>
<li>每日固定时间服用，用适量水送服</li>
<li><strong>不可与含铝制酸剂同服</strong>（影响吸收）</li>
</ul>

<h3>特殊人群</h3>
<ul>
<li><strong>儿童（2-5岁）</strong>：仅限输血依赖性铁过载，剂量同成人按 kg 计算</li>
<li><strong>老年人</strong>：无需调整起始剂量，但需密切监测</li>
<li><strong>肾功能不全</strong>：eGFR 40-60 mL/min/1.73 m² 减量 50%；<strong>eGFR＜40 禁用</strong></li>
<li><strong>肝功能不全</strong>：中重度肝功能不全需严密监测；重度禁用</li>
</ul>

<h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>重要安全警告</h2>
<div class="warning-box">
<strong>⚠️ 黑框警告：肾衰、肝衰、胃肠道出血</strong><br>
地拉罗司可能引起：<br>
• <strong>急性肾损伤</strong>（包括需透析的肾衰和 Fanconi 综合征）<br>
• <strong>肝毒性</strong>（包括肝衰竭）<br>
• <strong>胃肠道出血、溃疡和刺激</strong>
</div>

<div class="warning-box">
<strong>⚠️ 严格禁忌</strong>：<br>
• eGFR＜40 mL/min/1.73 m²<br>
• 体能状态差（PS 评分差）<br>
• 高危 MDS、晚期恶性肿瘤<br>
• 血小板＜50×10⁹/L<br>
• 对地拉罗司过敏者
</div>

<ul>
<li><strong>用药前必查</strong>：血清肌酐（双次）、ALT/AST/胆红素、血常规、铁蛋白、听力、眼科</li>
<li><strong>用药期间</strong>：<strong>每月</strong>监测血肌酐与肝功能；每月监测铁蛋白；<strong>每 12 个月</strong>检查听力与视力</li>
<li><strong>骨髓抑制</strong>：可能引起中性粒细胞减少、粒细胞缺乏、贫血加重、血小板减少（包括致命事件），需监测血常规</li>
<li><strong>严重皮肤反应</strong>：Stevens-Johnson 综合征（SJS）、中毒性表皮坏死松解症（TEN）、DRESS 综合征——一旦疑似立即停药</li>
<li><strong>超敏反应</strong>：严重过敏需立即停药并医学干预</li>
<li><strong>儿童与老年</strong>：需特别密切监测毒性</li>
<li><strong>妊娠</strong>：仅利大于弊时使用</li>
<li><strong>哺乳期</strong>：用药期间及最后剂量后 1 个月内避免哺乳</li>
</ul>

<h2><i class="fas fa-prescription-bottle-alt mr-2 text-orange-500"></i>规格与保存</h2>
<ul>
<li><strong>规格</strong>：分散片 125 mg / 250 mg / 500 mg</li>
<li><strong>包装</strong>：印度 Mankind DEFRATAJ 常见 30 片/盒</li>
<li><strong>保存</strong>：密封、25°C 以下干燥处，避光防潮</li>
</ul>
"""

price_rows1 = """
<tr><td>原研药</td><td>Exjade / Jadenu（恩瑞格，地拉罗司）</td><td>瑞士诺华 Novartis</td><td>由实际咨询为准</td></tr>
<tr><td>印度经济版</td><td>DEFRATAJ（地拉罗司分散片）</td><td>印度 Mankind Pharma</td><td>由实际咨询为准</td></tr>
<tr><td>印度经济版</td><td>DEFRIJET（地拉罗司分散片）</td><td>印度 Glenmark</td><td>由实际咨询为准</td></tr>
"""

# ============ 2. 瑞戈非尼 Regonat (CIPLA) ============
content2 = """
<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品简介</h2>
<p>瑞戈非尼（Regorafenib）是一种<strong>口服多激酶抑制剂</strong>，通过抑制 VEGFR1-3、PDGFR-β、FGFR1、KIT、RET、BRAF、BRAF V600E、RAF-1 等多种与肿瘤血管生成、肿瘤微环境和肿瘤增殖相关的激酶发挥抗肿瘤作用。它由拜耳（Bayer）原研，商品名为 <strong>Stivarga（拜万戈）</strong>，2012 年获 FDA 批准，是首个被证实对难治性 mCRC 和 HCC 均有效的口服多激酶抑制剂。Regonat 是印度 Cipla 生产的印度经济版（40 mg×28 片），获印度 CDSCO 批准上市，质量和原研品生物等效，是肝癌、结直肠癌、胃肠道间质瘤患者重要的经济治疗选择。</p>

<h2><i class="fas fa-crosshairs mr-2 text-orange-500"></i>适应症</h2>
<div class="info-box">
<ul class="list-disc list-inside space-y-2">
<li><strong>转移性结直肠癌（mCRC）</strong>：经氟尿嘧啶、奥沙利铂、伊立替康化疗以及抗 VEGF 治疗失败的患者（若 RAS 野生型还需经抗 EGFR 治疗失败）</li>
<li><strong>胃肠道间质瘤（GIST）</strong>：经伊马替尼和舒尼替尼治疗后进展或不能耐受的局部晚期不可切除/转移性患者</li>
<li><strong>肝细胞癌（HCC）</strong>：经索拉非尼治疗失败的患者</li>
</ul>
</div>

<h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
<h3>推荐标准剂量</h3>
<ul>
<li><strong>标准剂量</strong>：<strong>160 mg</strong>（4 片 × 40 mg），<strong>每日 1 次</strong>，口服</li>
<li><strong>服药周期</strong>：连续服药 <strong>21 天（3 周）</strong>，停药 <strong>7 天（1 周）</strong>，每 28 天为一个治疗周期</li>
<li><strong>持续时间</strong>：直至疾病进展或出现不可耐受的毒性</li>
</ul>

<h3>NCCN 推荐剂量爬坡方案（mCRC 备选）</h3>
<ul>
<li>第 1 周：80 mg/日（2 片）</li>
<li>第 2 周：120 mg/日（3 片）</li>
<li>第 3 周：160 mg/日（4 片）</li>
<li>第 4 周：停药休息</li>
<li>之后每个周期维持上周期最后剂量</li>
</ul>

<h3>剂量调整（按 40 mg/次阶梯）</h3>
<ul>
<li><strong>最大剂量</strong>：160 mg/日</li>
<li><strong>最低剂量</strong>：80 mg/日</li>
<li><strong>调整时机</strong>：按不良反应严重程度调整</li>
</ul>

<h3>服用方法</h3>
<ul>
<li><strong>每日固定时间</strong>服用，整片吞服，配水送服</li>
<li><strong>必须随低脂餐服用</strong>（&lt;600 卡路里，&lt;30% 脂肪），低脂餐后生物利用度最佳</li>
<li><strong>不可与高脂餐同服</strong>（影响吸收）</li>
<li>漏服当天想起尽快补服，<strong>不可次日双倍补服</strong></li>
<li>服药后呕吐<strong>不再补服</strong>，按计划服下一次</li>
</ul>

<h3>特殊人群</h3>
<ul>
<li><strong>肾功能不全</strong>：无需调整剂量；透析患者无推荐剂量</li>
<li><strong>肝功能不全</strong>：轻中度（胆红素≤3×ULN）无需调整，需密切监测；<strong>重度（胆红素&gt;3×ULN）不推荐使用</strong></li>
<li><strong>老年人</strong>：≥65 岁更易出现手足皮肤反应、肝毒性，应密切监测</li>
<li><strong>儿童（＜18 岁）</strong>：安全性未确立</li>
<li><strong>PS 2 及以上</strong>：临床数据有限，慎用</li>
</ul>

<h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>重要安全警告</h2>
<div class="warning-box">
<strong>⚠️ 黑框警告：肝毒性</strong><br>
瑞戈非尼可引起严重甚至致命的肝毒性。治疗前需查肝功能（ALT/AST/胆红素），治疗期间<strong>前 2 个月每 2 周</strong>监测肝功，之后每月或按需监测。如出现不明嗜睡或精神状态改变，需检测血氨并及时处理。
</div>

<ul>
<li><strong>感染风险</strong>：所有级别感染发生率 32%，≥3 级 9%，最常见为尿路感染、鼻咽炎、真菌感染、肺炎；严重感染可致命</li>
<li><strong>出血风险</strong>：严重甚至致命出血，一旦出现需永久停药</li>
<li><strong>胃肠道穿孔/瘘管</strong>：可致命，需警惕</li>
<li><strong>手足皮肤反应（HFSR）</strong>：最常见不良反应之一（≥20%），严重时需减量或停药</li>
<li><strong>高血压</strong>：治疗前 6 周每周监测血压，之后定期监测</li>
<li><strong>心肌缺血/梗死</strong>：新发或急性心缺血需停药，恢复后评估</li>
<li><strong>可逆性后部白质脑病综合征（RPLS）</strong>：需永久停药</li>
<li><strong>伤口愈合受损</strong>：择期手术前<strong>至少停药 2 周</strong>，大手术后至少 2 周内不可给药</li>
<li><strong>胚胎-胎儿毒性</strong>：育龄期女性治疗期间及最后剂量后 2 个月内避孕；男性也需在最后剂量后 2 个月内避孕</li>
<li><strong>哺乳期</strong>：治疗期间及最后剂量后 2 周内禁止哺乳</li>
</ul>

<h2><i class="fas fa-prescription-bottle-alt mr-2 text-orange-500"></i>规格与保存</h2>
<ul>
<li><strong>规格</strong>：40 mg/片薄膜衣片</li>
<li><strong>包装</strong>：印度 Cipla Regonat 常见 28 片/瓶</li>
<li><strong>保存</strong>：25°C 以下密封保存，避光防潮</li>
</ul>
"""

price_rows2 = """
<tr><td>原研药</td><td>Stivarga（拜万戈，瑞戈非尼）</td><td>德国拜耳 Bayer</td><td>由实际咨询为准</td></tr>
<tr><td>印度经济版</td><td>Regonat（瑞戈非尼 40mg）</td><td>印度 Cipla</td><td>由实际咨询为准</td></tr>
"""

# ============ 3. 曲氟尿苷替匹嘧啶 COMTRIPSY (Natco) ============
content3 = """
<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品简介</h2>
<p>曲氟尿苷替匹嘧啶（Trifluridine/Tipiracil，简称 TAS-102）是一种<strong>口服复方细胞毒抗肿瘤药物</strong>，由两种活性成分组成：<strong>曲氟尿苷（Trifluridine）</strong>是胸腺嘧啶核苷类似物，能掺入肿瘤细胞 DNA 干扰其合成；<strong>替匹嘧啶（Tipiracil）</strong>是胸苷磷酸化酶抑制剂，通过抑制 TPD 酶对曲氟尿苷的降解，提高其血浆浓度与生物利用度。该复方由日本大鹏药品（Taiho Pharmaceutical）原研，商品名为 <strong>Lonsurf（朗斯弗）</strong>，2015 年获 FDA 批准，是难治性 mCRC 和转移性胃癌的重要三线治疗选择。COMTRIPSY 是印度 Natco 生产的印度经济版（15 mg/6.14 mg 与 20 mg/8.19 mg 两种规格），与原研品生物等效。</p>

<h2><i class="fas fa-crosshairs mr-2 text-orange-500"></i>适应症</h2>
<div class="info-box">
<ul class="list-disc list-inside space-y-2">
<li><strong>转移性结直肠癌（mCRC）</strong>：单药或与贝伐珠单抗联合，用于经氟尿嘧啶、奥沙利铂、伊立替康化疗及抗 VEGF 治疗（若 RAS 野生型还需经抗 EGFR 治疗）失败的患者</li>
<li><strong>转移性胃癌/胃食管交界处腺癌</strong>：经至少两线化疗（含氟尿嘧啶、铂类、紫杉醇或伊立替康，HER2 阳性者还需 HER2 靶向治疗）失败的患者</li>
</ul>
</div>

<h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
<h3>标准推荐剂量（按体表面积 BSA 计算）</h3>
<ul>
<li><strong>基础剂量</strong>：<strong>35 mg/m²</strong>（以曲氟尿苷计）</li>
<li><strong>给药频率</strong>：<strong>每日 2 次</strong>（早晚餐后约 1 小时内服用）</li>
<li><strong>服药周期</strong>：每个 28 天周期内，<strong>第 1-5 天</strong> + <strong>第 8-12 天</strong> 服药（共 10 天服药），其余时间停药休息</li>
</ul>

<h3>按 BSA 调整的每次剂量（向上取整到 5 mg）</h3>
<ul>
<li><strong>BSA ＜1.07 m²</strong>：35 mg/次</li>
<li><strong>BSA 1.07-1.23 m²</strong>：40 mg/次</li>
<li><strong>BSA 1.23-1.38 m²</strong>：45 mg/次</li>
<li><strong>BSA 1.38-1.60 m²</strong>：50 mg/次</li>
<li><strong>BSA 1.60-1.83 m²</strong>：55 mg/次</li>
<li><strong>BSA 1.83-2.05 m²</strong>：60 mg/次</li>
<li><strong>BSA ≥2.05 m²</strong>：65 mg/次</li>
<li><strong>单次最大剂量</strong>：80 mg/次（160 mg/日）</li>
</ul>

<h3>服用方法</h3>
<ul>
<li><strong>餐时或餐后 1 小时内</strong>服用（食物不影响曲氟尿苷吸收，可减轻恶心）</li>
<li><strong>整片吞服</strong>，不可压碎、掰开或咀嚼（细胞毒药物，<strong>操作时请戴手套</strong>）</li>
<li>漏服或服药后呕吐：<strong>不必补服</strong>，按计划服下一次</li>
<li>建议每日大量饮水（≥2L/日）以减少尿中药物结晶</li>
</ul>

<h3>剂量调整</h3>
<ul>
<li><strong>首次减量</strong>：每次减 5 mg/m²（如 35→30 mg/m²）</li>
<li><strong>第二次减量</strong>：减至 25 mg/m²</li>
<li><strong>若仍不耐受</strong>：永久停药</li>
<li><strong>3 级发热性中性粒细胞减少或 4 级骨髓抑制</strong>：暂停用药至 ≤1 级，再低一剂量重启</li>
</ul>

<h3>特殊人群</h3>
<ul>
<li><strong>肾功能不全</strong>：轻中度（30-89 mL/min）无需调整；<strong>重度（15-29 mL/min）</strong>推荐 20 mg/m²；&lt;15 mL/min 不推荐</li>
<li><strong>肝功能不全</strong>：轻度无需调整；<strong>中重度（胆红素＞1.5×ULN）不推荐使用</strong></li>
<li><strong>老年人（≥65 岁）</strong>：无需调整剂量，但需更密切监测骨髓抑制</li>
<li><strong>儿童（＜18 岁）</strong>：安全性未确立</li>
<li><strong>妊娠</strong>：禁用（致畸风险）</li>
<li><strong>哺乳期</strong>：用药期间及最后剂量后 1 周内停止哺乳</li>
</ul>

<h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>重要安全提示</h2>
<ul>
<li><strong>骨髓抑制</strong>：最常见最严重的不良反应——<br>
&nbsp;&nbsp;• 中性粒细胞减少（70%）、贫血（60%）、血小板减少（40%）<br>
&nbsp;&nbsp;• <strong>每周期第 1 天和第 15 天</strong>必须查全血细胞计数<br>
&nbsp;&nbsp;• 中性粒细胞绝对值＜0.5×10⁹/L 时停药并使用 G-CSF</li>
<li><strong>胃肠道反应</strong>：恶心（30%）、食欲下降（30%）、腹泻（25%）、呕吐（20%）——可预防性给予 5-HT3 抑制剂止吐；腹泻可用洛哌丁胺</li>
<li><strong>乏力/疲乏</strong>：常见，需充分休息</li>
<li><strong>感染风险</strong>：化疗常见，需警惕发热</li>
<li><strong>避免妊娠</strong>：育龄期女性治疗期间及最后剂量后 6 个月内采取有效避孕</li>
</ul>

<h2><i class="fas fa-prescription-bottle-alt mr-2 text-orange-500"></i>规格与保存</h2>
<ul>
<li><strong>规格</strong>：15 mg/6.14 mg 与 20 mg/8.19 mg 两种片剂</li>
<li><strong>包装</strong>：印度 Natco COMTRIPSY 常见 20 片/盒（含 15mg 与 20mg 两种规格）</li>
<li><strong>保存</strong>：20-25°C 室温保存（15-30°C 允许），<strong>瓶内有干燥剂请勿服用</strong>；如脱离原瓶保存，<strong>30 天后未用完须丢弃</strong></li>
</ul>
"""

price_rows3 = """
<tr><td>原研药</td><td>Lonsurf 朗斯弗（曲氟尿苷替匹嘧啶）</td><td>日本大鹏药品 Taiho</td><td>由实际咨询为准</td></tr>
<tr><td>印度经济版</td><td>COMTRIPSY（曲氟尿苷替匹嘧啶片）</td><td>印度 Natco</td><td>由实际咨询为准</td></tr>
"""

# ============ 4. 沙芬酰胺 ZAFIMOVE (Emcure) ============
content4 = """
<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品简介</h2>
<p>沙芬酰胺（Safinamide）是一种<strong>新型多机制抗帕金森病药物</strong>，具有双重作用机制：<strong>① 高选择性、不可逆抑制 B 型单胺氧化酶（MAO-B）</strong>，减少脑内多巴胺降解，延长多巴胺作用时间；<strong>② 抑制电压门控钠通道</strong>，调节异常谷氨酸释放，间接减轻多巴胺能神经元过度兴奋，可能具有神经保护作用。该药由意大利 Newron Pharmaceuticals 与德国 Meiji Seika 合作研发，商品名为 <strong>Xadago</strong>，2015 年获欧盟 EMA 批准，2017 年获 FDA 批准，用于中晚期帕金森病的"剂末波动"治疗。ZAFIMOVE 是印度 Emcure Pharmaceuticals 生产的印度经济版（50 mg×10 片 / 100 mg×10 片），与原研品生物等效，是帕金森病患者长期联合治疗的经济选择。</p>

<h2><i class="fas fa-crosshairs mr-2 text-orange-500"></i>适应症</h2>
<div class="info-box">
<ul class="list-disc list-inside space-y-2">
<li><strong>中晚期原发性帕金森病的辅助治疗</strong>：作为左旋多巴（L-dopa）单药或联合其他抗帕金森药物的添加治疗，适用于出现"剂末现象"（motor fluctuations，"开-关"现象）的患者</li>
<li>FDA 适应症：作为左旋多巴/卡比多巴的辅助治疗，用于帕金森病"off"期发作患者</li>
</ul>
</div>

<h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
<h3>标准剂量（阶梯式调整）</h3>
<ul>
<li><strong>起始剂量</strong>：<strong>50 mg/次，每日 1 次</strong>，口服</li>
<li><strong>维持剂量</strong>：用药 2 周后，根据患者临床反应与耐受性，可增加至 <strong>100 mg/日</strong>（最大剂量）</li>
<li><strong>不可超量</strong>：超过 100 mg/日未证明有额外获益，反而增加不良反应</li>
</ul>

<h3>服用方法</h3>
<ul>
<li>口服给药，<strong>整片吞服</strong>，配水送服</li>
<li><strong>餐前餐后均可</strong>（进食不影响吸收）</li>
<li>建议<strong>每日固定时间</strong>服用，保持血药浓度稳定</li>
<li><strong>漏服处理</strong>：想起时若接近下次服药时间则跳过，<strong>不可双倍补服</strong></li>
</ul>

<h3>特殊人群</h3>
<ul>
<li><strong>老年人</strong>：65 岁以上无需调整剂量；<strong>75 岁以上临床数据有限</strong>，慎用</li>
<li><strong>肝功能不全</strong>：<br>
&nbsp;&nbsp;• 轻度：无需调整<br>
&nbsp;&nbsp;• 中度：<strong>最大剂量 50 mg/日</strong>，进展为重度需停药<br>
&nbsp;&nbsp;• <strong>重度：禁用</strong></li>
<li><strong>肾功能不全</strong>：无需调整剂量</li>
<li><strong>儿童（＜18 岁）</strong>：安全性未确立，不推荐</li>
<li><strong>妊娠</strong>：可能对胎儿有害，育龄期女性治疗期间及停药后 2 周内有效避孕</li>
<li><strong>哺乳期</strong>：应停止哺乳或停药</li>
</ul>

<h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>重要安全提示</h2>
<div class="warning-box">
<strong>⚠️ 严格禁忌</strong>：<br>
• 与其他 MAO 抑制剂（包括司来吉兰、雷沙吉兰）合用<br>
• 与<strong>哌替啶</strong>及其衍生物、曲马多、美沙酮、丙氧芬合用（致命 5-HT 综合征风险）<br>
• 与右美沙芬、SSRI/SNRI（如氟西汀、舍曲林、文拉法辛）、三环类抗抑郁药、环苯扎林、圣约翰草合用<br>
• 严重肝功能不全患者<br>
• <strong>白化病、视网膜变性、葡萄膜炎、遗传性视网膜病、严重增殖性糖尿病视网膜病变</strong>患者<br>
• 已知对沙芬酰胺过敏者
</div>

<ul>
<li><strong>高血压</strong>：可能引起或加重高血压，治疗期间应监测血压；避免摄入极大量酪胺类食物</li>
<li><strong>5-羟色胺综合征</strong>：与 SSRI 联用风险升高，临床应使用最低有效剂量的 SSRI</li>
<li><strong>嗜睡/突然入睡</strong>：可能引起日间嗜睡或突然入睡发作（驾驶、操作机器时危险），发生应考虑停药</li>
<li><strong>异动症</strong>：可能诱发或加重异动症，可通过减少左旋多巴剂量缓解</li>
<li><strong>幻觉/精神病样行为</strong>：可能诱发幻觉，伴严重精神疾病者通常不用</li>
<li><strong>冲动控制障碍</strong>：可能引起病理性赌博、性欲亢进、强迫性购物等行为</li>
<li><strong>停药综合征</strong>：快速减量或停药可能引起高热、意识混乱、肌强直（类似恶性综合征）</li>
<li><strong>眼科监测</strong>：有视网膜/黄斑变性、葡萄膜炎史者定期监测视力</li>
<li><strong>手术</strong>：择期手术前<strong>至少停药 7 天</strong></li>
</ul>

<h2><i class="fas fa-prescription-bottle-alt mr-2 text-orange-500"></i>规格与保存</h2>
<ul>
<li><strong>规格</strong>：50 mg / 100 mg 薄膜衣片</li>
<li><strong>包装</strong>：印度 Emcure ZAFIMOVE 常见 10 片/盒</li>
<li><strong>保存</strong>：25°C 以下干燥处，避光防潮</li>
</ul>
"""

price_rows4 = """
<tr><td>原研药</td><td>Xadago（沙芬酰胺 50mg/100mg）</td><td>意大利 Newron / 英国 Supernus</td><td>由实际咨询为准</td></tr>
<tr><td>印度经济版</td><td>ZAFIMOVE（沙芬酰胺 50mg/100mg）</td><td>印度 Emcure Pharmaceuticals</td><td>由实际咨询为准</td></tr>
<tr><td>印度经济版</td><td>Xafinact（沙芬酰胺 50mg/100mg）</td><td>印度 Sun Pharma</td><td>由实际咨询为准</td></tr>
"""

# ============ 5. 雷沙吉兰 RELGIN (Hetero) ============
content5 = """
<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品简介</h2>
<p>雷沙吉兰（Rasagiline）是一种<strong>第二代不可逆选择性 B 型单胺氧化酶抑制剂（MAO-B inhibitor）</strong>，通过选择性、不可逆地抑制 MAO-B，减少脑内多巴胺降解，提高多巴胺浓度，从而改善帕金森病的运动症状。其主要代谢产物 1-氨基茚满（1-aminoindan）不是苯丙胺类物质，可能具有神经保护作用（通过刺激蛋白激酶 C 磷酸化、下调 PKC 等多途径减少细胞死亡）。该药由 Teva（梯瓦）原研，商品名为 <strong>Azilect（安齐来）</strong>，2006 年获 FDA 批准。RELGIN 是印度 Hetero Labs 生产的印度经济版（0.5 mg/1 mg×30 片），与原研品生物等效，是帕金森病单药治疗与联合治疗中广泛使用的经济选择。</p>

<h2><i class="fas fa-crosshairs mr-2 text-orange-500"></i>适应症</h2>
<div class="info-box">
<ul class="list-disc list-inside space-y-2">
<li><strong>原发性帕金森病的单药治疗</strong>（早期 PD，无剂末波动时）</li>
<li><strong>与左旋多巴联合治疗</strong>，用于出现"剂末波动"的中晚期 PD 患者，减少"off"期时间</li>
</ul>
</div>

<h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
<h3>推荐剂量（按治疗方案区分）</h3>
<ul>
<li><strong>单药治疗</strong>：<strong>1 mg/次，每日 1 次</strong>，口服</li>
<li><strong>作为左旋多巴辅助治疗</strong>：<br>
&nbsp;&nbsp;• 起始：<strong>0.5 mg/次，每日 1 次</strong><br>
&nbsp;&nbsp;• 耐受良好但反应不足时：可增至 <strong>1 mg/次，每日 1 次</strong><br>
&nbsp;&nbsp;• 与左旋多巴联用时，可考虑减少左旋多巴剂量（避免异动症/幻觉）</li>
</ul>

<h3>服用方法</h3>
<ul>
<li>口服给药，<strong>餐前餐后均可</strong>（高脂饮食使 Cmax 降低约 60%，但 AUC 无明显影响）</li>
<li>每日<strong>固定时间</strong>服用，保持血药浓度稳定</li>
<li>整片吞服，配水送服</li>
<li><strong>漏服处理</strong>：想起时若接近下次服药时间则跳过，<strong>不可双倍补服</strong></li>
</ul>

<h3>特殊人群</h3>
<ul>
<li><strong>老年人</strong>：无需调整剂量</li>
<li><strong>肝功能不全</strong>：<br>
&nbsp;&nbsp;• 轻度：<strong>≤0.5 mg/日</strong><br>
&nbsp;&nbsp;• 中度：<strong>禁用</strong><br>
&nbsp;&nbsp;• 重度：<strong>绝对禁用</strong></li>
<li><strong>肾功能不全</strong>：轻中度无需调整；重度缺乏数据，慎用</li>
<li><strong>CYP1A2 抑制剂合用</strong>（如环丙沙星）：<strong>≤0.5 mg/日</strong>（AUC 升高 83%）</li>
<li><strong>儿童（＜18 岁）</strong>：安全性未确立，不推荐</li>
<li><strong>妊娠</strong>：FDA C 级，仅利大于弊时使用</li>
<li><strong>哺乳期</strong>：建议停药或停止哺乳</li>
<li><strong>手术患者</strong>：择期手术需<strong>停用雷沙吉兰至少 14 天</strong></li>
</ul>

<h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>重要安全提示</h2>
<div class="warning-box">
<strong>⚠️ 严格禁忌（致命性相互作用风险）</strong>：<br>
• <strong>阿片类镇痛药</strong>：哌替啶（度冷丁）、曲马多、美沙酮、丙氧芬<br>
• <strong>止咳药</strong>：右美沙芬<br>
• <strong>抗抑郁药</strong>：圣约翰草、米氮平、环苯扎林、MAOI、SSRI/SNRI/三环类<br>
• <strong>拟交感神经药</strong>：含伪麻黄碱、麻黄碱的感冒药/减肥药<br>
• 嗜铬细胞瘤患者、需全麻的择期手术患者<br>
• <strong>中重度肝功能不全</strong>
</div>

<ul>
<li><strong>5-羟色胺综合征</strong>：与 SSRI/SNRI/三环类抗抑郁药联用可发生高热、肌阵挛、意识改变，需间隔 14 天洗脱期</li>
<li><strong>高血压危象</strong>：与拟交感神经药或大量酪胺类食物（陈年奶酪、腌制肉类、酵母提取物、红酒、啤酒等）同服可诱发</li>
<li><strong>嗜睡/突然入睡</strong>：可能引起日间嗜睡或突然入睡发作（驾驶、操作机器时危险）</li>
<li><strong>体位性低血压</strong>：与左旋多巴联用时常见，治疗初期 2 个月最多见</li>
<li><strong>异动症</strong>：与左旋多巴联用时可能诱发或加重，可通过减少左旋多巴剂量缓解</li>
<li><strong>幻觉/精神病样行为</strong>：可能诱发幻觉，伴严重精神疾病者慎用</li>
<li><strong>冲动控制障碍</strong>：可能引起病理性赌博、性欲亢进、强迫性购物等</li>
<li><strong>皮肤黑色素瘤</strong>：PD 患者本身黑色素瘤风险升高，用药期间定期皮肤检查</li>
<li><strong>停药综合征</strong>：快速停药可能引起恶性综合征样表现（高热、肌强直、意识改变）</li>
<li><strong>联合治疗时左旋多巴减量</strong>：6-17% 患者需减少左旋多巴剂量（平均减 7-13%）</li>
</ul>

<h2><i class="fas fa-prescription-bottle-alt mr-2 text-orange-500"></i>规格与保存</h2>
<ul>
<li><strong>规格</strong>：0.5 mg / 1 mg 片剂</li>
<li><strong>包装</strong>：印度 Hetero RELGIN 常见 30 片/盒</li>
<li><strong>保存</strong>：15-30°C 干燥处，避光防潮</li>
</ul>
"""

price_rows5 = """
<tr><td>原研药</td><td>Azilect 安齐来（甲磺酸雷沙吉兰 1mg）</td><td>以色列 Teva 梯瓦</td><td>由实际咨询为准</td></tr>
<tr><td>印度经济版</td><td>RELGIN（甲磺酸雷沙吉兰 0.5mg/1mg）</td><td>印度 Hetero Labs</td><td>由实际咨询为准</td></tr>
"""

# 药品元信息
drugs = [
    {
        'idx': START_IDX,  # 149
        'name': '地拉罗司分散片',
        'generic': '地拉罗司 (Deferasirox)',
        'brand': 'DEFRATAJ',
        'category': '祛铁用药 / 慢性铁过载',
        'category_label': '药闻速递',
        'filename': 'news-149-defrataj.html',
        'content': content1,
        'price_rows': price_rows1,
    },
    {
        'idx': START_IDX + 1,  # 150
        'name': '瑞戈非尼片',
        'generic': '瑞戈非尼 (Regorafenib)',
        'brand': 'Regonat',
        'category': '肝癌 / 多激酶抑制剂',
        'category_label': '药闻速递',
        'filename': 'news-150-regonat.html',
        'content': content2,
        'price_rows': price_rows2,
    },
    {
        'idx': START_IDX + 2,  # 151
        'name': '曲氟尿苷替匹嘧啶片',
        'generic': '曲氟尿苷/替匹嘧啶 (Trifluridine/Tipiracil)',
        'brand': 'COMTRIPSY',
        'category': '结直肠癌 / TAS-102',
        'category_label': '药闻速递',
        'filename': 'news-151-comtripsy.html',
        'content': content3,
        'price_rows': price_rows3,
    },
    {
        'idx': START_IDX + 3,  # 152
        'name': '沙芬酰胺片',
        'generic': '沙芬酰胺 (Safinamide)',
        'brand': 'ZAFIMOVE',
        'category': '帕金森病 / MAO-B抑制剂',
        'category_label': '药闻速递',
        'filename': 'news-152-zafimove.html',
        'content': content4,
        'price_rows': price_rows4,
    },
    {
        'idx': START_IDX + 4,  # 153
        'name': '雷沙吉兰片',
        'generic': '雷沙吉兰 (Rasagiline)',
        'brand': 'RELGIN',
        'category': '帕金森病 / MAO-B抑制剂',
        'category_label': '药闻速递',
        'filename': 'news-153-relgin.html',
        'content': content5,
        'price_rows': price_rows5,
    },
]

# 生成HTML文件
for d in drugs:
    html = base
    # 替换药品元信息
    html = html.replace('地拉罗司口服混悬片', d['name'])
    html = html.replace('地拉罗司 (Deferasirox)', d['generic'])
    html = html.replace('Defrijet / Exjade（恩瑞格）', d['brand'])
    html = html.replace('慢性铁过载', d['category'].split(' / ')[0])
    # 替换article-content placeholder
    html = html.replace('<!-- ARTICLE_CONTENT_PLACEHOLDER -->', d['content'])
    # 替换price-rows placeholder
    html = html.replace('<!-- PRICE_ROWS_PLACEHOLDER -->', d['price_rows'])
    # 替换url中的id
    html = html.replace('news-148-deferasirox.html', d['filename'])
    # 替换ld+json中的name和url
    html = html.replace('地拉罗司口服混悬片用法用量指南', f"{d['name']}用法用量指南")
    html = html.replace('地拉罗司口服混悬片用法用量详解及原研药仿制药价格对比', f"{d['name']}用法用量详解及原研药仿制药价格对比")
    html = html.replace('地拉罗司口服混悬片', d['name'])
    html = html.replace('地拉罗司 (Deferasirox)', d['generic'])

    # 修改文件名为对应
    filepath = os.path.join(OUTPUT_DIR, d['filename'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"已生成: {filepath} ({os.path.getsize(filepath)} bytes)")

print("\n=== 完成 ===")
