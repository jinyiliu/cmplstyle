CH_BASE_COLORS = {}

BASE_COLORS_EN_TO_CH = {}

CH_TRAD_COLORS = {}

TRAD_COLORS_EN_TO_CH = {}

WHITE_COLORS_CH = {
    "缟羽": "#efefef", # 郭浩《中国传统色：故宫里的色彩美学》
    "浅云": "#eaeef1", # 郭浩《中国传统色：故宫里的色彩美学》
    "银白": "#eff0f1",
    "鹄白": "#ebeef0",
    "羊绒": "#eaebeb",
    "葱白": "#ebeee8", # 和同色系皦玉共用一个色值
    "蛤粉": "#ebeee1",
    "白垩": "#e0e1d9",
    "缟素": "#e6e6dc",
    "象牙": "#eeeadc",
    "米汤娇": "#eeead9", # 郭浩《中国传统色：故宫里的色彩美学》
    "蜜合": "#dfd7c2", # 郭浩《中国传统色：故宫里的色彩美学》
    "乳白": "#fffef3",
    "凝脂": "#f5f2e9", # 郭浩《中国传统色：故宫里的色彩美学》
    "山矾": "#f5f3f2", # 郭浩《中国传统色：故宫里的色彩美学》
    "玉頩": "#eae5e3", # 郭浩《中国传统色：故宫里的色彩美学》
    "芡食白": "#e2e1e4",
    "葭灰": "#beb1aa", # 郭浩《中国传统色：故宫里的色彩美学》
    "汉白玉": "#f8f4ed",
    "荷花白": "#fbecde",
    "蚌肉白": "#f9f1db",
    "荔肉白": "#f2e6ce",
    "米色": "#f9e9cd",
    "菊蕾白": "#e9ddb6",
    "酂白": "#f6f9e4", # 郭浩《中国传统色：故宫里的色彩美学》
    "皦玉": "#ebeee8", # 郭浩《中国传统色：故宫里的色彩美学》
    "吉量": "#ebeddf", # 郭浩《中国传统色：故宫里的色彩美学》
    "天球": "#e0dfc6", # 郭浩《中国传统色：故宫里的色彩美学》
    "韶粉": "#e0e0d0", # 郭浩《中国传统色：故宫里的色彩美学》
    "二目鱼": "#dfe0d9", # 郭浩《中国传统色：故宫里的色彩美学》
    "明月珰": "#d4d3ca", # 郭浩《中国传统色：故宫里的色彩美学》
    "霜地": "#c7c6b6", # 郭浩《中国传统色：故宫里的色彩美学》
    "溶溶月": "#bec2bc", # 郭浩《中国传统色：故宫里的色彩美学》
    "余白": "#c9cfc1", # 郭浩《中国传统色：故宫里的色彩美学》
    "草白": "#bfc1a9", # 郭浩《中国传统色：故宫里的色彩美学》
    "豆白": "#d5e0d5",
    "东方既白": "#f5fefb",
    "甜白": "#eceff4",
    "卵白": "#e4ecf0",
    "荻色": "#dfe5e8",
    "素采": "#d4dde1", # 郭浩《中国传统色：故宫里的色彩美学》
    "月白": "#d4e5ef", # 郭浩《中国传统色：故宫里的色彩美学》
    "云峰白": "#d8e3e7",
    "鱼肚白": "#c8d0d3",
    "影青": "#bdcbd2", # 郭浩《中国传统色：故宫里的色彩美学》
    "逍遥游": "#b2bfc3", # 郭浩《中国传统色：故宫里的色彩美学》
    "白青": "#98b6c2", # 郭浩《中国传统色：故宫里的色彩美学》
    "青鸾": "#9aa7b1", # 郭浩《中国传统色：故宫里的色彩美学》

    "天缥": "#d5ebe1", # 郭浩《中国传统色：故宫里的色彩美学》
    "绍衣": "#a8a19c", # 郭浩《中国传统色：故宫里的色彩美学》
    "仙米": "#d4c9aa", # 郭浩《中国传统色：故宫里的色彩美学》
    "筠雾": "#d5d1ae", # 郭浩《中国传统色：故宫里的色彩美学》
    "月魄": "#b2b6b6", # 郭浩《中国传统色：故宫里的色彩美学》
    "不皂": "#a7aaa1", # 郭浩《中国传统色：故宫里的色彩美学》
    "香皮": "#d8d1c5", # 郭浩《中国传统色：故宫里的色彩美学》
    "云母": "#c6beb1", # 郭浩《中国传统色：故宫里的色彩美学》
    "佩玖": "#ac9f8a", # 郭浩《中国传统色：故宫里的色彩美学》
    "玉色": "#eae4d1", # 郭浩《中国传统色：故宫里的色彩美学》
    "黄润": "#dfd6B8", # 郭浩《中国传统色：故宫里的色彩美学》
    "缣缃": "#d5c8a0", # 郭浩《中国传统色：故宫里的色彩美学》
    "蕉月": "#86908a", # 郭浩《中国传统色：故宫里的色彩美学》
    "藕丝秋半": "#d3cbc5", # 郭浩《中国传统色：故宫里的色彩美学》
    "黄粱": "#c4b798", # 郭浩《中国传统色：故宫里的色彩美学》
    "弗肯红": "#ecd9c7", # 郭浩《中国传统色：故宫里的色彩美学》
    "甘石": "#bdb2b2", # 郭浩《中国传统色：故宫里的色彩美学》
    "假山南": "#d4c1a6", # 郭浩《中国传统色：故宫里的色彩美学》
    "骨缥": "#ebe3c7", # 郭浩《中国传统色：故宫里的色彩美学》
    "青白玉": "#cac5a0", # 郭浩《中国传统色：故宫里的色彩美学》

}

