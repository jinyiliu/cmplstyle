CH_BASE_COLORS = {}

BASE_COLORS_EN_TO_CH = {}

CH_TRAD_COLORS = {}

TRAD_COLORS_EN_TO_CH = {}

WHITE_COLORS_CH = {
    "缟羽": "#efefef",
    "浅云": "#eaeef1",
    "银白": "#eff0f1",
    "鹄白": "#ebeef0",
    "羊绒": "#eaebeb",
    "葱白": "#ebeee8",
    "蛤粉": "#ebeee1",
    "白垩": "#e0e1d9",
    "缟素": "#e6e6dc",
    "象牙": "#eeeadc",
    "米汤娇": "#eeead9",
    "蜜合": "#dfd7c2",
    "乳白": "#fffef3",
    "凝脂": "#f5f2e9",
    "山矾": "#f5f3f2",
    "玉頩": "#eae5e3",
    "芡食白": "#e2e1e4",
    "葭灰": "#d3d4d3",
    "汉白玉": "#f8f4ed",
    "荷花白": "#fbecde",
    "蚌肉白": "#f9f1db",
    "荔肉白": "#f2e6ce",
    "米色": "#f9e9cd",
    "菊蕾白": "#e9ddb6",
    "酂白": "#f6f9e4",
    "皦玉": "#ebeee8",
    "吉量": "#ebeddf",
    "天球": "#e0dfc6",
    "韶粉": "#e0e0d0",
    "二目鱼": "#dfe0d9",
    "明月珰": "#d4d3ca",
    "霜地": "#c7c6b6",
    "溶溶月": "#bec2bc",
    "余白": "#c9cfc1",
    "草白": "#bfc1a9",
    "豆白": "#d5e0d5",
    "东方既白": "#f5fefb",
    "甜白": "#eceff4",
    "卵白": "#e4ecf0",
    "荻色": "#dfe5e8",
    "素采": "#d4dde1",
    "月白": "#d4e5ef",
    "云峰白": "#d8e3e7",
    "鱼肚白": "#c8d0d3",
    "影青": "#bdcbd2",
    "逍遥游": "#b2bfc3",
    "白青": "#98b6c2",
    "青鸾": "#9aa7b1",
}

BLACK_COLORS_CH = {
    "雷雨垂": "#7a7b78",
    "石涅": "#686167",
    "墨朱": "#70695d",
    "沙石": "#69635d",
    "墨黲": "#585248",
    "鸭雏": "#483d34",
    "驖骊": "#46433b",
    "青骊": "#422517",
    "金青": "#46443b",
    "茶青": "#3f3b31",
    "京元": "#31322c",
    "铁棕": "#1a0404",
    "铁色": "#595861",
    "黪墨": "#625d6b",
    "玄天": "#6b5458",
    "烟墨": "#5c4f55",
    "紫鼠": "#594c57",
    "曾青": "#535164",
    "青黛": "#45465e",
    "冥靘": "#454659", # 第一个字应为冥加一个色，但是暂时找不到这个字
    "青雀头黛": "#354e6b",
    "育阳染": "#576470",
    "霁蓝": "#3c4654",
    "骐麟": "#12264f",
    "油烟墨": "#3f3f3c",
    "绿云": "#45493d",
    "蒽油绿": "#373834",
    "老绿": "#1c2d29",
    "墨绿": "#1c2d25",
    "苷蓝绿": "#1f2623",
    "云杉绿": "#15231b",
    "螺子黛": "#13393e",
    "鹰背": "#39363f",
    "朱墨": "#2d2d30",
    "石青": "#2e282e",
    "墨紫": "#281d2c",
    "火薰": "#2f3243",
    "真青": "#192841",
    "花青": "#1a2847",
    "璆琳": "#343041",
    "鼎灰": "#36292f",
    "绀蝶": "#2c2f3b",
    "暗龙胆紫": "#22202e",
    "瑾瑜": "#1e2732",
    "元青": "#28292b",
    "袀玄": "#262729",
    "燕尾青": "#131423",
    "獺见": "#151d29",
}

