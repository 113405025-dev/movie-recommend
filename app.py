import streamlit as st

# =========================================================
# 🎬 1. 電影資料庫（30部真實完全體 2026年5月全制霸版）
# =========================================================
def get_absolute_comprehensive_database_2026():
    """
    台北五大影城（威秀、光點華山、秀泰、誠品、國賓）2026年5月熱映與影展熱售中全制霸資料庫。
    """
    database = [
        # =================【 A. 李滄東大師經典回顧展專區 (光點華山、誠品熱售中)】=================
        {
            "title": "燃燒烈愛 (Burning) - 數位重映",
            "genre": "劇情 / 懸疑 / 藝術",
            "style": ["孤獨", "寂寞", "文藝", "深度", "思考", "邊緣", "憂鬱", "沉悶", "李滄東"],
            "story": "改編自村上春樹小說，劉亞仁、文根英、史蒂芬元主演。極具後現代神祕感，步調溫慢、隱喻深沉，深刻解構當代青年的無力與階級焦慮。適合自己一個人、寂寞憂鬱時深沉動腦。",
            "theater": "光點華山電影館 (影展主場)、誠品電影院 (限量同步)"
        },
        {
            "title": "生命之詩 (Poetry) - 4K數位修復",
            "genre": "劇情 / 文藝 / 人性",
            "style": ["憂鬱", "難過", "生命", "深刻", "心靈", "深沉", "文藝", "李滄東"],
            "story": "榮獲坎城影展最佳劇本獎。講述一名開始失智的奶奶，在生活重壓與孫子犯下的罪行之間，苦苦尋找世間詩意與人性救贖的故事。適合心情低潮、想探討生命本質時觀看。",
            "theater": "光點華山電影館 (影展主場)、誠品電影院"
        },
        {
            "title": "密陽 (Secret Sunshine) - 經典重映",
            "genre": "劇情 / 人性 / 犯罪",
            "style": ["難過", "傷心", "淚水", "痛苦", "深刻", "心碎", "李滄東"],
            "story": "全度妍榮獲坎城影后之作。講述一個痛失摯愛的女子試圖透過宗教尋求救贖，卻面臨更殘酷人性考驗的故事。情感張力極其痛苦且深刻，適合需要痛哭釋放沉重情緒的影迷。",
            "theater": "光點華山電影館 (影展主場)"
        },
        {
            "title": "綠洲 (Oasis) - 經典重映",
            "genre": "劇情 / 愛情 / 社會",
            "style": ["浪漫", "愛情", "深刻", "文藝", "邊緣", "孤獨", "李滄東"],
            "story": "講述一個剛出獄的社會邊緣人與一位重度腦性麻痺女子之間，純粹、殘酷卻無比浪漫的愛情故事。挑戰世俗眼光，後勁極強，適合想看深度、非主流愛情故事的觀眾。",
            "theater": "光點華山電影館 (影展專題)"
        },
        {
            "title": "薄荷糖 (Peppermint Candy) - 經典重映",
            "genre": "劇情 / 歷史 / 時代",
            "style": ["深刻", "歷史", "傷心", "憂鬱", "沉悶", "一個人", "李滄東"],
            "story": "以倒敘法倒帶一個男人悲劇的一生，折射出韓國光州事件等時代巨變對個體的摧殘。那句『我要回去！』震撼影史。適合獨自一人靜靜品味歷史的深沉與宿命感。",
            "theater": "光點華山電影館 (影展專題)"
        },

        # =================【 B. 商業大製作 / 科幻 / 冒險 (威秀、秀泰、國賓首選)】=================
        {
            "title": "極限返航 (Project Hail Mary)",
            "genre": "科幻 / 奇幻 / 劇情",
            "style": ["震撼", "爽片", "科幻", "巨幕", "大片", "期待", "熱血"],
            "story": "萊恩葛斯林主演。科學老師在太空船醒來，必須獨自解開太陽衰亡的巨大謎團。場面壯闊，極度熱血刺激，適合消除日常或課業帶來的沉重壓力與煩躁感。",
            "theater": "威秀影城 (IMAX/4DX首選)、秀泰影城、國賓大戲院"
        },
        {
            "title": "曼達洛人與古古 (The Mandalorian & Grogu)",
            "genre": "動作 / 科幻 / 冒險",
            "style": ["熱血", "震撼", "大片", "刺激", "冒險", "期待", "同學", "死黨"],
            "story": "星際大戰系列睽違多年重返大銀幕之作！鋼鐵人導演執導。娛樂性與特效拉滿，最適合揪同學、死黨成群結隊去電影院狂歡發洩。",
            "theater": "威秀影城、西門秀泰、國賓影城"
        },
        {
            "title": "特技玩家",
            "genre": "動作 / 喜劇 / 浪漫",
            "style": ["放鬆", "歡樂", "幽默", "爆笑", "約會", "情侶", "娛樂"],
            "story": "好萊塢頂級特技演員的玩命冒險與愛情故事。節奏明快、有笑有淚，既有熱血特技又有浪漫愛情，非常適合情侶約會或跟死黨聚會放鬆。",
            "theater": "威秀影城、秀泰影城、微風國賓"
        },
        {
            "title": "麥克傑克森 (MICHAEL)",
            "genre": "音樂 / 傳記 / 劇情",
            "style": ["熱血", "震撼", "期待", "回憶", "深刻", "感動"],
            "story": "流行音樂天王麥可傑克森的官方傳記電影。重現無數經典舞台與震撼音樂現場，後勁極強，適合熱愛音樂、期待大場面震撼的觀眾。",
            "theater": "威秀影城、秀泰影城、國賓大戲院"
        },
        {
            "title": "猩球崛起：王國誕生",
            "genre": "動作 / 科幻 / 冒險",
            "style": ["震撼", "爽片", "熱血", "刺激", "科幻", "巨幕", "爆米花"],
            "story": "科幻史詩鉅作。人類與猿族命運的全新篇章，視覺特效與爆破場面極致震撼。適合消除日常或課業帶來的沉重壓力與煩躁感。",
            "theater": "威秀影城 (IMAX/4DX首選)、秀泰影城、國賓大戲院 (巨幕廳)"
        },

        # =================【 C. 動作巨製 / 遊戲改編 / 驚悚犯罪 (威秀、秀泰、國賓)】=================
        {
            "title": "寒戰1994 (Cold War 1994)",
            "genre": "動作 / 懸疑 / 犯罪",
            "style": ["動作", "發洩", "爽片", "震撼", "翻轉", "懸疑", "燒腦"],
            "story": "古天樂、吳彥祖、周潤發等頂級陣容。倒帶至回歸前夜的香港，警匪智商博弈與街頭槍戰全面升級。劇情層層翻轉，適合熱血發洩與喜愛高智商燒腦的觀眾。",
            "theater": "威秀影城、秀泰影城、國賓影城"
        },
        {
            "title": "屍速禁區 (Colony)",
            "genre": "動作 / 驚悚 / 冒險",
            "style": ["刺激", "驚悚", "動作", "爽片", "無尿點", "暴怒", "發洩"],
            "story": "《屍速列車》導演斥資200億打造，全智賢、池昌旭主演。極度末日感與瘋狂打鬥，節奏極速狂熱，看主角大殺四方能徹底解放生活中的暴怒與阿雜心情。",
            "theater": "威秀影城、秀泰影城、國賓影城"
        },
        {
            "title": "真人快打II (Mortal Kombat 2)",
            "genre": "動作 / 奇幻 / 格鬥",
            "style": ["動作", "發洩", "爽片", "熱血", "刺激", "死黨", "爆米花"],
            "story": "經典格鬥遊戲正統續集。血肉模糊、拳拳到肉的極致暴力美學，毫不拖泥帶水，純粹的爽片。適合期末考爆掉想找死黨用爆米花電影發洩情緒。",
            "theater": "威秀影城、秀泰影城"
        },
        {
            "title": "地下城の怪物先生 (MR.MONSTER)",
            "genre": "動作 / 奇幻 / 冒險",
            "style": ["冒險", "奇幻", "動作", "放鬆", "娛樂", "驚悚"],
            "story": "楊一展監製主演、好萊塢導演執導。地下城的暗黑怪物與人類冒險故事，充滿電玩感與爽快戰鬥，是一部不燒腦的標準爆米花舒壓電影。",
            "theater": "威秀影城、秀泰影城、國賓大戲院"
        },
        {
            "title": "芙莉歐莎：瘋狂麥斯傳奇篇章",
            "genre": "動作 / 冒險 / 驚悚",
            "style": ["刺激", "飛車", "打鬥", "發洩", "爽片", "暴怒", "無尿點"],
            "story": "廢土美學的極致神作！全片高速狂熱，充滿飛車追逐與爆破打鬥。被當、被主管罵、心情抓狂時，來看這部片宣洩紓壓、暴怒宣洩絕對是最爽選擇。",
            "theater": "威秀影城、秀泰影城、國賓大戲院"
        },

        # =================【 D. 恐怖話題 / 網路怪談 / 都市驚悚 (各大影城)】=================
        {
            "title": "後室 (Backrooms)",
            "genre": "恐怖 / 驚悚 / 科幻",
            "style": ["恐怖", "驚悚", "嚇人", "懸疑", "自己", "刺激", "邊緣"],
            "story": "A24將席捲全球網路的都市怪談Creepypasta搬上大銀幕！無盡的黃色房間、密閉恐懼與未知怪物的追擊。適合享受孤獨寂寞、想一個人進戲院被驚悚感強烈電擊的影迷。",
            "theater": "威秀影城、秀泰影城"
        },
        {
            "title": "絕．種 (The Seeding)",
            "genre": "恐怖 / 驚悚 / 心理",
            "style": ["驚悚", "心理", "犯罪", "沉悶", "深度", "思考"],
            "story": "入圍多個國際影展的話題驚悚片。講述一個男人被困在沙漠深坑中，遭受到神祕孤立群落的殘酷心理折磨。風格冷冽深沉，適合喜愛心理犯罪與深度驚悚者。",
            "theater": "威秀影城、長春國賓"
        },
        {
            "title": "破墓",
            "genre": "恐怖 / 驚悚 / 懸疑",
            "style": ["恐怖", "鬼片", "刺激", "同學", "朋友", "驚悚", "嚇人"],
            "story": "引爆亞洲話題的風水薩滿恐怖神作。遷葬引發的致命連鎖反應，儀式感十足，懸疑氣氛拉滿。非常適合揪朋友、同學一起進戲院被嚇，體驗爆米花爽片的快感。",
            "theater": "威秀影城、秀泰影城、國賓大戲院"
        },

        # =================【 E. 動畫 / 輕鬆喜劇 / 闔家觀賞 (各大影城)】=================
        {
            "title": "加菲貓：瘋狂大冒險",
            "genre": "動畫 / 喜劇 / 闔家觀賞",
            "style": ["放鬆", "歡樂", "卡通", "療癒", "溫馨", "不燒腦", "哈哈"],
            "story": "爆笑逗趣的冒險情節，全新演繹經典賤貓。劇情幽默放鬆，完全不需要動腦，非常適合帶爸媽長輩一起闔家觀賞，也是日常疲勞疲憊時的療癒首選。",
            "theater": "威秀影城、秀泰影城、誠品電影院、國賓影城"
        },
        {
            "title": "花綠青綻放之時 (A New Dawn)",
            "genre": "動畫 / 劇情 / 治癒",
            "style": ["放鬆", "療癒", "日常", "溫馨", "動畫", "治癒", "陪伴"],
            "story": "精緻唯美的文青風動畫。敘述日常生活中的微小轉折與心靈救贖，畫面與音樂極具療癒感，適合身體不舒服、心情低潮無力時用來給自己打氣。",
            "theater": "誠品電影院、光點華山電影館、威秀影城"
        },
        {
            "title": "名偵探柯南引爆摩天樓4K修復版",
            "genre": "動畫 / 懸疑 / 經典",
            "style": ["懸疑", "燒腦", "經典", "回憶", "一個人", "日常"],
            "story": "柯南電影系列第一部傳奇神作以4K高畫質重現大銀幕！經典的紅線剪斷選擇與摩天樓連環爆炸，充滿情懷。適合粉絲一個人去影廳回味最初的感動。",
            "theater": "威秀影城、秀泰影城、國賓影城"
        },
        {
            "title": "穿著Prada的惡魔2 (The Devil Wears Prada 2)",
            "genre": "劇情 / 喜劇 / 時尚",
            "style": ["放鬆", "職場", "喜劇", "幽默", "約會", "情侶"],
            "story": "經典時尚神作正宗續集。犀利幽默的對白再現職場生存學，劇情有笑有淚。非常適合職場受挫、被主管老闆罵的人來看片紓壓，也很適合情侶約會。",
            "theater": "威秀影城、誠品電影院、微風國賓"
        },

        # =================【 F. 溫馨親情 / 浪漫愛情 (誠品、威秀、秀泰)】=================
        {
            "title": "別離無恙 (Until We Meet Again)",
            "genre": "劇情 / 愛情 / 催淚",
            "style": ["難過", "傷心", "想哭", "哭爆", "浪漫", "失戀", "淚水"],
            "story": "目黑蓮、濱邊美波主演。探討生死告別的極致純愛催淚大作，情感極其細膩。失戀、分手或低潮時想哭爆釋放情緒的人必看。",
            "theater": "誠品電影院 (質感首選)、威秀影城、秀泰影城"
        },
        {
            "title": "你能吃到媽媽煮的飯的次數還剩365次",
            "genre": "劇情 / 溫馨 / 親情",
            "style": ["溫馨", "親情", "爸媽", "家人", "治癒", "陪伴", "感動"],
            "story": "改編自熱門感人小說。以獨特的數字視角計算兒女與父母相處的剩餘時間，溫暖催淚。最適合帶爸媽、長輩或全家人一起觀看。",
            "theater": "誠品電影院、光點華山電影館、國賓影城"
        },

        # =================【 G. 國際影展 / 本土紀錄片 / 文藝修復 (光點華山、誠品)】=================
        {
            "title": "單身動物園 (The Lobster) 數位重映",
            "genre": "劇情 / 奇幻 / 黑色幽默",
            "style": ["孤獨", "寂寞", "文藝", "深度", "思考", "邊緣", "單身"],
            "story": "經典反烏托邦神作重返大銀幕。不談戀愛就會變成動物的瘋狂設定，辛辣諷刺現代情感與單身主義。適合自己一個人、邊緣人深度品味。",
            "theater": "光點華山電影館 (藝文首選)、誠品電影院"
        },
        {
            "title": "末代皇帝（4K經典數位修復版）",
            "genre": "劇情 / 歷史 / 傳記",
            "style": ["文藝", "歷史", "深度", "深刻", "經典", "修復", "一個人"],
            "story": "影史奧斯卡九項大獎傳奇史詩。重現溥儀悲劇且壯麗的一生，坂本龍一的神級配樂在影廳重現，後勁極強。適合獨自一人靜靜享受歷史的深沉與孤獨感。",
            "theater": "光點華山電影館、誠品電影院、長春國賓"
        },
        {
            "title": "傳奇女伶高菊花 (La Paloma)",
            "genre": "紀錄片 / 傳記 / 歷史",
            "style": ["深刻", "難過", "生命", "低潮", "歷史", "獨立"],
            "story": "台灣歌手高菊花的重量級紀錄片。從女兒的視角挖掘史料，拼湊母親在體制與命運重壓下艱難生存的生存歷程。極具歷史厚度，看完令人低迴落淚。",
            "theater": "光點華山電影館 (獨家放映)、誠品電影院"
        },
        {
            "title": "甘露水 (Daughter of Nectar)",
            "genre": "紀錄片 / 藝術 / 歷史",
            "style": ["文藝", "深度", "心靈", "平淡", "日常", "生命"],
            "story": "圍繞台灣國寶級雕刻藝術作品《甘露水》背後的流轉、沉冤與重見天日的紀錄片。步調溫慢、充滿對台灣這片土地與藝術心靈的深刻凝視，極致療癒。",
            "theater": "光點華山電影館、誠品電影院"
        },
        {
            "title": "104歲哲代奶奶：一個人生活",
            "genre": "紀錄片 / 溫馨 / 日常",
            "style": ["療癒", "日常", "溫馨", "不舒服", "放鬆", "陪伴", "自己"],
            "story": "真實凝視哲代奶奶從101歲到104歲的生活。有孤單的面對也有充滿幽默的告別，展示生活哲學。非常適合日常疲勞、感到空虛時看，極度溫暖治癒。",
            "theater": "光點華山電影館、誠品電影院"
        },
        {
            "title": "經典大師：數位修復專題",
            "genre": "劇情 / 歷史 / 經典修復",
            "style": ["文藝", "歷史", "傳記", "懷舊", "一個人", "經典"],
            "story": "4K大銀幕重現影史傳奇大師的修復神作。深刻剖析人性、時代變遷與生命哲學。適合熱愛電影藝術、想一個人遠離世俗喧囂、安靜獨處的影迷。",
            "theater": "光點華山電影館 (修復電影大本營)、誠品電影院"
        }
    ]
    return database


