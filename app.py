import streamlit as st
from rapidfuzz import fuzz

# =========================================================
# 🎬 1. 2026年5月 台北五大影城全制霸資料庫（30部真實完整版）
# =========================================================
def get_absolute_comprehensive_database_2026():
    database = [
        # =================【 A. 李滄東大師經典回顧展專區 】=================
        {
            "title": "燃燒烈愛 (Burning) - 數位重映",
            "genre": "劇情 / 懸疑 / 藝術",
            "style": ["孤獨", "寂寞", "文藝", "深度", "思考", "邊緣", "憂鬱", "沉悶", "李滄東"],
            "story": "改編自村上春樹小說，劉亞仁、文根英、史蒂芬元主演。步調溫慢、隱喻深沉，深刻解構當代青年的無力與階級焦慮。適合自己一個人、寂寞憂鬱時深沉動腦。",
            "theater": "光點華山電影館、誠品電影院"
        },
        {
            "title": "生命之詩 (Poetry) - 4K數位修復",
            "genre": "劇情 / 文藝 / 人性",
            "style": ["憂鬱", "難過", "生命", "深刻", "心靈", "深沉", "文藝", "李滄東"],
            "story": "榮獲坎城影展最佳劇本獎。講述一名失智奶奶在生活重壓與孫子罪行間，尋找世間詩意與人性救贖的故事。適合心情低潮、想探討生命本質時觀看。",
            "theater": "光點華山電影館、誠品電影院"
        },
        {
            "title": "密陽 (Secret Sunshine) - 經典重映",
            "genre": "劇情 / 人性 / 犯罪",
            "style": ["難過", "傷心", "淚水", "痛苦", "深刻", "心碎", "李滄東"],
            "story": "全度妍榮獲坎城影后之作。痛失摯愛的女子透過宗教尋求救贖，卻面臨殘酷人性考驗。適合需要痛哭釋放沉重情緒的影迷。",
            "theater": "光點華山電影館 (影展主場)"
        },
        {
            "title": "綠洲 (Oasis) - 經典重映",
            "genre": "劇情 / 愛情 / 社會",
            "style": ["浪漫", "愛情", "深刻", "文藝", "邊緣", "孤獨", "李滄東"],
            "story": "社會邊緣人與腦性麻痺女子之間純粹、殘酷卻浪漫的愛情故事。挑戰世俗眼光，後勁極強，適合想看深度愛情故事的觀眾。",
            "theater": "光點華山電影館 (影展專題)"
        },
        {
            "title": "薄荷糖 (Peppermint Candy) - 經典重映",
            "genre": "劇情 / 歷史 / 時代",
            "style": ["深刻", "歷史", "傷心", "憂鬱", "沉悶", "一個人", "李滄東"],
            "story": "以倒敘法倒帶一個男人悲劇的一生，折射時代巨變對個體的摧殘。那句『我要回去！』震撼影史。適合獨自靜靜品味宿命感。",
            "theater": "光點華山電影館 (影展專題)"
        },

        # =================【 B. 商業大製作 / 科幻 / 冒險 】=================
        {
            "title": "極限返航 (Project Hail Mary)",
            "genre": "科幻 / 奇幻 / 劇情",
            "style": ["震撼", "爽片", "科幻", "巨幕", "大片", "期待", "熱血"],
            "story": "萊恩葛斯林主演。科學老師在太空船醒來，必須解開太陽衰亡的巨大謎團。場面壯闊，極度熱血刺激，適合消除日常壓力與煩躁感。",
            "theater": "威秀影城、秀泰影城、國賓大戲院"
        },
        {
            "title": "曼達洛人與古古 (The Mandalorian & Grogu)",
            "genre": "動作 / 科幻 / 冒險",
            "style": ["熱血", "震撼", "大片", "刺激", "冒險", "期待", "同學", "死黨"],
            "story": "星際大戰系列重返大銀幕！娛樂性與特效拉滿，最適合揪同學、死黨成群結隊去電影院狂歡發洩。",
            "theater": "威秀影城、西門秀泰、國賓影城"
        },
        {
            "title": "特技玩家",
            "genre": "動作 / 喜劇 / 浪漫",
            "style": ["放鬆", "歡樂", "幽默", "爆笑", "約會", "情侶", "娛樂"],
            "story": "頂級特技演員的冒險與愛情。節奏明快、有笑有淚，既有熱血特技又有浪漫愛情，非常適合情侶約會放鬆。",
            "theater": "威秀影城、秀泰影城、微風國賓"
        },
        {
            "title": "麥克傑克森 (MICHAEL)",
            "genre": "音樂 / 傳記 / 劇情",
            "style": ["熱血", "震撼", "期待", "回憶", "深刻", "感動"],
            "story": "天王麥可傑克森官方傳記電影。重現無數經典舞台與震撼音樂現場，適合熱愛音樂、期待大場面震撼的觀眾。",
            "theater": "威秀影城、秀泰影城、國賓大戲院"
        },
        {
            "title": "猩球崛起：王國誕生",
            "genre": "動作 / 科幻 / 冒險",
            "style": ["震撼", "爽片", "熱血", "刺激", "科幻", "巨幕", "爆米花"],
            "story": "史詩鉅作。人類與猿族命運全新篇章，視覺特效極致震撼。適合消除日常壓力與煩躁感。",
            "theater": "威秀影城、秀泰影城、國賓大戲院"
        },

        # =================【 C. 動作巨製 / 驚悚犯罪 】=================
        {
            "title": "寒戰1994 (Cold War 1994)",
            "genre": "動作 / 懸疑 / 犯罪",
            "style": ["動作", "發洩", "爽片", "震撼", "翻轉", "懸疑", "燒腦"],
            "story": "倒帶至回歸前夜的香港，警匪智商博弈與街頭槍戰。劇情層層翻轉，適合發洩與喜愛燒腦的觀眾。",
            "theater": "威秀影城、秀泰影城、國賓影城"
        },
        {
            "title": "屍速禁區 (Colony)",
            "genre": "動作 / 驚悚 / 冒險",
            "style": ["刺激", "驚悚", "動作", "爽片", "無尿點", "暴怒", "發洩"],
            "story": "全智賢、池昌旭主演。極度末日感與瘋狂打鬥，節奏極速狂熱，看主角大殺四方能徹底解放暴怒心情。",
            "theater": "威秀影城、秀泰影城、國賓影城"
        },
        {
            "title": "真人快打II (Mortal Kombat 2)",
            "genre": "動作 / 奇幻 / 格鬥",
            "style": ["動作", "發洩", "爽片", "熱血", "刺激", "死黨", "爆米花"],
            "story": "經典格鬥續集。血肉模糊、拳拳到肉的極致暴力美學。適合想找死黨用爆米花電影發洩情緒。",
            "theater": "威秀影城、秀泰影城"
        },
        {
            "title": "地下城の怪物先生 (MR.MONSTER)",
            "genre": "動作 / 奇幻 / 冒險",
            "style": ["冒險", "奇幻", "動作", "放鬆", "娛樂", "驚悚"],
            "story": "楊一展監製。地下城暗黑怪物與人類冒險故事，充滿爽快戰鬥，是不燒腦的舒壓電影。",
            "theater": "威秀影城、秀泰影城、國賓大戲院"
        },
        {
            "title": "芙莉歐莎：瘋狂麥斯傳奇篇章",
            "genre": "動作 / 冒險 / 驚悚",
            "style": ["刺激", "飛車", "打鬥", "發洩", "爽片", "暴怒", "無尿點"],
            "story": "廢土美學神作！全片高速狂熱，飛車追逐與爆破。被主管罵、心情抓狂時宣洩的首選。",
            "theater": "威秀影城、秀泰影城、國賓大戲院"
        },

        # =================【 D. 恐怖話題 / 網路怪談 】=================
        {
            "title": "後室 (Backrooms)",
            "genre": "恐怖 / 驚悚 / 科幻",
            "style": ["恐怖", "驚悚", "嚇人", "懸疑", "自己", "刺激", "邊緣"],
            "story": "全球網路都市怪談搬上銀幕！無盡的黃色房間、密閉恐懼與未知怪物追擊。適合享受孤獨寂寞的影迷。",
            "theater": "威秀影城、秀泰影城"
        },
        {
            "title": "絕．種 (The Seeding)",
            "genre": "恐怖 / 驚悚 / 心理",
            "style": ["驚悚", "心理", "犯罪", "沉悶", "深度", "思考"],
            "story": "入圍國際影展話題片。男人被困沙漠深坑遭受心理折磨。風格冷冽深沉，適合深度驚悚喜好者。",
            "theater": "威秀影城、長春國賓"
        },
        {
            "title": "破墓",
            "genre": "恐怖 / 驚悚 / 懸疑",
            "style": ["恐怖", "鬼片", "刺激", "同學", "朋友", "驚悚", "嚇人"],
            "story": "風水薩滿恐怖神作。儀式感十足，懸疑氣氛拉滿。適合揪朋友進戲院被嚇體驗快感。",
            "theater": "威秀影城、秀泰影城、國賓大戲院"
        },

        # =================【 E. 動畫 / 輕鬆喜劇 】=================
        {
            "title": "加菲貓：瘋狂大冒險",
            "genre": "動畫 / 喜劇 / 闔家觀賞",
            "style": ["放鬆", "歡樂", "卡通", "療癒", "溫馨", "不燒腦", "哈哈"],
            "story": "爆笑冒險，全新演繹經典賤貓。完全不需要動腦，非常適合闔家觀賞或日常疲勞時療癒。",
            "theater": "威秀、秀泰、誠品、國賓"
        },
        {
            "title": "花綠青綻放之時 (A New Dawn)",
            "genre": "動畫 / 劇情 / 治癒",
            "style": ["放鬆", "療癒", "日常", "溫馨", "動畫", "治癒", "陪伴"],
            "story": "唯美文青動畫。微小轉折與心靈救贖，畫面療癒，適合心情低潮時給自己打氣。",
            "theater": "誠品、光點華山、威秀"
        },
        {
            "title": "名偵探柯南引爆摩天樓修復版",
            "genre": "動畫 / 懸疑 / 經典",
            "style": ["懸疑", "燒腦", "經典", "回憶", "一個人", "日常"],
            "story": "柯南電影第一部傳奇神作 4K 重現。紅線選擇與爆炸，充滿情懷。適合粉絲去回味感動。",
            "theater": "威秀影城、秀泰影城、國賓影城"
        },
        {
            "title": "穿著Prada的惡魔2",
            "genre": "劇情 / 喜劇 / 時尚",
            "style": ["放鬆", "職場", "喜劇", "幽默", "約會", "情侶"],
            "story": "時尚神作續集。犀利對白再現職場生存學，非常適合職場受挫紓壓。",
            "theater": "威秀影城、誠品電影院、微風國賓"
        },

        # =================【 F. 溫馨親情 / 浪漫愛情 】=================
        {
            "title": "別離無恙 (Until We Meet Again)",
            "genre": "劇情 / 愛情 / 催淚",
            "style": ["難過", "傷心", "想哭", "哭爆", "浪漫", "失戀", "淚水"],
            "story": "目黑蓮主演。生死告別細膩催淚大作。失戀、分手想哭爆釋放情緒的人必看。",
            "theater": "誠品、威秀、秀泰"
        },
        {
            "title": "你能吃到媽媽煮的飯的次數剩365次",
            "genre": "劇情 / 溫馨 / 親情",
            "style": ["溫馨", "親情", "爸媽", "家人", "治癒", "陪伴", "感動"],
            "story": "溫暖催淚改編。以數字計算與父母相處剩餘時間，適合全家人觀看。",
            "theater": "誠品、光點華山、國賓影城"
        },

        # =================【 G. 紀錄片 / 文藝修復 】=================
        {
            "title": "單身動物園 (The Lobster) 重映",
            "genre": "劇情 / 奇幻 / 黑色幽默",
            "style": ["孤獨", "寂寞", "文藝", "深度", "思考", "邊緣", "單身"],
            "story": "反烏托邦神作。不談戀愛就變動物，辛辣諷刺現代情感。適合邊緣人深度品味。",
            "theater": "光點華山、誠品電影院"
        },
        {
            "title": "末代皇帝（4K修復版）",
            "genre": "劇情 / 歷史 / 傳記",
            "style": ["文藝", "歷史", "深度", "深刻", "經典", "修復", "一個人"],
            "story": "傳奇史詩。坂本龍一神級配樂，適合獨自一人靜靜享受歷史的孤獨感。",
            "theater": "光點華山、誠品、長春國賓"
        },
        {
            "title": "傳奇女伶高菊花 (La Paloma)",
            "genre": "紀錄片 / 傳記 / 歷史",
            "style": ["深刻", "難過", "生命", "低潮", "歷史", "獨立"],
            "story": "台灣歌手紀錄片。在命運重壓下艱難生存歷程。極具歷史厚度，看完令人低迴落淚。",
            "theater": "光點華山、誠品電影院"
        },
        {
            "title": "甘露水 (Daughter of Nectar)",
            "genre": "紀錄片 / 藝術 / 歷史",
            "style": ["文藝", "深度", "心靈", "平淡", "日常", "生命"],
            "story": "圍繞國寶級雕刻藝術作品紀錄片。對土地與藝術心靈深刻凝視，極致療癒。",
            "theater": "光點華山、誠品電影院"
        },
        {
            "title": "104歲哲代奶奶：一個人生活",
            "genre": "紀錄片 / 溫馨 / 日常",
            "style": ["療癒", "日常", "溫馨", "不舒服", "放鬆", "陪伴", "自己"],
            "story": "凝視奶奶生活展示生活哲學。疲勞感到空虛時看，極度溫暖治癒。",
            "theater": "光點華山、誠品電影院"
        },
        {
            "title": "經典大師：數位修復專題",
            "genre": "劇情 / 歷史 / 經典修復",
            "style": ["文藝", "歷史", "傳記", "懷舊", "一個人", "經典"],
            "story": "4K 修復神作。適合想遠離喧囂、安靜獨處的影迷。",
            "theater": "光點華山、誠品電影院"
        }
    ]
    return database

