#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 6月23日 行业资讯文章：6月22日5款创新药同日获批事件深度解读"""
import os

# 文章内容数据
TITLE = "6月22日NMPA\"五箭齐发\"：5款创新药同日获批，国产\"全球首创\"占比创新高，创新药\"全球同步\"窗口全面打开"
DESC = "2026年6月22日，国家药监局一日批准5款创新药上市，含全球首个实体瘤CAR-T(科济药业恺力美)、全球首个双抗ADC(百利天恒宜泽康)、全球首个狂犬病双抗(智翔金泰金速希)、国内首个口服SERD(礼来择叙)及国产首个加南类抗菌肽(普莱医药普亦克)。受理到获批最快仅6个月，6月当月13款创新药获批创同期新高。"
KEYWORDS = "NMPA,创新药获批,实体瘤CAR-T,双抗ADC,伦康依隆妥单抗,舒瑞基奥仑赛,蓝培医疗,2026年6月"

# 主内容
CONTENT = """<p>2026年6月22日，<strong>中国医药行业迎来历史性一天</strong>。国家药品监督管理局通过优先审评、附条件批准等加速通道，<strong>一日之内批准5款创新药上市</strong>——其中2款为\"全球首创\"（First-in-class），覆盖实体瘤细胞治疗、双抗ADC、狂犬病预防、乳腺癌靶向、抗感染五大刚需赛道。当日A股创新药板块探底回升，科创创新药ETF先跌5%后几乎收回，昭衍新药、华森制药、众生药业封涨停，<strong>科济药业港股单日涨超8%</strong>。6月当月获批数已达13款，创同期新高。这一\"五箭齐发\"事件被业内视为<strong>国产创新药\"从跟跑到领跑\"的标志性拐点</strong>。</p>

<!-- 数据卡片 -->
<div class="grid grid-cols-2 md:grid-cols-4 gap-4 my-6">
    <div class="data-card">
        <div class="number text-orange-500">5款</div>
        <div class="label">单日获批创新药</div>
    </div>
    <div class="data-card">
        <div class="number text-orange-500">2款</div>
        <div class="label">全球首创（First-in-class）</div>
    </div>
    <div class="data-card">
        <div class="number text-orange-500">6个月</div>
        <div class="label">最快审评周期（受理到获批）</div>
    </div>
    <div class="data-card">
        <div class="number text-orange-500">84亿美元</div>
        <div class="label">双抗ADC海外授权最高纪录</div>
    </div>
</div>

<h2><i class="fas fa-lightbulb mr-2 text-orange-500"></i>一、五款新药全景透视：含金量远超\"例行审批\"</h2>

<p>本次获批的5款创新药覆盖五大治疗领域，每款都具备打破现有治疗格局的潜力，<strong>完全不是普通新药审批</strong>。我们逐一看清这\"五箭\"的实质：</p>

<p><strong>第1箭：舒瑞基奥仑赛注射液（恺力美）——全球首款实体瘤CAR-T。</strong>科济药业旗下恺兴生命科技（上海）申报，<strong>用于CLDN18.2阳性、HER2阴性、至少二线治疗失败的晚期胃/食管胃结合部腺癌</strong>。这款产品的标志性意义在于：过去所有CAR-T细胞治疗仅能针对白血病、淋巴瘤等血液肿瘤，而<strong>占全部癌症90%的实体瘤（包括胃癌、肺癌、食管癌等）一直缺乏成熟细胞治疗方案</strong>。III期临床数据显示，所有接受舒瑞基奥仑赛输注的108例受试者中位总生存期（mOS）达<strong>9.17个月</strong>，而未使用该药的TPC组仅3.98个月（HR 0.288），安全性方面3级CRS仅4例，无4-5级CRS及任何ICANS发生。</p>

<p><strong>第2箭：注射用伦康依隆妥单抗（宜泽康）——全球首个双抗ADC。</strong>成都百利多特生物（百利天恒688506.SH）研发，<strong>用于既往经至少二线系统化疗和PD-1/PD-L1抑制剂治疗失败的复发/转移性鼻咽癌</strong>。这是全球首创EGFR×HER3双抗ADC，DAR值稳定在8。<strong>从NDA受理到获批仅6个月</strong>，III期BL-B01D1-303研究（n=386）显示客观缓解率（ORR）<strong>54.6% vs 化疗组27.0%</strong>，2025年10月《柳叶刀》主刊发表。更具标杆意义的是：<strong>2023年12月BMS以84亿美元获得其海外权益，首付款8亿美元</strong>，创全球ADC单药对外授权纪录。</p>

<p><strong>第3箭：斯乐韦米单抗注射液（金速希）——全球首个狂犬病双特异性抗体。</strong>智翔金泰（688443.SH）自主研发，<strong>用于成人狂犬病病毒暴露者的被动免疫</strong>，是目前剂量最小的狂犬病被动免疫制剂。中国每年狂犬病暴露后处置人次超千万，临床刚需巨大。</p>

<p><strong>第4箭：甲苯磺酸依仑司群片（择叙/INLURIYO）——国内首个口服SERD。</strong>礼来公司申报，<strong>用于ER+/HER2-/ESR1突变的局部晚期或转移性乳腺癌</strong>，是国内乳腺癌领域首个且目前唯一获批的口服选择性雌激素受体降解剂，填补了乳腺癌内分泌治疗的重要空白。</p>

<p><strong>第5箭：培来加南喷雾剂（普亦克）——国产首个加南类抗菌肽。</strong>普莱医药（江苏）申报，<strong>用于治疗Ⅰ度或浅Ⅱ度烧烫伤继发创面感染</strong>，属非抗生素类广谱抗感染药物，对超级细菌MRSA和含NDM-1基因多重耐药鲍曼不动杆菌均具有强效杀菌优势，<strong>应对抗生素耐药\"全球性难题\"提供中国方案</strong>。</p>

<h2><i class="fas fa-gavel mr-2 text-orange-500"></i>二、政策端三大变化：从\"审评提速\"到\"支付+定价+保护\"全链条松绑</h2>

<p>\"五箭齐发\"并非偶然事件，<strong>背后是政策红利在2026年集中落地</strong>，从顶层定价、审评审批、医保支付、资本市场四大维度全面松绑赋能：</p>

<p><strong>1. 顶层定价：1-5年价格保护期真金白银落地。</strong>国家明确全球首创1类创新药上市后给予1-5年价格稳定保护期，保护期内不强制大幅降价，暂不纳入常规集采；改良型新药设短期稳定周期；仿制药依旧集采控价。\"好坏创新一刀切\"时代正式结束，<strong>真正原创者有了保护</strong>。</p>

<p><strong>2. 审评审批：30日快速临床试验通道 + 6个月最快获批周期。</strong>国家药监局针对新靶点、新机制1类创新药、罕见病药、细胞基因治疗药物开通专属服务。本次获批的核心品种如百利天恒的双抗ADC，<strong>从受理到获批仅6个月</strong>，创历史最快纪录。</p>

<p><strong>3. 医保支付：双目录机制+预申报+商保扩面，\"高价创新药\"再无销售天花板。</strong>2026医保目录调整最大变革为：①首次同步推出商业健康保险创新药专属目录，<strong>\"医保保基础、商保保高价特效药\"双支付时代正式开启</strong>；②6月1日-10日首次设立预申报机制，未拿到正式批件的新药可提前申报，<strong>新药上市到进入医保的时间差被大幅压缩约一年</strong>；③附条件上市药申报期最长可延至8年，罕见病用药单独通道保留。</p>

<p><strong>4. 资本市场：科创板第五套标准重启+地方产业基金，研发资金不再\"卡脖子\"。</strong>证监会优化科创板第五套上市标准，重新放开未盈利创新药企上市通道；多地出台生物医药产业基金，定向补贴临床研发、海外BD授权，<strong>缓解创新药企长期研发资金压力</strong>。</p>

<div class="info-box">
<strong>6月数据：单月13款创新药获批，创同期新高。</strong>本次\"五箭齐发\"后，截至6月22日<strong>当月已有13款创新药获批上市</strong>，医药产业创新活力持续释放。其中包括：6月8日荣昌生物泰它西普获批两项新适应症（干燥综合征、IgA肾病，<strong>全球首款干燥综合征生物药</strong>）；6月9日再鼎医药维替索妥尤单抗（<strong>全球首个靶向组织因子ADC</strong>）获批治疗宫颈癌等。
</div>

<h2><i class="fas fa-users mr-2 text-orange-500"></i>三、对患者的三重影响：用药时间窗口、可及性、可负担性全面改善</h2>

<p>从患者视角，5款创新药密集获批+政策松绑，带来三个根本性变化：</p>

<p><strong>第一，时间窗口大幅前移。</strong>过去一款新药从临床到上市普遍需要3-5年，<strong>现在通过\"突破性治疗+附条件审批\"双通道最快6个月</strong>。本次获批的实体瘤CAR-T、全球首个双抗ADC，<strong>从NDA受理到获批仅6个月</strong>，意味着海外患者要等3-5年才能用上的前沿疗法，中国患者可实现\"全球同步获知、提前介入\"。</p>

<p><strong>第二，疑难癌种\"从无药可用\"到\"中国方案\"。</strong>本次获批的<strong>舒瑞基奥仑赛（恺力美）</strong>是<strong>全球首款实体瘤CAR-T</strong>，填补了CAR-T在占90%癌症的实体瘤领域长期空白；<strong>伦康依隆妥单抗（宜泽康）</strong>是<strong>全球首个双抗ADC</strong>，为既往经多线治疗失败的复发/转移性鼻咽癌患者带来54.6%的客观缓解率（vs 化疗27.0%）。这些全球首创的\"中国方案\"，<strong>让海外患者远赴重洋、动辄等待数年才能获取的前沿疗法，得以在国内与海外同步可及</strong>。</p>

<p><strong>第三，可负担性逐步改善。</strong>伴随2026年医保目录调整\"双目录+预申报+分层定价\"组合拳落地，未来创新药进入医保的周期将从\"上市后等1年\"压缩至\"同步预申报\"，商保目录同步覆盖ADC、CAR-T、基因治疗等高价创新药。<strong>但需特别提醒：商保报销需以个人保单条款为准，医保支付受DRG/DIP控费、医院药占比考核等多重因素影响</strong>，新药入院仍需1-2年过渡期。蓝培医疗可协助对接国内顶级专家资源，为患者提供第二诊疗意见与全球新药格局解读。</p>

<div class="warning-box">
<strong>用药安全提醒</strong>：上述5款创新药均为处方药，必须在具备肿瘤/感染/急救等专科诊疗资质的医院、经相应专科医生评估后使用。用药前需完善<strong>基线影像学、HER2/CLDN18.2等靶点检测、肝肾功能、心功能等基线评估</strong>。治疗期间需定期监测不良反应（实体瘤CAR-T重点监测细胞因子释放综合征CRS与免疫效应细胞相关神经毒性综合征ICANS；双抗ADC重点监测间质性肺炎与皮肤毒性）。靶点检测建议在有资质的病理科进行，避免假阴性/假阳性。具体用药方案与可及性问题，请通过文末联系方式咨询蓝培医疗专业顾问。
</div>

<h2><i class="fas fa-globe mr-2 text-orange-500"></i>四、全球同步意义：海外原研药\"中国同步上市\"窗口全面打开</h2>

<p>本次获批事件中，有三个数字值得特别关注：<strong>礼来的择叙、6月22日单日5款、6月当月13款</strong>。这三个数字共同指向一个趋势——<strong>海外原研药\"中国同步上市\"的窗口正在系统性打开</strong>。</p>

<p>过去跨国药企（MNC）在中国上市新药普遍比欧美晚3-5年，导致大量患者被迫\"代购、海外就医、跨境医疗旅游\"，蓝培医疗此类\"全球医疗资源咨询\"业务的核心需求即源于此。而本次礼来口服SERD\"择叙\"的获批——这是礼来乳腺癌重磅产品在全球加速落地中国的一个缩影——叠加国产创新药\"反向出海\"84亿美元交易纪录，<strong>标志着全球创新药格局正在从\"中国跟跑\"转向\"双向同步\"</strong>。</p>

<p>但客观来看，<strong>这种\"同步\"仍有结构性短板</strong>：</p>
<ul>
<li><strong>已获批但未进医保</strong>：当前5款新药均未纳入医保目录，自费价格对普通家庭仍是门槛；</li>
<li><strong>已获批但未进医院</strong>：DRG/DIP控费下，医院使用高价创新药的积极性受抑，需要\"双目录\"和\"三除外\"政策逐步落地；</li>
<li><strong>全球首创国产药的\"反向壁垒\"</strong>：海外患者要获取舒瑞基奥仑赛、伦康依隆妥单抗等国产新药，仍需通过东南亚/老挝/印度等地区合规渠道（老挝桃子互联网医院是经老挝卫生部授权的合规渠道之一）；</li>
<li><strong>罕见病、儿童药\"特殊窗口\"</strong>：双目录对高价罕见病药、儿童药的支持力度尚需观察。</li>
</ul>

<h2><i class="fas fa-handshake mr-2 text-orange-500"></i>五、蓝培视角：政策+产业双拐点下，跨境医疗资源咨询的三个新机会</h2>

<p>从蓝培医疗<strong>\"全球优质医疗资源咨询平台\"</strong>的定位出发，本次\"五箭齐发\"事件+政策红利集中落地，带来三个值得关注的新机会：</p>

<p><strong>第一，\"国产全球首创药\"反向出境咨询需求将快速放量。</strong>全球首款实体瘤CAR-T（科济药业恺力美）、全球首个双抗ADC（百利天恒宜泽康）等国产新药，未来3-5年将面临大量海外患者（尤其东南亚、中东、俄罗斯等）通过跨境医疗路径寻求合规获取的需求。<strong>老挝桃子互联网医院作为老挝卫生部授权的首家互联网医院，可成为这些\"国产全球首创药\"合规出境的核心通道</strong>。蓝培医疗可协助国内创新药企对接海外患者资源，反向赋能国产创新药的全球化进程。</p>

<p><strong>第二，\"MNC原研药中国同步上市\"加速，让蓝培的海外医疗咨询更聚焦\"难治、罕见、未在国内上市\"领域。</strong>随着越来越多MNC新药在中国同步获批，蓝培的全球医疗资源咨询业务将更聚焦于：①<strong>国内尚未获批的全球新药</strong>（如部分ADC、双抗、基因治疗药物的早期全球试验数据）；②<strong>已获批但未进医保/未进医院的高价创新药</strong>的全球可及性路径；③<strong>罕见病、孤儿药的全球医生与药企对接</strong>。这与公司\"帮助患者获取全球优质医疗资源\"的核心定位高度契合。</p>

<p><strong>第三，\"双目录+预申报+价格保护\"组合拳下，跨境医疗咨询的专业门槛进一步提升。</strong>未来患者对\"全球新药格局同步解读、医保与商保政策精准匹配、跨境合规获取路径设计\"等综合咨询需求将快速增长。<strong>蓝培医疗可结合老挝桃子互联网医院的合规渠道、覆盖6国语言的咨询能力、与多家全球新药研发机构的对接经验，为患者提供\"政策解读+海外资源对接+合规路径设计\"的一站式服务</strong>。</p>

<p>如您或家人遇到晚期实体瘤（含胃癌、食管癌、肝癌、肺癌等）、鼻咽癌、乳腺癌、狂犬病暴露、难治性感染等场景，需要了解<strong>全球抗癌药/ADC/CAR-T/双抗方案</strong>，或希望对接<strong>跨境医疗资源、获取第二诊疗意见、了解全球新药同步信息</strong>，欢迎随时联系蓝培医疗。我们的全球医疗资源顾问团队将根据您的具体病情、所在地区、预算范围，提供<strong>合规、可执行的方案建议</strong>。</p>"""

