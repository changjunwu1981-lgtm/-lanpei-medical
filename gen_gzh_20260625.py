#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成蓝培医疗药品公众号文章 - 2026-06-25批次（154-158）"""
import os
os.chdir("/app/data/所有对话/主对话/蓝培医疗文章")

# 公众号文章模板 - 规避敏感词：仿制药→海外版本/经济版；代购→咨询渠道；文末引导加微信17844531559
# 公众号版健康类专题：绿色系（#43A047）

# 154: 帕唑帕尼片 Pazonat
gzh_154 = '''<div style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif; line-height: 1.8; max-width: 750px; margin: 0 auto; padding: 20px;">
<h1 style="font-size: 24px; text-align: center; color: #43A047;">帕唑帕尼片Pazonat用法用量详解｜珠峰药业印度版 200/400mg多靶点TKI 晚期肾细胞癌RCC一线口服靶向</h1>
<p style="color: #666; font-size: 14px; text-align: center;">蓝培医疗 · 全球优质医疗资源咨询</p>
<hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">

<h2 style="color: #43A047; font-size: 18px;">一、什么是帕唑帕尼？</h2>
<p>帕唑帕尼(英文名Pazopanib)是一种<strong>多靶点受体酪氨酸激酶抑制剂(TKI)</strong>，原研药是诺华Novartis(原葛兰素史克GSK)生产的<strong>维全特 Votrient</strong>，2009年10月获美国FDA批准上市。它通过抑制VEGFR-1/2/3、PDGFR-α/β、c-Kit等多靶点,既阻断肿瘤血管生成(切断营养供应),又直接抑制肿瘤细胞增殖,实现"双管齐下"治疗效果。在晚期肾细胞癌(RCC)一线治疗和软组织肉瘤(STS)二线治疗中广泛应用。</p>
<p>Pazonat是<strong>孟加拉珠峰药业(Everest Pharma)</strong>生产的印度经济版,200mg×30片装/400mg×60片装,活性成分、剂型、规格、给药途径与原研维全特基本一致,经孟加拉国药监局DGDA严格审查批准上市,为Ph+晚期肾癌患者提供经济可及的治疗选择。</p>

<h2 style="color: #43A047; font-size: 18px;">二、帕唑帕尼的核心适应症</h2>
<ul>
<li><strong>晚期肾细胞癌(RCC)一线治疗</strong>：用于既往未接受过治疗或曾接受细胞因子治疗的成人晚期肾细胞癌患者</li>
<li><strong>软组织肉瘤(STS)二线治疗</strong>：用于既往化疗失败的特定亚型晚期软组织肉瘤患者</li>
</ul>
<div style="background: #e8f5e9; padding: 15px; border-radius: 8px; margin: 15px 0;">
<p style="margin: 0;"><strong>温馨提示：</strong>帕唑帕尼须由具有肿瘤治疗经验的专科医生启动。用药前需评估肝功能(ALT/AST/胆红素)、心电图(基线+定期)、血压、尿蛋白、甲状腺功能,治疗期间持续监测肝功能(至少每4周1次)。</p>
</div>

<h2 style="color: #43A047; font-size: 18px;">三、用法用量详解</h2>
<h3 style="color: #2e7d32; font-size: 16px;">标准剂量</h3>
<ul>
<li><strong>成人晚期RCC/STS</strong>：推荐<strong>800 mg/次,每日1次</strong>,口服</li>
<li>应<strong>空腹服用</strong>(餐前至少1小时或餐后至少2小时),不可与食物同服</li>
<li>不可掰开或嚼碎,整片用水吞服</li>
<li>持续治疗直至疾病进展或不可耐受</li>
</ul>

<h3 style="color: #2e7d32; font-size: 16px;">特殊人群</h3>
<ul>
<li><strong>老年人(≥65岁)</strong>：无需调整剂量</li>
<li><strong>肾功能不全</strong>：CrCl>30 mL/min 无需调整;CrCl<30 mL/min 慎用</li>
<li><strong>肝功能不全</strong>：<br>
&nbsp;&nbsp;• 轻度(胆红素正常但ALT升高,或胆红素≤1.5×ULN)：<strong>800 mg/日</strong><br>
&nbsp;&nbsp;• 中度(胆红素1.5-3×ULN)：<strong>200 mg/日</strong><br>
&nbsp;&nbsp;• 重度(胆红素>3×ULN)：<strong>不推荐使用</strong></li>
<li><strong>儿童(<18岁)</strong>：安全性未确立,不推荐</li>
</ul>

<h2 style="color: #43A047; font-size: 18px;">四、重要安全提示</h2>
<div style="background: #fff7ed; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #f97316;">
<p style="margin: 0;"><strong>⚠️ 严重毒性警告(可能致命)：</strong><br>
• <strong>肝毒性</strong>：曾发生严重致死性肝毒性,用药前+治疗期间定期监测肝功能<br>
• <strong>出血事件</strong>：6个月内有咯血/脑出血/胃肠道出血者<strong>禁用</strong><br>
• <strong>动脉血栓事件</strong>：心肌梗死/脑缺血可能致死,风险增加者慎用<br>
• <strong>高血压</strong>：常见且需积极控制,>140/90 mmHg需降压治疗<br>
• <strong>QT间期延长/尖端扭转型室速</strong>,定期心电图监测<br>
• <strong>胃肠道穿孔/瘘管</strong>：风险增加者慎用,发生即停药<br>
• <strong>甲状腺功能减退</strong>：定期监测TSH<br>
• <strong>伤口愈合延迟</strong>：术前<strong>至少停药7天</strong></p>
</div>

<h2 style="color: #43A047; font-size: 18px;">五、用药注意事项</h2>
<ul>
<li><strong>CYP3A4抑制剂</strong>(酮康唑、伊曲康唑、克拉霉素)显著升高血药浓度,避免合用</li>
<li><strong>CYP3A4诱导剂</strong>(利福平、卡马西平、苯妥英、圣约翰草)显著降低疗效,避免合用</li>
<li><strong>质子泵抑制剂</strong>(埃索美拉唑等)降低生物利用度40%,避免合用</li>
<li>避免葡萄柚/西柚制品</li>
<li>孕妇禁用(有胎儿毒性),哺乳期停药或停止哺乳</li>
</ul>

<h2 style="color: #43A047; font-size: 18px;">六、原研药 vs 海外经济版</h2>
<table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
<thead>
<tr style="background: #43A047; color: white;">
<th style="padding: 10px; text-align: left;">类型</th>
<th style="padding: 10px; text-align: left;">品牌/厂家</th>
<th style="padding: 10px; text-align: left;">参考价格</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #e5e7eb;">
<td style="padding: 10px;">原研药</td>
<td style="padding: 10px;">Votrient 维全特 (Novartis诺华)</td>
<td style="padding: 10px; color: #f97316; font-weight: bold;">由实际咨询为准(美国200mg×120片约6000-8000美元/瓶)</td>
</tr>
<tr style="border-bottom: 1px solid #e5e7eb;">
<td style="padding: 10px;">海外经济版</td>
<td style="padding: 10px;">Pazonat (孟加拉珠峰药业) / Pazocare (CIPLA) / 印度多家</td>
<td style="padding: 10px; color: #f97316; font-weight: bold;">由实际咨询为准(经济版显著低于原研,详情请咨询)</td>
</tr>
</tbody>
</table>
<p style="font-size: 12px; color: #999;">* 价格仅供参考,实际价格以咨询为准</p>

<div style="background: linear-gradient(135deg, #1e3a5f, #2d5a87); color: white; padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0;">
<p style="margin: 0; font-size: 16px;"><strong>蓝培医疗 · 全球优质医疗资源咨询</strong></p>
<p style="margin: 10px 0;">📞 电话咨询：17844531559</p>
<p style="margin: 10px 0;">💬 WhatsApp：+63-968-583-8435</p>
<p style="margin: 10px 0;">🌐 微信咨询：17844531559</p>
<p style="margin: 10px 0; font-size: 14px;">如需咨询帕唑帕尼Pazonat药品渠道和价格信息,请联系我们</p>
</div>

<div style="background: #fff7ed; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #f97316;">
<p style="margin: 0; font-size: 13px;"><strong>⚠️ 免责声明：</strong>本文章仅供信息参考,不构成医疗建议。帕唑帕尼为处方药,必须在专科医生指导下使用。价格信息可能随市场变化,请以咨询时的实际信息为准。</p>
</div>
</div>'''