# =========================================================
# 🎯 2. 智慧選片推薦引擎 (完全保留，不更動任何推薦影片程式碼)
# =========================================================
def recommend_movies_ultimate(user_input, movies):
    if not movies: return [], False
    user_input = user_input.lower()

    event_map = {
        "學業崩潰": ["被當", "重修", "二一", "期末考", "爆掉", "沒讀完", "報告", "延畢", "微積分", "當掉", "考試", "教授", "分數", "歐趴", "pass"],
        "職場受挫": ["被罵", "加班", "趕工", "開會", "提案", "扣薪", "奧客", "壞人", "小人", "豬隊友", "專案", "工作", "打卡", "上班", "主管", "老闆"],
        "生活幸運": ["中獎", "發票", "加薪", "請客", "撿到錢", "好運", "順利", "過關", "中頭獎", "買一送一", "幸運"],
        "情感變故": ["分手", "被甩", "失戀", "吵架", "冷戰", "已讀不回", "工具人", "好人卡", "綠綠的", "情傷", "變心", "前任"],
        "日常疲勞": ["塞車", "下大雨", "看醫生", "經痛", "失眠", "落枕", "排隊", "好累", "崩潰", "水逆", "倒楣", "累炸", "頭痛", "生病"]
    }
    companion_map = {
        "一個人": ["一個人", "獨享", "自己", "邊緣", "單身", "獨自", "單獨", "我邊緣", "宅在家", "沒人陪", "獨處"],
        "跟家人": ["家人", "父母", "爸媽", "帶小孩", "長輩", "兄弟姊妹", "家庭", "老爸", "老媽", "女兒", "兒子", "阿公", "阿媽", "闔家"],
        "跟朋友": ["朋友", "同學", "死黨", "閨蜜", "兄弟", "大家", "團體", "聚會", "室友", "學長", "學弟", "學姐", "學妹", "團康"],
        "喜歡的人": ["喜歡的人", "閃光", "閃", "暗戀", "曖昧", "約會", "女友", "男友", "情侶", "老婆", "老公", "對象", "寶貝", "另一半"]
    }
    mood_map = {
        "憂鬱": ["憂鬱", "鬱悶", "沮喪", "低潮", "寂寞", "孤單", "無力", "藍過", "提不起勁", "無聊", "空虛", "自閉", "大師", "李滄東"],
        "煩躁": ["煩躁", "煩", "不爽", "壓力大", "暴怒", "氣死", "傻眼", "阿雜", "想打人", "抓狂", "躁鬱", "超煩"],
        "興奮": ["興奮", "期待", "熱血", "爽片", "刺激", "爆破", "震撼", "嗨", "推", "極速", "狂熱"],
        "開心": ["開心", "快樂", "放鬆", "歡樂", "好笑", "搞笑", "幽默", "放空", "舒壓", "哈哈"],
        "難過": ["難過", "傷心", "想哭", "哭爆", "心碎", "痛哭", "落淚", "悲傷", "好慘"],
        "不舒服": ["不舒服", "累", "疲憊", "悶", "療癒", "溫馨", "溫慢", "溫暖", "需要安慰"]
    }

    style_targets = {
        "憂鬱": ["療癒", "心靈", "文藝", "平淡", "深沉", "溫馨", "正能量", "陪伴", "李滄東"],
        "煩躁": ["爽片", "刺激", "發洩", "動作", "飛車", "打鬥", "無尿點"],
        "興奮": ["熱血", "震撼", "大片", "科幻", "巨幕", "冒險", "期待"],
        "開心": ["放鬆", "歡樂", "卡通", "喜劇", "爆笑", "幽默", "哈哈"],
        "難過": ["難過", "傷心", "淚水", "失戀", "低潮", "深刻", "情傷", "想哭", "哭爆", "痛苦"],
        "不舒服": ["放鬆", "不燒腦", "療癒", "溫馨", "卡通", "日常", "陪伴"],
        "學業崩潰": ["爽片", "發洩", "歡樂", "爆笑", "放鬆", "動作"],
        "職場受挫": ["爽片", "刺激", "發洩", "動作", "職場", "喜劇"],
        "生活幸運": ["熱血", "震撼", "大片", "娛樂", "歡樂", "期待"],
        "情感變故": ["難過", "傷心", "淚水", "失戀", "情傷", "療癒", "浪漫", "愛情"],
        "日常疲勞": ["放鬆", "不燒腦", "卡通", "療癒", "溫馨", "日常"],
        "一個人": ["孤獨", "寂寞", "深度", "文藝", "深沉", "經典", "懸疑", "思考", "自己", "邊緣", "獨自", "李滄東"],
        "跟家人": ["闔家觀賞", "卡通", "溫馨", "歡樂", "放鬆", "喜劇", "親情", "爸媽", "家人"],
        "跟朋友": ["同學", "死黨", "朋友", "聚會", "爽片", "恐怖", "鬼片", "驚悚", "刺激"],
        "喜歡的人": ["約會", "浪漫", "愛情", "娛樂", "情侶", "喜劇"]
    }

    matched_events = [cat for cat, words in event_map.items() if any(w in user_input for w in words)]
    matched_companions = [cat for cat, words in companion_map.items() if any(w in user_input for w in words)]
    matched_moods = [cat for cat, words in mood_map.items() if any(w in user_input for w in words)]

    if any(k in user_input for k in ["李滄東", "大師", "影展", "文藝"]): matched_moods.append("憂鬱")
    if "學業崩潰" in matched_events or "職場受挫" in matched_events: matched_moods.append("煩躁")
    if "情感變故" in matched_events: matched_moods.append("難過")

    recommended = []
    for movie in movies:
        score = 0
        movie_text = (movie['title'] + movie['genre'] + movie['story']).lower()
        movie_styles = movie['style']
        
        if user_input in movie_text: score += 30
            
        for mood in set(matched_moods):
            for target in style_targets.get(mood, []):
                if target in movie_styles: score += 6
                if target in movie_text: score += 2
                    
        for comp in set(matched_companions):
            for target in style_targets.get(comp, []):
                if target in movie_styles: score += 8
                if target in movie_text: score += 3
                    
        for event in set(matched_events):
            for target in style_targets.get(event, []):
                if target in movie_styles: score += 6
                if target in movie_text: score += 2

        if score > 0: recommended.append((movie, score))

    if not recommended:
        for movie in movies:
            score = 0
            movie_text = (movie['title'] + movie['genre'] + movie['story']).lower()
            for char in user_input:
                if char in movie_text and char not in "，。！？ 的是我在:；、": score += 1
            if score > 1: recommended.append((movie, score))

    recommended.sort(key=lambda x: x[1], reverse=True)
    return [item[0] for item in recommended], len(recommended) > 0


