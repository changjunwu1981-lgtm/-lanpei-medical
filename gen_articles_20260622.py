#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成蓝培医疗药品文章HTML - 2026-06-22批次（139-143）"""

import os

# 基础模板（与gen_articles_20260621.py保持一致，添加 article-meta 日期）
def build_html(drug):
    """生成单篇HTML文件"""
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{drug['seo_title']}</title>
    <meta name="description" content="{drug['seo_desc']}">
    <meta name="keywords" content="{drug['seo_keywords']}">
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
        ru: {{site_name:"Lan培医疗",back_home:"На главную",news:"Новости",cta_title:"Нужна консультация?",phone_label:"Телефон",whatsapp_label:"WhatsApp",wechat_label:"WeChat",disclaimer_title:"Важное уведомление",disclaimer_text:"Для справки.",hotline:"Горячая линия",footer_platform:"Мед платформа",footer_disclaimer:"Для справки.",footer_copyright:"© 2026 Lanpei",chat_title:"Онлайн консультация",phone_consult:"Консультация",wechat_scan:"QR",wechat_copy:"WeChat",wechat_copied:"Скопировано!",phone_placeholder:"Телефон",callback_btn:"Звонок",chat_footer:"Lanpei Medical",bottom_cta_title:"Глобальные мед ресурсы",price_reference:"* Для справки.",original_vs_generic:"Оригинал vs Дженерик",type:"Тип",brand:"Бренд",origin:"Страна",price:"Цена",tab_drug:"Новости лекарств"}},
        vi: {{site_name:"Lanpei Medical",back_home:"Về trang chủ",news:"Tin tức",cta_title:"Cần tư vấn?",phone_label:"Điện thoại",whatsapp_label:"WhatsApp",wechat_label:"WeChat",disclaimer_title:"Thông báo",disclaimer_text:"Tham khảo.",hotline:"Hotline",footer_platform:"Nền tảng y tế",footer_disclaimer:"Tham khảo.",hotline:"Hotline",footer_copyright:"© 2026 Lanpei",chat_title:"Tư vấn online",phone_consult:"Tư vấn",wechat_scan:"QR",wechat_copy:"WeChat",wechat_copied:"Đã sao chép!",phone_placeholder:"Số DT",callback_btn:"Gọi lại",chat_footer:"Lanpei Medical",bottom_cta_title:"Tài nguyên y tế toàn cầu",price_reference:"* Tham khảo.",original_vs_generic:"Original vs Generic",type:"Loại",brand:"Nhãn",origin:"Xuất xứ",price:"Giá",tab_drug:"Tin thuốc"}},
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
        <div class="breadcrumb"><a href="https://lanpeimed.com" data-i18n="back_home">首页</a> &gt; <a href="https://lanpeimed.com/news.html" data-i18n="news">新闻资讯</a> &gt; <span class="inline-block bg-orange-100 text-orange-700 px-2 py-0.5 rounded text-xs font-medium" data-i18n="tab_drug">药闻速递</span> &gt; {drug['name']}</div>
        <article class="bg-white rounded-xl shadow-sm p-6 md:p-8">
            <h1 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">{drug['name']}</h1>
            <p class="text-gray-500 mb-6">{drug['subtitle']}</p>
{drug['content']}
            <div class="cta-box">
                <p id="cta-title" class="text-lg mb-3" data-i18n="cta_title">需要咨询{drug['name']}药品渠道和价格信息?</p>
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
.chat-input-area button:hover{{background:linear-gradient(135deg,#2d5a87,#3a6d9e)}}
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
</html>'''


# 139: 博舒替尼片 Bosuvi (Intas) - 白血病 - 100/400/500mg
drug_bosuvi = {
    "name": "博舒替尼片 Bosuvi",
    "filename": "news-139-bosuvi.html",
    "seo_title": "博舒替尼片Bosuvi用法用量详解｜Intas印度版 100/400/500mg二代TKI Ph+慢性粒细胞白血病CML口服靶向",
    "seo_desc": "博舒替尼片Bosuvi(Bosutinib Tablets 100/400/500mg,Intas印度版)用法用量详解,Ph+慢性粒细胞白血病(CML)新诊断慢性期/加速期/急变期靶向治疗,原研Bosulif等效替代,海外白血病靶向药咨询,全球优质医疗资源",
    "seo_keywords": "博舒替尼片,Bosuvi,Intas,Bosutinib,二代TKI,Ph+CML,慢性粒细胞白血病,白血病,口服靶向药,Bosulif",
    "subtitle": "Bosutinib Tablets 100/400/500mg (Bosuvi, Intas) - 二代酪氨酸激酶抑制剂(TKI) | 品牌:Bosulif博舒替尼(Pfizer)",
    "content": '''<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品概述</h2>
            <div class="info-box">
                <p><strong>通用名称:</strong>博舒替尼 (Bosutinib)</p>
                <p><strong>英文名称:</strong>Bosutinib Tablets 100mg/400mg/500mg (Bosuvi, Intas) - 2nd Gen Tyrosine Kinase Inhibitor (TKI)</p>
                <p><strong>品牌名称:</strong>原研药Bosulif博舒替尼(Pfizer辉瑞,2012年美国FDA批准),海外经济版Bosuvi(Intas)、Bonitar(Sun Pharma)、Bosutris(印度多家)等</p>
                <p><strong>规格:</strong>100mg/片(黄褐色,椭圆形);400mg/片(橙色,椭圆形);500mg/片(红色,椭圆形);均带Pfizer/Intas字样压印</p>
                <p><strong>药物类型:</strong>第二代酪氨酸激酶抑制剂(TKI);针对BCR-ABL激酶的ATP竞争性抑制剂,同时抑制SRC家族激酶;Intas(印度领先跨国仿制药企业,业务遍及85+国家)Bosuvi印度版,活性成分、剂型、规格、给药途径与原研Bosulif基本一致,经印度DCGI严格审查批准上市;为Ph+慢性粒细胞白血病患者提供经济可及的治疗选择</p>
            </div>
            <h2><i class="fas fa-briefcase-medical mr-2 text-orange-500"></i>适应症</h2>
            <p>博舒替尼片 Bosuvi适用于以下情况:</p>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>主要适应症-新诊断慢性期Ph+ CML:</strong>用于治疗成人新诊断的费城染色体阳性慢性粒细胞白血病慢性期(Ph+ CML-CP)患者</li>
                <li><strong>主要适应症-耐药或不耐受Ph+ CML:</strong>用于治疗既往接受过一种或多种TKI治疗失败或不耐受的成人Ph+ CML慢性期、加速期(AP)或急变期(BP)患者;当伊马替尼、尼洛替尼、达沙替尼不适合时考虑使用</li>
                <li><strong>儿科适应症:</strong>1岁及以上儿童慢性期Ph+ CML,新诊断者按BSA 300mg/m²/日;耐药/不耐受者按BSA 400mg/m²/日</li>
                <li><strong>用药前提:</strong>须由具有CML管理经验血液/肿瘤专科医生启动;用药前评估肝功能(ALT/AST/胆红素);基线胃肠道状态(腹泻管理);肾功能(老年/肾损者);注意与CYP3A抑制剂/诱导剂相互作用</li>
            </ul>
            <h2><i class="fas fa-cogs mr-2 text-orange-500"></i>作用机制</h2>
            <p>博舒替尼是强效第二代酪氨酸激酶抑制剂,能同时抑制BCR-ABL融合蛋白和SRC家族激酶(LYN/HCK)的活性;通过竞争性结合BCR-ABL的ATP结合位点,阻断酪氨酸残基磷酸化,抑制白血病细胞增殖信号传导;对野生型BCR-ABL及多数耐药突变(M244V、G250E、Q252H、E255K/V、F317L、F359V等)均有活性,但T315I和V299L突变耐药;口服后吸收迅速,4-6小时达峰;餐时服用生物利用度增加约2倍;血浆蛋白结合率约94%;主要经CYP3A4代谢,半衰期约22小时;约91%经粪便、3%经尿排泄;Intas(印度领先跨国仿制药企业,业务遍及85+国家)Bosuvi印度版与原研Bosulif在活性成分、剂型、规格、给药途径上完全一致,经印度DCGI严格审查批准上市</p>
            <h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
            <h3>标准剂量</h3>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>成人新诊断CP Ph+ CML:</strong>推荐400mg/次,口服,每日1次,餐时服用;持续治疗直至疾病进展或不可耐受</li>
                <li><strong>成人CP/AP/BP Ph+ CML R/I患者:</strong>推荐500mg/次,口服,每日1次,餐时服用;持续治疗直至疾病进展或不可耐受</li>
                <li><strong>剂量递增:</strong>成人新诊断CP患者:3个月时若BCR-ABL转录本>10%且无3级以上不良反应,可每2周递增100mg至最大600mg/日;成人R/I患者:疗效不满意且无3-4级AE,可递增100mg至最大600mg/日</li>
            </ul>
            <h3>服药方式</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>整片吞服,不可咀嚼/压碎/掰开/切割;不可接触破损药片(活性成分可能引起皮肤刺激);建议固定每日同一时间餐时服用;若漏服超过12小时,跳过本次,次日常规剂量服用,切勿双倍补服</li>
                <li>若不能整片吞服,可在医师指导下打开胶囊(部分版本)将内容物与苹果酱/酸奶混合立即吞服,不可保留</li>
            </ul>
            <h3>特殊人群剂量调整</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>老年人(≥65岁):无需初始剂量调整,但应密切监测肝肾毒性</li>
                <li>肝功能不全:轻度(Child-Pugh A):无需调整;中度(B):200mg/日;重度(C):100mg/日;肝酶>5×ULN:暂停至恢复至≤2.5×ULN后减量100mg/日恢复</li>
                <li>肾功能不全:CrCl>50mL/min:无需调整;CrCl 30-50mL/min:400mg/日;CrCl<30mL/min:300mg/日</li>
                <li>儿童(≥1岁):按BSA计算,新诊断300mg/m²/日;R/I 400mg/m²/日;最大不超过500mg/日</li>
            </ul>
            <h2><i class="fas fa-heartbeat mr-2 text-orange-500"></i>监测要求</h2>
            <div class="info-box">
                <p>用药前:肝功能(ALT/AST/胆红素)、肾功能、血常规、BCR-ABL定量、心电图(基础QTc);用药期间:第1个月每周1次血常规,之后每月;前3个月每月1次肝功能,之后按需;腹泻监测(分级管理);每3个月BCR-ABL定量评估分子学反应;出现胸闷、呼吸困难、水肿等立即评估心脏功能</p>
            </div>
            <h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>注意事项</h2>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>常见不良反应:</strong>极常见(≥20%):腹泻(80%+)、恶心、呕吐、腹痛、皮疹、疲乏、发热、肝酶升高;常见(10-20%):血小板减少、贫血、中性粒细胞减少、头痛、关节痛、呼吸困难、咳嗽、水肿</li>
                <li><strong>重要警告:</strong>①胃肠道毒性:80%以上患者出现腹泻(3-4级约8-9%),需预防性止泻、补液、调整剂量;②骨髓抑制:血小板减少/贫血/中性粒细胞减少,定期监测血常规;③肝毒性:前3个月每月监测肝功能;④心脏毒性:充血性心衰/心律失常/心包炎/心肌梗死(<1%但严重);⑤体液潴留:胸腔/心包积液、肺水肿、外周水肿</li>
                <li><strong>禁忌:</strong>对本品过敏者;严重肝功能不全未调整剂量者</li>
                <li><strong>特殊人群:</strong>孕妇:有胎儿毒性,使用需严格权衡利弊(育龄期用药需避孕至停药后1个月);哺乳期:不建议使用;儿童:1岁以下不推荐</li>
                <li><strong>药物相互作用:</strong>强CYP3A抑制剂(酮康唑、伊曲康唑、伏立康唑、克拉霉素、利托那韦等)显著升高血药浓度,需避免合用或密切监测;强CYP3A诱导剂(利福平、卡马西平、苯妥英、圣约翰草)显著降低血药浓度,需避免合用;质子泵抑制剂(PPI)可能降低吸收(避免同服或换用H2受体拮抗剂);葡萄柚/西柚制品增加血药浓度,需避免</li>
            </ul>
            <h2 id="price-title"><i class="fas fa-tags mr-2 text-orange-500"></i>原研药 vs 仿制药价格对比</h2>
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
                        <td>Bosulif 博舒替尼 (Pfizer)</td>
                        <td>美国/全球100+国家(2012年FDA;2013年EMA;中国未上市)</td>
                        <td><span class="price-tag">Bosulif 500mg×30片美国上市价约12000美元/瓶(约合人民币85000元/月);土耳其版500mg×28片约2000+人民币/盒;瑞士/欧洲原厂版500mg×28片约20000+人民币/盒(因品牌溢价、汇率波动);原研药价格高昂,需经合规医疗资源咨询渠道获得</span><br><span class="text-xs text-gray-500">原研药参考价</span></td>
                    </tr>
                    <tr>
                        <td>海外经济版</td>
                        <td>Bosuvi (Intas) / Bonitar (Sun Pharma) / Bosutris (印度多家) 等</td>
                        <td>印度</td>
                        <td><span class="price-tag">Bosuvi(Intas)500mg×30片印度市场零售价约6000-7500印度卢比(约合人民币500-650元/月);Bonitar(Sun Pharma)400mg×10片约2269印度卢比(约合人民币190元/盒),500mg×10片约3000+印度卢比(约合人民币250+/盒);多家印度仿制版经济性显著优于原研药(约原研1/100至1/200),需经合规医疗资源咨询渠道获得</span><br><span class="text-xs text-gray-500">经正规海外医疗资源咨询渠道</span></td>
                    </tr>
                </tbody>
            </table>
            <p id="price-reference" class="text-xs text-gray-400 mt-2" data-i18n="price_reference">* 价格仅供参考,实际价格以咨询为准</p>'''
}

# 140: 博舒替尼片 BONITAR (Sun Pharma) - 白血病
drug_bonitar = {
    "name": "博舒替尼片 BONITAR",
    "filename": "news-140-bonitar.html",
    "seo_title": "博舒替尼片BONITAR用法用量详解｜Sun Pharma印度版 100/400/500mg二代TKI Ph+CML口服靶向",
    "seo_desc": "博舒替尼片BONITAR(Bosutinib Tablets 100/400/500mg,Sun Pharma印度版)用法用量详解,Ph+慢性粒细胞白血病(CML)新诊断慢性期/加速期/急变期靶向治疗,原研Bosulif等效替代,海外白血病靶向药咨询,全球优质医疗资源",
    "seo_keywords": "博舒替尼片,BONITAR,Sun Pharma,Bosutinib,二代TKI,Ph+CML,慢性粒细胞白血病,白血病,口服靶向药,Bosulif,Bonitar",
    "subtitle": "Bosutinib Tablets 100/400/500mg (BONITAR, Sun Pharma) - 二代酪氨酸激酶抑制剂(TKI) | 品牌:Bosulif博舒替尼(Pfizer)",
    "content": '''<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品概述</h2>
            <div class="info-box">
                <p><strong>通用名称:</strong>博舒替尼 (Bosutinib)</p>
                <p><strong>英文名称:</strong>Bosutinib Tablets 100mg/400mg/500mg (BONITAR, Sun Pharma) - 2nd Gen Tyrosine Kinase Inhibitor (TKI)</p>
                <p><strong>品牌名称:</strong>原研药Bosulif博舒替尼(Pfizer辉瑞,2012年美国FDA批准),海外经济版BONITAR(Sun Pharma印度第一大制药企业)、Bosuvi(Intas)、Bosutris(印度多家)等</p>
                <p><strong>规格:</strong>100mg/片(10片/盒);400mg/片(10片/盒);500mg/片(10片/盒);带Sun Pharmaceutical字样压印</p>
                <p><strong>药物类型:</strong>第二代酪氨酸激酶抑制剂(TKI);针对BCR-ABL激酶的ATP竞争性抑制剂,同时抑制SRC家族激酶;Sun Pharma(印度第一大制药企业,全球第4大仿制药企业,业务遍及150+国家)BONITAR印度版,活性成分、剂型、规格、给药途径与原研Bosulif基本一致,经印度DCGI严格审查批准上市;为Ph+慢性粒细胞白血病患者提供经济可及的治疗选择</p>
            </div>
            <h2><i class="fas fa-briefcase-medical mr-2 text-orange-500"></i>适应症</h2>
            <p>博舒替尼片 BONITAR适用于以下情况:</p>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>主要适应症-新诊断慢性期Ph+ CML:</strong>用于治疗成人新诊断的费城染色体阳性慢性粒细胞白血病慢性期(Ph+ CML-CP)患者</li>
                <li><strong>主要适应症-耐药或不耐受Ph+ CML:</strong>用于治疗既往接受过一种或多种TKI治疗失败或不耐受的成人Ph+ CML慢性期、加速期(AP)或急变期(BP)患者;当伊马替尼、尼洛替尼、达沙替尼不适合时考虑使用</li>
                <li><strong>儿科适应症:</strong>1岁及以上儿童慢性期Ph+ CML,新诊断者按BSA 300mg/m²/日;耐药/不耐受者按BSA 400mg/m²/日</li>
                <li><strong>用药前提:</strong>须由具有CML管理经验血液/肿瘤专科医生启动;用药前评估肝功能(ALT/AST/胆红素);基线胃肠道状态(腹泻管理);肾功能(老年/肾损者);注意与CYP3A抑制剂/诱导剂相互作用</li>
            </ul>
            <h2><i class="fas fa-cogs mr-2 text-orange-500"></i>作用机制</h2>
            <p>博舒替尼是强效第二代酪氨酸激酶抑制剂,能同时抑制BCR-ABL融合蛋白和SRC家族激酶(LYN/HCK)的活性;通过竞争性结合BCR-ABL的ATP结合位点,阻断酪氨酸残基磷酸化,抑制白血病细胞增殖信号传导;对野生型BCR-ABL及多数耐药突变(M244V、G250E、Q252H、E255K/V、F317L、F359V等)均有活性,但T315I和V299L突变耐药;口服后吸收迅速,4-6小时达峰;餐时服用生物利用度增加约2倍;血浆蛋白结合率约94%;主要经CYP3A4代谢,半衰期约22小时;约91%经粪便、3%经尿排泄;Sun Pharma(印度第一大制药企业)BONITAR印度版与原研Bosulif在活性成分、剂型、规格、给药途径上完全一致,经印度DCGI严格审查批准上市</p>
            <h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
            <h3>标准剂量</h3>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>成人新诊断CP Ph+ CML:</strong>推荐400mg/次,口服,每日1次,餐时服用;持续治疗直至疾病进展或不可耐受</li>
                <li><strong>成人CP/AP/BP Ph+ CML R/I患者:</strong>推荐500mg/次,口服,每日1次,餐时服用;持续治疗直至疾病进展或不可耐受</li>
                <li><strong>剂量递增:</strong>成人新诊断CP患者:3个月时若BCR-ABL转录本>10%且无3级以上不良反应,可每2周递增100mg至最大600mg/日;成人R/I患者:疗效不满意且无3-4级AE,可递增100mg至最大600mg/日</li>
            </ul>
            <h3>服药方式</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>整片吞服,不可咀嚼/压碎/掰开/切割;不可接触破损药片(活性成分可能引起皮肤刺激);建议固定每日同一时间餐时服用;若漏服超过12小时,跳过本次,次日常规剂量服用,切勿双倍补服</li>
                <li>服药期间避免葡萄柚/西柚制品(升高血药浓度);避免阳光直射/UV照射(增加光敏反应风险,使用防晒霜)</li>
            </ul>
            <h3>特殊人群剂量调整</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>老年人(≥65岁):无需初始剂量调整,但应密切监测肝肾毒性</li>
                <li>肝功能不全:轻度(Child-Pugh A):无需调整;中度(B):200mg/日;重度(C):100mg/日;肝酶>5×ULN:暂停至恢复至≤2.5×ULN后减量100mg/日恢复</li>
                <li>肾功能不全:CrCl>50mL/min:无需调整;CrCl 30-50mL/min:400mg/日;CrCl<30mL/min:300mg/日</li>
                <li>儿童(≥1岁):按BSA计算,新诊断300mg/m²/日;R/I 400mg/m²/日;最大不超过500mg/日</li>
            </ul>
            <h2><i class="fas fa-heartbeat mr-2 text-orange-500"></i>监测要求</h2>
            <div class="info-box">
                <p>用药前:肝功能(ALT/AST/胆红素)、肾功能、血常规、BCR-ABL定量、心电图(基础QTc);用药期间:第1个月每周1次血常规,之后每月;前3个月每月1次肝功能,之后按需;腹泻监测(分级管理);每3个月BCR-ABL定量评估分子学反应;出现胸闷、呼吸困难、水肿等立即评估心脏功能</p>
            </div>
            <h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>注意事项</h2>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>常见不良反应:</strong>极常见(≥20%):腹泻(80%+)、恶心、呕吐、腹痛、皮疹、疲乏、发热、肝酶升高;常见(10-20%):血小板减少、贫血、中性粒细胞减少、头痛、关节痛、呼吸困难、咳嗽、水肿</li>
                <li><strong>重要警告:</strong>①胃肠道毒性:80%以上患者出现腹泻(3-4级约8-9%),需预防性止泻、补液、调整剂量;②骨髓抑制:血小板减少/贫血/中性粒细胞减少,定期监测血常规;③肝毒性:前3个月每月监测肝功能;④心脏毒性:充血性心衰/心律失常/心包炎/心肌梗死(<1%但严重);⑤体液潴留:胸腔/心包积液、肺水肿、外周水肿</li>
                <li><strong>禁忌:</strong>对本品过敏者;严重肝功能不全未调整剂量者</li>
                <li><strong>特殊人群:</strong>孕妇:有胎儿毒性,使用需严格权衡利弊(育龄期用药需避孕至停药后1个月);哺乳期:不建议使用;儿童:1岁以下不推荐</li>
                <li><strong>药物相互作用:</strong>强CYP3A抑制剂(酮康唑、伊曲康唑、伏立康唑、克拉霉素、利托那韦等)显著升高血药浓度,需避免合用或密切监测;强CYP3A诱导剂(利福平、卡马西平、苯妥英、圣约翰草)显著降低血药浓度,需避免合用;质子泵抑制剂(PPI)可能降低吸收(避免同服或换用H2受体拮抗剂);葡萄柚/西柚制品增加血药浓度,需避免</li>
            </ul>
            <h2 id="price-title"><i class="fas fa-tags mr-2 text-orange-500"></i>原研药 vs 仿制药价格对比</h2>
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
                        <td>Bosulif 博舒替尼 (Pfizer)</td>
                        <td>美国/全球100+国家(2012年FDA;2013年EMA;中国未上市)</td>
                        <td><span class="price-tag">Bosulif 500mg×30片美国上市价约12000美元/瓶(约合人民币85000元/月);土耳其版500mg×28片约2000+人民币/盒;瑞士/欧洲原厂版500mg×28片约20000+人民币/盒(因品牌溢价、汇率波动);原研药价格高昂,需经合规医疗资源咨询渠道获得</span><br><span class="text-xs text-gray-500">原研药参考价</span></td>
                    </tr>
                    <tr>
                        <td>海外经济版</td>
                        <td>BONITAR (Sun Pharma) / Bosuvi (Intas) / Bosutris (印度多家) 等</td>
                        <td>印度</td>
                        <td><span class="price-tag">BONITAR(Sun Pharma)100mg×10片印度市场零售价约690印度卢比(约合人民币58元/盒);400mg×10片约2269印度卢比(约合人民币190元/盒);500mg×10片约3000+印度卢比(约合人民币250+/盒);多家印度仿制版经济性显著优于原研药(约原研1/100至1/200),需经合规医疗资源咨询渠道获得</span><br><span class="text-xs text-gray-500">经正规海外医疗资源咨询渠道</span></td>
                    </tr>
                </tbody>
            </table>
            <p id="price-reference" class="text-xs text-gray-400 mt-2" data-i18n="price_reference">* 价格仅供参考,实际价格以咨询为准</p>'''
}

# 141: 依普利酮片 EPLECARD (Intas)
drug_eplecard = {
    "name": "依普利酮片 EPLECARD",
    "filename": "news-141-eplecard.html",
    "seo_title": "依普利酮片EPLECARD用法用量详解｜Intas印度版 25/50mg选择性醛固酮受体拮抗剂心衰高血压",
    "seo_desc": "依普利酮片EPLECARD(Eplerenone Tablets 25/50mg,Intas印度版)用法用量详解,急性心梗后充血性心衰治疗/原发性高血压,选择性醛固酮受体拮抗剂,原研Inspra等效替代,海外心衰用药咨询,全球优质医疗资源",
    "seo_keywords": "依普利酮片,EPLECARD,Intas,Eplerenone,选择性醛固酮受体拮抗剂,心衰,高血压,Inspra,醛固酮,保钾利尿剂",
    "subtitle": "Eplerenone Tablets 25mg/50mg (EPLECARD, Intas) - 选择性醛固酮受体拮抗剂 | 品牌:Inspra依普利酮(Viatris/Pfizer)",
    "content": '''<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品概述</h2>
            <div class="info-box">
                <p><strong>通用名称:</strong>依普利酮 (Eplerenone)</p>
                <p><strong>英文名称:</strong>Eplerenone Tablets 25mg/50mg (EPLECARD, Intas) - Selective Aldosterone Receptor Antagonist</p>
                <p><strong>品牌名称:</strong>原研药Inspra依普利酮(Viatris原辉瑞Upjohn,2002年美国FDA批准),海外经济版EPLECARD(Intas)、Eplerite(印度多家)、Eptus(Glenmark)、Exenta(Glenmark)等</p>
                <p><strong>规格:</strong>25mg/片(黄色,圆形,薄膜衣片);50mg/片(黄色,圆形,薄膜衣片)</p>
                <p><strong>药物类型:</strong>选择性醛固酮受体拮抗剂(MRA);保钾利尿剂;通过选择性阻断盐皮质激素受体(与雄激素/孕激素/糖皮质激素受体亲和力极低),抑制醛固酮介导的钠水潴留和钾镁排泄,发挥降压、减轻心衰、抗心肌/血管纤维化作用;相比非选择性MRA螺内酯,男性乳房增生/性功能障碍等激素相关副作用显著降低;Intas(印度领先跨国仿制药企业)EPLECARD印度版,活性成分、剂型、规格、给药途径与原研Inspra基本一致,经印度DCGI严格审查批准上市</p>
            </div>
            <h2><i class="fas fa-briefcase-medical mr-2 text-orange-500"></i>适应症</h2>
            <p>依普利酮片 EPLECARD适用于以下情况:</p>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>主要适应症-急性心梗后充血性心衰:</strong>用于改善急性心肌梗死后左室射血分数降低(LVEF≤40%)的稳定心衰(HFrEF)患者的生存率;需在标准治疗(ACEI/ARB+β受体阻滞剂)基础上加用</li>
                <li><strong>主要适应症-原发性高血压:</strong>用于治疗原发性高血压,可单独使用或与其他抗高血压药物(如ACEI/ARB、CCB、利尿剂)联合应用</li>
                <li><strong>临床优势(对比螺内酯):</strong>对盐皮质激素受体选择性高100-1000倍,几乎无抗雄激素/孕激素副作用,男性乳房增生/性功能障碍/月经紊乱发生率显著降低;患者依从性更好</li>
                <li><strong>用药前提:</strong>用药前必须检测血钾(排除>5.0mmol/L者)和血肌酐(估算肾小球滤过率eGFR);血钾>5.0mmol/L、严重肾功能不全(eGFR<30)、合用强CYP3A4抑制剂者禁用</li>
            </ul>
            <h2><i class="fas fa-cogs mr-2 text-orange-500"></i>作用机制</h2>
            <p>依普利酮是9,11-环氧甾烷类衍生物,选择性结合盐皮质激素受体(MR),阻断醛固酮介导的钠水潴留和钾排泄;通过抑制醛固酮-心肌/血管/肾脏MR结合,减少胶原沉积和纤维化,改善心室重构,降低心衰患者死亡率(EPHESUS研究证实);口服吸收良好,1.5小时达峰;食物不影响吸收;血浆蛋白结合率约50%;主要经CYP3A4代谢为无活性代谢物;半衰期4-6小时;约67%经粪便、32%经尿排泄;选择性高(对雄激素/孕激素/糖皮质激素受体亲和力低),激素相关副作用少;Intas(印度领先跨国仿制药企业)EPLECARD印度版与原研Inspra在活性成分、剂型、规格、给药途径上完全一致,经印度DCGI严格审查批准上市</p>
            <h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
            <h3>标准剂量</h3>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>急性心梗后充血性心衰(HFrEF):</strong>起始25mg/次,口服,每日1次;在4周内根据患者耐受情况逐渐增加至目标剂量50mg/日;需在标准治疗(ACEI/ARB+β受体阻滞剂)基础上加用</li>
                <li><strong>原发性高血压:</strong>起始50mg/次,口服,每日1次;4周内降压效果不显著可增加至50mg/次,每日2次(最大100mg/日);可单独使用或与其他降压药联合</li>
                <li><strong>服药时间:</strong>建议每日固定时间服用;建议早晨或下午4点前服用(避免夜尿影响睡眠)</li>
            </ul>
            <h3>服药方式</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>整片吞服,可餐时或空腹服用(食物对吸收影响小);不可咀嚼/压碎/掰开;建议每日同一时间服药;漏服处理:如想起尽快补服,如接近下次服药时间则跳过,不可双倍补服</li>
                <li>服药期间建议低钾饮食,避免高钾食物(香蕉/橙子/牛油果/番茄/豆类等)过量摄入;避免葡萄柚/西柚制品</li>
            </ul>
            <h3>特殊人群剂量调整</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>老年人(≥75岁):无需调整起始剂量,但应密切监测血钾</li>
                <li>肾功能不全:eGFR≥50mL/min:无需调整;eGFR 30-49:无需调整但需监测;eGFR<30:25mg隔日1次起始,最大25mg/日;透析者:不推荐</li>
                <li>肝功能不全:轻中度无需调整;重度不推荐</li>
                <li>与中度CYP3A4抑制剂(红霉素/氟康唑/维拉帕米/地尔硫卓)合用:起始25mg/日,最大25mg/日</li>
                <li>儿童:<18岁安全有效性未确立,不推荐</li>
            </ul>
            <h2><i class="fas fa-heartbeat mr-2 text-orange-500"></i>监测要求</h2>
            <div class="info-box">
                <p>用药前:血钾(必须<5.0mmol/L)、血肌酐/eGFR、肝功能;用药期间:起始/调整剂量后第1周、第4周、之后每3个月监测血钾(尤其肾损/老年/合用ACEI/ARB者);血钾>5.5mmol/L减量或停药;血钾>6.0mmol/L立即停药;血压、心率、体重;心衰症状和体征</p>
            </div>
            <h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>注意事项</h2>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>常见不良反应:</strong>常见(≥5%):高钾血症(尤其肾损/糖尿病/合用ACEI者)、腹泻、恶心、咳嗽、头晕、疲乏、血肌酐升高;少见:男性乳房增生(显著低于螺内酯)、低血压、头痛、流感样症状</li>
                <li><strong>重要警告:</strong>①高钾血症风险:可致命,用药前/中必须严格监测血钾,尤其老年/糖尿病/肾损/合用ACEI/ARB/补钾者;②肝毒性:转氨酶升高罕见但需注意;③低血压:剂量调整/体位性低血压需关注</li>
                <li><strong>禁忌:</strong>血钾>5.0mmol/L(基线);eGFR<30mL/min的严重肾功能不全;严重肝功能不全(Child-Pugh C);合用强效CYP3A4抑制剂(酮康唑、伊曲康唑、克拉霉素、利托那韦等);对本品过敏者</li>
                <li><strong>特殊人群:</strong>孕妇:仅利大于弊时使用;哺乳期:治疗期间及最后剂量后1周内避免哺乳;老年:密切监测血钾</li>
                <li><strong>药物相互作用:</strong>禁与强CYP3A4抑制剂(酮康唑/伊曲康唑/克拉霉素/利托那韦等)合用;慎与中度CYP3A4抑制剂(红霉素/氟康唑/维拉帕米)合用(减量至25mg);ACEI/ARB/补钾剂/保钾利尿剂增加高钾血症风险(密切监测);NSAIDs减少降压效果并增加肾损伤风险;锂剂血药浓度可能升高(监测);圣约翰草/利福平降低血药浓度</li>
            </ul>
            <h2 id="price-title"><i class="fas fa-tags mr-2 text-orange-500"></i>原研药 vs 仿制药价格对比</h2>
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
                        <td>Inspra 依普利酮 (Viatris/原辉瑞Upjohn)</td>
                        <td>美国/全球多个国家(2002年FDA;中国未上市)</td>
                        <td><span class="price-tag">Inspra 50mg×30片美国上市价约120-150美元/瓶(约合人民币850-1050元/月);50mg×100片美国约300-500美元/瓶;Inspra因选择性更高副作用更少,价格显著高于非选择性MRA螺内酯;原研药价格较高,需经合规医疗资源咨询渠道获得</span><br><span class="text-xs text-gray-500">原研药参考价</span></td>
                    </tr>
                    <tr>
                        <td>海外经济版</td>
                        <td>EPLECARD (Intas) / Eplerite (印度多家) / Eptus (Glenmark) / Exenta (Glenmark) 等</td>
                        <td>印度</td>
                        <td><span class="price-tag">EPLECARD(Intas)50mg×30片印度市场零售价约300-450印度卢比(约合人民币25-38元/月);多家印度仿制版经济性显著优于原研药(约原研1/20至1/30),需经合规医疗资源咨询渠道获得</span><br><span class="text-xs text-gray-500">经正规海外医疗资源咨询渠道</span></td>
                    </tr>
                </tbody>
            </table>
            <p id="price-reference" class="text-xs text-gray-400 mt-2" data-i18n="price_reference">* 价格仅供参考,实际价格以咨询为准</p>'''
}

# 142: 依普利酮片 EPTUS (Natco) - 注：按药品列表中归Natco
drug_eptus = {
    "name": "依普利酮片 EPTUS",
    "filename": "news-142-eptus.html",
    "seo_title": "依普利酮片EPTUS用法用量详解｜Natco印度版 25/50mg选择性醛固酮受体拮抗剂心衰高血压",
    "seo_desc": "依普利酮片EPTUS(Eplerenone Tablets 25/50mg,Natco印度版)用法用量详解,急性心梗后充血性心衰治疗/原发性高血压,选择性醛固酮受体拮抗剂,原研Inspra等效替代,海外心衰用药咨询,全球优质医疗资源",
    "seo_keywords": "依普利酮片,EPTUS,Natco,Eplerenone,选择性醛固酮受体拮抗剂,心衰,高血压,Inspra,醛固酮,保钾利尿剂",
    "subtitle": "Eplerenone Tablets 25mg/50mg (EPTUS, Natco) - 选择性醛固酮受体拮抗剂 | 品牌:Inspra依普利酮(Viatris/Pfizer)",
    "content": '''<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品概述</h2>
            <div class="info-box">
                <p><strong>通用名称:</strong>依普利酮 (Eplerenone)</p>
                <p><strong>英文名称:</strong>Eplerenone Tablets 25mg/50mg (EPTUS, Natco) - Selective Aldosterone Receptor Antagonist</p>
                <p><strong>品牌名称:</strong>原研药Inspra依普利酮(Viatris原辉瑞Upjohn,2002年美国FDA批准),海外经济版EPTUS(Natco印度知名仿制药企业)、EPLECARD(Intas)、Eplerite(印度多家)、Exenta(Glenmark)等</p>
                <p><strong>规格:</strong>25mg/片(白色至类白色,圆形,薄膜衣片);50mg/片(白色至类白色,圆形,薄膜衣片)</p>
                <p><strong>药物类型:</strong>选择性醛固酮受体拮抗剂(MRA);保钾利尿剂;通过选择性阻断盐皮质激素受体(与雄激素/孕激素/糖皮质激素受体亲和力极低),抑制醛固酮介导的钠水潴留和钾镁排泄,发挥降压、减轻心衰、抗心肌/血管纤维化作用;相比非选择性MRA螺内酯,男性乳房增生/性功能障碍等激素相关副作用显著降低;Natco(印度知名仿制药企业,以抗病毒/抗肿瘤/心血管仿制领域见长)EPTUS印度版,活性成分、剂型、规格、给药途径与原研Inspra基本一致,经印度DCGI严格审查批准上市</p>
            </div>
            <h2><i class="fas fa-briefcase-medical mr-2 text-orange-500"></i>适应症</h2>
            <p>依普利酮片 EPTUS适用于以下情况:</p>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>主要适应症-急性心梗后充血性心衰:</strong>用于改善急性心肌梗死后左室射血分数降低(LVEF≤40%)的稳定心衰(HFrEF)患者的生存率;需在标准治疗(ACEI/ARB+β受体阻滞剂)基础上加用</li>
                <li><strong>主要适应症-原发性高血压:</strong>用于治疗原发性高血压,可单独使用或与其他抗高血压药物(如ACEI/ARB、CCB、利尿剂)联合应用</li>
                <li><strong>临床优势(对比螺内酯):</strong>对盐皮质激素受体选择性高100-1000倍,几乎无抗雄激素/孕激素副作用,男性乳房增生/性功能障碍/月经紊乱发生率显著降低;患者依从性更好</li>
                <li><strong>用药前提:</strong>用药前必须检测血钾(排除>5.0mmol/L者)和血肌酐(估算肾小球滤过率eGFR);血钾>5.0mmol/L、严重肾功能不全(eGFR<30)、合用强CYP3A4抑制剂者禁用</li>
            </ul>
            <h2><i class="fas fa-cogs mr-2 text-orange-500"></i>作用机制</h2>
            <p>依普利酮是9,11-环氧甾烷类衍生物,选择性结合盐皮质激素受体(MR),阻断醛固酮介导的钠水潴留和钾排泄;通过抑制醛固酮-心肌/血管/肾脏MR结合,减少胶原沉积和纤维化,改善心室重构,降低心衰患者死亡率(EPHESUS研究证实);口服吸收良好,1.5小时达峰;食物不影响吸收;血浆蛋白结合率约50%;主要经CYP3A4代谢为无活性代谢物;半衰期4-6小时;约67%经粪便、32%经尿排泄;选择性高(对雄激素/孕激素/糖皮质激素受体亲和力低),激素相关副作用少;Natco(印度知名仿制药企业,以抗病毒/抗肿瘤/心血管仿制领域见长)EPTUS印度版与原研Inspra在活性成分、剂型、规格、给药途径上完全一致,经印度DCGI严格审查批准上市</p>
            <h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
            <h3>标准剂量</h3>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>急性心梗后充血性心衰(HFrEF):</strong>起始25mg/次,口服,每日1次;在4周内根据患者耐受情况逐渐增加至目标剂量50mg/日;需在标准治疗(ACEI/ARB+β受体阻滞剂)基础上加用</li>
                <li><strong>原发性高血压:</strong>起始50mg/次,口服,每日1次;4周内降压效果不显著可增加至50mg/次,每日2次(最大100mg/日);可单独使用或与其他降压药联合</li>
                <li><strong>服药时间:</strong>建议每日固定时间服用;建议早晨或下午4点前服用(避免夜尿影响睡眠)</li>
            </ul>
            <h3>服药方式</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>整片吞服,可餐时或空腹服用(食物对吸收影响小);不可咀嚼/压碎/掰开;建议每日同一时间服药;漏服处理:如想起尽快补服,如接近下次服药时间则跳过,不可双倍补服</li>
                <li>服药期间建议低钾饮食,避免高钾食物(香蕉/橙子/牛油果/番茄/豆类等)过量摄入;避免葡萄柚/西柚制品</li>
            </ul>
            <h3>特殊人群剂量调整</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>老年人(≥75岁):无需调整起始剂量,但应密切监测血钾</li>
                <li>肾功能不全:eGFR≥50mL/min:无需调整;eGFR 30-49:无需调整但需监测;eGFR<30:25mg隔日1次起始,最大25mg/日;透析者:不推荐</li>
                <li>肝功能不全:轻中度无需调整;重度不推荐</li>
                <li>与中度CYP3A4抑制剂(红霉素/氟康唑/维拉帕米/地尔硫卓)合用:起始25mg/日,最大25mg/日</li>
                <li>儿童:<18岁安全有效性未确立,不推荐</li>
            </ul>
            <h2><i class="fas fa-heartbeat mr-2 text-orange-500"></i>监测要求</h2>
            <div class="info-box">
                <p>用药前:血钾(必须<5.0mmol/L)、血肌酐/eGFR、肝功能;用药期间:起始/调整剂量后第1周、第4周、之后每3个月监测血钾(尤其肾损/老年/合用ACEI/ARB者);血钾>5.5mmol/L减量或停药;血钾>6.0mmol/L立即停药;血压、心率、体重;心衰症状和体征</p>
            </div>
            <h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>注意事项</h2>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>常见不良反应:</strong>常见(≥5%):高钾血症(尤其肾损/糖尿病/合用ACEI者)、腹泻、恶心、咳嗽、头晕、疲乏、血肌酐升高;少见:男性乳房增生(显著低于螺内酯)、低血压、头痛、流感样症状</li>
                <li><strong>重要警告:</strong>①高钾血症风险:可致命,用药前/中必须严格监测血钾,尤其老年/糖尿病/肾损/合用ACEI/ARB/补钾者;②肝毒性:转氨酶升高罕见但需注意;③低血压:剂量调整/体位性低血压需关注</li>
                <li><strong>禁忌:</strong>血钾>5.0mmol/L(基线);eGFR<30mL/min的严重肾功能不全;严重肝功能不全(Child-Pugh C);合用强效CYP3A4抑制剂(酮康唑、伊曲康唑、克拉霉素、利托那韦等);对本品过敏者</li>
                <li><strong>特殊人群:</strong>孕妇:仅利大于弊时使用;哺乳期:治疗期间及最后剂量后1周内避免哺乳;老年:密切监测血钾</li>
                <li><strong>药物相互作用:</strong>禁与强CYP3A4抑制剂(酮康唑/伊曲康唑/克拉霉素/利托那韦等)合用;慎与中度CYP3A4抑制剂(红霉素/氟康唑/维拉帕米)合用(减量至25mg);ACEI/ARB/补钾剂/保钾利尿剂增加高钾血症风险(密切监测);NSAIDs减少降压效果并增加肾损伤风险;锂剂血药浓度可能升高(监测);圣约翰草/利福平降低血药浓度</li>
            </ul>
            <h2 id="price-title"><i class="fas fa-tags mr-2 text-orange-500"></i>原研药 vs 仿制药价格对比</h2>
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
                        <td>Inspra 依普利酮 (Viatris/原辉瑞Upjohn)</td>
                        <td>美国/全球多个国家(2002年FDA;中国未上市)</td>
                        <td><span class="price-tag">Inspra 50mg×30片美国上市价约120-150美元/瓶(约合人民币850-1050元/月);50mg×100片美国约300-500美元/瓶;Inspra因选择性更高副作用更少,价格显著高于非选择性MRA螺内酯;原研药价格较高,需经合规医疗资源咨询渠道获得</span><br><span class="text-xs text-gray-500">原研药参考价</span></td>
                    </tr>
                    <tr>
                        <td>海外经济版</td>
                        <td>EPTUS (Natco) / EPLECARD (Intas) / Eplerite (印度多家) / Exenta (Glenmark) 等</td>
                        <td>印度</td>
                        <td><span class="price-tag">EPTUS(Natco)50mg×30片印度市场零售价约300-450印度卢比(约合人民币25-38元/月);多家印度仿制版经济性显著优于原研药(约原研1/20至1/30),需经合规医疗资源咨询渠道获得</span><br><span class="text-xs text-gray-500">经正规海外医疗资源咨询渠道</span></td>
                    </tr>
                </tbody>
            </table>
            <p id="price-reference" class="text-xs text-gray-400 mt-2" data-i18n="price_reference">* 价格仅供参考,实际价格以咨询为准</p>'''
}

# 143: 依普利酮片 EXENTA (Glenmark)
drug_exenta = {
    "name": "依普利酮片 EXENTA",
    "filename": "news-143-exenta.html",
    "seo_title": "依普利酮片EXENTA用法用量详解｜Glenmark印度版 25mg选择性醛固酮受体拮抗剂心衰高血压",
    "seo_desc": "依普利酮片EXENTA(Eplerenone Tablets 25mg,Glenmark印度版)用法用量详解,急性心梗后充血性心衰治疗/原发性高血压,选择性醛固酮受体拮抗剂,原研Inspra等效替代,海外心衰用药咨询,全球优质医疗资源",
    "seo_keywords": "依普利酮片,EXENTA,Glenmark,Eplerenone,选择性醛固酮受体拮抗剂,心衰,高血压,Inspra,醛固酮,保钾利尿剂",
    "subtitle": "Eplerenone Tablets 25mg (EXENTA, Glenmark) - 选择性醛固酮受体拮抗剂 | 品牌:Inspra依普利酮(Viatris/Pfizer)",
    "content": '''<h2><i class="fas fa-info-circle mr-2 text-orange-500"></i>药品概述</h2>
            <div class="info-box">
                <p><strong>通用名称:</strong>依普利酮 (Eplerenone)</p>
                <p><strong>英文名称:</strong>Eplerenone Tablets 25mg (EXENTA, Glenmark) - Selective Aldosterone Receptor Antagonist</p>
                <p><strong>品牌名称:</strong>原研药Inspra依普利酮(Viatris原辉瑞Upjohn,2002年美国FDA批准),海外经济版EXENTA(Glenmark印度知名仿制药企业)、EPTUS(Glenmark)、EPLECARD(Intas)、Eplerite(印度多家)等</p>
                <p><strong>规格:</strong>25mg/片(白色,圆形,薄膜衣片);Glenmark另有25/50/100mg多规格版本</p>
                <p><strong>药物类型:</strong>选择性醛固酮受体拮抗剂(MRA);保钾利尿剂;通过选择性阻断盐皮质激素受体(与雄激素/孕激素/糖皮质激素受体亲和力极低),抑制醛固酮介导的钠水潴留和钾镁排泄,发挥降压、减轻心衰、抗心肌/血管纤维化作用;相比非选择性MRA螺内酯,男性乳房增生/性功能障碍等激素相关副作用显著降低;Glenmark(印度知名跨国仿制药企业,在心血管/糖尿病/皮肤科仿制领域有重要地位)EXENTA印度版,活性成分、剂型、规格、给药途径与原研Inspra基本一致,经印度DCGI严格审查批准上市</p>
            </div>
            <h2><i class="fas fa-briefcase-medical mr-2 text-orange-500"></i>适应症</h2>
            <p>依普利酮片 EXENTA适用于以下情况:</p>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>主要适应症-急性心梗后充血性心衰:</strong>用于改善急性心肌梗死后左室射血分数降低(LVEF≤40%)的稳定心衰(HFrEF)患者的生存率;需在标准治疗(ACEI/ARB+β受体阻滞剂)基础上加用</li>
                <li><strong>主要适应症-原发性高血压:</strong>用于治疗原发性高血压,可单独使用或与其他抗高血压药物(如ACEI/ARB、CCB、利尿剂)联合应用</li>
                <li><strong>临床优势(对比螺内酯):</strong>对盐皮质激素受体选择性高100-1000倍,几乎无抗雄激素/孕激素副作用,男性乳房增生/性功能障碍/月经紊乱发生率显著降低;患者依从性更好</li>
                <li><strong>用药前提:</strong>用药前必须检测血钾(排除>5.0mmol/L者)和血肌酐(估算肾小球滤过率eGFR);血钾>5.0mmol/L、严重肾功能不全(eGFR<30)、合用强CYP3A4抑制剂者禁用</li>
            </ul>
            <h2><i class="fas fa-cogs mr-2 text-orange-500"></i>作用机制</h2>
            <p>依普利酮是9,11-环氧甾烷类衍生物,选择性结合盐皮质激素受体(MR),阻断醛固酮介导的钠水潴留和钾排泄;通过抑制醛固酮-心肌/血管/肾脏MR结合,减少胶原沉积和纤维化,改善心室重构,降低心衰患者死亡率(EPHESUS研究证实);口服吸收良好,1.5小时达峰;食物不影响吸收;血浆蛋白结合率约50%;主要经CYP3A4代谢为无活性代谢物;半衰期4-6小时;约67%经粪便、32%经尿排泄;选择性高(对雄激素/孕激素/糖皮质激素受体亲和力低),激素相关副作用少;Glenmark(印度知名跨国仿制药企业,在心血管/糖尿病/皮肤科仿制领域有重要地位)EXENTA印度版与原研Inspra在活性成分、剂型、规格、给药途径上完全一致,经印度DCGI严格审查批准上市</p>
            <h2><i class="fas fa-pills mr-2 text-orange-500"></i>用法用量</h2>
            <h3>标准剂量</h3>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>急性心梗后充血性心衰(HFrEF):</strong>起始25mg/次,口服,每日1次;在4周内根据患者耐受情况逐渐增加至目标剂量50mg/日;需在标准治疗(ACEI/ARB+β受体阻滞剂)基础上加用</li>
                <li><strong>原发性高血压:</strong>起始50mg/次,口服,每日1次;4周内降压效果不显著可增加至50mg/次,每日2次(最大100mg/日);可单独使用或与其他降压药联合</li>
                <li><strong>服药时间:</strong>建议每日固定时间服用;建议早晨或下午4点前服用(避免夜尿影响睡眠)</li>
            </ul>
            <h3>服药方式</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>整片吞服,可餐时或空腹服用(食物对吸收影响小);不可咀嚼/压碎/掰开;建议每日同一时间服药;漏服处理:如想起尽快补服,如接近下次服药时间则跳过,不可双倍补服</li>
                <li>服药期间建议低钾饮食,避免高钾食物(香蕉/橙子/牛油果/番茄/豆类等)过量摄入;避免葡萄柚/西柚制品</li>
            </ul>
            <h3>特殊人群剂量调整</h3>
            <ul class="list-disc list-inside space-y-2">
                <li>老年人(≥75岁):无需调整起始剂量,但应密切监测血钾</li>
                <li>肾功能不全:eGFR≥50mL/min:无需调整;eGFR 30-49:无需调整但需监测;eGFR<30:25mg隔日1次起始,最大25mg/日;透析者:不推荐</li>
                <li>肝功能不全:轻中度无需调整;重度不推荐</li>
                <li>与中度CYP3A4抑制剂(红霉素/氟康唑/维拉帕米/地尔硫卓)合用:起始25mg/日,最大25mg/日</li>
                <li>儿童:<18岁安全有效性未确立,不推荐</li>
            </ul>
            <h2><i class="fas fa-heartbeat mr-2 text-orange-500"></i>监测要求</h2>
            <div class="info-box">
                <p>用药前:血钾(必须<5.0mmol/L)、血肌酐/eGFR、肝功能;用药期间:起始/调整剂量后第1周、第4周、之后每3个月监测血钾(尤其肾损/老年/合用ACEI/ARB者);血钾>5.5mmol/L减量或停药;血钾>6.0mmol/L立即停药;血压、心率、体重;心衰症状和体征</p>
            </div>
            <h2><i class="fas fa-exclamation-triangle mr-2 text-orange-500"></i>注意事项</h2>
            <ul class="list-disc list-inside space-y-2">
                <li><strong>常见不良反应:</strong>常见(≥5%):高钾血症(尤其肾损/糖尿病/合用ACEI者)、腹泻、恶心、咳嗽、头晕、疲乏、血肌酐升高;少见:男性乳房增生(显著低于螺内酯)、低血压、头痛、流感样症状</li>
                <li><strong>重要警告:</strong>①高钾血症风险:可致命,用药前/中必须严格监测血钾,尤其老年/糖尿病/肾损/合用ACEI/ARB/补钾者;②肝毒性:转氨酶升高罕见但需注意;③低血压:剂量调整/体位性低血压需关注</li>
                <li><strong>禁忌:</strong>血钾>5.0mmol/L(基线);eGFR<30mL/min的严重肾功能不全;严重肝功能不全(Child-Pugh C);合用强效CYP3A4抑制剂(酮康唑、伊曲康唑、克拉霉素、利托那韦等);对本品过敏者</li>
                <li><strong>特殊人群:</strong>孕妇:仅利大于弊时使用;哺乳期:治疗期间及最后剂量后1周内避免哺乳;老年:密切监测血钾</li>
                <li><strong>药物相互作用:</strong>禁与强CYP3A4抑制剂(酮康唑/伊曲康唑/克拉霉素/利托那韦等)合用;慎与中度CYP3A4抑制剂(红霉素/氟康唑/维拉帕米)合用(减量至25mg);ACEI/ARB/补钾剂/保钾利尿剂增加高钾血症风险(密切监测);NSAIDs减少降压效果并增加肾损伤风险;锂剂血药浓度可能升高(监测);圣约翰草/利福平降低血药浓度</li>
            </ul>
            <h2 id="price-title"><i class="fas fa-tags mr-2 text-orange-500"></i>原研药 vs 仿制药价格对比</h2>
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
                        <td>Inspra 依普利酮 (Viatris/原辉瑞Upjohn)</td>
                        <td>美国/全球多个国家(2002年FDA;中国未上市)</td>
                        <td><span class="price-tag">Inspra 50mg×30片美国上市价约120-150美元/瓶(约合人民币850-1050元/月);50mg×100片美国约300-500美元/瓶;Inspra因选择性更高副作用更少,价格显著高于非选择性MRA螺内酯;原研药价格较高,需经合规医疗资源咨询渠道获得</span><br><span class="text-xs text-gray-500">原研药参考价</span></td>
                    </tr>
                    <tr>
                        <td>海外经济版</td>
                        <td>EXENTA (Glenmark) / EPTUS (Glenmark) / EPLECARD (Intas) / Eplerite (印度多家) 等</td>
                        <td>印度</td>
                        <td><span class="price-tag">EXENTA(Glenmark)25mg×15片印度市场零售价约675印度卢比(约合人民币57元/盒);多家印度仿制版经济性显著优于原研药(约原研1/20至1/30),需经合规医疗资源咨询渠道获得</span><br><span class="text-xs text-gray-500">经正规海外医疗资源咨询渠道</span></td>
                    </tr>
                </tbody>
            </table>
            <p id="price-reference" class="text-xs text-gray-400 mt-2" data-i18n="price_reference">* 价格仅供参考,实际价格以咨询为准</p>'''
}

# 写文件
drugs = [drug_bosuvi, drug_bonitar, drug_eplecard, drug_eptus, drug_exenta]
os.chdir("/app/data/所有对话/主对话/蓝培医疗文章")

for drug in drugs:
    html = build_html(drug)
    with open(drug['filename'], 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"生成: {drug['filename']} ({len(html)} 字符)")

print("\n所有5个HTML文件已生成完毕！")