BLACK_COLORS_CH = {
    "雷雨垂": "#7a7b78", # 郭浩《中国传统色：故宫里的色彩美学》
    "石涅": "#686a67", # 郭浩《中国传统色：故宫里的色彩美学》
    "墨朱": "#70695d", # 郭浩《中国传统色：故宫里的色彩美学》
    "沙石": "#69635d",
    "墨黲": "#585248", # 郭浩《中国传统色：故宫里的色彩美学》
    "鸭雏": "#483d34",
    "驖骊": "#46433b", # 郭浩《中国传统色：故宫里的色彩美学》
    "青骊": "#422517", # 郭浩《中国传统色：故宫里的色彩美学》
    "金青": "#46443b",
    "茶青": "#3f3b31",
    "京元": "#31322c", # 郭浩《中国传统色：故宫里的色彩美学》
    "铁棕": "#1a0404",
    "铁色": "#595861",
    "黪墨": "#625d6b",
    "玄天": "#6b5458", # 郭浩《中国传统色：故宫里的色彩美学》
    "烟墨": "#5c4f55", # 郭浩《中国传统色：故宫里的色彩美学》
    "紫鼠": "#594c57", # 郭浩《中国传统色：故宫里的色彩美学》
    "曾青": "#535164", # 郭浩《中国传统色：故宫里的色彩美学》
    "青黛": "#45465e", # 郭浩《中国传统色：故宫里的色彩美学》
    "䒌靘": "#454659", # 郭浩《中国传统色：故宫里的色彩美学》
    "青雀头黛": "#354e6b", # 郭浩《中国传统色：故宫里的色彩美学》
    "育阳染": "#576470", # 郭浩《中国传统色：故宫里的色彩美学》
    "霁蓝": "#3c4654", # 郭浩《中国传统色：故宫里的色彩美学》
    "骐驎": "#12264f", # 郭浩《中国传统色：故宫里的色彩美学》
    "油烟墨": "#3f3f3c",
    "绿云": "#45493d", # 郭浩《中国传统色：故宫里的色彩美学》
    "蒽油绿": "#373834",
    "老绿": "#1c2d29",
    "墨绿": "#1c2d25",
    "苷蓝绿": "#1f2623",
    "云杉绿": "#15231b",
    "螺子黛": "#13393e", # 郭浩《中国传统色：故宫里的色彩美学》
    "鹰背": "#39363f",
    "朱墨": "#2d2d30",
    "石青": "#2e282e",
    "墨紫": "#281d2c",
    "火薰": "#2f3243",
    "真青": "#192841",
    "花青": "#1a2847",
    "璆琳": "#343041", # 郭浩《中国传统色：故宫里的色彩美学》
    "鼎灰": "#36292f",
    "绀蝶": "#2c2f3b", # 郭浩《中国传统色：故宫里的色彩美学》
    "暗龙胆紫": "#22202e",
    "瑾瑜": "#1e2732", # 郭浩《中国传统色：故宫里的色彩美学》
    "元青": "#28292b",
    "袀玄": "#262729",
    "燕尾青": "#131423",
    "獺见": "#151d29", # 郭浩《中国传统色：故宫里的色彩美学》

    "菘蓝": "#6b798e", # 郭浩《中国传统色：故宫里的色彩美学》
    "濯绛": "#796860", # 郭浩《中国传统色：故宫里的色彩美学》
}

RED_COLORS_CH = {
    "小红": "#e67762", # 郭浩《中国传统色：故宫里的色彩美学》
    "抹红": "#de694c",
    "骍衣": "#ea5532",
    "朱膘": "#e94721",
    "鹤顶红": "#d24735", # 郭浩《中国传统色：故宫里的色彩美学》
    "杏红": "#cf3d15",
    "珊瑚": "#ca462f",
    "银朱": "#d12920", # 郭浩《中国传统色：故宫里的色彩美学》
    "火赫": "#bf301e",
    "珊瑚赫": "#c12c1f", # 郭浩《中国传统色：故宫里的色彩美学》
    "蕉红": "#c8191d",
    "牙红": "#b01f24",
    "岱赭": "#dd6b4f", # 郭浩《中国传统色：故宫里的色彩美学》
    "赩炽": "#cb523e", # 郭浩《中国传统色：故宫里的色彩美学》
    "朱殷": "#b93a26", # 郭浩《中国传统色：故宫里的色彩美学》
    "石榴裙": "#b13b2e", # 郭浩《中国传统色：故宫里的色彩美学》
    "绛红": "#b02e28",
    "赤缇": "#ba5b49", # 郭浩《中国传统色：故宫里的色彩美学》
    "纁黄": "#ba5140", # 郭浩《中国传统色：故宫里的色彩美学》
    "朱草": "#a64036", # 郭浩《中国传统色：故宫里的色彩美学》
    "綪茷": "#9e2a22", # 郭浩《中国传统色：故宫里的色彩美学》
    "朱湛": "#95302e", # 郭浩《中国传统色：故宫里的色彩美学》
    "朱樱": "#8f1d22", # 郭浩《中国传统色：故宫里的色彩美学》
    "大繎": "#822327", # 郭浩《中国传统色：故宫里的色彩美学》
    "丹色": "#d64241",
    "翘红": "#e9464d",
    "朱砂": "#d80835",
    "双红": "#c02a45",
    "胭脂": "#b32142",
    "红椒": "#e02623",
    "丹枫": "#d81918",
    "丹罽": "#e60012", # 郭浩《中国传统色：故宫里的色彩美学》
    "丹臒": "#c8161d", # 郭浩《中国传统色：故宫里的色彩美学》
    "胭脂虫": "#ab1d22", # 郭浩《中国传统色：故宫里的色彩美学》
    "水华朱": "#a72126", # 郭浩《中国传统色：故宫里的色彩美学》
    "顺圣": "#7c191e", # 郭浩《中国传统色：故宫里的色彩美学》
    "茜红": "#cc5d4e",
    "绯红": "#bf5552",
    "佛赤": "#8f3d2c", # 郭浩《中国传统色：故宫里的色彩美学》
    "枣红": "#8a2623",
    "荔色": "#89262c",
    "朱红": "#711318",
    "不老红": "#702029",
    "爵头": "#631216", # 郭浩《中国传统色：故宫里的色彩美学》
    "燃红": "#5d181a",
    "木兰": "#662b1f", # 郭浩《中国传统色：故宫里的色彩美学》
    "麒麟竭": "#4c1e1a", # 郭浩《中国传统色：故宫里的色彩美学》

    "缙云": "#ee7959", # 郭浩《中国传统色：故宫里的色彩美学》
    "老僧衣": "#a46244", # 郭浩《中国传统色：故宫里的色彩美学》
    "缊韨": "#984f31", # 郭浩《中国传统色：故宫里的色彩美学》
    "洛神朱": "#d23918", # 郭浩《中国传统色：故宫里的色彩美学》
    "朱颜酡": "#f29a76", # 郭浩《中国传统色：故宫里的色彩美学》
    "檎丹": "#e94829", # 郭浩《中国传统色：故宫里的色彩美学》
    "赤灵": "#954024", # 郭浩《中国传统色：故宫里的色彩美学》
    "丹秫": "#873424", # 郭浩《中国传统色：故宫里的色彩美学》
    "霁红": "#7c4449", # 郭浩《中国传统色：故宫里的色彩美学》
}