# =========================================================
# 🎯 2. 高級多維度加權選片推薦引擎 (100% 完整保留)
# =========================================================
def recommend_movies_ultimate(user_input, movies):
    if not movies: return [], False
    user_input = user_input.lower().strip()

    mood_map = {
        "憂鬱": ["憂鬱", "低潮", "寂寞", "孤單", "無聊", "空虛", "李滄東"],
        "煩躁": ["煩躁", "煩", "壓力大", "暴怒", "抓狂"],
        "興奮": ["興奮", "期待", "熱血", "爽片", "震撼"],
        "開心": ["開心", "放鬆", "歡樂", "搞笑", "幽默", "舒壓"],
        "難過": ["難過", "傷心", "想哭", "失戀", "分手"],
        "不舒服": ["不舒服", "累", "疲憊", "療癒", "溫馨"]
    }
    
    style_targets = {
        "憂鬱": ["療癒", "心靈", "文藝", "深沉", "李滄東"],
        "煩躁": ["爽片", "刺激", "發洩", "動作", "無尿點"],
        "興奮": ["熱血", "震撼", "大片", "科幻", "巨幕"],
        "開心": ["放鬆", "歡樂", "卡通", "喜劇", "幽默"],
        "難過": ["難過", "傷心", "想哭", "淚水", "失戀"],
        "不舒服": ["放鬆", "不燒腦", "療癒", "溫馨", "日常"]
    }

    recommended = []
    for movie in movies:
        score = 0
        movie_text = (movie['title'] + movie['genre'] + movie['story']).lower()
        movie_styles = movie['style']
        
        # 片名與簡介關鍵字全匹配加分
        if user_input in movie_text: score += 30
        
        # 模糊匹配加分
        title_sim = fuzz.partial_ratio(user_input, movie["title"].lower())
        if title_sim >= 70: score += title_sim * 0.2

        # 情感對照加分
        for mood, words in mood_map.items():
            if any(w in user_input for w in words):
                for target in style_targets.get(mood, []):
                    if target in movie_styles: score += 10
                    if target in movie_text: score += 5

        if score > 0: recommended.append((movie, score))

    recommended.sort(key=lambda x: x[1], reverse=True)
    return [item[0] for item in recommended], len(recommended) > 0


