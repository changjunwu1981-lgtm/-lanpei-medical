"""
生成5篇药品文章 HTML + 公众号txt
2026-06-13 第089-093号
- 089 非奈利酮片 finerenone
- 090 马昔腾坦片 macitentan
- 091 波生坦片 bosentan
- 092 达可替尼片 dacomitinib
- 093 培唑帕尼片 pazopanib
"""
import os, json, datetime

# 5个药品的核心数据
DRUGS = [
    {
        "num": 89,
        "name": "非奈利酮片",
        "generic_en": "Finerenone Tablets",
        "brand": "LuciFine",
        "category": "综合药品",
        "indication": "与2型糖尿病相关的慢性肾脏病(CKD)成人患者(伴白蛋白尿)，降低eGFR持续下降、终末期肾病、心血管死亡和因心力衰竭住院的风险",
        "spec": "10mg/片、20mg/片",
        "category_label": "糖尿病肾病用药",
        "drug_class": "非甾体类盐皮质激素受体拮抗剂(nsMRA)",
        "moa": "通过高选择性拮抗盐皮质激素受体(MR)，直接抑制醛固酮介导的炎症与纤维化级联反应，填补RASi无法覆盖的病理缺口",
        "dosage": "目标剂量20mg，每日一次；起始剂量按eGFR调整：eGFR≥60者20mg/日，eGFR 25-59者10mg/日，eGFR<25不推荐起始",
        "monitor": "开始治疗4周后检测血清钾和eGFR；血清钾>5.0mmol/L不能起始；>5.5mmol/L应暂停",
        "adverse": "高钾血症(14.0%)、低钠血症、低血压、瘙痒、eGFR降低；避免与葡萄柚同服",
        "missed": "当天发现尽快补服，仅限当日；切勿双倍补服",
        "title_seo": "非奈利酮片用法用量详解｜Kerendia可申达糖尿病肾病用药指南",
        "description_seo": "非奈利酮片(finerenone)用法用量详解，原研药Kerendia可申达降eGFR下降风险，老挝LuciFine版本咨询，全球优质医疗资源",
        "keywords_seo": "非奈利酮片,finerenone用法,非奈利酮价格,可申达,Kerendia,糖尿病肾病,CKD治疗,盐皮质激素拮抗剂",
        "price_original": "可申达/Kerendia 20mg×14片/盒 约3500-4000元(已纳入医保)",
        "price_generic": "老挝LuciFine 10mg×30片/盒 约200-300元",
        "cta_title_zh": "需要咨询非奈利酮药品渠道和价格信息？",
    },
    {
        "num": 90,
        "name": "马昔腾坦片",
        "generic_en": "Macitentan Tablets",
        "brand": "LuciMaci",
        "category": "综合药品",
        "indication": "肺动脉高压(PAH, WHO第1组)成人患者(WHO功能分级II-III级)，单药或与PDE5抑制剂/吸入性前列腺素类联合使用",
        "spec": "10mg/片",
        "category_label": "肺动脉高压用药",
        "drug_class": "内皮素受体拮抗剂(ERA)，ETA/ETB双重拮抗",
        "moa": "通过阻断内皮素-1与ETA和ETB受体的结合，抑制内皮素介导的血管收缩和肺动脉平滑肌细胞增殖",
        "dosage": "10mg每日一次口服，整片吞服，可与食物同服或空腹服用；不建议高于10mg/日",
        "monitor": "育龄女性治疗前需妊娠试验阴性，治疗期间每月1次；用药前查肝功能和血红蛋白，治疗期间定期复查",
        "adverse": "常见：贫血(13%)、鼻咽炎(14%)、头痛(14%)、肝功能异常(10%)、支气管炎(9%)；严重：肝毒性、血红蛋白下降、胎儿毒性",
        "missed": "尽快补服，并在常规时间服用下一剂；切勿双倍补服",
        "title_seo": "马昔腾坦片用法用量详解｜傲朴舒Opsumit肺动脉高压靶向药指南",
        "description_seo": "马昔腾坦片(Macitentan)用法用量详解，原研药傲朴舒Opsumit延缓PAH进展，老挝LuciMaci版本咨询",
        "keywords_seo": "马昔腾坦片,macitentan用法,马昔腾坦价格,傲朴舒,Opsumit,肺动脉高压,PAH,内皮素受体拮抗剂",
        "price_original": "傲朴舒/Opsumit 10mg×30片/盒 约4000元(已纳入医保)",
        "price_generic": "老挝LuciMaci 10mg×30片/盒 约300-400元",
        "cta_title_zh": "需要咨询马昔腾坦药品渠道和价格信息？",
    },
    {
        "num": 91,
        "name": "波生坦片",
        "generic_en": "Bosentan Tablets",
        "brand": "LuciBose",
        "category": "综合药品",
        "indication": "肺动脉高压(PAH, WHO第1组)WHO功能分级II-IV级成人/3岁以上儿童患者；系统性硬化症伴活动性指端溃疡",
        "spec": "62.5mg/片、125mg/片、分散片32mg",
        "category_label": "肺动脉高压用药",
        "drug_class": "内皮素受体拮抗剂(ERA)",
        "moa": "通过竞争性阻断内皮素-1与ETA和ETB受体的结合，舒张肺血管，降低肺血管阻力",
        "dosage": "初始62.5mg每日两次×4周，维持125mg每日两次；不推荐>125mg每日两次",
        "monitor": "治疗前及用药期间每月1次查肝转氨酶；前12个月每月1次血红蛋白；育龄女性每月妊娠试验",
        "adverse": "肝转氨酶升高(11%可逆)、贫血、呼吸道感染、头痛、潮红；严重：肝衰竭、胎儿致畸",
        "missed": "尽快补服，并在常规时间服用下一剂；切勿双倍补服",
        "title_seo": "波生坦片用法用量详解｜全可利Tracleer肺动脉高压经典用药指南",
        "description_seo": "波生坦片(Bosentan)用法用量详解，原研药全可利Tracleer延缓PAH进展，老挝LuciBose版本咨询",
        "keywords_seo": "波生坦片,bosentan用法,波生坦价格,全可利,Tracleer,肺动脉高压,PAH,内皮素受体拮抗剂",
        "price_original": "全可利/Tracleer 125mg×56片/盒 约4000-5000元(已纳入医保)",
        "price_generic": "老挝LuciBose 125mg×56片/盒 约800-1000元",
        "cta_title_zh": "需要咨询波生坦药品渠道和价格信息？",
    },
    {
        "num": 92,
        "name": "达可替尼片",
        "generic_en": "Dacomitinib Tablets",
        "brand": "LuciDac",
        "category": "肺癌",
        "indication": "单药用于EGFR 19号外显子缺失突变或21号外显子L858R置换突变的局部晚期或转移性非小细胞肺癌(NSCLC)患者的一线治疗",
        "spec": "15mg/片、30mg/片、45mg/片",
        "category_label": "EGFR突变肺癌靶向药",
        "drug_class": "第二代不可逆EGFR/HER1、HER2、HER4酪氨酸激酶抑制剂",
        "moa": "共价结合EGFR(HER1)、HER2、HER4的ATP结合口袋，永久性抑制激酶活性，阻断下游RAS-RAF-MEK-ERK和PI3K-AKT信号通路",
        "dosage": "45mg每日一次口服，可与食物同服或空腹服用；整片吞服；持续用药至疾病进展或不可耐受毒性",
        "monitor": "基线及治疗期定期监测肝功能、肺部症状、心电图；治疗前需经基因检测确认EGFR 19del或L858R突变",
        "adverse": "腹泻(86%，3-4级11%)、皮疹(49%)、甲沟炎(62%)、口腔黏膜炎(44%)；严重：间质性肺病(ILD)、严重腹泻、心脏毒性",
        "missed": "若漏服或呕吐，不追加剂量或补服，下次按原计划服用规定剂量",
        "title_seo": "达可替尼片用法用量详解｜多泽润Vizimpro EGFR突变肺癌一线靶向药指南",
        "description_seo": "达可替尼片(Dacomitinib)用法用量详解，原研药多泽润Vizimpro一线治疗EGFR突变NSCLC，老挝LuciDac版本咨询",
        "keywords_seo": "达可替尼片,dacomitinib用法,达克替尼价格,多泽润,Vizimpro,EGFR突变,非小细胞肺癌,NSCLC一线",
        "price_original": "多泽润/Vizimpro 45mg×30片/盒 约6000-7000元(已纳入医保)",
        "price_generic": "老挝LuciDac 45mg×30片/盒 约800-1000元",
        "cta_title_zh": "需要咨询达可替尼药品渠道和价格信息？",
    },
    {
        "num": 93,
        "name": "培唑帕尼片",
        "generic_en": "Pazopanib Tablets",
        "brand": "LuciPazo",
        "category": "肾癌",
        "indication": "晚期肾细胞癌(RCC)成人患者的一线治疗及曾接受细胞因子治疗的晚期RCC患者；既往化疗的晚期软组织肉瘤(STS)",
        "spec": "200mg/片、400mg/片",
        "category_label": "肾癌靶向药",
        "drug_class": "多靶点酪氨酸激酶抑制剂(TKI)，抑制VEGFR、PDGFR、KIT",
        "moa": "通过抑制VEGFR-2、KIT和PDGFR-β等受体的配体诱导的自身磷酸化，阻断血管生成和肿瘤细胞增殖信号",
        "dosage": "800mg(4片200mg)每日一次空腹服用(餐前1小时或餐后2小时)；整片用水吞服；中度肝损害者200mg每日一次",
        "monitor": "基线及治疗期定期监测肝功能、血压、心电图、甲状腺功能、尿蛋白；重度肝损害者不推荐使用",
        "adverse": "腹泻、高血压、脱发、恶心、厌食、呕吐、疲劳、肝毒性；严重：QT间期延长、心功能障碍、出血、动脉血栓",
        "missed": "若漏服，且距下次剂量不足12小时，则不应补服",
        "title_seo": "培唑帕尼片用法用量详解｜维全特Votrient晚期肾癌靶向药指南",
        "description_seo": "培唑帕尼片(Pazopanib)用法用量详解，原研药维全特Votrient治疗晚期RCC，老挝LuciPazo版本咨询",
        "keywords_seo": "培唑帕尼片,pazopanib用法,培唑帕尼价格,维全特,Votrient,晚期肾癌,RCC,肾细胞癌靶向药",
        "price_original": "维全特/Votrient 200mg×30片/盒 约4000-4500元(已纳入医保)",
        "price_generic": "老挝LuciPazo 200mg×120片/盒 约1000-1500元",
        "cta_title_zh": "需要咨询培唑帕尼药品渠道和价格信息？",
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
        zh: {{site_name:"蓝培医疗",back_home:"返回首页",news:"新闻资讯",cta_title:"需要咨询药品价格和购买渠道？",phone_label:"电话咨询",whatsapp_label:"WhatsApp",wechat_label:"微信咨询",disclaimer_title:"重要提示",disclaimer_text:"本文章仅供信息参考，不构成医疗建议。药品为处方药，必须在医生指导下使用。",hotline:"咨询热线",footer_platform:"全球优质医疗资源咨询平台",footer_disclaimer:"免责声明：本网站展示的医药信息仅供参考",footer_copyright:"© 2026 蓝培医疗 lanpeimed.com",chat_title:"蓝培医疗在线咨询",phone_consult:"电话咨询",wechat_scan:"微信扫一扫添加咨询",wechat_copy:"加微信",wechat_copied:"已复制!",phone_placeholder:"请输入手机号码",callback_btn:"给您回电",chat_footer:"蓝培医疗 · 全球优质医疗资源咨询",bottom_cta_title:"蓝培医疗 · 全球优质医疗资源咨询",price_reference:"* 价格仅供参考，实际价格以咨询为准",original_vs_generic:"原研药 vs 仿制药价格对比",type:"类型",brand:"品牌/厂家",origin:"产地",price:"参考价格",tab_drug:"药闻速递"}},
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
            <p class="text-gray-500 mb-6">{drug["generic_en"]} | {drug["category_label"]} | 品牌名：{drug["brand"]}</p>
'''


def get_article_body(drug):
    """生成文章主体内容"""
    return f'''            <h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品概述</h2>
            <div class="info-box">
                <p><strong>通用名称：</strong>{drug["name"]}</p>
                <p><strong>英文名称：</strong>{drug["generic_en"]}</p>
                <p><strong>品牌名称：</strong>原研药、海外经济版（{drug["brand"]}）</p>
                <p><strong>规格：</strong>{drug["spec"]}</p>
                <p><strong>药物类型：</strong>{drug["drug_class"]}</p>
            </div>
            <h2><i class="fas fa-briefcase-medical mr-2 text-orange-500"></i>适应症</h2>
            <p>{drug["name"]}适用于以下情况：</p>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>主要适应症：</strong>{drug["indication"]}</li>
                <li><strong>用药前提：</strong>必须由具有相应治疗经验的医生启动治疗，并对治疗过程进行严格监测</li>
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
                <li>每天在大致相同的时间服用</li>
                <li>整片用水吞服，不可掰开、压碎或咀嚼</li>
                <li>漏服处理：{drug["missed"]}</li>
                <li>如发生呕吐，不追加剂量，按原计划继续服用</li>
            </ul>
            <h3>剂量调整</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>根据不良反应和耐受性按需调整剂量</li>
                <li>不可超过推荐的最大日剂量</li>
                <li>中重度肝/肾功能损害者需医生评估后调整</li>
            </ul>
            <h2><i class="fas fa-heartbeat mr-2 text-orange-500"></i>监测要求</h2>
            <div class="info-box">
                <p><strong>重要：</strong>{drug["monitor"]}</p>
            </div>
            <h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>注意事项</h2>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>常见不良反应：</strong>{drug["adverse"]}</li>
                <li><strong>特殊人群：</strong>孕妇、哺乳期妇女、肝肾功能严重损害者使用前必须咨询专业医生</li>
                <li><strong>药物相互作用：</strong>多种药物可能影响疗效或增加毒性，服药前需告知医生所有在用药物</li>
                <li><strong>禁忌：</strong>对本品任何成分过敏者禁用；严重肝功能损害者禁用</li>
                <li><strong>驾驶操作：</strong>用药期间如出现头晕、视物模糊等避免驾驶或操作机械</li>
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
                        <td>{drug["name"].replace("片", "")}（参考原研厂家）</td>
                        <td>欧美/日本</td>
                        <td><span class="price-tag">{drug["price_original"]}</span><br><span class="text-xs text-gray-500">已纳入国内医保乙类</span></td>
                    </tr>
                    <tr>
                        <td>海外经济版</td>
                        <td>{drug["brand"]}</td>
                        <td>老挝</td>
                        <td><span class="price-tag">{drug["price_generic"]}</span><br><span class="text-xs text-gray-500">经正规海外医疗资源咨询渠道</span></td>
                    </tr>
                </tbody>
            </table>
            <p id="price-reference" class="text-xs text-gray-400 mt-2" data-i18n="price_reference">* 价格仅供参考，实际价格以咨询为准</p>
'''


def get_cta_and_remaining(drug):
    return f'''            <div class="cta-box">
                <p id="cta-title" class="text-lg mb-3" data-i18n="cta_title">{drug["cta_title_zh"]}</p>
                <p class="mb-2"><i class="fas fa-phone-alt mr-2"></i><span data-i18n="phone_label">电话咨询</span>：<a href="tel:17844531559">17844531559</a></p>
                <p class="mb-2"><i class="fab fa-whatsapp mr-2"></i><span data-i18n="whatsapp_label">WhatsApp</span>：<a href="https://wa.me/639685838435">+63-968-583-8435</a></p>
                <p><i class="fab fa-weixin mr-2"></i><span data-i18n="wechat_label">微信咨询</span>：17844531559</p>
            </div>
            <div class="warning-box">
                <p><strong id="disclaimer-title" data-i18n="disclaimer_title"><i class="fas fa-exclamation-triangle mr-1"></i>重要提示：</strong><span id="disclaimer-text" data-i18n="disclaimer_text">本文章仅供信息参考，不构成医疗建议。药品为处方药，必须在医生指导下使用。</span></p>
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
            <p id="footer-disclaimer" class="mt-2" data-i18n="footer_disclaimer">免责声明：本网站展示的医药信息仅供参考</p>
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
        <div class="chat-notice">因咨询人数多，如未及时回复，请致电：<span class="phone-red">17844531559</span>，或扫码加微信沟通：</div>
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
function requestCallback(){{var p=document.getElementById('chatPhone').value;if(!p||p.length<8){{alert('请输入正确的手机号码');return}}var msg='咨询回电请求：'+p+'，请蓝培医疗客服尽快联系我。';var waUrl='https://wa.me/639685838435?text='+encodeURIComponent(msg);window.open(waUrl,'_blank')}}
</script>
</body>
</html>
'''


# 公众号版
def get_gzh_article(drug):
    title_emojis = {
        "非奈利酮片": ("💊", "糖尿病肾病治疗新选择"),
        "马昔腾坦片": ("💨", "肺动脉高压靶向治疗"),
        "波生坦片": ("🫁", "肺动脉高压经典治疗药"),
        "达可替尼片": ("🎯", "EGFR突变肺癌一线靶向药"),
        "培唑帕尼片": ("🧬", "晚期肾癌靶向治疗"),
    }
    emoji, sub = title_emojis.get(drug["name"], ("💊", "用药指南"))
    return f'''【{drug["name"]}】{sub}，{drug["drug_class"]}！

{emoji} 一文带您了解{drug["name"]}

{drug["name"]}（{drug["generic_en"]}）是{drug["drug_class"]}，适用于{drug["indication"]}。

✨ 核心特点
✅ {drug["moa"][:60]}...
✅ 推荐剂量：{drug["dosage"][:80]}...
✅ 用药前需进行相关检查（详见正文）

📋 适应症
• {drug["indication"]}
• 治疗必须由有经验的医生指导

💊 用法用量
• {drug["dosage"]}
• 整片用水吞服，不可掰开、压碎或咀嚼
• 漏服处理：{drug["missed"]}
• 服药期间定期监测相关指标

⚠️ 注意事项
• 常见不良反应：{drug["adverse"]}
• 孕妇、哺乳期妇女、肝肾功能严重损害者需医生评估
• 多种药物可能影响疗效，服药前告知医生所有用药

📊 价格参考
• 原研药：{drug["price_original"]}
• 海外经济版（{drug["brand"]}）：{drug["price_generic"]}
（价格仅供参考，实际以咨询为准）

🏥 蓝培医疗专注全球医疗资源咨询服务，为您提供正品保障、价格优惠的海外经济版药品咨询渠道。

📞 咨询方式
• 电话：17844531559
• WhatsApp：+63-968-583-8435
• 微信：长按识别下方二维码

━━━━━━━━━━━━━━━
蓝培医疗 | 全球优质医疗资源咨询
'''


def main():
    output_dir = "蓝培医疗文章/2026-06-13"
    os.makedirs(output_dir, exist_ok=True)

    for drug in DRUGS:
        num_str = f"{drug['num']:03d}"
        # 文件名拼音简写
        pinyin_map = {
            "非奈利酮片": "feinailitong",
            "马昔腾坦片": "maxitengtan",
            "波生坦片": "boshengtan",
            "达可替尼片": "daketini",
            "培唑帕尼片": "peizuopani",
        }
        pinyin = pinyin_map.get(drug["name"], drug["generic_en"].lower().split()[0])

        # 网站版HTML
        html_content = get_html_head(drug) + get_article_body(drug) + get_price_table(drug) + get_cta_and_remaining(drug)
        html_path = f"{output_dir}/news-{num_str}-{pinyin}.html"
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✓ HTML: {html_path}")

        # 公众号版txt
        gzh_content = get_gzh_article(drug)
        gzh_path = f"{output_dir}/gzh-{num_str}-{pinyin}.txt"
        with open(gzh_path, 'w', encoding='utf-8') as f:
            f.write(gzh_content)
        print(f"✓ GZH:  {gzh_path}")

    print("\n所有5篇文章生成完毕。")

if __name__ == "__main__":
    main()