YELLOW_COLORS_CH = {
    "半见": "#fffbc7", # 郭浩《中国传统色：故宫里的色彩美学》
    "女贞黄": "#f7eead", # 郭浩《中国传统色：故宫里的色彩美学》
    "莺儿": "#ebe1a9", # 郭浩《中国传统色：故宫里的色彩美学》
    "绢纨": "#ece093", # 郭浩《中国传统色：故宫里的色彩美学》
    "禹余粮": "#e1d279", # 郭浩《中国传统色：故宫里的色彩美学》
    "田赤": "#e1d384", # 郭浩《中国传统色：故宫里的色彩美学》
    "姜黄": "#d6c560", # 郭浩《中国传统色：故宫里的色彩美学》
    "姚黄": "#d6bc46", # 郭浩《中国传统色：故宫里的色彩美学》
    "黄封": "#cab272", # 郭浩《中国传统色：故宫里的色彩美学》
    "栾华": "#c0ad5e", # 郭浩《中国传统色：故宫里的色彩美学》
    "大赤": "#aa9649", # 郭浩《中国传统色：故宫里的色彩美学》
    "苍黄": "#b6a014", # 郭浩《中国传统色：故宫里的色彩美学》
    "黄白游": "#fff799", # 郭浩《中国传统色：故宫里的色彩美学》
    "松花": "#ffee6f", # 郭浩《中国传统色：故宫里的色彩美学》
    "缃叶": "#ecd452", # 郭浩《中国传统色：故宫里的色彩美学》
    "槐黄": "#d6bb38",
    "草黄": "#d2b42c",
    "矫黄": "#daa91f",
    "金黄": "#d3a117",
    "鞠衣": "#d3a237", # 郭浩《中国传统色：故宫里的色彩美学》
    "太一余粮": "#d5b45c", # 郭浩《中国传统色：故宫里的色彩美学》
    "秋香": "#bf9c46", # 郭浩《中国传统色：故宫里的色彩美学》
    "香色": "#b69833",
    "老茯神": "#aa8534", # 郭浩《中国传统色：故宫里的色彩美学》
    "桑蕾": "#ead89a", # 郭浩《中国传统色：故宫里的色彩美学》
    "茉莉黄": "#f8df72",
    "葵扇黄": "#f8d86a",
    "油菜花黄": "#fbda41",
    "柠檬黄": "#fcd337",
    "柑黄": "#f4cf39",
    "雌黄": "#eac21d",
    "明黄": "#fcc800",
    "藤黄": "#e9ba20",
    "荩草": "#f1bd3f",
    "蜜蜡": "#e7b140",
    "黄河琉璃": "#e5a84b", # 郭浩《中国传统色：故宫里的色彩美学》
    "杏仁黄": "#f7e8aa",
    "黄栗留": "#fedc5e", # 郭浩《中国传统色：故宫里的色彩美学》
    "嫩鹅黄": "#f2c867", # 郭浩《中国传统色：故宫里的色彩美学》
    "栀子": "#fac03d", # 郭浩《中国传统色：故宫里的色彩美学》
    "炒米": "#e7b864",
    "黄不老": "#db9b34", # 郭浩《中国传统色：故宫里的色彩美学》
    "紫磨金": "#bc836b", # 郭浩《中国传统色：故宫里的色彩美学》
    "后土": "#e1a34b",
    "琥珀": "#d29836",
    "桂黄": "#eda01e",
    "雄黄": "#f3993a",
    "杏黄": "#d98700",

    "龙战": "#5f4321", # 郭浩《中国传统色：故宫里的色彩美学》
    "黄埃": "#b49273", # 郭浩《中国传统色：故宫里的色彩美学》
    "紫瓯": "#7c461e", # 郭浩《中国传统色：故宫里的色彩美学》
    "九斤黄": "#ddb078", # 郭浩《中国传统色：故宫里的色彩美学》
    "赤璋": "#e1c199", # 郭浩《中国传统色：故宫里的色彩美学》
    "茧色": "#c6a268", # 郭浩《中国传统色：故宫里的色彩美学》
}