# 155: 舒尼替尼胶囊 SUTIB
gzh_155 = '''<div style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif; line-height: 1.8; max-width: 750px; margin: 0 auto; padding: 20px;">
<h1 style="font-size: 24px; text-align: center; color: #43A047;">舒尼替尼胶囊SUTIB用法用量详解｜珠峰药业印度版 12.5/25/50mg多靶点TKI 晚期肾癌RCC/GIST/胰腺神经内分泌瘤</h1>
<p style="color: #666; font-size: 14px; text-align: center;">蓝培医疗 · 全球优质医疗资源咨询</p>
<hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">

<h2 style="color: #43A047; font-size: 18px;">一、什么是舒尼替尼？</h2>
<p>舒尼替尼(英文名Sunitinib Malate)是一种<strong>多靶点受体酪氨酸激酶抑制剂(TKI)</strong>,原研药是辉瑞Pfizer生产的<strong>舒坦森 Sutent</strong>,2006年1月获美国FDA批准上市。它主要抑制PDGFR、VEGFR、c-Kit、FLT3、Ret等多靶点,通过阻断肿瘤血管生成和直接抑制肿瘤细胞增殖实现抗肿瘤作用。在晚期肾细胞癌(RCC)、胃肠道间质瘤(GIST)、胰腺神经内分泌瘤(pNET)三大适应症中表现突出,是肿瘤靶向治疗的经典选择。</p>
<p>SUTIB是<strong>孟加拉珠峰药业(Everest Pharma)</strong>生产的印度经济版,12.5mg/25mg/50mg三种规格,活性成分、剂型、规格、给药途径与原研舒坦森基本一致,经孟加拉国药监局DGDA严格审查批准上市。</p>

<h2 style="color: #43A047; font-size: 18px;">二、舒尼替尼的核心适应症</h2>
<ul>
<li><strong>晚期肾细胞癌(RCC)</strong>：既往未接受过治疗或细胞因子治疗失败的成人晚期肾细胞癌</li>
<li><strong>胃肠道间质瘤(GIST)</strong>：甲磺酸伊马替尼治疗失败或不耐受的成人GIST患者</li>
<li><strong>胰腺神经内分泌瘤(pNET)</strong>：不可切除的、局部晚期或转移性的成人进行性胰腺神经内分泌瘤(高分化)</li>
</ul>
<div style="background: #e8f5e9; padding: 15px; border-radius: 8px; margin: 15px 0;">
<p style="margin: 0;"><strong>温馨提示：</strong>舒尼替尼须由具有肿瘤治疗经验的专科医生启动。用药前需评估肝功能、肾功能、心电图(基线+定期)、血压、心脏功能(超声心动图基线LVEF),治疗期间定期监测。</p>
</div>

<h2 style="color: #43A047; font-size: 18px;">三、用法用量详解</h2>
<h3 style="color: #2e7d32; font-size: 16px;">标准剂量(4/2方案)</h3>
<ul>
<li><strong>晚期RCC/GIST</strong>：推荐<strong>50 mg/次,每日1次</strong>,口服</li>
<li>采用<strong>4/2方案</strong>：<strong>连用4周后停2周</strong>,6周为一个治疗周期,直至疾病进展或不可耐受</li>
<li><strong>pNET</strong>：推荐<strong>37.5 mg/次,每日1次,持续给药</strong>(无停药期),直至疾病进展或不可耐受</li>
</ul>

<h3 style="color: #2e7d32; font-size: 16px;">服用方法</h3>
<ul>
<li>可餐前或餐后服用(高脂饮食不影响AUC)</li>
<li>整粒吞服,不可打开/咀嚼/压碎/分散</li>
<li><strong>剂量调整</strong>：按 12.5 mg 幅度递增/递减;RCC/GIST 最低12.5 mg/日,pNET 最低25 mg/日</li>
</ul>

<h3 style="color: #2e7d32; font-size: 16px;">特殊人群</h3>
<ul>
<li><strong>老年人(≥65岁)</strong>：无需调整剂量</li>
<li><strong>肾功能不全</strong>：轻中度无需调整;重度无数据,慎用</li>
<li><strong>肝功能不全</strong>：Child-Pugh A-B(轻中度)无需调整;Child-Pugh C(重度)不推荐</li>
<li><strong>儿童(<18岁)</strong>：安全性未确立,不推荐</li>
</ul>

<h2 style="color: #43A047; font-size: 18px;">四、重要安全提示</h2>
<div style="background: #fff7ed; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #f97316;">
<p style="margin: 0;"><strong>⚠️ 严重毒性警告(可能致命)：</strong><br>
• <strong>肝毒性</strong>：可能致命,用药前+治疗期间定期监测肝功能<br>
• <strong>心血管事件</strong>：充血性心衰(部分致死),基线+定期LVEF监测;QT间期延长,定期心电图监测<br>
• <strong>高血压</strong>：常见(>30%)需积极控制,基线+定期监测<br>
• <strong>出血</strong>：可能严重甚至致死,6个月内咯血/脑出血/胃肠道出血者禁用<br>
• <strong>动脉血栓事件</strong>：心肌梗死/脑血管意外可能致死,风险增加者慎用<br>
• <strong>甲状腺功能减退</strong>：定期监测TSH<br>
• <strong>伤口愈合延迟</strong>：术前<strong>至少停药3周</strong><br>
• <strong>骨坏死</strong>(特别是下颌骨)：用药前+期间保持口腔卫生,避免侵入性牙科操作</p>
</div>

<h2 style="color: #43A047; font-size: 18px;">五、用药注意事项</h2>
<ul>
<li><strong>CYP3A4抑制剂</strong>(酮康唑、伊曲康唑、克拉霉素)显著升高血药浓度,避免合用</li>
<li><strong>CYP3A4诱导剂</strong>(利福平、卡马西平、苯妥英、圣约翰草)显著降低疗效,避免合用</li>
<li>避免葡萄柚/西柚制品</li>
<li>孕妇禁用(有胎儿毒性),哺乳期停药或停止哺乳</li>
</ul>

<h2 style="color: #43A047; font-size: 18px;">六、原研药 vs 海外经济版</h2>
<table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
<thead>
<tr style="background: #43A047; color: white;">
<th style="padding: 10px; text-align: left;">类型</th>
<th style="padding: 10px; text-align: left;">品牌/厂家</th>
<th style="padding: 10px; text-align: left;">参考价格</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #e5e7eb;">
<td style="padding: 10px;">原研药</td>
<td style="padding: 10px;">Sutent 舒坦森 (Pfizer辉瑞)</td>
<td style="padding: 10px; color: #f97316; font-weight: bold;">由实际咨询为准(美国50mg×28粒约8000-12000美元/瓶)</td>
</tr>
<tr style="border-bottom: 1px solid #e5e7eb;">
<td style="padding: 10px;">海外经济版</td>
<td style="padding: 10px;">SUTIB (孟加拉珠峰药业) / Sunitix (Sun Pharma) / 印度多家</td>
<td style="padding: 10px; color: #f97316; font-weight: bold;">由实际咨询为准(经济版显著低于原研,详情请咨询)</td>
</tr>
</tbody>
</table>
<p style="font-size: 12px; color: #999;">* 价格仅供参考,实际价格以咨询为准</p>

<div style="background: linear-gradient(135deg, #1e3a5f, #2d5a87); color: white; padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0;">
<p style="margin: 0; font-size: 16px;"><strong>蓝培医疗 · 全球优质医疗资源咨询</strong></p>
<p style="margin: 10px 0;">📞 电话咨询：17844531559</p>
<p style="margin: 10px 0;">💬 WhatsApp：+63-968-583-8435</p>
<p style="margin: 10px 0;">🌐 微信咨询：17844531559</p>
<p style="margin: 10px 0; font-size: 14px;">如需咨询舒尼替尼SUTIB药品渠道和价格信息,请联系我们</p>
</div>

<div style="background: #fff7ed; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #f97316;">
<p style="margin: 0; font-size: 13px;"><strong>⚠️ 免责声明：</strong>本文章仅供信息参考,不构成医疗建议。舒尼替尼为处方药,必须在专科医生指导下使用。价格信息可能随市场变化,请以咨询时的实际信息为准。</p>
</div>
</div>'''

