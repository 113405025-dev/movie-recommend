import streamlit as st
from rapidfuzz import fuzz

# =========================================================
# 🎬 電影資料庫（超強情境優化版 2026）- 100% 完全保留
# =========================================================
def get_absolute_comprehensive_database_2026():
    database = [
        {
            "title": "燃燒烈愛 (Burning) - 數位重映",
            "genre": "劇情 / 懸疑 / 藝術",
            "style": ["孤獨", "寂寞", "文藝", "深度", "思考", "邊緣", "憂鬱", "沉悶", "李滄東", "失戀", "分手", "心情不好", "壓力大"],
            "story": "改編自村上春樹小說，劉亞仁、文根英、史蒂芬元主演。",
            "theater": "光點華山電影館 (影展主場)、誠品電影院"
        },
        {
            "title": "生命之詩 (Poetry) - 4K數位修復",
            "genre": "劇情 / 文藝 / 人性",
            "style": ["憂鬱", "難過", "生命", "深刻", "心靈", "李滄東", "想哭", "低潮"],
            "story": "榮獲坎城影展最佳劇本獎。",
            "theater": "光點華山電影館"
        },
        {
            "title": "密陽 (Secret Sunshine) - 經典重映",
            "genre": "劇情 / 人性 / 犯罪",
            "style": ["難過", "傷心", "淚水", "心碎", "李滄東", "痛苦", "失戀", "分手"],
            "story": "全度妍榮獲坎城影后之作。",
            "theater": "光點華山電影館"
        },
        {
            "title": "綠洲 (Oasis) - 經典重映",
            "genre": "劇情 / 愛情 / 社會",
            "style": ["浪漫", "愛情", "孤獨", "邊緣", "李滄東", "情侶", "約會"],
            "story": "社會邊緣人愛情故事。",
            "theater": "光點華山電影館"
        },
        {
            "title": "薄荷糖 (Peppermint Candy) - 經典重映",
            "genre": "劇情 / 歷史 / 時代",
            "style": ["憂鬱", "歷史", "沉悶", "一個人", "李滄東", "遺憾", "悲劇"],
            "story": "倒敘人生悲劇。",
            "theater": "光點華山電影館"
        },
        # ================= 商業片 =================
        {
            "title": "極限返航 (Project Hail Mary)",
            "genre": "科幻 / 劇情",
            "style": ["震撼", "爽片", "科幻", "熱血", "大場面", "冒險", "撿到錢", "發財", "心情好", "很爽"],
            "story": "太空科學危機。",
            "theater": "威秀影城"
        },
        {
            "title": "曼達洛人與古古",
            "genre": "動作 / 科幻",
            "style": ["熱血", "刺激", "冒險", "帥氣", "飆車", "大場面", "心情不錯"],
            "story": "星際冒險。",
            "theater": "威秀影城"
        },
        {
            "title": "特技玩家",
            "genre": "動作 / 喜劇",
            "style": ["放鬆", "幽默", "約會", "開心", "歡樂", "放鬆", "心情好", "心情不錯", "下班", "散心"],
            "story": "特技演員愛情故事。",
            "theater": "威秀影城"
        },
        {
            "title": "麥克傑克森 (MICHAEL)",
            "genre": "音樂 / 傳記",
            "style": ["熱血", "震撼", "感動", "經典", "音樂", "熱血"],
            "story": "MJ傳記電影。",
            "theater": "威秀影城"
        },
        {
            "title": "猩球崛起：王國誕生",
            "genre": "科幻 / 動作",
            "style": ["震撼", "爽片", "科幻", "特效", "大場面"],
            "story": "猿族新篇章。",
            "theater": "威秀影城"
        },
        # ================= 恐怖 =================
        {
            "title": "後室 (Backrooms)",
            "genre": "恐怖 / 驚悚",
            "style": ["恐怖", "驚悚", "刺激", "嚇人", "重口味", "刺激", "無腦"],
            "story": "無盡黃色房間怪談。",
            "theater": "威秀影城"
        },
        {
            "title": "破墓",
            "genre": "恐怖 / 懸疑",
            "style": ["恐怖", "鬼片", "驚悚", "阿飄", "有鬼", "嚇死人"],
            "story": "風水恐怖故事。",
            "theater": "威秀影城"
        },
        # ================= 動畫 =================
        {
            "title": "加菲貓：瘋狂大冒險",
            "genre": "動畫 / 喜劇",
            "style": ["放鬆", "療癒", "歡樂", "搞笑", "不用動腦", "休閒", "心情好", "心情不錯", "開心"],
            "story": "爆笑動畫電影。",
            "theater": "威秀影城"
        },
        {
            "title": "花綠青綻放之時",
            "genre": "動畫 / 治癒",
            "style": ["療癒", "溫馨", "日常", "暖心", "放空", "小品", "毛小孩", "放鬆"],
            "story": "治癒系動畫。",
            "theater": "誠品電影院"
        },
        # ================= 更多 =================
        {
            "title": "單身動物園",
            "genre": "劇情 / 奇幻",
            "style": ["孤獨", "深度", "思考", "反烏托邦", "單身", "諷刺"],
            "story": "反烏托邦單身世界。",
            "theater": "誠品電影院"
        },
        {
            "title": "末代皇帝（修復版）",
            "genre": "歷史 / 劇情",
            "style": ["經典", "歷史", "深刻", "老片", "藝術", "文青", "修復版"],
            "story": "溥儀人生。",
            "theater": "光點華山"
        }
    ]
    return database