CYAN_COLORS_CH = {
    "粉青": "#c4dad6",
    "蛋青": "#c3d9d6",
    "粉绿": "#b2c6bf",
    "醽醁": "#a6bab1", # 郭浩《中国传统色：故宫里的色彩美学》
    "水色": "#88ada6",
    "沧浪": "#b1d5c8", # 郭浩《中国传统色：故宫里的色彩美学》
    "豆青": "#a1bfb0",
    "苍筤": "#99bcac", # 郭浩《中国传统色：故宫里的色彩美学》
    "缥碧": "#80a492", # 郭浩《中国传统色：故宫里的色彩美学》
    "翠涛": "#819d8e", # 郭浩《中国传统色：故宫里的色彩美学》
    "千山翠": "#6b7d73", # 郭浩《中国传统色：故宫里的色彩美学》
    "海天蓝": "#c6e6e8",
    "繱犗": "#88bfb8", # 郭浩《中国传统色：故宫里的色彩美学》
    "二绿": "#5da39d", # 郭浩《中国传统色：故宫里的色彩美学》
    "铜青": "#3d8e86", # 郭浩《中国传统色：故宫里的色彩美学》
    "闪蓝": "#7cabb1",
    "正青": "#6ca8af", # 郭浩《中国传统色：故宫里的色彩美学》
    "扁青": "#509296", # 郭浩《中国传统色：故宫里的色彩美学》
    "法翠": "#108b96", # 郭浩《中国传统色：故宫里的色彩美学》
    "翠蓝": "#41888a",
    "青雘": "#007175", # 郭浩《中国传统色：故宫里的色彩美学》
    "䌦色": "#226b68", # 郭浩《中国传统色：故宫里的色彩美学》
    "石绿": "#206864", # 郭浩《中国传统色：故宫里的色彩美学》
    "天青": "#c6d7db",
    "井天": "#a4c9cc", # 郭浩《中国传统色：故宫里的色彩美学》
    "西子": "#87c0ca", # 郭浩《中国传统色：故宫里的色彩美学》
    "清水蓝": "#93d5dc",
    "松石": "#75c1c4",
    "天水碧": "#5aa4ae", # 郭浩《中国传统色：故宫里的色彩美学》
    "瀑布蓝": "#51c4d3",
    "甸子蓝": "#10aec2",
    "霁青": "#63bbd0",
    "碧青": "#5cb3cc",
    "法蓝": "#30aecf",
    "明矾蓝": "#0f95b0",
    "卵色": "#d5e3d4", # 郭浩《中国传统色：故宫里的色彩美学》
    "影青": "#bdcbd2",
    "白青": "#98b6c2",
    "虾青": "#94a9b8",
    "竹月": "#7f9faf", # 郭浩《中国传统色：故宫里的色彩美学》
    "空青": "#66889e", # 郭浩《中国传统色：故宫里的色彩美学》
    "太师青": "#547689", # 郭浩《中国传统色：故宫里的色彩美学》
    "虾壳青": "#869d90",
    "晚波蓝": "#648e93",
    "蜻蜓蓝": "#3b818c",
    "鱼师青": "#32788a", # 郭浩《中国传统色：故宫里的色彩美学》
    "青緺": "#284852", # 郭浩《中国传统色：故宫里的色彩美学》

    "软翠": "#006d87", # 郭浩《中国传统色：故宫里的色彩美学》
}

ORANGE_COLORS_CH = {
    "扶光": "#f0c2a2", # 郭浩《中国传统色：故宫里的色彩美学》
    "如梦令": "#ddbb99", # 郭浩《中国传统色：故宫里的色彩美学》
    "芸黄": "#d2a36c", # 郭浩《中国传统色：故宫里的色彩美学》
    "金埒": "#be9457", # 郭浩《中国传统色：故宫里的色彩美学》
    "蛾黄": "#be8a2f", # 郭浩《中国传统色：故宫里的色彩美学》
    "密陀僧": "#b3934b", # 郭浩《中国传统色：故宫里的色彩美学》
    "雌黄": "#b4884d", # 郭浩《中国传统色：故宫里的色彩美学》 # 与黄色系雌黄同名不同色值
    "椒房": "#db9c5e", # 郭浩《中国传统色：故宫里的色彩美学》
    "黄不老": "#db9b34", # 与黄色系黄不老重复
    "杏子": "#da9233", # 郭浩《中国传统色：故宫里的色彩美学》 # 与杏黄几乎同名
    "郁金裙": "#d08635", # 郭浩《中国传统色：故宫里的色彩美学》
    "柘黄": "#c67915", # 郭浩《中国传统色：故宫里的色彩美学》
    "蛋壳黄": "#f8c387",
    "玫瑰粉": "#f8b37f",
    "縓色": "#efab84",
    "海螺橙": "#f0945d",
    "鲑鱼红": "#f09c5a",
    "鹿皮褐": "#d99156",
    "库金": "#e18a3b", # 郭浩《中国传统色：故宫里的色彩美学》
    "红友": "#d9883d", # 郭浩《中国传统色：故宫里的色彩美学》
    "醉瓜肉": "#db8540",
    "麂棕": "#de7622",
    "媚蝶": "#bc6e37", # 郭浩《中国传统色：故宫里的色彩美学》
    "黄流": "#9f6027", # 郭浩《中国传统色：故宫里的色彩美学》
    "骍刚": "#f5b087", # 郭浩《中国传统色：故宫里的色彩美学》
    "晨曦红": "#ea8958",
    "美人蕉橙": "#fa7e23",
    "金红": "#ee781f",
    "菠萝红": "#fc7930",
    "金莲花橙": "#f86b1d",
    "蟹壳红": "#f27635",
    "陶瓷红": "#e16723",
    "余烬红": "#cf7543",
    "火砖红": "#cd6227",
    "光明砂": "#cc5d20", # 郭浩《中国传统色：故宫里的色彩美学》
    "韎韐": "#9f5221", # 郭浩《中国传统色：故宫里的色彩美学》
    "淡藏花红": "#f6ad8f",
    "野蔷薇红": "#fb9968",
    "赪霞": "#f18f60", # 郭浩《中国传统色：故宫里的色彩美学》
    "瓜瓤红": "#f68c60",
    "赪尾": "#ef845d", # 郭浩《中国传统色：故宫里的色彩美学》
    "朱柿": "#ed6d46", # 郭浩《中国传统色：故宫里的色彩美学》
    "苕荣": "#ed6d3d", # 郭浩《中国传统色：故宫里的色彩美学》
    "金驼": "#e46828",
    "铁棕": "#d85916", # 与黑色系铁棕同名
    "黄丹": "#ea5514", # 郭浩《中国传统色：故宫里的色彩美学》
    "落霞红": "#cf4813",
    "橘红": "#bb5133",
}