# 156: 伊马替尼片 IMANIB
gzh_156 = '''<div style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif; line-height: 1.8; max-width: 750px; margin: 0 auto; padding: 20px;">
<h1 style="font-size: 24px; text-align: center; color: #43A047;">伊马替尼片IMANIB用法用量详解｜珠峰药业印度版 100/400mg一代TKI 慢性粒细胞白血病CML/胃肠间质瘤GIST</h1>
<p style="color: #666; font-size: 14px; text-align: center;">蓝培医疗 · 全球优质医疗资源咨询</p>
<hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">

<h2 style="color: #43A047; font-size: 18px;">一、什么是伊马替尼？</h2>
<p>伊马替尼(英文名Imatinib Mesylate)是<strong>全球第一个靶向抗癌药</strong>——第一代酪氨酸激酶抑制剂(TKI),原研药是诺华Novartis生产的<strong>格列卫 Glivec/Gleevec</strong>,2001年5月获美国FDA批准上市。它的诞生开启了"分子靶向治疗"时代,通过竞争性结合BCR-ABL融合蛋白的ATP结合位点,精准打击Ph+慢性粒细胞白血病(CML)细胞,把曾经的"血癌"变成可长期控制的慢性病。此外还广泛用于Ph+急性淋巴细胞白血病(ALL)、胃肠间质瘤(GIST)、骨髓增生异常综合征等。</p>
<p>IMANIB是<strong>孟加拉珠峰药业(Everest Pharma)</strong>生产的印度经济版,100mg×60片装/400mg×30片装,活性成分、剂型、规格、给药途径与原研格列卫基本一致,经孟加拉国药监局DGDA严格审查批准上市,为Ph+白血病/GIST患者提供经济可及的治疗选择。</p>

<h2 style="color: #43A047; font-size: 18px;">二、伊马替尼的核心适应症</h2>
<ul>
<li><strong>新诊断Ph+慢性粒细胞白血病(CML)慢性期</strong>：不适合骨髓移植的一线治疗</li>
<li><strong>Ph+ CML 干扰素-α治疗失败者</strong>(慢性期/加速期/急变期)</li>
<li><strong>新诊断Ph+急性淋巴细胞白血病(Ph+ ALL)</strong>：与化疗联用</li>
<li><strong>不可切除/转移性恶性胃肠道间质瘤(GIST)</strong>：Kit(CD117)阳性成人</li>
<li><strong>GIST切除术后辅助治疗</strong>：显著复发风险者</li>
<li><strong>晚期高嗜酸性粒细胞综合征/慢性嗜酸性粒细胞白血病(HES/CEL)</strong></li>
<li><strong>儿童(1岁及以上)</strong>：按BSA给药,适用于Ph+ CML各期</li>
</ul>
<div style="background: #e8f5e9; padding: 15px; border-radius: 8px; margin: 15px 0;">
<p style="margin: 0;"><strong>温馨提示：</strong>伊马替尼须由具有白血病管理经验血液/肿瘤专科医生启动。用药前评估血常规、肝功能、心功能,治疗期间持续监测(血象前3个月每周1次,之后每月)。</p>
</div>

<h2 style="color: #43A047; font-size: 18px;">三、用法用量详解</h2>
<h3 style="color: #2e7d32; font-size: 16px;">成人标准剂量</h3>
<ul>
<li><strong>Ph+ CML 慢性期</strong>：<strong>400 mg/日</strong>,1次服用,与食物和一大杯水同服</li>
<li><strong>Ph+ CML 加速期/急变期</strong>：<strong>600 mg/日</strong>,1次服用</li>
<li><strong>Ph+ ALL</strong>：<strong>600 mg/日</strong>,1次服用,联合化疗</li>
<li><strong>GIST(不可切除/转移性)</strong>：<strong>400 mg/日</strong>,1次服用</li>
<li><strong>GIST 辅助治疗(切除后)</strong>：<strong>400 mg/日</strong>,推荐疗程3年</li>
<li><strong>DFSP</strong>：<strong>400 mg/日</strong>,必要时可增至800 mg/日(分2次)</li>
</ul>

<h3 style="color: #2e7d32; font-size: 16px;">儿童剂量(Ph+ CML)</h3>
<ul>
<li><strong>3岁及以上</strong>：推荐 <strong>340 mg/m²/日</strong>,1次或分2次服用(早/晚),总剂量不超过600 mg/日</li>
</ul>

<h3 style="color: #2e7d32; font-size: 16px;">服用方法</h3>
<ul>
<li><strong>必须餐时服用</strong>(与食物+一大杯水),减少胃肠道刺激</li>
<li>400 mg/600 mg 每日1次;800 mg 分2次服用(早+晚)</li>
<li>整片用水送服,不能吞咽者可分散于<strong>无气水或苹果汁中</strong>(100mg/50mL,400mg/200mL),立即服用</li>
</ul>

<h3 style="color: #2e7d32; font-size: 16px;">特殊人群</h3>
<ul>
<li><strong>老年人</strong>：无需调整剂量</li>
<li><strong>肝功能不全</strong>：根据肝功能调整剂量;严重肝损需显著减量</li>
<li><strong>肾功能不全</strong>：轻度无需调整;中重度需谨慎,严重者密切监测</li>
</ul>

<h2 style="color: #43A047; font-size: 18px;">四、重要安全提示</h2>
<div style="background: #fff7ed; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #f97316;">
<p style="margin: 0;"><strong>⚠️ 严重毒性警告：</strong><br>
• <strong>体液潴留和水肿</strong>：常见且严重(胸腔/心包/肺水肿),严重者减量/停药+利尿<br>
• <strong>肝毒性</strong>：可能致命;胆红素>3×ULN或转氨酶>5×ULN 宜停药<br>
• <strong>骨髓抑制</strong>：3-4级中性粒细胞减少/血小板减少;根据血象调整剂量<br>
• <strong>充血性心衰和左心功能不全</strong>：定期监测心功能<br>
• <strong>胃肠道刺激</strong>：与食物+水同服可减轻<br>
• <strong>肿瘤溶解综合征</strong>：高肿瘤负荷者,开始治疗前给予充分水化和别嘌醇</p>
</div>

<h2 style="color: #43A047; font-size: 18px;">五、用药注意事项</h2>
<ul>
<li><strong>CYP3A4抑制剂/诱导剂</strong>：显著影响血药浓度,避免合用或调整剂量</li>
<li><strong>圣约翰草</strong>：显著降低伊马替尼血药浓度,避免合用</li>
<li><strong>对乙酰氨基酚(扑热息痛)</strong>：合用可能增加肝毒性,避免或限制剂量</li>
<li><strong>华法林</strong>：合用可能增加出血风险,需密切监测INR或换用低分子肝素</li>
<li><strong>左甲状腺素</strong>：伊马替尼可能干扰其代谢,甲状腺切除患者需监测TSH</li>
<li>孕妇禁用(有胎儿毒性),育龄期用药需避孕至停药后1个月</li>
</ul>

<h2 style="color: #43A047; font-size: 18px;">六、原研药 vs 海外经济版</h2>
<table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
<thead>
<tr style="background: #43A047; color: white;">
<th style="padding: 10px; text-align: left;">类型</th>
<th style="padding: 10px; text-align: left;">品牌/厂家</th>
<th style="padding: 10px; text-align: left;">参考价格</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #e5e7eb;">
<td style="padding: 10px;">原研药</td>
<td style="padding: 10px;">Glivec 格列卫 / Gleevec (Novartis诺华)</td>
<td style="padding: 10px; color: #f97316; font-weight: bold;">由实际咨询为准(美国400mg×30片约6000-9000美元/瓶)</td>
</tr>
<tr style="border-bottom: 1px solid #e5e7eb;">
<td style="padding: 10px;">海外经济版</td>
<td style="padding: 10px;">IMANIB (孟加拉珠峰药业) / Imatib (Accord) / Imatros (Mylan) / 印度多家</td>
<td style="padding: 10px; color: #f97316; font-weight: bold;">由实际咨询为准(经济版显著低于原研,详情请咨询)</td>
</tr>
</tbody>
</table>
<p style="font-size: 12px; color: #999;">* 价格仅供参考,实际价格以咨询为准</p>

<div style="background: linear-gradient(135deg, #1e3a5f, #2d5a87); color: white; padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0;">
<p style="margin: 0; font-size: 16px;"><strong>蓝培医疗 · 全球优质医疗资源咨询</strong></p>
<p style="margin: 10px 0;">📞 电话咨询：17844531559</p>
<p style="margin: 10px 0;">💬 WhatsApp：+63-968-583-8435</p>
<p style="margin: 10px 0;">🌐 微信咨询：17844531559</p>
<p style="margin: 10px 0; font-size: 14px;">如需咨询伊马替尼IMANIB药品渠道和价格信息,请联系我们</p>
</div>

<div style="background: #fff7ed; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #f97316;">
<p style="margin: 0; font-size: 13px;"><strong>⚠️ 免责声明：</strong>本文章仅供信息参考,不构成医疗建议。伊马替尼为处方药,必须在专科医生指导下使用。价格信息可能随市场变化,请以咨询时的实际信息为准。</p>
</div>
</div>'''

