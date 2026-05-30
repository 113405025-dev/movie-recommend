import streamlit as st
from rapidfuzz import fuzz

# =========================================================
# 🎬 電影資料庫（超強情境優化版 2026）
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
# 🎯 智慧推薦引擎（完全結合 rapidfuzz 與大腦字典）
# =========================================================
def recommend_movies(user_input, movies):
    user_input = user_input.lower().strip()
    if not user_input:
        return []

    # 🧠 大腦字典
    synonyms_map = {
        "放鬆": ["放鬆", "無腦", "下班", "休閒", "輕鬆", "殺時間", "不用動腦", "放空", "無聊", "累了"],
        "爽片": ["爽片", "爽", "震撼", "刺激", "撿到錢", "發財", "熱血", "爆米花", "嗨", "大場面", "特效", "開車", "飆車"],
        "憂鬱": ["憂鬱", "傷心", "難過", "失戀", "想哭", "心碎", "沉悶", "寂寞", "孤獨", "經痛", "悶悶的", "壓力大", "低潮", "哭哭", "分手"],
        "恐怖": ["恐怖", "鬼片", "嚇人", "驚悚", "毛毛的", "刺激", "重口味", "血腥", "阿飄", "有鬼"],
        "療癒": ["療癒", "治癒", "溫馨", "日常", "可愛", "舒服", "放鬆", "暖心", "小品"],
        "浪漫": ["浪漫", "愛情", "情侶", "約會", "放閃", "甜蜜"],
        "歡樂": ["歡樂", "開心", "心情好", "心情不錯", "哈哈", "搞笑", "高興", "很好"]
    }

    # 擴充搜尋關鍵字
    search_keywords = [user_input]
    for standard_style, phrases in synonyms_map.items():
        if any(phrase in user_input for phrase in phrases):
            search_keywords.append(standard_style)
            search_keywords.extend(phrases)
    search_keywords = list(set(search_keywords))

    results = []

    # 計算得分
    for movie in movies:
        score = 0
        movie_text = (movie["title"] + movie["genre"] + movie["story"]).lower()

        # 核心 A：風格與情境標籤比對（徹底活用 rapidfuzz）
        for style in movie["style"]:
            style_lower = style.lower()
            for kw in search_keywords:
                # 1. 語意情境命中，直接大幅加分
                if kw == style_lower or style_lower in user_input or user_input in style_lower:
                    score += 35  
                
                # 2. 👀 徹底啟用 rapidfuzz 模糊比對
                similarity = fuzz.partial_ratio(kw, style_lower)
                if similarity >= 70:  
                    score += similarity * 0.15

        # 核心 B：基本文本包含
        if any(kw in movie_text for kw in search_keywords):
            score += 10
            
        # 核心 C：片名防呆（也是用 rapidfuzz）
        title_sim = fuzz.partial_ratio(user_input, movie["title"].lower())
        if title_sim >= 70:
            score += title_sim * 0.15

        if score > 0:
            results.append((movie, score))

    if not results:
        return []

    # ⚖️ 正確排序：依據分數 (x[1]) 由高到低排序
    results.sort(key=lambda x: x[1], reverse=True)

    # 抓出最高分的分數值
    top_score = results[0][1]
    threshold = top_score * 0.35
    
    # 取出符合門檻的電影
    final_movies = [
        movie for movie, score in results 
        if score >= threshold
    ]

    return final_movies


# =========================================================
# 🎨 Streamlit 使用者介面（完全對齊範例：百老匯燈泡、紅絲絨布幕、雙側膠捲）
# =========================================================
# 配置為 wide 寬版以符合範例中雙側膠捲與側欄的大氣格局
st.set_page_config(page_title="台北電影推薦", page_icon="🎬", layout="wide")