GREEN_COLORS_CH = {
    "断肠": "#ecebc2", # 郭浩《中国传统色：故宫里的色彩美学》
    "麴尘": "#c0d09d", # 郭浩《中国传统色：故宫里的色彩美学》
    "欧碧": "#c0d695", # 郭浩《中国传统色：故宫里的色彩美学》
    "春辰": "#a9be78", # 郭浩《中国传统色：故宫里的色彩美学》
    "苍葭": "#a8bf8f", # 郭浩《中国传统色：故宫里的色彩美学》
    "兰苕": "#a8b78c", # 郭浩《中国传统色：故宫里的色彩美学》
    "碧滋": "#90a07d", # 郭浩《中国传统色：故宫里的色彩美学》
    "渌波": "#9bb496", # 郭浩《中国传统色：故宫里的色彩美学》
    "青楸": "#81a380", # 郭浩《中国传统色：故宫里的色彩美学》
    "雀梅": "#788a6f", # 郭浩《中国传统色：故宫里的色彩美学》
    "青梅": "#778a77", # 郭浩《中国传统色：故宫里的色彩美学》
    "油绿": "#5d7259", # 郭浩《中国传统色：故宫里的色彩美学》
    "无心绿": "#bfd1b2",
    "绿矾": "#b4bda0",
    "艾绿": "#9daa6c",
    "梅子青": "#a9bd70",
    "苹果": "#a0bf52",
    "笋绿": "#84a740",
    "碧山": "#779649", # 郭浩《中国传统色：故宫里的色彩美学》
    "秋葵": "#6b8c32",
    "葱倩": "#6c8650", # 郭浩《中国传统色：故宫里的色彩美学》
    "石发": "#6a8d52", # 郭浩《中国传统色：故宫里的色彩美学》
    "漆姑": "#5d8351", # 郭浩《中国传统色：故宫里的色彩美学》
    "芰荷": "#4f794a", # 郭浩《中国传统色：故宫里的色彩美学》
    "嘉陵水绿": "#add5a2",
    "鹦哥绿": "#a5d1b5",
    "水绿": "#8db799",
    "麦绿": "#8eaf8c",
    "豆绿": "#91ae84",
    "葱绿": "#799a64",
    "庭芜绿": "#68945c", # 郭浩《中国传统色：故宫里的色彩美学》
    "四绿": "#6bb392",
    "三绿": "#53976f",
    "品绿": "#1c8d6c",
    "孔雀绿": "#007d62",
    "官绿": "#2a6e3f", # 郭浩《中国传统色：故宫里的色彩美学》
    "京绿": "#468c37",
    "明绿": "#49864d",
    "翠微": "#4c8045", # 郭浩《中国传统色：故宫里的色彩美学》
    "秧色": "#507936",
    "竹绿": "#357944",
    "青青": "#4f6f46", # 郭浩《中国传统色：故宫里的色彩美学》
    "翠虬": "#446a37", # 郭浩《中国传统色：故宫里的色彩美学》
    "松绿": "#3d6036",
    "莓莓": "#4e6548", # 郭浩《中国传统色：故宫里的色彩美学》
    "砂绿": "#425539",
    "螺青": "#3f503b", # 郭浩《中国传统色：故宫里的色彩美学》
    "结绿": "#555f4d", # 郭浩《中国传统色：故宫里的色彩美学》

    "冻缥": "#bec2b3", # 郭浩《中国传统色：故宫里的色彩美学》
    "春碧": "#9d9d82", # 郭浩《中国传统色：故宫里的色彩美学》
    "执大象": "#919177", # 郭浩《中国传统色：故宫里的色彩美学》
    "苔古": "#79836c", # 郭浩《中国传统色：故宫里的色彩美学》
    "青粲": "#c3d94e", # 郭浩《中国传统色：故宫里的色彩美学》
    "翠缥": "#b7d332", # 郭浩《中国传统色：故宫里的色彩美学》
    "水龙吟": "#84a729", # 郭浩《中国传统色：故宫里的色彩美学》
    "瓷秘": "#bfc096", # 郭浩《中国传统色：故宫里的色彩美学》
    "琬琰": "#a9a886", # 郭浩《中国传统色：故宫里的色彩美学》
    "青圭": "#92905d", # 郭浩《中国传统色：故宫里的色彩美学》
    "鸣珂": "#b3b59c", # 郭浩《中国传统色：故宫里的色彩美学》
    "青玉案": "#a8b092", # 郭浩《中国传统色：故宫里的色彩美学》
    "出岫": "#a9a773", # 郭浩《中国传统色：故宫里的色彩美学》
    "风入松": "#868c4e", # 郭浩《中国传统色：故宫里的色彩美学》
    "行香子": "#bfb99c", # 郭浩《中国传统色：故宫里的色彩美学》
    "王刍": "#a99f70", # 郭浩《中国传统色：故宫里的色彩美学》
    "荩箧": "#877d52", # 郭浩《中国传统色：故宫里的色彩美学》
    "葱青": "#edf1bb", # 郭浩《中国传统色：故宫里的色彩美学》
    "少艾": "#e3eb98", # 郭浩《中国传统色：故宫里的色彩美学》
    "绮钱": "#d8de8a", # 郭浩《中国传统色：故宫里的色彩美学》
    "翠樽": "#cdd171", # 郭浩《中国传统色：故宫里的色彩美学》
    "山岚": "#bed2bb", # 郭浩《中国传统色：故宫里的色彩美学》
    "菉竹": "#698e6a", # 郭浩《中国传统色：故宫里的色彩美学》
    "绿沈": "#938f4c", # 郭浩《中国传统色：故宫里的色彩美学》
    "绞衣": "#7f754c", # 郭浩《中国传统色：故宫里的色彩美学》
    "素綦": "#595333", # 郭浩《中国传统色：故宫里的色彩美学》
    "葭菼": "#cad7c5", # 郭浩《中国传统色：故宫里的色彩美学》
    "冰台": "#becab7", # 郭浩《中国传统色：故宫里的色彩美学》
    "青古": "#b3bda9", # 郭浩《中国传统色：故宫里的色彩美学》
    "翕赩": "#5f766a", # 郭浩《中国传统色：故宫里的色彩美学》
    "玄校": "#a9a082", # 郭浩《中国传统色：故宫里的色彩美学》
    "綟绶": "#756c4b", # 郭浩《中国传统色：故宫里的色彩美学》
}