CTA = """<div class="cta-box">
    <p id="cta-title" class="text-lg mb-3" data-i18n="cta_title">需要了解全球抗癌药/ADC/CAR-T/双抗方案或跨境医疗合规路径？</p>
    <p class="mb-2"><i class="fas fa-phone-alt mr-2"></i><span data-i18n="phone_label">电话咨询</span>：<a href="tel:17844531559">17844531559</a></p>
    <p class="mb-2"><i class="fab fa-whatsapp mr-2"></i><span data-i18n="whatsapp_label">WhatsApp</span>：<a href="https://wa.me/639685838435">+63-968-583-8435</a></p>
    <p><i class="fab fa-weixin mr-2"></i><span data-i18n="wechat_label">微信咨询</span>：17844531559</p>
</div>

<p class="text-center text-gray-600 mt-4">网站：<a href="https://lanpeimed.com">lanpeimed.com</a> · 蓝培医疗 · 全球优质医疗资源咨询平台</p>

<div class="warning-box">
    <p><strong id="disclaimer-title" data-i18n="disclaimer_title"><i class="fas fa-exclamation-triangle mr-1"></i>重要提示：</strong><span id="disclaimer-text" data-i18n="disclaimer_text">本文章仅供信息参考，不构成医疗建议。报道中提到的所有创新药为处方药，具体疾病治疗和用药方案请务必咨询专业医生。蓝培医疗为您提供全球优质医疗资源咨询服务，帮助患者了解合规的国内外专家会诊渠道、跨境医疗路径与全球新药同步信息。</span></p>
</div>"""

