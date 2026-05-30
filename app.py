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
# 🎯 智慧推薦引擎（完全結合 rapidfuzz 與大腦字典）- 100% 完全保留
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
# 🎨 Streamlit 使用者介面（大進步：色彩修正與畫面豐富版）
# =========================================================
st.set_page_config(page_title="台北電影推薦", page_icon="🎬", layout="centered")

# 透過強大的 CSS 強制修正 Streamlit 深色模式文字看不見的問題，並建立高級卡片感
st.markdown("""
    <style>
    /* 修正全域深色背景，確保不會跟原生文字打架 */
    [data-testid="stAppViewContainer"] {
        background-color: #0d121a;
    }
    
    /* 修正頂部區塊：大幅強化文字顏色對比度與發光質感 */
    .header-card {
        background: linear-gradient(135deg, #161f2e, #0f1622);
        padding: 35px 25px;
        border-radius: 18px;
        border-bottom: 4px solid #ffcc00;
        box-shadow: 0 8px 32px rgba(0, 200, 255, 0.15);
        margin-bottom: 30px;
        text-align: center;
    }
    .header-card h1 {
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 2.2rem !important;
        text-shadow: 0 0 10px rgba(255, 204, 0, 0.3);
    }
    .header-card p {
        color: #e2e8f0 !important;
        font-size: 1.05rem !important;
        margin-top: 10px;
    }

    /* 強制修正 Streamlit 原生 Metric 的灰色死角，變為亮白色與鮮豔綠色 */
    [data-testid="stMetricLabel"] > div {
        color: #cbd5e1 !important;
        font-size: 0.95rem !important;
        font-weight: bold !important;
    }
    [data-testid="stMetricValue"] > div {
        color: #ffffff !important;
        font-weight: 800 !important;
    }
    
    /* 提示字（Input Label）強制高亮 */
    .input-label-text {
        color: #ffffff !important;
        font-size: 1.05rem !important;
        font-weight: 600;
        margin-bottom: 8px;
    }

    /* 豪華獨立電影名片卡片 */
    .custom-movie-card {
        background: linear-gradient(145deg, #1a2333, #111824);
        padding: 24px;
        border-radius: 14px;
        border-left: 6px solid #ffcc00;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.5);
    }
    .custom-title {
        color: #ffffff !important;
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        margin-bottom: 12px;
    }
    
    /* 明亮圓角膠囊標籤 */
    .badge-yellow {
        background-color: #ffcc00 !important; 
        color: #0c1017 !important;
        padding: 4px 12px; border-radius: 20px;
        font-size: 0.85rem; font-weight: bold; display: inline-block; margin-right: 8px;
    }
    .badge-blue {
        background-color: #1e3a8a !important; 
        color: #93c5fd !important;
        padding: 4px 12px; border-radius: 20px;
        font-size: 0.85rem; font-weight: bold; display: inline-block; margin-right: 8px;
        border: 1px solid #3b82f6;
    }
    
    /* 內嵌高質感劇情簡介框 */
    .custom-story-box {
        background-color: #090d14;
        padding: 15px;
        border-radius: 8px;
        color: #e2e8f0;
        font-size: 0.98rem;
        line-height: 1.6;
        margin-top: 15px;
        border-left: 3px solid #4b5563;
    }
    </style>
""", unsafe_allow_html=True)

# 1. 頂部發光文字大外框（完全保留原生用詞）
st.markdown("""
    <div class="header-card">
        <h1>🎬 台北影城智慧電影推薦系統</h1>
        <p>本系統已將 <b>RapidFuzz 模糊匹配</b> 與 <b>雙向生活字典</b> 完美整合！</p>
    </div>
""", unsafe_allow_html=True)

# 2. 數據儀表板（修正前一版本對比度太低的問題，強制高亮顯示）
movies_db = get_absolute_comprehensive_database_2026()
col1, col2 = st.columns(2)
with col1:
    st.metric(label="📊 目前電影庫總數", value=f"{len(movies_db)} 部", delta="台北即時院線與重映片")
with col2:
    st.metric(label="⚙️ 核心匹配技術", value="RapidFuzz", delta="已啟用雙向字典防呆")

st.write("")
st.write("")

# 3. 豐富視覺元件：豐富中段畫面的快捷按鈕（這能讓原本空洞的地方填滿，視覺效果大提升！）
st.markdown("<div class='input-label-text'>💡 試試熱門情境快捷點選：</div>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("💔 分手想哭", use_container_width=True): st.session_state.my_input = "我分手了"
with c2:
    if st.button("🥳 心情大好", use_container_width=True): st.session_state.my_input = "今天心情不錯"
with c3:
    if st.button("🐱 療癒貓咪", use_container_width=True): st.session_state.my_input = "想看加非貓"
with c4:
    if st.button("🏎️ 刺激大場面", use_container_width=True): st.session_state.my_input = "大場面飆車"

# 獲取快捷鍵帶入的預設值
preset_value = st.session_state.get("my_input", "")

# 4. 輸入欄位（將原生提示詞改用自訂高亮樣式渲染）
st.markdown("<div class='input-label-text'>👉 輸入您的心情、生活狀態或想找的關鍵字：</div>", unsafe_allow_html=True)
user_input = st.text_input(
    "（隱藏標籤）", 
    value=preset_value,
    placeholder="試試看輸入：我分手了、今天心情不錯、想看加非貓、大場面飆車",
    label_visibility="collapsed" # 隱藏原生暗淡的標籤，用我們自訂的高亮標籤替代
)

st.write("")

# 原生按鈕與推薦邏輯 100% 保留
if st.button("🚀 啟動智慧推薦", type="primary", use_container_width=True):
    if user_input.strip() == "":
        st.warning("請先輸入一些關鍵字喔！")
    else:
        # 增加流暢的動態加載反饋
        with st.spinner("🧠 系統正在匹配 RapidFuzz 算力與雙向字典標籤..."):
            recommended = recommend_movies(user_input, movies_db)

        if not recommended:
            st.error("😭 抱歉，目前沒有找到完全契合的電影，換個說法試試看？")
        else:
            # 成功的氣球特效，大幅增加生動感
            st.balloons()
            
            # 原生文字完全保留
            st.success(f"🧠 系統成功解析情境！幫您找到 {len(recommended)} 部適合的電影：")
            
            # 5. 將原本黑嘛嘛的 expander 替換成這次大進步的「黑金霓虹高對比卡片」
            for m in recommended:
                st.markdown(f"""
                <div class="custom-movie-card">
                    <div class="custom-title">🍿 {m['title']}</div>
                    <div style="margin-top: 5px; margin-bottom: 5px;">
                        <span class="badge-blue">🎭 電影類型：{m['genre']}</span>
                        <span class="badge-yellow">📍 上映影城：{m['theater']}</span>
                    </div>
                    <div class="custom-story-box">
                        <b>📝 劇情簡介：</b>{m['story']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