PURPLE_COLORS_CH = {
    "退红": "#f0cfe3", # 郭浩《中国传统色：故宫里的色彩美学》
    "樱花": "#e4b8d5", # 郭浩《中国传统色：故宫里的色彩美学》
    "丁香": "#ce93bf", # 郭浩《中国传统色：故宫里的色彩美学》
    "罗兰紫": "#c08eaf",
    "青蛤壳紫": "#bc84a8",
    "木槿": "#ba79b1", # 郭浩《中国传统色：故宫里的色彩美学》
    "豆蔻紫": "#ad6598",
    "扁豆紫": "#a35c8f",
    "紫蒲": "#a6559d", # 郭浩《中国传统色：故宫里的色彩美学》
    "赪紫": "#8a1874", # 郭浩《中国传统色：故宫里的色彩美学》
    "萸紫": "#833c66",
    "真紫": "#652a41",
    "淡牵牛紫": "#d1c2d3",
    "凤信紫": "#c8adc4",
    "楝花": "#c59ac5",
    "轻紫": "#c5a4cc",
    "茄花": "#bb97c5",
    "槿紫": "#806d9e",
    "青莲": "#7b5aa3",
    "紫罗兰": "#5f479a",
    "桔梗紫": "#813c85",
    "齐紫": "#6c216d", # 郭浩《中国传统色：故宫里的色彩美学》
    "紫府": "#995d7f", # 郭浩《中国传统色：故宫里的色彩美学》
    "芥拾紫": "#602641", # 郭浩《中国传统色：故宫里的色彩美学》
    "昌荣": "#dcc7e1", # 郭浩《中国传统色：故宫里的色彩美学》
    "紫薄汗": "#bba1cb", # 郭浩《中国传统色：故宫里的色彩美学》
    "茈藐": "#a67eb7", # 郭浩《中国传统色：故宫里的色彩美学》
    "蕈紫": "#815c94",
    "紫紶": "#7d5284", # 郭浩《中国传统色：故宫里的色彩美学》
    "拂紫绵": "#7e527f", # 郭浩《中国传统色：故宫里的色彩美学》
    "三公子": "#663d74", # 郭浩《中国传统色：故宫里的色彩美学》
    "凝夜紫": "#422256", # 郭浩《中国传统色：故宫里的色彩美学》
    "葡萄青": "#501d46",
    "紫茄": "#49214a",
    "油紫": "#420b2f", # 郭浩《中国传统色：故宫里的色彩美学》
    "鸦雏": "#6a5b6d", # 郭浩《中国传统色：故宫里的色彩美学》
    "香炉烟紫": "#d3ccd6", # 郭浩《中国传统色：故宫里的色彩美学》
    "雪青": "#a59aca",
    "紫菂": "#9b8ea9", # 郭浩《中国传统色：故宫里的色彩美学》
    "藤萝紫": "#8076a3",
    "暮山紫": "#a4abd6", # 郭浩《中国传统色：故宫里的色彩美学》
    "紫苑": "#757cbb", # 郭浩《中国传统色：故宫里的色彩美学》
    "螺甸紫": "#74759b",
    "山梗紫": "#61649f",
    "野菊紫": "#525288",
    "优昙瑞": "#615ea8", # 郭浩《中国传统色：故宫里的色彩美学》
    "延维": "#4a4b9d", # 郭浩《中国传统色：故宫里的色彩美学》
    "满天星紫": "#2e317c",

    "红藤杖": "#928187", # 郭浩《中国传统色：故宫里的色彩美学》
    "迷楼灰": "#91828f", # 郭浩《中国传统色：故宫里的色彩美学》
    "葡萄褐": "#9e696d", # 郭浩《中国传统色：故宫里的色彩美学》
    "苏方": "#81474c", # 郭浩《中国传统色：故宫里的色彩美学》
    "福色": "#662b2f", # 郭浩《中国传统色：故宫里的色彩美学》
    "紫矿": "#9e4e56", # 郭浩《中国传统色：故宫里的色彩美学》
    "秋蓝": "#7d929f", # 郭浩《中国传统色：故宫里的色彩美学》
    "地血": "#814662", # 郭浩《中国传统色：故宫里的色彩美学》
    "石英": "#c8b6bb", # 郭浩《中国传统色：故宫里的色彩美学》
    "银褐": "#9c8d9b", # 郭浩《中国传统色：故宫里的色彩美学》
    "烟红": "#9d858f", # 郭浩《中国传统色：故宫里的色彩美学》
    "紫诰": "#76555d", # 郭浩《中国传统色：故宫里的色彩美学》
}