# 7 语言翻译
TRANSLATIONS = {
    "zh": {
        "site_name": "蓝培医疗",
        "back_home": "首页",
        "news": "新闻资讯",
        "tab_industry": "行业资讯",
        "cta_title": "需要了解全球抗癌药/ADC/CAR-T/双抗方案或跨境医疗合规路径？",
        "phone_label": "电话咨询",
        "whatsapp_label": "WhatsApp",
        "wechat_label": "微信咨询",
        "disclaimer_title": "重要提示",
        "disclaimer_text": "本文章仅供信息参考，不构成医疗建议。报道中提到的所有创新药为处方药，具体疾病治疗和用药方案请务必咨询专业医生。蓝培医疗为您提供全球优质医疗资源咨询服务，帮助患者了解合规的国内外专家会诊渠道、跨境医疗路径与全球新药同步信息。",
        "footer_platform": "全球优质医疗资源咨询平台",
        "footer_disclaimer": "免责声明：本网站展示的医药信息仅供参考，具体疾病治疗和用药细节请务必咨询医生和药师，蓝培不承担任何责任",
        "footer_copyright": "© 2026 蓝培医疗 lanpeimed.com",
        "chat_title": "蓝培医疗在线咨询",
        "phone_consult": "电话咨询",
        "wechat_scan": "微信扫一扫添加咨询",
        "wechat_copy": "加微信",
        "wechat_copied": "已复制!",
        "phone_placeholder": "请输入手机号码",
        "callback_btn": "给您回电",
        "chat_footer": "蓝培医疗 · 全球优质医疗资源咨询",
        "bottom_cta_title": "蓝培医疗 · 专业全球医疗资源咨询",
        "policy_summary": "要点速览",
        "service_guide": "蓝培视角"
    },
    "en": {
        "site_name": "Lanpei Medical",
        "back_home": "Home",
        "news": "News",
        "tab_industry": "Industry News",
        "cta_title": "Need to understand global anti-cancer drugs / ADC / CAR-T / bispecific antibody solutions or cross-border medical compliance paths?",
        "phone_label": "Phone",
        "whatsapp_label": "WhatsApp",
        "wechat_label": "WeChat",
        "disclaimer_title": "Important Notice",
        "disclaimer_text": "This article is for reference only and does not constitute medical advice. All innovative drugs mentioned are prescription drugs. Please consult professional doctors for specific treatment plans. Lanpei Medical provides global medical resource consulting services, helping patients understand compliance channels for domestic and international expert consultations, cross-border medical paths, and global new drug information.",
        "footer_platform": "Global Quality Medical Resources Platform",
        "footer_disclaimer": "Disclaimer: The medical information displayed on this website is for reference only. Please consult doctors and pharmacists for specific disease treatment and medication details. Lanpei assumes no responsibility.",
        "footer_copyright": "© 2026 Lanpei Medical lanpeimed.com",
        "chat_title": "Lanpei Medical Online Consultation",
        "phone_consult": "Phone Consultation",
        "wechat_scan": "Scan QR code to add WeChat",
        "wechat_copy": "Add WeChat",
        "wechat_copied": "Copied!",
        "phone_placeholder": "Enter phone number",
        "callback_btn": "Callback Request",
        "chat_footer": "Lanpei Medical · Global Medical Resources",
        "bottom_cta_title": "Lanpei Medical · Professional Global Medical Consulting",
        "policy_summary": "Key Highlights",
        "service_guide": "Lanpei Perspective"
    },
    "ru": {
        "site_name": "蓝培医疗",
        "back_home": "На главную",
        "news": "Новости",
        "tab_industry": "Новости отрасли",
        "cta_title": "Хотите узнать о глобальных противоопухолевых препаратах / ADC / CAR-T / биспецифических антителах или трансграничных медицинских путях?",
        "phone_label": "Телефон",
        "whatsapp_label": "WhatsApp",
        "wechat_label": "WeChat",
        "disclaimer_title": "Важное уведомление",
        "disclaimer_text": "Эта статья только для справки. Все упомянутые инновационные препараты являются рецептурными. Пожалуйста, консультируйтесь с врачом. Lanpei Medical предоставляет консультации по глобальным медицинским ресурсам.",
        "footer_platform": "Платформа глобальных медицинских ресурсов",
        "footer_disclaimer": "Отказ от ответственности: информация только для справки.",
        "footer_copyright": "© 2026 Lanpei Medical lanpeimed.com",
        "chat_title": "Онлайн консультация Lanpei",
        "phone_consult": "Телефонная консультация",
        "wechat_scan": "Сканируйте QR для добавления WeChat",
        "wechat_copy": "Добавить WeChat",
        "wechat_copied": "Скопировано!",
        "phone_placeholder": "Введите номер телефона",
        "callback_btn": "Обратный звонок",
        "chat_footer": "Lanpei Medical · Глобальные медицинские ресурсы",
        "bottom_cta_title": "Lanpei Medical · Профессиональные глобальные консультации",
        "policy_summary": "Ключевые моменты",
        "service_guide": "Перспектива Lanpei"
    },
    "vi": {
        "site_name": "Lanpei Medical",
        "back_home": "Về trang chủ",
        "news": "Tin tức",
        "tab_industry": "Tin ngành",
        "cta_title": "Cần tìm hiểu về thuốc chống ung thư toàn cầu / ADC / CAR-T / kháng thể đặc hiệu kép hoặc các đường dẫn y tế xuyên biên giới?",
        "phone_label": "Điện thoại",
        "whatsapp_label": "WhatsApp",
        "wechat_label": "WeChat",
        "disclaimer_title": "Thông báo quan trọng",
        "disclaimer_text": "Bài viết này chỉ để tham khảo. Tất cả các loại thuốc sáng tạo được đề cập là thuốc kê đơn. Vui lòng tham khảo ý kiến bác sĩ. Lanpei Medical cung cấp tư vấn nguồn y tế toàn cầu.",
        "footer_platform": "Nền tảng tài nguyên y tế toàn cầu",
        "footer_disclaimer": "Tuyên bố miễn trừ: Thông tin chỉ để tham khảo.",
        "footer_copyright": "© 2026 Lanpei Medical lanpeimed.com",
        "chat_title": "Tư vấn trực tuyến Lanpei",
        "phone_consult": "Tư vấn điện thoại",
        "wechat_scan": "Quét QR để thêm WeChat",
        "wechat_copy": "Thêm WeChat",
        "wechat_copied": "Đã sao chép!",
        "phone_placeholder": "Nhập số điện thoại",
        "callback_btn": "Yêu cầu gọi lại",
        "chat_footer": "Lanpei Medical · Tài nguyên y tế toàn cầu",
        "bottom_cta_title": "Lanpei Medical · Tư vấn y tế toàn cầu chuyên nghiệp",
        "policy_summary": "Điểm chính",
        "service_guide": "Quan điểm Lanpei"
    },
    "id": {
        "site_name": "Lanpei Medical",
        "back_home": "Beranda",
        "news": "Berita",
        "tab_industry": "Berita Industri",
        "cta_title": "Perlu memahami obat anti-kanker global / ADC / CAR-T / antibodi bispesifik atau jalur medis lintas batas?",
        "phone_label": "Telepon",
        "whatsapp_label": "WhatsApp",
        "wechat_label": "WeChat",
        "disclaimer_title": "Pemberitahuan Penting",
        "disclaimer_text": "Artikel ini hanya untuk referensi. Semua obat inovatif yang disebutkan adalah obat resep. Silakan konsultasikan dengan dokter profesional. Lanpei Medical menyediakan layanan konsultasi sumber daya medis global.",
        "footer_platform": "Platform Sumber Daya Medis Global",
        "footer_disclaimer": "Penafian: Informasi hanya untuk referensi.",
        "footer_copyright": "© 2026 Lanpei Medical lanpeimed.com",
        "chat_title": "Konsultasi Online Lanpei",
        "phone_consult": "Konsultasi Telepon",
        "wechat_scan": "Pindai QR untuk menambah WeChat",
        "wechat_copy": "Tambah WeChat",
        "wechat_copied": "Disalin!",
        "phone_placeholder": "Masukkan nomor telepon",
        "callback_btn": "Permintaan Panggilan Balik",
        "chat_footer": "Lanpei Medical · Sumber Daya Medis Global",
        "bottom_cta_title": "Lanpei Medical · Konsultasi Medis Global Profesional",
        "policy_summary": "Sorotan Utama",
        "service_guide": "Perspektif Lanpei"
    },
    "my": {
        "site_name": "Lanpei Medical",
        "back_home": "ပင်မစာမျက်နှာ",
        "news": "သတင်းများ",
        "tab_industry": "စက်မှုသတင်း",
        "cta_title": "ကမ္ဘာလုံးဆိုင်ရာ ကင်ဆာဆေးများ / ADC / CAR-T / နှစ်ထပ်ပဋိပစ္စည်း သို့မဟုတ် နယ်စပ်ဖြတ်ကျော် ဆေးဘက်ဆိုင်ရာ လမ်းကြောင်းများ နားလည်ရန် လိုအပ်ပါသလား။",
        "phone_label": "ဖုန်း",
        "whatsapp_label": "WhatsApp",
        "wechat_label": "WeChat",
        "disclaimer_title": "အရေးကြီးသော အသိပေးချက်",
        "disclaimer_text": "ဤဆောင်းပါးသည် ရည်ညွှန်းရန်အတွက်သာ ဖြစ်ပါသည်။ ဖော်ပြထားသော ဆန်းသစ်တီထွင်ဆေးများအားလုံးသည် ဆေးညွှန်းဖြင့်သာ ရရှိနိုင်ပါသည်။ ကျွမ်းကျင်ဆရာဝန်နှင့် တိုင်ပင်ဆွေးနွေးပါ။ Lanpei Medical သည် ကမ္ဘာလုံးဆိုင်ရာ ဆေးဘက်ဆိုင်ရာ အရင်းအမြစ် တိုင်ပင်ဆွေးနွေးမှု ဝန်ဆောင်မှုများကို ပံ့ပိုးပေးပါသည်။",
        "footer_platform": "ကမ္ဘာလုံးဆိုင်ရာ ဆေးဘက်ဆိုင်ရာ အရင်းအမြစ် ပလက်ဖောင်း",
        "footer_disclaimer": "ရှင်းလင်းချက်- အချက်အလက်များသည် ရည်ညွှန်းရန်အတွက်သာ ဖြစ်ပါသည်။",
        "footer_copyright": "© 2026 Lanpei Medical lanpeimed.com",
        "chat_title": "Lanpei အွန်လိုင်း တိုင်ပင်ဆွေးနွေးမှု",
        "phone_consult": "ဖုန်းတိုင်ပင်ဆွေးနွေးမှု",
        "wechat_scan": "WeChat ထည့်ရန် QR ကုဒ်ကို စကင်ဖတ်ပါ",
        "wechat_copy": "WeChat ထည့်ပါ",
        "wechat_copied": "ကူးယူပြီး!",
        "phone_placeholder": "ဖုန်းနံပါတ် ထည့်ပါ",
        "callback_btn": "ပြန်လည်ခေါ်ဆိုမှု",
        "chat_footer": "Lanpei Medical · ကမ္ဘာလုံးဆိုင်ရာ ဆေးဘက်ဆိုင်ရာ အရင်းအမြစ်များ",
        "bottom_cta_title": "Lanpei Medical · ကျွမ်းကျင် ကမ္ဘာလုံးဆိုင်ရာ ဆေးဘက်ဆိုင်ရာ တိုင်ပင်ဆွေးနွေးမှု",
        "policy_summary": "အဓိက အချက်အလက်များ",
        "service_guide": "Lanpei ရှုထောင့်"
    },
    "bd": {
        "site_name": "Lanpei Medical",
        "back_home": "হোম",
        "news": "সংবাদ",
        "tab_industry": "শিল্প সংবাদ",
        "cta_title": "বিশ্বব্যাপী ক্যান্সার বিরোধী ওষুধ / ADC / CAR-T / দ্বি-নির্দিষ্ট অ্যান্টিবডি বা সীমান্ত-অতিক্রমকারী চিকিৎসা পথ বুঝতে চান?",
        "phone_label": "ফোন",
        "whatsapp_label": "WhatsApp",
        "wechat_label": "WeChat",
        "disclaimer_title": "গুরুত্বপূর্ণ বিজ্ঞপ্তি",
        "disclaimer_text": "এই নিবন্ধটি শুধুমাত্র রেফারেন্সের জন্য। উল্লিখিত সমস্ত উদ্ভাবনী ওষুধ প্রেসক্রিপশন ওষুধ। পেশাদার ডাক্তারদের সাথে পরামর্শ করুন। Lanpei Medical বিশ্বব্যাপী চিকিৎসা সম্পদ পরামর্শ প্রদান করে।",
        "footer_platform": "বিশ্বব্যাপী মানসম্মত চিকিৎসা সম্পদ প্ল্যাটফর্ম",
        "footer_disclaimer": "দাবিত্যাগ: তথ্য শুধুমাত্র রেফারেন্সের জন্য।",
        "footer_copyright": "© 2026 Lanpei Medical lanpeimed.com",
        "chat_title": "Lanpei অনলাইন পরামর্শ",
        "phone_consult": "ফোন পরামর্শ",
        "wechat_scan": "WeChat যোগ করতে QR স্ক্যান করুন",
        "wechat_copy": "WeChat যোগ করুন",
        "wechat_copied": "কপি হয়েছে!",
        "phone_placeholder": "ফোন নম্বর লিখুন",
        "callback_btn": "কলব্যাক অনুরোধ",
        "chat_footer": "Lanpei Medical · বিশ্বব্যাপী চিকিৎসা সম্পদ",
        "bottom_cta_title": "Lanpei Medical · পেশাদার বিশ্বব্যাপী চিকিৎসা পরামর্শ",
        "policy_summary": "মূল হাইলাইটস",
        "service_guide": "Lanpei দৃষ্টিভঙ্গি"
    }
}