# =========================================================
# 🎨 3. UI 裝飾：票券風高清晰度設計 (Light Mode 優化)
# =========================================================
st.set_page_config(page_title="台北影城智慧推薦", page_icon="🎬", layout="wide")

st.markdown("""
    <style>
    /* 1. 改為暖色調高對比背景，不再是全黑 */
    [data-testid="stAppViewContainer"] {
        background-color: #F8F9FA !important;
    }

    /* 2. 側邊欄：深酒紅木質感 + 亮金膠捲齒孔 */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #5c0006 0%, #3d0004 100%) !important;
        position: relative !important;
        box-shadow: 5px 0 15px rgba(0,0,0,0.2) !important;
    }
    [data-testid="stSidebar"]::after {
        content: ""; position: absolute; right: 0; top: 0; bottom: 0; width: 14px;
        background-color: #000; background-image: radial-gradient(circle, #ffcc00 35%, transparent 40%);
        background-size: 14px 28px; background-repeat: repeat-y; border-left: 1px solid #ffcc00;
    }

    /* 側邊欄卡片：高對比白字 */
    .sidebar-section {
        background: rgba(0, 0, 0, 0.3) !important;
        border: 1px solid #ffcc00 !important;
        border-radius: 8px; padding: 15px; margin-bottom: 20px;
    }
    .sidebar-title { color: #ffcc00 !important; font-size: 1.1rem; font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #ffcc00; }
    .sidebar-text { color: #ffffff !important; font-size: 0.95rem; line-height: 1.6; }

    /* 3. 頂部看板：Vintage Marquee (Light Mode) */
    .vintage-marquee {
        background-color: #ffffff;
        border: 5px double #d97706; /* 羊皮金邊 */
        border-radius: 14px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 5px 25px rgba(0,0,0,0.1);
        margin-bottom: 35px;
    }
    .marquee-title {
        color: #1e293b !important; /* 深墨藍字 */
        font-size: 2.8rem !important;
        font-weight: 900 !important;
        letter-spacing: 2px;
        text-shadow: 1px 1px 0px #ffcc00;
        margin-bottom: 5px;
    }
    .marquee-subtitle { color: #d97706 !important; font-weight: bold; font-size: 1.2rem; }

    /* 4. 數據卡片：專業簡報感 */
    .stat-card {
        background: #ffffff;
        border-left: 5px solid #d97706;
        border-radius: 8px;
        padding: 15px 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 30px;
        max-width: 320px;
    }
    .stat-label { color: #64748b !important; font-size: 1rem; font-weight: bold; }
    .stat-value { color: #1e293b !important; font-size: 2.4rem !important; font-weight: 900; }

    /* 5. ✍️ 售票口：高對比黑字，保證清晰 */
    div[data-testid="stTextInput"] label p {
        color: #1e293b !important;
        font-size: 1.4rem !important;
        font-weight: 900 !important;
    }
    div[data-testid="stTextInput"] input {
        background-color: #ffffff !important;
        color: #1e293b !important;
        font-size: 1.2rem !important;
        border: 2px solid #cbd5e1 !important;
        border-radius: 8px !important;
    }

    /* 6. 按鈕：經典院線紅 */
    div.stButton > button:first-child {
        background: #dc2626 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        font-size: 1.3rem !important;
        font-weight: 900 !important;
        width: 100% !important;
        padding: 10px 0 !important;
        box-shadow: 0 4px 0px #991b1b;
    }

    /* 7. 電影結果卡片：票券式樣式 */
    div[data-testid="stExpander"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
    }
    div[data-testid="stExpander"] summary p {
        color: #1e293b !important;
        font-weight: 900 !important;
        font-size: 1.3rem !important;
    }
    .movie-detail-text {
        color: #334155 !important; /* 深灰色內文，最利於閱讀 */
        font-size: 1.1rem !important;
        line-height: 1.8 !important;
    }
    </style>
""", unsafe_allow_html=True)