PINK_COLORS_CH = {
    "胭脂雪": "#f1deec",
    "杏花": "#fadce9",
    "粉红": "#efc4ce", # 与同色系粉米同色
    "粉米": "#efc4ce", # 郭浩《中国传统色：故宫里的色彩美学》
    "桃夭": "#f6bec8", # 郭浩《中国传统色：故宫里的色彩美学》
    "姜红": "#eeb8c3",
    "水红": "#ecb0c1", # 郭浩《中国传统色：故宫里的色彩美学》
    "彤管": "#e2a2ac", # 郭浩《中国传统色：故宫里的色彩美学》
    "莲红": "#d9a0b3", # 郭浩《中国传统色：故宫里的色彩美学》
    "縓缘": "#ce8892", # 郭浩《中国传统色：故宫里的色彩美学》
    "紫梅": "#bb7a8c", # 郭浩《中国传统色：故宫里的色彩美学》
    "绛纱": "#b27777", # 郭浩《中国传统色：故宫里的色彩美学》
    "银红": "#e7cad3", # 郭浩《中国传统色：故宫里的色彩美学》
    "出炉银": "#edd2d3",
    "肉红": "#ddc5b8", # 郭浩《中国传统色：故宫里的色彩美学》
    "杨妃": "#f091a0", # 郭浩《中国传统色：故宫里的色彩美学》
    "长春": "#dc6b82", # 郭浩《中国传统色：故宫里的色彩美学》
    "渥赭": "#dd6b7b", # 郭浩《中国传统色：故宫里的色彩美学》
    "红麶": "#cd7372", # 郭浩《中国传统色：故宫里的色彩美学》
    "美人祭": "#c35c6a", # 郭浩《中国传统色：故宫里的色彩美学》
    "牙绯": "#c35c5d", # 郭浩《中国传统色：故宫里的色彩美学》
    "唇脂": "#c25160", # 郭浩《中国传统色：故宫里的色彩美学》
    "鞓红": "#b04552", # 郭浩《中国传统色：故宫里的色彩美学》
    "蚩尤旗": "#a85858", # 郭浩《中国传统色：故宫里的色彩美学》
    "盈盈": "#f9d3e3", # 郭浩《中国传统色：故宫里的色彩美学》
    "豇豆红": "#ed9db2",
    "芍药耕红": "#eba0b3",
    "桃红": "#f091a1",
    "霞光红": "#ef82a0",
    "淡绛红": "#ec7696",
    "苏梅": "#dd7694", # 郭浩《中国传统色：故宫里的色彩美学》
    "梅红": "#da6d83",
    "莲瓣红": "#ea517f",
    "松叶牡丹红": "#eb3c70",
    "娇红": "#d1254f",
    "朱孔阳": "#b81a35", # 郭浩《中国传统色：故宫里的色彩美学》
    "靠红": "#f3c2d9",
    "菡萏": "#ef92b5",
    "龙膏烛": "#de82a7", # 郭浩《中国传统色：故宫里的色彩美学》
    "黪紫": "#cc73a0", # 郭浩《中国传统色：故宫里的色彩美学》
    "胭脂水": "#b95a89", # 郭浩《中国传统色：故宫里的色彩美学》
    "琅𤣳紫": "#cb5c83", # 郭浩《中国传统色：故宫里的色彩美学》
    "初荷红": "#e16c96",
    "丹紫红": "#d2568c",
    "深莲红": "#c1527f", # 本与同色系莲红同名，改名为深莲红
    "红踯躅": "#b83570", # 郭浩《中国传统色：故宫里的色彩美学》
    "胭脂紫": "#b0436f", # 郭浩《中国传统色：故宫里的色彩美学》
    "洋葱紫": "#a8456b",

    "海天霞": "#f3a694", # 郭浩《中国传统色：故宫里的色彩美学》
    "紫茎屏风": "#a76283", # 郭浩《中国传统色：故宫里的色彩美学》
    "夏籥": "#d2af9d", # 郭浩《中国传统色：故宫里的色彩美学》
    "檀色": "#b26d5d", # 郭浩《中国传统色：故宫里的色彩美学》
    "赭罗": "#9a6655", # 郭浩《中国传统色：故宫里的色彩美学》
    "魏红": "#a73766", # 郭浩《中国传统色：故宫里的色彩美学》
    "魏紫": "#903754", # 郭浩《中国传统色：故宫里的色彩美学》
    "夕岚": "#e3adb9", # 郭浩《中国传统色：故宫里的色彩美学》
    "雌霓": "#cf929e", # 郭浩《中国传统色：故宫里的色彩美学》
    "茹藘": "#a35f65", # 郭浩《中国传统色：故宫里的色彩美学》
    "苍烟落照": "#c8b5b3", # 郭浩《中国传统色：故宫里的色彩美学》
    "十样锦": "#f8c6b5", # 郭浩《中国传统色：故宫里的色彩美学》
    "檀唇": "#da9e8c", # 郭浩《中国传统色：故宫里的色彩美学》
    "琼琚": "#d77f66", # 郭浩《中国传统色：故宫里的色彩美学》
    "棠梨": "#b15a43", # 郭浩《中国传统色：故宫里的色彩美学》
    "藕丝褐": "#a88787", # 郭浩《中国传统色：故宫里的色彩美学》
    "咸池": "#daa9a9", # 郭浩《中国传统色：故宫里的色彩美学》
}

BLUE_COLORS_CH = {
    "月白": "#d4e5ef", # 郭浩《中国传统色：故宫里的色彩美学》 # 与白色系月白重复
    "远天蓝": "#d0dfe6",
    "井天蓝": "#c3d7df",
    "云水蓝": "#baccd9",
    "星郎": "#bcd4e7", # 郭浩《中国传统色：故宫里的色彩美学》
    "碧落": "#aed0ee", # 郭浩《中国传统色：故宫里的色彩美学》
    "星蓝": "#93b5cf",
    "晴山蓝": "#8fb2c9",
    "羽扇豆蓝": "#619ac3",
    "晴蓝": "#5698c3",
    "宝石蓝": "#2386b9",
    "天蓝": "#1677b3",
    "湖水蓝": "#b0d5df",
    "秋波蓝": "#8abcd1",
    "涧石蓝": "#66a9c9",
    "孔雀蓝": "#4994c4", # 郭浩《中国传统色：故宫里的色彩美学》
    "景泰蓝": "#2775b6",
    "蔚蓝": "#2874af",
    "青冥": "#3271ae", # 郭浩《中国传统色：故宫里的色彩美学》
    "搪瓷蓝": "#11659a",
    "柔蓝": "#106898", # 郭浩《中国传统色：故宫里的色彩美学》
    "吐绶蓝": "#4182a4", # 郭浩《中国传统色：故宫里的色彩美学》
    "蝶翅蓝": "#4e7ca1",
    "海军蓝": "#346c9c",
    "晴山": "#a3bbdb", # 郭浩《中国传统色：故宫里的色彩美学》
    "东方既白": "#8ba3c7", # 郭浩《中国传统色：故宫里的色彩美学》
    "窃蓝": "#88abda", # 郭浩《中国传统色：故宫里的色彩美学》
    "监德": "#6f94cd", # 郭浩《中国传统色：故宫里的色彩美学》
    "苍苍": "#5976ba", # 郭浩《中国传统色：故宫里的色彩美学》
    "群青": "#2e59a7", # 郭浩《中国传统色：故宫里的色彩美学》
    "海涛蓝": "#15559a",
    "二青": "#1e50a2",
    "洒蓝": "#1e3b7a",
    "青金石": "#2b2e77",
    "宝蓝": "#1f286f",
    "青雀头黛": "#354e6b",
    "品月": "#8aabcc", # 郭浩《中国传统色：故宫里的色彩美学》
    "挼蓝": "#6e9bc5", # 郭浩《中国传统色：故宫里的色彩美学》
    "碧城": "#12507b", # 郭浩《中国传统色：故宫里的色彩美学》
    "蓝采和": "#06436f", # 郭浩《中国传统色：故宫里的色彩美学》
    "绀宇": "#003d74", # 郭浩《中国传统色：故宫里的色彩美学》
    "品蓝": "#003d74", # 和绀宇一个颜色
    "帝释青": "#003460", # 郭浩《中国传统色：故宫里的色彩美学》
    "佛头青": "#19325f", # 郭浩《中国传统色：故宫里的色彩美学》
    "骐驎": "#12264f", # 郭浩《中国传统色：故宫里的色彩美学》 # 与黑色系骐驎重复
    "花青": "#1a2847", # 郭浩《中国传统色：故宫里的色彩美学》
    "海青": "#080f40",
    "瑾瑜": "#1e2732", # 郭浩《中国传统色：故宫里的色彩美学》 # 与黑色系瑾瑜重复

    "云门": "#a2d2e2", # 郭浩《中国传统色：故宫里的色彩美学》
}