# 生成翻译对象字符串
import json
trans_json = json.dumps(TRANSLATIONS, ensure_ascii=False, indent=8)

HTML = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITLE} - 蓝培医疗行业资讯</title>
    <meta name="description" content="{DESC}">
    <meta name="keywords" content="{KEYWORDS}">
    <script>
var _hmt = _hmt || []; (function() {{ var hm = document.createElement("script"); hm.src = "https://hm.baidu.com/hm.js?59ed620a6512d2be372b2677fa87e40e"; var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(hm, s); }});
    </script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {{ --primary: #1e3a5f; --accent: #f97316; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #333; line-height: 1.8; }}
        .gradient-bg {{ background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); }}
        a {{ color: #1e3a5f; text-decoration: none; }}
        a:hover {{ color: #f97316; }}
        .info-box {{ background: #f0f7ff; border-left: 4px solid #1e3a5f; padding: 16px 20px; border-radius: 0 8px 8px 0; margin: 16px 0; }}
        .data-card {{ background: white; border-radius: 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); text-align: center; }}
        .data-card .number {{ font-size: 32px; font-weight: bold; color: #1e3a5f; }}
        .data-card .label {{ font-size: 14px; color: #6b7280; margin-top: 4px; }}
        .highlight-box {{ background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border-radius: 12px; padding: 20px; margin: 20px 0; border-left: 4px solid #f97316; }}
        .cta-box {{ background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); color: white; padding: 24px; border-radius: 12px; text-align: center; margin: 30px 0; }}
        .cta-box a {{ color: #fb923c; font-weight: bold; font-size: 18px; }}
        .warning-box {{ background: #fff7ed; border-left: 4px solid #f97316; padding: 16px 20px; border-radius: 0 8px 8px 0; margin: 16px 0; }}
        .breadcrumb {{ font-size: 14px; color: #6b7280; margin-bottom: 20px; }}
        .breadcrumb a {{ color: #6b7280; }}
        .breadcrumb a:hover {{ color: #f97316; }}
        h2 {{ color: #1e3a5f; border-bottom: 2px solid #f0f7ff; padding-bottom: 8px; margin-top: 30px; }}
        h3 {{ color: #2d5a87; margin-top: 20px; }}
        .lang-btn.active {{ background: #f97316; color: white; }}
        .article-content p {{ margin-bottom: 16px; }}
        .article-content ul {{ margin: 16px 0; padding-left: 24px; }}
        .article-content li {{ margin-bottom: 8px; }}
    </style>

    <script>
    // ===================== 多语言支持 =====================
    const translations = {trans_json};

    let currentLang = 'zh';

    function changeLanguage(lang) {{
        currentLang = lang;
        document.querySelectorAll('.lang-btn').forEach(btn => {{
            btn.classList.remove('bg-[#f97316]', 'text-white');
            if (btn.dataset.lang === lang) {{
                btn.classList.add('bg-[#f97316]', 'text-white');
            }}
        }});
        updateTranslations();
    }}

    function updateTranslations() {{
        const t = translations[currentLang];
        document.querySelectorAll('[data-i18n]').forEach(el => {{
            const key = el.getAttribute('data-i18n');
            if (t[key]) {{
                el.textContent = t[key];
            }}
        }});
        const footerPlatform = document.getElementById('footer-platform');
        if (footerPlatform) footerPlatform.textContent = t.footer_platform;
        const footerDisclaimer = document.getElementById('footer-disclaimer');
        if (footerDisclaimer) footerDisclaimer.textContent = t.footer_disclaimer;
        const ctaTitle = document.getElementById('cta-title');
        if (ctaTitle) ctaTitle.textContent = t.cta_title;
        const disclaimerTitle = document.getElementById('disclaimer-title');
        if (disclaimerTitle) disclaimerTitle.textContent = t.disclaimer_title;
        const disclaimerText = document.getElementById('disclaimer-text');
        if (disclaimerText) disclaimerText.textContent = t.disclaimer_text;
        const bottomCta = document.getElementById('bottom-cta');
        if (bottomCta) bottomCta.innerHTML = '<p class="font-bold">' + t.bottom_cta_title + '</p><p class="text-sm mt-1">' + t.phone_label + ' 17844531559 | ' + t.whatsapp_label + ' +639685838435 | ' + t.wechat_label + ' 17844531559</p>';
        const chatTitle = document.querySelector('.chat-header-left span');
        if (chatTitle) chatTitle.textContent = t.chat_title;
        const wechatScanText = document.querySelector('.chat-body > div:nth-child(2) p');
        if (wechatScanText) wechatScanText.textContent = t.wechat_scan;
        const phoneConsultLabel = document.querySelector('.chat-contact-item:nth-child(1) .label');
        if (phoneConsultLabel) phoneConsultLabel.textContent = t.phone_consult;
        const whatsappLabel = document.querySelector('.chat-contact-item:nth-child(2) .label');
        if (whatsappLabel) whatsappLabel.textContent = t.whatsapp_label;
        const wechatCopyLabel = document.getElementById('wechatLabel');
        if (wechatCopyLabel) wechatCopyLabel.textContent = t.wechat_copy;
        const phoneInput = document.getElementById('chatPhone');
        if (phoneInput) phoneInput.placeholder = t.phone_placeholder;
        const callbackBtn = document.querySelector('.chat-input-area button');
        if (callbackBtn) callbackBtn.textContent = t.callback_btn;
        const chatFooter = document.querySelector('.chat-footer');
        if (chatFooter) chatFooter.textContent = t.chat_footer;
    }}
    </script>
</head>
<body class="bg-gray-50">
    <!-- Top Bar with Language Switcher -->
    <div class="bg-gray-900 text-white py-2 text-sm">
        <div class="max-w-7xl mx-auto px-4 flex justify-between items-center flex-wrap gap-2">
            <div class="flex items-center gap-4 flex-wrap">
                <span class="flex items-center gap-1"><i class="fas fa-phone"></i> +86-17844531559</span>
                <span class="flex items-center gap-1"><i class="fas fa-envelope"></i> 173166453@qq.com</span>
            </div>
            <div class="flex items-center gap-3">
                <div class="flex gap-2">
                    <button onclick="changeLanguage('zh')" class="px-2 py-0.5 rounded text-xs hover:bg-gray-700 lang-btn active" data-lang="zh">中文</button>
                    <button onclick="changeLanguage('en')" class="px-2 py-0.5 rounded text-xs hover:bg-gray-700 lang-btn" data-lang="en">English</button>
                    <button onclick="changeLanguage('ru')" class="px-2 py-0.5 rounded text-xs hover:bg-gray-700 lang-btn" data-lang="ru">Русский</button>
                    <button onclick="changeLanguage('vi')" class="px-2 py-0.5 rounded text-xs hover:bg-gray-700 lang-btn" data-lang="vi">Tiếng Việt</button>
                    <button onclick="changeLanguage('id')" class="px-2 py-0.5 rounded text-xs hover:bg-gray-700 lang-btn" data-lang="id">Indonesia</button>
                    <button onclick="changeLanguage('my')" class="px-2 py-0.5 rounded text-xs hover:bg-gray-700 lang-btn" data-lang="my">Myanmar</button>
                    <button onclick="changeLanguage('bd')" class="px-2 py-0.5 rounded text-xs hover:bg-gray-700 lang-btn" data-lang="bd">বাংলা</button>
                </div>
                <div class="flex gap-2 ml-4">
                    <a href="https://wa.me/639685838435" target="_blank" class="hover:text-green-400"><i class="fab fa-whatsapp"></i></a>
                    <a href="javascript:void(0)" onclick="showWechat()" class="hover:text-green-400"><i class="fab fa-weixin"></i></a>
                </div>
            </div>
        </div>
    </div>

    <!-- Header -->
    <header class="gradient-bg text-white py-4">
        <div class="max-w-4xl mx-auto px-4">
            <div class="flex items-center justify-between">
                <h1 class="text-xl font-bold"><a href="https://lanpeimed.com" class="text-white" data-i18n="site_name">蓝培医疗</a></h1>
                <div class="flex gap-3 text-sm">
                    <a href="https://lanpeimed.com" class="text-blue-200 hover:text-white"><i class="fas fa-home mr-1"></i><span data-i18n="back_home">首页</span></a>
                    <a href="https://lanpeimed.com/news.html" class="text-blue-200 hover:text-white"><i class="fas fa-newspaper mr-1"></i><span data-i18n="news">新闻资讯</span></a>
                </div>
            </div>
        </div>
    </header>

    <main class="max-w-4xl mx-auto px-4 py-6">
        <div class="breadcrumb">
            <a href="https://lanpeimed.com" data-i18n="back_home">首页</a> &gt; <a href="https://lanpeimed.com/news.html" data-i18n="news">新闻资讯</a> &gt; <span class="inline-block bg-orange-100 text-orange-700 px-2 py-0.5 rounded text-xs font-medium" data-i18n="tab_industry">行业资讯</span> &gt; 6月22日5款创新药同日获批
        </div>

        <article class="bg-white rounded-xl shadow-sm p-6 md:p-8">
            <h1 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">{TITLE}</h1>
            <p class="text-gray-500 mb-6">发布时间：2026年6月23日 | 来源：国家药品监督管理局官网、财联社、新京报、长城国瑞证券、医药魔方、网易新闻 | 分类：<span data-i18n="tab_industry">行业资讯</span></p>

            <div class="article-content">
                {CONTENT}

                <!-- CTA -->
                {CTA}
            </div>
        </article>

        <!-- Bottom CTA -->
        <div id="bottom-cta" class="bg-orange-500 text-white p-4 rounded-xl text-center mt-6">
            <p class="font-bold" data-i18n="bottom_cta_title">蓝培医疗 · 专业全球医疗资源咨询</p>
            <p class="text-sm mt-1">电话 17844531559 | WhatsApp +639685838435 | 微信 17844531559</p>
        </div>
    </main>

    <footer class="gradient-bg text-white py-6 mt-8">
        <div class="max-w-4xl mx-auto px-4 text-center text-sm text-blue-200">
            <p id="footer-platform" data-i18n="footer_platform">全球优质医疗资源咨询平台</p>
            <p id="footer-disclaimer" class="mt-2" data-i18n="footer_disclaimer">免责声明：本网站展示的医药信息仅供参考，具体疾病治疗和用药细节请务必咨询医生和药师，蓝培不承担任何责任</p>
            <p id="footer-copyright" class="mt-1" data-i18n="footer_copyright">© 2026 蓝培医疗 lanpeimed.com</p>
        </div>
    </footer>

<!-- 在线咨询浮窗 -->
<style>
.chat-widget-btn{{position:fixed;bottom:30px;right:30px;width:60px;height:60px;background:linear-gradient(135deg,#1e3a5f,#2d5a87);border-radius:50%;cursor:pointer;box-shadow:0 4px 20px rgba(30,58,95,0.4);z-index:9999;display:flex;align-items:center;justify-content:center;transition:all .3s}}
.chat-widget-btn:hover{{transform:scale(1.1);box-shadow:0 6px 25px rgba(30,58,95,0.5)}}
.chat-widget-btn i{{color:#fff;font-size:24px}}
.chat-widget-btn .pulse-ring{{position:absolute;width:100%;height:100%;border-radius:50%;background:rgba(249,115,22,0.3);animation:chatPulse 2s infinite}}
@keyframes chatPulse{{0%,100%{{transform:scale(1);opacity:1}}50%{{transform:scale(1.4);opacity:0}}}}
.chat-box{{position:fixed;bottom:100px;right:30px;width:340px;background:#fff;border-radius:16px;box-shadow:0 8px 40px rgba(0,0,0,0.2);z-index:9998;display:none;flex-direction:column;overflow:hidden;animation:chatSlideUp .3s ease}}
@keyframes chatSlideUp{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:translateY(0)}}}}
.chat-box.active{{display:flex}}
.chat-header{{background:linear-gradient(135deg,#1e3a5f,#2d5a87);color:#fff;padding:14px 16px;display:flex;align-items:center;justify-content:space-between}}
.chat-header-left{{display:flex;align-items:center;gap:10px}}
.chat-header-left .logo{{width:32px;height:32px;background:#f97316;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:bold}}
.chat-header-left span{{font-size:15px;font-weight:600}}
.chat-header .close-btn{{background:none;border:none;color:#fff;font-size:18px;cursor:pointer;padding:4px}}
.chat-body{{padding:16px;flex:1}}
.chat-notice{{background:#fff7ed;border:1px solid #fed7aa;border-radius:8px;padding:12px;margin-bottom:14px;font-size:13px;line-height:1.7;color:#333}}
.chat-notice .phone-red{{color:#dc2626;font-weight:bold;font-size:16px}}
.chat-contact-row{{display:flex;gap:10px;margin-bottom:14px}}
.chat-contact-item{{flex:1;background:#f0f7ff;border-radius:8px;padding:10px;text-align:center;font-size:12px;color:#1e3a5f;cursor:pointer;transition:all .2s}}
.chat-contact-item:hover{{background:#e0efff;transform:translateY(-2px)}}
.chat-contact-item i{{font-size:20px;margin-bottom:4px;display:block}}
.chat-contact-item .label{{font-weight:600;margin-top:4px}}
.chat-input-area{{display:flex;gap:8px;margin-top:10px}}
.chat-input-area input{{flex:1;border:1px solid #d1d5db;border-radius:8px;padding:10px 12px;font-size:13px;outline:none}}
.chat-input-area input:focus{{border-color:#1e3a5f}}
.chat-input-area button{{background:linear-gradient(135deg,#1e3a5f,#2d5a87);color:#fff;border:none;border-radius:8px;padding:10px 16px;font-size:13px;cursor:pointer;white-space:nowrap;font-weight:600}}
.chat-input-area button:hover{{background:linear-gradient(135deg,#2d5a87,#3a6d9e)}}
.chat-footer{{text-align:center;padding:8px;font-size:11px;color:#9ca3af;border-top:1px solid #f3f4f6}}
</style>
<div class="chat-widget-btn" onclick="toggleChat()">
    <div class="pulse-ring"></div>
    <i class="fas fa-headset"></i>
</div>
<div class="chat-box" id="chatBox">
    <div class="chat-header">
        <div class="chat-header-left">
            <div class="logo">蓝培</div>
            <span data-i18n="chat_title">蓝培医疗在线咨询</span>
        </div>
        <button class="close-btn" onclick="toggleChat()"><i class="fas fa-times"></i></button>
    </div>
    <div class="chat-body">
        <div class="chat-notice">
            因咨询人数多，如未及时回复，请致电：<span class="phone-red">17844531559</span>，或扫码加微信沟通：
        </div>
        <div style="text-align:center;margin-bottom:14px">
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=WeChat%3A17844531559" alt="微信二维码" style="width:120px;height:120px;border:2px solid #e5e7eb;border-radius:8px">
            <p style="font-size:12px;color:#6b7280;margin-top:6px" data-i18n="wechat_scan">微信扫一扫添加咨询</p>
        </div>
        <div class="chat-contact-row">
            <a href="tel:17844531559" class="chat-contact-item" style="text-decoration:none">
                <i class="fas fa-phone-alt" style="color:#1e3a5f"></i>
                <div class="label" data-i18n="phone_consult">电话咨询</div>
            </a>
            <a href="https://wa.me/639685838435" target="_blank" class="chat-contact-item" style="text-decoration:none">
                <i class="fab fa-whatsapp" style="color:#25d366"></i>
                <div class="label" data-i18n="whatsapp_label">WhatsApp</div>
            </a>
            <a href="javascript:void(0)" onclick="copyWechat()" class="chat-contact-item" style="text-decoration:none">
                <i class="fab fa-weixin" style="color:#07c160"></i>
                <div class="label" id="wechatLabel" data-i18n="wechat_copy">加微信</div>
            </a>
        </div>
        <div class="chat-input-area">
            <input type="tel" id="chatPhone" placeholder="请输入手机号码" data-i18n-placeholder="phone_placeholder">
            <button onclick="requestCallback()" data-i18n="callback_btn">给您回电</button>
        </div>
    </div>
    <div class="chat-footer" data-i18n="chat_footer">蓝培医疗 · 全球优质医疗资源咨询</div>
</div>
<script>
function toggleChat(){{var b=document.getElementById('chatBox');b.classList.toggle('active')}}
function copyWechat(){{navigator.clipboard.writeText('17844531559');var l=document.getElementById('wechatLabel');l.textContent=translations[currentLang].wechat_copied;setTimeout(function(){{l.textContent=translations[currentLang].wechat_copy}},2000)}}
function requestCallback(){{var p=document.getElementById('chatPhone').value;if(!p||p.length<8){{alert('请输入正确的手机号码');return}}var msg='咨询回电请求：'+p+'，请蓝培医疗客服尽快联系我。';var waUrl='https://wa.me/639685838435?text='+encodeURIComponent(msg);window.open(waUrl,'_blank')}}
function showWechat(){{document.getElementById('chatBox').classList.add('active')}}
document.addEventListener('DOMContentLoaded', function() {{ updateTranslations(); }});
</script>

</body>
</html>
"""

# 写入文件
out_path = "/app/data/所有对话/主对话/蓝培医疗文章/news-industry-0623-5yao-rizhan.html"
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f"✓ 已生成行业资讯文章：{out_path}")
print(f"✓ 文件大小：{os.path.getsize(out_path) / 1024:.1f} KB")
# 字数估算（中文字符数）
import re
text_only = re.sub(r'<[^>]+>', '', CONTENT)
chinese_chars = re.findall(r'[\u4e00-\u9fff]', text_only)
print(f"✓ 中文字符数：{len(chinese_chars)}（目标 800-1200）")