RED_COLORS_CH = {
    "小红": "#e67762",
    "抹红": "#de694c",
    "骍衣": "#ea5532",
    "朱膘": "#e94721",
    "鹤顶红": "#d24735",
    "杏红": "#cf3d15",
    "珊瑚": "#ca462f",
    "银朱": "#d12920",
    "火赫": "#bf301e",
    "珊瑚赫": "#c12c1f",
    "蕉红": "#c8191d",
    "牙红": "#b01f24",
    "岱赭": "#dd6b4f",
    "赩炽": "#cb523e",
    "朱殷": "#b93a26",
    "石榴裙": "#b13b2e",
    "绛红": "#b02e28",
    "赤缇": "#ba5b49",
    "纁黄": "#ba5140",
    "朱草": "#a64036",
    "綪茷": "#9e2a22",
    "朱湛": "#95302e",
    "朱樱": "#bf1d22",
    "大繎": "#822327",
    "丹色": "#d64241",
    "翘红": "#e9464d",
    "朱砂": "#d80835",
    "双红": "#c02a45",
    "胭脂": "#b32142",
    "红椒": "#e02623",
    "丹枫": "#d81918",
    "丹罽": "#e60012",
    "丹臒": "#c8161d",
    "胭脂虫": "#ab1d22",
    "水华朱": "#a72126",
    "顺圣": "#7c191e",
    "茜红": "#cc5d4e",
    "绯红": "#bf5552",
    "佛赤": "#8f3d2c",
    "烟红": "#902e22",
    "枣红": "#8a2623",
    "荔色": "#89262c",
    "朱红": "#711318",
    "不老红": "#702029",
    "爵头": "#631216",
    "燃红": "#5d181a",
    "木兰": "#662b1e",
    "麒麟竭": "#4c1e1a",
}

YELLOW_COLORS_CH = {
    "半见": "#fffbc7",
    "女贞黄": "#f7eead",
    "莺儿": "#ebe1a9",
    "绢纨": "#ece093",
    "禹余粮": "#e1d279",
    "田赤": "#e1d384",
    "姜黄": "#d6c560",
    "姚黄": "#d6bc46",
    "黄封": "#cab272",
    "栾华": "#c0ad5e",
    "大赤": "#aa9649",
    "苍黄": "#b6a014",
    "黄白游": "#fff799",
    "松花": "#ffee6f",
    "缃叶": "#ecd452",
    "槐黄": "#d6bb38",
    "草黄": "#d2b42c",
    "矫黄": "#daa91f",
    "金黄": "#d3a117",
    "鞠衣": "#d3a237",
    "太一余粮": "#d5b45c",
    "秋香": "#bf9c46",
    "香色": "#b69833",
    "老茯神": "#aa8534",
    "桑蕾": "#ead89a",
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
    "黄河琉璃": "#e5a84b", # 黄琉璃
    "杏仁黄": "#f7e8aa",
    "黄栗留": "#fedc5e",
    "嫩鹅黄": "#f2c867",
    "栀子": "#fac03d",
    "炒米": "#e7b864",
    "黄不老": "#db9b34",
    "紫磨金": "#dda541",
    "后土": "#e1a34b",
    "琥珀": "#d29836",
    "桂黄": "#eda01e",
    "雄黄": "#f3993a",
    "杏黄": "#d98700",
}

CYAN_COLORS_CH = {
    "粉青": "#c4dad6",
    "蛋青": "#c3d9d6",
    "粉绿": "#b2c6bf",
    "醽醁": "#a6bab1",
    "水色": "#88ada6",
    "沧浪": "#b1d5c8",
    "豆青": "#a1bfb0",
    "苍筤": "#99bcac",
    "葱青": "#8cb7a2",
    "缥碧": "#80a492",
    "翠涛": "#819d8e",
    "千山翠": "#6b7d73",
    "海天蓝": "#c6e6e8",
    "繱犗": "#88bfb8",
    "二绿": "#5da39d",
    "铜青": "#3d8e86",
    "闪蓝": "#7cabb1",
    "正青": "#6ca8af",
    "扁青": "#509296",
    "法翠": "#108b96",
    "翠蓝": "#41888a",
    "青雘": "#007175",
    "䌦色": "#226b68",
    "石绿": "#206864",
    "天青": "#c6d7db",
    "井天": "#a4c9cc",
    "西子": "#87c0ca",
    "清水蓝": "#93d5dc",
    "松石": "#75c1c4",
    "天水碧": "#5aa4ae",
    "瀑布蓝": "#51c4d3",
    "甸子蓝": "#10aec2",
    "霁青": "#63bbd0",
    "碧青": "#5cb3cc",
    "法蓝": "#30aecf",
    "明矾蓝": "#0f95b0",
    "卵色天": "#c8d8e1",
    "影青": "#bdcbd2",
    "白青": "#98b6c2",
    "虾青": "#94a9b8",
    "竹月": "#7f9faf",
    "空青": "#66889e",
    "太师青": "#547689",
    "虾壳青": "#869d90",
    "晚波蓝": "#648e93",
    "蜻蜓蓝": "#3b818c",
    "鱼师青": "#32788a",
    "青緺": "#284852",
}