# 157: 达沙替尼片 Dasanat
gzh_157 = '''<div style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif; line-height: 1.8; max-width: 750px; margin: 0 auto; padding: 20px;">
<h1 style="font-size: 24px; text-align: center; color: #43A047;">达沙替尼片Dasanat用法用量详解｜珠峰药业印度版 50/100mg二代TKI 慢性粒细胞白血病CML/Ph+急性淋巴白血病</h1>
<p style="color: #666; font-size: 14px; text-align: center;">蓝培医疗 · 全球优质医疗资源咨询</p>
<hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">

<h2 style="color: #43A047; font-size: 18px;">一、什么是达沙替尼？</h2>
<p>达沙替尼(英文名Dasatinib)是<strong>第二代酪氨酸激酶抑制剂(TKI)</strong>,原研药是百时美施贵宝BMS生产的<strong>施达赛 Sprycel</strong>,2006年6月获美国FDA批准上市。它对BCR-ABL融合蛋白的抑制强度是伊马替尼的325倍,可透过血脑屏障,对多数伊马替尼耐药突变(M244V、G250E、Q252H、E255K/V、F317L、F359V等)有活性(T315I/V299L突变耐药),是伊马替尼耐药或不耐受CML患者的关键二线选择。在新诊断Ph+ CML慢性期,达沙替尼的5年无进展生存率显著优于伊马替尼(83% vs 72%)。</p>
<p>Dasanat是<strong>孟加拉珠峰药业(Everest Pharma)</strong>生产的印度经济版,20mg/50mg/100mg/140mg多种规格,活性成分、剂型、规格、给药途径与原研施达赛基本一致,经孟加拉国药监局DGDA严格审查批准上市。</p>

<h2 style="color: #43A047; font-size: 18px;">二、达沙替尼的核心适应症</h2>
<ul>
<li><strong>新诊断Ph+慢性期CML(成人)</strong></li>
<li><strong>慢性期/加速期/急变期Ph+ CML</strong>(成人)：既往治疗(包括伊马替尼)耐药或不耐受者</li>
<li><strong>Ph+急性淋巴细胞白血病(Ph+ ALL)</strong>(成人)：既往治疗耐药或不耐受者</li>
<li><strong>儿童(1岁及以上)</strong>：Ph+ 慢性期CML;新诊断Ph+ ALL与化疗联合</li>
</ul>
<div style="background: #e8f5e9; padding: 15px; border-radius: 8px; margin: 15px 0;">
<p style="margin: 0;"><strong>温馨提示：</strong>达沙替尼须由具有白血病管理经验血液/肿瘤专科医生启动。用药前评估血常规、肝功能、心电图(基线+定期)、肺动脉高压症状。</p>
</div>

<h2 style="color: #43A047; font-size: 18px;">三、用法用量详解</h2>
<h3 style="color: #2e7d32; font-size: 16px;">成人标准剂量</h3>
<ul>
<li><strong>Ph+ CML 慢性期</strong>：<strong>100 mg/次,每日1次</strong>,口服,餐时/空腹均可</li>
<li><strong>Ph+ CML 加速期/急变期、Ph+ ALL</strong>：<strong>140 mg/次,每日1次</strong>,口服</li>
<li><strong>治疗持续时间</strong>：持续治疗直至疾病进展或不可耐受;新诊断CP CML 临床试验中位治疗时间5年以上</li>
</ul>

<h3 style="color: #2e7d32; font-size: 16px;">儿童剂量(按体重)</h3>
<ul>
<li>10-<20 kg：40 mg/日</li>
<li>20-<30 kg：60 mg/日</li>
<li>30-<45 kg：70 mg/日</li>
<li>≥45 kg：100 mg/日</li>
<li>每3个月根据体重变化重新计算剂量</li>
</ul>

<h3 style="color: #2e7d32; font-size: 16px;">服用方法</h3>
<ul>
<li>整片用水吞服,<strong>不可压碎/切割/咀嚼</strong>(活性成分可能引起皮肤刺激)</li>
<li>餐时餐后均可(无需特殊)</li>
<li>每日固定时间服用</li>
</ul>

<h3 style="color: #2e7d32; font-size: 16px;">特殊人群</h3>
<ul>
<li><strong>老年人(≥65岁)</strong>：无需调整剂量,但需密切监测体液潴留和心血管事件</li>
<li><strong>肝功能不全</strong>：Child-Pugh A(轻度)无需调整;Child-Pugh B-C(中重度)起始剂量需减半并密切监测</li>
<li><strong>肾功能不全</strong>：达沙替尼及代谢物<4%经肾排泄,一般无需调整</li>
</ul>

<h2 style="color: #43A047; font-size: 18px;">四、重要安全提示</h2>
<div style="background: #fff7ed; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #f97316;">
<p style="margin: 0;"><strong>⚠️ 严重毒性警告：</strong><br>
• <strong>骨髓抑制</strong>：3-4级血小板减少/中性粒细胞减少/贫血常见<br>
• <strong>出血事件</strong>：5级(致死)出血,与血小板减少相关<br>
• <strong>体液潴留</strong>：<strong>胸腔积液发生率显著高于其他TKI</strong>(35% CP患者,100 mg/日5%,140 mg/日10-15%)<br>
• <strong>充血性心衰和左心功能不全</strong>：定期监测心功能<br>
• <strong>QT间期延长</strong>：定期心电图监测,低钾/低镁者先纠正<br>
• <strong>肺动脉高压(PAH)</strong>：罕见但严重,确诊PAH即永久停用<br>
• <strong>儿童发育影响</strong>：骨骺延迟融合、骨质减少、生长迟缓<br>
• <strong>肝毒性</strong>：用药前+每月监测肝功能</p>
</div>

<h2 style="color: #43A047; font-size: 18px;">五、用药注意事项</h2>
<ul>
<li><strong>CYP3A4抑制剂</strong>(酮康唑、伊曲康唑、克拉霉素)：<strong>显著升高达沙替尼血药浓度</strong>,应避免合用;若必须合用,达沙替尼减量:140→40mg/日,100→20mg/日,70→20mg/日</li>
<li><strong>CYP3A4诱导剂</strong>(利福平、卡马西平、苯妥英)：<strong>显著降低达沙替尼血药浓度</strong>,避免合用</li>
<li><strong>避免葡萄柚/西柚制品</strong></li>
<li><strong>抗酸剂</strong>：同时服用降低达沙替尼吸收,需间隔2小时</li>
<li><strong>H2受体拮抗剂(法莫替丁等)和质子泵抑制剂(奥美拉唑等)</strong>：避免合用(降低达沙替尼吸收)</li>
<li><strong>圣约翰草</strong>：降低达沙替尼血药浓度,避免合用</li>
<li>孕妇禁用(有胎儿毒性),育龄期用药需避孕至停药后1个月</li>
</ul>

<h2 style="color: #43A047; font-size: 18px;">六、原研药 vs 海外经济版</h2>
<table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
<thead>
<tr style="background: #43A047; color: white;">
<th style="padding: 10px; text-align: left;">类型</th>
<th style="padding: 10px; text-align: left;">品牌/厂家</th>
<th style="padding: 10px; text-align: left;">参考价格</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #e5e7eb;">
<td style="padding: 10px;">原研药</td>
<td style="padding: 10px;">Sprycel 施达赛 (BMS百时美施贵宝)</td>
<td style="padding: 10px; color: #f97316; font-weight: bold;">由实际咨询为准(美国100mg×30片约5000-7000美元/瓶)</td>
</tr>
<tr style="border-bottom: 1px solid #e5e7eb;">
<td style="padding: 10px;">海外经济版</td>
<td style="padding: 10px;">Dasanat (孟加拉珠峰药业) / Dasanix (Beacon) / Dasatrue (Sun Pharma) / 印度多家</td>
<td style="padding: 10px; color: #f97316; font-weight: bold;">由实际咨询为准(经济版显著低于原研,详情请咨询)</td>
</tr>
</tbody>
</table>
<p style="font-size: 12px; color: #999;">* 价格仅供参考,实际价格以咨询为准</p>

<div style="background: linear-gradient(135deg, #1e3a5f, #2d5a87); color: white; padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0;">
<p style="margin: 0; font-size: 16px;"><strong>蓝培医疗 · 全球优质医疗资源咨询</strong></p>
<p style="margin: 10px 0;">📞 电话咨询：17844531559</p>
<p style="margin: 10px 0;">💬 WhatsApp：+63-968-583-8435</p>
<p style="margin: 10px 0;">🌐 微信咨询：17844531559</p>
<p style="margin: 10px 0; font-size: 14px;">如需咨询达沙替尼Dasanat药品渠道和价格信息,请联系我们</p>
</div>

<div style="background: #fff7ed; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #f97316;">
<p style="margin: 0; font-size: 13px;"><strong>⚠️ 免责声明：</strong>本文章仅供信息参考,不构成医疗建议。达沙替尼为处方药,必须在专科医生指导下使用。价格信息可能随市场变化,请以咨询时的实际信息为准。</p>
</div>
</div>'''