# =========================================================
# 🎯 智慧推薦引擎 - 100% 完全保留
# =========================================================
def recommend_movies(user_input, movies):
    user_input = user_input.lower().strip()
    if not user_input:
        return []

    synonyms_map = {
        "放鬆": ["放鬆", "無腦", "下班", "休閒", "輕鬆", "殺時間", "不用動腦", "放空", "無聊", "累了"],
        "爽片": ["爽片", "爽", "震撼", "刺激", "撿到錢", "發財", "熱血", "爆米花", "嗨", "大場面", "特效", "開車", "飆車"],
        "憂鬱": ["憂鬱", "傷心", "難過", "失戀", "想哭", "心碎", "沉悶", "寂寞", "孤獨", "經痛", "悶悶的", "壓力大", "低潮", "哭哭", "分手"],
        "恐怖": ["恐怖", "鬼片", "嚇人", "驚悚", "毛毛的", "刺激", "重口味", "血腥", "阿飄", "有鬼"],
        "療癒": ["療癒", "治癒", "溫馨", "日常", "可愛", "舒服", "放鬆", "暖心", "小品"],
        "浪漫": ["浪漫", "愛情", "情侶", "約會", "放閃", "甜蜜"],
        "歡樂": ["歡樂", "開心", "心情好", "心情不錯", "哈哈", "搞笑", "高興", "很好"]
    }

    search_keywords = [user_input]
    for standard_style, phrases in synonyms_map.items():
        if any(phrase in user_input for phrase in phrases):
            search_keywords.append(standard_style)
            search_keywords.extend(phrases)
    search_keywords = list(set(search_keywords))

    results = []
    for movie in movies:
        score = 0
        movie_text = (movie["title"] + movie["genre"] + movie["story"]).lower()

        for style in movie["style"]:
            style_lower = style.lower()
            for kw in search_keywords:
                if kw == style_lower or style_lower in user_input or user_input in style_lower:
                    score += 35  
                similarity = fuzz.partial_ratio(kw, style_lower)
                if similarity >= 70:  
                    score += similarity * 0.15

        if any(kw in movie_text for kw in search_keywords):
            score += 10
            
        title_sim = fuzz.partial_ratio(user_input, movie["title"].lower())
        if title_sim >= 70:
            score += title_sim * 0.15

        if score > 0:
            results.append((movie, score))

    if not results:
        return []

    results.sort(key=lambda x: x[1], reverse=True)
    top_score = results[0][1]
    threshold = top_score * 0.35
    final_movies = [movie for movie, score in results if score >= threshold]
    return final_movies