ORANGE_COLORS_CH = {
    "扶光": "#f0c2a2",
    "如梦令": "#ddbb99",
    "芸黄": "#d2a36c",
    "金埒": "#be9457",
    "蛾黄": "#be8a2f",
    "密陀僧": "#b3934b",
    "雌黄": "#b4884d", # 与黄色系雌黄重复
    "椒房": "#db9c5e",
    "黄不老": "#db9b34", # 与黄色系黄不老重复
    "杏子": "#da9233", # 与杏黄几乎同名
    "郁金裙": "#d08635",
    "柘黄": "#c67915",
    "蛋壳黄": "#f8c387",
    "玫瑰粉": "#f8b37f",
    "縓色": "#efab84",
    "海螺橙": "#f0945d",
    "鲑鱼红": "#f09c5a",
    "鹿皮褐": "#d99156",
    "库金": "#e18a3b",
    "红友": "#d9883d",
    "醉瓜肉": "#db8540",
    "麂棕": "#de7622",
    "媚蝶": "#bc6e37",
    "黄流": "#9f6027",
    "骍刚": "#f5b087",
    "晨曦红": "#ea8958",
    "美人蕉橙": "#fa7e23",
    "金红": "#ee781f",
    "菠萝红": "#fc7930",
    "金莲花橙": "#f86b1d",
    "蟹壳红": "#f27635",
    "陶瓷红": "#e16723",
    "余烬红": "#cf7543",
    "火砖红": "#cd6227",
    "光明砂": "#cc5d20",
    "韎韐": "#9f5221",
    "淡藏花红": "#f6ad8f",
    "野蔷薇红": "#fb9968",
    "赪霞": "#f18f60",
    "瓜瓤红": "#f68c60",
    "赪尾": "#ef845d",
    "朱柿": "#ed6d46",
    "苕荣": "#ed6d3d",
    "金驼": "#e46828",
    "铁棕": "#d85916", # 与黑色系铁棕同名
    "黄丹": "#ea5514",
    "落霞红": "#cf4813",
    "橘红": "#bb5133",
}

GREEN_COLORS_CH = {
    "断肠": "#e8edb9",
    "麴尘": "#c0d09d",
    "欧碧": "#c0d695",
    "春辰": "#a9be78",
    "苍葭": "#a8bf8f",
    "兰苕": "#a8b78c",
    "碧滋": "#90a07d",
    "渌波": "#9bb496",
    "青楸": "#81a380",
    "雀梅": "#788a6f",
    "青梅": "#778a77",
    "油绿": "#5d7259",
    "无心绿": "#bfd1b2",
    "绿矾": "#b4bda0",
    "艾绿": "#9daa6c",
    "梅子青": "#a9bd70",
    "苹果": "#a0bf52",
    "笋绿": "#84a740",
    "碧山": "#779649",
    "秋葵": "#6b8c32",
    "葱倩": "#6c8650",
    "石发": "#6a8d52",
    "漆姑": "#5d8351",
    "芰荷": "#4f794a",
    "嘉陵水绿": "#add5a2",
    "鹦哥绿": "#a5d1b5",
    "水绿": "#8db799",
    "麦绿": "#8eaf8c",
    "豆绿": "#91ae84",
    "葱绿": "#799a64",
    "庭芜绿": "#68945c",
    "四绿": "#6bb392",
    "三绿": "#53976f",
    "品绿": "#1c8d6c",
    "孔雀绿": "#007d62",
    "管绿": "#2a6e3f",
    "京绿": "#468c37",
    "明绿": "#49864d",
    "翠微": "#4c8045",
    "秧色": "#507936",
    "竹绿": "#357944",
    "青青": "#4f6f46",
    "翠虬": "#446a37",
    "松绿": "#3d6036",
    "莓莓": "#4e6548",
    "砂绿": "#425539",
    "螺青": "#3f503b",
    "结绿": "#555f4d",
}