BROWN_COLORS_CH = {
    "绢色": "#ead8ae",
    "糙米": "#dbcba1",
    "紫花布": "#bea78b", # 郭浩《中国传统色：故宫里的色彩美学》
    "蒸栗": "#a58a5f", # 郭浩《中国传统色：故宫里的色彩美学》
    "黄琮": "#9e8c6b", # 郭浩《中国传统色：故宫里的色彩美学》
    "绿豆褐": "#92896b", # 郭浩《中国传统色：故宫里的色彩美学》
    "茶绿褐": "#8e8570",
    "茶色": "#887657", # 郭浩《中国传统色：故宫里的色彩美学》
    "流黄": "#8b7042", # 郭浩《中国传统色：故宫里的色彩美学》
    "橄榄": "#77642a",
    "伽罗": "#6d5c3d", # 郭浩《中国传统色：故宫里的色彩美学》
    "昆布": "#554f30",
    "血牙": "#e9d1b5",
    "露褐": "#bd8253", # 郭浩《中国传统色：故宫里的色彩美学》
    "沉香": "#99806c", # 郭浩《中国传统色：故宫里的色彩美学》
    "明茶褐": "#9e8368", # 郭浩《中国传统色：故宫里的色彩美学》
    "荆褐": "#906c4a", # 郭浩《中国传统色：故宫里的色彩美学》
    "赭石": "#845a33",
    "枯黄": "#895d31",
    "枯竹褐": "#82572d",
    "驼褐": "#7c5b3e", # 郭浩《中国传统色：故宫里的色彩美学》
    "射干": "#7c623f", # 郭浩《中国传统色：故宫里的色彩美学》
    "油葫芦": "#644d31", # 郭浩《中国传统色：故宫里的色彩美学》
    "苍艾": "#5a4b3b", # 郭浩《中国传统色：故宫里的色彩美学》
    "珠子褐": "#bea89d", # 郭浩《中国传统色：故宫里的色彩美学》
    "丁香褐": "#bd9683", # 郭浩《中国传统色：故宫里的色彩美学》
    "驼茸": "#9e725a",
    "棠梨褐": "#955a42", # 郭浩《中国传统色：故宫里的色彩美学》
    "紫砂": "#7c4622",
    "朱石栗": "#81492c", # 郭浩《中国传统色：故宫里的色彩美学》
    "檀褐": "#945635", # 郭浩《中国传统色：故宫里的色彩美学》
    "驼色": "#66462a",
    "古铜": "#604322",
    "油栗褐": "#604223",
    "茶褐": "#5d3d21",
    "古铜绿": "#533c1b",
    "鹰背褐": "#8f6d5f", # 郭浩《中国传统色：故宫里的色彩美学》
    "麝香褐": "#694b3c", # 郭浩《中国传统色：故宫里的色彩美学》
    "椒褐": "#72453a", # 郭浩《中国传统色：故宫里的色彩美学》
    "蜜褐": "#683632", # 郭浩《中国传统色：故宫里的色彩美学》
    "栗棕": "#5c1e19",
    "枣褐": "#68361a", # 郭浩《中国传统色：故宫里的色彩美学》
    "目童子": "#5b3222", # 郭浩《中国传统色：故宫里的色彩美学》
    "栗壳": "#775039", # 郭浩《中国传统色：故宫里的色彩美学》
    "烟色": "#564232",
    "酱色": "#402929",
    "豆沙": "#481e1c",
    "青骊": "#422517", # 郭浩《中国传统色：故宫里的色彩美学》 # 与黑色系青骊重复
    
    "緅絺": "#804c2e", # 郭浩《中国传统色：故宫里的色彩美学》
    "地籁": "#dfceb4", # 郭浩《中国传统色：故宫里的色彩美学》
    "大块": "#bfa782", # 郭浩《中国传统色：故宫里的色彩美学》
    "养生主": "#b49b7f", # 郭浩《中国传统色：故宫里的色彩美学》
    "大云": "#94784f", # 郭浩《中国传统色：故宫里的色彩美学》
    "石莲褐": "#92897b", # 郭浩《中国传统色：故宫里的色彩美学》
    "黄螺": "#b4a379", # 郭浩《中国传统色：故宫里的色彩美学》
    "降真香": "#9e8358", # 郭浩《中国传统色：故宫里的色彩美学》
    "远志": "#81663b", # 郭浩《中国传统色：故宫里的色彩美学》
    "石蜜": "#d4bf89", # 郭浩《中国传统色：故宫里的色彩美学》
    "沙饧": "#bfa670", # 郭浩《中国传统色：故宫里的色彩美学》
    "巨吕": "#aa8e59", # 郭浩《中国传统色：故宫里的色彩美学》
    "吉金": "#896d47", # 郭浩《中国传统色：故宫里的色彩美学》
    "冥色": "#665f4d", # 郭浩《中国传统色：故宫里的色彩美学》
}