# =========================================================
# 🎨 3. UI 裝飾：膠捲＋電影院風格（只改介面，不動其他邏輯）
# =========================================================
st.set_page_config(page_title="大台北電影智慧推薦", page_icon="🎬", layout="centered")

st.markdown("""
    <style>
    /* =========================================================
       0. 全域背景：電影院黑紅色調 + 投影感
    ========================================================= */
    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(circle at 50% 8%, rgba(255,255,255,0.08) 0%, transparent 20%),
            radial-gradient(circle at 50% 100%, rgba(185, 28, 28, 0.10) 0%, transparent 28%),
            linear-gradient(180deg, #240303 0%, #0c0c10 38%, #06070b 100%) !important;
        position: relative !important;
        overflow-x: hidden !important;
    }

    /* 左右固定膠捲裝飾 */
    [data-testid="stAppViewContainer"]::before,
    [data-testid="stAppViewContainer"]::after {
        content: "";
        position: fixed;
        top: 14px;
        bottom: 14px;
        width: 88px;
        z-index: 0;
        border-radius: 16px;
        border: 3px solid #111111;
        box-shadow: inset 0 0 25px rgba(0,0,0,0.85), 0 0 18px rgba(0,0,0,0.35);
        background:
            radial-gradient(circle at 12px 20px, #0a0a0a 0 6px, transparent 7px),
            radial-gradient(circle at calc(100% - 12px) 20px, #0a0a0a 0 6px, transparent 7px),
            linear-gradient(180deg, #8f0a0a 0%, #470303 55%, #250202 100%);
        background-size: 100% 42px, 100% 42px, 100% 100%;
        background-repeat: repeat-y, repeat-y, no-repeat;
        opacity: 0.95;
        pointer-events: none;
    }

    [data-testid="stAppViewContainer"]::before { left: 14px; }
    [data-testid="stAppViewContainer"]::after  { right: 14px; }

    /* 主要內容區維持在裝飾之上 */
    .block-container {
        position: relative;
        z-index: 2;
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }

    /* =========================================================
       1. 側邊欄：電影院紅色布幕感 + 可上下滾動
    ========================================================= */
    [data-testid="stSidebar"] {
        background:
            linear-gradient(90deg, rgba(0,0,0,0.55) 0%, transparent 12%, transparent 88%, rgba(0,0,0,0.55) 100%),
            repeating-linear-gradient(
                90deg,
                #2b0208 0px,
                #5f0716 18px,
                #8b1024 34px,
                #5f0716 52px,
                #2b0208 70px
            ) !important;
        position: relative !important;
        box-shadow: 8px 0 30px rgba(0,0,0,0.9) !important;
        overflow: hidden !important;
    }

    /* 讓側邊欄內容可以上下滾動 */
    [data-testid="stSidebarContent"] {
        max-height: 100vh !important;
        overflow-y: auto !important;
        overflow-x: hidden !important;
        padding-bottom: 48px !important;
        background:
            radial-gradient(circle at 50% 0%, rgba(255,255,255,0.10) 0%, transparent 26%),
            linear-gradient(180deg, rgba(40,0,8,0.15) 0%, rgba(0,0,0,0.35) 100%) !important;
        position: relative !important;
        z-index: 2 !important;
    }

    /* 側邊欄捲軸：細版金色，不會破壞布幕感 */
    [data-testid="stSidebarContent"]::-webkit-scrollbar {
        width: 8px;
    }

    [data-testid="stSidebarContent"]::-webkit-scrollbar-track {
        background: rgba(0,0,0,0.35);
        border-radius: 999px;
    }

    [data-testid="stSidebarContent"]::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #fbbf24 0%, #b45309 100%);
        border-radius: 999px;
    }

    [data-testid="stSidebarContent"]::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #fde68a 0%, #d97706 100%);
    }

    /* 布幕上方暗影，像舞台簾幕垂下來 */
    [data-testid="stSidebar"] .stSidebar::before {
        content: none;
    }

    /* 右排劇院燈泡 */
    [data-testid="stSidebar"]::after {
        content: "";
        position: absolute;
        right: 0;
        top: 0;
        bottom: 0;
        width: 16px;
        background-image: radial-gradient(circle, #fbbf24 34%, #7c2d12 38%, transparent 44%);
        background-size: 16px 30px;
        background-repeat: repeat-y;
        border-left: 1px solid rgba(251, 191, 36, 0.35);
        box-shadow: -4px 0 12px rgba(0,0,0,0.35);
        z-index: 3;
        pointer-events: none;
    }

    /* 左排劇院燈泡 */
    [data-testid="stSidebar"]::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 16px;
        background-image: radial-gradient(circle, #fbbf24 34%, #7c2d12 38%, transparent 44%);
        background-size: 16px 30px;
        background-repeat: repeat-y;
        border-right: 1px solid rgba(251, 191, 36, 0.35);
        box-shadow: 4px 0 12px rgba(0,0,0,0.35);
        z-index: 3;
        pointer-events: none;
    }

    .sidebar-section {
        background:
            linear-gradient(180deg, rgba(0, 0, 0, 0.62) 0%, rgba(20, 5, 8, 0.72) 100%) !important;
        border: 1px solid rgba(251, 191, 36, 0.78) !important;
        border-radius: 14px;
        padding: 16px;
        margin: 0 18px 22px 18px;
        box-shadow:
            0 5px 16px rgba(0,0,0,0.65),
            inset 0 0 16px rgba(255,255,255,0.035);
        backdrop-filter: blur(3px);
    }

    .sidebar-title {
        color: #ffffff !important;
        font-size: 1.15rem;
        font-weight: 900;
        margin-bottom: 12px;
        border-bottom: 1px dashed rgba(251, 191, 36, 0.85);
        padding-bottom: 6px;
        text-shadow: 0 0 6px rgba(245, 158, 11, 0.55), 2px 2px 3px rgba(0,0,0,0.75);
    }

    .sidebar-text {
        color: #f9fafb !important;
        font-size: 0.95rem;
        line-height: 1.6;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.65);
    }

    .pulse-container {
        display: flex;
        align-items: center;
        margin-bottom: 8px;
    }

    .pulse-dot {
        width: 10px;
        height: 10px;
        background: #22c55e;
        border-radius: 50%;
        margin-right: 10px;
        box-shadow: 0 0 8px #22c55e;
    }


    /* =========================================================
       2. 主視覺看板：更吸睛的電影招牌 / 膠捲票券感
    ========================================================= */
    .broadway-marquee-box {
        background:
            linear-gradient(90deg, rgba(0,0,0,0.94) 0%, rgba(70, 0, 0, 0.94) 16%, rgba(160, 0, 0, 0.98) 50%, rgba(70, 0, 0, 0.94) 84%, rgba(0,0,0,0.94) 100%) !important;
        border: 4px solid #0a0a0a !important;
        border-radius: 24px;
        padding: 36px 30px 32px 30px;
        text-align: center;
        box-shadow:
            0 0 0 4px rgba(245, 158, 11, 0.35),
            0 0 34px rgba(220, 38, 38, 0.48),
            0 0 72px rgba(0,0,0,0.78),
            inset 0 0 22px rgba(255,255,255,0.08),
            inset 0 0 42px rgba(0,0,0,0.78);
        margin-bottom: 38px;
        position: relative;
        overflow: hidden;
    }

    /* 外層像電影票券的虛線框 */
    .broadway-marquee-box::before {
        content: "";
        position: absolute;
        inset: 14px;
        border: 2px dashed rgba(251, 191, 36, 0.62);
        border-radius: 16px;
        pointer-events: none;
        box-shadow: inset 0 0 20px rgba(0,0,0,0.45);
    }

    /* 中央舞台聚光，讓標題更亮 */
    .broadway-marquee-box::after {
        content: "";
        position: absolute;
        left: 50%;
        top: 50%;
        width: 86%;
        height: 130%;
        transform: translate(-50%, -50%);
        background: radial-gradient(circle, rgba(255,255,255,0.16) 0%, rgba(245,158,11,0.10) 27%, transparent 68%);
        pointer-events: none;
        z-index: 0;
    }

    .broadway-marquee-box * {
        position: relative;
        z-index: 1;
    }

    /* 上方小標籤：像正在上映的電影招牌 */
    .cinema-kicker {
        display: inline-block;
        color: #fff7ed !important;
        background: rgba(0,0,0,0.52);
        border: 1px solid rgba(245, 158, 11, 0.82);
        border-radius: 999px;
        padding: 6px 18px;
        font-size: 0.92rem;
        font-weight: 900;
        letter-spacing: 2px;
        margin-bottom: 14px;
        box-shadow: 0 0 14px rgba(245, 158, 11, 0.28);
    }

    .marquee-main-title {
        color: #ffffff !important;
        font-size: 2.62rem !important;
        font-weight: 1000 !important;
        letter-spacing: 2.4px;
        margin: 0 0 12px 0 !important;
        line-height: 1.18;
        text-shadow:
            0 3px 0 #3b0303,
            0 0 10px rgba(255,255,255,0.38),
            0 0 24px rgba(245,158,11,0.45),
            0 0 40px rgba(220,38,38,0.52);
    }

    .title-highlight {
        color: #fbbf24 !important;
        text-shadow:
            0 2px 0 #451a03,
            0 0 12px rgba(251,191,36,0.88),
            0 0 30px rgba(251,191,36,0.58);
    }

    .marquee-sub-title {
        color: #f8fafc !important;
        font-size: 1.08rem !important;
        font-weight: 800 !important;
        line-height: 1.7;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.9);
        margin-top: 4px;
    }

    /* 下方膠捲小燈點 */
    .film-dot-row {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 18px;
    }

    .film-dot-row span {
        display: block;
        width: 12px;
        height: 12px;
        background: #fbbf24;
        border-radius: 3px;
        box-shadow: 0 0 10px rgba(251,191,36,0.85);
    }

    /* =========================================================
       3. 輸入框區塊：清楚可辨識優先
    ========================================================= */
    div[data-testid="stTextInput"] {
        background: rgba(8, 10, 16, 0.82) !important;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid rgba(220, 38, 38, 0.50);
        box-shadow: 0 10px 24px rgba(0,0,0,0.42);
        backdrop-filter: blur(4px);
    }

    div[data-testid="stTextInput"] label p {
        color: #bfdbfe !important;
        font-size: 1.28rem !important;
        font-weight: 900 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9) !important;
        letter-spacing: 0.6px;
    }

    div[data-testid="stTextInput"] input {
        background-color: #111827 !important;
        color: #ffffff !important;
        font-size: 1.12rem !important;
        font-weight: 700 !important;
        border: 2px solid #b91c1c !important;
        border-radius: 10px !important;
        padding: 12px !important;
        transition: all 0.3s ease;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #60a5fa !important;
        box-shadow: 0 0 0 2px rgba(96, 165, 250, 0.22), 0 0 14px rgba(96, 165, 250, 0.32) !important;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: #cbd5e1 !important;
        opacity: 0.95 !important;
        font-weight: 600;
    }


    /* =========================================================
       4. 按鈕：電影票 / 海報風格
    ========================================================= */
    div.stButton > button {
        background: linear-gradient(180deg, #dc2626 0%, #991b1b 100%) !important;
        color: #ffffff !important;
        font-weight: 900 !important;
        font-size: 1.18rem !important;
        border: 2px solid #f59e0b !important;
        border-radius: 30px !important;
        padding: 10px 24px !important;
        box-shadow: 0 4px 15px rgba(127, 29, 29, 0.45) !important;
        width: 100%;
        letter-spacing: 1.5px;
        transition: all 0.25s ease-in-out;
    }

    div.stButton > button:hover {
        transform: translateY(-2px) scale(1.01);
        background: linear-gradient(180deg, #ef4444 0%, #b91c1c 100%) !important;
        box-shadow: 0 8px 22px rgba(245, 158, 11, 0.25) !important;
        color: #fff7ed !important;
    }


    /* =========================================================
       5. 推薦結果卡片：黑底紅框，字清楚
    ========================================================= */
    div[data-testid="stExpander"] {
        background: linear-gradient(180deg, rgba(9, 10, 14, 0.96) 0%, rgba(15, 20, 34, 0.96) 100%) !important;
        border: 1px solid rgba(245, 158, 11, 0.50) !important;
        border-left: 8px solid #b91c1c !important;
        border-radius: 12px !important;
        box-shadow: 0 8px 22px rgba(0,0,0,0.55) !important;
        overflow: hidden;
    }

    div[data-testid="stExpander"] summary {
        background: linear-gradient(90deg, rgba(64,0,0,0.85) 0%, rgba(10,10,10,0.35) 100%);
        padding-top: 10px !important;
        padding-bottom: 10px !important;
    }

    /* 推薦影片 title：改成有底色的醒目票券框 */
    div[data-testid="stExpander"] summary p {
        display: inline-block !important;
        background: linear-gradient(90deg, #fbbf24 0%, #f97316 45%, #b91c1c 100%) !important;
        color: #111827 !important;
        font-weight: 1000 !important;
        font-size: 1.22rem !important;
        padding: 7px 14px !important;
        border-radius: 999px !important;
        border: 2px solid rgba(255,255,255,0.85) !important;
        box-shadow: 0 0 14px rgba(251,191,36,0.32) !important;
        text-shadow: none !important;
        letter-spacing: 0.4px;
    }

    .movie-detail-text {
        color: #f9fafb !important;
        font-size: 1.08rem !important;
        line-height: 1.85 !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.45);
    }

    .movie-detail-tag {
        color: #fbbf24 !important;
        font-weight: 900 !important;
    }


    /* =========================================================
       6. 提示訊息字體可讀性
    ========================================================= */
    [data-testid="stAlertContainer"] {
        border-radius: 12px !important;
    }

    [data-testid="stMarkdownContainer"] p,
    .stMarkdown p {
        color: inherit;
    }


    /* =========================================================
       7. 手機 / 小螢幕：避免左右膠捲太擠
    ========================================================= */
    @media (max-width: 1100px) {
        [data-testid="stAppViewContainer"]::before,
        [data-testid="stAppViewContainer"]::after {
            width: 56px;
            opacity: 0.55;
        }
    }

    @media (max-width: 760px) {
        [data-testid="stAppViewContainer"]::before,
        [data-testid="stAppViewContainer"]::after {
            display: none;
        }

        .marquee-main-title {
            font-size: 1.8rem !important;
        }

        .marquee-sub-title {
            font-size: 0.96rem !important;
        }

        .cinema-kicker {
            font-size: 0.78rem !important;
            letter-spacing: 1px;
        }

        .film-dot-row span {
            width: 9px;
            height: 9px;
        }

        div[data-testid="stTextInput"] label p {
            font-size: 1.1rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)


# =========================================================
# 🗂️ 4. 側邊功能導覽列 (100% 保持您滿意的外觀與功能)
# =========================================================
with st.sidebar:
    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="sidebar-section">
            <div class="sidebar-title">🍿 台北華麗巨幕影廳</div>
            <div class="sidebar-text">
                本系統專為台北影迷打造，全面收錄 <b>威秀、光點華山、誠品、秀泰、國賓</b> 等 2026 年 5 月當期最強檔片單。
            </div>
        </div>
        <div class="sidebar-section">
            <div class="sidebar-title">🎥 影展焦點預告片</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.video("https://www.youtube.com/watch?v=oho89asI5S4")
    
    st.markdown("""
        <div class="sidebar-section">
            <div class="sidebar-title">💡 雙向生活字典範例</div>
            <div class="sidebar-text">
                • <b>課業/職場</b>：輸入「期末考爆掉、主管罵人」<br>
                • <b>同伴/伴侶</b>：輸入「自己一個人、情侶約會」<br>
                • <b>核心意圖</b>：輸入「李滄東大師、大場面飆車」
            </div>
        </div>

        <div class="sidebar-section">
            <div class="sidebar-title">⚡ 院線即時票務連線</div>
            <div class="pulse-container">
                <div class="pulse-dot"></div>
                <div class="sidebar-text"><b>大台北威秀影城：線上運作中</b></div>
            </div>
            <div class="pulse-container">
                <div class="pulse-dot"></div>
                <div class="sidebar-text"><b>光點華山/誠品院線：影展同步中</b></div>
            </div>
            <div class="pulse-container">
                <div class="pulse-dot"></div>
                <div class="sidebar-text"><b>西門秀泰/國賓大戲院：資料正常</b></div>
            </div>
        </div>
    """, unsafe_allow_html=True)


# =========================================================
# 🎫 5. 主頁面核心呈現（修改標題與一般化提示用語）
# =========================================================
# 看板大標題（已修正為您要求的名稱）
st.markdown("""
    <div class="broadway-marquee-box">
        <div class="cinema-kicker">NOW SHOWING・TAIPEI CINEMA</div>
        <h1 class="marquee-main-title">🎬 台北影城智慧<span class="title-highlight">電影</span>推薦系統</h1>
        <div class="marquee-sub-title">🎟️ 2026年5月完全體版｜生活情境矩陣核心 × 五大實體院線熱映片單</div>
        <div class="film-dot-row">
            <span></span><span></span><span></span><span></span><span></span><span></span><span></span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 輸入框（已修正為一般平常的說法）
user_input = st.text_input(
    "🛎️ 請輸入您目前的狀態、心情或想尋找的電影關鍵字：", 
    placeholder="在此輸入情境（例如：期末考爆掉、情侶約會放鬆、我想看李滄東...）"
)

st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

# 按鈕文字（已修正）
if st.button("🎟️ 開始電影推薦"):
    if user_input.strip() == "":
        st.warning("請先輸入您的情境或電影關鍵字後再點擊啟動喔！")
    else:
        movie_db = get_absolute_comprehensive_database_2026()
        
        # 這是您的推薦演算法核心，100% 完整保留，完全沒有更動
        recommended, is_matched = recommend_movies_ultimate(user_input, movie_db)

        if not is_matched or not recommended:
            st.error("😭 抱歉，目前沒找到符合您當前情境的電影，要不要換種心情或關鍵字試試看？")
        else:
            st.markdown(f"<h3 style='color: #22c55e; font-weight: bold; text-shadow: 1px 1px 2px #000;'>🧠 系統成功對應情境！為您推薦以下 {len(recommended)} 部適合的片單：</h3>", unsafe_allow_html=True)
            
            for m in recommended:
                with st.expander(f"🍿 {m['title']}", expanded=True):
                    st.markdown(f"""
                        <div class="movie-detail-text">
                            <span class="movie-detail-tag">🎭 電影類型：</span>{m['genre']}<br>
                            <span class="movie-detail-tag">📍 上映影城：</span>{m['theater']}<br>
                            <span class="movie-detail-tag">📝 劇情簡介與情境推薦：</span>{m['story']}
                        </div>
                    """, unsafe_allow_html=True)
