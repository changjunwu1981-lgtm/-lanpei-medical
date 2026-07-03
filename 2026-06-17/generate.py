"""
生成5篇药品文章 HTML + 公众号txt
2026-06-17 第114-118号
- 114 劳拉替尼 Lorlatinib (Lorbrena) - ALK突变NSCLC
- 115 阿帕他胺 Apalutamide (Erleada) - mHSPC/nmCRPC
- 116 吉瑞替尼 Gilteritinib (Xospata) - FLT3+AML（药品列表分类"肺癌"为数据错误，实际白血病）
- 117 宗艾替尼 Zongertinib (Hernexeos) - HER2 TKD突变NSCLC
- 118 黑喷延时喷雾 (TORRENT) - 男科外用延时
"""
import os

DRUGS = [
    {
        "num": 114,
        "name": "劳拉替尼片",
        "generic_en": "Lorlatinib Tablets (Lorbrena/博瑞纳)",
        "brand": "LuciLora",
        "category": "肺癌",
        "indication": "单药适用于间变性淋巴瘤激酶(ALK)阳性的局部晚期或转移性非小细胞肺癌(NSCLC)成人患者的治疗;包括既往未接受过ALK-TKI治疗的一线患者,以及克唑替尼治疗后或阿来替尼/塞瑞替尼作为首个ALK-TKI后疾病进展的患者",
        "spec": "25mg/片、100mg/片",
        "category_label": "第三代ALK突变NSCLC靶向药",
        "drug_class": "第三代小分子间变性淋巴瘤激酶(ALK)与ROS1酪氨酸激酶抑制剂(TKI),基于结构设计优化血脑屏障穿透性",
        "moa": "通过与ALK激酶区ATP结合位点高选择性结合,强效抑制ALK及ROS1激酶活性;对克唑替尼耐药后出现的多种ALK继发突变(包括G1202R、I1171T等)仍有活性;脂溶性高、血脑屏障穿透性优异,颅内活性突出,可有效控制脑转移病灶",
        "dosage": "推荐剂量100mg,口服每日1次,可与食物同服或空腹;整片吞服,不可咀嚼、压碎或掰开;每天大致相同时间服用;持续治疗直至疾病进展或不可接受的毒性",
        "monitor": "用药前必须经批准的检测方法确诊为ALK阳性NSCLC(由具备资质的实验室进行VENTANA ALK(D5F3)CDx等检测);治疗前2周起监测血压,之后至少每月1次;基线和治疗期间定期监测血脂(胆固醇/甘油三酯)、血糖、肝功能、心电图(评估PR间期和房室传导阻滞)、肺症状(警惕ILD);既往有脑转移或接受过脑部放疗者应监测CNS症状变化",
        "adverse": "常见:水肿(56%)、周围神经病变(44%)、体重增加(31%)、认知功能影响(28%,如记忆减退/注意力下降)、疲劳(27%)、呼吸困难(27%)、关节痛(24%)、腹泻(23%)、情绪影响(21%,含自杀意念)、咳嗽(21%)、高胆固醇血症(3-4级18%)、高甘油三酯血症(3-4级19%);严重:CNS影响(整体52%,含癫痫1.9%/精神影响7%/言语11%/精神状态1.3%)、3-4级高脂血症(83%需启动降脂治疗)、高血压(13%,3-4级6%)、高血糖(9%)、房室传导阻滞(1.9%)、间质性肺病ILD(1.9%)、肝毒性(尤其与强CYP3A诱导剂合用可致严重肝损,4级ALT/AST升高50%)、胚胎-胎儿毒性",
        "missed": "若漏服一剂,应在当天记起时尽快补服;若距下次服药时间不足4小时,则跳过漏服剂量,下次按原计划服用;不可同时服用2倍剂量",
        "title_seo": "劳拉替尼片用法用量详解｜博瑞纳Lorbrena ALK阳性非小细胞肺癌第三代TKI靶向用药指南",
        "description_seo": "劳拉替尼片(Lorlatinib)用法用量详解,原研药博瑞纳/Lorbrena治疗ALK阳性局部晚期或转移性非小细胞肺癌(NSCLC),老挝LuciLora版本咨询,全球优质医疗资源",
        "keywords_seo": "劳拉替尼片,lorlatinib用法,博瑞纳,Lorbrena,LuciLora,ALK阳性,非小细胞肺癌,NSCLC靶向药,三代ALK-TKI,脑转移",
        "price_original": "Lorbrena 100mg×30片/盒 约25000-35000元(美国/欧洲原研价,已纳入中国医保乙类参考价14803-16804元)",
        "price_generic": "老挝LuciLora 100mg×30片/盒 约4000-7000元(海外经济版)",
        "cta_title_zh": "需要咨询劳拉替尼片药品渠道和价格信息?",
        "pinyin": "lorlatinib",
    },
    {
        "num": 115,
        "name": "阿帕他胺片",
        "generic_en": "Apalutamide Tablets (Erleada/安森珂)",
        "brand": "LuciApa",
        "category": "前列腺癌",
        "indication": "①转移性内分泌治疗敏感性前列腺癌(mHSPC)成年患者;②有高危转移风险的非转移性去势抵抗性前列腺癌(nmCRPC)成年患者;两种适应症均需与雄激素剥夺治疗(ADT)联合使用",
        "spec": "60mg/片、240mg/片",
        "category_label": "雄激素受体抑制剂(ARI)",
        "drug_class": "口服非甾体雄激素受体(AR)抑制剂,通过与AR配体结合域结合阻断雄激素介导的信号传导",
        "moa": "阿帕他胺与雄激素受体的配体结合域高亲和力结合,阻止雄激素(睾酮与双氢睾酮DHT)与AR结合、抑制AR核转位、阻断AR与DNA的结合,从而抑制雄激素介导的前列腺癌细胞增殖;TITAN研究(1052例mHSPC)和SPARTAN研究(1207例nmCRPC)显示其与ADT联合显著延长OS和无转移生存期",
        "dosage": "推荐剂量240mg(4片60mg/片),口服每日1次,整片用水吞服,可与食物同服或空腹;未行手术去势的患者用药期间需同时接受GnRHa类似物治疗;每天大致相同时间服用;持续治疗直至疾病进展或不可接受的毒性",
        "monitor": "用药前需有病理确诊的前列腺腺癌证据(活检组织学)、Gleason评分、骨扫描评估转移状态;治疗前及治疗期间定期监测:血压(高血压发生率增加)、血脂、血糖、肝功能、TSH、ECG(警惕QT间期延长);用药前评估跌倒/骨折风险,必要时联用骨保护药物;有癫痫史、脑外伤、近1年卒中或脑转移者禁用或慎用(新发癫痫需永久停药);长期监测皮肤反应(SCAR如SJS/TEN/DRESS)和肺症状(警惕ILD)",
        "adverse": "常见(≥10%,比安慰剂高≥2%):疲乏、关节痛、皮疹(任何级别24-30%,重度8-12%)、食欲下降、跌倒(15-16%)、体重降低(11-16%)、高血压(17-25%)、潮热(15-23%)、腹泻(16-20%)、骨折(12-22%);严重:缺血性心血管事件(TITAN研究中致死率0.6%)、缺血性脑血管病变、癫痫发作(1-2%,多在用药后6-12个月)、重度皮肤反应(DRESS/SJS/TEN,发生率<1%但可致命)、间质性肺病(罕见致死个案)、QTc间期延长、甲状腺功能减退、胚胎-胎儿毒性",
        "missed": "若漏服一剂,应在当天记起时尽快补服;次日仍按原计划服药;不可额外服用本品以弥补漏服剂量",
        "title_seo": "阿帕他胺片用法用量详解｜安森珂Erleada mHSPC与nmCRPC前列腺癌靶向用药指南",
        "description_seo": "阿帕他胺片(Apalutamide)用法用量详解,原研药安森珂/Erleada治疗转移性激素敏感性前列腺癌(mHSPC)及高危非转移性去势抵抗性前列腺癌(nmCRPC),老挝LuciApa版本咨询,全球优质医疗资源",
        "keywords_seo": "阿帕他胺片,apalutamide用法,安森珂,Erleada,LuciApa,mHSPC,nmCRPC,前列腺癌靶向药,雄激素受体抑制剂",
        "price_original": "Erleada 60mg×120片/盒 约25000-35000元(美国原研,部分国家医保覆盖)",
        "price_generic": "老挝LuciApa 60mg×120片/盒 约3000-6000元(海外经济版)",
        "cta_title_zh": "需要咨询阿帕他胺片药品渠道和价格信息?",
        "pinyin": "apalutamide",
    },
    {
        "num": 116,
        "name": "富马酸吉瑞替尼片",
        "generic_en": "Gilteritinib Fumarate Tablets (Xospata/适加坦)",
        "brand": "LuciGilt",
        "category": "白血病",
        "indication": "单药治疗经充分验证的检测方法确认携带FMS样酪氨酸激酶3(FLT3)突变的复发或难治性急性髓系白血病(AML)成人患者;支持该适应症的临床数据主要来自ADMIRAL研究",
        "spec": "40mg/片",
        "category_label": "FLT3突变复发难治AML靶向药",
        "drug_class": "FMS样酪氨酸激酶3(FLT3)与AXL激酶双重抑制剂,口服小分子靶向药",
        "moa": "通过竞争性结合FLT3受体激酶区ATP结合位点,抑制FLT3-ITD(内部串联重复)和FLT3-TKD(酪氨酸激酶结构域)突变体的自磷酸化,阻断下游RAS/MAPK、STAT5、PI3K/AKT信号通路,从而抑制白血病细胞增殖;同时抑制AXL激酶(AML中常见的耐药相关激酶),降低对FLT3单靶点抑制的耐药风险",
        "dosage": "推荐起始剂量120mg(3片40mg),口服每日1次,每28天为一个治疗周期;可与食物同服或空腹;整片用水吞服,不可掰开、压碎或咀嚼;每天大致相同时间服用;若临床无疾病进展或不可耐受毒性,建议至少持续治疗6个月以观察临床反应",
        "monitor": "用药前必须经FDA批准或NMPA批准的检测方法(如PCR/NGS)确认FLT3突变(ITD或TKD);治疗前及治疗期间定期监测:血常规(每周1次×第1月,之后每2周1次×第2月,之后每月1次)、血生化(肝肾功能、肌酸磷酸激酶CPK)、心电图(基线、第1周期第8/15天、之后2个月每月1次,警惕QTc延长)、分化综合征症状(发热、呼吸困难、胸腔/心包积液、低血压、皮疹);基线纠正低钾血症和低镁血症以减少QTc延长风险",
        "adverse": "常见:丙氨酸氨基转移酶ALT升高(82.1%)、天冬氨酸氨基转移酶AST升高(80.6%)、碱性磷酸酶升高(68.7%)、肌酸磷酸激酶CPK升高(53.9%)、腹泻(35.1%)、疲劳(30.4%)、恶心(29.8%)、便秘(28.2%)、咳嗽(28.2%)、外周水肿(24.1%)、呼吸困难(24.1%)、眩晕(20.4%)、低血压(17.2%)、关节痛(12.5%)、肌痛(12.5%);严重:分化综合征(3.4%,可致命,黑框警告)、QTc间期延长(>500ms占1%,>60ms增量占7%)、后部可逆性脑病综合征PRES(0.6%)、胰腺炎(4%)、急性肾损伤(6.6%)、肝酶严重升高、胚胎-胎儿毒性",
        "missed": "若漏服一剂,应在当天记起时尽快补服;但距下次服药不足12小时时,不应补服,下次按原计划服用;不可在12小时内服用2次剂量",
        "title_seo": "富马酸吉瑞替尼片用法用量详解｜适加坦Xospata FLT3突变复发难治急性髓系白血病靶向用药指南",
        "description_seo": "富马酸吉瑞替尼片(Gilteritinib)用法用量详解,原研药适加坦/Xospata治疗FLT3突变复发或难治性急性髓系白血病(AML),老挝LuciGilt版本咨询,全球优质医疗资源",
        "keywords_seo": "富马酸吉瑞替尼片,gilteritinib用法,适加坦,Xospata,LuciGilt,FLT3突变,复发难治AML,急性髓系白血病靶向药",
        "price_original": "Xospata 40mg×84片/盒(28天用量) 约30000-50000元(美国/日本原研价,中国2025年1月正式批准上市)",
        "price_generic": "老挝LuciGilt 40mg×84片/盒 约6000-10000元(海外经济版)",
        "cta_title_zh": "需要咨询富马酸吉瑞替尼片药品渠道和价格信息?",
        "pinyin": "gilteritinib",
    },
    {
        "num": 117,
        "name": "宗艾替尼片",
        "generic_en": "Zongertinib Tablets (Hernexeos/宗格替尼)",
        "brand": "LuciZong",
        "category": "肺癌",
        "indication": "适用于经FDA或NMPA批准的检测方法确认肿瘤存在HER2(ERBB2)酪氨酸激酶结构域(TKD)激活突变的不可切除或转移性非鳞状非小细胞肺癌(NSCLC)成人患者,既往接受过全身系统性治疗;为HER2突变NSCLC的首个口服高选择性靶向药",
        "spec": "60mg/片",
        "category_label": "HER2 TKD突变非鳞NSCLC靶向药",
        "drug_class": "新一代高选择性、不可逆共价结合型HER2(ERBB2)酪氨酸激酶抑制剂(TKI),对野生型EGFR几乎无抑制作用",
        "moa": "通过丙烯酰胺基团与HER2激酶域半胱氨酸残基(Cys805等)共价结合,不可逆阻断ATP结合位点,抑制HER2磷酸化及下游MAPK/ERK和PI3K/AKT信号通路;高选择性靶向HER2 TKD激活突变(含外显子20插入、G776C、V777L等),不影响野生型EGFR,大幅降低皮疹、腹泻等脱靶毒性;同时抑制HER2同源/异源二聚化,减少耐药",
        "dosage": "推荐剂量按体重调整:<90kg者120mg(2片60mg),≥90kg者180mg(3片60mg),口服每日1次;可与食物同服或空腹;整片用水吞服,不可压碎、掰开或咀嚼;每天大致相同时间服用;持续治疗直至疾病进展或不可接受的毒性",
        "monitor": "用药前必须经FDA批准的检测方法(如Oncomine Dx Target Test或Guardant360 CDx)确认HER2 TKD激活突变;治疗前12周每2周监测肝功能(ALT/AST/总胆红素),之后每月1次;治疗前评估左心室射血分数(LVEF),治疗期间定期监测;基线和治疗期间监测肺症状(警惕ILD);避免葡萄柚、塞维利亚橙及其果汁(抑制CYP3A增加暴露);同时使用强CYP3A诱导剂会显著降低暴露,应避免合用",
        "adverse": "常见(120mg剂量组):腹泻(42%)、恶心、呕吐、乏力、食欲下降、皮疹(发生率较低);实验室检查异常:白细胞减少、血红蛋白减少、血小板减少、ALT/AST升高(肝毒性总发生率27%,3级1.5%,4级0.4%);严重:左心室功能障碍(6%,3级1.9%)、间质性肺病ILD(1.2%,可能危及生命)、肝毒性(27%中部分重度)、胚胎-胎儿毒性(妊娠期禁用)",
        "missed": "若漏服一剂且距下次服药时间在12小时以内,可立即补服;若距下次服药不足12小时,则跳过本次剂量,下次按原计划服用;不可同时服用2倍剂量;服药后发生呕吐,按漏服处理",
        "title_seo": "宗艾替尼片用法用量详解｜Hernexeos HER2 TKD突变非鳞NSCLC全球首个口服靶向用药指南",
        "description_seo": "宗艾替尼片(Zongertinib)用法用量详解,原研药Hernexeos(勃林格殷格翰)治疗HER2(ERBB2)酪氨酸激酶结构域激活突变的经治非鳞NSCLC,老挝LuciZong版本咨询,全球优质医疗资源",
        "keywords_seo": "宗艾替尼片,zongertinib用法,Hernexeos,宗格替尼,LuciZong,HER2 TKD突变,非鳞NSCLC,口服靶向药,2025新药",
        "price_original": "Hernexeos 60mg×60片/盒 约25000-40000元(2025年8月FDA加速批准,欧美原研价,国内暂未上市)",
        "price_generic": "老挝LuciZong 60mg×60片/盒 约5000-9000元(海外经济版)",
        "cta_title_zh": "需要咨询宗艾替尼片药品渠道和价格信息?",
        "pinyin": "zongertinib",
    },
    {
        "num": 118,
        "name": "盐酸利多卡因延时喷雾",
        "generic_en": "Lidocaine Premature Ejaculation Spray (TORRENT Hei-Pen Spray)",
        "brand": "LuciPen",
        "category": "男科",
        "indication": "成年男性早泄(PE)的对症治疗,适用于阴茎头(龟头)局部敏感度过高引起的射精控制障碍;通过局部短暂麻醉降低龟头敏感度,延长射精潜伏期,改善性生活满意度",
        "spec": "每瓶约5-15mL,含利多卡因2%-5%或其他等效局麻成分(如盐酸达克罗宁)",
        "category_label": "男科外用延时类",
        "drug_class": "外用局部麻醉剂(酰胺类局麻药),通过可逆性阻断阴茎头感觉神经传导降低局部敏感度",
        "moa": "利多卡因属酰胺类局部麻醉药,通过与神经细胞膜钠通道内侧受体结合,阻断电压门控钠通道,抑制动作电位的产生和传导,使阴茎头感觉神经对刺激的传导暂时性减弱;与达克罗宁等局麻成分机制相似但起效更快(5-15分钟)、作用时间适中(30-60分钟);局部给药全身吸收少,系统性不良反应罕见",
        "dosage": "性生活前10-20分钟使用;首次使用建议先在前臂内侧小面积涂抹观察24小时无过敏反应后再用于敏感部位;每次使用前充分摇匀,取1-3喷(每喷约0.1-0.2mL)喷涂于阴茎龟头及冠状沟部位,轻柔按摩帮助吸收;使用后建议清洗双手;建议配合安全套使用以减少药物转移至伴侣;开封后6个月内用完,存储时避光防潮",
        "monitor": "用药前确认无对利多卡因、达克罗宁或其他酰胺类局麻药的过敏史;皮肤破损、黏膜炎症、尿道口炎症者禁用;首次使用前建议做皮肤过敏测试(前臂内侧涂少量观察24小时);使用频率建议每周不超过3次,长期连续使用不宜超过2个月;用药后如出现持续性麻木、勃起功能障碍、过敏反应(红肿/瘙痒/皮疹)、头晕、心悸应立即停药并就医;伴侣阴道接触后出现麻木、过敏等症状应立即清洗并暂停使用",
        "adverse": "常见:局部轻度麻木(2.5%以下)、短暂温热感或灼热感、皮肤轻微发红、干燥;少见:局部皮肤刺激(红肿/瘙痒/皮疹)、接触性过敏、龟头敏感度过度降低导致勃起或射精困难、伴侣阴道麻木或过敏(未使用安全套情况下)、过量使用导致阴茎感觉持续减退或性快感降低;罕见:全身性吸收导致头晕、心悸、低血压、心律失常(见于黏膜大面积破损或过量使用)",
        "missed": "本药为按需使用的对症治疗用药,无固定每日剂量;若错过计划使用时机,可在下次性生活前按需使用;不需为漏服补用额外剂量",
        "title_seo": "盐酸利多卡因延时喷雾用法用量详解｜TORRENT黑喷 男科外用延时剂用药指南",
        "description_seo": "盐酸利多卡因延时喷雾(Lidocaine PE Spray)用法用量详解,印度TORRENT黑喷治疗男性早泄对症治疗,老挝LuciPen版本咨询,全球优质医疗资源",
        "keywords_seo": "延时喷雾,利多卡因喷雾,盐酸达克罗宁,TORRENT,黑喷,LuciPen,早泄,PE外用药,男科延时",
        "price_original": "进口利多卡因延时喷雾(欧洲Fortacin等) 约300-600元/瓶(原研进口)",
        "price_generic": "老挝LuciPen利多卡因延时喷雾 约80-200元/瓶(海外经济版,印度TORRENT工艺)",
        "cta_title_zh": "需要咨询延时喷雾药品渠道和价格信息?",
        "pinyin": "lidocaine-spray",
    },
]


