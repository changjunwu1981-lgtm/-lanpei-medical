#!/usr/bin/env python3
"""
基于 0617 article 的"新模板"，生成 0621 industry article
- 主题：CSCO 尿路上皮癌指南
- 使用 7 语言切换 + i18n
- 修正用词规范
- 推送到 GitHub
"""

import os
import re
import shutil
import subprocess

WORK_DIR = "/app/data/所有对话/主对话/蓝培医疗文章"
TEMPLATE_FILE = f"{WORK_DIR}/2026-06-21/temp_industry_template_0617.html"
TARGET_DATE = "0621"
TARGET_SLUG = "csco-niaolu-shangpi-ai-2026"
TARGET_FILENAME = f"news-industry-{TARGET_DATE}-{TARGET_SLUG}.html"

# 0621 article 的标题、描述、关键词
TITLE_HTML = "2026版CSCO尿路上皮癌指南重磅更新：维迪西妥单抗+特瑞普利单抗&quot;免疫+ADC&quot;方案列为1A类证据，中国方案首次登顶NEJM"
DESCRIPTION = "2026年6月19日，2026 CSCO尿路上皮癌创新诊疗学术会议在京召开，宣布维迪西妥单抗联合特瑞普利单抗方案获CSCO尿路上皮癌诊疗指南1A类证据、一级优先推荐，覆盖82.6% HER2表达人群。RC48-C016研究NEJM发表数据：mPFS 13.1个月（vs化疗6.5个月）、mOS 31.5个月（vs化疗16.9个月）、ORR 76.1%，是中国泌尿肿瘤领域首个NEJM原创研究。"
KEYWORDS = "CSCO,尿路上皮癌,维迪西妥单抗,特瑞普利单抗,RC48-C016,NEJM,1A类证据,免疫+ADC,蓝培医疗"
PUBLISH_DATE = "2026年6月21日"
PUBLISH_SOURCE = "CSCO 2026 尿路上皮癌学术会议、北京大学肿瘤医院、《科技日报》、荣昌生物官方公告"