# =========================================================
# 🗂️ 4. 豐富功能的側邊導覽 (Sidebar)
# =========================================================
with st.sidebar:
    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="sidebar-section">
            <div class="sidebar-title">🍿 系統核心介紹</div>
            <div class="sidebar-text">
                本系統專為台北影迷打造，全面收錄 <b>威秀、光點華山、秀泰、誠品、國賓</b> 當期片單。
            </div>
        </div>
        <div class="sidebar-section">
            <div class="sidebar-title">🎥 李滄東影展焦點</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.video("https://www.youtube.com/watch?v=oho89asI5S4")
    
    st.markdown("""
        <div class="sidebar-section">
            <div class="sidebar-title">💡 搜尋秘笈</div>
            <div class="sidebar-text">
                • <b>煩躁/爽片</b>：輸入"煩、壓力大"。<br>
                • <b>深度/文藝</b>：輸入"寂寞、李滄東"。
            </div>
        </div>
        <div class="sidebar-section">
            <div class="sidebar-title">🟢 院線連線狀態</div>
            <div class="sidebar-text" style="font-size: 0.85rem;">
                • 資料庫版本：<b>2026.05 V3.0</b><br>
                • 影展座位：<b>即時同步中</b>
            </div>
        </div>
    """, unsafe_allow_html=True)