# =========================================================
# 🎨 頂級電影院視覺設計（輸入框大強烈醒目版）
# =========================================================
st.set_page_config(page_title="威秀電影推薦系統", page_icon="🎬", layout="wide")

st.markdown("""
    <style>
    /* 全域背景：極致黑色，襯托霓虹 */
    [data-testid="stAppViewContainer"] {
        background-color: #050505;
    }

    /* 🎬 側邊欄美化：深紅絲絨 */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #500000 0%, #150000 100%);
        border-right: 8px double #ffcc00;
        padding-top: 20px;
    }
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] h2 {
        color: #ffcc00 !important;
        font-weight: bold;
    }

    /* 頂部霓虹招牌標題 */
    .cinema-marquee {
        background-color: #111111;
        padding: 35px;
        border-radius: 12px;
        border: 4px solid #ff0033;
        box-shadow: 0 0 25px #ff0033, inset 0 0 15px #ff0033;
        text-align: center;
        margin-bottom: 35px;
    }
    .marquee-title {
        color: #fff !important;
        font-weight: 900 !important;
        font-size: 3.2rem !important;
        text-shadow: 0 0 8px #fff, 0 0 20px #ffcc00, 0 0 30px #ffcc00;
        letter-spacing: 6px;
    }

    /* 🎯 核心醒目化：Streamlit 原生輸入格 CSS 強制重寫 */
    div[data-testid="stTextInput"] input {
        background-color: #ffffff !important; /* 強制純白背景 */
        color: #000000 !important;            /* 強制純黑文字，絕對看得見 */
        font-size: 1.3rem !important;         /* 放大字體 */
        font-weight: bold !important;
        border: 3px solid #ffcc00 !important; /* 霓虹金邊 */
        border-radius: 8px !important;
        box-shadow: 0 0 15px #ffcc00 !important; /* 金光外發散 */
        padding: 15px !important;
    }
    /* 聚焦時的輸入格樣式 */
    div[data-testid="stTextInput"] input:focus {
        border: 3px solid #ff0033 !important;
        box-shadow: 0 0 20px #ff0033 !important; /* 點擊時變霓虹紅 */
    }

    /* 🎬 範例 4 復古黃黑電影膠捲卡片 (Film Strip Card) */
    .retro-film-strip {
        background-color: #161616;
        border-left: 5px solid #ffcc00;
        border-right: 5px solid #ffcc00;
        margin-bottom: 35px;
        box-shadow: 0 12px 25px rgba(0,0,0,0.8);
        border-radius: 6px;
        overflow: hidden;
    }
    /* 膠捲齒孔設計：黑底黃孔 */
    .film-holes-top {
        background-color: #000000;
        color: #ffcc00;
        font-family: monospace;
        font-size: 16px;
        letter-spacing: 12px;
        padding: 6px;
        text-align: center;
        border-bottom: 2px solid #222;
    }
    .film-holes-bottom {
        background-color: #000000;
        color: #ffcc00;
        font-family: monospace;
        font-size: 16px;
        letter-spacing: 12px;
        padding: 6px;
        text-align: center;
        border-top: 2px solid #222;
    }
    .film-content {
        padding: 25px;
    }

    .movie-title {
        color: #ffcc00 !important;
        font-size: 1.9rem !important;
        font-weight: 800 !important;
        text-shadow: 2px 2px 4px #000;
        margin-bottom: 12px;
    }
    .badge-red {
        background-color: #ff0033; color: white;
        padding: 6px 16px; border-radius: 4px;
        font-size: 0.95rem; font-weight: bold; display: inline-block; margin-right: 12px;
    }
    .story-box {
        background-color: #222222;
        padding: 18px;
        border-radius: 6px;
        color: #eeeeee;
        font-size: 1.1rem;
        border-left: 4px solid #ffcc00;
        margin-top: 15px;
        line-height: 1.6;
    }

    /* 數據儀表板 */
    .stMetric label, .stMetric div {
        color: #ffcc00 !important;
        font-weight: bold !important;
    }
    
    /* 威秀紅高級發光大按鈕 */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff0033 0%, #b30022 100%) !important;
        color: white !important;
        border: 2px solid #ffcc00 !important;
        border-radius: 8px !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
        padding: 12px 0px !important;
        box-shadow: 0 4px 15px rgba(255, 0, 51, 0.4);
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        box-shadow: 0 0 25px #ff0033 !important;
        transform: scale(1.01);
    }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# 🏠 側邊欄美化區
# =========================================================
with st.sidebar:
    st.markdown("## 🎞️ 影廳導覽")
    st.image("https://img.icons8.com/clouds/200/movie-projector.png")
    st.write("---")
    st.markdown("### 🍿 觀影小撇步")
    st.info("輸入「憂鬱」或「想哭」，系統會為你挑選觸動心靈的傑作。")
    st.markdown("### 🎭 影城狀態")
    st.success("威秀影城：連線中")
    st.success("藝術院線：同步中")
    st.write("---")
    st.markdown("© 2026 台北電影智慧推薦")

# =========================================================
# 🎬 主頁面內容
# =========================================================

st.markdown("""
    <div class="cinema-marquee">
        <div class="marquee-title">威秀電影推薦系統</div>
        <p style="color: #ffcc00; font-size: 1.2rem; margin-top:10px; font-weight: bold;">
            本系統已將 RapidFuzz 模糊匹配 與 雙向生活字典 完美整合！
        </p>
    </div>
""", unsafe_allow_html=True)

db = get_absolute_comprehensive_database_2026()
col_m1, col_m2 = st.columns(2)
with col_m1:
    st.metric(label="🎬 院線總部數", value=f"{len(db)} 部")
with col_m2:
    st.metric(label="🔥 匹配演算引擎", value="RapidFuzz PRO")

st.write("---")

# 售票亭高對比提示字
st.markdown("<h2 style='color: #ffffff; text-shadow: 0 0 10px #ff0033; font-weight: 800;'>🎟️ 售票口：請輸入您今天的心情或想看的關鍵字？</h2>", unsafe_allow_html=True)

# 醒目化改造後的輸入框
user_input = st.text_input(
    "👉 提示：輸入完成後，請點擊下方大紅按鈕啟動推薦", 
    placeholder="在此輸入情境（例如：我分手了、今天心情不錯、想看大場面飆車...）"
)

st.write("")

if st.button("🎬 啟動智慧劃位推薦", use_container_width=True):
    if user_input.strip() == "":
        st.warning("請先輸入一些關鍵字喔！")
    else:
        with st.spinner("🎟️ 正在後台為您劃位並搜尋合適影片..."):
            recommended = recommend_movies(user_input, db)

        if not recommended:
            st.error("😭 抱歉，目前沒有找到完全契合的電影，換個說法試試看？")
        else:
            st.balloons()
            st.success(f"🧠 系統成功解析情境！幫您找到 {len(recommended)} 部適合的電影：")
            
            # 引入範例 4 的黃黑超精緻復古底片卡片
            for m in recommended:
                st.markdown(f"""
                <div class="retro-film-strip">
                    <div class="film-holes-top">■   ■   ■   11A ▷   ■   ■   ■   12   ■   ■   ■</div>
                    <div class="film-content">
                        <div class="movie-title">🍿 {m['title']}</div>
                        <div style="margin-top: 10px; margin-bottom: 10px;">
                            <span class="badge-red">🎭 類型：{m['genre']}</span>
                            <span style="color: #ffcc00; font-weight: bold; font-size: 1.1rem;">📍 上映影城：{m['theater']}</span>
                        </div>
                        <div class="story-box">
                            <b>📝 劇情簡介：</b>{m['story']}
                        </div>
                    </div>
                    <div class="film-holes-bottom">■   ■   ■   11A ▷   ■   ■   ■   12   ■   ■   ■</div>
                </div>
                """, unsafe_allow_html=True)