# 0621 article 的核心内容
ARTICLE_CONTENT = """                <p>2026年6月19日，<strong>2026中国临床肿瘤学会（CSCO）尿路上皮癌创新诊疗学术会议</strong>在北京召开。大会核心信息显示，<strong>新版《CSCO尿路上皮癌诊疗指南》正式将维迪西妥单抗联合特瑞普利单抗方案列为1A类证据、一级优先推荐</strong>，适用于转移性膀胱尿路上皮癌和上尿路尿路上皮癌一线治疗，无论患者是否可耐受顺铂。这一"中国方案"的诞生，依托于<strong>北京大学肿瘤医院郭军教授牵头的RC48-C016 III期研究</strong>——其结果于2025年10月19日全文发表于<strong>《新英格兰医学杂志》（NEJM，影响因子78.5）</strong>，同步在2025年ESMO年会主席论坛口头报告，是中国泌尿肿瘤领域首篇NEJM原创研究。这标志着中国尿路上皮癌诊疗领域完成从"跟跑"到"领跑"的跨越，<strong>首个获批上市的国产"免疫+ADC"创新联合疗法</strong>正式落地临床。</p>

                <!-- 数据卡片 -->
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4 my-6">
                    <div class="data-card">
                        <div class="number text-orange-500">13.1月</div>
                        <div class="label">mPFS（vs 化疗6.5月）</div>
                    </div>
                    <div class="data-card">
                        <div class="number text-orange-500">31.5月</div>
                        <div class="label">mOS（vs 化疗16.9月）</div>
                    </div>
                    <div class="data-card">
                        <div class="number text-orange-500">76.1%</div>
                        <div class="label">客观缓解率 ORR</div>
                    </div>
                    <div class="data-card">
                        <div class="number text-orange-500">82.6%</div>
                        <div class="label">HER2表达人群覆盖</div>
                    </div>
                </div>

                <h2><i class="fas fa-lightbulb mr-2 text-orange-500"></i><span data-i18n="policy_summary">要点速览</span></h2>

                <h2><i class="fas fa-chart-line mr-2 text-orange-500"></i>1. 关键数据：mPFS 13.1个月、mOS 31.5个月、ORR 76.1%全面超越化疗</h2>
                <p>RC48-C016研究是一项在中国开展的开放标签、多中心、随机对照3期试验，对比维迪西妥单抗联合特瑞普利单抗与一线化疗方案（吉西他滨联合顺铂/卡铂）用于既往未接受系统治疗的<strong>HER2表达（IHC 1+/2+/3+）</strong>晚期尿路上皮癌患者。研究由北京大学肿瘤医院郭军教授担任主要研究者，周爱萍教授任共同主要研究者，在全国<strong>74家临床研究中心</strong>开展，<strong>共入组484例受试者</strong>。</p>
                <p>截至2025年3月31日的数据分析显示：</p>
                <ul>
                    <li><strong>中位PFS达13.1个月</strong>（vs 化疗组6.5个月），<strong>疾病进展或死亡风险降低64%</strong>（HR=0.36，95%CI: 0.28–0.46，P&lt;0.0001）；</li>
                    <li><strong>中位OS达31.5个月</strong>（vs 化疗组16.9个月），<strong>死亡风险降低46%</strong>（HR=0.54，95%CI: 0.41–0.73，P&lt;0.0001）；</li>
                    <li><strong>客观缓解率（ORR）达76.1%</strong>（vs 化疗组50.2%），完全缓解率4.5%；</li>
                    <li><strong>疾病控制率（DCR）达91.4%</strong>（vs 化疗组77.6%）；</li>
                    <li>中位疗效持续时间<strong>14.6个月</strong>，远超含铂化疗组的5.6个月；</li>
                    <li>≥3级治疗相关不良事件仅<strong>55.1%</strong>，显著低于化疗组的86.9%；摆脱了传统化疗严重的骨髓抑制毒性。</li>
                </ul>
                <p>亚组分析显示，无论患者HER2表达水平（IHC 1+至3+）、顺铂耐受状态或肿瘤部位（上/下尿路），生存获益均保持一致——这意味着该方案覆盖了<strong>约82.6%的HER2表达患者人群</strong>，不受HER2表达水平高低或顺铂耐受状态影响，实现了广泛人群的精准获益。</p>

                <div class="info-box">
                    <strong>NEJM背书与"中国首创"</strong>：RC48-C016是中国泌尿肿瘤领域首篇NEJM原创研究。NEJM副主编、北京大学未来技术学院创始院长肖瑞平教授现场评价："C016研究是中国临床研究从量变到质变的标志性成果，十余年来中国临床研究质量与数量同步提升，该项研究以扎实的循证证据、明确的临床价值赢得了国际学术界的高度认可。"更值得自豪的是，这一"免疫+ADC"联合方案中的<strong>两款药物均为中国原研</strong>——维迪西妥单抗来自荣昌生物，特瑞普利单抗来自君实生物，2026年5月21日NMPA正式批准其HER2表达局部晚期或转移性尿路上皮癌一线治疗适应症（特瑞普利单抗第13项适应症）。
                </div>

                <h2><i class="fas fa-stethoscope mr-2 text-orange-500"></i>2. 指南升级：从"化疗为王"到"免化疗精准联合"的时代转折</h2>
                <p>尿路上皮癌是泌尿系统最常见的恶性肿瘤之一，主要包括膀胱癌、肾盂癌和输尿管癌。长期以来，以顺铂为基础的联合化疗是局部晚期或转移性尿路上皮癌一线治疗的"金标准"，这一模式主导临床<strong>近半个世纪</strong>。然而，传统化疗<strong>中位生存期仅约14-15个月</strong>，且血液学毒性、肾毒性等严重不良反应使大量患者——尤其是肾功能不全或体能状态较差者——无法耐受，临床需求长期未被满足。</p>
                <p>新版《CSCO尿路上皮癌诊疗指南》正式将维迪西妥单抗联合特瑞普利单抗方案列为<strong>1A类证据、一级优先推荐</strong>，标志着<strong>尿路上皮癌一线治疗正式从"化疗为王"进入"免化疗精准联合"的新时代</strong>。CSCO秘书长郭军教授指出："和传统化疗相比，该方案可以将患者的总生存、无进展生存、客观缓解率全部提升一倍，真正改变了中国晚期尿路上皮癌的治疗格局。"</p>
                <p>解放军总医院杨波教授在大会对比解读CSCO与NCCN尿路上皮癌指南差异时指出：相较于国际指南，<strong>CSCO指南更贴合中国临床实际</strong>，兼顾循证证据等级、专家共识与药物可及性，单独设置上尿路尿路上皮癌诊疗路径，在顺铂不耐受人群方案、本土创新药物推荐等方面更具本土化优势，临床可操作性更强。</p>

                <h2><i class="fas fa-globe mr-2 text-orange-500"></i>3. 国际验证：欧美人群数据"几乎一致"——中国方案可复制性获证</h2>
                <p>中国方案的全球价值，进一步得到国际研究的验证。2025年2月ASCO-GU大会公布的<strong>RC48-G001研究</strong>显示，维迪西妥单抗+特瑞普利单抗（DV+P）方案在<strong>欧美人群</strong>中取得与RC48-C016<strong>几乎一致</strong>的结果——这意味着中国研究的循证证据具有跨人群可复制性。郭军教授评价："这验证了中国研究和国创药物的可信性，是值得中国业界骄傲的成果。"</p>
                <p>从更宏观的视角看，RC48-C016研究的成功具有多重示范意义：</p>
                <ul>
                    <li><strong>从"跟跑"到"领跑"</strong>：中国在尿路上皮癌HER2精准治疗领域取得世界领先；</li>
                    <li><strong>"中国同创"模式成功</strong>：本土创新药企（荣昌+君实）联合本土研究者，共同研发出全球首创的联合方案；</li>
                    <li><strong>10年循证闭环</strong>：从2015年首项C系列研究启动，到逐步完成后线→一线、单药→联合的完整循证闭环；</li>
                    <li><strong>国际标准化建立</strong>：中国在全球率先建立尿路上皮癌专属HER2表达判读标准，被欧美人群研究重复验证；</li>
                    <li><strong>推动其他癌种探索</strong>：为胃癌、乳腺癌等其他HER2表达癌种探索类似联合策略提供关键依据。</li>
                </ul>

                <h2><i class="fas fa-coins mr-2 text-orange-500"></i>4. 药物经济学：15年周期内的"显著优势"</h2>
                <p>本次大会上，南京医科大学李歆教授现场发布的<strong>药物经济学评价</strong>显示：</p>
                <ul>
                    <li>维迪西妥单抗联合特瑞普利单抗方案<strong>15年周期内可显著提升患者健康生命年</strong>；</li>
                    <li>增量成本效果比<strong>低于中国人均GDP 3倍的支付阈值</strong>，符合医保准入的经济学标准；</li>
                    <li>若纳入患者生存期延长带来的社会劳动价值，仅<strong>5年即可显现显著的经济学优势</strong>；</li>
                    <li>方案有效率高、不良反应可控，能够减少患者反复住院、频繁更换方案，<strong>全周期综合成本效益优异</strong>。</li>
                </ul>
                <p>与会专家建议，<strong>应积极推动该方案纳入国家医保目录</strong>，同步加强基层医生教育与HER2检测能力建设，让这一中国方案真正惠及更广泛人群，助力"健康中国2030"肿瘤生存提升目标实现。</p>

                <h2><i class="fas fa-users mr-2 text-orange-500"></i>5. 对患者的影响：晚期尿路上皮癌治疗的"中国方案"已触手可及</h2>
                <p>对于<strong>每年新发9.29万例、死亡超4万例</strong>的中国尿路上皮癌患者而言，2026版CSCO指南更新+新适应症获批+医保谈判推进，意味着：</p>
                <ul>
                    <li><strong>一线治疗格局彻底改写</strong>：从"化疗为王"转向"免化疗精准联合"，生存期翻倍；</li>
                    <li><strong>82.6% HER2表达人群获益</strong>：覆盖绝大多数尿路上皮癌患者，不再受HER2表达水平限制；</li>
                    <li><strong>顺铂不耐受者迎来希望</strong>：约半数无法耐受传统化疗的患者，现在有了新选择；</li>
                    <li><strong>中国本土原研药</strong>：维迪西妥+特瑞普利均为国产1类创新药，预期价格友好，长期用药成本可控；</li>
                    <li><strong>"免化疗"生活质量</strong>：3级以上不良反应率从86.9%降至55.1%，治疗耐受性显著提升；</li>
                    <li><strong>医保准入加速期</strong>：2026年医保目录调整"预申报"机制下，该方案有望在2027年纳入医保。</li>
                </ul>

                <div class="warning-box">
                    <strong>用药提醒</strong>：维迪西妥单抗联合特瑞普利单抗方案为处方药，必须在具备肿瘤诊疗资质的医院、经泌尿/肿瘤内科医生评估后使用。用药前需完善<strong>HER2免疫组化检测（IHC 1+/2+/3+）</strong>、基线影像学评估（CT/MRI）、肝肾功能、心功能等基线状态。治疗期间需定期监测不良反应（特别是免疫相关不良反应，如免疫性肺炎、肝炎、甲状腺功能异常等）。HER2检测建议在有资质的病理科进行，避免假阴性或假阳性。如有治疗方案、用药可及性、医保政策等问题，请通过文末联系方式咨询蓝培医疗专业顾问。
                </div>

                <h2><i class="fas fa-road mr-2 text-orange-500"></i>6. 未来方向：从晚期到围手术期、保器官治疗的纵深拓展</h2>
                <p>CSCO副理事长姚欣教授表示，适应症获批是产学研医多方联动的成果，<strong>未来探索将向围手术期、保器官治疗等方向延伸</strong>。具体方向包括：</p>
                <ul>
                    <li><strong>围手术期治疗</strong>：探索维迪西妥单抗+特瑞普利单抗在肌层浸润性膀胱癌（MIBC）新辅助治疗、辅助治疗中的价值；</li>
                    <li><strong>保器官治疗</strong>：对部分膀胱癌患者，探索通过联合方案达到保留膀胱的可能性；</li>
                    <li><strong>联合方案拓展</strong>：探索与放疗、靶向治疗（如FGFR抑制剂）的联合应用；</li>
                    <li><strong>生物标志物精筛</strong>：通过ctDNA、HER2低表达/超低表达等更精细分层，进一步优化获益人群；</li>
                    <li><strong>海外拓展</strong>：基于RC48-C016和RC48-G001的跨人群一致性，该方案有望成为全球HER2表达尿路上皮癌一线治疗新标准。</li>
                </ul>

                <h2><i class="fas fa-handshake mr-2 text-orange-500"></i><span data-i18n="service_guide">蓝培视角</span></h2>

                <p>从蓝培医疗<strong>"全球优质医疗资源咨询平台"</strong>的定位出发，新版CSCO尿路上皮癌指南的发布与免疫+ADC联合方案的落地，带来三个值得关注的结构性变化：</p>

                <p><strong>第一，"中国同创"模式跑通后，更多国产创新药组合值得期待。</strong>荣昌+君实的联手证明：本土创新药企之间完全可以走通"联合研发-联合申报-联合推广"的全链路。这对于其他中国创新药企（如信达、康方、亚盛等）形成示范效应，未来"国产药+国产药"的联合方案在HER2、CLDN18.2、PD-1/PD-L1等多个靶点都有可能出现突破性进展。蓝培医疗持续跟踪中国创新药企动向，可为患者提供全球新药格局的最新解读。</p>

                <p><strong>第二，HER2检测能力建设是落地关键。</strong>新方案要求所有患者用药前完成HER2 IHC检测（覆盖82.6%人群），这意味着基层医院病理科的HER2检测能力将面临大规模升级需求。蓝培医疗可协助对接北京肿瘤医院郭军团队等顶级泌尿肿瘤专家资源，为基层患者提供第二诊疗意见及检测建议。</p>

                <p><strong>第三，全球HER2靶向药格局正在被"中国方案"重塑。</strong>在国际市场上，HER2-ADC赛道此前由第一三共DS-8201（德曲妥珠单抗）和罗氏Kadcyla主导。RC48-C016和RC48-G001两项研究的"跨人群一致性"，使中国原创ADC+免疫联合方案有望成为<strong>全球HER2表达尿路上皮癌一线治疗新标准</strong>。蓝培医疗对接全球肿瘤专家资源，可为有需要的患者提供跨境远程会诊及全球新药咨询渠道。</p>

                <p>如您或家人遇到尿路上皮癌（含膀胱癌、肾盂癌、输尿管癌）、胃癌、乳腺癌、肺癌等HER2表达肿瘤，需要了解全球抗癌药/ADC药物/HER2靶向药方案，或希望对接跨境医疗资源、获取第二诊疗意见，欢迎随时联系蓝培医疗。我们的全球医疗资源顾问团队将根据您的具体病情、所在地区、预算范围，<strong>提供合规、可执行的方案建议</strong>。</p>
"""