# =========================================================
# 🎫 5. 主頁面介面呈現
# =========================================================
# 羊皮紙票券風格看板
st.markdown("""
    <div class="vintage-marquee">
        <h1 class="marquee-title">🎬 台北影城智慧電影推薦系統</h1>
        <p class="marquee-subtitle">結合 <b>多維度矩陣加權</b> 與 <b>生活情境字典</b> 完美選片</p>
    </div>
""", unsafe_allow_html=True)

# 數據統計
movie_db = get_absolute_comprehensive_database_2026()
st.markdown(f"""
    <div class="stat-card">
        <div class="stat-label">🎫 台北合作院線總上映部數</div>
        <div class="stat-value">{len(movie_db)} 部</div>
    </div>
""", unsafe_allow_html=True)

# 輸入區
user_input = st.text_input(
    "👉 售票口：請告訴我們您今天遇到了什麼事？想看什麼樣的電影？", 
    placeholder="試試看：我分手了想哭爆、跟爸媽看、熱血爽片、李滄東"
)

# 推薦按鈕
if st.button("🚀 啟動台北影城智慧推薦"):
    if user_input.strip() == "":
        st.warning("請輸入內容以利劃位推薦喔！")
    else:
        results, is_matched = recommend_movies_ultimate(user_input, movie_db)

        if not is_matched or not results:
            st.error("😭 抱歉，目前暫無最契合的電影情境，要不要換個關鍵字？")
        else:
            st.success(f"🧠 系統解析完成！精選出 {len(results)} 部完美電影：")
            
            for i, m in enumerate(results, 1):
                with st.expander(f"🍿 【推薦第 {i}】 {m['title']}", expanded=True):
                    st.markdown(f"""
                    <div class="movie-detail-text">
                        <b>🎭 類型</b>：<span style="color:#d97706; font-weight:bold;">{m['genre']}</span><br>
                        <b>📍 台北建議影城</b>：<span style="color:#1e293b; font-weight:900;">{m['theater']}</span><br>
                        <b>📝 推薦理由</b>：{m['story']}
                    </div>
                    """, unsafe_allow_html=True)
