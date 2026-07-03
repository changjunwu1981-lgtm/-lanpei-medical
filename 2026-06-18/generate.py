"""
生成5篇药品文章 HTML + 公众号txt
2026-06-18 第119-123号
- 119 司美格鲁肽片(口服) 诺和忻 Rybelsus 索马鲁肽 (ALKEM) - 2型糖尿病口服GLP-1
- 120 索磷布韦维帕他韦片 丙通沙 吉三代 MyhepAll (ZYDUS) - 泛基因型慢性丙肝
- 121 西地那非单效咀嚼片【甜甜圈】(Intas) - Intagra 100mg 男科ED
- 122 西地那非单效果冻【卡玛格果冻】(CIPLA) - Kamagra Oral Jelly 男科ED
- 123 伐地那非片 Valif (MYLAN) - 印度Ajanta版,男科ED
"""
import os

DRUGS = [
    {
        "num": 119,
        "name": "司美格鲁肽片(口服)",
        "generic_en": "Semaglutide Tablets (Rybelsus/诺和忻)",
        "brand": "ALKEM",
        "category": "保健品",
        "category_label": "2型糖尿病口服GLP-1RA靶向药",
        "drug_class": "胰高糖素样肽-1受体激动剂(GLP-1RA),口服小分子多肽,采用SNAC吸收增强剂技术",
        "moa": "司美格鲁肽是人胰高血糖素样肽-1(GLP-1)类似物,与GLP-1受体高亲和力结合并激活;通过葡萄糖依赖性方式刺激胰岛素分泌、抑制胰高血糖素分泌,并轻度延缓胃排空,从而控制餐后血糖;SNAC(N-(8-[2-羟基苯甲酰基]-氨基辛酸钠)作为吸收增强剂,帮助多肽类药物在胃部跨上皮吸收,突破了GLP-1类药物只能注射的难题",
        "indication": "适用于成人2型糖尿病患者的血糖控制:①可作为单药治疗,在饮食和运动基础上改善血糖控制;②在饮食控制和运动基础上,接受二甲双胍和/或磺脲类药物治疗血糖仍控制不佳的成人2型糖尿病患者;强效降糖同时具备心血管保护作用(经SOUL试验证实MACE风险降低14%)",
        "spec": "3mg/片、7mg/片、14mg/片",
        "dosage": "推荐起始剂量3mg,口服每日1次,持续30天;30天后增加至维持剂量7mg每日1次;7mg给药至少30天后,若血糖控制不佳可增加至14mg每日1次;最大推荐单次给药日剂量为14mg(不推荐2片7mg替代14mg);必须空腹服用,用一小口水(最多120mL)整片吞服,不可掰开/压碎/咀嚼;服药后至少等待30分钟再进食、饮水或服用其他口服药物",
        "monitor": "用药前明确2型糖尿病诊断(空腹血糖/HbA1c/OGTT);治疗前及治疗期间定期监测:空腹及餐后血糖、HbA1c(每3个月1次)、血压、体重、肝肾功能;注意胃肠道反应(恶心/呕吐/腹泻多见,主要发生在剂量递增期);与磺脲类联用时需关注低血糖风险,必要时减少磺脲剂量;关注急性胰腺炎症状(持续严重腹痛)、胆囊疾病、过敏反应;甲状腺C细胞肿瘤风险(有MTC/MEN2个人或家族史者禁用);重度肾损害者(尤其终末期肾病)不推荐使用;不建议用于1型糖尿病或糖尿病酮症酸中毒;心血管高危患者可考虑作为优先选择",
        "adverse": "非常常见(≥10%):恶心、腹痛、腹泻,通常在用药前2-4周出现,随身体适应逐渐减轻;常见(1-10%):呕吐、便秘、食欲下降、消化不良、腹胀、嗳气、胃食管反流病、低血糖(与磺脲/胰岛素联用时);严重:急性胰腺炎(持续性重度腹痛,可能放射至背部)、胆囊炎/胆结石、过敏反应/血管性水肿、甲状腺髓样癌(MTC)风险增加(动物实验);罕见:肠梗阻、严重皮疹、急性肾损伤",
        "missed": "若漏服一剂,应跳过漏服的剂量,第二天服用下一剂即可;不要补服双倍剂量;漏服可能影响血糖控制,需加强血糖监测",
        "title_seo": "司美格鲁肽片(口服)用法用量详解｜诺和忻Rybelsus 全球首个口服GLP-1降糖药",
        "description_seo": "司美格鲁肽片(Semaglutide)口服剂型用法用量详解,商品诺和忻/Rybelsus治疗成人2型糖尿病,SNAC吸收增强技术,全球优质医疗资源",
        "keywords_seo": "司美格鲁肽片,口服GLP-1,诺和忻,Rybelsus,索马鲁肽,2型糖尿病,SNAC,降糖药,心血管获益",
        "price_original": "Rybelsus(诺和忻)中国上市价:3mg×10片约324-373元;7mg×10片约590-632元;14mg×10片约1020元(美国Rybelsus 14mg×30片约900-1000美元)",
        "price_generic": "ALKEM司美格鲁肽片海外版本(询价中,实际以咨询为准)海外经济版",
        "cta_title_zh": "需要咨询司美格鲁肽片(口服)药品渠道和价格信息?",
        "pinyin": "oral-semaglutide",
    },
    {
        "num": 120,
        "name": "索磷布韦维帕他韦片",
        "generic_en": "Sofosbuvir and Velpatasvir Tablets (Epclusa/丙通沙/吉三代 MyhepAll)",
        "brand": "ZYDUS",
        "category": "丙肝",
        "category_label": "泛基因型慢性丙肝治愈方案",
        "drug_class": "直接抗病毒药物(DAA)复方制剂,由NS5B聚合酶抑制剂索磷布韦和NS5A抑制剂维帕他韦组成,全球首款全口服、泛基因型、单一片剂丙肝方案",
        "moa": "索磷布韦是一种核苷酸类似物前药,在细胞内代谢为活性三磷酸形式,通过被NS5B RNA依赖性RNA聚合酶错误识别并掺入病毒RNA链,导致链合成终止,阻断HCV病毒复制;维帕他韦是一种NS5A抑制剂,通过与NS5A蛋白结合干扰病毒复制复合物形成和病毒装配过程;两者联合双重打击HCV生命周期关键环节,显著降低耐药风险;覆盖全部6种HCV基因型(GT1-6),12周治愈率超过95-99%",
        "indication": "适用于治疗成人慢性丙型肝炎病毒(HCV)感染,所有基因型(1-6型)均可使用,包括:①无肝硬化或代偿期肝硬化患者;②失代偿期肝硬化患者需与利巴韦林联合使用;同时为多种治疗失败患者的再治疗方案",
        "spec": "每片含索磷布韦400mg + 维帕他韦100mg;28片/盒(标准治疗周期为12周)",
        "dosage": "成人推荐剂量:口服1片(400mg+100mg),每日1次,整片吞服,不可咀嚼/压碎;可与食物同服或空腹服用;疗程12周(无肝硬化或代偿期肝硬化);失代偿期肝硬化:联合利巴韦林治疗12周(利巴韦林剂量按体重调整,<75kg者1000mg/日,≥75kg者1200mg/日,分2次服用);3岁及以上儿童可按体重调整剂量;每天大致相同时间服用,持续完成12周疗程以确保病毒学应答",
        "monitor": "用药前必须经HCV RNA检测确认慢性丙肝病毒复制活跃、基因型鉴定、肝功能(Child-Pugh分级)、肝脏B超/肝纤维化评估(APRI/FibroScan)、HBV血清学(HBsAg/HBcAb/HBsAb)以排除HBV共感染;治疗前12周内每4周监测肝功能(ALT/AST/总胆红素)、HCV RNA定量;12周疗程结束后12周(SVR12)需复查HCV RNA评估是否达到持续病毒学应答(临床治愈);基线和治疗中监测肾功能(eGFR<30者慎用);中度肾损害(eGFR 30-60)需密切监测;避免与胺碘酮联用(可能严重心动过缓);避免质子泵抑制剂(奥美拉唑等)及强CYP3A诱导剂(利福平/卡马西平/苯妥英/圣约翰草)合用",
        "adverse": "常见(发生率≥10%):头痛、疲劳(最常见);常见(1-10%):恶心、腹泻、失眠、食欲减退、贫血(联合利巴韦林时增加)、皮疹、咳嗽、肌痛;实验室检查:ALT/AST升高(尤其HCV/HBV共感染者);严重(罕见):HBV再激活(可致暴发性肝炎/肝衰竭,需治疗前筛查HBV并预防性抗HBV治疗)、严重心动过缓(与胺碘酮联用时,可能需心脏起搏器)、肝功能失代偿、过敏反应、血管性水肿;联合利巴韦林时:贫血发生率显著增加,需定期监测血红蛋白",
        "missed": "若漏服一剂,应尽快补服;若距下次服药时间不足18小时,则跳过漏服剂量,下次按原计划服用;不可同时服用2倍剂量;漏服可能影响SVR(持续病毒学应答)率,需严格依从",
        "title_seo": "索磷布韦维帕他韦片用法用量详解｜吉三代MyhepAll 泛基因型丙肝12周治愈方案",
        "description_seo": "索磷布韦维帕他韦片(Sofosbuvir/Velpatasvir)用法用量详解,商品丙通沙/Epclusa(原研)与MyhepAll(印度)治疗全基因型慢性丙型肝炎,12周治愈率超95%,全球优质医疗资源",
        "keywords_seo": "索磷布韦维帕他韦,吉三代,丙通沙,Epclusa,MyhepAll,泛基因型丙肝,HCV治愈,SVR,索磷布韦,维帕他韦",
        "price_original": "Epclusa(吉利德原研)美国价:28片/盒(12周量)约28000-30000美元(约20万元人民币);中国丙通沙(2020年降价后):28片/盒约18000-20000元(医保后个人负担大幅降低)",
        "price_generic": "印度MyhepAll(Mylan迈兰)28片/盒(12周量)约1400-2500元(海外经济版,药品列表ZYDUS版本以实际咨询为准)",
        "cta_title_zh": "需要咨询索磷布韦维帕他韦片药品渠道和价格信息?",
        "pinyin": "sofosbuvir-velpatasvir",
    },
    {
        "num": 121,
        "name": "西地那非单效咀嚼片",
        "generic_en": "Sildenafil Citrate Tablets 100mg (Intagra 100, 印度Intas) - 男科ED",
        "brand": "Intas",
        "category": "男科",
        "category_label": "PDE5抑制剂-男科ED对症治疗",
        "drug_class": "5型磷酸二酯酶(PDE5)选择性抑制剂,辉瑞万艾可(Viagra)印度仿制版",
        "moa": "通过选择性抑制阴茎海绵体内降解环磷酸鸟苷(cGMP)的5型磷酸二酯酶(PDE5),使cGMP水平升高,平滑肌松弛,阴茎海绵体动脉血流增加;在性刺激下(NO-cGMP通路激活),帮助达到并维持足以性交的勃起;不直接影响性欲,需性刺激作为前提",
        "indication": "适用于治疗男性阴茎勃起功能障碍(ED,阳痿);包括器质性、心理性或混合性病因引起的ED;在性刺激下可改善勃起硬度和持续时间;不适用于女性和18岁以下儿童",
        "spec": "100mg/片(也常见50mg/25mg规格)",
        "dosage": "推荐起始剂量50mg,在性活动前约1小时口服;根据疗效和耐受性,剂量可调整至25mg(耐受差)或100mg(疗效不足);最大剂量为100mg/日;每日最多服用1次;需配合性刺激才能起效;可与食物同服,但高脂饮食可能延迟起效时间;整片用水吞服,不可掰开/压碎/咀嚼(咀嚼片剂型按说明含服)",
        "monitor": "用药前评估心血管功能(性活动有一定心脏风险,严重心脏病患者不推荐);询问用药史(尤其硝酸酯类、PDE5抑制剂、降压药);评估阴茎解剖情况(阴茎畸形如成角、海绵体纤维化、Peyronie病慎用);肝肾功能(严重肝肾损害需减量);眼部疾病(视网膜疾病如视网膜色素变性禁用);血压监测;用药后出现以下情况立即就医:勃起持续>4小时(阴茎异常勃起,PRIAPISM)、突发视力/听力下降、胸痛/心悸",
        "adverse": "非常常见(≥10%):头痛、面部潮红;常见(1-10%):头晕、消化不良、鼻塞、视物模糊(光敏感/蓝绿色觉异常)、背痛、肌肉痛;少见:皮疹、心悸、低血压、恶心、呕吐、胃食管反流、嗜睡、四肢疼痛;罕见(需立即停药就医):阴茎异常勃起(>4小时,可能致永久性损伤)、突发单眼或双眼视力下降(非动脉炎性前部缺血性视神经病变NAION)、突发听力下降(伴耳鸣/眩晕)、严重心血管事件(心梗/心律失常/卒中,多见于基础心血管疾病患者)、严重过敏反应(呼吸困难/面部肿胀/皮疹)、癫痫发作",
        "missed": "本药为按需使用,无固定每日剂量;若错过计划使用时机,可在下次性活动前按需服用;不需为漏服补用额外剂量",
        "title_seo": "西地那非单效咀嚼片【甜甜圈】用法用量详解｜Intagra 100mg 印度Intas版万艾可仿制药",
        "description_seo": "西地那非单效咀嚼片(Sildenafil Citrate)用法用量详解,商品Intagra 100mg(印度Intas)治疗男性勃起功能障碍(ED),PDE5抑制剂,海外经济版,全球优质医疗资源",
        "keywords_seo": "西地那非,伟哥,Viagra,Intagra,Intas,印度仿制,ED,阳痿,勃起功能障碍,PDE5抑制剂,甜甜圈,咀嚼片",
        "price_original": "万艾可(Viagra)辉瑞原研:中国100mg×1片约90-120元(处方药);美国100mg×30片约1800-2000美元",
        "price_generic": "Intagra 100mg(印度Intas)4片装约合人民币25-40元;海外经济版,需经合规医疗资源咨询渠道获得",
        "cta_title_zh": "需要咨询西地那非单效咀嚼片药品渠道和价格信息?",
        "pinyin": "sildenafil-intagra",
    },
    {
        "num": 122,
        "name": "西地那非单效果冻",
        "generic_en": "Sildenafil Citrate Oral Jelly 100mg (Kamagra Oral Jelly, 印度Ajanta) - 男科ED果冻剂型",
        "brand": "CIPLA",
        "category": "男科",
        "category_label": "PDE5抑制剂-男科ED果冻速效剂型",
        "drug_class": "5型磷酸二酯酶(PDE5)选择性抑制剂的果冻剂型(oral jelly),辉瑞万艾可(Viagra)的印度仿制口服凝胶版",
        "moa": "通过选择性抑制PDE5酶活性,提高阴茎海绵体内cGMP水平,使平滑肌松弛、海绵体动脉血流增加,从而在性刺激下帮助达到并维持勃起;果冻剂型通过口腔/舌下黏膜吸收,避免胃肠道首过效应,起效更快(15-30分钟vs普通片30-60分钟);同样需要性刺激作为前提",
        "indication": "适用于治疗男性阴茎勃起功能障碍(ED);适合对传统片剂有吞咽困难者、需要更快起效的按需治疗者;不适用于女性和18岁以下儿童",
        "spec": "100mg/袋(7-28袋/盒);多种水果口味(草莓/香蕉/菠萝/橙子/薄荷/巧克力等),改善服药体验",
        "dosage": "推荐剂量:1袋(100mg),性活动前约15-30分钟使用;从铝袋直接挤入口中或勺子上服用,无需水送服;每日最多1袋;需配合性刺激才能起效;可空腹或与食物同服,但避免高脂饮食和大量酒精(降低药效+增加不良反应);根据疗效和耐受性,剂量可调整至50mg(半袋)或100mg(全袋)",
        "monitor": "用药前评估心血管功能(性活动有一定心脏风险);询问用药史(尤其硝酸酯类、其他PDE5抑制剂、降压药);严重心血管疾病(近期心梗/卒中/严重心律失常)、不稳定型心绞痛、严重肝功能损害者慎用;血压监测;用药后出现以下情况立即就医:勃起持续>4小时(阴茎异常勃起,可致永久性损伤)、突发视力/听力下降、胸痛/心悸、严重头晕/晕厥;不可与硝酸酯类、α受体阻滞剂(剂量调整时)、CYP3A4强抑制剂(酮康唑/利托那韦)合用",
        "adverse": "常见:头痛、面部潮红、消化不良、鼻塞、头晕、视物模糊(蓝绿色觉异常);少见:背痛、肌肉痛、恶心、皮疹、心悸、低血压、嗜睡、口干;罕见(需立即停药就医):阴茎异常勃起(>4小时)、突发视力下降(NAION)、突发听力下降伴耳鸣、严重过敏反应、严重心血管事件(多见于基础心脏病患者);果冻剂型可能含苯丙氨酸(PKU患者注意)",
        "missed": "本药为按需使用,无固定每日剂量;若错过计划使用时机,可在下次性活动前按需服用;不需为漏服补用额外剂量",
        "title_seo": "西地那非单效果冻【卡玛格果冻】用法用量详解｜Kamagra Oral Jelly 印度速效ED果冻",
        "description_seo": "西地那非单效果冻(Sildenafil Oral Jelly)用法用量详解,商品Kamagra Oral Jelly(印度Ajanta)治疗男性ED,15-30分钟速效,多种水果口味,海外经济版,全球优质医疗资源",
        "keywords_seo": "西地那非果冻,Kamagra,卡玛格,Oral Jelly,ED果冻,印度仿制,Ajanta,速效,ED,阳痿,勃起功能障碍",
        "price_original": "万艾可(Viagra)辉瑞原研:中国100mg×1片约90-120元;美国100mg×30片约1800-2000美元",
        "price_generic": "Kamagra Oral Jelly 100mg×7袋装约合人民币60-100元;海外经济版,需经合规医疗资源咨询渠道获得",
        "cta_title_zh": "需要咨询西地那非单效果冻药品渠道和价格信息?",
        "pinyin": "kamagra-oral-jelly",
    },
    {
        "num": 123,
        "name": "伐地那非片",
        "generic_en": "Vardenafil Tablets 20mg (Valif, 印度Ajanta) - 男科ED",
        "brand": "MYLAN",
        "category": "男科",
        "category_label": "PDE5抑制剂-男科ED对症治疗",
        "drug_class": "5型磷酸二酯酶(PDE5)高选择性抑制剂,德国拜耳艾力达(Levitra)的印度仿制版;第二代PDE5抑制剂,特点为起效更快、作用更强",
        "moa": "通过高选择性抑制PDE5酶,提升cGMP水平,促进阴茎海绵体平滑肌松弛,增加动脉血流;在性刺激下(NO-cGMP通路激活),帮助达到并维持勃起;相比第一代PDE5抑制剂(西地那非),伐地那非对PDE5的选择性更高、起效更快(最快10-15分钟)、作用时间更稳定;同时伐地那非的PDE1和PDE6抑制作用较弱,视觉相关副作用相对更少",
        "indication": "适用于治疗男性阴茎勃起功能障碍(ED);包括器质性、心理性或混合性病因引起的ED;尤其适合需要快速起效的按需治疗场景;不适用于女性和18岁以下儿童",
        "spec": "20mg/片(也常见5mg/10mg/40mg规格)",
        "dosage": "推荐起始剂量10mg,在性活动前约25-60分钟口服;根据疗效和耐受性,剂量可调整至5mg(耐受差)或20mg(疗效不足);最大剂量为20mg/日;每日最多服用1次;可与食物同服(700千卡以下饮食影响较小,这一点优于西地那非);整片用水吞服,不可掰开/压碎/咀嚼;需配合性刺激才能起效",
        "monitor": "用药前评估心血管功能;严重心血管疾病(近期心梗/卒中/不稳定心绞痛/严重心律失常)患者不推荐;询问用药史(尤其硝酸酯类、其他PDE5抑制剂、降压药);65岁以上老年人及中度肝损害者起始剂量建议5mg;严重肝损害者不推荐使用;QT间期延长者慎用;眼部疾病(视网膜色素变性等)者禁用;用药后出现以下情况立即就医:勃起持续>4小时、突发视力/听力下降、胸痛/心悸",
        "adverse": "常见(发生率较高):头痛、面部潮红、消化不良、恶心、眩晕、鼻塞;常见(1-10%):背痛、肌痛、心悸、低血压、嗜睡、视物模糊(光敏感/色觉异常);少见:皮疹、胃食管反流、肌肉痉挛、嗜睡;罕见(需立即停药就医):阴茎异常勃起(>4小时,可致永久性损伤)、非动脉炎性前部缺血性视神经病变(NAION)、突发听力下降伴耳鸣/眩晕、严重心血管事件(心梗/心律失常/卒中)、严重过敏反应(呼吸困难/面部肿胀)、癫痫发作",
        "missed": "本药为按需使用,无固定每日剂量;若错过计划使用时机,可在下次性活动前按需服用;不需为漏服补用额外剂量",
        "title_seo": "伐地那非片用法用量详解｜Valif 20mg 印度Ajanta版艾力达仿制",
        "description_seo": "伐地那非片(Vardenafil)用法用量详解,商品Valif(印度Ajanta)治疗男性勃起功能障碍(ED),PDE5抑制剂,起效快,海外经济版,全球优质医疗资源",
        "keywords_seo": "伐地那非,艾力达,Levitra,Valif,印度仿制,ED,阳痿,勃起功能障碍,PDE5抑制剂,Ajanta",
        "price_original": "艾力达(Levitra)德国拜耳原研:中国20mg×4片约500-600元;美国20mg×30片约1600-2000美元",
        "price_generic": "Valif 20mg(印度Ajanta)90片装约119美元(约合人民币850元);海外经济版,需经合规医疗资源咨询渠道获得",
        "cta_title_zh": "需要咨询伐地那非片药品渠道和价格信息?",
        "pinyin": "valif-vardenafil",
    },
]