# 強大 CSS 裝飾注入：精準重現上傳範例中的所有視覺細節
st.markdown("""
    <style>
    /* 1. 全域背景：電影院深夜黑 */
    [data-testid="stAppViewContainer"] {
        background-color: #0b0b0d !important;
    }

    /* 2. 側邊欄：紅絲絨布幕背景 + 左右雙條黑底金齒孔底片膠捲（100% 還原範例左側） */
    [data-testid="stSidebar"] {
        background: linear-gradient(0deg, #500005 0%, #7a0010 50%, #400003 100%) !important;
        position: relative !important;
        box-shadow: inset -5px 0 20px rgba(0,0,0,0.8) !important;
    }
    /* 側欄左側膠捲條 */
    [data-testid="stSidebar"]::before {
        content: "11A ▷ 12";
        writing-mode: vertical-rl;
        text-orientation: mixed;
        color: #ffcc00;
        font-family: monospace;
        font-size: 11px;
        font-weight: bold;
        text-align: center;
        padding-top: 50px;
        position: absolute;
        left: 0; top: 0; bottom: 0; width: 18px;
        background-color: #000000;
        background-image: radial-gradient(circle, #ffcc00 35%, transparent 40%);
        background-size: 18px 24px;
        background-repeat: repeat-y;
        border-right: 1.5px solid #ffcc00;
        z-index: 10;
    }
    /* 側欄右側膠捲條 */
    [data-testid="stSidebar"]::after {
        content: "";
        position: absolute;
        right: 0; top: 0; bottom: 0; width: 18px;
        background-color: #000000;
        background-image: radial-gradient(circle, #ffcc00 35%, transparent 40%);
        background-size: 18px 24px;
        background-repeat: repeat-y;
        border-left: 1.5px solid #ffcc00;
        z-index: 10;
    }

    /* 3. 百老匯復古霓虹跑馬燈大標題區塊（完全對齊範例核心） */
    .broadway-marquee {
        background: linear-gradient(180deg, #700008 0%, #3a0003 100%) !important;
        border: 4px solid #ffcc00 !important;
        border-radius: 14px !important;
        padding: 30px 20px !important;
        text-align: center !important;
        /* 模擬燈泡發光鏈 */
        box-shadow: 0 0 0 4px #000000, 
                    0 0 20px #ffcc00, 
                    inset 0 0 20px rgba(0,0,0,0.6) !important;
        position: relative;
        margin-bottom: 35px !important;
    }
    /* 建立四週規律排列的復古發光圓形燈泡效果 */
    .broadway-marquee::before {
        content: "";
        position: absolute;
        top: 4px; left: 4px; right: 4px; bottom: 4px;
        border: 2px dashed #ffffff;
        border-radius: 10px;
        opacity: 0.15;
        pointer-events: none;
    }
    .broadway-title {
        color: #ffffff !important;
        font-size: 2.6rem !important;
        font-weight: 900 !important;
        letter-spacing: 2px !important;
        text-shadow: 0 0 12px #ffcc00, 2px 2px 4px #000000 !important;
        margin: 0 0 10px 0 !important;
    }
    .broadway-subtitle {
        color: #ffcc00 !important;
        font-size: 1.15rem !important;
        font-weight: normal !important;
        margin: 0 !important;
        text-shadow: 1px 1px 2px #000000 !important;
    }

    /* 4. 單格數據卡片樣式（完全對齊範例左卡，金黃微光圓角外框） */
    .single-stat-card {
        background: linear-gradient(135deg, #1f1f24 0%, #151518 100%) !important;
        border: 2px solid #ffcc00 !important;
        border-radius: 10px !important;
        padding: 20px 25px !important;
        box-shadow: 0 0 15px rgba(255, 204, 0, 0.25) !important;
        margin-bottom: 30px !important;
        max-width: 400px;
    }
    .stat-label {
        color: #ffffff !important;
        font-size: 1.05rem !important;
        font-weight: bold !important;
        opacity: 0.9;
        margin-bottom: 8px;
    }
    .stat-value {
        color: #ffcc00 !important;
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        text-shadow: 1px 1px 2px #000000 !important;
    }

    /* 5. 輸入框文字與提示：100% 清晰度提升 */
    div[data-testid="stTextInput"] label p {
        color: #ffffff !important;
        font-size: 1.4rem !important;
        font-weight: bold !important;
    }
    div[data-testid="stTextInput"] input {
        background-color: #1a1a1f !important;
        color: #ffffff !important;
        font-size: 1.15rem !important;
        border: 2px solid #ffcc00 !important;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.5) !important;
    }

    /* 6. 劇院大紅長條啟動按鈕（完全對齊範例寬度與色調） */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #e60021 0%, #aa0012 100%) !important;
        color: #ffffff !important;
        border: 2px solid #ffcc00 !important;
        border-radius: 8px !important;
        font-size: 1.25rem !important;
        font-weight: 900 !important;
        width: 100% !important;
        padding: 12px 0 !important;
        box-shadow: 0 5px 15px rgba(230, 0, 33, 0.4) !important;
        text-shadow: 1px 1px 3px #000000 !important;
    }
    
    /* 7. 搜尋結果：改造成膠捲卡片樣式 */
    div[data-testid="stExpander"] {
        background-color: #141417 !important;
        border: 2px solid #ffcc00 !important;
        border-radius: 8px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.5) !important;
    }
    div[data-testid="stExpander"] summary {
        color: #ffcc00 !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 🎯 側邊欄裝飾（僅作為大氣布幕展示，原內容與邏輯不變） ---
with st.sidebar:
    st.markdown("<h3 style='color:#ffcc00;text-align:center;margin-top:20px;'>🎬 影廳導覽</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#ffffff;font-size:0.9rem;padding:0 10px;'>輸入您的心情，系統將自動比對推薦最觸動心靈的精選藝術與院線佳作。</p>", unsafe_allow_html=True)

# --- 🎫 主頁面百老匯大霓虹燈標題（已更換名字，且拿掉任何 RapidFuzz PRO 字樣） ---
st.markdown("""
    <div class="broadway-marquee">
        <h1 class="broadway-title">🎬 台北影城智慧電影推薦系統</h1>
    </div>
""", unsafe_allow_html=True)

# --- 📊 院線總數數據卡片（完全對齊範例左側單卡，移除右側 RapidFuzz PRO 卡） ---
movies_db = get_absolute_comprehensive_database_2026()
st.markdown(f"""
    <div class="single-stat-card">
        <div class="stat-label">🎬 院線總上映部數</div>
        <div class="stat-value">{len(movies_db)} 部</div>
    </div>
""", unsafe_allow_html=True)

# --- ✍️ 售票口輸入區（100% 保留您原本的標題文字與 Placeholder） ---
user_input = st.text_input(
    "👉 輸入您的心情、生活狀態或想找的關鍵字：", 
    placeholder="試試看輸入：我分手了、今天心情不錯、想看加非貓、大場面飆車"
)

# --- 🚀 啟動按鈕與後端完全不變的邏輯比對 ---
if st.button("🚀 啟動智慧推薦"):
    if user_input.strip() == "":
        st.warning("請先輸入一些關鍵字喔！")
    else:
        recommended = recommend_movies(user_input, movies_db)

        if not recommended:
            st.error("😭 抱歉，目前沒有找到完全契合的電影，換個說法試試看？")
        else:
            st.success(f"🧠 系統成功解析情境！幫您找到 {len(recommended)} 部適合的電影：")
            
            for m in recommended:
                with st.expander(f"🍿 {m['title']}", expanded=True):
                    st.markdown(f"**🎭 電影類型**：`{m['genre']}`")
                    st.markdown(f"**📍 上映影城**：{m['theater']}")
                    st.markdown(f"**📝 劇情簡介**：{m['story']}")
# 渲染高質感雙排方形齒孔底片膠捲卡片，文字強制純白！
            for m in recommended:
                st.markdown(f"""
                <div class="retro-film-strip">
                    <div class="film-holes-top">■   ■   ■   11A  ▷  ■   ■   ■   12  ■   ■   ■</div>
                    <div class="film-content">
                        <div class="movie-title">🍿 {m['title']}</div>
                        <div style="margin-top: 10px; margin-bottom: 10px;">
                            <span class="badge-red">🎭 類型：{m['genre']}</span>
                            <span style="color: #ffcc00; font-weight: 900; font-size: 1.15rem; text-shadow: 1px 1px 2px #000;">📍 上映影城：{m['theater']}</span>
                        </div>
                        <div class="story-box">
                            <b style="color: #ffcc00; font-size: 1.2rem;">📝 劇情簡介：</b>{m['story']}
                        </div>
                    </div>
                    <div class="film-holes-bottom">■   ■   ■   11A  ▷  ■   ■   ■   12  ■   ■   ■</div>
                </div>
                """, unsafe_allow_html=True)                    