PURPLE_COLORS_CH = {
    "退红": "#f0cfe3",
    "樱花": "#e4b8d5",
    "丁香": "#ce93bf",
    "罗兰紫": "#c08eaf",
    "青蛤壳紫": "#bc84a8",
    "木槿": "#ba7ab1",
    "豆蔻紫": "#ad6598",
    "扁豆紫": "#a35c8f",
    "紫蒲": "#a6569d",
    "赪紫": "#8a1874",
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
    "齐紫": "#6c216d",
    "紫府": "#995d7f",
    "芥拾紫": "#602641",
    "昌荣": "#dcc7e1",
    "紫薄汗": "#bba1cb",
    "茈藐": "#a67eb7",
    "蕈紫": "#815c94",
    "紫紶": "#7d5284",
    "拂紫绵": "#7e527f",
    "三公子": "#663d74",
    "凝夜紫": "#422256",
    "葡萄青": "#501d46",
    "紫茄": "#49214a",
    "油紫": "#420b2f",
    "鸦雏": "#6a5b6d",
    "香炉烟紫": "#d3ccd6",
    "雪青": "#a59aca",
    "紫菂": "#9b8ea9",
    "藤萝紫": "#8076a3",
    "暮山紫": "#a4abd6",
    "紫苑": "#757cbb",
    "螺甸紫": "#74759b",
    "山梗紫": "#61649f",
    "野菊紫": "#525288",
    "优昙瑞": "#615ea8",
    "延维": "#4a4b9d",
    "满天星紫": "#2e317c",
}

PINK_COLORS_CH = {
    "胭脂雪": "#f1deec",
    "杏花": "#fadce9",
    "粉红": "#efc4ce",
    "粉米": "#efc4ce",
    "桃夭": "#f6bec8",
    "姜红": "#eeb8c3",
    "水红": "#ecb0c1",
    "彤管": "#e2a2ac",
    "淡莲红": "#d9a0b3", # 本与同色系莲红同名，改名为淡莲红
    "縓缘": "#ce8892",
    "紫梅": "#bb7a8c",
    "绾色": "#b27777",
    "银红": "#e7cad3",
    "出炉银": "#edd2d3",
    "肉红": "#e5b7b7",
    "杨妃": "#f091a0",
    "长春": "#dc6b82",
    "渥赭": "#dd6b7b",
    "红麶": "#cd7372",
    "美人祭": "#c35c6a",
    "牙绯": "#c35c5d",
    "唇脂": "#c25160",
    "鞓红": "#b04552",
    "蚩尤旗": "#a85858",
    "盈盈": "#f9d3e3",
    "豇豆红": "#ed9db2",
    "芍药耕红": "#eba0b3",
    "桃红": "#f091a1",
    "霞光红": "#ef82a0",
    "淡绛红": "#ec7696",
    "苏梅": "#dd7694",
    "梅红": "#da6d83",
    "莲瓣红": "#ea517f",
    "松叶牡丹红": "#eb3c70",
    "娇红": "#d1254f",
    "朱孔阳": "#b81a35",
    "靠红": "#f3c2d9",
    "菡萏": "#ef92b5",
    "龙膏烛": "#de82a7",
    "黪紫": "#cc73a0",
    "胭脂水": "#b95a89",
    "琅𤣳紫": "#cb5c83",
    "初荷红": "#e16c96",
    "丹紫红": "#d2568c",
    "莲红": "#c1527f",
    "红踯躅": "#c14379",
    "胭脂紫": "#b0436f",
    "洋葱紫": "#a8456b",
}