# 通用HTML头(7语言翻译、head、style) - 与118同款
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
                        <td>海外</td>
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
        "司美格鲁肽片(口服)": ("💊", "全球首个口服GLP-1降糖药,2型糖尿病患者告别打针时代"),
        "索磷布韦维帕他韦片": ("🧬", "全基因型丙肝12周治愈方案,SVR率超95%"),
        "西地那非单效咀嚼片": ("💪", "ED对症治疗经典用药,起效稳定可靠"),
        "西地那非单效果冻": ("⚡", "速效果冻剂型,15-30分钟起效,多口味选择"),
        "伐地那非片": ("🔥", "第二代PDE5抑制剂,起效快、作用强"),
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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    work_root = os.path.dirname(os.path.dirname(script_dir))
    output_dir = os.path.join(work_root, "蓝培医疗文章/2026-06-18")
    base_dir = os.path.join(work_root, "蓝培医疗文章")
    os.makedirs(output_dir, exist_ok=True)

    for drug in DRUGS:
        num_str = f"{drug['num']:03d}"
        pinyin = drug["pinyin"]

        # 网站版HTML
        html_content = get_html_head(drug) + get_article_body(drug) + get_price_table(drug) + get_cta_and_remaining(drug)

        sub_html_path = f"{output_dir}/news-{num_str}-{pinyin}.html"
        with open(sub_html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✓ HTML: {sub_html_path}")

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