def main():
    # 1. 读取 0617 模板
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    # 2. 替换关键字段
    new_html = template
    # 替换 title
    new_html = re.sub(
        r'<title>.*?</title>',
        f'<title>{TITLE_HTML} - 蓝培医疗行业资讯</title>',
        new_html,
        count=1
    )
    # 替换 description
    new_html = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{DESCRIPTION}">',
        new_html,
        count=1
    )
    # 替换 keywords
    new_html = re.sub(
        r'<meta name="keywords" content=".*?">',
        f'<meta name="keywords" content="{KEYWORDS}">',
        new_html,
        count=1
    )

    # 替换面包屑
    new_html = re.sub(
        r'<a href="https://lanpeimed.com/news.html" data-i18n="news">新闻资讯</a> &gt; <span class="inline-block bg-orange-100 text-orange-700 px-2 py-0.5 rounded text-xs font-medium" data-i18n="tab_industry">行业资讯</span> &gt;.*?</div>',
        '<a href="https://lanpeimed.com/news.html" data-i18n="news">新闻资讯</a> &gt; <span class="inline-block bg-orange-100 text-orange-700 px-2 py-0.5 rounded text-xs font-medium" data-i18n="tab_industry">行业资讯</span> &gt; CSCO尿路上皮癌指南更新</div>',
        new_html,
        count=1
    )

    # 替换文章标题
    new_html = re.sub(
        r'<h1 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">.*?</h1>',
        f'<h1 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">{TITLE_HTML}</h1>',
        new_html,
        count=1
    )

    # 替换发布信息
    new_html = re.sub(
        r'<p class="text-gray-500 mb-6">发布时间：.*?</p>',
        f'<p class="text-gray-500 mb-6">发布时间：{PUBLISH_DATE} | 来源：{PUBLISH_SOURCE} | 分类：<span data-i18n="tab_industry">行业资讯</span></p>',
        new_html,
        count=1
    )

    # 替换文章内容（从 <div class="article-content"> 后面开始，到 </div></article> 前面结束）
    pattern_content = re.compile(
        r'(<div class="article-content">)\s*<p>.*?(<!-- CTA -->\s*<div class="cta-box">)',
        re.DOTALL
    )
    new_html = pattern_content.sub(
        r'\1\n' + ARTICLE_CONTENT + r'\n            ' + r'\2',
        new_html,
        count=1
    )

    # 替换 CTA 标题（0621 用 ADC 相关）
    new_html = new_html.replace(
        'id="cta-title" class="text-lg mb-3" data-i18n="cta_title">想了解更多跨境医疗与国内会诊合规信息？</p>',
        'id="cta-title" class="text-lg mb-3" data-i18n="cta_title">需要咨询全球抗癌药/ADC药物/HER2靶向药方案？</p>'
    )

    # 修正 disclaimer_text
    new_html = new_html.replace(
        '"本文章仅供信息参考，不构成医疗建议。具体疾病治疗和手术方案请务必咨询专业医生。蓝培医疗为您提供全球优质医疗资源咨询服务，帮助患者了解合规的国内外专家会诊渠道。"',
        '"本文章仅供信息参考，不构成医疗建议。具体疾病治疗和用药方案请务必咨询专业医生。蓝培医疗为您提供全球优质医疗资源咨询服务，帮助患者了解HER2-ADC、免疫联合等创新疗法的合规获取渠道。"'
    )

    # 修正英文 disclaimer
    new_html = new_html.replace(
        '"This article is for reference only and does not constitute medical advice. Please consult professional doctors. Lanpei Medical provides global medical resource consulting services."',
        '"This article is for reference only and does not constitute medical advice. Please consult professional doctors. Lanpei Medical provides global medical resource consulting services, helping patients understand compliance access to innovative therapies such as HER2-ADC and immunotherapy combinations."'
    )

    # 3. 写入目标文件
    target_path_zh = f"{WORK_DIR}/news/{TARGET_FILENAME}"
    with open(target_path_zh, "w", encoding="utf-8") as f:
        f.write(new_html)

    # 4. 同时复制到根目录
    target_path_root = f"{WORK_DIR}/{TARGET_FILENAME}"
    shutil.copy(target_path_zh, target_path_root)

    print(f"✅ 已生成：{target_path_zh}")
    print(f"✅ 已生成：{target_path_root}")
    print(f"📊 文件大小：{os.path.getsize(target_path_zh)} bytes")
    print(f"📊 行数：{sum(1 for _ in open(target_path_zh, encoding='utf-8'))} lines")
    return target_path_zh, target_path_root


if __name__ == "__main__":
    main()