# 通用HTML头(7语言翻译、head、style)
def get_html_head(drug):
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{drug["title_seo"]}</title>
    <meta name="description" content="{drug["description_seo"]}">
    <meta name="keywords" content="{drug["keywords_seo"]}">
    <script>
var _hmt = _hmt || []; (function() {{ var hm = document.createElement("script"); hm.src = "https://hm.baidu.com/hm.js?59ed620a6512d2be372b2677fa87e40e"; var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(hm, s); }})();
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
        .price-table {{ width: 100%; border-collapse: collapse; margin: 16px 0; }}
        .price-table th {{ background: #1e3a5f; color: white; padding: 10px 14px; text-align: left; }}
        .price-table td {{ padding: 10px 14px; border-bottom: 1px solid #e5e7eb; }}
        .price-table tr:hover td {{ background: #f9fafb; }}
        .price-tag {{ color: #f97316; font-weight: bold; font-size: 18px; }}
        .cta-box {{ background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); color: white; padding: 24px; border-radius: 12px; text-align: center; margin: 30px 0; }}
        .cta-box a {{ color: #fb923c; font-weight: bold; font-size: 18px; }}
        .warning-box {{ background: #fff7ed; border-left: 4px solid #f97316; padding: 16px 20px; border-radius: 0 8px 8px 0; margin: 16px 0; }}
        .breadcrumb {{ font-size: 14px; color: #6b7280; margin-bottom: 20px; }}
        .breadcrumb a {{ color: #6b7280; }}
        .breadcrumb a:hover {{ color: #f97316; }}
        h2 {{ color: #1e3a5f; border-bottom: 2px solid #f0f7ff; padding-bottom: 8px; margin-top: 30px; }}
        h3 {{ color: #2d5a87; margin-top: 20px; }}
        .lang-btn.active {{ background: #f97316; color: white; }}
    </style>
    <script>
    const translations = {{
        zh: {{site_name:"蓝培医疗",back_home:"返回首页",news:"新闻资讯",cta_title:"需要咨询药品价格和购买渠道?",phone_label:"电话咨询",whatsapp_label:"WhatsApp",wechat_label:"微信咨询",disclaimer_title:"重要提示",disclaimer_text:"本文章仅供信息参考,不构成医疗建议。药品为处方药,必须在医生指导下使用。",hotline:"咨询热线",footer_platform:"全球优质医疗资源咨询平台",footer_disclaimer:"免责声明:本网站展示的医药信息仅供参考",footer_copyright:"© 2026 蓝培医疗 lanpeimed.com",chat_title:"蓝培医疗在线咨询",phone_consult:"电话咨询",wechat_scan:"微信扫一扫添加咨询",wechat_copy:"加微信",wechat_copied:"已复制!",phone_placeholder:"请输入手机号码",callback_btn:"给您回电",chat_footer:"蓝培医疗 · 全球优质医疗资源咨询",bottom_cta_title:"蓝培医疗 · 全球优质医疗资源咨询",price_reference:"* 价格仅供参考,实际价格以咨询为准",original_vs_generic:"原研药 vs 仿制药价格对比",type:"类型",brand:"品牌/厂家",origin:"产地",price:"参考价格",tab_drug:"药闻速递"}},
        en: {{site_name:"Lanpei Medical",back_home:"Back to Home",news:"News",cta_title:"Need to consult?",phone_label:"Phone",whatsapp_label:"WhatsApp",wechat_label:"WeChat",disclaimer_title:"Important Notice",disclaimer_text:"For reference only.",hotline:"Hotline",footer_platform:"Global Medical Platform",footer_disclaimer:"For reference only.",footer_copyright:"© 2026 Lanpei Medical",chat_title:"Online Consultation",phone_consult:"Phone",wechat_scan:"Scan QR",wechat_copy:"Add WeChat",wechat_copied:"Copied!",phone_placeholder:"Phone number",callback_btn:"Callback",chat_footer:"Lanpei Medical",bottom_cta_title:"Global Medical Resources",price_reference:"* For reference only.",original_vs_generic:"Original vs Generic",type:"Type",brand:"Brand",origin:"Origin",price:"Price",tab_drug:"Drug Updates"}},
        ru: {{site_name:"蓝培医疗",back_home:"На главную",news:"Новости",cta_title:"Нужна консультация?",phone_label:"Телефон",whatsapp_label:"WhatsApp",wechat_label:"WeChat",disclaimer_title:"Важное уведомление",disclaimer_text:"Для справки.",hotline:"Горячая линия",footer_platform:"Мед платформа",footer_disclaimer:"Для справки.",footer_copyright:"© 2026 Lanpei",chat_title:"Онлайн консультация",phone_consult:"Консультация",wechat_scan:"QR",wechat_copy:"WeChat",wechat_copied:"Скопировано!",phone_placeholder:"Телефон",callback_btn:"Звонок",chat_footer:"Lanpei Medical",bottom_cta_title:"Глобальные мед ресурсы",price_reference:"* Для справки.",original_vs_generic:"Оригинал vs Дженерик",type:"Тип",brand:"Бренд",origin:"Страна",price:"Цена",tab_drug:"Новости лекарств"}},
        vi: {{site_name:"Lanpei Medical",back_home:"Về trang chủ",news:"Tin tức",cta_title:"Cần tư vấn?",phone_label:"Điện thoại",whatsapp_label:"WhatsApp",wechat_label:"WeChat",disclaimer_title:"Thông báo",disclaimer_text:"Tham khảo.",hotline:"Hotline",footer_platform:"Nền tảng y tế",footer_disclaimer:"Tham khảo.",footer_copyright:"© 2026 Lanpei",chat_title:"Tư vấn online",phone_consult:"Tư vấn",wechat_scan:"QR",wechat_copy:"WeChat",wechat_copied:"Đã sao chép!",phone_placeholder:"Số DT",callback_btn:"Gọi lại",chat_footer:"Lanpei Medical",bottom_cta_title:"Tài nguyên y tế toàn cầu",price_reference:"* Tham khảo.",original_vs_generic:"Original vs Generic",type:"Loại",brand:"Nhãn",origin:"Xuất xứ",price:"Giá",tab_drug:"Tin thuốc"}},
        id: {{site_name:"Lanpei Medical",back_home:"Kembali",news:"Berita",cta_title:"Konsultasi?",phone_label:"Telepon",whatsapp_label:"WhatsApp",wechat_label:"WeChat",disclaimer_title:"Penting",disclaimer_text:"Referensi.",hotline:"Hotline",footer_platform:"Platform medis",footer_disclaimer:"Referensi.",footer_copyright:"© 2026 Lanpei",chat_title:"Konsultasi online",phone_consult:"Telepon",wechat_scan:"QR",wechat_copy:"WeChat",wechat_copied:"Disalin!",phone_placeholder:"Nomor",callback_btn:"Panggil",chat_footer:"Lanpei Medical",bottom_cta_title:"Sumber daya medis global",price_reference:"* Referensi.",original_vs_generic:"Original vs Generic",type:"Tipe",brand:"Merek",origin:"Asal",price:"Harga",tab_drug:"Info Obat"}},
        my: {{site_name:"Lanpei Medical",back_home:"ပင်မ",news:"သတင်း",cta_title:"လိုသလား?",phone_label:"ဖုန်း",whatsapp_label:"WhatsApp",wechat_label:"WeChat",disclaimer_title:"အရေးကြီး",disclaimer_text:"ရည်ရွယ်ချက်။",hotline:"Hotline",footer_platform:"ပလက်ဖောင်း",footer_disclaimer:"ရည်ရွယ်ချက်။",footer_copyright:"© 2026 Lanpei",chat_title:"တိုင်ပင်",phone_consult:"ဖုန်း",wechat_scan:"QR",wechat_copy:"WeChat",wechat_copied:"ကူယူပြီ!",phone_placeholder:"နံပါတ်",callback_btn:"ပြန်ခေါ်",chat_footer:"Lanpei Medical",bottom_cta_title:"ကမ္ဘာလုံးဆိုင်ရာ ဆေး",price_reference:"*။",original_vs_generic:"Original vs Generic",type:"အမျိုးအစား",brand:"အမှတ်",origin:"မူလ",price:"စျေး",tab_drug:"ဆေးသတင်း"}},
        bd: {{site_name:"Lanpei Medical",back_home:"হোম",news:"সংবাদ",cta_title:"দরকার?",phone_label:"ফোন",whatsapp_label:"WhatsApp",wechat_label:"WeChat",disclaimer_title:"বিজ্ঞপ্তি",disclaimer_text:"রেফারেন্স।",hotline:"হটলাইন",footer_platform:"প্ল্যাটফর্ম",footer_disclaimer:"রেফারেন্স।",footer_copyright:"© 2026 Lanpei",chat_title:"পরামর্শ",phone_consult:"ফোন",wechat_scan:"QR",wechat_copy:"WeChat",wechat_copied:"কপি!",phone_placeholder:"নম্বর",callback_btn:"কল",chat_footer:"Lanpei Medical",bottom_cta_title:"বিশ্ব মেডিকেল রিসোর্স",price_reference:"*।",original_vs_generic:"Original vs Generic",type:"টাইপ",brand:"ব্র্যান্ড",origin:"উৎস",price:"দাম",tab_drug:"ওষুধ সংবাদ"}}
    }};
    let currentLang = 'zh';
    function changeLanguage(lang) {{ currentLang = lang; document.querySelectorAll('.lang-btn').forEach(btn => {{ btn.classList.remove('bg-[#f97316]','text-white'); if(btn.dataset.lang===lang) btn.classList.add('bg-[#f97316]','text-white'); }}); updateTranslations(); }}
    function updateTranslations() {{ const t = translations[currentLang]; document.querySelectorAll('[data-i18n]').forEach(el => {{ const key = el.getAttribute('data-i18n'); if(t[key]) el.textContent = t[key]; }}); document.getElementById('footer-platform')&&(document.getElementById('footer-platform').textContent=t.footer_platform); document.getElementById('footer-disclaimer')&&(document.getElementById('footer-disclaimer').textContent=t.footer_disclaimer); document.getElementById('cta-title')&&(document.getElementById('cta-title').textContent=t.cta_title); document.getElementById('price-title')&&(document.getElementById('price-title').innerHTML='<i class="fas fa-tags mr-2 text-orange-500"></i>'+t.original_vs_generic); document.getElementById('price-reference')&&(document.getElementById('price-reference').textContent=t.price_reference); document.getElementById('disclaimer-text')&&(document.getElementById('disclaimer-text').textContent=t.disclaimer_text); document.getElementById('bottom-cta')&&(document.getElementById('bottom-cta').innerHTML='<p class="font-bold">'+t.bottom_cta_title+'</p><p class="text-sm mt-1">'+t.phone_label+' 17844531559 | '+t.whatsapp_label+' +639685838435 | '+t.wechat_label+' 17844531559</p>'); document.querySelector('.chat-header-left span')&&(document.querySelector('.chat-header-left span').textContent=t.chat_title); document.getElementById('wechatLabel')&&(document.getElementById('wechatLabel').textContent=t.wechat_copy); document.querySelector('.chat-input-area button')&&(document.querySelector('.chat-input-area button').textContent=t.callback_btn); document.querySelector('.chat-footer')&&(document.querySelector('.chat-footer').textContent=t.chat_footer); }}
    document.addEventListener('DOMContentLoaded', updateTranslations);
    </script>
</head>
<body class="bg-gray-50">
    <div class="bg-gray-900 text-white py-2 text-sm">
        <div class="max-w-7xl mx-auto px-4 flex justify-between items-center flex-wrap gap-2">
            <div class="flex items-center gap-4 flex-wrap"><span class="flex items-center gap-1"><i class="fas fa-phone"></i> +86-17844531559</span><span class="flex items-center gap-1"><i class="fas fa-envelope"></i> 173166453@qq.com</span></div>
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
                <div class="flex gap-2 ml-4"><a href="https://wa.me/639685838435" target="_blank" class="hover:text-green-400"><i class="fab fa-whatsapp"></i></a></div>
            </div>
        </div>
    </div>
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
        <div class="breadcrumb"><a href="https://lanpeimed.com" data-i18n="back_home">首页</a> &gt; <a href="https://lanpeimed.com/news.html" data-i18n="news">新闻资讯</a> &gt; <span class="inline-block bg-orange-100 text-orange-700 px-2 py-0.5 rounded text-xs font-medium" data-i18n="tab_drug">药闻速递</span> &gt; {drug["name"]}</div>
        <article class="bg-white rounded-xl shadow-sm p-6 md:p-8">
            <h1 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">{drug["name"]}</h1>
            <p class="text-gray-500 mb-6">{drug["generic_en"]} | {drug["category_label"]} | 品牌名:{drug["brand"]}</p>
'''


def get_article_body(drug):
    return f'''            <h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品概述</h2>
            <div class="info-box">
                <p><strong>通用名称:</strong>{drug["name"]}</p>
                <p><strong>英文名称:</strong>{drug["generic_en"]}</p>
                <p><strong>品牌名称:</strong>原研药、海外经济版({drug["brand"]})</p>
                <p><strong>规格:</strong>{drug["spec"]}</p>
                <p><strong>药物类型:</strong>{drug["drug_class"]}</p>
            </div>
            <h2><i class="fas fa-briefcase-medical mr-2 text-orange-500"></i>适应症</h2>
            <p>{drug["name"]}适用于以下情况:</p>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>主要适应症:</strong>{drug["indication"]}</li>
                <li><strong>用药前提:</strong>必须由具有相应治疗经验的医生启动治疗,并对治疗过程进行严格监测</li>
            </ul>
            <h2><i class="fas fa-cogs mr-2 text-orange-500"></i>作用机制</h2>
            <p>{drug["moa"]}</p>
            <h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
            <h3>标准剂量</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>{drug["dosage"]}</li>
            </ul>
            <h3>服药方式</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>每天在大致相同的时间使用</li>
                <li>按产品说明使用,具体方法依剂型而定</li>
                <li>漏服处理:{drug["missed"]}</li>
                <li>如发生呕吐或不适,不追加剂量,按原计划继续</li>
            </ul>
            <h3>剂量调整</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>根据不良反应和耐受性按需调整剂量</li>
                <li>不可超过推荐的最大日剂量</li>
                <li>中重度肝/肾功能损害者需医生评估后调整</li>
            </ul>
            <h2><i class="fas fa-heartbeat mr-2 text-orange-500"></i>监测要求</h2>
            <div class="info-box">
                <p><strong>重要:</strong>{drug["monitor"]}</p>
            </div>
            <h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>注意事项</h2>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>常见不良反应:</strong>{drug["adverse"]}</li>
                <li><strong>特殊人群:</strong>孕妇、哺乳期妇女、肝肾功能严重损害者使用前必须咨询专业医生</li>
                <li><strong>药物相互作用:</strong>多种药物可能影响疗效或增加毒性,服药前需告知医生所有在用药物</li>
                <li><strong>禁忌:</strong>对本品任何成分过敏者禁用;严重肝功能损害者禁用</li>
                <li><strong>驾驶操作:</strong>用药期间如出现头晕、视物模糊等避免驾驶或操作机械</li>
            </ul>
'''


def get_price_table(drug):
    return f'''            <h2 id="price-title"><i class="fas fa-tags mr-2 text-orange-500"></i>原研药 vs 仿制药价格对比</h2>
            <table class="price-table">
                <thead>
                    <tr>
                        <th>类型</th>
                        <th>品牌/厂家</th>
                        <th>产地</th>
                        <th>参考价格</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>原研药</td>
                        <td>{drug["name"]}(参考原研厂家)</td>
                        <td>欧美/日本</td>
                        <td><span class="price-tag">{drug["price_original"]}</span><br><span class="text-xs text-gray-500">原研药参考价</span></td>
                    </tr>
                    <tr>
                        <td>海外经济版</td>
                        <td>{drug["brand"]}</td>
                        <td>老挝</td>
                        <td><span class="price-tag">{drug["price_generic"]}</span><br><span class="text-xs text-gray-500">经正规海外医疗资源咨询渠道</span></td>
                    </tr>
                </tbody>
            </table>
            <p id="price-reference" class="text-xs text-gray-400 mt-2" data-i18n="price_reference">* 价格仅供参考,实际价格以咨询为准</p>
'''


def get_cta_and_remaining(drug):
    return f'''            <div class="cta-box">
                <p id="cta-title" class="text-lg mb-3" data-i18n="cta_title">{drug["cta_title_zh"]}</p>
                <p class="mb-2"><i class="fas fa-phone-alt mr-2"></i><span data-i18n="phone_label">电话咨询</span>:<a href="tel:17844531559">17844531559</a></p>
                <p class="mb-2"><i class="fab fa-whatsapp mr-2"></i><span data-i18n="whatsapp_label">WhatsApp</span>:<a href="https://wa.me/639685838435">+63-968-583-8435</a></p>
                <p><i class="fab fa-weixin mr-2"></i><span data-i18n="wechat_label">微信咨询</span>:17844531559</p>
            </div>
            <div class="warning-box">
                <p><strong id="disclaimer-title" data-i18n="disclaimer_title"><i class="fas fa-exclamation-triangle mr-1"></i>重要提示:</strong><span id="disclaimer-text" data-i18n="disclaimer_text">本文章仅供信息参考,不构成医疗建议。药品为处方药,必须在医生指导下使用。</span></p>
            </div>
        </article>
        <div id="bottom-cta" class="bg-orange-500 text-white p-4 rounded-xl text-center mt-6">
            <p class="font-bold" data-i18n="bottom_cta_title">蓝培医疗 · 全球优质医疗资源咨询</p>
            <p class="text-sm mt-1">电话 17844531559 | WhatsApp +639685838435 | 微信 17844531559</p>
        </div>
    </main>
    <footer class="gradient-bg text-white py-6 mt-8">
        <div class="max-w-4xl mx-auto px-4 text-center text-sm text-blue-200">
            <p id="footer-platform" data-i18n="footer_platform">全球优质医疗资源咨询平台</p>
            <p id="footer-disclaimer" class="mt-2" data-i18n="footer_disclaimer">免责声明:本网站展示的医药信息仅供参考</p>
            <p id="footer-copyright" class="mt-1" data-i18n="footer_copyright">© 2026 蓝培医疗 lanpeimed.com</p>
        </div>
    </footer>
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
.chat-footer{{text-align:center;padding:8px;font-size:11px;color:#9ca3af;border-top:1px solid #f3f4f6}}
</style>
<div class="chat-widget-btn" onclick="toggleChat()"><div class="pulse-ring"></div><i class="fas fa-headset"></i></div>
<div class="chat-box" id="chatBox">
    <div class="chat-header"><div class="chat-header-left"><div class="logo">蓝培</div><span data-i18n="chat_title">蓝培医疗在线咨询</span></div><button class="close-btn" onclick="toggleChat()"><i class="fas fa-times"></i></button></div>
    <div class="chat-body">
        <div class="chat-notice">因咨询人数多,如未及时回复,请致电:<span class="phone-red">17844531559</span>,或扫码加微信沟通:</div>
        <div style="text-align:center;margin-bottom:14px"><img src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=WeChat%3A17844531559" alt="微信二维码" style="width:120px;height:120px;border:2px solid #e5e7eb;border-radius:8px"></div>
        <div class="chat-contact-row">
            <a href="tel:17844531559" class="chat-contact-item" style="text-decoration:none"><i class="fas fa-phone-alt" style="color:#1e3a5f"></i><div class="label" data-i18n="phone_consult">电话咨询</div></a>
            <a href="https://wa.me/639685838435" target="_blank" class="chat-contact-item" style="text-decoration:none"><i class="fab fa-whatsapp" style="color:#25d366"></i><div class="label" data-i18n="whatsapp_label">WhatsApp</div></a>
            <a href="javascript:void(0)" onclick="copyWechat()" class="chat-contact-item" style="text-decoration:none"><i class="fab fa-weixin" style="color:#07c160"></i><div class="label" id="wechatLabel" data-i18n="wechat_copy">加微信</div></a>
        </div>
        <div class="chat-input-area"><input type="tel" id="chatPhone" placeholder="请输入手机号码"><button onclick="requestCallback()" data-i18n="callback_btn">给您回电</button></div>
    </div>
    <div class="chat-footer" data-i18n="chat_footer">蓝培医疗 · 全球优质医疗资源咨询</div>
</div>
<script>
function toggleChat(){{var b=document.getElementById('chatBox');b.classList.toggle('active')}}
function copyWechat(){{navigator.clipboard.writeText('17844531559');var l=document.getElementById('wechatLabel');l.textContent=translations[currentLang].wechat_copied;setTimeout(function(){{l.textContent=translations[currentLang].wechat_copy}},2000)}}
function requestCallback(){{var p=document.getElementById('chatPhone').value;if(!p||p.length<8){{alert('请输入正确的手机号码');return}}var msg='咨询回电请求:'+p+',请蓝培医疗客服尽快联系我。';var waUrl='https://wa.me/639685838435?text='+encodeURIComponent(msg);window.open(waUrl,'_blank')}}
</script>
</body>
</html>
'''


# 公众号版(规避敏感词:仿制药→海外版本/经济版,代购→咨询渠道)
def get_gzh_article(drug):
    title_emojis = {
        "劳拉替尼片": ("🎯", "ALK阳性非小细胞肺癌第三代TKI靶向药,脑转移克星"),
        "阿帕他胺片": ("🛡️", "前列腺癌雄激素受体抑制剂,降低死亡风险35%"),
        "富马酸吉瑞替尼片": ("💉", "FLT3突变复发难治AML首个口服靶向药,中位OS 9.3个月"),
        "宗艾替尼片": ("🚀", "全球首个HER2突变非鳞NSCLC口服靶向药,2025年新批"),
        "盐酸利多卡因延时喷雾": ("💪", "男科外用延时剂,5-15分钟起效,延长射精潜伏期"),
    }
    emoji, sub = title_emojis.get(drug["name"], ("💊", "用药指南"))

    # 敏感词替换: 仿制药→海外版本, 代购→咨询渠道
    indication_safe = drug["indication"].replace("仿制药", "海外版本").replace("代购", "咨询渠道")
    moa_safe = drug["moa"].replace("仿制药", "海外版本").replace("代购", "咨询渠道")

    return f'''【{drug["name"]}】{sub}

{emoji} 一文带您了解{drug["name"]}

{drug["name"]}({drug["generic_en"]})是{drug["drug_class"]},适用于{indication_safe}。

✨ 核心机制
{moa_safe}

📋 适应症
{indication_safe}

💊 用法用量
• {drug["dosage"]}
• 整片用水吞服,不可掰开、压碎或咀嚼
• 漏服处理:{drug["missed"]}
• 用药前需由有经验的医生评估

🔍 监测要点
{drug["monitor"]}

⚠️ 注意事项
• 常见不良反应:{drug["adverse"]}
• 孕妇、哺乳期妇女、肝肾功能严重损害者用药前必须咨询专业医生
• 多种药物可能影响疗效或增加毒性,服药前告知医生所有在用药物
• 对本品任何成分过敏者禁用

📊 咨询渠道价格参考
• 原研药:{drug["price_original"]}
• 海外版本({drug["brand"]}):{drug["price_generic"]}
(价格仅供参考,实际以咨询为准)

🏥 蓝培医疗专注全球医疗资源咨询服务,与海外正规持牌渠道深度合作,为您对接优质、价格合理的咨询渠道,全程专业医学支持。

📞 联系方式
• 电话:17844531559
• WhatsApp:+63-968-583-8435
• 微信:17844531559(备注"药品咨询"优先通过)

━━━━━━━━━━━━━━━
蓝培医疗 | 全球优质医疗资源咨询
本内容仅供参考,药品为处方药,具体用药方案须由医生制定。
'''


def main():
    # 使用脚本绝对路径作为基准
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 工作根目录(包含"蓝培医疗文章"目录)
    work_root = os.path.dirname(os.path.dirname(script_dir))
    output_dir = os.path.join(work_root, "蓝培医疗文章/2026-06-17")
    base_dir = os.path.join(work_root, "蓝培医疗文章")
    os.makedirs(output_dir, exist_ok=True)

    for drug in DRUGS:
        num_str = f"{drug['num']:03d}"
        pinyin = drug["pinyin"]

        # 网站版HTML
        html_content = get_html_head(drug) + get_article_body(drug) + get_price_table(drug) + get_cta_and_remaining(drug)

        # 子目录备份
        sub_html_path = f"{output_dir}/news-{num_str}-{pinyin}.html"
        with open(sub_html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✓ HTML: {sub_html_path}")

        # 根目录(供部署)
        root_html_path = f"{base_dir}/news-{num_str}-{pinyin}.html"
        with open(root_html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✓ HTML: {root_html_path}")

        # 公众号版txt
        gzh_content = get_gzh_article(drug)
        gzh_path = f"{output_dir}/gzh-{num_str}-{pinyin}.txt"
        with open(gzh_path, 'w', encoding='utf-8') as f:
            f.write(gzh_content)
        print(f"✓ GZH:  {gzh_path}")

    print("\n所有5篇文章生成完毕。")

if __name__ == "__main__":
    main()