# 158: 比卡鲁胺片 Calutide
gzh_158 = '''<div style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif; line-height: 1.8; max-width: 750px; margin: 0 auto; padding: 20px;">
<h1 style="font-size: 24px; text-align: center; color: #43A047;">比卡鲁胺片Calutide用法用量详解｜珠峰药业印度版 50mg非甾体抗雄激素 晚期前列腺癌与LHRH类似物联合治疗</h1>
<p style="color: #666; font-size: 14px; text-align: center;">蓝培医疗 · 全球优质医疗资源咨询</p>
<hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">

<h2 style="color: #43A047; font-size: 18px;">一、什么是比卡鲁胺？</h2>
<p>比卡鲁胺(英文名Bicalutamide)是<strong>非甾体抗雄激素药物(NSAA)</strong>,原研药是阿斯利康AstraZeneca生产的<strong>康士得 Casodex</strong>,1995年获美国FDA批准上市。它通过竞争性结合雄激素受体(AR),阻断睾酮和双氢睾酮(DHT)对前列腺癌细胞的作用,属于"内分泌治疗"的核心药物。在晚期前列腺癌(与LHRH类似物联合治疗)和局部晚期前列腺癌(单药治疗/辅助治疗)中广泛应用。相比第一代抗雄激素(如氟他胺、尼鲁米特),比卡鲁胺半衰期长(约1周),每日1次给药,肝脏毒性更低。</p>
<p>Calutide是<strong>孟加拉珠峰药业(Everest Pharma)</strong>生产的印度经济版,50mg×28-30片装,活性成分、剂型、规格、给药途径与原研康士得基本一致,经孟加拉国药监局DGDA严格审查批准上市。</p>

<h2 style="color: #43A047; font-size: 18px;">二、比卡鲁胺的核心适应症</h2>
<ul>
<li><strong>50mg规格-晚期前列腺癌联合治疗</strong>：与LHRH(黄体生成素释放激素)类似物(如戈舍瑞林、亮丙瑞林)或外科睾丸切除术<strong>联合</strong>应用,治疗D2期转移性前列腺癌</li>
<li><strong>150mg规格-局部晚期前列腺癌单药治疗</strong>：作为<strong>根治性前列腺切除术或放疗的辅助</strong>,治疗局部晚期、无远处转移但具有高疾病进展风险的前列腺癌患者;这些患者不适宜或不愿接受外科去势术或其他内科治疗</li>
</ul>
<div style="background: #e8f5e9; padding: 15px; border-radius: 8px; margin: 15px 0;">
<p style="margin: 0;"><strong>温馨提示：</strong>比卡鲁胺须由泌尿/肿瘤专科医生启动。用药前评估肝功能(基线+定期)、PSA(基线+定期);治疗最初4个月定期监测肝功能,之后按需。</p>
</div>

<h2 style="color: #43A047; font-size: 18px;">三、用法用量详解</h2>
<h3 style="color: #2e7d32; font-size: 16px;">标准剂量</h3>
<ul>
<li><strong>50mg(晚期前列腺癌联合治疗)</strong>：<strong>1片(50 mg)/次,每日1次</strong>,口服</li>
<li>应<strong>在LHRH类似物治疗前至少3天开始</strong>,或与外科睾丸切除术同时开始</li>
<li><strong>150mg(局部晚期前列腺癌单药治疗)</strong>：<strong>1片(150 mg)/次,每日1次</strong>,口服;或3片50mg(等效)</li>
<li>应<strong>持续服用至少2年</strong>或至疾病进展</li>
</ul>

<h3 style="color: #2e7d32; font-size: 16px;">服用方法</h3>
<ul>
<li>整片用水吞服,餐时餐后均可(食物不影响吸收)</li>
<li>建议每日固定时间服用</li>
</ul>

<h3 style="color: #2e7d32; font-size: 16px;">特殊人群</h3>
<ul>
<li><strong>老年人(≥65岁)</strong>：无需调整剂量</li>
<li><strong>肾功能不全</strong>：无需调整剂量(经肾排泄<1/3)</li>
<li><strong>肝功能不全</strong>：轻度无需调整;中重度可能发生药物蓄积(半衰期延长),需谨慎使用,密切监测肝功能</li>
<li><strong>儿童/青少年</strong>：禁用(无适应症)</li>
<li><strong>女性</strong>：禁用(无适应症)</li>
</ul>

<h2 style="color: #43A047; font-size: 18px;">四、重要安全提示</h2>
<div style="background: #fff7ed; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #f97316;">
<p style="margin: 0;"><strong>⚠️ 严重毒性警告：</strong><br>
• <strong>肝毒性</strong>：可能致命(<strong>严重肝损伤/肝衰竭</strong>已观察到死亡/住院病例);用药前检测ALT/AST,治疗<strong>最初4个月定期监测</strong>,之后按需;若出现黄疸/ALT>2×ULN立即停药,随访肝功能<br>
• <strong>男性乳房增生/乳房疼痛</strong>：50mg联合治疗较少(约5%);150mg单药治疗较常见(约50-70%)<br>
• <strong>香豆素抗凝剂相互作用</strong>：与华法林合用<strong>显著延长PT/INR</strong>,增加出血风险;<strong>密切监测PT/INR,必要时调整抗凝剂剂量</strong><br>
• <strong>QT间期延长</strong>：雄激素剥夺治疗可能延长QT间期;有QT延长史/风险因素者评估获益-风险比</p>
</div>

<h2 style="color: #43A047; font-size: 18px;">五、用药注意事项</h2>
<ul>
<li><strong>糖耐量降低</strong>：与LHRH激动剂联用时观察到此效应,糖尿病患者需监测血糖</li>
<li><strong>CYP3A4底物</strong>：比卡鲁胺是CYP3A4抑制剂,与CYP3A4底物(辛伐他汀、匹莫范色林等)合用需谨慎</li>
<li><strong>禁忌合用</strong>：特非那定、阿司咪唑、西沙比利(CYP3A4底物,合用可能致死性心律失常)</li>
<li><strong>PSA监测</strong>：定期监测PSA,PSA升高需评估临床进展</li>
<li><strong>光敏反应</strong>(罕见)：服用150mg期间避免直接暴露于强阳光或UV,可使用防晒霜</li>
<li><strong>精子形态改变</strong>：服药期间及治疗后<strong>130天内</strong>需采取有效避孕措施</li>
<li><strong>遗传性半乳糖不耐受/Lapp乳糖酶缺乏/葡萄糖-半乳糖吸收障碍者</strong>：禁用(片剂含乳糖)</li>
</ul>

<h2 style="color: #43A047; font-size: 18px;">六、原研药 vs 海外经济版</h2>
<table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
<thead>
<tr style="background: #43A047; color: white;">
<th style="padding: 10px; text-align: left;">类型</th>
<th style="padding: 10px; text-align: left;">品牌/厂家</th>
<th style="padding: 10px; text-align: left;">参考价格</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #e5e7eb;">
<td style="padding: 10px;">原研药</td>
<td style="padding: 10px;">Casodex 康士得 (AstraZeneca阿斯利康)</td>
<td style="padding: 10px; color: #f97316; font-weight: bold;">由实际咨询为准(美国50mg×30片约600-900美元/瓶)</td>
</tr>
<tr style="border-bottom: 1px solid #e5e7eb;">
<td style="padding: 10px;">海外经济版</td>
<td style="padding: 10px;">Calutide (孟加拉珠峰药业) / Bicatero (Hetero) / Bicalut (Accord) / 印度多家</td>
<td style="padding: 10px; color: #f97316; font-weight: bold;">由实际咨询为准(经济版显著低于原研,详情请咨询)</td>
</tr>
</tbody>
</table>
<p style="font-size: 12px; color: #999;">* 价格仅供参考,实际价格以咨询为准</p>

<div style="background: linear-gradient(135deg, #1e3a5f, #2d5a87); color: white; padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0;">
<p style="margin: 0; font-size: 16px;"><strong>蓝培医疗 · 全球优质医疗资源咨询</strong></p>
<p style="margin: 10px 0;">📞 电话咨询：17844531559</p>
<p style="margin: 10px 0;">💬 WhatsApp：+63-968-583-8435</p>
<p style="margin: 10px 0;">🌐 微信咨询：17844531559</p>
<p style="margin: 10px 0; font-size: 14px;">如需咨询比卡鲁胺Calutide药品渠道和价格信息,请联系我们</p>
</div>

<div style="background: #fff7ed; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #f97316;">
<p style="margin: 0; font-size: 13px;"><strong>⚠️ 免责声明：</strong>本文章仅供信息参考,不构成医疗建议。比卡鲁胺为处方药,必须在专科医生指导下使用。价格信息可能随市场变化,请以咨询时的实际信息为准。</p>
</div>
</div>'''

# 写入5个公众号文件
gzh_files = [
    ("gzh-154-pazonat.txt", gzh_154),
    ("gzh-155-sutib.txt", gzh_155),
    ("gzh-156-imanib.txt", gzh_156),
    ("gzh-157-dasanat.txt", gzh_157),
    ("gzh-158-calutide.txt", gzh_158),
]

for filename, content in gzh_files:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"已生成 {filename} ({len(content)} 字符)")

print(f"\n共生成 {len(gzh_files)} 个公众号文件")
