import requests
import datetime
# test_skills = [ 
#     {
#         "name": "驚異のスタミナA",
#         "type": "A",
#         "effect": "発動確率35％/スタミナ消費量-60％",
#         "cname": "惊人体力A",
#         "ceffect": "35%概率 自身体力消耗-60%",
#         "zhs_name": "惊人的体力A",
#         "zhs_effect": "发动概率35%/体力消耗量-60%",
#         "zht_name": "驚人的體力A",
#         "zht_effect": "發動機率35％/體力消耗量-60%",
#         "en_name": "Miraculous Stamina A",
#         "en_effect": "35% chance thatStamina Consumption -60%",
#         "kr_name": "경이로운 스태미너 A",
#         "kr_effect": "발동 확률 35％/스태미너 소비량 -60%",
#         "pp_type": "",
#         "property": "stm"
#     },
#     {
#         "name": "驚異のスタミナB",
#         "type": "A",
#         "effect": "発動確率40％/スタミナ消費量-55％",
#         "cname": "惊人体力B",
#         "ceffect": "40%概率 自身体力消耗-55%",
#         "zhs_name": "惊人的体力B",
#         "zhs_effect": "发动概率40%/体力消耗量-55%",
#         "zht_name": "驚人的體力B",
#         "zht_effect": "發動機率40％/體力消耗量-55%",
#         "en_name": "Miraculous Stamina B",
#         "en_effect": "40% chance thatStamina Consumption -55%",
#         "kr_name": "경이로운 스태미너 B",
#         "kr_effect": "발동 확률 40％/스태미너 소비량 -55%",
#         "pp_type": "",
#         "property": "stm"
#     },
#     {
#     "name": "プラチナアタッカー", "type": "P", "effect": "アタッカーになる確率+15%", "cname": "白金进攻者", "ceffect": "成为攻击者的可能性+ 15％", "zhs_name": "白金攻击手", "zhs_effect": "成为攻击手的概率+15%", "zht_name": "白金攻擊手", "zht_effect": "成為攻擊手的機率為+15%", "en_name": "Platinum Attacker", "en_effect": "Probability of being the attacker: +15%", "kr_name": "플래티넘 어태커", "kr_effect": "어태커가 될 확률 +15%", "pp_type": "10", "property": "SP"
#     },
#     {
#     "name": "内から湧き上がるスタミナ6", "type": "P", "effect": "スタミナ消費量-11％", "cname": "展现体力6", "ceffect": "自身体力消耗-11%", "zhs_name": "从深处涌现的体力6", "zhs_effect": "体力消耗量-11%", "zht_name": "從體內湧現出的體力6", "zht_effect": "體力消耗量-11%", "en_name": "Stamina from Within 6", "en_effect": "Stamina Consumption -11%", "kr_name": "솟아나는 스태미너 6", "kr_effect": "스태미너 소비량 -11%", "pp_type": "9", "property": "stm"
#     },
#     {
#     "name": "可憐なフェイント", "type": "F", "effect": "フェイント成功で獲得アピールポイント+30%", "cname": "卖萌佯攻", "ceffect": "（此技能拥有角色 技巧攻击成功）佯攻成功时 获得分数+30%", "zhs_name": "楚楚可怜的假动作", "zhs_effect": "假动作成功后获得的魅力值+30%", "zht_name": "甜蜜的佯攻", "zht_effect": "佯攻成功時獲得的魅力點數為+30%", "en_name": "Sweet Feint", "en_effect": "After a successful feint,Appeal Points gained+30%", "kr_name": "가련한 페인트", "kr_effect": "페인트 성공 시 얻는 어필 포인트 +30%", "pp_type": "", "property": "tec"
#     },
    
# ]

test_girls = [
    {
    "id": "0", "name": "みさき", "ename": "misaki", "cname": "美咲 / 海咲", "birthday": "7/7", "keywords": "misaki 老婆 laopo meixiao haixiao", "pow": "1040", "tec": "900", "stm": "1050", "apl": "20", "type": "pow", "release": "20171115", "free": "20171115", "age": "18", "height": "156", "Bust": "85", "Waist": "54", "Hips": "89", "blood": "A", "cv": "津田美波", "ACC_head": "pow", "ACC_face": "stm", "ACC_hand": "pow"
  },
  {
    "id": "1", "name": "こころ", "ename": "kokoro", "cname": "心", "birthday": "12/1", "keywords": "kokoro 老婆 laopo xin", "pow": "1000", "tec": "850", "stm": "1150", "apl": "10", "type": "pow", "release": "20171115", "free": "20171115", "age": "19", "height": "158", "Bust": "90", "Waist": "55", "Hips": "87", "blood": "A", "cv": "川橙绫子", "ACC_head": "pow", "ACC_face": "pow", "ACC_hand": "stm"
  },
]

skills = [
    {
        "name": "驚異のスタミナA",
        "type": "A",
        "effect": "発動確率35％/スタミナ消費量-60％",
        "cname": "惊人体力A",
        "ceffect": "35%概率 自身体力消耗-60%",
        "zhs_name": "惊人的体力A",
        "zhs_effect": "发动概率35%/体力消耗量-60%",
        "zht_name": "驚人的體力A",
        "zht_effect": "發動機率35％/體力消耗量-60%",
        "en_name": "Miraculous Stamina A",
        "en_effect": "35% chance thatStamina Consumption -60%",
        "kr_name": "경이로운 스태미너 A",
        "kr_effect": "발동 확률 35％/스태미너 소비량 -60%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "驚異のスタミナB",
        "type": "A",
        "effect": "発動確率40％/スタミナ消費量-55％",
        "cname": "惊人体力B",
        "ceffect": "40%概率 自身体力消耗-55%",
        "zhs_name": "惊人的体力B",
        "zhs_effect": "发动概率40%/体力消耗量-55%",
        "zht_name": "驚人的體力B",
        "zht_effect": "發動機率40％/體力消耗量-55%",
        "en_name": "Miraculous Stamina B",
        "en_effect": "40% chance thatStamina Consumption -55%",
        "kr_name": "경이로운 스태미너 B",
        "kr_effect": "발동 확률 40％/스태미너 소비량 -55%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "驚異のスタミナC",
        "type": "A",
        "effect": "発動確率45％/スタミナ消費量-50％",
        "cname": "惊人体力C",
        "ceffect": "45%概率 自身体力消耗-50%",
        "zhs_name": "惊人的体力C",
        "zhs_effect": "发动概率45%/体力消耗量-50%",
        "zht_name": "驚人的體力C",
        "zht_effect": "發動機率45％/體力消耗量-50%",
        "en_name": "Miraculous Stamina C",
        "en_effect": "45% chance thatStamina Consumption -50%",
        "kr_name": "경이로운 스태미너 C",
        "kr_effect": "발동 확률 45％/스태미너 소비량 -50%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "驚異のスタミナD",
        "type": "A",
        "effect": "発動確率50％/スタミナ消費量-45％",
        "cname": "惊人体力D",
        "ceffect": "50%概率 自身体力消耗-45%",
        "zhs_name": "惊人的体力D",
        "zhs_effect": "发动概率50%/体力消耗量-45%",
        "zht_name": "驚人的體力D",
        "zht_effect": "發動機率50％/體力消耗量-45%",
        "en_name": "Miraculous Stamina D",
        "en_effect": "50% chance thatStamina Consumption -45%",
        "kr_name": "경이로운 스태미너 D",
        "kr_effect": "발동 확률 50％/스태미너 소비량 -45%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "驚異のスタミナE",
        "type": "A",
        "effect": "発動確率55％/スタミナ消費量-40％",
        "cname": "惊人体力E",
        "ceffect": "55%概率 自身体力消耗-40%",
        "zhs_name": "惊人的体力E",
        "zhs_effect": "发动概率55%/体力消耗量-40%",
        "zht_name": "驚人的體力E",
        "zht_effect": "發動機率55％/體力消耗量-40%",
        "en_name": "Miraculous Stamina E",
        "en_effect": "55% chance thatStamina Consumption -40%",
        "kr_name": "경이로운 스태미너 E",
        "kr_effect": "발동 확률 55％/스태미너 소비량 -40%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "驚異のスタミナE+",
        "type": "A",
        "effect": "発動確率55％/スタミナ消費量-45％",
        "cname": "惊人体力E+",
        "ceffect": "55%概率 自身体力消耗-45%",
        "zhs_name": "惊人的体力E+",
        "zhs_effect": "发动概率55%/体力消耗量-45%",
        "zht_name": "驚人的體力E+",
        "zht_effect": "發動機率55％/體力消耗量-45%",
        "en_name": "Miraculous Stamina E+",
        "en_effect": "Probability 55% make Stamina Consumption -45%",
        "kr_name": "경이로운 스태미너 E+",
        "kr_effect": "발동 확률 55％/스태미너 소비량 -45%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "驚異のスタミナF",
        "type": "A",
        "effect": "発動確率60％/スタミナ消費量-35％",
        "cname": "惊人体力F",
        "ceffect": "60%概率 自身体力消耗-35%",
        "zhs_name": "惊人的体力F",
        "zhs_effect": "发动概率60%/体力消耗量-35%",
        "zht_name": "驚人的體力F",
        "zht_effect": "發動機率60％/體力消耗量-35%",
        "en_name": "Miraculous Stamina F",
        "en_effect": "60% chance thatStamina Consumption -35%",
        "kr_name": "경이로운 스태미너 F",
        "kr_effect": "발동 확률 60％/스태미너 소비량 -35%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "裏の裏を突くフェイントA",
        "type": "A",
        "effect": "アタック時発動確率35％/テクニック+60％",
        "cname": "背身假动作A",
        "ceffect": "攻击时35%概率 自身技巧+60%",
        "zhs_name": "出其不意×2的假动作A",
        "zhs_effect": "攻击时发动概率35%/技术+60%",
        "zht_name": "攻其不備的假動作A",
        "zht_effect": "攻擊時發動機率35%/技巧+60%",
        "en_name": "Double Reverse Attack Feint A",
        "en_effect": "35% chance when Attacking,Technique +60%",
        "kr_name": "의표의 의표를 찌르는 페인트A",
        "kr_effect": "어택 시 발동 확률 35％/테크닉 +60%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "裏の裏を突くフェイントB",
        "type": "A",
        "effect": "アタック時発動確率40％/テクニック+55％",
        "cname": "背身假动作B",
        "ceffect": "攻击时40%概率 自身技巧+55%",
        "zhs_name": "出其不意×2的假动作B",
        "zhs_effect": "攻击时发动概率40%/技术+55%",
        "zht_name": "攻其不備的假動作B",
        "zht_effect": "攻擊時發動機率40%/技巧+55%",
        "en_name": "Double Reverse Attack Feint B",
        "en_effect": "40% chance when Attacking,Technique +55%",
        "kr_name": "의표의 의표를 찌르는 페인트B",
        "kr_effect": "어택 시 발동 확률 40％/테크닉 +55%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "裏の裏を突くフェイントC",
        "type": "A",
        "effect": "アタック時発動確率45％/テクニック+50％",
        "cname": "背身假动作C",
        "ceffect": "攻击时45%概率 自身技巧+50%",
        "zhs_name": "出其不意×2的假动作C",
        "zhs_effect": "攻击时发动概率45%/技术+50%",
        "zht_name": "攻其不備的假動作C",
        "zht_effect": "攻擊時發動機率45%/技巧+50%",
        "en_name": "Double Reverse Attack Feint C",
        "en_effect": "45% chance when Attacking,Technique +50%",
        "kr_name": "의표의 의표를 찌르는 페인트C",
        "kr_effect": "어택 시 발동 확률 45％/테크닉 +50%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "裏の裏を突くフェイントD",
        "type": "A",
        "effect": "アタック時発動確率50％/テクニック+45％",
        "cname": "背身假动作D",
        "ceffect": "攻击时50%概率 自身技巧+45%",
        "zhs_name": "出其不意×2的假动作D",
        "zhs_effect": "攻击时发动概率50%/技术+45%",
        "zht_name": "攻其不備的假動作D",
        "zht_effect": "攻擊時發動機率50%/技巧+45%",
        "en_name": "Double Reverse Attack Feint D",
        "en_effect": "50% chance when Attacking,Technique +45%",
        "kr_name": "의표의 의표를 찌르는 페인트D",
        "kr_effect": "어택 시 발동 확률 50％/테크닉 +45%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "裏の裏を突くフェイントE",
        "type": "A",
        "effect": "アタック時発動確率55％/テクニック+45％",
        "cname": "背身假动作E",
        "ceffect": "攻击时55%概率 自身技巧+45%",
        "zhs_name": "出其不意×2的假动作E",
        "zhs_effect": "攻击时发动概率55%/技术+45%",
        "zht_name": "攻其不備的假動作E",
        "zht_effect": "攻擊時發動機率55%/技巧+45%",
        "en_name": "Double Reverse Attack Feint E",
        "en_effect": "55% chance when Attacking,Technique +45%",
        "kr_name": "의표의 의표를 찌르는 페인트E",
        "kr_effect": "어택 시 발동 확률 55％/테크닉 +45%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "裏の裏を突くフェイントF",
        "type": "A",
        "effect": "アタック時発動確率60％/テクニック+35％",
        "cname": "背身假动作F",
        "ceffect": "攻击时60%概率 自身技巧+35%",
        "zhs_name": "出其不意×2的假动作F",
        "zhs_effect": "攻击时发动概率60%/技术+35%",
        "zht_name": "攻其不備的假動作F",
        "zht_effect": "攻擊時發動機率60%/技巧+35%",
        "en_name": "Double Reverse Attack Feint F",
        "en_effect": "60% chance when Attacking,Technique +35%",
        "kr_name": "의표의 의표를 찌르는 페인트F",
        "kr_effect": "어택 시 발동 확률 60％/테크닉 +35%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "裏の裏を突くフェイントG",
        "type": "A",
        "effect": "アタック時発動確率55％/テクニック+50％",
        "cname": "背身假动作G",
        "ceffect": "攻击时55%概率 自身技巧+50%",
        "zhs_name": "出其不意×2的假动作G",
        "zhs_effect": "攻击时发动概率55%/技术+50%",
        "zht_name": "攻其不備的假動作G",
        "zht_effect": "攻擊時發動機率55%/技巧+50%",
        "en_name": "Double Reverse Attack Feint G",
        "en_effect": "55% chance when Attacking,Technique +50%",
        "kr_name": "의표의 의표를 찌르는 페인트G",
        "kr_effect": "어택 시 발동 확률 55％/테크닉 +50%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "裏の裏を突くフェイントH",
        "type": "A",
        "effect": "アタック時発動確率55％/テクニック+60％",
        "cname": "背身假动作H",
        "ceffect": "攻击时55%概率 自身技巧+60%",
        "zhs_name": "出其不意×2的假动作H",
        "zhs_effect": "攻击时发动概率55%/技术+60%",
        "zht_name": "攻其不備的假動作H",
        "zht_effect": "攻擊時發動機率55%/技巧+60%",
        "en_name": "Double Reverse Attack Feint H",
        "en_effect": "55% chance when Attacking,Technique +60%",
        "kr_name": "의표의 의표를 찌르는 페인트H",
        "kr_effect": "어택 시 발동 확률 55％/테크닉 +60%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "完璧なレシーブA",
        "type": "A",
        "effect": "レシーブ時発動確率35％/テクニック+60％",
        "cname": "完美防守A",
        "ceffect": "防御时35%概率 自身技巧+60%",
        "zhs_name": "完美的接球A",
        "zhs_effect": "接球时发动概率35%/技术+60%",
        "zht_name": "完美的接球A",
        "zht_effect": "接球時發動機率35％/技巧+60%",
        "en_name": "Perfect Receive A",
        "en_effect": "35% chance when Receiving,Technique +60%",
        "kr_name": "완벽한 리시브 A",
        "kr_effect": "리시브 시 발동 확률 35％/테크닉 +60%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "完璧なレシーブB",
        "type": "A",
        "effect": "レシーブ時発動確率40％/テクニック+55％",
        "cname": "完美防守B",
        "ceffect": "防御时40%概率 自身技巧+55%",
        "zhs_name": "完美的接球B",
        "zhs_effect": "接球时发动概率40%/技术+55%",
        "zht_name": "完美的接球B",
        "zht_effect": "接球時發動機率40％/技巧+55%",
        "en_name": "Perfect Receive B",
        "en_effect": "40% chance when Receiving,Technique +55%",
        "kr_name": "완벽한 리시브 B",
        "kr_effect": "리시브 시 발동 확률 40％/테크닉 +55%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "完璧なレシーブD",
        "type": "A",
        "effect": "レシーブ時発動確率50％/テクニック+45％",
        "cname": "完美防守D",
        "ceffect": "防御时50%概率 自身技巧+45%",
        "zhs_name": "完美的接球D",
        "zhs_effect": "接球时发动概率50%/技术+45%",
        "zht_name": "完美的接球D",
        "zht_effect": "接球時發動機率50％/技巧+45%",
        "en_name": "Perfect Receive D",
        "en_effect": "50% chance when Receiving,Technique +45%",
        "kr_name": "완벽한 리시브 D",
        "kr_effect": "리시브 시 발동 확률 50％/테크닉 +45%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "完璧なレシーブE",
        "type": "A",
        "effect": "レシーブ時発動確率55%/テクニック+45%",
        "cname": "完美防守E",
        "ceffect": "防御时55%概率 自身技巧+45%",
        "zhs_name": "完美的接球E",
        "zhs_effect": "接球时发动概率55%/技术+45%",
        "zht_name": "完美的接球E",
        "zht_effect": "接球時發動機率55％/技巧+45%",
        "en_name": "Perfect Receive E",
        "en_effect": "55% chance when Receiving,Technique +45%",
        "kr_name": "완벽한 리시브 E",
        "kr_effect": "리시브 시 발동 확률 55％/테크닉 +45%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "完璧なレシーブF",
        "type": "A",
        "effect": "レシーブ時発動確率60％/テクニック+35％",
        "cname": "完美防守F",
        "ceffect": "防御时60%概率 自身技巧+35%",
        "zhs_name": "完美的接球F",
        "zhs_effect": "接球时发动概率60%/技术+35%",
        "zht_name": "完美的接球F",
        "zht_effect": "接球時發動機率60％/技巧+35%",
        "en_name": "Perfect Receive F",
        "en_effect": "60% chance when Receiving,Technique +35%",
        "kr_name": "완벽한 리시브 F",
        "kr_effect": "리시브 시 발동 확률 60％/테크닉 +35%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "灼熱のダンスA",
        "type": "A",
        "effect": "発動確率35％/相手のスタミナ消費量+60％",
        "cname": "灼热之舞A",
        "ceffect": "35%概率 对手体力消耗+60%",
        "zhs_name": "灼热的舞蹈A",
        "zhs_effect": "发动概率35%/对手的体力消耗量+60%",
        "zht_name": "火熱舞蹈A",
        "zht_effect": "發動機率35％/對手的體力消耗量+60%",
        "en_name": "Incandescent Dance A",
        "en_effect": "35% chance that Opponent's Stamina Consumption +60%",
        "kr_name": "작열하는 댄스 A",
        "kr_effect": "발동 확률 35％/상대방의 스태미너 소비량 +60%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "灼熱のダンスB",
        "type": "A",
        "effect": "発動確率40％/相手のスタミナ消費量+55％",
        "cname": "灼热之舞B",
        "ceffect": "40%概率 对手体力消耗+55%",
        "zhs_name": "灼热的舞蹈B",
        "zhs_effect": "发动概率40%/对手的体力消耗量+55%",
        "zht_name": "火熱舞蹈B",
        "zht_effect": "發動機率40％/對手的體力消耗量+55%",
        "en_name": "Incandescent Dance B",
        "en_effect": "40% chance that Opponent's Stamina Consumption +55%",
        "kr_name": "작열하는 댄스 B",
        "kr_effect": "발동 확률 40％/상대방의 스태미너 소비량 +55%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "灼熱のダンスC",
        "type": "A",
        "effect": "発動確率45％/相手のスタミナ消費量+50％",
        "cname": "灼热之舞C",
        "ceffect": "45%概率 对手体力消耗+50%",
        "zhs_name": "灼热的舞蹈C",
        "zhs_effect": "发动概率45%/对手的体力消耗量+50%",
        "zht_name": "火熱舞蹈C",
        "zht_effect": "發動機率45％/對手的體力消耗量+55%",
        "en_name": "Incandescent Dance C",
        "en_effect": "45% chance that Opponent's Stamina Consumption +50%",
        "kr_name": "작열하는 댄스 C",
        "kr_effect": "발동 확률 45％/상대방의 스태미너 소비량 +50%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "灼熱のダンスD",
        "type": "A",
        "effect": "発動確率50％/相手のスタミナ消費量+45％",
        "cname": "灼热之舞D",
        "ceffect": "50%概率 对手体力消耗+45%",
        "zhs_name": "灼热的舞蹈D",
        "zhs_effect": "发动概率50%/对手的体力消耗量+45%",
        "zht_name": "火熱舞蹈D",
        "zht_effect": "發動機率50％/對手的體力消耗量+45%",
        "en_name": "Incandescent Dance D",
        "en_effect": "50% chance that Opponent's Stamina Consumption +45%",
        "kr_name": "작열하는 댄스 D",
        "kr_effect": "발동 확률 50％/상대방의 스태미너 소비량 +45%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "灼熱のダンスE",
        "type": "A",
        "effect": "発動確率55％/相手のスタミナ消費量+45％",
        "cname": "灼热之舞E",
        "ceffect": "55%概率 对手体力消耗+45%",
        "zhs_name": "灼热的舞蹈E",
        "zhs_effect": "发动概率55%/对手的体力消耗量+45%",
        "zht_name": "火熱舞蹈E",
        "zht_effect": "發動機率55％/對手的體力消耗量+45%",
        "en_name": "Incandescent Dance E",
        "en_effect": "55% chance that Opponent's Stamina Consumption +45%",
        "kr_name": "작열하는 댄스 E",
        "kr_effect": "발동 확률 55％/상대방의 스태미너 소비량 +45%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "灼熱のダンスF",
        "type": "A",
        "effect": "発動確率60％/相手のスタミナ消費量+35％",
        "cname": "灼热之舞F",
        "ceffect": "60%概率 对手体力消耗+35%",
        "zhs_name": "灼热的舞蹈F",
        "zhs_effect": "发动概率60%/对手的体力消耗量+35%",
        "zht_name": "火熱舞蹈F",
        "zht_effect": "發動機率60％/對手的體力消耗量+35%",
        "en_name": "Incandescent Dance F",
        "en_effect": "60% chance that Opponent's Stamina Consumption +35%",
        "kr_name": "작열하는 댄스 F",
        "kr_effect": "발동 확률 60％/상대방의 스태미너 소비량 +35%",
        "pp_type": "",
        "property": "stm"
    },
    {
        "name": "強烈なプレッシャーA",
        "type": "A",
        "effect": "レシーブ時発動確率35%/相手のパワー-60%",
        "cname": "强大压力A",
        "ceffect": "防御时35%概率 对手力量-60%",
        "zhs_name": "强烈的压力A",
        "zhs_effect": "接球时发动概率35%/对手的力量-60%",
        "zht_name": "強烈的壓力A",
        "zht_effect": "接球時發動機率35％/對手的力量-60%",
        "en_name": "Intense Pressure A",
        "en_effect": "35% chance when Receiving, Opponent's Power -60%",
        "kr_name": "강렬한 압박 A",
        "kr_effect": "리시브 시 발동 확률 35％/상대방의 파워 -60%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈なプレッシャーB",
        "type": "A",
        "effect": "レシーブ時発動確率40%/相手のパワー-55%",
        "cname": "强大压力B",
        "ceffect": "防御时40%概率 对手力量-55%",
        "zhs_name": "强烈的压力B",
        "zhs_effect": "接球时发动概率40%/对手的力量-55%",
        "zht_name": "強烈的壓力B",
        "zht_effect": "接球時發動機率40％/對手的力量-55%",
        "en_name": "Intense Pressure B",
        "en_effect": "40% chance when Receiving, Opponent's Power -55%",
        "kr_name": "강렬한 압박 B",
        "kr_effect": "리시브 시 발동 확률 40％/상대방의 파워 -55%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈なプレッシャーC",
        "type": "A",
        "effect": "レシーブ時発動確率45%/相手のパワー-50%",
        "cname": "强大压力C",
        "ceffect": "防御时45%概率 对手力量-50%",
        "zhs_name": "强烈的压力C",
        "zhs_effect": "接球时发动概率45%/对手的力量-50%",
        "zht_name": "強烈的壓力C",
        "zht_effect": "接球時發動機率45％/對手的力量-50%",
        "en_name": "Intense Pressure C",
        "en_effect": "45% chance when Receiving, Opponent's Power -50%",
        "kr_name": "강렬한 압박 C",
        "kr_effect": "리시브 시 발동 확률 45％/상대방의 파워 -50%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈なプレッシャーD",
        "type": "A",
        "effect": "レシーブ時発動確率50%/相手のパワー-45%",
        "cname": "强大压力D",
        "ceffect": "防御时50%概率 对手力量-45%",
        "zhs_name": "强烈的压力D",
        "zhs_effect": "接球时发动概率50%/对手的力量-45%",
        "zht_name": "強烈的壓力D",
        "zht_effect": "接球時發動機率50％/對手的力量-45%",
        "en_name": "Intense Pressure D",
        "en_effect": "50% chance when Receiving, Opponent's Power -45%",
        "kr_name": "강렬한 압박 D",
        "kr_effect": "리시브 시 발동 확률 50％/상대방의 파워 -45%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈なプレッシャーE",
        "type": "A",
        "effect": "レシーブ時発動確率55%/相手のパワー-40%",
        "cname": "强大压力E",
        "ceffect": "防御时55%概率 对手力量-40%",
        "zhs_name": "强烈的压力E",
        "zhs_effect": "接球时发动概率55%/对手的力量-40%",
        "zht_name": "強烈的壓力E",
        "zht_effect": "接球時發動機率55％/對手的力量-40%",
        "en_name": "Intense Pressure E",
        "en_effect": "55% chance when Receiving, Opponent's Power -40%",
        "kr_name": "강렬한 압박 E",
        "kr_effect": "리시브 시 발동 확률 55％/상대방의 파워 -40%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈なプレッシャーF",
        "type": "A",
        "effect": "レシーブ時発動確率60%/相手のパワー-35%",
        "cname": "强大压力F",
        "ceffect": "防御时60%概率 对手力量-35%",
        "zhs_name": "强烈的压力F",
        "zhs_effect": "接球时发动概率60%/对手的力量-35%",
        "zht_name": "強烈的壓力F",
        "zht_effect": "接球時發動機率60％/對手的力量-35%",
        "en_name": "Intense Pressure F",
        "en_effect": "60% chance when Receiving, Opponent's Power -35%",
        "kr_name": "강렬한 압박 F",
        "kr_effect": "리시브 시 발동 확률 60％/상대방의 파워 -35%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈スパイクA",
        "type": "A",
        "effect": "アタック時発動確率35％/パワー+60％",
        "cname": "强力扣杀A",
        "ceffect": "攻击时35%概率 自身力量+60%",
        "zhs_name": "强力杀球A",
        "zhs_effect": "攻击时发动概率35%/力量+60%",
        "zht_name": "強力殺球A",
        "zht_effect": "攻擊時發動機率35%/力量+60%",
        "en_name": "Powerful Spike A",
        "en_effect": "35% chance when Attacking, Power +60%",
        "kr_name": "강렬 스파이크 A",
        "kr_effect": "어택 시 발동 확률 35％/파워 +60%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈スパイクB",
        "type": "A",
        "effect": "アタック時発動確率40％/パワー+55％",
        "cname": "强力扣杀B",
        "ceffect": "攻击时40%概率 自身力量+55%",
        "zhs_name": "强力杀球B",
        "zhs_effect": "攻击时发动概率40%/力量+55%",
        "zht_name": "強力殺球B",
        "zht_effect": "攻擊時發動機率40%/力量+55%",
        "en_name": "Powerful Spike B",
        "en_effect": "40% chance when Attacking, Power +55%",
        "kr_name": "강렬 스파이크 B",
        "kr_effect": "어택 시 발동 확률 40％/파워 +55%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈スパイクC",
        "type": "A",
        "effect": "アタック時発動確率45％/パワー+50％",
        "cname": "强力扣杀C",
        "ceffect": "攻击时45%概率 自身力量+50%",
        "zhs_name": "强力杀球C",
        "zhs_effect": "攻击时发动概率45%/力量+50%",
        "zht_name": "強力殺球C",
        "zht_effect": "攻擊時發動機率45%/力量+50%",
        "en_name": "Powerful Spike C",
        "en_effect": "45% chance when Attacking, Power +50%",
        "kr_name": "강렬 스파이크 C",
        "kr_effect": "어택 시 발동 확률 45％/파워 +50%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈スパイクD",
        "type": "A",
        "effect": "アタック時発動確率50％/パワー+45％",
        "cname": "强力扣杀D",
        "ceffect": "攻击时50%概率 自身力量+45%",
        "zhs_name": "强力杀球D",
        "zhs_effect": "攻击时发动概率50%/力量+45%",
        "zht_name": "強力殺球D",
        "zht_effect": "攻擊時發動機率50%/力量+45%",
        "en_name": "Powerful Spike D",
        "en_effect": "50% chance when Attacking, Power +45%",
        "kr_name": "강렬 스파이크 D",
        "kr_effect": "어택 시 발동 확률 50％/파워 +45%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈スパイクE",
        "type": "A",
        "effect": "アタック時発動確率55％/パワー+45％",
        "cname": "强力扣杀E",
        "ceffect": "攻击时55%概率 自身力量+45%",
        "zhs_name": "强力杀球E",
        "zhs_effect": "攻击时发动概率55%/力量+45%",
        "zht_name": "強力殺球E",
        "zht_effect": "攻擊時發動機率55%/力量+45%",
        "en_name": "Powerful Spike E",
        "en_effect": "55% chance when Attacking, Power +45%",
        "kr_name": "강렬 스파이크 E",
        "kr_effect": "어택 시 발동 확률 55％/파워 +45%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈スパイクF",
        "type": "A",
        "effect": "アタック時発動確率60％/パワー+35％",
        "cname": "强力扣杀F",
        "ceffect": "攻击时60%概率 自身力量+35%",
        "zhs_name": "强力杀球F",
        "zhs_effect": "攻击时发动概率60%/力量+35%",
        "zht_name": "強力殺球F",
        "zht_effect": "攻擊時發動機率60%/力量+35%",
        "en_name": "Powerful Spike F",
        "en_effect": "60% chance when Attacking, Power +35%",
        "kr_name": "강렬 스파이크 F",
        "kr_effect": "어택 시 발동 확률 60％/파워 +35%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈スパイクG",
        "type": "A",
        "effect": "アタック時発動確率55％/パワー+50％",
        "cname": "强力扣杀G",
        "ceffect": "攻击时55%概率 自身力量+50%",
        "zhs_name": "强力杀球G",
        "zhs_effect": "攻击时发动概率55%/力量+50%",
        "zht_name": "強力殺球G",
        "zht_effect": "攻擊時發動機率55%/力量+50%",
        "en_name": "Powerful Spike G",
        "en_effect": "55% chance when Attacking, Power +50%",
        "kr_name": "강렬 스파이크 G",
        "kr_effect": "어택 시 발동 확률 55％/파워 +50%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "強烈スパイクH",
        "type": "A",
        "effect": "アタック時発動確率55％/パワー+60％",
        "cname": "强力扣杀H",
        "ceffect": "攻击时55%概率 自身力量+60%",
        "zhs_name": "强力杀球H",
        "zhs_effect": "攻击时发动概率55%/力量+60%",
        "zht_name": "強力殺球H",
        "zht_effect": "攻擊時發動機率55%/力量+60%",
        "en_name": "Powerful Spike H",
        "en_effect": "55% chance when Attacking, Power +60%",
        "kr_name": "강렬 스파이크 H",
        "kr_effect": "어택 시 발동 확률 55％/파워 +60%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "高度な心理戦A",
        "type": "A",
        "effect": "アタック時発動確率35％/相手のテクニック-60％",
        "cname": "高等心战A",
        "ceffect": "攻击时35%概率 对手技巧-60%",
        "zhs_name": "高度心理战A",
        "zhs_effect": "攻击时发动概率35%/对手的技术-60%",
        "zht_name": "高明的心理戰A",
        "zht_effect": "攻擊時發動機率35%/對手的技巧-60%",
        "en_name": "Advanced Strategy A",
        "en_effect": "35% chance when Attacking, Opponent's Technique -60%",
        "kr_name": "고도의 심리전 A",
        "kr_effect": "어택 시 발동 확률 35％/상대방의 테크닉 -60%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "高度な心理戦B",
        "type": "A",
        "effect": "アタック時発動確率40％/相手のテクニック-55％",
        "cname": "高等心战B",
        "ceffect": "攻击时40%概率 对手技巧-55%",
        "zhs_name": "高度心理战B",
        "zhs_effect": "攻击时发动概率40%/对手的技术-55%",
        "zht_name": "高明的心理戰B",
        "zht_effect": "攻擊時發動機率40%/對手的技巧-55%",
        "en_name": "Advanced Strategy B",
        "en_effect": "40% chance when Attacking, Opponent's Technique -55%",
        "kr_name": "고도의 심리전 B",
        "kr_effect": "어택 시 발동 확률 40％/상대방의 테크닉 -55%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "高度な心理戦C",
        "type": "A",
        "effect": "アタック時発動確率45％/相手のテクニック-50％",
        "cname": "高等心战C",
        "ceffect": "攻击时45%概率 对手技巧-50%",
        "zhs_name": "高度心理战C",
        "zhs_effect": "攻击时发动概率45%/对手的技术-50%",
        "zht_name": "高明的心理戰C",
        "zht_effect": "攻擊時發動機率45%/對手的技巧-50%",
        "en_name": "Advanced Strategy C",
        "en_effect": "45% chance when Attacking, Opponent's Technique -50%",
        "kr_name": "고도의 심리전 C",
        "kr_effect": "어택 시 발동 확률 45％/상대방의 테크닉 -50%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "高度な心理戦D",
        "type": "A",
        "effect": "アタック時発動確率50％/相手のテクニック-45％",
        "cname": "高等心战D",
        "ceffect": "攻击时50%概率 对手技巧-45%",
        "zhs_name": "高度心理战D",
        "zhs_effect": "攻击时发动概率50%/对手的技术-45%",
        "zht_name": "高明的心理戰D",
        "zht_effect": "攻擊時發動機率50%/對手的技巧-45%",
        "en_name": "Advanced Strategy D",
        "en_effect": "50% chance when Attacking, Opponent's Technique -45%",
        "kr_name": "고도의 심리전 D",
        "kr_effect": "어택 시 발동 확률 50％/상대방의 테크닉 -45%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "高度な心理戦E",
        "type": "A",
        "effect": "アタック時発動確率55％/相手のテクニック-40％",
        "cname": "高等心战E",
        "ceffect": "攻击时55%概率 对手技巧-40%",
        "zhs_name": "高度心理战E",
        "zhs_effect": "攻击时发动概率55%/对手的技术-40%",
        "zht_name": "高明的心理戰E",
        "zht_effect": "攻擊時發動機率55%/對手的技巧-40%",
        "en_name": "Advanced Strategy E",
        "en_effect": "55% chance when Attacking, Opponent's Technique -40%",
        "kr_name": "고도의 심리전 E",
        "kr_effect": "어택 시 발동 확률 55％/상대방의 테크닉 -40%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "高度な心理戦F",
        "type": "A",
        "effect": "アタック時発動確率60％/相手のテクニック-35％",
        "cname": "高等心战F",
        "ceffect": "攻击时60%概率 对手技巧-35%",
        "zhs_name": "高度心理战F",
        "zhs_effect": "攻击时发动概率60%/对手的技术-35%",
        "zht_name": "高明的心理戰F",
        "zht_effect": "攻擊時發動機率60%/對手的技巧-35%",
        "en_name": "Advanced Strategy F",
        "en_effect": "60% chance when Attacking, Opponent's Technique -35%",
        "kr_name": "고도의 심리전 F",
        "kr_effect": "어택 시 발동 확률 60％/상대방의 테크닉 -35%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "観客総立ちB",
        "type": "A",
        "effect": "発動確率40％/テンション上昇量+55％",
        "cname": "观众欢呼B",
        "ceffect": "40%概率 蓄气量+55%",
        "zhs_name": "观众全体起立B",
        "zhs_effect": "发动概率40%/情绪上升量+55%",
        "zht_name": "全場觀眾起身站立B",
        "zht_effect": "發動機率40％/情緒上升量+55%",
        "en_name": "Spectators All Standing B",
        "en_effect": "40% chance that Tension Gauge Increase +55%",
        "kr_name": "관객 전체 기립 B",
        "kr_effect": "발동 확률 40％/텐션 상승량 +55%",
        "pp_type": "",
        "property": "apl"
    },
    {
        "name": "観客総立ちC",
        "type": "A",
        "effect": "発動確率45％/テンション上昇量+50％",
        "cname": "观众欢呼C",
        "ceffect": "45%概率 蓄气量+50%",
        "zhs_name": "观众全体起立C",
        "zhs_effect": "发动概率45%/情绪上升量+50%",
        "zht_name": "全場觀眾起身站立C",
        "zht_effect": "發動機率45％/情緒上升量+50%",
        "en_name": "Spectators All Standing C",
        "en_effect": "45% chance that Tension Gauge Increase +50%",
        "kr_name": "관객 전체 기립 C",
        "kr_effect": "발동 확률 45％/텐션 상승량 +50%",
        "pp_type": "",
        "property": "apl"
    },
    {
        "name": "観客総立ちD",
        "type": "A",
        "effect": "発動確率50％/テンション上昇量+45％",
        "cname": "观众欢呼D",
        "ceffect": "50%概率 蓄气量+45%",
        "zhs_name": "观众全体起立D",
        "zhs_effect": "发动概率50%/情绪上升量+45%",
        "zht_name": "全場觀眾起身站立D",
        "zht_effect": "發動機率50％/情緒上升量+45%",
        "en_name": "Spectators All Standing D",
        "en_effect": "50% chance that Tension Gauge Increase +45%",
        "kr_name": "관객 전체 기립 D",
        "kr_effect": "발동 확률 50％/텐션 상승량 +45%",
        "pp_type": "",
        "property": "apl"
    },
    {
        "name": "観客総立ちE",
        "type": "A",
        "effect": "発動確率55％/テンション上昇量+45％",
        "cname": "观众欢呼E",
        "ceffect": "55%概率 蓄气量+45%",
        "zhs_name": "观众全体起立E",
        "zhs_effect": "发动概率55%/情绪上升量+45%",
        "zht_name": "全場觀眾起身站立E",
        "zht_effect": "發動機率55％/情緒上升量+45%",
        "en_name": "Spectators All Standing E",
        "en_effect": "55% chance that Tension Gauge Increase +45%",
        "kr_name": "관객 전체 기립 E",
        "kr_effect": "발동 확률 55％/텐션 상승량 +45%",
        "pp_type": "",
        "property": "apl"
    },
    {
        "name": "観客総立ちF",
        "type": "A",
        "effect": "発動確率60％/テンション上昇量+35％",
        "cname": "观众欢呼F",
        "ceffect": "60%概率 蓄气量+35%",
        "zhs_name": "观众全体起立F",
        "zhs_effect": "发动概率60%/情绪上升量+35%",
        "zht_name": "全場觀眾起身站立F",
        "zht_effect": "發動機率60％/情緒上升量+35%",
        "en_name": "Spectators All Standing F",
        "en_effect": "60% chance that Tension Gauge Increase +35%",
        "kr_name": "관객 전체 기립 F",
        "kr_effect": "발동 확률 60％/텐션 상승량 +35%",
        "pp_type": "",
        "property": "apl"
    },
    {
        "name": "不動のレシーブA",
        "type": "A",
        "effect": "レシーブ時発動確率60%/パワー+35%",
        "cname": "不动防御A",
        "ceffect": "防御时35%概率 自身力量+60%",
        "zhs_name": "坚定的接球A",
        "zhs_effect": "接球时发动概率35%/力量+60%",
        "zht_name": "平穩的接球A",
        "zht_effect": "接球時發動機率35％/力量+60%",
        "en_name": "Firm Receive A",
        "en_effect": "35% chance when Receiving, Power +60%",
        "kr_name": "부동의 리시브 A",
        "kr_effect": "리시브 시 발동 확률 35％/파워 +60%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "不動のレシーブB",
        "type": "A",
        "effect": "レシーブ時発動確率40%/パワー+55%",
        "cname": "不动防御B",
        "ceffect": "防御时40%概率 自身力量+55%",
        "zhs_name": "坚定的接球B",
        "zhs_effect": "接球时发动概率40%/力量+55%",
        "zht_name": "平穩的接球B",
        "zht_effect": "接球時發動機率40％/力量+55%",
        "en_name": "Firm Receive B",
        "en_effect": "40% chance when Receiving, Power +55%",
        "kr_name": "부동의 리시브 B",
        "kr_effect": "리시브 시 발동 확률 40％/파워 +55%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "不動のレシーブC",
        "type": "A",
        "effect": "レシーブ時発動確率45%/パワー+50%",
        "cname": "不动防御C",
        "ceffect": "防御时45%概率 自身力量+50%",
        "zhs_name": "坚定的接球C",
        "zhs_effect": "接球时发动概率45%/力量+50%",
        "zht_name": "平穩的接球C",
        "zht_effect": "接球時發動機率45％/力量+50%",
        "en_name": "Firm Receive C",
        "en_effect": "45% chance when Receiving, Power +50%",
        "kr_name": "부동의 리시브 C",
        "kr_effect": "리시브 시 발동 확률 45％/파워 +50%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "不動のレシーブD",
        "type": "A",
        "effect": "レシーブ時発動確率50%/パワー+45%",
        "cname": "不动防御D",
        "ceffect": "防御时50%概率 自身力量+45%",
        "zhs_name": "坚定的接球D",
        "zhs_effect": "接球时发动概率50%/力量+45%",
        "zht_name": "平穩的接球D",
        "zht_effect": "接球時發動機率50％/力量+45%",
        "en_name": "Firm Receive D",
        "en_effect": "50% chance when Receiving, Power +45%",
        "kr_name": "부동의 리시브 D",
        "kr_effect": "리시브 시 발동 확률 50％/파워 +45%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "不動のレシーブE",
        "type": "A",
        "effect": "レシーブ時発動確率55%/パワー+45%",
        "cname": "不动防御E",
        "ceffect": "防御时55%概率 自身力量+45%",
        "zhs_name": "坚定的接球E",
        "zhs_effect": "接球时发动概率55%/力量+45%",
        "zht_name": "平穩的接球E",
        "zht_effect": "接球時發動機率55％/力量+45%",
        "en_name": "Firm Receive E",
        "en_effect": "55% chance when Receiving, Power +45%",
        "kr_name": "부동의 리시브 E",
        "kr_effect": "리시브 시 발동 확률 55％/파워 +45%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "不動のレシーブF",
        "type": "A",
        "effect": "レシーブ時発動確率60%/パワー+35%",
        "cname": "不动防御F",
        "ceffect": "防御时60%概率 自身力量+35%",
        "zhs_name": "坚定的接球F",
        "zhs_effect": "接球时发动概率60%/力量+35%",
        "zht_name": "平穩的接球F",
        "zht_effect": "接球時發動機率60％/力量+35%",
        "en_name": "Firm Receive F",
        "en_effect": "60% chance when Receiving, Power +35%",
        "kr_name": "부동의 리시브 F",
        "kr_effect": "리시브 시 발동 확률 60％/파워 +35%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "鉄壁のレシーブA",
        "type": "A",
        "effect": "レシーブ時発動確率35％/テクニック+60％",
        "cname": "铁壁防守A",
        "ceffect": "防御时35%概率 自身技巧+60%",
        "zhs_name": "铁壁的接球A",
        "zhs_effect": "接球时发动概率35%/技术+60%",
        "zht_name": "鐵壁的接球A",
        "zht_effect": "接球時發動機率35％/技巧+60%",
        "en_name": "Invulnerable Receive A",
        "en_effect": "35% chance when Receiving, Technique +60%",
        "kr_name": "철벽의 리시브 A",
        "kr_effect": "리시브 시 발동 확률 35％/테크닉 +60%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "鉄壁のレシーブB",
        "type": "A",
        "effect": "レシーブ時発動確率40％/テクニック+55％",
        "cname": "铁壁防守B",
        "ceffect": "防御时40%概率 自身技巧+55%",
        "zhs_name": "铁壁的接球B",
        "zhs_effect": "接球时发动概率40%/技术+55%",
        "zht_name": "鐵壁的接球B",
        "zht_effect": "接球時發動機率40％/技巧+55%",
        "en_name": "Invulnerable Receive B",
        "en_effect": "40% chance when Receiving, Technique +55%",
        "kr_name": "철벽의 리시브 B",
        "kr_effect": "리시브 시 발동 확률 40％/테크닉 +55%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "鉄壁のレシーブC",
        "type": "A",
        "effect": "レシーブ時発動確率45％/テクニック+50％",
        "cname": "铁壁防守C",
        "ceffect": "防御时45%概率 自身技巧+50%",
        "zhs_name": "铁壁的接球C",
        "zhs_effect": "接球时发动概率45%/技术+50%",
        "zht_name": "鐵壁的接球C",
        "zht_effect": "接球時發動機率45％/技巧+50%",
        "en_name": "Invulnerable Receive C",
        "en_effect": "45% chance when Receiving, Technique +50%",
        "kr_name": "철벽의 리시브 C",
        "kr_effect": "리시브 시 발동 확률 45％/테크닉 +50%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "鉄壁のレシーブD",
        "type": "A",
        "effect": "レシーブ時発動確率50％/テクニック+45％",
        "cname": "铁壁防守D",
        "ceffect": "防御时50%概率 自身技巧+45%",
        "zhs_name": "铁壁的接球D",
        "zhs_effect": "接球时发动概率50%/技术+45%",
        "zht_name": "鐵壁的接球D",
        "zht_effect": "接球時發動機率50％/技巧+45%",
        "en_name": "Invulnerable Receive D",
        "en_effect": "50% chance when Receiving, Technique +45%",
        "kr_name": "철벽의 리시브 D",
        "kr_effect": "리시브 시 발동 확률 50％/테크닉 +45%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "鉄壁のレシーブE",
        "type": "A",
        "effect": "レシーブ時発動確率55％/テクニック+45％",
        "cname": "铁壁防守E",
        "ceffect": "防御时55%概率 自身技巧+45%",
        "zhs_name": "铁壁的接球E",
        "zhs_effect": "接球时发动概率55%/技术+45%",
        "zht_name": "鐵壁的接球E",
        "zht_effect": "接球時發動機率55％/技巧+45%",
        "en_name": "Invulnerable Receive E",
        "en_effect": "55% chance when Receiving, Technique +45%",
        "kr_name": "철벽의 리시브 E",
        "kr_effect": "리시브 시 발동 확률 55％/테크닉 +45%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "鉄壁のレシーブF",
        "type": "A",
        "effect": "レシーブ時発動確率60％/テクニック+35％",
        "cname": "铁壁防守F",
        "ceffect": "防御时60%概率 自身技巧+35%",
        "zhs_name": "铁壁的接球F",
        "zhs_effect": "接球时发动概率60%/技术+35%",
        "zht_name": "鐵壁的接球F",
        "zht_effect": "接球時發動機率60％/技巧+35%",
        "en_name": "Invulnerable Receive F",
        "en_effect": "60% chance when Receiving, Technique +35%",
        "kr_name": "철벽의 리시브 F",
        "kr_effect": "리시브 시 발동 확률 60％/테크닉 +35%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "天才的な先読みB",
        "type": "A",
        "effect": "レシーブ時発動確率40%/相手のテクニック-55%",
        "cname": "天才预判B",
        "ceffect": "防御时40%概率 对手技巧-55%",
        "zhs_name": "天才的预判B",
        "zhs_effect": "接球时发动概率40%/对手的技术-55%",
        "zht_name": "天才的預判B",
        "zht_effect": "接球時發動機率40％/對手的技巧-55%",
        "en_name": "Ingenious Foresight B",
        "en_effect": "40% chance when Receiving, Opponent's Technique -55%",
        "kr_name": "천재적인 예측 B",
        "kr_effect": "리시브 시 발동 확률 40％/상대방의 테크닉 -55%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "天才的な先読みC",
        "type": "A",
        "effect": "レシーブ時発動確率45%/相手のテクニック-50%",
        "cname": "天才预判C",
        "ceffect": "防御时45%概率 对手技巧-50%",
        "zhs_name": "天才的预判C",
        "zhs_effect": "接球时发动概率45%/对手的技术-50%",
        "zht_name": "天才的預判C",
        "zht_effect": "接球時發動機率45％/對手的技巧-50%",
        "en_name": "Ingenious Foresight C",
        "en_effect": "45% chance when Receiving, Opponent's Technique -50%",
        "kr_name": "천재적인 예측 C",
        "kr_effect": "리시브 시 발동 확률 45％/상대방의 테크닉 -50%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "天才的な先読みD",
        "type": "A",
        "effect": "レシーブ時発動確率50%/相手のテクニック-45%",
        "cname": "天才预判D",
        "ceffect": "防御时50%概率 对手技巧-45%",
        "zhs_name": "天才的预判D",
        "zhs_effect": "接球时发动概率50%/对手的技术-45%",
        "zht_name": "天才的預判D",
        "zht_effect": "接球時發動機率50％/對手的技巧-45%",
        "en_name": "Ingenious Foresight D",
        "en_effect": "50% chance when Receiving, Opponent's Technique -45%",
        "kr_name": "천재적인 예측 D",
        "kr_effect": "리시브 시 발동 확률 50％/상대방의 테크닉 -45%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "天才的な先読みE",
        "type": "A",
        "effect": "レシーブ時発動確率55%/相手のテクニック-40%",
        "cname": "天才预判E",
        "ceffect": "防御时55%概率 对手技巧-40%",
        "zhs_name": "天才的预判E",
        "zhs_effect": "接球时发动概率55%/对手的技术-40%",
        "zht_name": "天才的預判E",
        "zht_effect": "接球時發動機率55％/對手的技巧-40%",
        "en_name": "Ingenious Foresight E",
        "en_effect": "55% chance when Receiving, Opponent's Technique -40%",
        "kr_name": "천재적인 예측 E",
        "kr_effect": "리시브 시 발동 확률 55％/상대방의 테크닉 -40%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "天才的な先読みF",
        "type": "A",
        "effect": "レシーブ時発動確率60%/相手のテクニック-35%",
        "cname": "天才预判F",
        "ceffect": "防御时60%概率 对手技巧-35%",
        "zhs_name": "天才的预判F",
        "zhs_effect": "接球时发动概率60%/对手的技术-35%",
        "zht_name": "天才的預判F",
        "zht_effect": "接球時發動機率60％/對手的技巧-35%",
        "en_name": "Ingenious Foresight F",
        "en_effect": "60% chance when Receiving, Opponent's Technique -35%",
        "kr_name": "천재적인 예측 F",
        "kr_effect": "리시브 시 발동 확률 60％/상대방의 테크닉 -35%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "圧倒的な気迫A",
        "type": "A",
        "effect": "アタック時発動確率35％/相手のパワー-60％",
        "cname": "压倒性的气魄A",
        "ceffect": "攻击时35%概率 对手力量-60%",
        "zhs_name": "压倒性的气势A",
        "zhs_effect": "攻击时发动概率35%/对手的力量-60%",
        "zht_name": "壓倒性的氣勢A",
        "zht_effect": "攻擊時發動機率35%/對手的力量-60%",
        "en_name": "Overwhelming Spirit A",
        "en_effect": "35% chance when Attacking, Opponent's Power -60%",
        "kr_name": "압도적인 기백 A",
        "kr_effect": "어택 시 발동 확률 35％/상대방의 파워 -60%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "圧倒的な気迫B",
        "type": "A",
        "effect": "アタック時発動確率40％/相手のパワー-55％",
        "cname": "压倒性的气魄B",
        "ceffect": "攻击时40%概率 对手力量-55%",
        "zhs_name": "压倒性的气势B",
        "zhs_effect": "攻击时发动概率40%/对手的力量-55%",
        "zht_name": "壓倒性的氣勢B",
        "zht_effect": "攻擊時發動機率40%/對手的力量-55%",
        "en_name": "Overwhelming Spirit B",
        "en_effect": "40% chance when Attacking, Opponent's Power -55%",
        "kr_name": "압도적인 기백 B",
        "kr_effect": "어택 시 발동 확률 40％/상대방의 파워 -55%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "圧倒的な気迫C",
        "type": "A",
        "effect": "アタック時発動確率45％/相手のパワー-50％",
        "cname": "压倒性的气魄C",
        "ceffect": "攻击时45%概率 对手力量-50%",
        "zhs_name": "压倒性的气势C",
        "zhs_effect": "攻击时发动概率45%/对手的力量-50%",
        "zht_name": "壓倒性的氣勢C",
        "zht_effect": "攻擊時發動機率45%/對手的力量-50%",
        "en_name": "Overwhelming Spirit C",
        "en_effect": "45% chance when Attacking, Opponent's Power -50%",
        "kr_name": "압도적인 기백 C",
        "kr_effect": "어택 시 발동 확률 45％/상대방의 파워 -50%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "圧倒的な気迫D",
        "type": "A",
        "effect": "アタック時発動確率50％/相手のパワー-45％",
        "cname": "压倒性的气魄D",
        "ceffect": "攻击时50%概率 对手力量-45%",
        "zhs_name": "压倒性的气势D",
        "zhs_effect": "攻击时发动概率50%/对手的力量-45%",
        "zht_name": "壓倒性的氣勢D",
        "zht_effect": "攻擊時發動機率50%/對手的力量-45%",
        "en_name": "Overwhelming Spirit D",
        "en_effect": "50% chance when Attacking, Opponent's Power -45%",
        "kr_name": "압도적인 기백 D",
        "kr_effect": "어택 시 발동 확률 50％/상대방의 파워 -45%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "圧倒的な気迫E",
        "type": "A",
        "effect": "アタック時発動確率55％/相手のパワー-40％",
        "cname": "压倒性的气魄E",
        "ceffect": "攻击时55%概率 对手力量-40%",
        "zhs_name": "压倒性的气势E",
        "zhs_effect": "攻击时发动概率55%/对手的力量-40%",
        "zht_name": "壓倒性的氣勢E",
        "zht_effect": "攻擊時發動機率55%/對手的力量-40%",
        "en_name": "Overwhelming Spirit E",
        "en_effect": "55% chance when Attacking, Opponent's Power -40%",
        "kr_name": "압도적인 기백 E",
        "kr_effect": "어택 시 발동 확률 55％/상대방의 파워 -40%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "圧倒的な気迫F",
        "type": "A",
        "effect": "アタック時発動確率60％/相手のパワー-35％",
        "cname": "压倒性的气魄F",
        "ceffect": "攻击时60%概率 对手力量-35%",
        "zhs_name": "压倒性的气势F",
        "zhs_effect": "攻击时发动概率60%/对手的力量-35%",
        "zht_name": "壓倒性的氣勢F",
        "zht_effect": "攻擊時發動機率60%/對手的力量-35%",
        "en_name": "Overwhelming Spirit F",
        "en_effect": "60% chance when Attacking, Opponent's Power -35%",
        "kr_name": "압도적인 기백 F",
        "kr_effect": "어택 시 발동 확률 60％/상대방의 파워 -35%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "クリティカルヒットB",
        "type": "A",
        "effect": "アタック時発動確率25％/パワー+40％",
        "cname": "强力一击B",
        "ceffect": "攻击时25%概率 自身力量+40%",
        "zhs_name": "致命的击球B",
        "zhs_effect": "攻击时发动概率25%/力量+40%",
        "zht_name": "會心一擊B",
        "zht_effect": "攻擊時發動機率25%/力量+40%",
        "en_name": "Critical Hit B",
        "en_effect": "25% chance when Attacking, Power +40%",
        "kr_name": "크리티컬 힛 B",
        "kr_effect": "어택 시 발동 확률 25％/파워 +40%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "クリティカルヒットE",
        "type": "A",
        "effect": "アタック時発動確率40％/パワー+25％",
        "cname": "强力一击E",
        "ceffect": "攻击时40%概率 自身力量+25%",
        "zhs_name": "致命的击球E",
        "zhs_effect": "攻击时发动概率40%/力量+25%",
        "zht_name": "會心一擊E",
        "zht_effect": "攻擊時發動機率40%/力量+25%",
        "en_name": "Critical Hit E",
        "en_effect": "40% chance when Attacking, Power +35%",
        "kr_name": "크리티컬 힛 E",
        "kr_effect": "어택 시 발동 확률 40％/파워 +25%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "W・疲れ知らずの猛攻G",
        "type": "A",
        "effect": "アタック時発動確率40％/パワー+40％、スタミナ消費量-40％",
        "cname": "W・不知疲倦的猛攻G",
        "ceffect": "攻击时40%概率 自身力量+40%、自身体力消耗-40%（同时触发）",
        "zhs_name": "W·不知疲倦的猛攻G",
        "zhs_effect": "攻击时发动概率40%/力量+40%、体力消耗量-40%",
        "zht_name": "W‧不知疲勞的猛攻G",
        "zht_effect": "攻擊時發動機率40%/力量+40%、體力消耗量-40%",
        "en_name": "W Untiring Ferocious Attack G",
        "en_effect": "40% chance when Attacking,Power +40%, Stamina Consumption -40%",
        "kr_name": "W-지칠 줄 모르는 맹공 G",
        "kr_effect": "어택 시 발동 확률 40％/파워 +40%,스태미너 소비량 -40%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "W・洗練された技巧G",
        "type": "A",
        "effect": "アタック時発動確率40％/テクニック+40％、スタミナ消費量-40％",
        "cname": "W・千锤百炼的技巧",
        "ceffect": "攻击时40%概率 自身技巧+40%、自身体力消耗-40%（同时触发）",
        "zhs_name": "W·精炼的技巧G",
        "zhs_effect": "攻击时发动概率40%/技术+40%、体力消耗量-40%",
        "zht_name": "W‧洗練的技巧G",
        "zht_effect": "攻擊時發動機率40%/技巧+40%、體力消耗量-40%",
        "en_name": "W Refined Skill G",
        "en_effect": "40% chance when Attacking, Technique +40%,Stamina Consumption -40%",
        "kr_name": "W・세련된 기교 G",
        "kr_effect": "어택 시 발동 확률 40％/테크닉 +40%,스태미너 소비량 -40%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "内から湧き上がるスタミナ3",
        "type": "P",
        "effect": "スタミナ消費量-10％",
        "cname": "展现体力3",
        "ceffect": "自身体力消耗-10%",
        "zhs_name": "从深处涌现的体力3",
        "zhs_effect": "体力消耗量-10%",
        "zht_name": "從體內湧現出的體力3",
        "zht_effect": "體力消耗量-10%",
        "en_name": "Stamina from Within 3",
        "en_effect": "Stamina Consumption -10%",
        "kr_name": "솟아나는 스태미너 3",
        "kr_effect": "스태미너 소비량 -10%",
        "pp_type": "7",
        "property": "stm"
    },
    {
        "name": "内から湧き上がるスタミナ4",
        "type": "P",
        "effect": "スタミナ消費量-10％",
        "cname": "展现体力4",
        "ceffect": "自身体力消耗-10%",
        "zhs_name": "从深处涌现的体力4",
        "zhs_effect": "体力消耗量-10%",
        "zht_name": "從體內湧現出的體力4",
        "zht_effect": "體力消耗量-10%",
        "en_name": "Stamina from Within 4",
        "en_effect": "Stamina Consumption -10%",
        "kr_name": "솟아나는 스태미너 4",
        "kr_effect": "스태미너 소비량 -10%",
        "pp_type": "7",
        "property": "stm"
    },
    {
        "name": "内から湧き上がるスタミナ5",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "展现体力5",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "从深处涌现的体力5",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "從體內湧現出的體力5",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Stamina from Within 5",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "솟아나는 스태미너 5",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "内から湧き上がるスタミナ6",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "展现体力6",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "从深处涌现的体力6",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "從體內湧現出的體力6",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Stamina from Within 6",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "솟아나는 스태미너 6",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "隠しきれない魅力3",
        "type": "P",
        "effect": "アピール+10％",
        "cname": "隐藏之美3",
        "ceffect": "魅力+10%",
        "zhs_name": "无法遮掩的魅力3",
        "zhs_effect": "魅力+10%",
        "zht_name": "藏不住的吸引力3",
        "zht_effect": "魅力+10%",
        "en_name": "Unconcealable Charm 3",
        "en_effect": "Appeal +10%",
        "kr_name": "감출 수 없는 매력 3",
        "kr_effect": "어필 +10%",
        "pp_type": "7",
        "property": "apl"
    },
    {
        "name": "隠しきれない魅力4",
        "type": "P",
        "effect": "アピール+10％",
        "cname": "隐藏之美4",
        "ceffect": "魅力+10%",
        "zhs_name": "无法遮掩的魅力4",
        "zhs_effect": "魅力+10%",
        "zht_name": "藏不住的吸引力4",
        "zht_effect": "魅力+10%",
        "en_name": "Unconcealable Charm 4",
        "en_effect": "Appeal +10%",
        "kr_name": "감출 수 없는 매력 4",
        "kr_effect": "어필 +10%",
        "pp_type": "7",
        "property": "apl"
    },
    {
        "name": "隠しきれない魅力5",
        "type": "P",
        "effect": "アピール+11％",
        "cname": "隐藏之美5",
        "ceffect": "魅力+11%",
        "zhs_name": "无法遮掩的魅力5",
        "zhs_effect": "魅力+11%",
        "zht_name": "藏不住的吸引力5",
        "zht_effect": "魅力+11%",
        "en_name": "Unconcealable Charm 5",
        "en_effect": "Appeal +11%",
        "kr_name": "감출 수 없는 매력 5",
        "kr_effect": "어필 +11%",
        "pp_type": "8",
        "property": "apl"
    },
    {
        "name": "隠しきれない魅力6",
        "type": "P",
        "effect": "アピール+10％",
        "cname": "隐藏之美6",
        "ceffect": "魅力+10%",
        "zhs_name": "无法遮掩的魅力6",
        "zhs_effect": "魅力+11%",
        "zht_name": "藏不住的吸引力6",
        "zht_effect": "魅力+11%",
        "en_name": "Unconcealable Charm 6",
        "en_effect": "Appeal +11%",
        "kr_name": "감출 수 없는 매력 6",
        "kr_effect": "어필 +11%",
        "pp_type": "7",
        "property": "apl"
    },
    {
        "name": "閃きのテクニック3",
        "type": "P",
        "effect": "テクニック+10％",
        "cname": "闪耀技巧3",
        "ceffect": "技巧+10%",
        "zhs_name": "灵光一现的技术3",
        "zhs_effect": "技术+10%",
        "zht_name": "靈光一閃的技巧3",
        "zht_effect": "技巧+10%",
        "en_name": "Flashy Technique 3",
        "en_effect": "Technique +10%",
        "kr_name": "번뜩이는 테크닉 3",
        "kr_effect": "테크닉 +10%",
        "pp_type": "7",
        "property": "tec"
    },
    {
        "name": "閃きのテクニック4",
        "type": "P",
        "effect": "テクニック+10％",
        "cname": "闪耀技巧4",
        "ceffect": "技巧+10%",
        "zhs_name": "灵光一现的技术4",
        "zhs_effect": "技术+10%",
        "zht_name": "靈光一閃的技巧4",
        "zht_effect": "技巧+10%",
        "en_name": "Flashy Technique 4",
        "en_effect": "Technique +10%",
        "kr_name": "번뜩이는 테크닉 4",
        "kr_effect": "테크닉 +10%",
        "pp_type": "7",
        "property": "tec"
    },
    {
        "name": "閃きのテクニック5",
        "type": "P",
        "effect": "テクニック+10％",
        "cname": "闪耀技巧5",
        "ceffect": "技巧+11%",
        "zhs_name": "灵光一现的技术5",
        "zhs_effect": "技术+11%",
        "zht_name": "靈光一閃的技巧5",
        "zht_effect": "技巧+11%",
        "en_name": "Flashy Technique 5",
        "en_effect": "Technique +11%",
        "kr_name": "번뜩이는 테크닉 5",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "閃きのテクニック6",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "闪耀技巧6",
        "ceffect": "技巧+11%",
        "zhs_name": "灵光一现的技术6",
        "zhs_effect": "技术+11%",
        "zht_name": "靈光一閃的技巧6",
        "zht_effect": "技巧+11%",
        "en_name": "Flashy Technique 6",
        "en_effect": "Technique +11%",
        "kr_name": "번뜩이는 테크닉 6",
        "kr_effect": "테크닉 +11%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "秘められたパワー3",
        "type": "P",
        "effect": "パワー+10％",
        "cname": "神秘之力3",
        "ceffect": "力量+10%",
        "zhs_name": "隐藏的力量3",
        "zhs_effect": "力量+10%",
        "zht_name": "隱藏的力量3",
        "zht_effect": "力量+10%",
        "en_name": "Hidden Power 3",
        "en_effect": "Power +10%",
        "kr_name": "숨겨진 파워 3",
        "kr_effect": "파워 +10%",
        "pp_type": "7",
        "property": "pow"
    },
    {
        "name": "秘められたパワー4",
        "type": "P",
        "effect": "パワー+10％",
        "cname": "神秘之力4",
        "ceffect": "力量+10%",
        "zhs_name": "隐藏的力量4",
        "zhs_effect": "力量+10%",
        "zht_name": "隱藏的力量4",
        "zht_effect": "力量+10%",
        "en_name": "Hidden Power 4",
        "en_effect": "Power +10%",
        "kr_name": "숨겨진 파워 4",
        "kr_effect": "파워 +10%",
        "pp_type": "7",
        "property": "pow"
    },
    {
        "name": "秘められたパワー5",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "神秘之力5",
        "ceffect": "力量+11%",
        "zhs_name": "隐藏的力量5",
        "zhs_effect": "力量+11%",
        "zht_name": "隱藏的力量5",
        "zht_effect": "力量+11%",
        "en_name": "Hidden Power 5",
        "en_effect": "Power +11%",
        "kr_name": "숨겨진 파워 5",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "秘められたパワー6",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "神秘之力6",
        "ceffect": "力量+11%",
        "zhs_name": "隐藏的力量6",
        "zhs_effect": "力量+11%",
        "zht_name": "隱藏的力量6",
        "zht_effect": "力量+11%",
        "en_name": "Hidden Power 6",
        "en_effect": "Power +11%",
        "kr_name": "숨겨진 파워 6",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "生粋のレシーバー3",
        "type": "P",
        "effect": "レシーブ時、テクニック+10％",
        "cname": "专业防守3",
        "ceffect": "防御时 技巧+10%",
        "zhs_name": "天生的接球手3",
        "zhs_effect": "接球时、技术+10%",
        "zht_name": "紮實的接球手3",
        "zht_effect": "接球時、技巧+10%",
        "en_name": "Natural Receiver 3",
        "en_effect": "When Receiving , Technique +10%",
        "kr_name": "타고난 리시버 3",
        "kr_effect": "리시브 시,테크닉 +10%",
        "pp_type": "7",
        "property": "tec"
    },
    {
        "name": "生粋のレシーバー4",
        "type": "P",
        "effect": "レシーブ時、テクニック+10％",
        "cname": "专业防守4",
        "ceffect": "防御时 技巧+10%",
        "zhs_name": "天生的接球手4",
        "zhs_effect": "接球时、技术+10%",
        "zht_name": "紮實的接球手4",
        "zht_effect": "接球時、技巧+10%",
        "en_name": "Natural Receiver 4",
        "en_effect": "When Receiving , Technique +10%",
        "kr_name": "타고난 리시버 4",
        "kr_effect": "리시브 시,테크닉 +10%",
        "pp_type": "7",
        "property": "tec"
    },
    {
        "name": "プラチナアタッカー",
        "type": "P",
        "effect": "アタッカーになる確率+15%",
        "cname": "白金进攻者",
        "ceffect": "成为攻击者的可能性+ 15％",
        "zhs_name": "白金攻击手",
        "zhs_effect": "成为攻击手的概率+15%",
        "zht_name": "白金攻擊手",
        "zht_effect": "成為攻擊手的機率為+15%",
        "en_name": "Platinum Attacker",
        "en_effect": "Probability of being the attacker: +15%",
        "kr_name": "플래티넘 어태커",
        "kr_effect": "어태커가 될 확률 +15%",
        "pp_type": "10",
        "property": "SP"
    },
    {
        "name": "可憐なフェイント",
        "type": "F",
        "effect": "フェイント成功で獲得アピールポイント+30%",
        "cname": "卖萌佯攻",
        "ceffect": "（此技能拥有角色 技巧攻击成功）佯攻成功时 获得分数+30%",
        "zhs_name": "楚楚可怜的假动作",
        "zhs_effect": "假动作成功后获得的魅力值+30%",
        "zht_name": "甜蜜的佯攻",
        "zht_effect": "佯攻成功時獲得的魅力點數為+30%",
        "en_name": "Sweet Feint",
        "en_effect": "After a successful feint,Appeal Points gained+30%",
        "kr_name": "가련한 페인트",
        "kr_effect": "페인트 성공 시 얻는 어필 포인트 +30%",
        "pp_type": "",
        "property": "tec"
    },
    {
        "name": "プラチナレシーバー",
        "type": "P",
        "effect": "レシーバーになる確率+15%",
        "cname": "白金防守者",
        "ceffect": "成为防守者的可能性+ 15％",
        "zhs_name": "白金接球手",
        "zhs_effect": "成为接球手的概率为+15%",
        "zht_name": "白金接球手",
        "zht_effect": "成為接球手的機率為+15%",
        "en_name": "Platinum Receiver",
        "en_effect": "Probability of being the receiver: +15%",
        "kr_name": "플래티넘 리시버",
        "kr_effect": "리시버가 될 확률 +15%",
        "pp_type": "10",
        "property": "SP"
    },
    {
        "name": "熱烈なエール",
        "type": "F",
        "effect": "チームメイト得点時、獲得アピールポイント+30%",
        "cname": "强力辅助",
        "ceffect": "（非此技能拥有角色 不限定攻击类型 攻击成功）队友得分时 获得分数+30%",
        "zhs_name": "热烈的欢呼",
        "zhs_effect": "队友得分时获得的魅力值+30%",
        "zht_name": "熱烈的聲援",
        "zht_effect": "隊友得分時獲得的魅力點數為+30%",
        "en_name": "Fierce Yell",
        "en_effect": "When a teammate scores,Appeal Points gained+30%",
        "kr_name": "열렬한 성원",
        "kr_effect": "팀원 득점 시 얻는 어필 포인트 +30%",
        "pp_type": "",
        "property": "SP"
    },
    {
        "name": "豪快なスパイク",
        "type": "F",
        "effect": "スパイク成功で獲得アピールポイント+30％",
        "cname": "潇洒扣杀",
        "ceffect": "（此技能拥有角色 力量攻击成功）扣球成功时 获得分数+30%",
        "zhs_name": "豪爽的杀球",
        "zhs_effect": "杀球成功后获得的魅力值+30%",
        "zht_name": "豪快的殺球",
        "zht_effect": "殺球成功時獲得的魅力點數為+30%",
        "en_name": "Killer Spike",
        "en_effect": "After a successful spike,Appeal Points gained+30%",
        "kr_name": "호쾌한 스파이크",
        "kr_effect": "스파이크 성공 시 얻는 어필 포인트 +30%",
        "pp_type": "",
        "property": "pow"
    },
    {
        "name": "エンジェルスパイク",
        "type": "P",
        "effect": "スパイク狙い指示時、スパイク攻撃の確率+10%",
        "cname": "Angel Spike 天使一击",
        "ceffect": "下达扣杀指令时 扣杀（力量）攻击概率+10%",
        "zhs_name": "天使杀球",
        "zhs_effect": "作出杀球指示时，杀球攻击的概率为+10%",
        "zht_name": "天使殺球",
        "zht_effect": "指示專門殺球時，殺球攻擊的機率+10%",
        "en_name": "Angel Spike",
        "en_effect": "Spike ATK probability +10% when ordered to spike",
        "kr_name": "엔젤 스파이크",
        "kr_effect": "스파이크 중시 지시 시 스파이크 공격 확률 +10%",
        "pp_type": "12",
        "property": "SP"
    },
    {
        "name": "フェアリーフェイント",
        "type": "P",
        "effect": "フェイント狙い指示時、スパイク攻撃の確率-10%",
        "cname": "Fairy Feint 精灵假象",
        "ceffect": "下达佯攻指令时 扣杀（力量）攻击概率-10%",
        "zhs_name": "妖精佯攻",
        "zhs_effect": "作出佯攻指示时，杀球攻击的概率为-10%",
        "zht_name": "妖精佯攻",
        "zht_effect": "指示專門佯攻時，殺球攻擊的機率-10%",
        "en_name": "Fairy Feint",
        "en_effect": "Spike ATK probability -10% when ordered to feint",
        "kr_name": "페어리 페인트",
        "kr_effect": "페인트 중시 지시 시 스파이크 공격 확률 -10%",
        "pp_type": "12",
        "property": "SP"
    },
    {
        "name": "団長のパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "团长的力量",
        "ceffect": "力量+11%",
        "zhs_name": "",
        "zhs_effect": "力量+11%",
        "zht_name": "",
        "zht_effect": "力量+11%",
        "en_name": "",
        "en_effect": "Power +11%",
        "kr_name": "",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "スコルピオン・パワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "天蝎座・力量",
        "ceffect": "力量+11%",
        "zhs_name": "天蝎之力",
        "zhs_effect": "力量+11%",
        "zht_name": "天蠍之力",
        "zht_effect": "力量+11%",
        "en_name": "Scorpion Power",
        "en_effect": "Power +11%",
        "kr_name": "스콜피온 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "サジタリウス・テクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "射手座・技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "射手技术",
        "zhs_effect": "技术+11%",
        "zht_name": "射手技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Sagittarius Technique",
        "en_effect": "Technique +11%",
        "kr_name": "사지타리우스의 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "アクアリウス・テクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "水瓶座・技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "水瓶技巧",
        "zhs_effect": "技术+11%",
        "zht_name": "水瓶技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Aquarius Technique",
        "en_effect": "Technique +11%",
        "kr_name": "아쿠아리우스 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "とろけるほどのパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "融化的力量",
        "ceffect": "力量+11%",
        "zhs_name": "融情蜜意般的力量",
        "zhs_effect": "力量+11%",
        "zht_name": "融情蜜意般的力量",
        "zht_effect": "力量+11%",
        "en_name": "Power to Melt Hearts",
        "en_effect": "Power +11%",
        "kr_name": "황홀할 만큼의 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "ピスケス・テクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "双鱼座・技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "双鱼技术",
        "zhs_effect": "技术+11%",
        "zht_name": "雙魚技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Pisces Technique",
        "en_effect": "Technique +11%",
        "kr_name": "피스케스 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "禁断の水着のパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "禁忌泳装的力量",
        "ceffect": "力量+11%",
        "zhs_name": "",
        "zhs_effect": "力量+11%",
        "zht_name": "",
        "zht_effect": "力量+11%",
        "en_name": "",
        "en_effect": "Power +11%",
        "kr_name": "",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "アリエス・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "水瓶座・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "白羊体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "白羊體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Aries Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "아리에스 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "タウルス・パワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "金牛座・力量",
        "ceffect": "力量+11%",
        "zhs_name": "金牛力量",
        "zhs_effect": "力量+11%",
        "zht_name": "金牛力量",
        "zht_effect": "力量+11%",
        "en_name": "Taurus Power",
        "en_effect": "Power +11%",
        "kr_name": "타우루스 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "ジェミニ・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "双子座・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "双子体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "雙子體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Gemini Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "제미니 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "ふわもこのパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "轻飘飘的力量",
        "ceffect": "力量+11%",
        "zhs_name": "蓬松的力量",
        "zhs_effect": "力量+11%",
        "zht_name": "蓬鬆的力量",
        "zht_effect": "力量+11%",
        "en_name": "Bubbly Power",
        "en_effect": "Power +11%",
        "kr_name": "부드러운 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "カンケル・パワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "巨蟹座・力量",
        "ceffect": "力量+11%",
        "zhs_name": "巨蟹力量",
        "zhs_effect": "力量+11%",
        "zht_name": "巨蟹力量",
        "zht_effect": "力量+11%",
        "en_name": "Cancer Power",
        "en_effect": "Power +11%",
        "kr_name": "캔서 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "半蔵のパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "半藏的力量",
        "ceffect": "力量+11%",
        "zhs_name": "半藏的力量",
        "zhs_effect": "力量+11%",
        "zht_name": "半藏的力量",
        "zht_effect": "力量+11%",
        "en_name": "Hanzō's Power",
        "en_effect": "Power +11%",
        "kr_name": "한조 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "月閃のテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "月闪的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "月闪技术",
        "zhs_effect": "技术+11%",
        "zht_name": "月閃技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Gessen's Technique",
        "en_effect": "Technique +11%",
        "kr_name": "월섬 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "紅蓮隊のパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "红莲队的力量",
        "ceffect": "力量+11%",
        "zhs_name": "焰红的力量",
        "zhs_effect": "力量+11%",
        "zht_name": "焰紅的力量",
        "zht_effect": "力量+11%",
        "en_name": "Homura's Power",
        "en_effect": "Power +11%",
        "kr_name": "홍련대 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "蛇女忍のパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "蛇女忍的力量",
        "ceffect": "力量+11%",
        "zhs_name": "蛇女的力量",
        "zhs_effect": "力量+11%",
        "zht_name": "蛇女的力量",
        "zht_effect": "力量+11%",
        "en_name": "Hebijo's Power",
        "en_effect": "Power +11%",
        "kr_name": "헤비죠 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "巫神楽のテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "巫神乐的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "巫神乐技术",
        "zhs_effect": "技术+11%",
        "zht_name": "巫神樂技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Mikagura's Technique",
        "en_effect": "Technique +11%",
        "kr_name": "미카구라 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "レオ・テクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "狮子座・技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "狮子技术",
        "zhs_effect": "技术+11%",
        "zht_name": "獅子技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Leo Technique",
        "en_effect": "Technique +11%",
        "kr_name": "레오 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "レオ・パワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "狮子座・力量",
        "ceffect": "力量+11%",
        "zhs_name": "狮子力量",
        "zhs_effect": "力量+11%",
        "zht_name": "獅子力量",
        "zht_effect": "力量+11%",
        "en_name": "Leo Power",
        "en_effect": "Power +11%",
        "kr_name": "레오 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "ウィルゴ・パワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "处女座・力量",
        "ceffect": "力量+11%",
        "zhs_name": "处女力量",
        "zhs_effect": "力量+11%",
        "zht_name": "處女力量",
        "zht_effect": "力量+11%",
        "en_name": "Virgo Power",
        "en_effect": "Power +11%",
        "kr_name": "비르고 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "ヴァルキリーのパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "女武神的力量",
        "ceffect": "力量+11%",
        "zhs_name": "女武神的力量",
        "zhs_effect": "力量+11%",
        "zht_name": "女武神的力量",
        "zht_effect": "力量+11%",
        "en_name": "Valkyrie Power",
        "en_effect": "Power +11%",
        "kr_name": "발키리 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "ウィルゴ・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "处女座・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "处女体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "處女體力",
        "zht_effect": "體力-11%",
        "en_name": "Virgo Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "비르고 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "リブラ・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "天秤座・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "天秤体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "天秤體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Libra Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "리브라 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "乙姫のテクニック",
        "type": "P",
        "effect": "テクニック+10％",
        "cname": "乙姫的技巧",
        "ceffect": "技巧+10%",
        "zhs_name": "乙姬的技术",
        "zhs_effect": "技术+10%",
        "zht_name": "乙姬的技巧",
        "zht_effect": "技巧+10%",
        "en_name": "Oto-hime's Technique",
        "en_effect": "Technique +10%",
        "kr_name": "선녀의 테크닉",
        "kr_effect": "테크닉 +10%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "トパーズ・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "黄玉・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "黄玉体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "黃玉體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Topaz Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "토파즈 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "ラピスラズリ・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "蓝玉・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "青金石体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "青金石體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Lapiz Lazuli Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "라피스 라즐리 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "雪華のパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "雪花的力量",
        "ceffect": "力量+11%",
        "zhs_name": "雪华的力量",
        "zhs_effect": "力量+11%",
        "zht_name": "雪華的力量",
        "zht_effect": "力量+11%",
        "en_name": "Snowflake Power",
        "en_effect": "Power +11%",
        "kr_name": "눈꽃 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "ガーネット・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "红玉・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "石榴石‧体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "石榴石・體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Garnet Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "가넷 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "カプリコーン・テクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "摩羯座・技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "魔羯技术",
        "zhs_effect": "技术+11%",
        "zht_name": "摩羯技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Capricorn Technique",
        "en_effect": "Technique +11%",
        "kr_name": "캐프리콘 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "ライザのテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "莱莎的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "莱莎的技术",
        "zhs_effect": "技术+11%",
        "zht_name": "萊莎的技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Ryza's Technique",
        "en_effect": "Technique +11%",
        "kr_name": "라이자 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "アメジスト・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "紫玉・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "紫水晶体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "紫水晶體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Amethyst Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "자수정 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "ショコラティエのパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "巧克力的力量",
        "ceffect": "力量+11%",
        "zhs_name": "",
        "zhs_effect": "力量+11%",
        "zht_name": "",
        "zht_effect": "力量+11%",
        "en_name": "",
        "en_effect": "Power +11%",
        "kr_name": "",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "アクアマリン・パワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "蓝晶・力量",
        "ceffect": "力量+11%",
        "zhs_name": "海蓝宝石力量",
        "zhs_effect": "力量+11%",
        "zht_name": "海藍寶石力量",
        "zht_effect": "力量+11%",
        "en_name": "Aquamarine Power",
        "en_effect": "Power +11%",
        "kr_name": "아쿠아마린 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "バーラタのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "巴拉塔的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "アクアマリン・テクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "蓝晶・技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "海蓝宝石技术",
        "zhs_effect": "技术+11%",
        "zht_name": "海藍寶石技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Aquamarine Technique",
        "en_effect": "Technique +11%",
        "kr_name": "아쿠아마린 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "明鏡止水のテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "明镜止水的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "",
        "zhs_effect": "技术+11%",
        "zht_name": "",
        "zht_effect": "技巧+11%",
        "en_name": "",
        "en_effect": "Technique +11%",
        "kr_name": "",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "恋のテクニック",
        "type": "P",
        "effect": "テクニック+10％",
        "cname": "恋之技巧",
        "ceffect": "技巧+10%",
        "zhs_name": "恋爱的技术",
        "zhs_effect": "技术+10%",
        "zht_name": "戀愛的技巧",
        "zht_effect": "技巧+10%",
        "en_name": "Love Technique",
        "en_effect": "Technique +10%",
        "kr_name": "사랑의 테크닉",
        "kr_effect": "테크닉 +10%",
        "pp_type": "7",
        "property": "tec"
    },
    {
        "name": "ダイヤモンド・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "金刚石・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "钻石体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "鑽石體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Diamond Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "다이아몬드 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "エメラルド・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "祖母绿・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "翡翠体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "翡翠體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Emerald Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "에메랄드 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "咲き誇るパワー",
        "type": "P",
        "effect": "パワー+10％",
        "cname": "盛开的力量",
        "ceffect": "力量+10%",
        "zhs_name": "盛开的力量",
        "zhs_effect": "力量+10%",
        "zht_name": "盛開的力量",
        "zht_effect": "力量+10%",
        "en_name": "Full Bloom Power",
        "en_effect": "Power +10%",
        "kr_name": "흐드러지는 파워",
        "kr_effect": "파워 +10%",
        "pp_type": "7",
        "property": "pow"
    },
    {
        "name": "エメラルド・パワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "祖母绿・力量",
        "ceffect": "力量+11%",
        "zhs_name": "翡翠力量",
        "zhs_effect": "力量+11%",
        "zht_name": "翡翠力量",
        "zht_effect": "力量+11%",
        "en_name": "Emerald Power",
        "en_effect": "Power +11%",
        "kr_name": "에메랄드 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "パール・テクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "珍珠・技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "珍珠技术",
        "zhs_effect": "技术+11%",
        "zht_name": "珍珠技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Pearl Technique",
        "en_effect": "Technique +11%",
        "kr_name": "진주 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "パール・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "珍珠・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "珍珠体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "珍珠體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Pearl Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "진주 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "ルビー・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "红宝石・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "红宝石体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "紅寶石體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Ruby Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "루비 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "SUGOIスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "SUGOI体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "ペリドット・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "橄榄石・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "橄榄石体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "橄欖石體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Peridot Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "페리도트 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "順風満帆のスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "顺风满帆的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "一帆风顺的体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "一帆風順的體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Smooth Sailing Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "순풍만범의 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "順風満帆のテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "顺风满帆的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "一帆风顺的技术",
        "zhs_effect": "技术+11%",
        "zht_name": "一帆風順的技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Smooth Sailing Technique",
        "en_effect": "Technique +11%",
        "kr_name": "순풍만범의 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "順風満帆のパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "顺风满帆的力量",
        "ceffect": "力量+11%",
        "zhs_name": "一帆风顺的力量",
        "zhs_effect": "力量+11%",
        "zht_name": "一帆風順的力量",
        "zht_effect": "力量+11%",
        "en_name": "Smooth Sailing Power",
        "en_effect": "Power +11%",
        "kr_name": "순풍만범의 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "サファイア・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "蓝宝石・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "蓝宝石体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "藍寶石體力",
        "zht_effect": "体力消耗量-11%",
        "en_name": "Sapphire Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "사파이어 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "サファイア・テクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "蓝宝石・技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "蓝宝石技术",
        "zhs_effect": "技术+11%",
        "zht_name": "藍寶石技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Sapphire Technique",
        "en_effect": "Technique +11%",
        "kr_name": "사파이어 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "シトリーのパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "希特莉的力量",
        "ceffect": "力量+11%",
        "zhs_name": "",
        "zhs_effect": "力量+11%",
        "zht_name": "",
        "zht_effect": "力量+11%",
        "en_name": "",
        "en_effect": "Power +11%",
        "kr_name": "",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "リザのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "丽莎的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "丽莎的体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "麗莎的體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Lisa's Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "리자 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "ダビのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "塔比的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "妲比的体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "妲比的體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Davi's Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "다비 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "モナのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "莫娜的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "莫娜的体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "莫娜的體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Mona's Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "모나 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "イブのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "伊芙的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "夏娃的体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "夏娃的體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Eve's Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "이브 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "オパール・テクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "蛋白石・技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "蛋白石技术",
        "zhs_effect": "技术+11%",
        "zht_name": "蛋白石技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Opal Technique",
        "en_effect": "Technique +11%",
        "kr_name": "오팔 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "月影のスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "月影的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "月下魅影的体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "月下魅影的體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Moonlight Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "월영의 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "吸血鬼のテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "吸血鬼的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "吸血鬼的技术",
        "zhs_effect": "技术+11%",
        "zht_name": "吸血鬼的技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Vampire Technique",
        "en_effect": "Technique +11%",
        "kr_name": "뱀파이어 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "スコルピオン・テクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "天蝎座・技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "天蝎技术",
        "zhs_effect": "技术+11%",
        "zht_name": "天蠍技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Scorpion Technique",
        "en_effect": "Technique +11%",
        "kr_name": "스콜피온 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "オパール・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "蛋白石・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "蛋白石体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "蛋白石體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Opal Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "오팔 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "エトワールのテクニック",
        "type": "P",
        "effect": "テクニック+10％",
        "cname": "星星的技巧",
        "ceffect": "技巧+10%",
        "zhs_name": "星光的技术",
        "zhs_effect": "技术+10%",
        "zht_name": "群星的技巧",
        "zht_effect": "技巧+10%",
        "en_name": "Étoile Technique",
        "en_effect": "Technique +10%",
        "kr_name": "에투알 테크닉",
        "kr_effect": "테크닉 +10%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "白椿のパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "白椿的力量",
        "ceffect": "力量+12%",
        "zhs_name": "白山茶力量",
        "zhs_effect": "力量+12%",
        "zht_name": "白山茶力量",
        "zht_effect": "力量+12%",
        "en_name": "White Camellia Power",
        "en_effect": "Power +12%",
        "kr_name": "흰 동백 파워",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "カトレアのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "卡特兰的力量",
        "ceffect": "力量+12%",
        "zhs_name": "卡特兰力量",
        "zhs_effect": "力量+12%",
        "zht_name": "卡特蘭力量",
        "zht_effect": "力量+12%",
        "en_name": "Cattleya Power",
        "en_effect": "Power +12%",
        "kr_name": "카틀레야 파워",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "カトレアのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-12％",
        "cname": "卡特兰的体力",
        "ceffect": "自身体力消耗-12%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-12%",
        "zht_name": "",
        "zht_effect": "體力消耗量-12%",
        "en_name": "",
        "en_effect": "Stamina Consumption -12%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -12%",
        "pp_type": "13",
        "property": "stm"
    },
    {
        "name": "貂蝉(三國志14)のスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "貂蝉(三国志14)的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "貂蝉(三国志14)体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "貂蟬(三國志14)體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Diao Chan's (RTK 14) Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "초선(삼국지 14) 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "シャルマンパワー",
        "type": "P",
        "effect": "パワー+10％",
        "cname": "迷人的力量",
        "ceffect": "力量+10%",
        "zhs_name": "魅惑的力量",
        "zhs_effect": "力量+10%",
        "zht_name": "魅惑的力量",
        "zht_effect": "力量+10%",
        "en_name": "Charmant Power",
        "en_effect": "Power +10%",
        "kr_name": "샤르망 파워",
        "kr_effect": "파워 +10%",
        "pp_type": "7",
        "property": "pow"
    },
    {
        "name": "シンビジウムのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "大花蕙兰的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "大花蕙兰技术",
        "zhs_effect": "技术+12%",
        "zht_name": "大花蕙蘭技巧",
        "zht_effect": "技巧+12%",
        "en_name": "Cymbidium Technique",
        "en_effect": "Technique +12%",
        "kr_name": "심비디엄 테크닉",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "百花献瑞のパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "百花献瑞力量",
        "ceffect": "力量+11%",
        "zhs_name": "百花献瑞力量",
        "zhs_effect": "力量+11%",
        "zht_name": "百花獻瑞力量",
        "zht_effect": "力量+11%",
        "en_name": "Auspicious Blossom Power",
        "en_effect": "Power +11%",
        "kr_name": "백화헌서 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "ランデブーのパワー",
        "type": "P",
        "effect": "パワー+10％",
        "cname": "约会的力量",
        "ceffect": "力量+10%",
        "zhs_name": "约会的力量",
        "zhs_effect": "力量+10%",
        "zht_name": "相約的力量",
        "zht_effect": "力量+10%",
        "en_name": "Rendezvous Power",
        "en_effect": "Power +10%",
        "kr_name": "랑데부 파워",
        "kr_effect": "파워 +10%",
        "pp_type": "7",
        "property": "pow"
    },
    {
        "name": "フリージアのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "小苍兰的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "小苍兰技术",
        "zhs_effect": "技术+12%",
        "zht_name": "小蒼蘭技巧",
        "zht_effect": "技巧+12%",
        "en_name": " Freesia Technique",
        "en_effect": "Technique +12%",
        "kr_name": "프리지어 테크닉",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "ショコラティエのテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "巧克力的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "",
        "zhs_effect": "技术+11%",
        "zht_name": "",
        "zht_effect": "技巧+11%",
        "en_name": "",
        "en_effect": "Technique +11%",
        "kr_name": "",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "お姉さんのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "姐姐的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "姐姐体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "姊姊體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Big Sis' Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "누나 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "ラーレのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-12％",
        "cname": "郁金香的体力",
        "ceffect": "自身体力消耗-12%",
        "zhs_name": "郁金香体力",
        "zhs_effect": "体力消耗量-12%",
        "zht_name": "鬱金香體力",
        "zht_effect": "體力消耗量-12%",
        "en_name": "Lale Stamina",
        "en_effect": "Stamina Consumption -12%",
        "kr_name": "라레 스태미너",
        "kr_effect": "스태미너 소비량 -12%",
        "pp_type": "13",
        "property": "stm"
    },
    {
        "name": "アルストロメリアのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "六出花的力量",
        "ceffect": "力量+12%",
        "zhs_name": "水仙百合力量",
        "zhs_effect": "力量+12%",
        "zht_name": "水仙百合力量",
        "zht_effect": "力量+12%",
        "en_name": "Alstroemeria Power",
        "en_effect": "Power +12%",
        "kr_name": "알스트로메리아 파워",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "アルストロメリアのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "六出花的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "水仙百合技术",
        "zhs_effect": "技术+12%",
        "zht_name": "水仙百合技巧",
        "zht_effect": "技巧+12%",
        "en_name": "Alstroemeria Technique",
        "en_effect": "Technique +12%",
        "kr_name": "알스트로메리아 테크닉",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "カーネーションのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "康乃馨的力量",
        "ceffect": "力量+12%",
        "zhs_name": "康乃馨的力量",
        "zhs_effect": "力量+12%",
        "zht_name": "康乃馨的力量",
        "zht_effect": "力量+12%",
        "en_name": "Carnation Power",
        "en_effect": "Power +12%",
        "kr_name": "카네이션 파워",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "ミッドナイトのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-10％",
        "cname": "午夜的体力",
        "ceffect": "自身体力消耗-10%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-10%",
        "zht_name": "",
        "zht_effect": "體力消耗量-10%",
        "en_name": "",
        "en_effect": "Stamina Consumption -10%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -10%",
        "pp_type": "7",
        "property": "stm"
    },
    {
        "name": "カーネーションのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-12％",
        "cname": "康乃馨的体力",
        "ceffect": "自身体力消耗-12%",
        "zhs_name": "康乃馨的体力",
        "zhs_effect": "体力消耗量-12%",
        "zht_name": "康乃馨的體力",
        "zht_effect": "體力消耗量-12%",
        "en_name": "Carnation Stamina",
        "en_effect": "Stamina Consumption -12%",
        "kr_name": "카네이션의 스태미너",
        "kr_effect": "스태미너 소비량 -12%",
        "pp_type": "13",
        "property": "stm"
    },
    {
        "name": "ローゼンのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-12％",
        "cname": "蔷薇的体力",
        "ceffect": "自身体力消耗-12%",
        "zhs_name": "玫瑰的体力",
        "zhs_effect": "体力消耗量-12%",
        "zht_name": "玫瑰的體力",
        "zht_effect": "體力消耗量-12%",
        "en_name": "Rose Stamina",
        "en_effect": "Stamina Consumption -12%",
        "kr_name": "로즈 스태미너",
        "kr_effect": "스태미너 소비량 -12%",
        "pp_type": "13",
        "property": "stm"
    },
    {
        "name": "ソレイユのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-10％",
        "cname": "太阳的耐力",
        "ceffect": "自身体力消耗-10%",
        "zhs_name": "太阳的体力",
        "zhs_effect": "体力消耗量-10%",
        "zht_name": "太陽的體力",
        "zht_effect": "體力消耗量-10%",
        "en_name": "Soleil Stamina",
        "en_effect": "Stamina Consumption -10%",
        "kr_name": "솔레이 스태미너",
        "kr_effect": "스태미너 소비량 -10%",
        "pp_type": "7",
        "property": "stm"
    },
    {
        "name": "スイートなスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-10％",
        "cname": "甜蜜的耐力",
        "ceffect": "自身体力消耗-10%",
        "zhs_name": "甜蜜的体力",
        "zhs_effect": "体力消耗量-10%",
        "zht_name": "甜蜜的體力",
        "zht_effect": "體力消耗量-10%",
        "en_name": "Sweet Stamina",
        "en_effect": "Stamina Consumption -10%",
        "kr_name": "스위트 스태미너",
        "kr_effect": "스태미너 소비량 -10%",
        "pp_type": "7",
        "property": "stm"
    },
    {
        "name": "ハイビスカスのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "扶桑花的力量",
        "ceffect": "力量+12%",
        "zhs_name": "扶桑的力量",
        "zhs_effect": "力量+12%",
        "zht_name": "扶桑的力量",
        "zht_effect": "力量+12%",
        "en_name": "Hibiscus Power",
        "en_effect": "Power +12%",
        "kr_name": "히비스커스의 파워",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "ロートヴァインのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-10％",
        "cname": "红葡萄酒的耐力",
        "ceffect": "自身体力消耗-10%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-10%",
        "zht_name": "",
        "zht_effect": "體力消耗量-10%",
        "en_name": "",
        "en_effect": "Stamina Consumption -10%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -10%",
        "pp_type": "7",
        "property": "stm"
    },
    {
        "name": "リシアンサスのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "石竹的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "洋桔梗技术",
        "zhs_effect": "技术+12%",
        "zht_name": "洋桔梗技巧",
        "zht_effect": "技巧+12%",
        "en_name": "Lisianthus Technique",
        "en_effect": "Technique +12%",
        "kr_name": "리시안셔스 테크닉",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "リシアンサスのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "石竹的力量",
        "ceffect": "力量+12%",
        "zhs_name": "洋桔梗力量",
        "zhs_effect": "力量+12%",
        "zht_name": "洋桔梗力量",
        "zht_effect": "力量+12%",
        "en_name": "Lisianthus Power",
        "en_effect": "Power +12%",
        "kr_name": "리시안셔스 파워",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "ピサラのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-10％",
        "cname": "毘萨菈的耐力",
        "ceffect": "自身体力消耗-10%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-10%",
        "zht_name": "",
        "zht_effect": "體力消耗量-10%",
        "en_name": "",
        "en_effect": "Stamina Consumption -10%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -10%",
        "pp_type": "7",
        "property": "stm"
    },
    {
        "name": "ギルのテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "吉尔的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "",
        "zhs_effect": "技术+11%",
        "zht_name": "",
        "zht_effect": "技巧+11%",
        "en_name": "",
        "en_effect": "Technique +11%",
        "kr_name": "",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "ダリアのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "大丽花的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "大丽花技术",
        "zhs_effect": "技术+12%",
        "zht_name": "大麗花技巧",
        "zht_effect": "技巧+12%",
        "en_name": "Dahlia Technique",
        "en_effect": "Technique +12%",
        "kr_name": "달리아 테크닉",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "ダリアのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-12％",
        "cname": "大丽花的耐力",
        "ceffect": "自身体力消耗-12%",
        "zhs_name": "大丽花体力",
        "zhs_effect": "体力消耗量-12%",
        "zht_name": "大麗花體力",
        "zht_effect": "體力消耗量-12%",
        "en_name": "Dahlia Stamina",
        "en_effect": "Stamina Consumption -12%",
        "kr_name": "달리아 스태미너",
        "kr_effect": "스태미너 소비량 -12%",
        "pp_type": "13",
        "property": "stm"
    },
    {
        "name": "ダリアのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "大丽花的力量",
        "ceffect": "力量+12%",
        "zhs_name": "大丽花力量",
        "zhs_effect": "力量+12%",
        "zht_name": "大麗花力量",
        "zht_effect": "力量+12%",
        "en_name": "Dahlia Power",
        "en_effect": "Power +12%",
        "kr_name": "달리아 파워",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "アリエス・パワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "水瓶座・力量",
        "ceffect": "力量+11%",
        "zhs_name": "白羊力量",
        "zhs_effect": "力量+11%",
        "zht_name": "白羊力量",
        "zht_effect": "力量+11%",
        "en_name": "Aries Power",
        "en_effect": "Power +11%",
        "kr_name": "아리에스 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "カンケル・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "巨蟹座・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "巨蟹体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "巨蟹體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Cancer Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "캔서 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "月影のテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "月影的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "月影的技术",
        "zhs_effect": "技术+11%",
        "zht_name": "月影的技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Moonlight Technique",
        "en_effect": "Technique +11%",
        "kr_name": "월영의 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "コスモスのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-12％",
        "cname": "秋樱的体力",
        "ceffect": "自身体力消耗-12%",
        "zhs_name": "秋英属体力",
        "zhs_effect": "体力消耗量-12%",
        "zht_name": "秋英屬體力",
        "zht_effect": "體力消耗量-12%",
        "en_name": "Cosmos Stamina",
        "en_effect": "Stamina Consumption -12%",
        "kr_name": "코스모스 스태미너",
        "kr_effect": "스태미너 소비량 -12%",
        "pp_type": "13",
        "property": "stm"
    },
    {
        "name": "コスモスのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "秋樱的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "秋英属技术",
        "zhs_effect": "技术+12%",
        "zht_name": "秋英屬技巧",
        "zht_effect": "技巧+12%",
        "en_name": "Cosmos Technique",
        "en_effect": "Technique +12%",
        "kr_name": "코스모스 테크닉",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "花鳥風月のパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "花鸟风月的力量",
        "ceffect": "力量+11%",
        "zhs_name": "花鸟风月的力量",
        "zhs_effect": "力量+11%",
        "zht_name": "花鳥風月的力量",
        "zht_effect": "力量+11%",
        "en_name": "Beauty of Nature's Power",
        "en_effect": "Power +11%",
        "kr_name": "화조풍월의 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "リンゴのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "苹果的力量",
        "ceffect": "力量+12%",
        "zhs_name": "苹果的力量",
        "zhs_effect": "力量+12%",
        "zht_name": "蘋果的力量",
        "zht_effect": "力量+12%",
        "en_name": "Apple Power",
        "en_effect": "Power +12%",
        "kr_name": "사과 파워",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "ミカンのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "蜜柑的力量",
        "ceffect": "力量+12%",
        "zhs_name": "桔子的力量",
        "zhs_effect": "力量+12%",
        "zht_name": "柑橘的力量",
        "zht_effect": "力量+12%",
        "en_name": "Orange Power",
        "en_effect": "Power +12%",
        "kr_name": "오렌지 파워",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "ルミナスのテクニック",
        "type": "P",
        "effect": "テクニック+10％",
        "cname": "发光的技巧",
        "ceffect": "技巧+10%",
        "zhs_name": "发光的技术",
        "zhs_effect": "技术+10%",
        "zht_name": "光輝的技巧",
        "zht_effect": "技巧+10%",
        "en_name": "Luminous Technique",
        "en_effect": "Technique +10%",
        "kr_name": "루미너스 테크닉",
        "kr_effect": "테크닉 +10%",
        "pp_type": "7",
        "property": "tec"
    },
    {
        "name": "ラズベリーのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "蓝莓的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "覆盆子的技术",
        "zhs_effect": "技术+12%",
        "zht_name": "覆盆子的技巧",
        "zht_effect": "技巧+12%",
        "en_name": "Raspberry Technique",
        "en_effect": "Technique +12%",
        "kr_name": "라즈베리 테크닉",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "オフィスウェアのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "办公装的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "办公室服装体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "OL裝體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Office Wear Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "사무복 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "パフュームのパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "香水的力量",
        "ceffect": "力量+11%",
        "zhs_name": "芳香的力量",
        "zhs_effect": "力量+11%",
        "zht_name": "香氛的力量",
        "zht_effect": "力量+11%",
        "en_name": "Perfume Power",
        "en_effect": "Power +11%",
        "kr_name": "퍼퓸 파워",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "イチゴのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "草莓的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "草莓技术",
        "zhs_effect": "技术+12%",
        "zht_name": "草莓技巧",
        "zht_effect": "技巧+12%",
        "en_name": "Strawberry Technique",
        "en_effect": "Technique +12%",
        "kr_name": "스트로베리 테크닉",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "ソフィーのテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "苏菲的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "苏菲的技术",
        "zhs_effect": "技术+11%",
        "zht_name": "蘇菲的技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Sophie's Technique",
        "en_effect": "Technique +11%",
        "kr_name": "소피 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "プラフタのテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "普拉芙妲的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "普拉芙妲的技术",
        "zhs_effect": "技术+11%",
        "zht_name": "普拉芙妲的技巧",
        "zht_effect": "技巧+11%",
        "en_name": "Plachta's Technique",
        "en_effect": "Technique +11%",
        "kr_name": "플라흐타 테크닉",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "葛城のパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "葛城的力量",
        "ceffect": "力量+11%",
        "zhs_name": "",
        "zhs_effect": "力量+11%",
        "zht_name": "",
        "zht_effect": "力量+11%",
        "en_name": "",
        "en_effect": "Power +11%",
        "kr_name": "",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "マンゴーのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "芒果的力量",
        "ceffect": "力量+12%",
        "zhs_name": "芒果力量",
        "zhs_effect": "力量+12%",
        "zht_name": "芒果力量",
        "zht_effect": "力量+12%",
        "en_name": "Mango Power",
        "en_effect": "Power +12%",
        "kr_name": "망고 파워",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "マンゴーのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "芒果的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "芒果技术",
        "zhs_effect": "技术+12%",
        "zht_name": "芒果技巧",
        "zht_effect": "技巧+12%",
        "en_name": "Mango Technique",
        "en_effect": "Technique +12%",
        "kr_name": "망고 테크닉",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "メロンのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "哈密瓜的力量",
        "ceffect": "力量+12%",
        "zhs_name": "蜜瓜力量",
        "zhs_effect": "力量+12%",
        "zht_name": "甜瓜力量",
        "zht_effect": "力量+12%",
        "en_name": "Melon Power",
        "en_effect": "Power +12%",
        "kr_name": "멜론 파워",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "メロンのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "哈密瓜的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "蜜瓜技术",
        "zhs_effect": "技术+12%",
        "zht_name": "甜瓜技巧",
        "zht_effect": "技巧+12%",
        "en_name": "Melon Technique",
        "en_effect": "Technique +12%",
        "kr_name": "멜론 테크닉",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "バーレスクのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "谐星的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "诙谐体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "詼諧體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Burlesque Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "벌레스크 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "バーレスク・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "谐星的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "诙谐体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "詼諧體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Burlesque Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "벌레스크 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "バナナのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "香蕉的力量",
        "ceffect": "力量+12%",
        "zhs_name": "香蕉力量",
        "zhs_effect": "力量+12%",
        "zht_name": "香蕉力量",
        "zht_effect": "力量+12%",
        "en_name": "Banana Power",
        "en_effect": "Power +12%",
        "kr_name": "바나누 파워",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "不思議なウサギのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "奇怪兔子的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "サクランボのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "樱桃的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "樱桃技术",
        "zhs_effect": "技术+12%",
        "zht_name": "櫻桃技巧",
        "zht_effect": "技巧+12%",
        "en_name": "Cherry Technique",
        "en_effect": "Technique +12%",
        "kr_name": "체리 테크닉",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "ラピスラズリ・パワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "蓝玉・力量",
        "ceffect": "力量+11%",
        "zhs_name": "",
        "zhs_effect": "力量+11%",
        "zht_name": "",
        "zht_effect": "力量+11%",
        "en_name": "",
        "en_effect": "Power +11%",
        "kr_name": "",
        "kr_effect": "파워 +11%",
        "pp_type": "9",
        "property": "pow"
    },
    {
        "name": "プラチナラインのテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "白金线的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "",
        "zhs_effect": "技术+11%",
        "zht_name": "",
        "zht_effect": "技巧+11%",
        "en_name": "",
        "en_effect": "Technique +11%",
        "kr_name": "",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "バーラタCSのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "婆罗多CS的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "明鏡止水CSのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "明镜止水CS的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "メイデンのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-10％",
        "cname": "少女的耐力",
        "ceffect": "自身体力消耗-10%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-10%",
        "zht_name": "",
        "zht_effect": "體力消耗量-10%",
        "en_name": "",
        "en_effect": "Stamina Consumption -10%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -10%",
        "pp_type": "7",
        "property": "stm"
    },
    {
        "name": "パイナップルのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "菠萝的力量",
        "ceffect": "力量+12%",
        "zhs_name": "",
        "zhs_effect": "力量+12%",
        "zht_name": "",
        "zht_effect": "力量+12%",
        "en_name": "",
        "en_effect": "Power +12%",
        "kr_name": "",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "モモのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "桃子的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "",
        "zhs_effect": "技术+12%",
        "zht_name": "",
        "zht_effect": "技巧+12%",
        "en_name": "",
        "en_effect": "Technique +12%",
        "kr_name": "",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "モモのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "桃子的力量",
        "ceffect": "力量+12%",
        "zhs_name": "",
        "zhs_effect": "力量+12%",
        "zht_name": "",
        "zht_effect": "力量+12%",
        "en_name": "",
        "en_effect": "Power +12%",
        "kr_name": "",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "ウィルゴ・テクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "处女座・技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "",
        "zhs_effect": "技术+11%",
        "zht_name": "",
        "zht_effect": "技巧+11%",
        "en_name": "",
        "en_effect": "Technique +11%",
        "kr_name": "",
        "kr_effect": "테크닉 +11%",
        "pp_type": "9",
        "property": "tec"
    },
    {
        "name": "カプリコーン・スタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "摩羯座・体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "9",
        "property": "stm"
    },
    {
        "name": "ブドウのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "葡萄的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "",
        "zhs_effect": "技术+12%",
        "zht_name": "",
        "zht_effect": "技巧+12%",
        "en_name": "",
        "en_effect": "Technique +12%",
        "kr_name": "",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "ブドウのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "葡萄的力量",
        "ceffect": "力量+12%",
        "zhs_name": "",
        "zhs_effect": "力量+12%",
        "zht_name": "",
        "zht_effect": "力量+12%",
        "en_name": "",
        "en_effect": "Power +12%",
        "kr_name": "",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "ペダリングのテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "蹬车的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "",
        "zhs_effect": "技术+11%",
        "zht_name": "",
        "zht_effect": "技巧+11%",
        "en_name": "",
        "en_effect": "Technique +11%",
        "kr_name": "",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "X・Y・Zのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-10％",
        "cname": "X・Y・Z的耐力",
        "ceffect": "自身体力消耗-10%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-10%",
        "zht_name": "",
        "zht_effect": "體力消耗量-10%",
        "en_name": "",
        "en_effect": "Stamina Consumption -10%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -10%",
        "pp_type": "7",
        "property": "stm"
    },
    {
        "name": "マロンのパワー",
        "type": "P",
        "effect": "パワー+12％",
        "cname": "栗子的力量",
        "ceffect": "力量+12%",
        "zhs_name": "",
        "zhs_effect": "力量+12%",
        "zht_name": "",
        "zht_effect": "力量+12%",
        "en_name": "",
        "en_effect": "Power +12%",
        "kr_name": "",
        "kr_effect": "파워 +12%",
        "pp_type": "13",
        "property": "pow"
    },
    {
        "name": "幻影のパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "幻影的力量",
        "ceffect": "力量+11%",
        "zhs_name": "",
        "zhs_effect": "力量+11%",
        "zht_name": "",
        "zht_effect": "力量+11%",
        "en_name": "",
        "en_effect": "Power +11%",
        "kr_name": "",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "桂花のパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "桂花的力量",
        "ceffect": "力量+11%",
        "zhs_name": "",
        "zhs_effect": "力量+11%",
        "zht_name": "",
        "zht_effect": "力量+11%",
        "en_name": "",
        "en_effect": "Power +11%",
        "kr_name": "",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "マロンのテクニック",
        "type": "P",
        "effect": "テクニック+12％",
        "cname": "栗子的技巧",
        "ceffect": "技巧+12%",
        "zhs_name": "",
        "zhs_effect": "技术+12%",
        "zht_name": "",
        "zht_effect": "技巧+12%",
        "en_name": "",
        "en_effect": "Technique +12%",
        "kr_name": "",
        "kr_effect": "테크닉 +12%",
        "pp_type": "13",
        "property": "tec"
    },
    {
        "name": "デア・マリーナのテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "女神之泪的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "",
        "zhs_effect": "技术+11%",
        "zht_name": "",
        "zht_effect": "技巧+11%",
        "en_name": "",
        "en_effect": "Technique +11%",
        "kr_name": "",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "シャルキーのパワー&スタミナ",
        "type": "P",
        "effect": "パワー+7％/スタミナ消費量-7％",
        "cname": "东方调的力量&体力",
        "ceffect": "力量+7%/自身体力消耗-7%",
        "zhs_name": "",
        "zhs_effect": "力量+7%/体力消耗量-7%",
        "zht_name": "",
        "zht_effect": "力量+7%/體力消耗量-7%",
        "en_name": "",
        "en_effect": " Power +7%/Stamina Consumption -7%",
        "kr_name": "",
        "kr_effect": "파워 +7%/스태미너 소비량 -7%",
        "pp_type": "14",
        "property": "pow"
    },
    {
        "name": "綺羅星のスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "绮罗星的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "サポーネのパワー&スタミナ",
        "type": "P",
        "effect": "パワー+7％/スタミナ消費量-7％",
        "cname": "香皂调的力量&体力",
        "ceffect": "力量+7%/自身体力消耗-7%",
        "zhs_name": "",
        "zhs_effect": "力量+7%/体力消耗量-7%",
        "zht_name": "",
        "zht_effect": "力量+7%/體力消耗量-7%",
        "en_name": "",
        "en_effect": " Power +7%/Stamina Consumption -7%",
        "kr_name": "",
        "kr_effect": "파워 +7%/스태미너 소비량 -7%",
        "pp_type": "14",
        "property": "pow"
    },
    {
        "name": "レインディアのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "麋鹿的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "魔王のテクニック",
        "type": "P",
        "effect": "テクニック+11％",
        "cname": "魔王的技巧",
        "ceffect": "技巧+11%",
        "zhs_name": "",
        "zhs_effect": "技术+11%",
        "zht_name": "",
        "zht_effect": "技巧+11%",
        "en_name": "",
        "en_effect": "Technique +11%",
        "kr_name": "",
        "kr_effect": "테크닉 +11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "ヲトメのパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "少女的力量",
        "ceffect": "力量+11%",
        "zhs_name": "",
        "zhs_effect": "力量+11%",
        "zht_name": "",
        "zht_effect": "力量+11%",
        "en_name": "",
        "en_effect": "Power +11%",
        "kr_name": "",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "パンサーのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-10％",
        "cname": "豹纹的耐力",
        "ceffect": "自身体力消耗-10%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-10%",
        "zht_name": "",
        "zht_effect": "體力消耗量-10%",
        "en_name": "",
        "en_effect": "Stamina Consumption -10%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -10%",
        "pp_type": "7",
        "property": "stm"
    },
    {
        "name": "スリップストリームのパワー",
        "type": "P",
        "effect": "パワー+11％",
        "cname": "滑流的力量",
        "ceffect": "力量+11%",
        "zhs_name": "",
        "zhs_effect": "力量+11%",
        "zht_name": "",
        "zht_effect": "力量+11%",
        "en_name": "",
        "en_effect": "Power +11%",
        "kr_name": "",
        "kr_effect": "파워 +11%",
        "pp_type": "8",
        "property": "pow"
    },
    {
        "name": "サーバントのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "女仆的耐力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "キラキラのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "闪耀的耐力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "闪亮体力",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "閃亮體力",
        "zht_effect": "體力消耗量-11%",
        "en_name": "Shiny Stamina",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "반짝거리는 스태미너",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "にしざーさんのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "西沢的耐力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "ギャルのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "辣妹的耐力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "キュイールのテクニック&スタミナ",
        "type": "P",
        "effect": "テクニック+7％/スタミナ消費量-7％",
        "cname": "皮革调的技巧&体力",
        "ceffect": "技巧+7%/自身体力消耗-7%",
        "zhs_name": "",
        "zhs_effect": "技术+7%/体力消耗量-7%",
        "zht_name": "",
        "zht_effect": "技巧+7%/體力消耗量-7%",
        "en_name": "",
        "en_effect": "Technique +7%/Stamina Consumption -7%",
        "kr_name": "",
        "kr_effect": "테크닉 +7%/스태미너 소비량 -7%",
        "pp_type": "14",
        "property": "tec"
    },
    {
        "name": "ネージュのテクニック&スタミナ",
        "type": "P",
        "effect": "テクニック+7％/スタミナ消費量-7％",
        "cname": "清新调的技巧&体力",
        "ceffect": "技巧+7%/自身体力消耗-7%",
        "zhs_name": "",
        "zhs_effect": "技术+7%/体力消耗量-7%",
        "zht_name": "",
        "zht_effect": "技巧+7%/體力消耗量-7%",
        "en_name": "",
        "en_effect": "Technique +7%/Stamina Consumption -7%",
        "kr_name": "",
        "kr_effect": "테크닉 +7%/스태미너 소비량 -7%",
        "pp_type": "14",
        "property": "tec"
    },
    {
        "name": "コスタのパワー&スタミナ",
        "type": "P",
        "effect": "パワー+7％/スタミナ消費量-7％",
        "cname": "木质调的力量&体力",
        "ceffect": "力量+7%/自身体力消耗-7%",
        "zhs_name": "",
        "zhs_effect": "力量+7%/体力消耗量-7%",
        "zht_name": "",
        "zht_effect": "力量+7%/體力消耗量-7%",
        "en_name": "",
        "en_effect": " Power +7%/Stamina Consumption -7%",
        "kr_name": "",
        "kr_effect": "파워 +7%/스태미너 소비량 -7%",
        "pp_type": "14",
        "property": "pow"
    },
    {
        "name": "コスタのテクニック&スタミナ",
        "type": "P",
        "effect": "テクニック+7％/スタミナ消費量-7％",
        "cname": "木质调的技巧&体力",
        "ceffect": "技巧+7%/自身体力消耗-7%",
        "zhs_name": "",
        "zhs_effect": "技术+7%/体力消耗量-7%",
        "zht_name": "",
        "zht_effect": "技巧+7%/體力消耗量-7%",
        "en_name": "",
        "en_effect": "Technique +7%/Stamina Consumption -7%",
        "kr_name": "",
        "kr_effect": "테크닉 +7%/스태미너 소비량 -7%",
        "pp_type": "14",
        "property": "tec"
    },
    {
        "name": "ブルームのパワー&スタミナ",
        "type": "P",
        "effect": "パワー+7％/スタミナ消費量-7％",
        "cname": "花香调的力量&体力",
        "ceffect": "力量+7%/自身体力消耗-7%",
        "zhs_name": "",
        "zhs_effect": "力量+7%/体力消耗量-7%",
        "zht_name": "",
        "zht_effect": "力量+7%/體力消耗量-7%",
        "en_name": "",
        "en_effect": " Power +7%/Stamina Consumption -7%",
        "kr_name": "",
        "kr_effect": "파워 +7%/스태미너 소비량 -7%",
        "pp_type": "14",
        "property": "pow"
    },
    {
        "name": "ブルームのテクニック&スタミナ",
        "type": "P",
        "effect": "テクニック+7％/スタミナ消費量-7％",
        "cname": "花香调的技巧&体力",
        "ceffect": "技巧+7%/自身体力消耗-7%",
        "zhs_name": "",
        "zhs_effect": "技术+7%/体力消耗量-7%",
        "zht_name": "",
        "zht_effect": "技巧+7%/體力消耗量-7%",
        "en_name": "",
        "en_effect": "Technique +7%/Stamina Consumption -7%",
        "kr_name": "",
        "kr_effect": "테크닉 +7%/스태미너 소비량 -7%",
        "pp_type": "14",
        "property": "tec"
    },
    {
        "name": "シダーのパワー&スタミナ",
        "type": "P",
        "effect": "パワー+7％/スタミナ消費量-7％",
        "cname": "木制调的力量&体力",
        "ceffect": "力量+7%/自身体力消耗-7%",
        "zhs_name": "",
        "zhs_effect": "力量+7%/体力消耗量-7%",
        "zht_name": "",
        "zht_effect": "力量+7%/體力消耗量-7%",
        "en_name": "",
        "en_effect": " Power +7%/Stamina Consumption -7%",
        "kr_name": "",
        "kr_effect": "파워 +7%/스태미너 소비량 -7%",
        "pp_type": "14",
        "property": "pow"
    },
    {
        "name": "パイレーツのスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "海盗的耐力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "ノブレスのテクニック＆スタミナ",
        "type": "P",
        "effect": "テクニック+7％/スタミナ消費量-7％",
        "cname": "贵族的技巧&体力",
        "ceffect": "技巧+7%/自身体力消耗-7%",
        "zhs_name": "",
        "zhs_effect": "技术+7%/体力消耗量-7%",
        "zht_name": "",
        "zht_effect": "技巧+7%/體力消耗量-7%",
        "en_name": "",
        "en_effect": "Technique +7%/Stamina Consumption -7%",
        "kr_name": "",
        "kr_effect": "테크닉 +7%/스태미너 소비량 -7%",
        "pp_type": "14",
        "property": "tec"
    },
    {
        "name": "目を引くほどのテクニック",
        "type": "P",
        "effect": "テクニック＋11％",
        "cname": "夺目技术",
        "ceffect": "技巧+11%",
        "zhs_name": "夺目技术",
        "zhs_effect": "技术＋11%",
        "zht_name": "奪目技巧",
        "zht_effect": "技巧＋11%",
        "en_name": "Eye-catching Technique",
        "en_effect": "Technique ＋11%",
        "kr_name": "눈길을 끌 정도의 테크닉",
        "kr_effect": "테크닉 ＋11%",
        "pp_type": "8",
        "property": "tec"
    },
    {
        "name": "マーレのパワー＆スタミナ",
        "type": "P",
        "effect": "パワー+7％/スタミナ消費量-7％",
        "cname": "玛雷的力量&体力",
        "ceffect": "力量+7%/自身体力消耗-7%",
        "zhs_name": "",
        "zhs_effect": "力量+7%/体力消耗量-7%",
        "zht_name": "",
        "zht_effect": "力量+7%/體力消耗量-7%",
        "en_name": "",
        "en_effect": " Power +7%/Stamina Consumption -7%",
        "kr_name": "",
        "kr_effect": "파워 +7%/스태미너 소비량 -7%",
        "pp_type": "14",
        "property": "pow"
    },
    {
        "name": "月兎のスタミナ",
        "type": "P",
        "effect": "スタミナ消費量-11％",
        "cname": "月兔的体力",
        "ceffect": "自身体力消耗-11%",
        "zhs_name": "",
        "zhs_effect": "体力消耗量-11%",
        "zht_name": "",
        "zht_effect": "體力消耗量-11%",
        "en_name": "",
        "en_effect": "Stamina Consumption -11%",
        "kr_name": "",
        "kr_effect": "스태미너 소비량 -11%",
        "pp_type": "8",
        "property": "stm"
    },
    {
        "name": "ローレルのテクニック＆スタミナ",
        "type": "P",
        "effect": "テクニック+7％/スタミナ消費量-7％",
        "cname": "劳雷尔的技巧&体力",
        "ceffect": "技巧+7%/自身体力消耗-7%",
        "zhs_name": "",
        "zhs_effect": "技术+7%/体力消耗量-7%",
        "zht_name": "",
        "zht_effect": "技巧+7%/體力消耗量-7%",
        "en_name": "",
        "en_effect": "Technique +7%/Stamina Consumption -7%",
        "kr_name": "",
        "kr_effect": "테크닉 +7%/스태미너 소비량 -7%",
        "pp_type": "14",
        "property": "tec"
    },
    {
        "name": "通用技能4PP",
        "type": "P",
        "effect": "对应属性+5%",
        "cname": " 活动限定SR满觉醒",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "4",
        "property": ""
    },
    {
        "name": "通用技能5PP_1",
        "type": "P",
        "effect": "对应属性+1%",
        "cname": " 攀岩活动赠送",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "0",
        "property": ""
    },
    {
        "name": "通用技能5PP_2",
        "type": "P",
        "effect": "对应属性+1%",
        "cname": " 24级以下 升级奖励",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "1",
        "property": ""
    },
    {
        "name": "通用技能5PP_3",
        "type": "P",
        "effect": "对应属性+6%",
        "cname": " 活动限定SR满觉醒",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "5",
        "property": ""
    },
    {
        "name": "通用技能7PP_1",
        "type": "P",
        "effect": "对应属性+5%",
        "cname": " 圣诞SR满觉醒",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "11",
        "property": ""
    },
    {
        "name": "通用技能7PP_2",
        "type": "P",
        "effect": "对应属性+5%",
        "cname": " 女神石板解锁",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "17",
        "property": ""
    },
    {
        "name": "通用技能8PP_1",
        "type": "P",
        "effect": "对应属性+2%",
        "cname": " 24级以上 升级奖励",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "2",
        "property": ""
    },
    {
        "name": "通用技能8PP_2",
        "type": "P",
        "effect": "对应属性+5%",
        "cname": " 普通常驻SR满觉醒",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "3",
        "property": ""
    },
    {
        "name": "通用技能12PP_1",
        "type": "P",
        "effect": "对应属性+10%",
        "cname": " 常驻/活动限定SSR满觉醒",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "7",
        "property": ""
    },
    {
        "name": "通用技能12PP_2",
        "type": "P",
        "effect": "对应属性+11%",
        "cname": " 活动限定SSR满觉醒",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "9",
        "property": ""
    },
    {
        "name": "通用技能13PP",
        "type": "P",
        "effect": "对应属性+11%",
        "cname": " 活动限定SSR满觉醒",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "8",
        "property": ""
    },
    {
        "name": "通用技能14PP_1",
        "type": "P",
        "effect": "对应属性+12%",
        "cname": " 第三年生日限定SSR满觉醒",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "13",
        "property": ""
    },
    {
        "name": "通用技能14PP_2",
        "type": "P",
        "effect": "对应属性+7%/体力消耗-7%",
        "cname": " 第五年生日限定SSR满觉醒",
        "ceffect": "",
        "zhs_name": "",
        "zhs_effect": "",
        "zht_name": "",
        "zht_effect": "",
        "en_name": "",
        "en_effect": "",
        "kr_name": "",
        "kr_effect": "",
        "pp_type": "14",
        "property": ""
    }
]

girls = [
  {
    "id": "0", "name": "みさき", "ename": "misaki", "cname": "美咲 / 海咲", "birthday": "7/7", "keywords": "misaki 老婆 laopo meixiao haixiao", "pow": "1040", "tec": "900", "stm": "1050", "apl": "20", "type": "pow", "release": "20171115", "free": "20171115", "age": "18", "height": "156", "Bust": "85", "Waist": "54", "Hips": "89", "blood": "A", "cv": "津田美波", "ACC_head": "pow", "ACC_face": "stm", "ACC_hand": "pow"
  },
  {
    "id": "1", "name": "こころ", "ename": "kokoro", "cname": "心", "birthday": "12/1", "keywords": "kokoro 老婆 laopo xin", "pow": "1000", "tec": "850", "stm": "1150", "apl": "10", "type": "pow", "release": "20171115", "free": "20171115", "age": "19", "height": "158", "Bust": "90", "Waist": "55", "Hips": "87", "blood": "A", "cv": "川橙绫子", "ACC_head": "pow", "ACC_face": "pow", "ACC_hand": "stm"
  },
  {
    "id": "2", "name": "マリー・ローズ", "ename": "marie", "cname": "玛丽・萝丝", "birthday": "6/6", "keywords": "marie mali 老婆 laopo", "pow": "800", "tec": "1090", "stm": "1100", "apl": "20", "type": "tec", "release": "20171115", "free": "20171115", "age": "18", "height": "147", "Bust": "74", "Waist": "56", "Hips": "78", "blood": "AB", "cv": "相沢舞", "ACC_head": "stm", "ACC_face": "tec", "ACC_hand": "tec"
  },
  {
    "id": "3", "name": "たまき", "ename": "tamaki", "cname": "环", "birthday": "8/19", "keywords": "tamaki huan", "pow": "1040", "tec": "970", "stm": "980", "apl": "20", "type": "pow", "release": "20180412", "free": "20180726", "age": "22", "height": "169", "Bust": "84", "Waist": "54", "Hips": "87", "blood": "B", "cv": "大西纱织", "ACC_head": "pow", "ACC_face": "stm", "ACC_hand": "pow"
  },
  {
    "id": "4", "name": "レイファン", "ename": "leifang", "cname": "雷芳 / 丽凤", "birthday": "4/23", "keywords": "leifang", "pow": "900", "tec": "1090", "stm": "1000", "apl": "10", "type": "tec", "release": "20180705", "free": "20181108", "age": "21", "height": "163", "Bust": "87", "Waist": "55", "Hips": "86", "blood": "B", "cv": "冬马由美", "ACC_head": "stm", "ACC_face": "tec", "ACC_hand": "tec"
  },
  {
    "id": "5", "name": "ルナ", "ename": "luna", "cname": "露娜", "birthday": "10/15", "keywords": "luna lvna", "pow": "830", "tec": "820", "stm": "1340", "apl": "20", "type": "stm", "release": "20180118", "free": "20180426", "age": "18", "height": "149", "Bust": "92", "Waist": "56", "Hips": "88", "blood": "O", "cv": "三上枝织", "ACC_head": "tec", "ACC_face": "pow", "ACC_hand": "stm"
  },
  {
    "id": "6", "name": "かすみ", "ename": "kasumi", "cname": "霞", "birthday": "2/23", "keywords": "kasumi xia", "pow": "900", "tec": "1040", "stm": "1050", "apl": "20", "type": "tec", "release": "20171115", "free": "20171115", "age": "19", "height": "158", "Bust": "89", "Waist": "54", "Hips": "85", "blood": "A", "cv": "桑岛法子", "ACC_head": "tec", "ACC_face": "tec", "ACC_hand": "stm"
  },
  {
    "id": "7", "name": "ほのか", "ename": "honoka", "cname": "穗乃果 / 穗香", "birthday": "3/24", "keywords": "honoka suinaiguo suixiang", "pow": "850", "tec": "850", "stm": "1300", "apl": "10", "type": "stm", "release": "20171115", "free": "20171115", "age": "18", "height": "150", "Bust": "99", "Waist": "58", "Hips": "91", "blood": "AB", "cv": "野中蓝", "ACC_head": "pow", "ACC_face": "pow", "ACC_hand": "stm"
  },
  {
    "id": "8", "name": "女天狗", "ename": "nyotengu", "cname": "女天狗", "birthday": "11/19", "keywords": "nyotengu nvtiangou", "pow": "1050", "tec": "800", "stm": "1150", "apl": "10", "type": "pow", "release": "20171115", "free": "20171115", "age": "1018", "height": "172", "Bust": "93", "Waist": "58", "Hips": "88", "blood": "?", "cv": "佐藤朱", "ACC_head": "pow", "ACC_face": "stm", "ACC_hand": "tec"
  },
  {
    "id": "9", "name": "ヒトミ", "ename": "hitomi", "cname": "瞳", "birthday": "5/25", "keywords": "hitomi tong", "pow": "900", "tec": "800", "stm": "1300", "apl": "10", "type": "stm", "release": "20171115", "free": "20171115", "age": "20", "height": "160", "Bust": "90", "Waist": "58", "Hips": "85", "blood": "O", "cv": "堀江由衣", "ACC_head": "pow", "ACC_face": "pow", "ACC_hand": "stm"
  },
  {
    "id": "10", "name": "エレナ", "ename": "helena", "cname": "海莲娜", "birthday": "1/30", "keywords": "helena hailianna", "pow": "850", "tec": "1000", "stm": "1150", "apl": "10", "type": "tec", "release": "20171115", "free": "20171115", "age": "23", "height": "170", "Bust": "90", "Waist": "56", "Hips": "86", "blood": "AB", "cv": "小山裕香", "ACC_head": "stm", "ACC_face": "tec", "ACC_hand": "tec"
  },
  {
    "id": "11", "name": "あやね", "ename": "ayane", "cname": "绫音", "birthday": "8/5", "keywords": "ayane lingyin", "pow": "800", "tec": "1000", "stm": "1200", "apl": "10", "type": "tec", "release": "20171115", "free": "20171115", "age": "18", "height": "157", "Bust": "93", "Waist": "54", "Hips": "84", "blood": "AB", "cv": "山崎和佳奈", "ACC_head": "stm", "ACC_face": "tec", "ACC_hand": "tec"
  },
  {
    "id": "12", "name": "紅葉", "ename": "momiji", "cname": "红叶", "birthday": "9/20", "keywords": "momiji hongye", "pow": "800", "tec": "900", "stm": "1290", "apl": "20", "type": "stm", "release": "20171115", "free": "20171115", "age": "21", "height": "161", "Bust": "92", "Waist": "58", "Hips": "88", "blood": "A", "cv": "皆口裕子", "ACC_head": "stm", "ACC_face": "tec", "ACC_hand": "tec"
  },
  {
    "id": "13", "name": "フィオナ", "ename": "fiona", "cname": "菲欧娜", "birthday": "2/11", "keywords": "fiona feiouna", "pow": "800", "tec": "870", "stm": "1310", "apl": "20", "type": "stm", "release": "20180927", "free": "20190118", "age": "18", "height": "152", "Bust": "88", "Waist": "55", "Hips": "84", "blood": "O", "cv": "本渡枫", "ACC_head": "pow", "ACC_face": "stm", "ACC_hand": "tec"
  },
  {
    "id": "14", "name": "なぎさ", "ename": "nagisa", "cname": "渚 / 凪咲", "birthday": "5/5", "keywords": "nagisa zhu zhixiao", "pow": "1060", "tec": "900", "stm": "1020", "apl": "20", "type": "pow", "release": "20181218", "free": "20190418", "age": "20", "height": "156", "Bust": "79", "Waist": "54", "Hips": "87", "blood": "A", "cv": "内田真礼", "ACC_head": "pow", "ACC_face": "stm", "ACC_hand": "pow"
  },
  {
    "id": "15", "name": "カンナ", "ename": "kanna", "cname": "神奈 / 神无", "birthday": "9/15", "keywords": "kanna kangna", "pow": "1080", "tec": "820", "stm": "1100", "apl": "10", "type": "pow", "release": "20190411", "free": "20190731", "age": "1014", "height": "149", "Bust": "75", "Waist": "56", "Hips": "79", "blood": "?", "cv": "大空直美", "ACC_head": "pow", "ACC_face": "stm", "ACC_hand": "pow"
  },
  {
    "id": "16", "name": "モニカ", "ename": "monica", "cname": "莫妮卡", "birthday": "1/1", "keywords": "monica monika 老婆 laopo mao", "pow": "840", "tec": "1110", "stm": "1030", "apl": "20", "type": "tec", "release": "20190807", "free": "20191123", "age": "19", "height": "160", "Bust": "86", "Waist": "55", "Hips": "88", "blood": "O", "cv": "幸村惠理", "ACC_head": "tec", "ACC_face": "stm", "ACC_hand": "tec"
  },
  {
    "id": "17", "name": "さゆり", "ename": "sayuri", "cname": "小百合 / 纱友里", "birthday": "3/31", "keywords": "sayuri xiaobaihe", "pow": "800", "tec": "800", "stm": "1400", "apl": "20", "type": "stm", "release": "20191205", "free": "20200317", "age": "24", "height": "162", "Bust": "98", "Waist": "59", "Hips": "92", "blood": "O", "cv": "和气杏未", "ACC_head": "tec", "ACC_face": "stm", "ACC_hand": "tec"
  },
  {
    "id": "18", "name": "パティ", "ename": "patty", "cname": "帕蒂 / 派蒂", "birthday": "7/31", "keywords": "patty pati", "pow": "1070", "tec": "880", "stm": "1060", "apl": "10", "type": "pow", "release": "20200430", "free": "20200923", "age": "19", "height": "159", "Bust": "85", "Waist": "56", "Hips": "86", "blood": "B", "cv": "高野麻里佳", "ACC_head": "pow", "ACC_face": "stm", "ACC_hand": "pow"
  },
  {
    "id": "19", "name": "つくし", "ename": "tsukushi", "cname": "筑紫", "birthday": "10/24", "keywords": "tsukushi shancai", "pow": "850", "tec": "1100", "stm": "1050", "apl": "10", "type": "tec", "release": "20200826", "free": "20210112", "age": "18", "height": "151", "Bust": "95", "Waist": "55", "Hips": "89", "blood": "AB", "cv": "指出毬亚", "ACC_head": "tec", "ACC_face": "stm", "ACC_hand": "tec"
  },
  {
    "id": "20", "name": "ロベリア", "ename": "lobelia", "cname": "洛贝莉娅", "birthday": "6/25", "keywords": "lobelia luobeiliya", "pow": "800", "tec": "950", "stm": "1250", "apl": "20", "type": "stm", "release": "20201225", "free": "20210603", "age": "18", "height": "152", "Bust": "78", "Waist": "54", "Hips": "82", "blood": "B", "cv": "古賀葵", "ACC_head": "tec", "ACC_face": "stm", "ACC_hand": "tec"
  },
  {
    "id": "21", "name": "ななみ", "ename": "nanami", "cname": "七海 / 奈波", "birthday": "4/16", "keywords": "nanami nanamei naibo qihai", "pow": "1050", "tec": "930", "stm": "1030", "apl": "20", "type": "pow", "release": "20210401", "free": "20210909", "age": "18", "height": "158", "Bust": "88", "Waist": "54", "Hips": "87", "blood": "O", "cv": "島袋美由利", "ACC_head": "pow", "ACC_face": "pow", "ACC_hand": "stm"
  },
  {
    "id": "22", "name": "エリーゼ", "ename": "elise", "cname": "伊莉丝", "birthday": "9/3", "keywords": "yilisi elise", "pow": "920", "tec": "1060", "stm": "1040", "apl": "10", "type": "tec", "release": "20210714", "free": "20220113", "age": "22", "height": "168", "Bust": "94", "Waist": "58", "Hips": "90", "blood": "A", "cv": "濑户麻沙美", "ACC_head": "stm", "ACC_face": "tec", "ACC_hand": "tec"
  },
  {
    "id": "23", "name": "こはる", "ename": "koharu", "cname": "心春 / 小春", "birthday": "12/22", "keywords": "xiaochun xinchun koharu", "pow": "940", "tec": "840", "stm": "1240", "apl": "10", "type": "stm", "release": "20211102", "free": "20220513", "age": "18", "height": "151", "Bust": "83", "Waist": "54", "Hips": "85", "blood": "A", "cv": "长绳麻理亚", "ACC_head": "pow", "ACC_face": "pow", "ACC_hand": "stm"
  },
  {
    "id": "24", "name": "ティナ", "ename": "tina", "cname": "蒂娜", "birthday": "12/6", "keywords": "tina dina", "pow": "1120", "tec": "800", "stm": "1100", "apl": "10", "type": "pow", "release": "20220128", "free": "20220818", "age": "24", "height": "174", "Bust": "95", "Waist": "60", "Hips": "89", "blood": "O", "cv": "永岛由子", "ACC_head": "pow", "ACC_face": "stm", "ACC_hand": "pow"
  },
  {
    "id": "25", "name": "エイミー", "ename": "amy", "cname": "艾米", "birthday": "6/18", "keywords": "amy aimi", "pow": "890", "tec": "1120", "stm": "1030", "apl": "10", "type": "tec", "release": "20220404", "free": "20221013", "age": "18", "height": "156", "Bust": "89", "Waist": "55", "Hips": "88", "blood": "A", "cv": "铃代纱弓", "ACC_head": "stm", "ACC_face": "tec", "ACC_hand": "tec"
  },
  {
    "id": "26", "name": "シャンディ", "ename": "shandy", "cname": "杉蒂", "birthday": "3/3", "keywords": "shandy shandi", "pow": "1100", "tec": "880", "stm": "1040", "apl": "20", "type": "pow", "release": "20220824", "free": "20230118", "age": "21", "height": "161", "Bust": "91", "Waist": "56", "Hips": "89", "blood": "AB", "cv": "下地紫野", "ACC_head": "pow", "ACC_face": "stm", "ACC_hand": "pow"
  },
  {
    "id": "27", "name": "ゆきの", "ename": "yukino", "cname": "雪乃 / 诗乃", "birthday": "1/20", "keywords": "yukino xuenai shinai", "pow": "1090", "tec": "950", "stm": "1000", "apl": "20", "type": "pow", "release": "20230222", "free": "?", "age": "18", "height": "165", "Bust": "89", "Waist": "55", "Hips": "87", "blood": "B", "cv": "前田佳织里", "ACC_head": "pow", "ACC_face": "stm", "ACC_hand": "pow"
  },
  {
    "id": "99", "name": "-", "ename": "all", "cname": "通用", "birthday": "N/A", "keywords": "all suoyou", "pow": "null", "tec": "null", "stm": "null", "apl": "null", "type": "null", "release": "null", "free": "null", "age": "null", "height": "null", "Bust": "null", "Waist": "null", "Hips": "null", "blood": "null", "cv": "null", "ACC_head": "null", "ACC_face": "null", "ACC_hand": "null"
  }
]

ssrs = [
  {
    "id": "0", "girl": "kokoro", "name": "せとか(こころ)", "zhs_name": "濑户果(心)", "zht_name": "瀨戶香(心)", "en_name": "Setoka(Kokoro)", "kr_name": "천혜향(코코로)", "type": "pow", "pow": "4572", "tec": "3694", "stm": "3704", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー3", "skill3": "", "sell": "2017/11/15", "resell": "N/A", "break": "1", "special_fun": ""
  },
  {
    "id": "1", "girl": "misaki", "name": "純白のスリットワンピ(みさき)", "zhs_name": "纯白开叉连衣裙(海咲)", "zht_name": "純白色開衩連身裙(海咲)", "en_name": "Pure White Slit One-Piece (Misaki)", "kr_name": "순백 슬릿 원피스 (미사키)", "type": "pow", "pow": "4522", "tec": "3664", "stm": "3814", "apl": "200", "skill1": "強烈スパイクF", "skill2": "秘められたパワー3", "skill3": "", "sell": "2017/11/15", "resell": "N/A", "break": "1", "special_fun": ""
  },
  {
    "id": "2", "girl": "honoka", "name": "デルフィニウム(ほのか)", "zhs_name": "翠雀(穗香)", "zht_name": "翠雀(穗香)", "en_name": "Delphinium(Honoka)", "kr_name": "델피니움(호노카)", "type": "stm", "pow": "3864", "tec": "3376", "stm": "4472", "apl": "230", "skill1": "驚異のスタミナD", "skill2": "隠しきれない魅力3", "skill3": "", "sell": "2017/11/15", "resell": "N/A", "break": "1", "special_fun": ""
  },
  {
    "id": "3", "girl": "nyotengu", "name": "けごん(女天狗)", "zhs_name": "华严(女天狗)", "zht_name": "華嚴(女天狗)", "en_name": "Kegon(Nyotengu)", "kr_name": "화염(뇨텐구)", "type": "pow", "pow": "4622", "tec": "3734", "stm": "3644", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー3", "skill3": "", "sell": "2017/11/15", "resell": "N/A", "break": "1", "special_fun": ""
  },
  {
    "id": "4", "girl": "hitomi", "name": "リーブラ(ヒトミ)", "zhs_name": "天枰座(瞳)", "zht_name": "天秤座(瞳)", "en_name": "Libra(Hitomi)", "kr_name": "리브라(히토미)", "type": "stm", "pow": "3794", "tec": "3326", "stm": "4622", "apl": "200", "skill1": "灼熱のダンスB", "skill2": "内から湧き上がるスタミナ3", "skill3": "", "sell": "2017/11/15", "resell": "N/A", "break": "1", "special_fun": ""
  },
  {
    "id": "5", "girl": "helena", "name": "ヴァイオレットフィズ(エレナ)", "zhs_name": "紫罗兰菲兹(海莲娜)", "zht_name": "紫羅蘭香檳(海蓮娜)", "en_name": "Violet Fizz(Helena)", "kr_name": "바이올렛 피즈 (엘레나)", "type": "tec", "pow": "3684", "tec": "4542", "stm": "3486", "apl": "230", "skill1": "高度な心理戦E", "skill2": "閃きのテクニック3", "skill3": "", "sell": "2017/11/15", "resell": "N/A", "break": "1", "special_fun": ""
  },
  {
    "id": "6", "girl": "ayane", "name": "フィルギャ(あやね)", "zhs_name": "费尔加(绫音)", "zht_name": "守伴者(綾音)", "en_name": "Fylgja(Ayane)", "kr_name": "필갸(아야네)", "type": "tec", "pow": "3764", "tec": "4622", "stm": "3356", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "生粋のレシーバー3", "skill3": "", "sell": "2017/11/15", "resell": "N/A", "break": "1", "special_fun": ""
  },
  {
    "id": "7", "girl": "marie", "name": "ミヌエット(マリー)", "zhs_name": "小步舞曲(玛莉)", "zht_name": "小步舞曲(瑪莉)", "en_name": "Minuet(Marie)", "kr_name": "미뉴에트(마리)", "type": "tec", "pow": "3644", "tec": "4552", "stm": "3546", "apl": "200", "skill1": "完璧なレシーブB", "skill2": "閃きのテクニック3", "skill3": "", "sell": "2017/11/15", "resell": "N/A", "break": "1", "special_fun": ""
  },
  {
    "id": "8", "girl": "kasumi", "name": "ネモフィラ(かすみ)", "zhs_name": "粉蝶花(霞)", "zht_name": "粉蝶花(霞)", "en_name": "Nemophila(Kasumi)", "kr_name": "네모필라(카스미)", "type": "tec", "pow": "3714", "tec": "4602", "stm": "3426", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "生粋のレシーバー3", "skill3": "", "sell": "2017/11/15", "resell": "N/A", "break": "1", "special_fun": ""
  },
  {
    "id": "9", "girl": "momiji", "name": "ひので(紅葉)", "zhs_name": "日出(红叶)", "zht_name": "日出(紅葉)", "en_name": "Sunrise(Momiji)", "kr_name": "해돋이(모미지)", "type": "stm", "pow": "3654", "tec": "3586", "stm": "4502", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "内から湧き上がるスタミナ3", "skill3": "", "sell": "2017/11/15", "resell": "N/A", "break": "1", "special_fun": ""
  },
  {
    "id": "10", "girl": "misaki", "name": "寝起きブラウス(みさき)", "zhs_name": "起居衬衫(海咲)", "zht_name": "晨起薄衫(海咲)", "en_name": "Rise and Shine Blouse (Misaki)", "kr_name": "일상용 블라우스(미사키)", "type": "tec", "pow": "4022", "tec": "4414", "stm": "3864", "apl": "200", "skill1": "強烈スパイクA", "skill2": "生粋のレシーバー4", "skill3": "", "sell": "2017/11/17", "resell": "2018/5/24 2018/11/15", "break": "1", "special_fun": ""
  },
  {
    "id": "11", "girl": "kasumi", "name": "純白のスリットワンピ(かすみ)", "zhs_name": "纯白开叉连衣裙(霞)", "zht_name": "純白色開衩連身裙(霞)", "en_name": "Pure White Slit One-Piece(Kasumi)", "kr_name": "순백 슬릿 원피스(카스미)", "type": "pow", "pow": "4772", "tec": "3834", "stm": "3694", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "秘められたパワー4", "skill3": "", "sell": "2017/11/21", "resell": "2018/2/23 2018/9/13", "break": "1", "special_fun": ""
  },
  {
    "id": "12", "girl": "honoka", "name": "シークレットハート(ほのか)", "zhs_name": "秘密之心(穗香)", "zht_name": "祕密的心(穗香)", "en_name": "Secret Heart(Honoka)", "kr_name": "시크릿 하트(호노카)", "type": "tec", "pow": "3774", "tec": "4662", "stm": "3606", "apl": "200", "skill1": "灼熱のダンスA", "skill2": "閃きのテクニック4", "skill3": "", "sell": "2017/12/4", "resell": "2018/3/24 2018/5/2 2018/11/16 2019/3/24 2020/3/24", "break": "1", "special_fun": ""
  },
  {
    "id": "13", "girl": "marie", "name": "プリンセス・ロゼット(マリー)", "zhs_name": "罗塞特公主(玛莉)", "zht_name": "玫瑰皇女(瑪莉)", "en_name": "Princess Rosette (Marie)", "kr_name": "민족 의상(루나)", "type": "stm", "pow": "3734", "tec": "3686", "stm": "4622", "apl": "200", "skill1": "高度な心理戦A", "skill2": "内から湧き上がるスタミナ4", "skill3": "", "sell": "2017/12/7", "resell": "2018/9/6 2019/6/6 2020/6/6", "break": "1", "special_fun": ""
  },
  {
    "id": "14", "girl": "marie", "name": "振袖・薔薇舞(マリー)", "zhs_name": "振袖・蔷薇舞(玛莉)", "zht_name": "振袖‧薔薇舞(瑪莉)", "en_name": "Rose Dance Kimono (Marie)", "kr_name": "후리소데(장미의 춤)(마리)", "type": "tec", "pow": "3794", "tec": "4772", "stm": "3676", "apl": "200", "skill1": "強烈スパイクC", "skill2": "生粋のレシーバー4", "skill3": "", "sell": "2017/12/26", "resell": "2018/6/6 2019/1/1 2019/2/28 2019/12/26 2020/12/28 2022/1/1 2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "15", "girl": "kasumi", "name": "振袖・花浅葱(かすみ)", "zhs_name": "振袖・花浅葱(霞)", "zht_name": "振袖‧花淺蔥(霞)", "en_name": "Blue Floral Kimono (Kasumi)", "kr_name": "후리소데(옥색 꽃무늬)(카스미)", "type": "tec", "pow": "3794", "tec": "4772", "stm": "3676", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "閃きのテクニック4", "skill3": "", "sell": "2017/12/26", "resell": "2018/2/23 2019/1/1 2019/2/28 2019/12/26 2020/12/28 2022/1/1 2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "16", "girl": "kokoro", "name": "振袖・桃吹雪(こころ)", "zhs_name": "振袖・桃吹雪(心)", "zht_name": "振袖‧桃吹雪(心)", "en_name": "Peach Storm Kimono (Kokoro)", "kr_name": "후리소데(흩날리는 도화)(코코로)", "type": "pow", "pow": "4772", "tec": "3794", "stm": "3934", "apl": "200", "skill1": "高度な心理戦C", "skill2": "秘められたパワー4", "skill3": "", "sell": "2017/12/26", "resell": "2019/1/1 2019/2/28 2019/12/26 2020/12/28 2022/1/1 2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "17", "girl": "momiji", "name": "あなご(紅葉)", "zhs_name": "康吉鳗(红叶)", "zht_name": "星鰻(紅葉)", "en_name": "Eel (Momiji)", "kr_name": "붕장어(모미지)", "type": "tec", "pow": "3724", "tec": "4682", "stm": "3636", "apl": "200", "skill1": "灼熱のダンスA", "skill2": "生粋のレシーバー4", "skill3": "", "sell": "2017/12/28", "resell": "2018/6/21 2018/9/20 2019/3/27 2020/5/21", "break": "0", "special_fun": ""
  },
  {
    "id": "18", "girl": "misaki", "name": "はじめてのあさり(みさき)", "zhs_name": "第一次的贝壳泳裝(海咲)", "zht_name": "第一次穿貝殼泳裝(海咲)", "en_name": "First Set (Misaki)", "kr_name": "첫 조개잡이 (미사키)", "type": "pow", "pow": "4672", "tec": "3744", "stm": "3884", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/1/2", "resell": "2018/7/7 2018/12/27 2020/8/23", "break": "1", "special_fun": ""
  },
  {
    "id": "19", "girl": "kasumi", "name": "マルガリータ(かすみ)", "zhs_name": "玛格丽特(霞)", "zht_name": "瑪格麗特(霞)", "en_name": "Margarita (Kasumi)", "kr_name": "마가리타(카스미)", "type": "apl", "pow": "3416", "tec": "3216", "stm": "3644", "apl": "600", "skill1": "観客総立ちF", "skill2": "隠しきれない魅力4", "skill3": "", "sell": "2018/1/10", "resell": "2018/7/19 2019/1/31 2019/5/30 2019/9/26 2019/11/14 2020/1/16 2020/5/7 2021/2/25", "break": "0", "special_fun": "池子附带相同外形 变色全角色通用的SR衣服"
  },
  {
    "id": "20", "girl": "luna", "name": "フォークロア(ルナ)", "zhs_name": "民俗(露娜)", "zht_name": "民俗風(露娜)", "en_name": "Folklore (Luna)", "kr_name": "민족 의상(루나)", "type": "stm", "pow": "3824", "tec": "3356", "stm": "4562", "apl": "200", "skill1": "灼熱のダンスA", "skill2": "内から湧き上がるスタミナ3", "skill3": "", "sell": "2018/1/18", "resell": "2018/10/15 2019/10/15 2020/10/15 2021/1/18 2022/1/18 2023/1/18", "break": "1", "special_fun": ""
  },
  {
    "id": "21", "girl": "hitomi", "name": "ピスタチオ(ヒトミ)", "zhs_name": "开心果(瞳)", "zht_name": "開心果(瞳)", "en_name": "Pistachio (Hitomi)", "kr_name": "피스타치오(히토미)", "type": "pow", "pow": "4672", "tec": "3694", "stm": "3934", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/1/25", "resell": "2018/5/25 2018/10/18 2019/5/25 2019/11/14 2020/5/25 2020/5/26", "break": "0", "special_fun": ""
  },
  {
    "id": "22", "girl": "ayane", "name": "パピヨンダンス(あやね)", "zhs_name": "蝴蝶之舞(绫音)", "zht_name": "蝶舞(綾音)", "en_name": "Butterfly Dance (Ayane)", "kr_name": "파피용 댄스(아야네)", "type": "tec", "pow": "3744", "tec": "4672", "stm": "3626", "apl": "200", "skill1": "強烈スパイクB", "skill2": "閃きのテクニック5", "skill3": "", "sell": "2018/2/1", "resell": "2018/6/14 2019/8/7", "break": "1", "special_fun": ""
  },
  {
    "id": "23_1", "girl": "marie", "name": "フォー・ユー(マリー)", "zhs_name": "为了你(玛莉)", "zht_name": "爲了你(瑪莉)", "en_name": "For You (Marie)", "kr_name": "For you(루나)", "type": "pow", "pow": "4822", "tec": "3684", "stm": "3764", "apl": "230", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/2/8", "resell": "2019/2/14 2020/2/13 2020/6/6", "break": "0", "special_fun": ""
  },
  {
    "id": "23_2", "girl": "honoka", "name": "フォー・ユー(ほのか)", "zhs_name": "为了你(穗香)", "zht_name": "爲了你(穗香)", "en_name": "For You (Honoka)", "kr_name": "For you(호노카)", "type": "pow", "pow": "4822", "tec": "3684", "stm": "3764", "apl": "230", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/2/8", "resell": "2019/2/14 2020/2/13", "break": "0", "special_fun": ""
  },
  {
    "id": "23_3", "girl": "kasumi", "name": "フォー・ユー(かすみ)", "zhs_name": "为了你(霞)", "zht_name": "爲了你(霞)", "en_name": "For You (Kasumi)", "kr_name": "For you(카스미)", "type": "pow", "pow": "4822", "tec": "3684", "stm": "3764", "apl": "230", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/2/8", "resell": "2019/2/14 2020/2/13", "break": "0", "special_fun": ""
  },
  {
    "id": "23_4", "girl": "ayane", "name": "フォー・ユー(あやね)", "zhs_name": "为了你(绫音)", "zht_name": "爲了你(綾音)", "en_name": "For You (Ayane)", "kr_name": "For you(아야네)", "type": "pow", "pow": "4822", "tec": "3684", "stm": "3764", "apl": "230", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/2/8", "resell": "2019/2/14 2020/2/13 2020/8/5", "break": "0", "special_fun": ""
  },
  {
    "id": "23_5", "girl": "kokoro", "name": "フォー・ユー(こころ)", "zhs_name": "为了你(心)", "zht_name": "爲了你(心)", "en_name": "For You (Kokoro)", "kr_name": "For you(코코로)", "type": "pow", "pow": "4822", "tec": "3684", "stm": "3764", "apl": "230", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/2/8", "resell": "2019/2/14 2019/12/1 2020/2/13", "break": "0", "special_fun": ""
  },
  {
    "id": "23_6", "girl": "nyotengu", "name": "フォー・ユー(女天狗)", "zhs_name": "为了你(女天狗)", "zht_name": "爲了你(女天狗)", "en_name": "For You (Nyotengu)", "kr_name": "For you(뇨텐구)", "type": "pow", "pow": "4822", "tec": "3684", "stm": "3764", "apl": "230", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/2/8", "resell": "2019/2/14 2019/11/19 2020/2/13", "break": "0", "special_fun": ""
  },
  {
    "id": "23_7", "girl": "hitomi", "name": "フォー・ユー(ヒトミ)", "zhs_name": "为了你(瞳)", "zht_name": "爲了你(瞳)", "en_name": "For You (Hitomi)", "kr_name": "For you(히토미)", "type": "pow", "pow": "4822", "tec": "3684", "stm": "3764", "apl": "230", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/2/8", "resell": "2019/2/14 2020/2/13 2020/5/25", "break": "0", "special_fun": ""
  },
  {
    "id": "23_8", "girl": "momiji", "name": "フォー・ユー(紅葉)", "zhs_name": "为了你(红叶)", "zht_name": "爲了你(紅葉)", "en_name": "For You (Momiji)", "kr_name": "For you(모미지)", "type": "pow", "pow": "4822", "tec": "3684", "stm": "3764", "apl": "230", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/2/8", "resell": "2019/2/14 2020/2/13 2020/9/20", "break": "0", "special_fun": ""
  },
  {
    "id": "23_9", "girl": "helena", "name": "フォー・ユー(エレナ)", "zhs_name": "为了你(海莲娜)", "zht_name": "爲了你(海蓮娜)", "en_name": "For You (Helena)", "kr_name": "For you(엘레나)", "type": "pow", "pow": "4822", "tec": "3684", "stm": "3764", "apl": "230", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/2/8", "resell": "2019/2/14 2020/1/30 2020/2/13", "break": "0", "special_fun": ""
  },
  {
    "id": "23_10", "girl": "misaki", "name": "フォー・ユー(みさき)", "zhs_name": "为了你(海咲)", "zht_name": "爲了你(海咲)", "en_name": "For You (Misaki)", "kr_name": "For you(미사키)", "type": "pow", "pow": "4822", "tec": "3684", "stm": "3764", "apl": "230", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/2/8", "resell": "2019/2/14 2020/2/13 2020/7/7", "break": "0", "special_fun": ""
  },
  {
    "id": "23_11", "girl": "luna", "name": "フォー・ユー(ルナ)", "zhs_name": "为了你(露娜)", "zht_name": "爲了你(露娜)", "en_name": "For You (Luna)", "kr_name": "For you(루나)", "type": "pow", "pow": "4822", "tec": "3684", "stm": "3764", "apl": "230", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/2/8", "resell": "2019/10/15 2020/10/15 2021/1/18 2022/1/18 2023/1/18", "break": "0", "special_fun": ""
  },
  {
    "id": "24", "girl": "nyotengu", "name": "ダークプリズン(女天狗)", "zhs_name": "黑狱(女天狗)", "zht_name": "暗黑監獄(女天狗)", "en_name": "Dark Prison (Nyotengu)", "kr_name": "다크 프리즌 (뇨텐구)", "type": "tec", "pow": "4092", "tec": "4424", "stm": "3784", "apl": "200", "skill1": "強烈スパイクF", "skill2": "閃きのテクニック4", "skill3": "", "sell": "2018/2/15", "resell": "2018/7/5 2019/2/21 2019/10/17 2019/11/19", "break": "1", "special_fun": ""
  },
  {
    "id": "25", "girl": "helena", "name": "黄金のラビリンス(エレナ)", "zhs_name": "黄金迷宫(海莲娜)", "zht_name": "黃金迷宮(海蓮娜)", "en_name": "Golden Labyrinth (Helena)", "kr_name": "황금의 라비린스 (엘레나)", "type": "apl", "pow": "3206", "tec": "3446", "stm": "3624", "apl": "600", "skill1": "観客総立ちD", "skill2": "隠しきれない魅力4", "skill3": "", "sell": "2018/2/22", "resell": "2018/8/2 2019/11/14 2020/1/30", "break": "0", "special_fun": ""
  },
  {
    "id": "26", "girl": "kokoro", "name": "マドレーヌ(こころ)", "zhs_name": "马德琳(心)", "zht_name": "馬德琳(心)", "en_name": "Madeleine (Kokoro)", "kr_name": "마들렌 (코코로)", "type": "stm", "pow": "4364", "tec": "3306", "stm": "4772", "apl": "200", "skill1": "強烈なプレッシャーA", "skill2": "内から湧き上がるスタミナ5", "skill3": "", "sell": "2018/3/1", "resell": "2018/8/9 2019/3/7 2019/11/14 2019/12/1 2020/5/21", "break": "1", "special_fun": ""
  },
  {
    "id": "27", "girl": "honoka", "name": "モーモーデニム(ほのか)", "zhs_name": "哞哞牛仔吊带裤(穗香)", "zht_name": "哞哞牛仔吊帶褲(穗香)", "en_name": "Moo Moo Denim (Honoka)", "kr_name": "로즈 휩 (마리)", "type": "stm", "pow": "4144", "tec": "3416", "stm": "4682", "apl": "200", "skill1": "強烈スパイクC", "skill2": "内から湧き上がるスタミナ3", "skill3": "", "sell": "2018/3/8", "resell": "2018/3/24 2018/8/16 2018/10/18 2019/3/7", "break": "1", "special_fun": ""
  },
  {
    "id": "28", "girl": "marie", "name": "ローズホイップ(マリー)", "zhs_name": "玫瑰冰淇淋(玛莉)", "zht_name": "玫瑰奶霜(瑪莉)", "en_name": "Rose Whip (Marie)", "kr_name": "음메음메 데님 (호노카)", "type": "stm", "pow": "3784", "tec": "3736", "stm": "4722", "apl": "200", "skill1": "強烈スパイクB", "skill2": "内から湧き上がるスタミナ5", "skill3": "", "sell": "2018/3/15", "resell": "2018/6/6 2018/11/29 2019/4/18", "break": "1", "special_fun": ""
  },
  {
    "id": "29", "girl": "ayane", "name": "うすかわたけのこ(あやね)", "zhs_name": "薄皮竹笋(绫音)", "zht_name": "薄皮竹筍(綾音)", "en_name": "Thin Towel Wrap (Ayane)", "kr_name": "박막 죽순(아야네)", "type": "stm", "pow": "3834", "tec": "3886", "stm": "4722", "apl": "200", "skill1": "完璧なレシーブF", "skill2": "内から湧き上がるスタミナ5", "skill3": "", "sell": "2018/3/22", "resell": "2021/12/9", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "30", "girl": "misaki", "name": "うすかわたけのこ(みさき)", "zhs_name": "薄皮竹笋(海咲)", "zht_name": "薄皮竹筍(海咲)", "en_name": "Thin Towel Wrap (Misaki)", "kr_name": "박막 죽순(미사키)", "type": "tec", "pow": "3894", "tec": "4882", "stm": "3666", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "閃きのテクニック5", "skill3": "", "sell": "2018/3/22", "resell": "2021/12/9", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "31", "girl": "nyotengu", "name": "リコリス・リーフ(女天狗)", "zhs_name": "彼岸花与叶(女天狗)", "zht_name": "甘草葉(女天狗)", "en_name": "Licorice Leaf (Nyotengu)", "kr_name": "리커리쉬 리프 (뇨텐구)", "type": "stm", "pow": "4114", "tec": "3586", "stm": "4742", "apl": "200", "skill1": "強烈スパイクA", "skill2": "内から湧き上がるスタミナ5", "skill3": "", "sell": "2018/3/29", "resell": "2018/8/23 2020/3/30", "break": "0", "special_fun": ""
  },
  {
    "id": "32", "girl": "kasumi", "name": "さくら・リーフ(かすみ)", "zhs_name": "樱与叶(霞)", "zht_name": "櫻花葉(霞)", "en_name": "Sakura Leaf (Kasumi)", "kr_name": "사쿠라 리프 (카스미)", "type": "tec", "pow": "3884", "tec": "4952", "stm": "3606", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "閃きのテクニック5", "skill3": "", "sell": "2018/3/29", "resell": "2018/8/23 2020/2/23 2020/3/30", "break": "0", "special_fun": ""
  },
  {
    "id": "33", "girl": "hitomi", "name": "永遠のクラテル(ヒトミ)", "zhs_name": "永恒的巨爵(瞳)", "zht_name": "永遠的巨爵(瞳)", "en_name": "Eternal Krater (Hitomi)", "kr_name": "영원의 크라텔(히토미)", "type": "apl", "pow": "3486", "tec": "3256", "stm": "3584", "apl": "500", "skill1": "観客総立ちC", "skill2": "隠しきれない魅力4", "skill3": "", "sell": "2018/4/5", "resell": "2018/5/25 2018/9/27 2020/2/20", "break": "0", "special_fun": ""
  },
  {
    "id": "34", "girl": "momiji", "name": "深紅のスリットワンピ(紅葉)", "zhs_name": "深红开叉连衣裙(红叶)", "zht_name": "深紅開衩連身裙(紅葉)", "en_name": "Crimson Slit One-Piece (Momiji)", "kr_name": "진홍색 슬릿 원피스(모미지)", "type": "stm", "pow": "4094", "tec": "3506", "stm": "4642", "apl": "200", "skill1": "強烈スパイクC", "skill2": "内から湧き上がるスタミナ5", "skill3": "", "sell": "2018/4/12", "resell": "2018/10/25", "break": "1", "special_fun": ""
  },
  {
    "id": "35", "girl": "helena", "name": "純白のスリットワンピ(エレナ)", "zhs_name": "纯白开叉连衣裙(海莲娜)", "zht_name": "純白色開衩連身裙(海蓮娜)", "en_name": "Pure White Slit One-Piece (Helena)", "kr_name": "순백 슬릿 원피스(엘레나)", "type": "pow", "pow": "4742", "tec": "3854", "stm": "3704", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "秘められたパワー4", "skill3": "", "sell": "2018/4/12", "resell": "2018/10/25", "break": "1", "special_fun": ""
  },
  {
    "id": "36", "girl": "tamaki", "name": "ノクティルカ(たまき)", "zhs_name": "夜光藻(环)", "zht_name": "夜光蟲(環)", "en_name": "Noctiluca (Tamaki)", "kr_name": "녹티르카(타마키)", "type": "pow", "pow": "4442", "tec": "3794", "stm": "3864", "apl": "200", "skill1": "強烈スパイクA", "skill2": "秘められたパワー3", "skill3": "", "sell": "2018/4/12", "resell": "2018/8/19 2019/8/19 2020/8/19 2021/4/12 2022/4/12 2023/4/12", "break": "1", "special_fun": ""
  },
  {
    "id": "37", "girl": "misaki", "name": "星色シンフォニー(みさき)", "zhs_name": "星色仙乐(海咲)", "zht_name": "星色交響曲(海咲)", "en_name": "Star-Colored Symphony (Misaki)", "kr_name": "별빛 심포니(미사키)", "type": "tec", "pow": "3944", "tec": "4802", "stm": "3696", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "", "sell": "2018/4/19", "resell": "2018/7/7 2018/8/30 2019/4/25", "break": "0", "special_fun": ""
  },
  {
    "id": "38", "girl": "kokoro", "name": "桜色ハーモニー(こころ)", "zhs_name": "樱色和弦(心)", "zht_name": "櫻花粉紅和聲(心)", "en_name": "Pink Harmony (Kokoro)", "kr_name": "연분홍색 하모니(코코로)", "type": "tec", "pow": "3944", "tec": "4802", "stm": "3696", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "", "sell": "2018/4/19", "resell": "2018/8/30 2019/4/25", "break": "0", "special_fun": ""
  },
  {
    "id": "39", "girl": "luna", "name": "ワンダーランド(ルナ)", "zhs_name": "仙境(露娜)", "zht_name": "奇幻國度(露娜)", "en_name": "Wonderland (Luna)", "kr_name": "원더랜드(루나)", "type": "tec", "pow": "3844", "tec": "4592", "stm": "3706", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "閃きのテクニック4", "skill3": "", "sell": "2018/4/26", "resell": "2018/7/26 2018/10/15 2019/2/7 2019/8/22", "break": "1", "special_fun": ""
  },
  {
    "id": "40", "girl": "tamaki", "name": "ナイトケージ(たまき)", "zhs_name": "夜笼(环)", "zht_name": "夜籠(環)", "en_name": "Night Cage (Tamaki)", "kr_name": "나이트 케이지(타마키)", "type": "stm", "pow": "4044", "tec": "3456", "stm": "4642", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "内から湧き上がるスタミナ4", "skill3": "", "sell": "2018/5/2", "resell": "2018/8/19 2019/8/19 2020/8/19 2021/4/12 2022/4/12 2023/4/12", "break": "1", "special_fun": ""
  },
  {
    "id": "41", "girl": "nyotengu", "name": "マリオネット(女天狗)", "zhs_name": "牵线木偶(女天狗)", "zht_name": "活動人偶(女天狗)", "en_name": "Marionette (Nyotengu)", "kr_name": "마리오네트(뇨텐구)", "type": "pow", "pow": "5002", "tec": "3884", "stm": "3814", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー5", "skill3": "", "sell": "2018/5/2", "resell": "2018/10/11 2019/5/3 2019/11/19", "break": "1", "special_fun": ""
  },
  {
    "id": "42", "girl": "marie", "name": "プラチナ・ミヌエット(マリー)", "zhs_name": "白金小步舞曲(玛莉)", "zht_name": "白金小步舞曲(瑪莉)", "en_name": "Platinum Minuet (Marie)", "kr_name": "플래티넘 미뉴에트(마리)", "type": "tec", "pow": "3884", "tec": "5052", "stm": "3746", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "プラチナアタッカー", "skill3": "可憐なフェイント", "sell": "2018/5/10", "resell": "2018/6/6 2018/9/19", "break": "1", "special_fun": ""
  },
  {
    "id": "43", "girl": "helena", "name": "プラチナ・フィズ(エレナ)", "zhs_name": "白金菲士(海莲娜)", "zht_name": "白金費茲(海蓮娜)", "en_name": "Platinum Fizz (Helena)", "kr_name": "플래티넘 피즈(엘레나)", "type": "tec", "pow": "3884", "tec": "5042", "stm": "3686", "apl": "230", "skill1": "完璧なレシーブA", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2018/5/10", "resell": "2018/9/19", "break": "1", "special_fun": ""
  },
  {
    "id": "44", "girl": "luna", "name": "いなば(ルナ)", "zhs_name": "因幡(露娜)", "zht_name": "因幡(露娜)", "en_name": "Inaba (Luna)", "kr_name": "이나바(루나)", "type": "apl", "pow": "3526", "tec": "3376", "stm": "4274", "apl": "500", "skill1": "強烈スパイクC", "skill2": "観客総立ちC", "skill3": "秘められたパワー4", "sell": "2018/5/17", "resell": "2018/10/15 2018/12/6 2019/5/9", "break": "1", "special_fun": ""
  },
  {
    "id": "45", "girl": "ayane", "name": "ケットシー(あやね)", "zhs_name": "猫妖(绫音)", "zht_name": "貓妖(綾音)", "en_name": "Cat Sith (Ayane)", "kr_name": "캐트 시(아야네)", "type": "apl", "pow": "3336", "tec": "4326", "stm": "3514", "apl": "500", "skill1": "高度な心理戦D", "skill2": "隠しきれない魅力4", "skill3": "熱烈なエール", "sell": "2018/5/17", "resell": "2018/8/5 2018/12/6 2019/5/9", "break": "1", "special_fun": ""
  },
  {
    "id": "46", "girl": "honoka", "name": "うすかわたけのこ(ほのか)", "zhs_name": "薄皮竹笋(穗香)", "zht_name": "薄皮竹筍(穗香)", "en_name": "Thin Towel Wrap (Honoka)", "kr_name": "박막 죽순(호노카)", "type": "pow", "pow": "4972", "tec": "3814", "stm": "3914", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "秘められたパワー6", "skill3": "", "sell": "2018/5/24", "resell": "2019/6/20 2021/12/9", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "47", "girl": "kokoro", "name": "うすかわたけのこ(こころ)", "zhs_name": "薄皮竹笋(心)", "zht_name": "薄皮竹筍(心)", "en_name": "Thin Towel Wrap (Kokoro)", "kr_name": "박막 죽순(코코로)", "type": "pow", "pow": "4952", "tec": "3954", "stm": "3794", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "秘められたパワー6", "skill3": "", "sell": "2018/5/24", "resell": "2019/6/20 2021/12/9", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "48", "girl": "momiji", "name": "やすらぎニット(紅葉)", "zhs_name": "舒适针织衫(红叶)", "zht_name": "安寧毛衣(紅葉)", "en_name": "Peaceful Knit (Momiji)", "kr_name": "편안한 니트(모미지)", "type": "stm", "pow": "4274", "tec": "3566", "stm": "4802", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "プラチナアタッカー", "skill3": "豪快なスパイク", "sell": "2018/5/31", "resell": "2018/9/20 2018/11/1 2019/9/20 2019/12/11 2020/9/20 2020/9/23", "break": "1", "special_fun": ""
  },
  {
    "id": "49", "girl": "kasumi", "name": "くつろぎニット(かすみ)", "zhs_name": "休闲针织衫(霞)", "zht_name": "寬鬆毛衣(霞)", "en_name": "Relaxing Knit (Kasumi)", "kr_name": "느긋한 니트(카스미)", "type": "tec", "pow": "3974", "tec": "5072", "stm": "3596", "apl": "200", "skill1": "完璧なレシーブD", "skill2": "高度な心理戦B", "skill3": "プラチナレシーバー", "sell": "2018/5/31", "resell": "2018/11/1 2019/12/11 2020/2/23 2020/9/23", "break": "1", "special_fun": ""
  },
  {
    "id": "50", "girl": "nyotengu", "name": "白金・けごん(女天狗)", "zhs_name": "白金华严(女天狗)", "zht_name": "白金華嚴(女天狗)", "en_name": "Platinum Kegon (Nyotengu)", "kr_name": "플래티넘 화엄(뇨텐구)", "type": "stm", "pow": "4234", "tec": "3536", "stm": "4872", "apl": "200", "skill1": "鉄壁のレシーブA", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2018/6/7", "resell": "2018/11/8 2019/8/29", "break": "1", "special_fun": ""
  },
  {
    "id": "51", "girl": "kokoro", "name": "白金・せとか(こころ)", "zhs_name": "白金濑户果(心)", "zht_name": "白金瀨戶香(心)", "en_name": "Platinum Setoka (Kokoro)", "kr_name": "플래티넘 천혜향(코코로)", "type": "pow", "pow": "5042", "tec": "3884", "stm": "3974", "apl": "200", "skill1": "強烈なプレッシャーA", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2018/6/7", "resell": "2018/11/8 2019/8/29", "break": "1", "special_fun": ""
  },
  {
    "id": "52", "girl": "hitomi", "name": "ぼうけん用サイクルウェア(ヒトミ)", "zhs_name": "冒险用骑行服(瞳)", "zht_name": "冒險用單車衣(瞳)", "en_name": "Cycle Wear for Adventures (Hitomi)", "kr_name": "모험용 사이클 웨어(히토미)", "type": "tec", "pow": "3974", "tec": "4902", "stm": "3766", "apl": "200", "skill1": "高度な心理戦D", "skill2": "プラチナアタッカー", "skill3": "可憐なフェイント", "sell": "2018/6/14", "resell": "2018/10/4 2020/10/15", "break": "1", "special_fun": ""
  },
  {
    "id": "53", "girl": "luna", "name": "たんけん用サイクルウェア(ルナ)", "zhs_name": "探险用骑行服(露娜)", "zht_name": "探險用單車衣(露娜)", "en_name": "Cycle Wear for Exploring (Luna)", "kr_name": "탐험용 사이클 웨어(루나)", "type": "tec", "pow": "3944", "tec": "4872", "stm": "3826", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "完璧なレシーブB", "skill3": "プラチナレシーバー", "sell": "2018/6/14", "resell": "2018/10/4 2020/10/15", "break": "1", "special_fun": ""
  },
  {
    "id": "54", "girl": "misaki", "name": "おつまみピンチョス(みさき)", "zhs_name": "拽拽Pinchos(海咲)", "zht_name": "拽拽Pinchos(海咲)", "en_name": "Appetizer Pinchos (Misaki)", "kr_name": "애피타이저 핀초(미사키)", "type": "pow", "pow": "5142", "tec": "3964", "stm": "3794", "apl": "200", "skill1": "強烈スパイクC", "skill2": "不動のレシーブA", "skill3": "秘められたパワー5", "sell": "2018/6/21", "resell": "2018/7/7 2018/9/22 2019/3/27 2019/7/7 2019/10/15 2020/4/6 2020/5/27 2020/7/7 2020/11/5 2021/3/25 2021/10/14", "break": "1", "special_fun": "第一件允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "55", "girl": "honoka", "name": "天使のほほえみ(ほのか)", "zhs_name": "天使的微笑(穗香)", "zht_name": "天使的微笑(穗香)", "en_name": "Angel’s Smile (Honoka)", "kr_name": "천사의 미소(호노카)", "type": "pow", "pow": "5092", "tec": "3914", "stm": "3894", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2018/6/28", "resell": "2019/1/11 2019/6/26", "break": "0", "special_fun": ""
  },
  {
    "id": "56", "girl": "marie", "name": "小悪魔のささやき(マリー)", "zhs_name": "小恶魔的耳语(玛莉)", "zht_name": "小惡魔的耳語(瑪莉)", "en_name": "Devil’s Whisper (Marie)", "kr_name": "작은 악마의 속삭임(마리)", "type": "stm", "pow": "4174", "tec": "3766", "stm": "4702", "apl": "200", "skill1": "強烈スパイクF", "skill2": "裏の裏を突くフェイントF", "skill3": "閃きのテクニック4", "sell": "2018/6/28", "resell": "2019/1/11 2019/6/26", "break": "0", "special_fun": ""
  },
  {
    "id": "57", "girl": "leifang", "name": "五色絢爛(レイファン)", "zhs_name": "五色绚烂(丽凤)", "zht_name": "五彩絢爛(麗鳳)", "en_name": "Five-Colored Brilliance (Leifang)", "kr_name": "오색 현란(레이팡)", "type": "tec", "pow": "3794", "tec": "4552", "stm": "3396", "apl": "200", "skill1": "高度な心理戦D", "skill2": "強烈なプレッシャーC", "skill3": "生粋のレシーバー3", "sell": "2018/7/5", "resell": "2019/4/23 2021/7/5 2022/7/5 2023/7/5", "break": "1", "special_fun": ""
  },
  {
    "id": "58", "girl": "kasumi", "name": "ゼラニウム(かすみ)", "zhs_name": "天竺葵(霞)", "zht_name": "天竺葵(霞)", "en_name": "Geranium (Kasumi)", "kr_name": "제라늄(카스미)", "type": "pow", "pow": "5152", "tec": "3884", "stm": "3864", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "プラチナアタッカー", "skill3": "豪快なスパイク", "sell": "2018/7/5", "resell": "2019/2/28 2020/2/23", "break": "1", "special_fun": ""
  },
  {
    "id": "59", "girl": "hitomi", "name": "キャンディーポップ(ヒトミ)", "zhs_name": "糖果汽水(瞳)", "zht_name": "糖果汽水(瞳)", "en_name": "Candy Pop (Hitomi)", "kr_name": "캔디팝(히토미)", "type": "pow", "pow": "4952", "tec": "4014", "stm": "3934", "apl": "200", "skill1": "強烈スパイクA", "skill2": "不動のレシーブF", "skill3": "プラチナレシーバー", "sell": "2018/7/5", "resell": "2019/2/28", "break": "0", "special_fun": ""
  },
  {
    "id": "60", "girl": "helena", "name": "ゴールド・ピース(エレナ)", "zhs_name": "黄金超深V(海莲娜)", "zht_name": "黃金超深V(海蓮娜)", "en_name": "Gold Peace (Helena)", "kr_name": "골드 피스(엘레나)", "type": "tec", "pow": "3884", "tec": "5082", "stm": "3676", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "完璧なレシーブE", "skill3": "プラチナレシーバー", "sell": "2018/7/12", "resell": "2019/5/23 2020/1/30 2020/9/17", "break": "0", "special_fun": ""
  },
  {
    "id": "61", "girl": "ayane", "name": "ブルー・ピース(あやね)", "zhs_name": "海蓝超深V(绫音)", "zht_name": "海藍超深V(綾音)", "en_name": "Blue Peace (Ayane)", "kr_name": "블루 피스(아야네)", "type": "tec", "pow": "3924", "tec": "5002", "stm": "3716", "apl": "200", "skill1": "高度な心理戦A", "skill2": "プラチナアタッカー", "skill3": "可憐なフェイント", "sell": "2018/7/12", "resell": "2018/8/5 2019/5/23 2019/8/5 2020/8/5 2020/9/17", "break": "0", "special_fun": ""
  },
  {
    "id": "62", "girl": "leifang", "name": "旗袍・鳳凰飛翔(レイファン)", "zhs_name": "旗袍・凤凰飞翔(丽凤)", "zht_name": "旗袍・鳳凰飛翔(麗鳳)", "en_name": "Flying Phoenix Cheongsam (Leifang)", "kr_name": "치파오(봉황비상)(레이팡)", "type": "stm", "pow": "3874", "tec": "4016", "stm": "4752", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "閃きのテクニック3", "skill3": "熱烈なエール", "sell": "2018/7/19", "resell": "2019/4/23 2020/4/23 2021/7/5 2022/7/5 2023/7/5", "break": "0", "special_fun": ""
  },
  {
    "id": "63", "girl": "leifang", "name": "旗袍・陰陽太極(レイファン)", "zhs_name": "旗袍・阴阳太极(丽凤)", "zht_name": "旗袍・陰陽太極(麗鳳)", "en_name": "Yinyang Taichi Cheongsam (Leifang)", "kr_name": "치파오(음양태극)(레이팡)", "type": "stm", "pow": "4244", "tec": "3576", "stm": "4822", "apl": "200", "skill1": "強烈スパイクF", "skill2": "秘められたパワー3", "skill3": "熱烈なエール", "sell": "2018/7/19", "resell": "2019/4/23 2020/4/23 2021/7/5 2022/7/5 2023/7/5", "break": "0", "special_fun": ""
  },
  {
    "id": "64", "girl": "luna", "name": "旗袍・玄武(ルナ)", "zhs_name": "旗袍・玄武(露娜)", "zht_name": "旗袍・玄武(露娜)", "en_name": "Black Tortoise Cheongsam (Luna)", "kr_name": "치파오(현무)(루나)", "type": "stm", "pow": "3984", "tec": "3926", "stm": "4732", "apl": "200", "skill1": "高度な心理戦D", "skill2": "プラチナアタッカー", "skill3": "可憐なフェイント", "sell": "2018/7/19", "resell": "2018/10/15 2018/11/22 2019/3/20 2019/5/2 2020/4/30 2021/1/1 2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "65", "girl": "marie", "name": "旗袍・青龍(マリー)", "zhs_name": "旗袍・青龙(玛莉)", "zht_name": "旗袍・青龍(瑪莉)", "en_name": "Blue Dragon Cheongsam (Marie)", "kr_name": "치파오(청룡)(마리)", "type": "tec", "pow": "3884", "tec": "5082", "stm": "3676", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナB", "skill3": "閃きのテクニック5", "sell": "2018/7/19", "resell": "2018/11/22 2019/3/20 2019/5/2 2020/4/30 2021/1/1 2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "66", "girl": "kokoro", "name": "旗袍・白虎(こころ)", "zhs_name": "旗袍・白虎(心)", "zht_name": "旗袍・白虎(心)", "en_name": "White Tiger Cheongsam (Kokoro)", "kr_name": "치파오(백호)(코코로)", "type": "stm", "pow": "4144", "tec": "3816", "stm": "4682", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "驚異のスタミナA", "skill3": "閃きのテクニック5", "sell": "2018/7/19", "resell": "2018/11/22 2019/3/20 2019/5/2 2020/4/30 2021/1/1 2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "67", "girl": "tamaki", "name": "リナライトプリズム(たまき)", "zhs_name": "青石棱镜(环)", "zht_name": "青石棱鏡 (環)", "en_name": "Linarite Prism (Tamaki)", "kr_name": "리나라이트 프리즘(타마키)", "type": "pow", "pow": "5002", "tec": "3964", "stm": "3934", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2018/7/26", "resell": "2018/8/19 2018/11/18 2020/1/16", "break": "1", "special_fun": ""
  },
  {
    "id": "68", "girl": "helena", "name": "テルライトプリズム(エレナ)", "zhs_name": "黄水晶棱镜(海莲娜)", "zht_name": "黃水晶棱鏡(海蓮娜)", "en_name": "Tellurite Prism (Helena)", "kr_name": "텔라이트 프리즘(엘레나)", "type": "stm", "pow": "4224", "tec": "3626", "stm": "4792", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "高度な心理戦D", "skill3": "内から湧き上がるスタミナ3", "sell": "2018/7/26", "resell": "2018/11/18 2020/1/16", "break": "1", "special_fun": ""
  },
  {
    "id": "69", "girl": "momiji", "name": "ロゼライトプリズム(紅葉)", "zhs_name": "玫瑰石棱镜(红叶)", "zht_name": "玫瑰石棱鏡(紅葉)", "en_name": "Roselite Prism (Momiji)", "kr_name": "로제라이트 프리즘(모미지)", "type": "pow", "pow": "5082", "tec": "3954", "stm": "3864", "apl": "200", "skill1": "強烈スパイクD", "skill2": "灼熱のダンスB", "skill3": "秘められたパワー3", "sell": "2018/7/26", "resell": "2018/9/20 2018/11/18 2020/1/16", "break": "1", "special_fun": ""
  },
  {
    "id": "70", "girl": "leifang", "name": "サンドイッチ(レイファン)", "zhs_name": "三明治(丽凤)", "zht_name": "三明治(麗鳳)", "en_name": "Sandwich (Leifang)", "kr_name": "샌드위치(레이팡)", "type": "pow", "pow": "5232", "tec": "3844", "stm": "3824", "apl": "200", "skill1": "強烈なプレッシャーA", "skill2": "不動のレシーブB", "skill3": "プラチナレシーバー", "sell": "2018/7/26", "resell": "2019/4/23 2020/4/23 2021/7/5 2022/7/5 2023/7/5", "break": "0", "special_fun": ""
  },
  {
    "id": "71", "girl": "nyotengu", "name": "紅孔雀(女天狗)", "zhs_name": "红孔雀(女天狗)", "zht_name": "紅孔雀(女天狗)", "en_name": "Crimson Peacock (Nyotengu)", "kr_name": "붉은 공작(뇨텐구)", "type": "apl", "pow": "3636", "tec": "4026", "stm": "3514", "apl": "500", "skill1": "高度な心理戦A", "skill2": "隠しきれない魅力4", "skill3": "可憐なフェイント", "sell": "2018/8/2", "resell": "2019/1/18 2019/4/11 2019/7/11 2019/11/19 2020/7/31", "break": "1", "special_fun": ""
  },
  {
    "id": "72", "girl": "tamaki", "name": "藍孔雀(たまき)", "zhs_name": "蓝孔雀(环)", "zht_name": "藍孔雀(環)", "en_name": "Indigo Peacock (Tamaki)", "kr_name": "쪽빛 공작(타마키)", "type": "apl", "pow": "3926", "tec": "3776", "stm": "3474", "apl": "500", "skill1": "強烈スパイクB", "skill2": "観客総立ちC", "skill3": "隠しきれない魅力4", "sell": "2018/8/2", "resell": "2018/8/19 2019/1/18 2019/4/11 2019/7/11 2020/7/31", "break": "1", "special_fun": ""
  },
  {
    "id": "73", "girl": "marie", "name": "うすかわたけのこ(マリー)", "zhs_name": "薄皮竹笋(玛莉)", "zht_name": "薄皮竹筍(瑪莉)", "en_name": "Thin Towel Wrap (Marie)", "kr_name": "박막 죽순(마리)", "type": "pow", "pow": "4972", "tec": "3814", "stm": "3914", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "秘められたパワー6", "skill3": "", "sell": "2018/8/9", "resell": "2019/6/14 2021/12/9", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "74", "girl": "kasumi", "name": "うすかわたけのこ(かすみ)", "zhs_name": "薄皮竹笋(霞)", "zht_name": "薄皮竹筍(霞)", "en_name": "Thin Towel Wrap (Kasumi)", "kr_name": "박막 죽순(카스미)", "type": "pow", "pow": "4972", "tec": "3814", "stm": "3914", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "秘められたパワー6", "skill3": "", "sell": "2018/8/9", "resell": "2019/6/14 2021/12/9", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "75", "girl": "luna", "name": "うすかわたけのこ(ルナ)", "zhs_name": "薄皮竹笋(露娜)", "zht_name": "薄皮竹筍(露娜)", "en_name": "Thin Towel Wrap (Luna)", "kr_name": "박막 죽순(루나)", "type": "tec", "pow": "3894", "tec": "4882", "stm": "3666", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "閃きのテクニック6", "skill3": "", "sell": "2018/8/16", "resell": "2019/9/5 2021/12/9", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "76", "girl": "momiji", "name": "うすかわたけのこ(紅葉)", "zhs_name": "薄皮竹笋(红叶)", "zht_name": "薄皮竹筍(紅葉)", "en_name": "Thin Towel Wrap (Momiji)", "kr_name": "박막 죽순(모미지)", "type": "tec", "pow": "3894", "tec": "4882", "stm": "3666", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "閃きのテクニック6", "skill3": "", "sell": "2018/8/16", "resell": "2019/9/5 2021/12/9", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "77", "girl": "honoka", "name": "ピーチシロップ(ほのか)", "zhs_name": "蜜桃糖浆(穗香)", "zht_name": "蜜桃糖漿(穗香)", "en_name": "Peach Syrup (Honoka)", "kr_name": "피치 시럽(호노카)", "type": "stm", "pow": "3904", "tec": "4016", "stm": "4922", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "高度な心理戦D", "skill3": "内から湧き上がるスタミナ6", "sell": "2018/8/23", "resell": "2019/7/31 2021/9/3", "break": "1", "special_fun": ""
  },
  {
    "id": "78", "girl": "kokoro", "name": "ブルーハワイ(こころ)", "zhs_name": "蓝色夏威夷(心)", "zht_name": "藍色夏威夷(心)", "en_name": "Blue Hawaii (Kokoro)", "kr_name": "블루 하와이(코코로)", "type": "tec", "pow": "3864", "tec": "5052", "stm": "3726", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2018/8/23", "resell": "2019/7/31 2019/12/1 2021/9/3", "break": "1", "special_fun": ""
  },
  {
    "id": "79", "girl": "ayane", "name": "しろほおずき(あやね)", "zhs_name": "素白鬼灯(绫音)", "zht_name": "素白鬼燈(綾音)", "en_name": "White Physalis (Ayane)", "kr_name": "백귀등(아야네)", "type": "pow", "pow": "5032", "tec": "3934", "stm": "3934", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2018/8/30", "resell": "2019/4/18 2019/7/18 2020/1/22", "break": "1", "special_fun": ""
  },
  {
    "id": "80", "girl": "kasumi", "name": "しろほおずき(かすみ)", "zhs_name": "素白鬼灯(霞)", "zht_name": "素白鬼燈(霞)", "en_name": "White Physalis (Kasumi)", "kr_name": "백귀등(카스미)", "type": "stm", "pow": "4424", "tec": "3816", "stm": "4902", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "強烈なプレッシャーC", "skill3": "内から湧き上がるスタミナ6", "sell": "2018/8/30", "resell": "2019/4/18 2019/7/18 2020/1/22", "break": "1", "special_fun": ""
  },
  {
    "id": "81", "girl": "misaki", "name": "こもれびハミング(みさき)", "zhs_name": "树荫光斑蜂鸟(海咲)", "zht_name": "樹蔭光斑蜂鳥(海咲)", "en_name": "Sunlight Humming (Misaki)", "kr_name": "햇살 속의 허밍(미사키)", "type": "stm", "pow": "4344", "tec": "3856", "stm": "4842", "apl": "200", "skill1": "灼熱のダンスA", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2018/9/6", "resell": "2019/3/14 2019/8/15 2020/6/7 2021/8/27 2022/1/19 2022/9/8", "break": "1", "special_fun": ""
  },
  {
    "id": "82", "girl": "hitomi", "name": "こもれびハミング(ヒトミ)", "zhs_name": "树荫光斑蜂鸟(瞳)", "zht_name": "樹蔭光斑蜂鳥(瞳)", "en_name": "Sunlight Humming (Hitomi)", "kr_name": "햇살 속의 허밍(히토미)", "type": "pow", "pow": "4982", "tec": "3964", "stm": "3954", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "灼熱のダンスC", "skill3": "秘められたパワー6", "sell": "2018/9/6", "resell": "2019/3/14 2019/8/15 2020/6/7 2021/8/27 2022/1/19 2022/9/8", "break": "1", "special_fun": ""
  },
  {
    "id": "83", "girl": "luna", "name": "げんげつのあさり(ルナ)", "zhs_name": "弦月之贝(露娜)", "zht_name": "弦月之貝(露娜)", "en_name": "Crescent Moon Set (Luna)", "kr_name": "초승달 조개잡이(루나)", "type": "tec", "pow": "3814", "tec": "4902", "stm": "3926", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "驚異のスタミナF", "skill3": "閃きのテクニック6", "sell": "2018/9/13", "resell": "2018/10/15 2018/12/27 2019/4/4", "break": "1", "special_fun": ""
  },
  {
    "id": "84", "girl": "momiji", "name": "ゆうづきのあさり(紅葉)", "zhs_name": "夕月之贝(红叶)", "zht_name": "夕月之貝(紅葉)", "en_name": "Evening Moon Set (Momiji)", "kr_name": "저녁달 조개잡이(모미지)", "type": "tec", "pow": "3834", "tec": "4972", "stm": "3836", "apl": "200", "skill1": "鉄壁のレシーブD", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2018/9/13", "resell": "2018/9/20 2018/12/27 2019/4/4", "break": "1", "special_fun": ""
  },
  {
    "id": "85", "girl": "tamaki", "name": "おつまみピンチョス(たまき)", "zhs_name": "拽拽Pinchos(环)", "zht_name": "拽拽Pinchos(環)", "en_name": "Appetizer Pinchos (Tamaki)", "kr_name": "애피타이저 핀초(타마키)", "type": "stm", "pow": "4394", "tec": "3866", "stm": "4882", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "内から湧き上がるスタミナ5", "sell": "2018/9/19", "resell": "2019/1/25 2019/3/27 2019/10/9 2020/4/6 2020/8/21 2020/11/5 2021/10/14", "break": "1", "special_fun": "第二件允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "86", "girl": "fiona", "name": "ノーブル・チュチュ(フィオナ)", "zhs_name": "贵族芭蕾舞裙(菲欧娜)", "zht_name": "貴族芭蕾舞裙(菲歐娜)", "en_name": "Noble Tutu (Fiona)", "kr_name": "노블 츄츄(피오나)", "type": "stm", "pow": "4024", "tec": "3456", "stm": "4562", "apl": "200", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナD", "skill3": "内から湧き上がるスタミナ3", "sell": "2018/9/27", "resell": "2019/2/11 2020/2/11 2021/9/27 2022/9/27", "break": "1", "special_fun": ""
  },
  {
    "id": "87", "girl": "marie", "name": "キムリック(マリー)", "zhs_name": "威尔士猫(玛莉)", "zht_name": "威爾斯貓(瑪莉)", "en_name": "Cymric (Marie)", "kr_name": "킴릭(마리)", "type": "pow", "pow": "4942", "tec": "4064", "stm": "3894", "apl": "200", "skill1": "強烈スパイクB", "skill2": "高度な心理戦C", "skill3": "秘められたパワー5", "sell": "2018/9/27", "resell": "2019/4/11 2019/6/6 2020/2/27 2020/5/18 2020/6/6", "break": "0", "special_fun": ""
  },
  {
    "id": "88", "girl": "helena", "name": "リベルテ(エレナ)", "zhs_name": "自由(海莲娜)", "zht_name": "自由(海蓮娜)", "en_name": "Liberte (Helena)", "kr_name": "리베르테(엘레나)", "type": "pow", "pow": "5042", "tec": "3944", "stm": "3914", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "プラチナアタッカー", "skill3": "豪快なスパイク", "sell": "2018/9/27", "resell": "2019/4/11 2020/2/27 2020/5/18", "break": "0", "special_fun": ""
  },
  {
    "id": "89", "girl": "nyotengu", "name": "レッド・キャビア(女天狗)", "zhs_name": "鲜红・鱼子酱(女天狗)", "zht_name": "紅色魚子醬(女天狗)", "en_name": "Red Caviar (Nyotengu)", "kr_name": "레드 캐비어(뇨텐구)", "type": "tec", "pow": "4054", "tec": "4952", "stm": "3636", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "強烈なプレッシャーC", "skill3": "閃きのテクニック5", "sell": "2018/10/4", "resell": "2019/6/7 2019/11/19", "break": "1", "special_fun": ""
  },
  {
    "id": "90", "girl": "honoka", "name": "アルマス・キャビア(ほのか)", "zhs_name": "阿尔马斯・鱼子酱(穗香)", "zht_name": "阿爾馬斯魚子醬(穗香)", "en_name": "Almas Caviar (Honoka)", "kr_name": "알머스 캐비어(호노카)", "type": "tec", "pow": "4124", "tec": "4842", "stm": "3676", "apl": "200", "skill1": "高度な心理戦D", "skill2": "プラチナアタッカー", "skill3": "可憐なフェイント", "sell": "2018/10/4", "resell": "2019/3/24 2019/6/7 2020/3/24", "break": "1", "special_fun": ""
  },
  {
    "id": "91", "girl": "marie", "name": "デスチャ・ダビコスチューム(マリー)", "zhs_name": "命运之子・妲比服装(玛莉)", "zht_name": "命運之子‧妲比服裝(瑪莉)", "en_name": "Destiny Child Davi Costume (Marie)", "kr_name": "데스티니 차일드 다비 코스튬(마리)", "type": "pow", "pow": "5042", "tec": "4174", "stm": "3884", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "エンジェルスパイク", "skill3": "豪快なスパイク", "sell": "2018/10/11", "resell": "2020/10/7", "break": "1", "special_fun": "Destiny Child 天命之子 联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "92", "girl": "tamaki", "name": "デスチャ・モナコスチューム(たまき)", "zhs_name": "命运之子・莫娜服装(环)", "zht_name": "命運之子‧莫娜服裝(環)", "en_name": "Destiny Child Mona Costume (Tamaki)", "kr_name": "데스티니 차일드 모나 코스튬(타마키)", "type": "pow", "pow": "5192", "tec": "4054", "stm": "3854", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2018/10/11", "resell": "2020/10/7", "break": "1", "special_fun": "Destiny Child 天命之子 联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "93", "girl": "misaki", "name": "デスチャ・リザコスチューム(みさき)", "zhs_name": "命运之子・丽莎服装(海咲)", "zht_name": "命運之子‧麗莎服裝(海咲)", "en_name": "Destiny Child Lisa Costume (Misaki)", "kr_name": "데스티니 차일드 리자 코스튬(미사키)", "type": "stm", "pow": "4614", "tec": "4136", "stm": "4792", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "エンジェルスパイク", "skill3": "豪快なスパイク", "sell": "2018/10/18", "resell": "2020/10/7", "break": "1", "special_fun": "Destiny Child 天命之子 联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "94", "girl": "kasumi", "name": "デスチャ・イブコスチューム(かすみ)", "zhs_name": "命运之子・夏娃服装(霞)", "zht_name": "命運之子‧夏娃服裝(霞)", "en_name": "Destiny Child Eve Costume (Kasumi)", "kr_name": "데스티니 차일드 이브 코스튬(카스미)", "type": "stm", "pow": "4624", "tec": "4236", "stm": "4682", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2018/10/18", "resell": "2020/10/7", "break": "1", "special_fun": "Destiny Child 天命之子 联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "95", "girl": "fiona", "name": "セレナーデ(フィオナ)", "zhs_name": "小夜曲(菲欧娜)", "zht_name": "小夜曲(菲歐娜)", "en_name": "Serenade (Fiona)", "kr_name": "세레나데(피오나)", "type": "tec", "pow": "4134", "tec": "4782", "stm": "3726", "apl": "200", "skill1": "高度な心理戦E", "skill2": "プラチナアタッカー", "skill3": "可憐なフェイント", "sell": "2018/10/25", "resell": "2019/2/11 2020/2/11 2021/9/27 2022/9/27", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "96", "girl": "ayane", "name": "タイドプール(あやね)", "zhs_name": "潮池(绫音)", "zht_name": "潮池(綾音)", "en_name": "Tide Pool (Ayane)", "kr_name": "타이드 풀(아야네)", "type": "tec", "pow": "3934", "tec": "4912", "stm": "3796", "apl": "200", "skill1": "灼熱のダンスD", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2018/10/25", "resell": "", "break": "0", "special_fun": ""
  },
  {
    "id": "97", "girl": "kokoro", "name": "ストラタム(こころ)", "zhs_name": "横纹渐变(心)", "zht_name": "橫紋漸變(心)", "en_name": "Stratum (Kokoro)", "kr_name": "스트레이텀(코코로)", "type": "tec", "pow": "4094", "tec": "5042", "stm": "3606", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "強烈なプレッシャーC", "skill3": "閃きのテクニック5", "sell": "2018/10/25", "resell": "2019/12/1", "break": "0", "special_fun": ""
  },
  {
    "id": "98", "girl": "honoka", "name": "スマイルポップ(ほのか)", "zhs_name": "微笑POP(穗香)", "zht_name": "微笑POP(穗香)", "en_name": "Smile Pop (Honoka)", "kr_name": "스마일 팝(호노카)", "type": "stm", "pow": "4084", "tec": "4186", "stm": "4872", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "強烈なプレッシャーB", "skill3": "内から湧き上がるスタミナ5", "sell": "2018/11/1", "resell": "2019/7/4 2020/2/6", "break": "1", "special_fun": ""
  },
  {
    "id": "99", "girl": "luna", "name": "スマイルポップ(ルナ)", "zhs_name": "微笑POP(露娜)", "zht_name": "微笑POP(露娜)", "en_name": "Smile Pop (Luna)", "kr_name": "스마일 팝(루나)", "type": "stm", "pow": "4174", "tec": "4066", "stm": "4802", "apl": "200", "skill1": "高度な心理戦F", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2018/11/1", "resell": "2019/7/4 2020/2/6", "break": "1", "special_fun": ""
  },
  {
    "id": "100_1", "girl": "misaki", "name": "SOS団コーデガチャ(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3834", "stm": "4014", "apl": "230", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナA", "skill3": "団長のパワー", "sell": "2018/11/5", "resell": "", "break": "1", "special_fun": "凉宫春日的犹豫 吃相难看，敷衍狗屎的联动服装"
  },
  {
    "id": "100_2", "girl": "hitomi", "name": "SOS団コーデガチャ(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3834", "stm": "4014", "apl": "230", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナA", "skill3": "団長のパワー", "sell": "2018/11/5", "resell": "", "break": "1", "special_fun": "凉宫春日的犹豫 吃相难看，敷衍狗屎的联动服装"
  },
  {
    "id": "100_3", "girl": "momiji", "name": "SOS団コーデガチャ(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3834", "stm": "4014", "apl": "230", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナA", "skill3": "団長のパワー", "sell": "2018/11/5", "resell": "", "break": "1", "special_fun": "凉宫春日的犹豫 吃相难看，敷衍狗屎的联动服装"
  },
  {
    "id": "100_4", "girl": "honoka", "name": "SOS団コーデガチャ(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3834", "stm": "4014", "apl": "230", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナA", "skill3": "団長のパワー", "sell": "2018/11/5", "resell": "", "break": "1", "special_fun": "凉宫春日的犹豫 吃相难看，敷衍狗屎的联动服装"
  },
  {
    "id": "100_5", "girl": "kasumi", "name": "SOS団コーデガチャ(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3834", "stm": "4014", "apl": "230", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナA", "skill3": "団長のパワー", "sell": "2018/11/5", "resell": "", "break": "1", "special_fun": "凉宫春日的犹豫 吃相难看，敷衍狗屎的联动服装"
  },
  {
    "id": "100_6", "girl": "ayane", "name": "SOS団コーデガチャ(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3834", "stm": "4014", "apl": "230", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナA", "skill3": "団長のパワー", "sell": "2018/11/5", "resell": "", "break": "1", "special_fun": "凉宫春日的犹豫 吃相难看，敷衍狗屎的联动服装"
  },
  {
    "id": "100_7", "girl": "luna", "name": "SOS団コーデガチャ(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3834", "stm": "4014", "apl": "230", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナA", "skill3": "団長のパワー", "sell": "2018/11/5", "resell": "", "break": "1", "special_fun": "凉宫春日的犹豫 吃相难看，敷衍狗屎的联动服装"
  },
  {
    "id": "100_8", "girl": "tamaki", "name": "SOS団コーデガチャ(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3834", "stm": "4014", "apl": "230", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナA", "skill3": "団長のパワー", "sell": "2018/11/5", "resell": "", "break": "1", "special_fun": "凉宫春日的犹豫 吃相难看，敷衍狗屎的联动服装"
  },
  {
    "id": "100_9", "girl": "nyotengu", "name": "SOS団コーデガチャ(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3834", "stm": "4014", "apl": "230", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナA", "skill3": "団長のパワー", "sell": "2018/11/5", "resell": "", "break": "1", "special_fun": "凉宫春日的犹豫 吃相难看，敷衍狗屎的联动服装"
  },
  {
    "id": "100_10", "girl": "marie", "name": "SOS団コーデガチャ(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3834", "stm": "4014", "apl": "230", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナA", "skill3": "団長のパワー", "sell": "2018/11/5", "resell": "", "break": "1", "special_fun": "凉宫春日的犹豫 吃相难看，敷衍狗屎的联动服装"
  },
  {
    "id": "100_11", "girl": "kokoro", "name": "SOS団コーデガチャ(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3834", "stm": "4014", "apl": "230", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナA", "skill3": "団長のパワー", "sell": "2018/11/5", "resell": "", "break": "1", "special_fun": "凉宫春日的犹豫 吃相难看，敷衍狗屎的联动服装"
  },
  {
    "id": "100_12", "girl": "helena", "name": "SOS団コーデガチャ(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3834", "stm": "4014", "apl": "230", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナA", "skill3": "団長のパワー", "sell": "2018/11/5", "resell": "", "break": "1", "special_fun": "凉宫春日的犹豫 吃相难看，敷衍狗屎的联动服装"
  },
  {
    "id": "101", "girl": "leifang", "name": "カラフルウィット(レイファン)", "zhs_name": "缤纷妙趣(丽凤)", "zht_name": "繽紛妙趣(麗鳳)", "en_name": "Colorful Wit (Leifang)", "kr_name": "컬러풀 위트(레이팡)", "type": "pow", "pow": "4892", "tec": "4174", "stm": "3834", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "高度な心理戦C", "skill3": "秘められたパワー6", "sell": "2018/11/8", "resell": "2019/5/16", "break": "1", "special_fun": ""
  },
  {
    "id": "102", "girl": "hitomi", "name": "カラフルウィット(ヒトミ)", "zhs_name": "缤纷妙趣(瞳)", "zht_name": "繽紛妙趣(瞳)", "en_name": "Colorful Wit (Hitomi)", "kr_name": "컬러풀 위트(히토미)", "type": "pow", "pow": "5002", "tec": "4054", "stm": "3844", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "プラチナアタッカー", "skill3": "豪快なスパイク", "sell": "2018/11/8", "resell": "2019/5/16", "break": "1", "special_fun": ""
  },
  {
    "id": "103_1", "girl": "kasumi", "name": "ファースト・ルージュ(かすみ)", "zhs_name": "嫣红桂冠(霞)", "zht_name": "嫣红桂冠(霞)", "en_name": "First Rouge (Kasumi)", "kr_name": "퍼스트 루주(카스미)", "type": "pow", "pow": "4852", "tec": "3954", "stm": "4044", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/18", "resell": "2019/11/23 2020/2/23 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "103_2", "girl": "misaki", "name": "ファースト・ルージュ(みさき)", "zhs_name": "嫣红桂冠(海咲)", "zht_name": "嫣红桂冠(海咲)", "en_name": "First Rouge (Misaki)", "kr_name": "퍼스트 루주(미사키)", "type": "pow", "pow": "4852", "tec": "3954", "stm": "4044", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/18", "resell": "2019/11/23 2020/3/5 2020/7/7 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "103_3", "girl": "marie", "name": "ファースト・ルージュ(マリー)", "zhs_name": "嫣红桂冠(玛莉)", "zht_name": "嫣红桂冠(玛莉)", "en_name": "First Rouge (Marie)", "kr_name": "퍼스트 루주(마리)", "type": "pow", "pow": "4852", "tec": "3954", "stm": "4044", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/18", "resell": "2019/11/23 2020/6/6 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "103_4", "girl": "luna", "name": "ファースト・ルージュ(ルナ)", "zhs_name": "嫣红桂冠(露娜)", "zht_name": "嫣红桂冠(露娜)", "en_name": "First Rouge (Luna)", "kr_name": "퍼스트 루주(루나)", "type": "pow", "pow": "4852", "tec": "3954", "stm": "4044", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/18", "resell": "2019/11/23 2020/3/5 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "103_5", "girl": "honoka", "name": "ファースト・ルージュ(ほのか)", "zhs_name": "嫣红桂冠(穗香)", "zht_name": "嫣红桂冠(穗香)", "en_name": "First Rouge (Honoka)", "kr_name": "퍼스트 루주(호노카)", "type": "pow", "pow": "4852", "tec": "3954", "stm": "4044", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/18", "resell": "2019/11/23 2020/3/5 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "103_6", "girl": "kokoro", "name": "ファースト・ルージュ(こころ)", "zhs_name": "嫣红桂冠(心)", "zht_name": "嫣红桂冠(心)", "en_name": "First Rouge (Kokoro)", "kr_name": "퍼스트 루주(코코로)", "type": "pow", "pow": "4852", "tec": "3954", "stm": "4044", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/18", "resell": "2019/11/23 2019/12/1 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "103_7", "girl": "hitomi", "name": "ファースト・ルージュ(ヒトミ)", "zhs_name": "嫣红桂冠(瞳)", "zht_name": "嫣红桂冠(瞳)", "en_name": "First Rouge (Hitomi)", "kr_name": "퍼스트 루주(히토미)", "type": "pow", "pow": "4852", "tec": "3954", "stm": "4044", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/18", "resell": "2019/11/23 2020/5/25 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "104", "girl": "nyotengu", "name": "ステラ・スコルピオン(女天狗)", "zhs_name": "星辰‧天蝎(女天狗)", "zht_name": "星辰・天蠍(女天狗)", "en_name": "Stellar Scorpion (Nyotengu)", "kr_name": "스텔라 스콜피온(뇨텐구)", "type": "pow", "pow": "5322", "tec": "3884", "stm": "3994", "apl": "200", "skill1": "強烈スパイクC", "skill2": "スコルピオン・パワー", "skill3": "豪快なスパイク", "sell": "2018/11/19", "resell": "2019/10/31 2019/11/19 2020/11/19 2021/9/16 2021/11/19 2022/9/8 2022/11/19", "break": "1", "special_fun": "强力生日服装 可惜出的早没有粒子光效（后续添加了特效）"
  },
  {
    "id": "105_1", "girl": "ayane", "name": "プレミア・ナイト(あやね)", "zhs_name": "典藏之夜(绫音)", "zht_name": "典藏之夜(绫音)", "en_name": "Premier Night (Ayane)", "kr_name": "프리미어 나이트(아야네)", "type": "pow", "pow": "4782", "tec": "4004", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/22", "resell": "2019/11/23 2020/3/5 2020/8/5 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "105_2", "girl": "tamaki", "name": "プレミア・ナイト(たまき)", "zhs_name": "典藏之夜(环)", "zht_name": "典藏之夜(环)", "en_name": "Premier Night (Tamaki)", "kr_name": "프리미어 나이트(타마키)", "type": "pow", "pow": "4782", "tec": "4004", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/22", "resell": "2019/11/23 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "105_3", "girl": "nyotengu", "name": "プレミア・ナイト(女天狗)", "zhs_name": "典藏之夜(女天狗)", "zht_name": "典藏之夜(女天狗)", "en_name": "Premier Night (Nyotengu)", "kr_name": "프리미어 나이트(뇨텐구)", "type": "pow", "pow": "4782", "tec": "4004", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/22", "resell": "2019/11/23 2019/11/19 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "105_4", "girl": "leifang", "name": "プレミア・ナイト(レイファン)", "zhs_name": "典藏之夜(丽凤)", "zht_name": "典藏之夜(丽凤)", "en_name": "Premier Night (Leifang)", "kr_name": "프리미어 나이트(레이팡)", "type": "pow", "pow": "4782", "tec": "4004", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/22", "resell": "2019/11/23 2020/3/5 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "105_5", "girl": "momiji", "name": "プレミア・ナイト(紅葉)", "zhs_name": "典藏之夜(红叶)", "zht_name": "典藏之夜(红叶)", "en_name": "Premier Night (Momiji)", "kr_name": "프리미어 나이트(모미지)", "type": "pow", "pow": "4782", "tec": "4004", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/22", "resell": "2019/11/23 2020/9/20 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "105_6", "girl": "helena", "name": "プレミア・ナイト(エレナ)", "zhs_name": "典藏之夜(海莲娜)", "zht_name": "典藏之夜(海莲娜)", "en_name": "Premier Night (Helena)", "kr_name": "프리미어 나이트(엘레나)", "type": "pow", "pow": "4782", "tec": "4004", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2018/11/22", "resell": "2019/11/23 2020/1/30 2020/3/5 2020/11/24 2023/5/19", "break": "1", "special_fun": "游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "106", "girl": "tamaki", "name": "クリムゾン・フェザー(たまき)", "zhs_name": "深红羽翼(环)", "zht_name": "深紅羽翼(環)", "en_name": "Crimson Feather (Tamaki)", "kr_name": "크림슨 페더(타마키)", "type": "apl", "pow": "4006", "tec": "4556", "stm": "3814", "apl": "600", "skill1": "高度な心理戦A", "skill2": "隠しきれない魅力5", "skill3": "可憐なフェイント", "sell": "2018/11/29", "resell": "2019/9/14", "break": "1", "special_fun": ""
  },
  {
    "id": "107", "girl": "kasumi", "name": "ブロッサム・フェザー(かすみ)", "zhs_name": "花簇羽翼(霞)", "zht_name": "花簇羽翼(霞)", "en_name": "Blossom Feather (Kasumi)", "kr_name": "블로섬 페더(카스미)", "type": "apl", "pow": "3806", "tec": "4766", "stm": "3904", "apl": "600", "skill1": "裏の裏を突くフェイントE", "skill2": "観客総立ちB", "skill3": "隠しきれない魅力5", "sell": "2018/11/29", "resell": "2019/9/14", "break": "1", "special_fun": ""
  },
  {
    "id": "108", "girl": "kokoro", "name": "ステラ・サジタリウス(こころ)", "zhs_name": "星辰‧射手(心)", "zht_name": "星辰・射手(心)", "en_name": "Stellar Sagittarius (Kokoro)", "kr_name": "스텔라 사지타리우스(코코로)", "type": "tec", "pow": "3884", "tec": "5322", "stm": "3736", "apl": "200", "skill1": "高度な心理戦D", "skill2": "サジタリウス・テクニック", "skill3": "可憐なフェイント", "sell": "2018/12/1", "resell": "2019/10/31 2019/12/1 2020/12/1 2021/9/16 2021/12/1 2022/9/8 2022/12/1", "break": "1", "special_fun": "坑爹生日第一弹 一个后妈力量角色本来力量衣服就少 生日你给我来个技巧服？"
  },
  {
    "id": "109", "girl": "leifang", "name": "ピンキー・プラム(レイファン)", "zhs_name": "粉嫩布霖(丽凤)", "zht_name": "粉嫩布霖(麗鳳)", "en_name": "Pinky Plum (Leifang)", "kr_name": "핑키 플럼(레이팡)", "type": "tec", "pow": "4104", "tec": "4782", "stm": "3756", "apl": "200", "skill1": "高度な心理戦E", "skill2": "プラチナアタッカー", "skill3": "可憐なフェイント", "sell": "2018/12/6", "resell": "2019/7/25", "break": "1", "special_fun": ""
  },
  {
    "id": "110", "girl": "misaki", "name": "ミルキー・プラム(みさき)", "zhs_name": "奶白布霖(海咲)", "zht_name": "奶白布霖(海咲)", "en_name": "Milky Plum (Misaki)", "kr_name": "밀키 플럼(미사키)", "type": "tec", "pow": "4144", "tec": "4812", "stm": "3686", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "強烈なプレッシャーF", "skill3": "閃きのテクニック6", "sell": "2018/12/6", "resell": "2019/7/25", "break": "1", "special_fun": ""
  },
  {
    "id": "111_1", "girl": "momiji", "name": "フレーズノエル(紅葉)", "zhs_name": "草莓圣诞(红叶)", "zht_name": "草莓聖誕(紅葉)", "en_name": "Noël aux Fraises (Momiji)", "kr_name": "프레이즈 노엘(모미지)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": "2019/12/17 2020/9/20 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_2", "girl": "helena", "name": "フレーズノエル(エレナ)", "zhs_name": "草莓圣诞(海莲娜)", "zht_name": "草莓聖誕(海蓮娜)", "en_name": "Noël aux Fraises (Helena)", "kr_name": "프레이즈 노엘(엘레나)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": "2019/12/17 2020/1/30 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_3", "girl": "luna", "name": "フレーズノエル(ルナ)", "zhs_name": "草莓圣诞(露娜)", "zht_name": "草莓聖誕(露娜)", "en_name": "Noël aux Fraises (Luna)", "kr_name": "프레이즈 노엘(루나)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": "2019/12/17 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_4", "girl": "ayane", "name": "フレーズノエル(あやね)", "zhs_name": "草莓圣诞(绫音)", "zht_name": "草莓聖誕(綾音)", "en_name": "Noël aux Fraises (Ayane)", "kr_name": "프레이즈 노엘(아야네)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": "2019/12/17 2020/8/5 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_5", "girl": "kasumi", "name": "フレーズノエル(かすみ)", "zhs_name": "草莓圣诞(霞)", "zht_name": "草莓聖誕(霞)", "en_name": "Noël aux Fraises (Kasumi)", "kr_name": "프레이즈 노엘(카스미)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": "2019/12/17 2020/2/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_6", "girl": "hitomi", "name": "フレーズノエル(ヒトミ)", "zhs_name": "草莓圣诞(瞳)", "zht_name": "草莓聖誕(瞳)", "en_name": "Noël aux Fraises (Hitomi)", "kr_name": "프레이즈 노엘(히토미)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": "2019/12/17 2020/5/25 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_7", "girl": "leifang", "name": "フレーズノエル(レイファン)", "zhs_name": "草莓圣诞(丽凤)", "zht_name": "草莓聖誕(麗鳳)", "en_name": "Noël aux Fraises (Leifang)", "kr_name": "프레이즈 노엘(레이팡)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": "2019/12/17 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_8", "girl": "nyotengu", "name": "フレーズノエル(女天狗)", "zhs_name": "草莓圣诞(女天狗)", "zht_name": "草莓聖誕(女天狗)", "en_name": "Noël aux Fraises (Nyotengu)", "kr_name": "프레이즈 노엘(뇨텐구)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": " 2019/11/19 2019/12/17 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_9", "girl": "honoka", "name": "フレーズノエル(ほのか)", "zhs_name": "草莓圣诞(穗香)", "zht_name": "草莓聖誕(穗香)", "en_name": "Noël aux Fraises (Honoka)", "kr_name": "프레이즈 노엘(호노카)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": "2019/12/17 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_10", "girl": "tamaki", "name": "フレーズノエル(たまき)", "zhs_name": "草莓圣诞(环)", "zht_name": "草莓聖誕(環)", "en_name": "Noël aux Fraises (Tamaki)", "kr_name": "프레이즈 노엘(타마키)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": "2019/12/17 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_11", "girl": "marie", "name": "フレーズノエル(マリー)", "zhs_name": "草莓圣诞(玛莉)", "zht_name": "草莓聖誕(瑪莉)", "en_name": "Noël aux Fraises (Marie)", "kr_name": "프레이즈 노엘(루나)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": "2019/12/17 2020/6/6 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_12", "girl": "kokoro", "name": "フレーズノエル(こころ)", "zhs_name": "草莓圣诞(心)", "zht_name": "草莓聖誕(心)", "en_name": "Noël aux Fraises (Kokoro)", "kr_name": "프레이즈 노엘(코코로)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": "2019/12/1 2019/12/17 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_13", "girl": "misaki", "name": "フレーズノエル(みさき)", "zhs_name": "草莓圣诞(海咲)", "zht_name": "草莓聖誕(海咲)", "en_name": "Noël aux Fraises (Misaki)", "kr_name": "프레이즈 노엘(미사키)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2018/12/13", "resell": "2019/12/17 2020/7/7 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "112", "girl": "nagisa", "name": "クリスタルスノー(なぎさ)", "zhs_name": "雪之水晶(凪咲)", "zht_name": "雪之水晶(凪咲)", "en_name": "Crystal Snow (Nagisa)", "kr_name": "크리스탈 스노우(나기사)", "type": "pow", "pow": "4522", "tec": "3954", "stm": "3724", "apl": "200", "skill1": "強烈スパイクB", "skill2": "灼熱のダンスD", "skill3": "秘められたパワー3", "sell": "2018/12/18", "resell": "2019/5/5 2020/5/5 2021/12/18 2022/12/18", "break": "1", "special_fun": ""
  },
  {
    "id": "113", "girl": "hitomi", "name": "おせちのあさり(ヒトミ)", "zhs_name": "晨曦之贝(瞳)", "zht_name": "晨曦之貝(瞳)", "en_name": "Dawn Set (Hitomi)", "kr_name": "아침색깔 조개잡이(히토미)", "type": "tec", "pow": "4114", "tec": "4862", "stm": "3666", "apl": "200", "skill1": "高度な心理戦B", "skill2": "フェアリーフェイント", "skill3": "可憐なフェイント", "sell": "2018/12/27", "resell": "2019/5/25 2020/5/25 2021/12/18", "break": "1", "special_fun": ""
  },
  {
    "id": "114", "girl": "tamaki", "name": "としこしのあさり(たまき)", "zhs_name": "深宵之贝(环)", "zht_name": "深宵之貝(環)", "en_name": "Dusk Set (Tamaki)", "kr_name": "자정 조개잡이(타마키)", "type": "tec", "pow": "4054", "tec": "5102", "stm": "3586", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "驚異のスタミナB", "skill3": "閃きのテクニック3", "sell": "2018/12/27", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "115", "girl": "nagisa", "name": "ラバー・ブラック(なぎさ)", "zhs_name": "黑胶(凪咲)", "zht_name": "黑膠(凪咲)", "en_name": "Rubber Black (Nagisa)", "kr_name": "러버 블랙(나기사)", "type": "tec", "pow": "4194", "tec": "4902", "stm": "3546", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "強烈なプレッシャーA", "skill3": "閃きのテクニック3", "sell": "2019/1/1", "resell": "2019/5/5 2020/5/5 2022/12/18", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "116", "girl": "nyotengu", "name": "常世華(女天狗)", "zhs_name": "常世华(女天狗)", "zht_name": "常世華(女天狗)", "en_name": "Eternal Flower (Nyotengu)", "kr_name": "불사화(뇨텐구)", "type": "tec", "pow": "4214", "tec": "4802", "stm": "3626", "apl": "200", "skill1": "高度な心理戦D", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2019/1/1", "resell": "2019/2/28 2019/12/26 2020/12/28 2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "117", "girl": "misaki", "name": "振袖・明星(みさき)", "zhs_name": "振袖・明星(海咲)", "zht_name": "振袖・明星(海咲)", "en_name": "Shining Star Kimono (Misaki)", "kr_name": "후리소데(샛별)(미사키)", "type": "stm", "pow": "4354", "tec": "3986", "stm": "4802", "apl": "200", "skill1": "強烈スパイクD", "skill2": "灼熱のダンスB", "skill3": "内から湧き上がるスタミナ3", "sell": "2019/1/1", "resell": "2019/2/28 2019/12/26 2020/12/28 2022/1/1 2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "118", "girl": "ayane", "name": "振袖・綾目蝶(あやね)", "zhs_name": "振袖・绫目蝶(绫音)", "zht_name": "振袖・綾目蝶(綾音)", "en_name": "Twill Butterfly Kimono (Ayane)", "kr_name": "후리소데(눈무늬나비)(아야네)", "type": "stm", "pow": "4084", "tec": "4106", "stm": "4952", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "灼熱のダンスC", "skill3": "内から湧き上がるスタミナ3", "sell": "2019/1/1", "resell": "2019/2/28 2019/12/26 2020/12/28 2022/1/1 2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "119", "girl": "momiji", "name": "巫女舞(紅葉)", "zhs_name": "巫女舞(红叶)", "zht_name": " 巫女舞(紅葉)", "en_name": "Shrine Maiden's Dance (Momiji)", "kr_name": "무녀의 춤(모미지)", "type": "pow", "pow": "4842", "tec": "4074", "stm": "3984", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "エンジェルスパイク", "skill3": "豪快なスパイク", "sell": "2019/1/4", "resell": "2019/9/20 2020/1/2 2020/9/20 2021/1/4 2022/1/6 2022/12/28", "break": "1", "special_fun": ""
  },
  {
    "id": "120", "girl": "luna", "name": "巫女舞(ルナ)", "zhs_name": "巫女舞(露娜)", "zht_name": "巫女舞(露娜)", "en_name": "Shrine Maiden's Dance (Luna)", "kr_name": "무녀의 춤(루나)", "type": "pow", "pow": "4902", "tec": "4194", "stm": "3904", "apl": "200", "skill1": "クリティカルヒットB", "skill2": "高度な心理戦B", "skill3": "秘められたパワー5", "sell": "2019/1/4", "resell": "2020/1/2 2021/1/4 2022/1/6 2022/12/28", "break": "1", "special_fun": ""
  },
  {
    "id": "121", "girl": "honoka", "name": "巫女舞(ほのか)", "zhs_name": "巫女舞(穗香)", "zht_name": "巫女舞(穗香)", "en_name": "Shrine Maiden's Dance (Honoka)", "kr_name": "무녀의 춤(호노카)", "type": "pow", "pow": "4942", "tec": "4084", "stm": "3974", "apl": "200", "skill1": "クリティカルヒットE", "skill2": "灼熱のダンスD", "skill3": "秘められたパワー5", "sell": "2019/1/4", "resell": "2020/1/2 2021/1/4 2022/1/6 2022/12/28", "break": "1", "special_fun": ""
  },
  {
    "id": "122", "girl": "ayane", "name": "シャドウイリス(あやね)", "zhs_name": "暗影菖蒲(绫音)", "zht_name": "暗影菖蒲(綾音)", "en_name": "Shadow Iris (Ayane)", "kr_name": "섀도우 아이리스(아야네)", "type": "tec", "pow": "4244", "tec": "4772", "stm": "3626", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2019/1/11", "resell": "2019/8/5 2019/11/29 2020/5/25 2020/8/5", "break": "1", "special_fun": ""
  },
  {
    "id": "123", "girl": "kasumi", "name": "ダークイリス(かすみ)", "zhs_name": "黑暗菖蒲(霞)", "zht_name": "黑暗菖蒲(霞)", "en_name": "Dark Iris (Kasumi)", "kr_name": "다크 아이리스(카스미)", "type": "tec", "pow": "4274", "tec": "4882", "stm": "3486", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "強烈スパイクF", "skill3": "閃きのテクニック3", "sell": "2019/1/11", "resell": "2019/11/29 2020/5/25", "break": "1", "special_fun": ""
  },
  {
    "id": "124", "girl": "fiona", "name": "ピュア・コンチェルト(フィオナ)", "zhs_name": "纯真协奏曲(菲欧娜)", "zht_name": "純真協奏曲(菲歐娜)", "en_name": "Pure Concerto (Fiona)", "kr_name": "퓨어 콘체르트(피오나)", "type": "tec", "pow": "4344", "tec": "4842", "stm": "3526", "apl": "230", "skill1": "裏の裏を突くフェイントD", "skill2": "灼熱のダンスC", "skill3": "閃きのテクニック4", "sell": "2019/1/18", "resell": "2019/9/19 2019/12/5", "break": "1", "special_fun": ""
  },
  {
    "id": "125", "girl": "helena", "name": "ディア・コンチェルト(エレナ)", "zhs_name": "挚爱协奏曲(海莲娜)", "zht_name": "摯愛協奏曲(海蓮娜)", "en_name": "Dear Concerto (Helena)", "kr_name": "디어 콘체르트(엘레나)", "type": "tec", "pow": "4274", "tec": "4882", "stm": "3486", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2019/1/18", "resell": "2019/9/19 2019/12/5", "break": "1", "special_fun": ""
  },
  {
    "id": "126", "girl": "nagisa", "name": "リリーベル(なぎさ)", "zhs_name": "与你同在(凪咲)", "zht_name": "與你同在(凪咲)", "en_name": "With You (Nagisa)", "kr_name": "위드유(나기사)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/1/24", "resell": "2019/5/5 2020/5/5 2022/12/18", "break": "1", "special_fun": ""
  },
  {
    "id": "127", "girl": "misaki", "name": "プラチナ・スターパーカー(みさき)", "zhs_name": "白金之星连帽衫(海咲)", "zht_name": "白金之星連帽衫(海咲)", "en_name": "Platinum Star Parka (Misaki)", "kr_name": "플래티넘 스타 파카(미사키)", "type": "stm", "pow": "4244", "tec": "4056", "stm": "4742", "apl": "200", "skill1": "高度な心理戦C", "skill2": "内から湧き上がるスタミナ5", "skill3": "可憐なフェイント", "sell": "2019/1/24", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "128", "girl": "hitomi", "name": "プラチナ・リーブラ(ヒトミ)", "zhs_name": "白金天枰座(瞳)", "zht_name": "白金天秤座(瞳)", "en_name": "Platinum Libra (Hitomi)", "kr_name": "플래티넘 리브라(히토미)", "type": "stm", "pow": "4214", "tec": "3886", "stm": "4942", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/1/24", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "129", "girl": "helena", "name": "ステラ・アクアリウス(エレナ)", "zhs_name": "星辰‧水瓶(海莲娜)", "zht_name": "星辰・水瓶(海蓮娜)", "en_name": "Stellar Aquarius (Helena)", "kr_name": "스텔라 아쿠아리우스(엘레나)", "type": "tec", "pow": "3814", "tec": "5322", "stm": "3806", "apl": "200", "skill1": "高度な心理戦B", "skill2": "アクアリウス・テクニック", "skill3": "可憐なフェイント", "sell": "2019/1/30", "resell": "2019/10/31 2020/2/11 2021/1/29 2021/9/16 2022/1/30 2022/9/8 2023/1/30", "break": "1", "special_fun": "较强力生日服装 可惜出的早没有粒子光效"
  },
  {
    "id": "130", "girl": "momiji", "name": "のりまき(紅葉)", "zhs_name": "寿司卷(红叶)", "zht_name": "壽司卷(紅葉)", "en_name": "Norimaki (Momiji)", "kr_name": "노리마키(모미지)", "type": "pow", "pow": "5122", "tec": "3974", "stm": "3904", "apl": "200", "skill1": "強烈スパイクE", "skill2": "高度な心理戦C", "skill3": "秘められたパワー5", "sell": "2019/1/31", "resell": "2019/9/20 2020/1/29 2020/9/20", "break": "0", "special_fun": ""
  },
  {
    "id": "131", "girl": "leifang", "name": "のりまき(レイファン)", "zhs_name": "寿司卷(丽凤)", "zht_name": "壽司卷(麗鳳)", "en_name": "Norimaki (Leifang)", "kr_name": "노리마키(레이팡)", "type": "pow", "pow": "4952", "tec": "3964", "stm": "3984", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2019/1/31", "resell": "2020/1/29", "break": "0", "special_fun": ""
  },
  {
    "id": "132_1", "girl": "kasumi", "name": "ダンまち・ヘスティアコスチューム(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_2", "girl": "honoka", "name": "ダンまち・ヘスティアコスチューム(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_3", "girl": "marie", "name": "ダンまち・ヘスティアコスチューム(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_4", "girl": "ayane", "name": "ダンまち・ヘスティアコスチューム(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_5", "girl": "nyotengu", "name": "ダンまち・ヘスティアコスチューム(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_6", "girl": "kokoro", "name": "ダンまち・ヘスティアコスチューム(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_7", "girl": "hitomi", "name": "ダンまち・ヘスティアコスチューム(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_8", "girl": "momiji", "name": "ダンまち・ヘスティアコスチューム(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_9", "girl": "helena", "name": "ダンまち・ヘスティアコスチューム(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_10", "girl": "misaki", "name": "ダンまち・ヘスティアコスチューム(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_11", "girl": "luna", "name": "ダンまち・ヘスティアコスチューム(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_12", "girl": "tamaki", "name": "ダンまち・ヘスティアコスチューム(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_13", "girl": "leifang", "name": "ダンまち・ヘスティアコスチューム(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "132_14", "girl": "fiona", "name": "ダンまち・ヘスティアコスチューム(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4144", "tec": "4842", "stm": "3626", "apl": "230", "skill1": "裏の裏を突くフェイントA", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2019/2/7", "resell": "", "break": "0", "special_fun": "劇場版 ダンジョンに出会いを求めるのは間違っているだろうか -オリオンの矢- 联动服装"
  },
  {
    "id": "133", "girl": "fiona", "name": "ステラ・アクアリウス(フィオナ)", "zhs_name": "星辰‧水瓶(菲欧娜)", "zht_name": "星辰・水瓶(菲歐娜)", "en_name": "Stellar Aquarius (Fiona)", "kr_name": "스텔라 아쿠아리우스(피오나)", "type": "tec", "pow": "3814", "tec": "5322", "stm": "3806", "apl": "200", "skill1": "高度な心理戦B", "skill2": "アクアリウス・テクニック", "skill3": "可憐なフェイント", "sell": "2019/2/11", "resell": "2019/10/31 2021/2/11 2021/9/16 2022/2/11 2022/9/8 2023/2/11", "break": "1", "special_fun": "较强力生日服装 可惜出的早没有粒子光效"
  },
  {
    "id": "134_1", "girl": "kasumi", "name": "メルティ・ハート(かすみ)", "zhs_name": "融化之心(霞)", "zht_name": "融化之心(霞)", "en_name": "Melty Heart (Kasumi)", "kr_name": "멜티 하트(카스미)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2020/2/20 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_2", "girl": "honoka", "name": "メルティ・ハート(ほのか)", "zhs_name": "融化之心(穗香)", "zht_name": "融化之心(穗香)", "en_name": "Melty Heart (Honoka)", "kr_name": "멜티 하트(호노카)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2020/2/20 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_3", "girl": "marie", "name": "メルティ・ハート(マリー)", "zhs_name": "融化之心(玛莉)", "zht_name": "融化之心(瑪莉)", "en_name": "Melty Heart (Marie)", "kr_name": "멜티 하트(루나)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2020/2/20 2020/6/6 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_4", "girl": "ayane", "name": "メルティ・ハート(あやね)", "zhs_name": "融化之心(绫音)", "zht_name": "融化之心(綾音)", "en_name": "Melty Heart (Ayane)", "kr_name": "멜티 하트(아야네)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2020/2/20 2020/8/5 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_5", "girl": "nyotengu", "name": "メルティ・ハート(女天狗)", "zhs_name": "融化之心(女天狗)", "zht_name": "融化之心(女天狗)", "en_name": "Melty Heart (Nyotengu)", "kr_name": "멜티 하트(뇨텐구)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2019/11/19 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_6", "girl": "kokoro", "name": "メルティ・ハート(こころ)", "zhs_name": "融化之心(心)", "zht_name": "融化之心(心)", "en_name": "Melty Heart (Kokoro)", "kr_name": "멜티 하트(코코로)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2019/12/1 2020/2/20 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_7", "girl": "hitomi", "name": "メルティ・ハート(ヒトミ)", "zhs_name": "融化之心(瞳)", "zht_name": "融化之心(瞳)", "en_name": "Melty Heart (Hitomi)", "kr_name": "멜티 하트(히토미)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2020/2/20 2020/5/25 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_8", "girl": "momiji", "name": "メルティ・ハート(紅葉)", "zhs_name": "融化之心(红叶)", "zht_name": "融化之心(紅葉)", "en_name": "Melty Heart (Momiji)", "kr_name": "멜티 하트(모미지)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2020/2/20 2020/9/20 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_9", "girl": "helena", "name": "メルティ・ハート(エレナ)", "zhs_name": "融化之心(海莲娜)", "zht_name": "融化之心(海蓮娜)", "en_name": "Melty Heart (Helena)", "kr_name": "멜티 하트(엘레나)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2020/1/30 2020/2/20 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_10", "girl": "misaki", "name": "メルティ・ハート(みさき)", "zhs_name": "融化之心(海咲)", "zht_name": "融化之心(海咲)", "en_name": "Melty Heart (Misaki)", "kr_name": "멜티 하트(미사키)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2020/2/20 2020/7/7 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_11", "girl": "luna", "name": "メルティ・ハート(ルナ)", "zhs_name": "融化之心(露娜)", "zht_name": "融化之心(露娜)", "en_name": "Melty Heart (Luna)", "kr_name": "멜티 하트(루나)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2020/2/20 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_12", "girl": "tamaki", "name": "メルティ・ハート(たまき)", "zhs_name": "融化之心(环)", "zht_name": "融化之心(環)", "en_name": "Melty Heart (Tamaki)", "kr_name": "멜티 하트(타마키)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2020/2/20 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_13", "girl": "leifang", "name": "メルティ・ハート(レイファン)", "zhs_name": "融化之心(丽凤)", "zht_name": "融化之心(麗鳳)", "en_name": "Melty Heart (Leifang)", "kr_name": "멜티 하트(레이팡)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2020/2/20 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "134_14", "girl": "fiona", "name": "メルティ・ハート(フィオナ)", "zhs_name": "融化之心(菲欧娜)", "zht_name": "融化之心(菲歐娜)", "en_name": "Melty Heart (Fiona)", "kr_name": "멜티 하트(피오나)", "type": "pow", "pow": "4882", "tec": "4084", "stm": "3884", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーE", "skill3": "とろけるほどのパワー", "sell": "2019/2/14", "resell": "2020/2/20 2021/2/10 2022/2/10", "break": "1", "special_fun": ""
  },
  {
    "id": "135", "girl": "fiona", "name": "けなげなキューピッド(フィオナ)", "zhs_name": "勇敢丘比特(菲欧娜)", "zht_name": "勇敢丘比特(菲歐娜)", "en_name": "Heroic Cupid (Fiona)", "kr_name": "기특한 큐피드(피오나)", "type": "apl", "pow": "4656", "tec": "3836", "stm": "3984", "apl": "600", "skill1": "強烈なプレッシャーB", "skill2": "隠しきれない魅力4", "skill3": "豪快なスパイク", "sell": "2019/2/21", "resell": "2022/5/13", "break": "1", "special_fun": ""
  },
  {
    "id": "136", "girl": "marie", "name": "いたずらキューピッド(マリー)", "zhs_name": "淘气丘比特(玛莉)", "zht_name": "淘氣丘比特(瑪莉)", "en_name": "Naughty Cupid (Marie)", "kr_name": "장난꾸러기 큐피드(마리)", "type": "apl", "pow": "4466", "tec": "3946", "stm": "4064", "apl": "600", "skill1": "灼熱のダンスD", "skill2": "観客総立ちE", "skill3": "隠しきれない魅力4", "sell": "2019/2/21", "resell": "2022/5/13", "break": "1", "special_fun": ""
  },
  {
    "id": "137", "girl": "kasumi", "name": "ステラ・ピスケス(かすみ)", "zhs_name": "星辰‧双鱼(霞)", "zht_name": "星辰・雙魚(霞)", "en_name": "Stellar Pisces (Kasumi)", "kr_name": "스텔라 피스케스(카스미)", "type": "tec", "pow": "3924", "tec": "5322", "stm": "3696", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "ピスケス・テクニック", "skill3": "可憐なフェイント", "sell": "2019/2/23", "resell": "2019/10/31 2020/2/23 2021/2/23 2021/9/16 2022/2/23 2022/9/8 2023/2/23", "break": "1", "special_fun": "强力生日服装 可惜出的早没有粒子光效"
  },
  {
    "id": "138", "girl": "kokoro", "name": "クロックワーク(こころ)", "zhs_name": "发条时钟(心)", "zht_name": "發條時鐘(心)", "en_name": "Clockwork (Kokoro)", "kr_name": "클록 워크(코코로)", "type": "tec", "pow": "4224", "tec": "4932", "stm": "3486", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2019/2/28", "resell": "2019/9/26 2022/10/13", "break": "1", "special_fun": ""
  },
  {
    "id": "139", "girl": "ayane", "name": "クロックワーク(あやね)", "zhs_name": "发条时钟(绫音)", "zht_name": "發條時鐘(綾音)", "en_name": "Clockwork (Ayane)", "kr_name": "클록 워크(아야네)", "type": "tec", "pow": "4284", "tec": "4902", "stm": "3556", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "強烈なプレッシャーA", "skill3": "閃きのテクニック6", "sell": "2019/2/28", "resell": "2019/9/26 2022/10/13", "break": "1", "special_fun": ""
  },
  {
    "id": "140", "girl": "tamaki", "name": "アバンチュール(たまき)", "zhs_name": "冒险(环)", "zht_name": "冒險(環)", "en_name": "Aventure (Tamaki)", "kr_name": "아방튀르(타마키)", "type": "pow", "pow": "4932", "tec": "3904", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2019/3/7", "resell": "2020/3/25 2021/4/15", "break": "1", "special_fun": ""
  },
  {
    "id": "141", "girl": "nyotengu", "name": "アバンチュール(女天狗)", "zhs_name": "冒险(女天狗)", "zht_name": "冒險(女天狗)", "en_name": "Aventure (Nyotengu)", "kr_name": "아방튀르(뇨텐구)", "type": "pow", "pow": "5132", "tec": "3864", "stm": "4004", "apl": "200", "skill1": "強烈スパイクB", "skill2": "驚異のスタミナD", "skill3": "秘められたパワー6", "sell": "2019/3/7", "resell": "2020/3/25 2021/4/15", "break": "1", "special_fun": ""
  },
  {
    "id": "142_1", "girl": "misaki", "name": "ウィズ・ユー(みさき)", "zhs_name": "与你同在(海咲)", "zht_name": "與你同在(海咲)", "en_name": "With You (Misaki)", "kr_name": "위드유(미사키)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2020/3/11 2020/7/7 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_2", "girl": "luna", "name": "ウィズ・ユー(ルナ)", "zhs_name": "与你同在(露娜)", "zht_name": "與你同在(露娜)", "en_name": "With You (Luna)", "kr_name": "위드유(루나)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2020/3/11 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_3", "girl": "marie", "name": "ウィズ・ユー(マリー)", "zhs_name": "与你同在(玛莉)", "zht_name": "與你同在(瑪莉)", "en_name": "With You (Marie)", "kr_name": "위드유(마리)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2020/3/11 2020/6/6 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_4", "girl": "honoka", "name": "ウィズ・ユー(ほのか)", "zhs_name": "与你同在(穗香)", "zht_name": "與你同在(穗香)", "en_name": "With You (Honoka)", "kr_name": "위드유(호노카)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2020/3/11 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_5", "girl": "kasumi", "name": "ウィズ・ユー(かすみ)", "zhs_name": "与你同在(霞)", "zht_name": "與你同在(霞)", "en_name": "With You (Kasumi)", "kr_name": "위드유(카스미)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2020/2/23 2020/3/11 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_6", "girl": "ayane", "name": "ウィズ・ユー(あやね)", "zhs_name": "与你同在(绫音)", "zht_name": "與你同在(綾音)", "en_name": "With You (Ayane)", "kr_name": "위드유(아야네)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2020/3/11 2020/8/5 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_7", "girl": "momiji", "name": "ウィズ・ユー(紅葉)", "zhs_name": "与你同在(红叶)", "zht_name": "與你同在(紅葉)", "en_name": "With You (Momiji)", "kr_name": "위드유(모미지)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2020/3/11 2020/9/20 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_8", "girl": "tamaki", "name": "ウィズ・ユー(たまき)", "zhs_name": "与你同在(环)", "zht_name": "與你同在(環)", "en_name": "With You (Tamaki)", "kr_name": "위드유(타마키)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2020/3/11 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_9", "girl": "kokoro", "name": "ウィズ・ユー(こころ)", "zhs_name": "与你同在(心)", "zht_name": "與你同在(心)", "en_name": "With You (Kokoro)", "kr_name": "위드유(코코로)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2019/12/1 2020/3/11 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_10", "girl": "hitomi", "name": "ウィズ・ユー(ヒトミ)", "zhs_name": "与你同在(瞳)", "zht_name": "與你同在(瞳)", "en_name": "With You (Hitomi)", "kr_name": "위드유(히토미)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2020/3/11 2020/5/25 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_11", "girl": "helena", "name": "ウィズ・ユー(エレナ)", "zhs_name": "与你同在(海莲娜)", "zht_name": "與你同在(海蓮娜)", "en_name": "With You (Helena)", "kr_name": "위드유(엘레나)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2020/1/30 2020/3/11 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_12", "girl": "leifang", "name": "ウィズ・ユー(レイファン)", "zhs_name": "与你同在(丽凤)", "zht_name": "與你同在(麗鳳)", "en_name": "With You (Leifang)", "kr_name": "위드유(레이팡)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2020/3/11 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_13", "girl": "fiona", "name": "ウィズ・ユー(フィオナ)", "zhs_name": "与你同在(菲欧娜)", "zht_name": "與你同在(菲歐娜)", "en_name": "WWith You (Fiona)", "kr_name": "위드유(피오나)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2020/3/11 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_14", "girl": "nyotengu", "name": "ウィズ・ユー(女天狗)", "zhs_name": "与你同在(女天狗)", "zht_name": "與你同在(女天狗)", "en_name": "With You (Nyotengu)", "kr_name": "위드유(뇨텐구)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2019/3/14", "resell": "2019/11/19 2020/3/11 2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "143", "girl": "misaki", "name": "禁断の水着♥星屑(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "4902", "tec": "3734", "stm": "4214", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "禁断の水着のパワー", "skill3": "豪快なスパイク", "sell": "2019/3/19", "resell": "", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)DEAD OR ALIVE Xtreme 3 Scarlet 特典(炒冷饭大师就是我脱裤魔 卡婊是什么？)"
  },
  {
    "id": "144", "girl": "luna", "name": "プリンセス・グレイス(ルナ)", "zhs_name": "优雅公主(露娜)", "zht_name": "優雅公主(露娜)", "en_name": "Princess Grace (Luna)", "kr_name": "프린세스 그레이스(루나)", "type": "pow", "pow": "5022", "tec": "3794", "stm": "4084", "apl": "200", "skill1": "強烈なプレッシャーA", "skill2": "内から湧き上がるスタミナ4", "skill3": "豪快なスパイク", "sell": "2019/3/20", "resell": "", "break": "1", "special_fun": "玛丽衣服砍掉半边裙边我看不出来？"
  },
  {
    "id": "145", "girl": "misaki", "name": "プリンセス・グレイス(みさき)", "zhs_name": "优雅公主(海咲)", "zht_name": "優雅公主(海咲)", "en_name": "Princess Grace (Misaki)", "kr_name": "프린세스 그레이스(미사키)", "type": "pow", "pow": "5112", "tec": "3884", "stm": "4004", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナB", "skill3": "秘められたパワー6", "sell": "2019/3/20", "resell": "", "break": "1", "special_fun": "玛丽衣服砍掉半边裙边我看不出来？"
  },
  {
    "id": "146", "girl": "fiona", "name": "プリンセス・グレイス(フィオナ)", "zhs_name": "优雅公主(菲欧娜)", "zht_name": "優雅公主(菲歐娜)", "en_name": "Princess Grace (Fiona)", "kr_name": "프린세스 그레이스(피오나)", "type": "pow", "pow": "5122", "tec": "3824", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "灼熱のダンスF", "skill3": "秘められたパワー5", "sell": "2019/3/20", "resell": "", "break": "1", "special_fun": "玛丽衣服砍掉半边裙边我看不出来？"
  },
  {
    "id": "147", "girl": "honoka", "name": "ステラ・アリエス(ほのか)", "zhs_name": "星辰‧白羊(穗香)", "zht_name": "星辰・白羊(穗香)", "en_name": "Stellar Aries (Honoka)", "kr_name": "스텔라 아리에스(호노카)", "type": "stm", "pow": "4044", "tec": "3976", "stm": "5322", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "アリエス・スタミナ", "skill3": "可憐なフェイント", "sell": "2019/3/24", "resell": "2019/10/31 2020/3/24 2021/3/24 2021/9/16 2022/3/24 2022/9/8 2023/3/24", "break": "1", "special_fun": "坑爹生日第二发 一堆废物技能"
  },
  {
    "id": "148", "girl": "fiona", "name": "おつまみピンチョス(フィオナ)", "zhs_name": "拽拽Pinchos(菲欧娜)", "zht_name": "拽拽Pinchos(菲歐娜)", "en_name": "Appetizer Pinchos (Fiona)", "kr_name": "애피타이저 핀초(피오나)", "type": "tec", "pow": "3974", "tec": "5142", "stm": "3626", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "驚異のスタミナB", "skill3": "閃きのテクニック6", "sell": "2019/3/27", "resell": "2019/10/9 2020/11/5 2021/3/25 2021/10/14", "break": "1", "special_fun": "第三件允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "149", "girl": "fiona", "name": "緋色レクイエム(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3994", "tec": "3796", "stm": "5252", "apl": "200", "skill1": "灼熱のダンスD", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2019/4/1", "resell": "2020/5/24", "break": "1", "special_fun": "可切换到红眼丧尸皮肤。满觉后手臂绷带消失。ZOMBIE LAND SAGA佐贺偶像是传奇 角色CV相同，官方蹭热度？联动？应该是蹭热度吧，不然衣服和活动为什么只持续1天"
  },
  {
    "id": "150", "girl": "marie", "name": "ルミナス・プリュム(マリー)", "zhs_name": "夜光羽翼(玛莉)", "zht_name": "夜光羽翼(瑪莉)", "en_name": "Luminous Plume (Marie)", "kr_name": "루미너스 플룸(마리)", "type": "stm", "pow": "3754", "tec": "4136", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "内から湧き上がるスタミナ6", "skill3": "可憐なフェイント", "sell": "2019/4/4", "resell": "", "break": "1", "special_fun": "使用天狗扇 扇动的时候 翅膀会出现粒子效果(光之舞)"
  },
  {
    "id": "151", "girl": "ayane", "name": "ルミナス・プリュム(あやね)", "zhs_name": "夜光羽翼(绫音)", "zht_name": "夜光羽翼(綾音)", "en_name": "Luminous Plume (Ayane)", "kr_name": "루미너스 플룸(아야네)", "type": "tec", "pow": "3844", "tec": "5032", "stm": "3866", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "驚異のスタミナB", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/4/4", "resell": "", "break": "1", "special_fun": "使用天狗扇 扇动的时候 翅膀会出现粒子效果(光之舞)"
  },
  {
    "id": "152", "girl": "kanna", "name": "百鬼夜行(カンナ)", "zhs_name": "百鬼夜行(神无)", "zht_name": "百鬼夜行(神無)", "en_name": "Pandemonium (Kanna)", "kr_name": "백귀야행(칸나)", "type": "pow", "pow": "5212", "tec": "3694", "stm": "4094", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "灼熱のダンスE", "skill3": "秘められたパワー3", "sell": "2019/4/11", "resell": "2019/9/15 2020/9/15 2022/4/11 2023/4/11", "break": "1", "special_fun": ""
  },
  {
    "id": "153", "girl": "nyotengu", "name": "アナトリア(女天狗)", "zhs_name": "安纳托利亚(女天狗)", "zht_name": "安納托利亞(女天狗)", "en_name": "Anatolia (Nyotengu)", "kr_name": "아나톨리아(뇨텐구)", "type": "pow", "pow": "5012", "tec": "3734", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "内から湧き上がるスタミナ5", "skill3": "豪快なスパイク", "sell": "2019/4/11", "resell": "", "break": "0", "special_fun": ""
  },
  {
    "id": "154", "girl": "momiji", "name": "パラレルライン(紅葉)", "zhs_name": "平行线(红叶)", "zht_name": "平行線(紅葉)", "en_name": "Parallel Lines (Momiji)", "kr_name": "패럴렐 라인(모미지)", "type": "pow", "pow": "5152", "tec": "3844", "stm": "4004", "apl": "200", "skill1": "強烈スパイクB", "skill2": "驚異のスタミナB", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/4/11", "resell": "", "break": "0", "special_fun": ""
  },
  {
    "id": "155", "girl": "nagisa", "name": "春彩のスクールウェア(なぎさ)", "zhs_name": "春色校服(凪咲)", "zht_name": "春色校服(凪咲)", "en_name": "Springtime Schoolwear (Nagisa)", "kr_name": "화사한 봄철 학생복(나기사)", "type": "tec", "pow": "4114", "tec": "4982", "stm": "3646", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦D", "skill3": "閃きのテクニック4", "sell": "2019/4/18", "resell": "2020/4/14 2020/1/22 2020/10/15 2021/4/8 2021/8/20 2022/4/21 2023/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "156", "girl": "misaki", "name": "春彩のスクールウェア(みさき)", "zhs_name": "春色校服(海咲)", "zht_name": "春色校服(海咲)", "en_name": "Springtime Schoolwear (Misaki)", "kr_name": "화사한 봄철 학생복(미사키)", "type": "tec", "pow": "4174", "tec": "4862", "stm": "3606", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック5", "skill3": "可憐なフェイント", "sell": "2019/4/18", "resell": "2020/4/14 2020/1/22 2020/10/15 2021/4/8 2021/8/20 2022/4/21 2023/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "157", "girl": "leifang", "name": "ステラ・タウルス(レイファン)", "zhs_name": "星辰‧金牛(丽凤)", "zht_name": "星辰・金牛(麗鳳)", "en_name": "Stellar Taurus (Leifang)", "kr_name": "스텔라 타우루스(레이팡)", "type": "pow", "pow": "5322", "tec": "3734", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "タウルス・パワー", "skill3": "豪快なスパイク", "sell": "2019/4/23", "resell": "2019/10/31 2020/4/23 2021/9/16 2022/4/23 2022/9/8 2023/4/23", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现粒子效果(光之舞)后妈角色日常生日坑爹"
  },
  {
    "id": "158", "girl": "kanna", "name": "疾風迅雷(カンナ)", "zhs_name": "疾风迅雷(神无)", "zht_name": "疾風迅雷(神無)", "en_name": "Lightning Speed (Kanna)", "kr_name": "질풍신뢰(칸나)", "type": "stm", "pow": "4324", "tec": "3536", "stm": "5232", "apl": "200", "skill1": "強烈スパイクF", "skill2": "灼熱のダンスB", "skill3": "内から湧き上がるスタミナ3", "sell": "2019/4/25", "resell": "2019/9/15 2020/9/15 2022/4/11 2023/4/11", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "159", "girl": "honoka", "name": "ハッピーエッグ(ほのか)", "zhs_name": "快乐彩蛋(穗香)", "zht_name": "快樂彩蛋(穗香)", "en_name": "Happy Egg (Honoka)", "kr_name": "해피 에그(호노카)", "type": "tec", "pow": "4214", "tec": "4872", "stm": "3556", "apl": "200", "skill1": "高度な心理戦A", "skill2": "閃きのテクニック5", "skill3": "豪快なスパイク", "sell": "2019/4/25", "resell": "2020/4/21", "break": "1", "special_fun": ""
  },
  {
    "id": "160", "girl": "luna", "name": "ハッピーエッグ(ルナ)", "zhs_name": "快乐彩蛋(露娜)", "zht_name": "快樂彩蛋(露娜)", "en_name": "Happy Egg (Luna)", "kr_name": "해피 에그(루나)", "type": "tec", "pow": "4044", "tec": "5002", "stm": "3696", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦A", "skill3": "閃きのテクニック5", "sell": "2019/4/25", "resell": "2020/4/21", "break": "1", "special_fun": ""
  },
  {
    "id": "161", "girl": "leifang", "name": "幻燈朱雀(レイファン)", "zhs_name": "幻灯朱雀(丽凤)", "zht_name": "幻燈朱雀(麗鳳)", "en_name": "Vermilion Bird Mirage (Leifang)", "kr_name": "환등주작(레이팡)", "type": "stm", "pow": "4514", "tec": "3606", "stm": "4922", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/5/2", "resell": "2019/10/24", "break": "1", "special_fun": ""
  },
  {
    "id": "162", "girl": "tamaki", "name": "幻燈黒竜(たまき)", "zhs_name": "幻灯黑龙(环)", "zht_name": "幻燈黑龍(環)", "en_name": "Black Dragon Mirage (Tamaki)", "kr_name": "환등흑룡(타마키)", "type": "pow", "pow": "5152", "tec": "3734", "stm": "4114", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーD", "skill3": "秘められたパワー6", "sell": "2019/5/2", "resell": "2019/10/24", "break": "1", "special_fun": ""
  },
  {
    "id": "163", "girl": "nagisa", "name": "ステラ・タウルス(なぎさ)", "zhs_name": "星辰‧金牛(凪咲)", "zht_name": "星辰・金牛(凪咲)", "en_name": "Stellar Taurus (Nagisa)", "kr_name": "스텔라 타우루스(나기사)", "type": "pow", "pow": "5322", "tec": "3734", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "タウルス・パワー", "skill3": "豪快なスパイク", "sell": "2019/5/5", "resell": "2019/10/31 2020/5/5 2021/5/5 2021/9/16 2022/5/5 2022/9/8 2023/5/5", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现粒子效果(光之舞)强力生日衣服"
  },
  {
    "id": "164", "girl": "kanna", "name": "ハニーカラメルキャンディー(カンナ)", "zhs_name": "蜂蜜焦糖(神无)", "zht_name": "蜂蜜焦糖(神無)", "en_name": "Honey Caramel Candy (Kanna)", "kr_name": "허니 캐러멜 캔디(칸나)", "type": "stm", "pow": "4274", "tec": "3566", "stm": "5202", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2019/5/9", "resell": "2019/9/15 2020/9/15 2022/4/11 2023/4/11", "break": "1", "special_fun": ""
  },
  {
    "id": "165", "girl": "fiona", "name": "コットンキャンディー(フィオナ)", "zhs_name": "棉花糖(菲欧娜)", "zht_name": "棉花糖(菲歐娜)", "en_name": "Cotton Candy (Fiona)", "kr_name": "코튼 캔디(피오나)", "type": "stm", "pow": "4354", "tec": "3416", "stm": "5272", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2019/5/9", "resell": "2019/9/12", "break": "1", "special_fun": ""
  },
  {
    "id": "166", "girl": "marie", "name": "コットンキャンディー(マリー)", "zhs_name": "棉花糖(玛莉)", "zht_name": "棉花糖(瑪莉)", "en_name": "Cotton Candy (Marie)", "kr_name": "코튼 캔디(마리)", "type": "stm", "pow": "4504", "tec": "3456", "stm": "5132", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナB", "skill3": "内から湧き上がるスタミナ5", "sell": "2019/5/9", "resell": "2019/9/12", "break": "1", "special_fun": ""
  },
  {
    "id": "167", "girl": "nagisa", "name": "シルバーソーン・リーフ(なぎさ)", "zhs_name": "银刺绿叶(凪咲)", "zht_name": "銀刺綠葉(凪咲)", "en_name": "Silverthorn Leaf (Nagisa)", "kr_name": "실버손 리프(나기사)", "type": "stm", "pow": "3754", "tec": "4056", "stm": "5232", "apl": "200", "skill1": "高度な心理戦C", "skill2": "内から湧き上がるスタミナ4", "skill3": "可憐なフェイント", "sell": "2019/5/16", "resell": "", "break": "0", "special_fun": ""
  },
  {
    "id": "168", "girl": "helena", "name": "ロイヤル・リーフ(エレナ)", "zhs_name": "皇家绿叶(海莲娜)", "zht_name": "皇家綠葉(海蓮娜)", "en_name": "Royal Leaf (Helena)", "kr_name": "로얄 리프(엘레나)", "type": "stm", "pow": "3684", "tec": "4216", "stm": "5192", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "驚異のスタミナB", "skill3": "内から湧き上がるスタミナ5", "sell": "2019/5/16", "resell": "", "break": "0", "special_fun": ""
  },
  {
    "id": "169", "girl": "honoka", "name": "ゆるふわパーカー(ほのか)", "zhs_name": "轻柔连帽衫(穗香)", "zht_name": "輕柔連帽衫(穗香)", "en_name": "Soft 'n Fluffy Parka (Honoka)", "kr_name": "부드러운 파카(호노카)", "type": "pow", "pow": "5032", "tec": "3684", "stm": "4184", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2019/5/23", "resell": "2020/6/14 2022/4/5 2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "170", "girl": "kokoro", "name": "ゆるふわパーカー(こころ)", "zhs_name": "轻柔连帽衫(心)", "zht_name": "輕柔連帽衫(心)", "en_name": "Soft 'n Fluffy Parka (Kokoro)", "kr_name": "부드러운 파카(코코로)", "type": "pow", "pow": "5202", "tec": "3714", "stm": "4084", "apl": "200", "skill1": "強烈スパイクC", "skill2": "高度な心理戦A", "skill3": "秘められたパワー6", "sell": "2019/5/23", "resell": "2020/6/14 2022/4/5 2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "171", "girl": "misaki", "name": "ゆるふわパーカー(みさき)", "zhs_name": "轻柔连帽衫(海咲)", "zht_name": "輕柔連帽衫(海咲)", "en_name": "Soft 'n Fluffy Parka (Misaki)", "kr_name": "부드러운 파카(미사키)", "type": "pow", "pow": "5202", "tec": "3714", "stm": "4084", "apl": "200", "skill1": "強烈スパイクC", "skill2": "高度な心理戦A", "skill3": "秘められたパワー6", "sell": "2019/5/23", "resell": "2020/6/14 2022/4/5 2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "172", "girl": "momiji", "name": "ゆるふわパーカー(紅葉)", "zhs_name": "轻柔连帽衫(红叶)", "zht_name": "輕柔連帽衫(紅葉)", "en_name": "Soft 'n Fluffy Parka (Momiji)", "kr_name": "부드러운 파카(모미지)", "type": "pow", "pow": "5202", "tec": "3714", "stm": "4084", "apl": "200", "skill1": "強烈スパイクC", "skill2": "高度な心理戦A", "skill3": "秘められたパワー6", "sell": "2019/5/23", "resell": "2020/6/14 2022/4/5 2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "173", "girl": "hitomi", "name": "ステラ・ジェミニ(ヒトミ)", "zhs_name": "星辰‧双子(瞳)", "zht_name": "星辰・雙子(瞳)", "en_name": "Stellar Gemini (Hitomi)", "kr_name": "스텔라 제미니(히토미)", "type": "stm", "pow": "4254", "tec": "3766", "stm": "5322", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "ジェミニ・スタミナ", "skill3": "豪快なスパイク", "sell": "2019/5/25", "resell": "2019/10/31 2020/5/25 2021/5/25 2021/9/16 2022/5/25 2022/9/8 2023/5/25", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现粒子效果(光之舞)后妈角色日常坑爹 比honoka生日好一点"
  },
  {
    "id": "174_1", "girl": "kasumi", "name": "ハーフセイル(かすみ)", "zhs_name": "半帆(霞)", "zht_name": "半帆(霞)", "en_name": "Half Sail (Kasumi)", "kr_name": "절반의 돛(카스미)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/2/23 2020/3/17 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_2", "girl": "honoka", "name": "ハーフセイル(ほのか)", "zhs_name": "半帆(穗香)", "zht_name": "半帆(穗香)", "en_name": "Half Sail (Honoka)", "kr_name": "절반의 돛(호노카)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/3/17 2020/3/24 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_3", "girl": "marie", "name": "ハーフセイル(マリー)", "zhs_name": "半帆(玛莉)", "zht_name": "半帆(瑪莉)", "en_name": "Half Sail (Marie)", "kr_name": "절반의 돛(루나)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/3/17 2020/6/6 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_4", "girl": "ayane", "name": "ハーフセイル(あやね)", "zhs_name": "半帆(绫音)", "zht_name": "半帆(綾音)", "en_name": "Half Sail (Ayane)", "kr_name": "절반의 돛(아야네)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/3/17 2020/8/5 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_5", "girl": "nyotengu", "name": "ハーフセイル(女天狗)", "zhs_name": "半帆(女天狗)", "zht_name": "半帆(女天狗)", "en_name": "Half Sail (Nyotengu)", "kr_name": "절반의 돛(뇨텐구)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2019/11/19 2020/3/17 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_6", "girl": "kokoro", "name": "ハーフセイル(こころ)", "zhs_name": "半帆(心)", "zht_name": "半帆(心)", "en_name": "Half Sail (Kokoro)", "kr_name": "절반의 돛(코코로)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2019/12/1 2020/3/17 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_7", "girl": "hitomi", "name": "ハーフセイル(ヒトミ)", "zhs_name": "半帆(瞳)", "zht_name": "半帆(瞳)", "en_name": "Half Sail (Hitomi)", "kr_name": "절반의 돛(히토미)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/3/17 2020/5/25 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_8", "girl": "momiji", "name": "ハーフセイル(紅葉)", "zhs_name": "半帆(红叶)", "zht_name": "半帆(紅葉)", "en_name": "Half Sail (Momiji)", "kr_name": "절반의 돛(모미지)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/3/17 2020/9/20 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_9", "girl": "helena", "name": "ハーフセイル(エレナ)", "zhs_name": "半帆(海莲娜)", "zht_name": "半帆(海蓮娜)", "en_name": "Half Sail (Helena)", "kr_name": "절반의 돛(엘레나)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/1/30 2020/3/17 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_10", "girl": "misaki", "name": "ハーフセイル(みさき)", "zhs_name": "半帆(海咲)", "zht_name": "半帆(海咲)", "en_name": "Half Sail (Misaki)", "kr_name": "절반의 돛(미사키)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/3/17 2020/7/7 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_11", "girl": "luna", "name": "ハーフセイル(ルナ)", "zhs_name": "半帆(露娜)", "zht_name": "半帆(露娜)", "en_name": "Half Sail (Luna)", "kr_name": "절반의 돛(루나)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/3/17 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_12", "girl": "tamaki", "name": "ハーフセイル(たまき)", "zhs_name": "半帆(环)", "zht_name": "半帆(環)", "en_name": "Half Sail (Tamaki)", "kr_name": "절반의 돛(타마키)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/3/17 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_13", "girl": "leifang", "name": "ハーフセイル(レイファン)", "zhs_name": "半帆(丽凤)", "zht_name": "半帆(麗鳳)", "en_name": "Half Sail (Leifang)", "kr_name": "절반의 돛(레이팡)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/3/17 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_14", "girl": "fiona", "name": "ハーフセイル(フィオナ)", "zhs_name": "半帆(菲欧娜)", "zht_name": "半帆(菲歐娜)", "en_name": "Half Sail (Fiona)", "kr_name": "절반의 돛(피오나)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/3/17 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "174_15", "girl": "nagisa", "name": "ハーフセイル(なぎさ)", "zhs_name": "半帆(凪咲)", "zht_name": "半帆(凪咲)", "en_name": "Half Sail (Nagisa)", "kr_name": "절반의 돛(나기사)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2019/5/30", "resell": "2020/3/17 2021/3/4", "break": "1", "special_fun": ""
  },
  {
    "id": "175", "girl": "marie", "name": "ステラ・ジェミニ(マリー)", "zhs_name": "星辰‧双子(玛莉)", "zht_name": "星辰・雙子(瑪莉)", "en_name": "Stellar Gemini (Marie)", "kr_name": "스텔라 제미니(마리)", "type": "stm", "pow": "4254", "tec": "3766", "stm": "5322", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "ジェミニ・スタミナ", "skill3": "豪快なスパイク", "sell": "2019/6/6", "resell": "2019/10/31 2020/6/6 2021/6/6 2021/9/16 2022/6/6 2022/9/8", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现粒子效果(光之舞)你说老娘一个人气角色，是KT策划脑子有问题？有钱不赚，怎么就得了这么一件垃圾生日衣服？"
  },
  {
    "id": "176", "girl": "nagisa", "name": "ふりふりワンちゃん(なぎさ)", "zhs_name": "摇尾小狗(凪咲)", "zht_name": "搖尾小狗(凪咲)", "en_name": "Furry Doggy (Nagisa)", "kr_name": "흔들흔들 강아지(나기사)", "type": "apl", "pow": "3836", "tec": "4646", "stm": "4044", "apl": "550", "skill1": "裏の裏を突くフェイントA", "skill2": "観客総立ちE", "skill3": "隠しきれない魅力4", "sell": "2019/6/7", "resell": "2020/1/9 2021/4/1", "break": "1", "special_fun": "增加“毛皮表现”效果，摸头会摇尾巴"
  },
  {
    "id": "177", "girl": "hitomi", "name": "もふもふクマちゃん(ヒトミ)", "zhs_name": "毛绒小熊(瞳)", "zht_name": "毛絨小熊(瞳)", "en_name": "Fluffy Bear (Hitomi)", "kr_name": "폭신폭신 아기곰(히토미)", "type": "apl", "pow": "3916", "tec": "4526", "stm": "3984", "apl": "550", "skill1": "高度な心理戦D", "skill2": "隠しきれない魅力5", "skill3": "可憐なフェイント", "sell": "2019/6/7", "resell": "2020/1/9 2021/4/1", "break": "0", "special_fun": "增加“毛皮表现”效果，摸头会摆小熊的姿势。但是和なぎさ不一样，后妈角色不配有爆衣效果"
  },
  {
    "id": "178_1", "girl": "kasumi", "name": "ふわもこフォーム(かすみ)", "zhs_name": "蓬松泡沫(霞)", "zht_name": "蓬鬆泡沫(霞)", "en_name": "Bubbly Foam (Kasumi)", "kr_name": "부드러운 거품(카스미)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/2/23 2020/3/25 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_2", "girl": "honoka", "name": "ふわもこフォーム(ほのか)", "zhs_name": "蓬松泡沫(穗香)", "zht_name": "蓬鬆泡沫(穗香)", "en_name": "Bubbly Foam (Honoka)", "kr_name": "부드러운 거품(호노카)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/3/25 2020/8/22 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_3", "girl": "marie", "name": "ふわもこフォーム(マリー)", "zhs_name": "蓬松泡沫(玛莉)", "zht_name": "蓬鬆泡沫(瑪莉)", "en_name": "Bubbly Foam (Marie)", "kr_name": "부드러운 거품(루나)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/3/25 2020/6/6 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_4", "girl": "ayane", "name": "ふわもこフォーム(あやね)", "zhs_name": "蓬松泡沫(绫音)", "zht_name": "蓬鬆泡沫(綾音)", "en_name": "Bubbly Foam (Ayane)", "kr_name": "부드러운 거품(아야네)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/3/25 2020/8/5 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_5", "girl": "nyotengu", "name": "ふわもこフォーム(女天狗)", "zhs_name": "蓬松泡沫(女天狗)", "zht_name": "蓬鬆泡沫(女天狗)", "en_name": "Bubbly Foam (Nyotengu)", "kr_name": "부드러운 거품(뇨텐구)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2019/11/19 2020/3/25 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_6", "girl": "kokoro", "name": "ふわもこフォーム(こころ)", "zhs_name": "蓬松泡沫(心)", "zht_name": "蓬鬆泡沫(心)", "en_name": "Bubbly Foam (Kokoro)", "kr_name": "부드러운 거품(코코로)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2019/12/1 2020/3/25 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_7", "girl": "hitomi", "name": "ふわもこフォーム(ヒトミ)", "zhs_name": "蓬松泡沫(瞳)", "zht_name": "蓬鬆泡沫(瞳)", "en_name": "Bubbly Foam (Hitomi)", "kr_name": "부드러운 거품(히토미)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/3/25 2020/5/25 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_8", "girl": "momiji", "name": "ふわもこフォーム(紅葉)", "zhs_name": "蓬松泡沫(红叶)", "zht_name": "蓬鬆泡沫(紅葉)", "en_name": "Bubbly Foam (Momiji)", "kr_name": "부드러운 거품(모미지)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/3/25 2020/9/20 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_9", "girl": "helena", "name": "ふわもこフォーム(エレナ)", "zhs_name": "蓬松泡沫(海莲娜)", "zht_name": "蓬鬆泡沫(海蓮娜)", "en_name": "Bubbly Foam (Helena)", "kr_name": "부드러운 거품(엘레나)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/1/30 2020/3/25 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_10", "girl": "misaki", "name": "ふわもこフォーム(みさき)", "zhs_name": "蓬松泡沫(海咲)", "zht_name": "蓬鬆泡沫(海咲)", "en_name": "Bubbly Foam (Misaki)", "kr_name": "부드러운 거품(미사키)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/3/25 2020/7/7 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_11", "girl": "luna", "name": "ふわもこフォーム(ルナ)", "zhs_name": "蓬松泡沫(露娜)", "zht_name": "蓬鬆泡沫(露娜)", "en_name": "Bubbly Foam (Luna)", "kr_name": "부드러운 거품(루나)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/3/25 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_12", "girl": "tamaki", "name": "ふわもこフォーム(たまき)", "zhs_name": "蓬松泡沫(环)", "zht_name": "蓬鬆泡沫(環)", "en_name": "Bubbly Foam (Tamaki)", "kr_name": "부드러운 거품(타마키)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/3/25 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_13", "girl": "leifang", "name": "ふわもこフォーム(レイファン)", "zhs_name": "蓬松泡沫(丽凤)", "zht_name": "蓬鬆泡沫(麗鳳)", "en_name": "Bubbly Foam (Leifang)", "kr_name": "부드러운 거품(레이팡)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/3/25 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_14", "girl": "fiona", "name": "ふわもこフォーム(フィオナ)", "zhs_name": "蓬松泡沫(菲欧娜)", "zht_name": "蓬鬆泡沫(菲歐娜)", "en_name": "Bubbly Foam (Fiona)", "kr_name": "부드러운 거품(피오나)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/3/25 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_15", "girl": "nagisa", "name": "ふわもこフォーム(なぎさ)", "zhs_name": "蓬松泡沫(凪咲)", "zht_name": "蓬鬆泡沫(凪咲)", "en_name": "Bubbly Foam (Nagisa)", "kr_name": "부드러운 거품 (나기사)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2019/6/14", "resell": "2019/10/31 2020/3/25 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "179", "girl": "kasumi", "name": "ミスティック・オーシャン(かすみ)", "zhs_name": "神秘海洋(霞)", "zht_name": "神秘海洋(霞)", "en_name": "Mystical Ocean (Kasumi)", "kr_name": "미스틱 오션(카스미)", "type": "stm", "pow": "4514", "tec": "3686", "stm": "4842", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2019/6/20", "resell": "2020/6/4", "break": "1", "special_fun": ""
  },
  {
    "id": "180", "girl": "luna", "name": "ミスティック・フォレスト(ルナ)", "zhs_name": "神秘森林(露娜)", "zht_name": "神秘森林(露娜)", "en_name": "Mystical Forest (Luna)", "kr_name": "미스틱 포레스트(루나)", "type": "pow", "pow": "5202", "tec": "3714", "stm": "3984", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "プラチナアタッカー", "skill3": "豪快なスパイク", "sell": "2019/6/20", "resell": "2020/6/4", "break": "1", "special_fun": ""
  },
  {
    "id": "181", "girl": "tamaki", "name": "おつまみシュリンプ(たまき)", "zhs_name": "拽拽衬衫(环)", "zht_name": "拽拽襯衫(環)", "en_name": "Appetizer Shrimp (Tamaki)", "kr_name": "에피타이저 쉬림프(타마키)", "type": "tec", "pow": "4114", "tec": "5042", "stm": "3586", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "驚異のスタミナE", "skill3": "閃きのテクニック6", "sell": "2019/6/26", "resell": "2020/6/17", "break": "1", "special_fun": "第二波可拉扯交互的衣服、允许多部分拉扯"
  },
  {
    "id": "182", "girl": "misaki", "name": "おつまみシュリンプ(みさき)", "zhs_name": "拽拽衬衫(海咲)", "zht_name": "拽拽襯衫(海咲)", "en_name": "Appetizer Shrimp (Misaki)", "kr_name": "에피타이저 쉬림프(미사키)", "type": "tec", "pow": "4114", "tec": "5042", "stm": "3586", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "驚異のスタミナE", "skill3": "閃きのテクニック6", "sell": "2019/6/26", "resell": "2019/7/7 2020/6/17 2020/7/7", "break": "1", "special_fun": "第二波可拉扯交互的衣服、允许多部分拉扯"
  },
  {
    "id": "183", "girl": "nagisa", "name": "ワイルドウインド(なぎさ)", "zhs_name": "狂风(凪咲)", "zht_name": "狂風(凪咲)", "en_name": "Wild Wind (Nagisa)", "kr_name": "와일드 윈드(나기사)", "type": "pow", "pow": "5222", "tec": "3804", "stm": "3974", "apl": "200", "skill1": "強烈スパイクE", "skill2": "驚異のスタミナF", "skill3": "秘められたパワー4", "sell": "2019/7/4", "resell": "2020/5/23", "break": "1", "special_fun": ""
  },
  {
    "id": "184", "girl": "tamaki", "name": "ワイルドウインド(たまき)", "zhs_name": "狂风(环)", "zht_name": "狂風(環)", "en_name": "Wild Wind (Tamaki)", "kr_name": "와일드 윈드(타마키)", "type": "pow", "pow": "5132", "tec": "3854", "stm": "3914", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "豪快なスパイク", "sell": "2019/7/4", "resell": "2020/5/23", "break": "1", "special_fun": ""
  },
  {
    "id": "185", "girl": "misaki", "name": "ステラ・カンケル(みさき)", "zhs_name": "星辰・巨蟹(海咲)", "zht_name": "星辰・巨蟹(海咲)", "en_name": "Stellar Cancer (Misaki)", "kr_name": "스텔라 캔서(미사키)", "type": "pow", "pow": "5322", "tec": "3784", "stm": "4094", "apl": "200", "skill1": "強烈スパイクB", "skill2": "カンケル・パワー", "skill3": "豪快なスパイク", "sell": "2019/7/7", "resell": "2019/10/31 2020/7/7 2021/9/16 2022/7/7 2022/9/8 2023/7/7", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现红色粒子效果(光之舞)老娘第一亲女儿 看到了吗 强力的生日衣服"
  },
  {
    "id": "186", "girl": "marie", "name": "ほしぞらきんぎょ(マリー)", "zhs_name": "星空金鱼(玛莉)", "zht_name": "星空金魚(瑪莉)", "en_name": "Starry Night Goldfish (Marie)", "kr_name": "금붕어(별하늘)(마리)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "高度な心理戦B", "skill2": "閃きのテクニック6", "skill3": "可憐なフェイント", "sell": "2019/7/11", "resell": "2020/5/28 2022/8/18 2023/4/13", "break": "1", "special_fun": ""
  },
  {
    "id": "187", "girl": "kokoro", "name": "おまつりきんぎょ(こころ)", "zhs_name": "祭典金鱼(心)", "zht_name": "祭典金魚(心)", "en_name": "Festival Goldfish (Kokoro)", "kr_name": "금붕어(축제)(코코로)", "type": "stm", "pow": "3964", "tec": "4256", "stm": "4822", "apl": "200", "skill1": "灼熱のダンスA", "skill2": "高度な心理戦F", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/7/11", "resell": "2020/5/28 2022/8/18 2023/4/13", "break": "1", "special_fun": ""
  },
  {
    "id": "188", "girl": "leifang", "name": "おまつりきんぎょ(レイファン)", "zhs_name": "祭典金鱼(丽凤)", "zht_name": "祭典金魚(麗鳳)", "en_name": "Festival Goldfish (Leifang)", "kr_name": "금붕어(축제)(레이팡)", "type": "stm", "pow": "3964", "tec": "4256", "stm": "4822", "apl": "200", "skill1": "灼熱のダンスA", "skill2": "高度な心理戦F", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/7/11", "resell": "2020/5/28 2022/8/18 2023/4/13", "break": "1", "special_fun": ""
  },
  {
    "id": "189", "girl": "fiona", "name": "おまつりきんぎょ(フィオナ)", "zhs_name": "祭典金鱼(菲欧娜)", "zht_name": "祭典金魚(菲歐娜)", "en_name": "Festival Goldfish (Fiona)", "kr_name": "금붕어(축제)(피오나)", "type": "stm", "pow": "3964", "tec": "4256", "stm": "4822", "apl": "200", "skill1": "灼熱のダンスA", "skill2": "高度な心理戦F", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/7/11", "resell": "2020/5/28 2022/8/18 2023/4/13", "break": "1", "special_fun": ""
  },
  {
    "id": "190", "girl": "honoka", "name": "半蔵忍装束(ほのか)", "zhs_name": "半藏忍装束(穗香)", "zht_name": "半藏忍裝束(穗香)", "en_name": "Hanzō Ninja Suit (Honoka)", "kr_name": "한조 닌자복(호노카)", "type": "pow", "pow": "5212", "tec": "3894", "stm": "3894", "apl": "200", "skill1": "強烈スパイクC", "skill2": "強烈なプレッシャーD", "skill3": "半蔵のパワー", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "191", "girl": "kasumi", "name": "半蔵忍装束(かすみ)", "zhs_name": "半藏忍装束(霞)", "zht_name": "半藏忍裝束(霞)", "en_name": "Hanzō Ninja Suit (Kasumi)", "kr_name": "한조 닌자복(카스미)", "type": "pow", "pow": "5212", "tec": "3894", "stm": "3894", "apl": "200", "skill1": "強烈スパイクC", "skill2": "強烈なプレッシャーD", "skill3": "半蔵のパワー", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "192", "girl": "ayane", "name": "半蔵忍装束(あやね)", "zhs_name": "半藏忍装束(绫音)", "zht_name": "半藏忍裝束(綾音)", "en_name": "Hanzō Ninja Suit (Ayane)", "kr_name": "한조 닌자복(아야네)", "type": "pow", "pow": "5212", "tec": "3894", "stm": "3894", "apl": "200", "skill1": "強烈スパイクC", "skill2": "強烈なプレッシャーD", "skill3": "半蔵のパワー", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "193", "girl": "kokoro", "name": "月閃忍装束(こころ)", "zhs_name": "月闪忍装束(心)", "zht_name": "月閃忍裝束(心)", "en_name": "Gessen Ninja Suit (Kokoro)", "kr_name": "월섬 닌자복(코코로)", "type": "tec", "pow": "3894", "tec": "5212", "stm": "3636", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦D", "skill3": "月閃のテクニック", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "194", "girl": "nagisa", "name": "月閃忍装束(なぎさ)", "zhs_name": "月闪忍装束(凪咲)", "zht_name": "月閃忍裝束(凪咲)", "en_name": "Gessen Ninja Suit (Nagisa)", "kr_name": "월섬 닌자복(나기사)", "type": "tec", "pow": "3894", "tec": "5212", "stm": "3636", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦D", "skill3": "月閃のテクニック", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "195", "girl": "nyotengu", "name": "月閃忍装束(女天狗)", "zhs_name": "月闪忍装束(女天狗)", "zht_name": "月閃忍裝束(女天狗)", "en_name": "Gessen Ninja Suit (Nyotengu)", "kr_name": "월섬 닌자복(뇨텐구)", "type": "tec", "pow": "3894", "tec": "5212", "stm": "3636", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦D", "skill3": "月閃のテクニック", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "196", "girl": "marie", "name": "紅蓮隊忍装束(マリー)", "zhs_name": "红莲队忍装束(玛莉)", "zht_name": "紅蓮隊忍裝束(瑪莉)", "en_name": "Crimson Squad Ninja Suit (Marie)", "kr_name": "홍련대 닌자복(마리)", "type": "pow", "pow": "5212", "tec": "3894", "stm": "3894", "apl": "200", "skill1": "強烈スパイクC", "skill2": "強烈なプレッシャーD", "skill3": "紅蓮隊のパワー", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "197", "girl": "hitomi", "name": "紅蓮隊忍装束(ヒトミ)", "zhs_name": "红莲队忍装束(瞳)", "zht_name": "紅蓮隊忍裝束(瞳)", "en_name": "Crimson Squad Ninja Suit (Hitomi)", "kr_name": "홍련대 닌자복(히토미)", "type": "pow", "pow": "5212", "tec": "3894", "stm": "3894", "apl": "200", "skill1": "強烈スパイクC", "skill2": "強烈なプレッシャーD", "skill3": "紅蓮隊のパワー", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "198", "girl": "fiona", "name": "紅蓮隊忍装束(フィオナ)", "zhs_name": "红莲队忍装束(菲欧娜)", "zht_name": "紅蓮隊忍裝束(菲歐娜)", "en_name": "Crimson Squad Ninja Suit (Fiona)", "kr_name": "홍련대 닌자복(피오나)", "type": "pow", "pow": "5212", "tec": "3894", "stm": "3894", "apl": "200", "skill1": "強烈スパイクC", "skill2": "強烈なプレッシャーD", "skill3": "紅蓮隊のパワー", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "199", "girl": "tamaki", "name": "蛇女忍装束(たまき)", "zhs_name": "蛇女忍装束(环)", "zht_name": "蛇女忍裝束(環)", "en_name": "Hebijo Ninja Suit (Tamaki)", "kr_name": "헤비죠 닌자복(타마키)", "type": "pow", "pow": "5212", "tec": "3894", "stm": "3894", "apl": "200", "skill1": "強烈スパイクC", "skill2": "強烈なプレッシャーD", "skill3": "蛇女忍のパワー", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "200", "girl": "leifang", "name": "蛇女忍装束(レイファン)", "zhs_name": "蛇女忍装束(丽凤)", "zht_name": "蛇女忍裝束(麗鳳)", "en_name": "Hebijo Ninja Suit (Leifang)", "kr_name": "헤비죠 닌자복(레이팡)", "type": "pow", "pow": "5212", "tec": "3894", "stm": "3894", "apl": "200", "skill1": "強烈スパイクC", "skill2": "強烈なプレッシャーD", "skill3": "蛇女忍のパワー", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "201", "girl": "helena", "name": "蛇女忍装束(エレナ)", "zhs_name": "蛇女忍装束(海莲娜)", "zht_name": "蛇女忍裝束(海蓮娜)", "en_name": "Hebijo Ninja Suit (Helena)", "kr_name": "헤비죠 닌자복(엘레나)", "type": "pow", "pow": "5212", "tec": "3894", "stm": "3894", "apl": "200", "skill1": "強烈スパイクC", "skill2": "強烈なプレッシャーD", "skill3": "蛇女忍のパワー", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "202", "girl": "misaki", "name": "巫神楽忍装束(みさき)", "zhs_name": "巫神乐忍装束(海咲)", "zht_name": "巫神樂忍裝束(海咲)", "en_name": "Mikagura Ninja Suit (Misaki)", "kr_name": "미카구라 닌자복(미사키)", "type": "tec", "pow": "3894", "tec": "5212", "stm": "3636", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦D", "skill3": "巫神楽のテクニック", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "203", "girl": "momiji", "name": "巫神楽忍装束(紅葉)", "zhs_name": "巫神乐忍装束(红叶)", "zht_name": "巫神樂忍裝束(紅葉)", "en_name": "Mikagura Ninja Suit (Momiji)", "kr_name": "미카구라 닌자복(모미지)", "type": "tec", "pow": "3894", "tec": "5212", "stm": "3636", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦D", "skill3": "巫神楽のテクニック", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "204", "girl": "luna", "name": "巫神楽忍装束(ルナ)", "zhs_name": "巫神乐忍装束(露娜)", "zht_name": "巫神樂忍裝束(露娜)", "en_name": "Mikagura Ninja Suit (Luna)", "kr_name": "미카구라 닌자복(루나)", "type": "tec", "pow": "3894", "tec": "5212", "stm": "3636", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦D", "skill3": "巫神楽のテクニック", "sell": "2019/7/18", "resell": "2022/3/17", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "205", "girl": "kasumi", "name": "シノマス水着・飛鳥(かすみ)", "zhs_name": "忍者大师泳装", "zht_name": "", "en_name": "Shinomas Swimsuit", "kr_name": "시노비 마스터 수영복", "type": "stm", "pow": "3994", "tec": "3736", "stm": "5312", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/7/25", "resell": "2022/3/23", "break": "1", "special_fun": "「シノビマスター 閃乱カグラ NEW LINK」联动服装"
  },
  {
    "id": "206", "girl": "honoka", "name": "シノマス水着・雲雀(ほのか)", "zhs_name": "忍者大师泳装", "zht_name": "", "en_name": "Shinomas Swimsuit", "kr_name": "시노비 마스터 수영복", "type": "stm", "pow": "3994", "tec": "3736", "stm": "5312", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/7/25", "resell": "2022/3/23", "break": "1", "special_fun": "「シノビマスター 閃乱カグラ NEW LINK」联动服装"
  },
  {
    "id": "207", "girl": "marie", "name": "シノマス水着・両備(マリー)", "zhs_name": "忍者大师泳装", "zht_name": "", "en_name": "Shinomas Swimsuit", "kr_name": "시노비 마스터 수영복", "type": "stm", "pow": "3994", "tec": "3736", "stm": "5312", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/7/25", "resell": "2022/3/23", "break": "1", "special_fun": "「シノビマスター 閃乱カグラ NEW LINK」联动服装"
  },
  {
    "id": "208", "girl": "ayane", "name": "シノマス水着・柳生(あやね)", "zhs_name": "忍者大师泳装", "zht_name": "", "en_name": "Shinomas Swimsuit", "kr_name": "시노비 마스터 수영복", "type": "stm", "pow": "3994", "tec": "3736", "stm": "5312", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/7/25", "resell": "2022/3/23", "break": "1", "special_fun": "「シノビマスター 閃乱カグラ NEW LINK」联动服装"
  },
  {
    "id": "209", "girl": "nyotengu", "name": "シノマス水着・叢(女天狗)", "zhs_name": "忍者大师泳装", "zht_name": "", "en_name": "Shinomas Swimsuit", "kr_name": "시노비 마스터 수영복", "type": "stm", "pow": "3994", "tec": "3736", "stm": "5312", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/7/25", "resell": "2022/3/23", "break": "1", "special_fun": "「シノビマスター 閃乱カグラ NEW LINK」联动服装"
  },
  {
    "id": "210", "girl": "kokoro", "name": "シノマス水着・雪泉(こころ)", "zhs_name": "忍者大师泳装", "zht_name": "", "en_name": "Shinomas Swimsuit", "kr_name": "시노비 마스터 수영복", "type": "stm", "pow": "3994", "tec": "3736", "stm": "5312", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/7/25", "resell": "2022/3/23", "break": "1", "special_fun": "「シノビマスター 閃乱カグラ NEW LINK」联动服装"
  },
  {
    "id": "211", "girl": "hitomi", "name": "シノマス水着・詠(ヒトミ)", "zhs_name": "忍者大师泳装", "zht_name": "", "en_name": "Shinomas Swimsuit", "kr_name": "시노비 마스터 수영복", "type": "stm", "pow": "3994", "tec": "3736", "stm": "5312", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/7/25", "resell": "2022/3/23", "break": "1", "special_fun": "「シノビマスター 閃乱カグラ NEW LINK」联动服装"
  },
  {
    "id": "212", "girl": "momiji", "name": "シノマス水着・焔(紅葉)", "zhs_name": "忍者大师泳装", "zht_name": "", "en_name": "Shinomas Swimsuit", "kr_name": "시노비 마스터 수영복", "type": "stm", "pow": "3994", "tec": "3736", "stm": "5312", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/7/25", "resell": "2022/3/23", "break": "1", "special_fun": "「シノビマスター 閃乱カグラ NEW LINK」联动服装"
  },
  {
    "id": "213", "girl": "helena", "name": "シノマス水着・春花(エレナ)", "zhs_name": "忍者大师泳装", "zht_name": "", "en_name": "Shinomas Swimsuit", "kr_name": "시노비 마스터 수영복", "type": "stm", "pow": "3994", "tec": "3736", "stm": "5312", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/7/25", "resell": "2022/3/23", "break": "1", "special_fun": "「シノビマスター 閃乱カグラ NEW LINK」联动服装"
  },
  {
    "id": "214", "girl": "kanna", "name": "祭囃子(カンナ)", "zhs_name": "祭典小调(神无)", "zht_name": "祭典小調(神無)", "en_name": "Festival Ensemble (Kanna)", "kr_name": "축제용 연주복(칸나)", "type": "tec", "pow": "4084", "tec": "5002", "stm": "3656", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "高度な心理戦C", "skill3": "閃きのテクニック3", "sell": "2019/7/31", "resell": "2020/5/19 2020/8/27 2021/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "215", "girl": "nyotengu", "name": "祭囃子(女天狗)", "zhs_name": "祭典小调(女天狗)", "zht_name": "祭典小調(女天狗)", "en_name": "Festival Ensemble (Nyotengu)", "kr_name": "축제용 연주복(뇨텐구)", "type": "tec", "pow": "4054", "tec": "4902", "stm": "3686", "apl": "200", "skill1": "高度な心理戦A", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2019/7/31", "resell": "2020/5/19 2020/8/27 2021/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "216", "girl": "ayane", "name": "ステラ・レオ(あやね)", "zhs_name": "星辰・狮子(绫音)", "zht_name": "星辰・獅子(綾音)", "en_name": "Stellar Leo (Ayane)", "kr_name": "스텔라 레오(아야네)", "type": "tec", "pow": "3984", "tec": "5322", "stm": "3636", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "レオ・テクニック", "skill3": "可憐なフェイント", "sell": "2019/8/5", "resell": "2019/10/31 2020/8/5 2021/8/5 2021/9/16 2022/8/5 2022/9/8 2023/8/5", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现粒子效果(光之舞)，服装拥有炸裂效果(碎片满天飞)强力生日衣服"
  },
  {
    "id": "217", "girl": "monica", "name": "ロイヤルフラッシュ(モニカ)", "zhs_name": "同花大顺(莫妮卡)", "zht_name": "同花大順(莫妮卡)", "en_name": "Royal Flush (Monica)", "kr_name": "로얄 플러시(모니카)", "type": "tec", "pow": "3944", "tec": "5042", "stm": "3756", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦B", "skill3": "閃きのテクニック3", "sell": "2019/8/7", "resell": "2020/1/1 2022/8/7", "break": "1", "special_fun": ""
  },
  {
    "id": "218", "girl": "kasumi", "name": "ハレーション(かすみ)", "zhs_name": "光晕(霞)", "zht_name": "光暈(霞)", "en_name": "Halation (Kasumi)", "kr_name": "헐레이션(카스미)", "type": "tec", "pow": "4024", "tec": "5022", "stm": "3696", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "高度な心理戦D", "skill3": "閃きのテクニック6", "sell": "2019/8/7", "resell": "", "break": "0", "special_fun": "跟新角色莫妮卡 一起登场的 DOA5LR DLC冷饭衣服 毫无存在感"
  },
  {
    "id": "219", "girl": "honoka", "name": "ホライズン(ほのか)", "zhs_name": "地平线(穗香)", "zht_name": "地平線(穗香)", "en_name": "Horizon (Honoka)", "kr_name": "호라이즌(호노카)", "type": "tec", "pow": "3944", "tec": "4902", "stm": "3796", "apl": "200", "skill1": "高度な心理戦E", "skill2": "内から湧き上がるスタミナ4", "skill3": "可憐なフェイント", "sell": "2019/8/7", "resell": "", "break": "0", "special_fun": "跟新角色莫妮卡 一起登场的 DOA5LR DLC冷饭衣服 毫无存在感"
  },
  {
    "id": "220", "girl": "ayane", "name": "ミケーリア(あやね)", "zhs_name": "含笑花(绫音)", "zht_name": "含笑花(綾音)", "en_name": "Michelia (Ayane)", "kr_name": "초령(아야네)", "type": "stm", "pow": "3634", "tec": "4316", "stm": "5142", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "灼熱のダンスE", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/8/15", "resell": "", "break": "0", "special_fun": ""
  },
  {
    "id": "221", "girl": "luna", "name": "スネグールカ(ルナ)", "zhs_name": "雪姑娘(露娜)", "zht_name": "雪姑娘(露娜)", "en_name": "Snegurochka (Luna)", "kr_name": "눈아가씨(루나)", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5102", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナD", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/8/15", "resell": "", "break": "0", "special_fun": ""
  },
  {
    "id": "222", "girl": "leifang", "name": "ヴァーミリオン(レイファン)", "zhs_name": "朱红(丽凤)", "zht_name": "朱红(丽凤)", "en_name": "Vermillion (Leifang)", "kr_name": "", "type": "stm", "pow": "3564", "tec": "4296", "stm": "5232", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "灼熱のダンスE", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/8/15", "resell": "", "break": "0", "special_fun": ""
  },
  {
    "id": "223", "girl": "helena", "name": "シャルトリュー(エレナ)", "zhs_name": "沙特尔猫(海莲娜)", "zht_name": "沙特尔猫(海莲娜)", "en_name": "Chartreux (Helena)", "kr_name": "", "type": "stm", "pow": "3804", "tec": "4256", "stm": "4982", "apl": "200", "skill1": "高度な心理戦B", "skill2": "内から湧き上がるスタミナ6", "skill3": "可憐なフェイント", "sell": "2019/8/15", "resell": "", "break": "0", "special_fun": ""
  },
  {
    "id": "224", "girl": "tamaki", "name": "ステラ・レオ(たまき)", "zhs_name": "星辰・狮子(环)", "zht_name": "星辰・獅子(環)", "en_name": "Stellar Leo (Tamaki)", "kr_name": "스텔라 레오(타마키)", "type": "pow", "pow": "5322", "tec": "3984", "stm": "3894", "apl": "200", "skill1": "強烈スパイクD", "skill2": "レオ・パワー", "skill3": "豪快なスパイク", "sell": "2019/8/19", "resell": "2019/10/31 2020/8/19 2021/8/19 2021/9/16 2022/8/19 2022/9/8", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现粒子效果(光之舞) 本以为环不会再受到迫害，结果衣服A技能和SSR饰品A技能同名冲突。KT策划再次丢掉了自己的脑子。服装拥有炸裂效果(碎片满天飞)"
  },
  {
    "id": "225_1", "girl": "kasumi", "name": "すずかぜロマンチカ(かすみ)", "zhs_name": "凉风罗曼(霞)", "zht_name": "涼風羅曼(霞)", "en_name": "Breeze Romantika (Kasumi)", "kr_name": "산들바람 로맨티카(카스미)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/2/23 2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_2", "girl": "ayane", "name": "すずかぜロマンチカ(あやね)", "zhs_name": "凉风罗曼(绫音)", "zht_name": "涼風羅曼(綾音)", "en_name": "Breeze Romantika (Ayane)", "kr_name": "산들바람 로맨티카(아야네)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/8/5 2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_3", "girl": "kokoro", "name": "すずかぜロマンチカ(こころ)", "zhs_name": "凉风罗曼(心)", "zht_name": "涼風羅曼(心)", "en_name": "Breeze Romantika (Kokoro)", "kr_name": "산들바람 로맨티카(코코로)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2019/12/1 2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_4", "girl": "momiji", "name": "すずかぜロマンチカ(紅葉)", "zhs_name": "凉风罗曼(红叶)", "zht_name": "涼風羅曼(紅葉)", "en_name": "Breeze Romantika (Momiji)", "kr_name": "산들바람 로맨티카(모미지)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/8/27 2020/9/20 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_5", "girl": "misaki", "name": "すずかぜロマンチカ(みさき)", "zhs_name": "凉风罗曼(海咲)", "zht_name": "涼風羅曼(海咲)", "en_name": "Breeze Romantika (Misaki)", "kr_name": "산들바람 로맨티카(미사키)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/7/7 2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_6", "girl": "luna", "name": "すずかぜロマンチカ(ルナ)", "zhs_name": "凉风罗曼(露娜)", "zht_name": "涼風羅曼(露娜)", "en_name": "Breeze Romantika (Luna)", "kr_name": "산들바람 로맨티카(루나)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_7", "girl": "fiona", "name": "すずかぜロマンチカ(フィオナ)", "zhs_name": "凉风罗曼(菲欧娜)", "zht_name": "涼風羅曼(菲歐娜)", "en_name": "Breeze Romantika (Fiona)", "kr_name": "산들바람 로맨티카(피오나)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_8", "girl": "nagisa", "name": "すずかぜロマンチカ(なぎさ)", "zhs_name": "凉风罗曼(凪咲)", "zht_name": "涼風羅曼(凪咲)", "en_name": "Breeze Romantika (Nagisa)", "kr_name": "산들바람 로맨티카(나기사)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_9", "girl": "honoka", "name": "すずかぜロマンチカ(ほのか)", "zhs_name": "凉风罗曼(穗香)", "zht_name": "涼風羅曼(穗香)", "en_name": "Breeze Romantika (Honoka)", "kr_name": "산들바람 로맨티카(호노카)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/3/24 2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_10", "girl": "marie", "name": "すずかぜロマンチカ(マリー)", "zhs_name": "凉风罗曼(玛莉)", "zht_name": "涼風羅曼(瑪莉)", "en_name": "Breeze Romantika (Marie)", "kr_name": "산들바람 로맨티카(마리)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/6/6 2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_11", "girl": "nyotengu", "name": "すずかぜロマンチカ(女天狗)", "zhs_name": "凉风罗曼(女天狗)", "zht_name": "涼風羅曼(女天狗)", "en_name": "Breeze Romantika (Nyotengu)", "kr_name": "산들바람 로맨티카(뇨텐구)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2019/11/19 2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_12", "girl": "hitomi", "name": "すずかぜロマンチカ(ヒトミ)", "zhs_name": "凉风罗曼(瞳)", "zht_name": "涼風羅曼(瞳)", "en_name": "Breeze Romantika (Hitomi)", "kr_name": "산들바람 로맨티카(히토미)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/5/25 2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_13", "girl": "helena", "name": "すずかぜロマンチカ(エレナ)", "zhs_name": "凉风罗曼(海莲娜)", "zht_name": "涼風羅曼(海蓮娜)", "en_name": "Breeze Romantika (Helena)", "kr_name": "산들바람 로맨티카(엘레나)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/1/30 2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_14", "girl": "tamaki", "name": "すずかぜロマンチカ(たまき)", "zhs_name": "凉风罗曼(环)", "zht_name": "涼風羅曼(環)", "en_name": "Breeze Romantika (Tamaki)", "kr_name": "산들바람 로맨티카(타마키)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_15", "girl": "leifang", "name": "すずかぜロマンチカ(レイファン)", "zhs_name": "凉风罗曼(丽凤)", "zht_name": "涼風羅曼(麗鳳)", "en_name": "Breeze Romantika (Leifang)", "kr_name": "산들바람 로맨티카(레이팡)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_16", "girl": "kanna", "name": "すずかぜロマンチカ(カンナ)", "zhs_name": "凉风罗曼(神无)", "zht_name": "涼風羅曼(神無)", "en_name": "Breeze Romantika (Kanna)", "kr_name": "산들바람 로맨티카(칸나)", "type": "pow", "pow": "5002", "tec": "3844", "stm": "4054", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2019/8/22", "resell": "2020/8/27 2021/8/4 2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "226", "girl": "kanna", "name": "はいからブロッサム(カンナ)", "zhs_name": "洋式制服之花(神无)", "zht_name": "洋式制服之花(神無)", "en_name": "Stylish Blossom (Kanna)", "kr_name": "하이 컬러 블로섬(칸나)", "type": "apl", "pow": "3756", "tec": "4526", "stm": "4244", "apl": "550", "skill1": "裏の裏を突くフェイントC", "skill2": "観客総立ちE", "skill3": "隠しきれない魅力5", "sell": "2019/8/29", "resell": "2020/7/16 2021/7/9", "break": "1", "special_fun": ""
  },
  {
    "id": "227", "girl": "fiona", "name": "はいからブロッサム(フィオナ)", "zhs_name": "洋式制服之花(菲欧娜)", "zht_name": "洋式制服之花(菲歐娜)", "en_name": "Stylish Blossom (Fiona)", "kr_name": "하이 컬러 블로섬(피오나)", "type": "apl", "pow": "3666", "tec": "4496", "stm": "4264", "apl": "550", "skill1": "高度な心理戦E", "skill2": "隠しきれない魅力4", "skill3": "可憐なフェイント", "sell": "2019/8/29", "resell": "2020/7/16 2021/7/9", "break": "1", "special_fun": ""
  },
  {
    "id": "228", "girl": "momiji", "name": "はいからブロッサム(紅葉)", "zhs_name": "洋式制服之花(红叶)", "zht_name": "洋式制服之花(紅葉)", "en_name": "Stylish Blossom (Momiji)", "kr_name": "하이 컬러 블로섬(모미지)", "type": "apl", "pow": "3756", "tec": "4526", "stm": "4244", "apl": "550", "skill1": "裏の裏を突くフェイントC", "skill2": "観客総立ちE", "skill3": "隠しきれない魅力5", "sell": "2019/8/29", "resell": "2020/7/16 2021/7/9", "break": "1", "special_fun": ""
  },
  {
    "id": "229", "girl": "tamaki", "name": "うすかわたけのこ(たまき)", "zhs_name": "薄皮竹笋(环)", "zht_name": "薄皮竹筍(環)", "en_name": "Thin Towel Wrap (Tamaki)", "kr_name": "박막 죽순(타마키)", "type": "tec", "pow": "3994", "tec": "4992", "stm": "3656", "apl": "200", "skill1": "高度な心理戦D", "skill2": "内から湧き上がるスタミナ5", "skill3": "可憐なフェイント", "sell": "2019/9/5", "resell": "2021/12/9", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "230", "girl": "helena", "name": "うすかわたけのこ(エレナ)", "zhs_name": "薄皮竹笋(海莲娜)", "zht_name": "薄皮竹筍(海蓮娜)", "en_name": "Thin Towel Wrap (Helena)", "kr_name": "박막 죽순(엘레나)", "type": "tec", "pow": "3844", "tec": "5202", "stm": "3696", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "驚異のスタミナD", "skill3": "閃きのテクニック6", "sell": "2019/9/5", "resell": "2021/12/9", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "231", "girl": "monica", "name": "スペード・クイーン(モニカ)", "zhs_name": "黑桃皇后(莫妮卡)", "zht_name": "黑桃皇后(莫妮卡)", "en_name": "Queen of Spades (Monica)", "kr_name": "스페이드 퀸(모니카)", "type": "stm", "pow": "3744", "tec": "4236", "stm": "5062", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ4", "skill3": "可憐なフェイント", "sell": "2019/9/5", "resell": "2020/1/1 2022/8/7", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "232_1", "girl": "fiona", "name": "ネイキッドサマー(フィオナ)", "zhs_name": "清透夏日(菲欧娜)", "zht_name": "清透夏日(菲歐娜)", "en_name": "Naked Summer (Fiona)", "kr_name": "네이키드 서머(피오나)", "type": "stm", "pow": "3594", "tec": "4406", "stm": "5042", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2019/9/12", "resell": "2020/5/12", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "232_2", "girl": "nagisa", "name": "ネイキッドサマー(なぎさ)", "zhs_name": "清透夏日(凪咲)", "zht_name": "清透夏日(凪咲)", "en_name": "Naked Summer (Nagisa)", "kr_name": "네이키드 서머(나기사)", "type": "stm", "pow": "3594", "tec": "4406", "stm": "5042", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2019/9/12", "resell": "2020/5/12", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "232_3", "girl": "kanna", "name": "ネイキッドサマー(カンナ)", "zhs_name": "清透夏日(神无)", "zht_name": "清透夏日(神無)", "en_name": "Naked Summer (Kanna)", "kr_name": "네이키드 서머(칸나)", "type": "stm", "pow": "3594", "tec": "4406", "stm": "5042", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2019/9/12", "resell": "2020/5/12", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "232_4", "girl": "momiji", "name": "ネイキッドサマー(紅葉)", "zhs_name": "清透夏日(红叶)", "zht_name": "清透夏日(紅葉)", "en_name": "Naked Summer (Momiji)", "kr_name": "네이키드 서머(모미지)", "type": "stm", "pow": "3594", "tec": "4406", "stm": "5042", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2019/9/12", "resell": "2020/5/12", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "232_5", "girl": "tamaki", "name": "ネイキッドサマー(たまき)", "zhs_name": "清透夏日(环)", "zht_name": "清透夏日(環)", "en_name": "Naked Summer (Tamaki)", "kr_name": "네이키드 서머v(타마키)", "type": "stm", "pow": "3594", "tec": "4406", "stm": "5042", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2019/9/12", "resell": "2020/5/7", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "232_6", "girl": "marie", "name": "ネイキッドサマー(マリー)", "zhs_name": "清透夏日(玛莉)", "zht_name": "清透夏日(瑪莉)", "en_name": "Naked Summer (Marie)", "kr_name": "네이키드 서머(마리)", "type": "stm", "pow": "3594", "tec": "4406", "stm": "5042", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2019/9/12", "resell": "2020/5/7", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "232_7", "girl": "kasumi", "name": "ネイキッドサマー(かすみ)", "zhs_name": "清透夏日(霞)", "zht_name": "清透夏日(霞)", "en_name": "Naked Summer (Kasumi)", "kr_name": "네이키드 서머(카스미)", "type": "stm", "pow": "3594", "tec": "4406", "stm": "5042", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2019/9/12", "resell": "2020/2/23 2020/5/7", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "232_8", "girl": "kokoro", "name": "ネイキッドサマー(こころ)", "zhs_name": "清透夏日(心)", "zht_name": "清透夏日(心)", "en_name": "Naked Summer (Kokoro)", "kr_name": "네이키드 서머(코코로)", "type": "stm", "pow": "3594", "tec": "4406", "stm": "5042", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2019/9/12", "resell": "2019/12/1 2020/5/7", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "233", "girl": "kanna", "name": "ステラ・ウィルゴ(カンナ)", "zhs_name": "星辰・处女(神无)", "zht_name": "星辰・處女(神無)", "en_name": "Stellar Virgo (Kanna)", "kr_name": "스텔라 비르고(칸나)", "type": "pow", "pow": "5322", "tec": "3714", "stm": "4164", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ウィルゴ・パワー", "skill3": "豪快なスパイク", "sell": "2019/9/15", "resell": "2019/10/31 2020/9/15 2021/9/15 2021/9/16 2022/9/8 2022/9/15", "break": "1", "special_fun": "生日池子只开4天，真实边缘人没有之一。使用天狗扇 扇动的时候 会出现粒子效果(光之舞)"
  },
  {
    "id": "234_1", "girl": "nyotengu", "name": "ヴィーナス・ヴァルキリー(女天狗)", "zhs_name": "维纳斯女武神(女天狗)", "zht_name": "維納斯女武神(女天狗)", "en_name": "Venus Valkyrie (Nyotengu)", "kr_name": "비너스 발키리(뇨텐구)", "type": "pow", "pow": "4952", "tec": "3754", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "驚異のスタミナF", "skill3": "ヴァルキリーのパワー", "sell": "2019/9/19", "resell": "2019/11/19 2020/9/23 2020/12/9 2023/1/26", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞) 2020-12-9 更新 最大觉醒任务赠送小道具 剑"
  },
  {
    "id": "234_2", "girl": "honoka", "name": "ヴィーナス・ヴァルキリー(ほのか)", "zhs_name": "维纳斯女武神(穗香)", "zht_name": "維納斯女武神(穗香)", "en_name": "Venus Valkyrie (Honoka)", "kr_name": "비너스 발키리(호노카)", "type": "pow", "pow": "4952", "tec": "3754", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "驚異のスタミナF", "skill3": "ヴァルキリーのパワー", "sell": "2019/9/19", "resell": "2020/3/24 2020/9/23 2020/12/9 2023/1/26", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞) 2020-12-9 更新 最大觉醒任务赠送小道具 剑"
  },
  {
    "id": "234_3", "girl": "misaki", "name": "ヴィーナス・ヴァルキリー(みさき)", "zhs_name": "维纳斯女武神(海咲)", "zht_name": "維納斯女武神(海咲)", "en_name": "Venus Valkyrie (Misaki)", "kr_name": "비너스 발키리(미사키)", "type": "pow", "pow": "4952", "tec": "3754", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "驚異のスタミナF", "skill3": "ヴァルキリーのパワー", "sell": "2019/9/19", "resell": "2020/9/23 2020/12/9 2023/1/26", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞) 2020-12-9 更新 最大觉醒任务赠送小道具 剑"
  },
  {
    "id": "234_4", "girl": "leifang", "name": "ヴィーナス・ヴァルキリー(レイファン)", "zhs_name": "维纳斯女武神(丽凤)", "zht_name": "維納斯女武神(麗鳳)", "en_name": "Venus Valkyrie (Leifang)", "kr_name": "비너스 발키리(레이팡)", "type": "pow", "pow": "4952", "tec": "3754", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "驚異のスタミナF", "skill3": "ヴァルキリーのパワー", "sell": "2019/9/19", "resell": "2020/9/23 2020/12/9 2023/1/26", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞) 2020-12-9 更新 最大觉醒任务赠送小道具 剑"
  },
  {
    "id": "234_5", "girl": "helena", "name": "ヴィーナス・ヴァルキリー(エレナ)", "zhs_name": "维纳斯女武神(海莲娜)", "zht_name": "維納斯女武神(海蓮娜)", "en_name": "Venus Valkyrie (Helena)", "kr_name": "비너스 발키리(엘레나)", "type": "pow", "pow": "4952", "tec": "3754", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "驚異のスタミナF", "skill3": "ヴァルキリーのパワー", "sell": "2019/9/19", "resell": "2020/1/30 2020/9/23 2020/12/9 2023/1/26", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞) 2020-12-9 更新 最大觉醒任务赠送小道具 剑"
  },
  {
    "id": "234_6", "girl": "ayane", "name": "ヴィーナス・ヴァルキリー(あやね)", "zhs_name": "维纳斯女武神(绫音)", "zht_name": "維納斯女武神(綾音)", "en_name": "Venus Valkyrie (Ayane)", "kr_name": "비너스 발키리(아야네)", "type": "pow", "pow": "4952", "tec": "3754", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "驚異のスタミナF", "skill3": "ヴァルキリーのパワー", "sell": "2019/9/19", "resell": "2020/9/23 2020/12/9 2023/1/26", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞) 2020-12-9 更新 最大觉醒任务赠送小道具 剑"
  },
  {
    "id": "234_7", "girl": "luna", "name": "ヴィーナス・ヴァルキリー(ルナ)", "zhs_name": "维纳斯女武神(露娜)", "zht_name": "維納斯女武神(露娜)", "en_name": "Venus Valkyrie (Luna)", "kr_name": "비너스 발키리(루나)", "type": "pow", "pow": "4952", "tec": "3754", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "驚異のスタミナF", "skill3": "ヴァルキリーのパワー", "sell": "2019/9/19", "resell": "2020/9/23 2020/12/9 2023/1/26", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞) 2020-12-9 更新 最大觉醒任务赠送小道具 剑"
  },
  {
    "id": "234_8", "girl": "hitomi", "name": "ヴィーナス・ヴァルキリー(ヒトミ)", "zhs_name": "维纳斯女武神(瞳)", "zht_name": "維納斯女武神(瞳)", "en_name": "Venus Valkyrie (Hitomi)", "kr_name": "비너스 발키리(히토미)", "type": "pow", "pow": "4952", "tec": "3754", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "驚異のスタミナF", "skill3": "ヴァルキリーのパワー", "sell": "2019/9/19", "resell": "2020/5/25 2020/9/23 2020/12/9 2023/1/26", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞) 2020-12-9 更新 最大觉醒任务赠送小道具 剑"
  },
  {
    "id": "235", "girl": "momiji", "name": "ステラ・ウィルゴ(紅葉)", "zhs_name": "星辰・处女(红叶)", "zht_name": "星辰・處女(紅葉)", "en_name": "Stellar Virgo (Momiji)", "kr_name": "스텔라 비르고(모미지)", "type": "stm", "pow": "4594", "tec": "3426", "stm": "5322", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ウィルゴ・スタミナ", "skill3": "豪快なスパイク", "sell": "2019/9/20", "resell": "2019/10/31 2020/9/20 2021/9/20 2021/9/16 2022/9/8 2022/9/20", "break": "1", "special_fun": "没有逃过同星座第二件生日服必有坑的诅咒。使用天狗扇 扇动的时候 会出现粒子效果(光之舞)"
  },
  {
    "id": "236", "girl": "honoka", "name": "やわらかエンジンTシャツ(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4084", "tec": "3776", "stm": "4882", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "灼熱のダンスF", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/9/21", "resell": "", "break": "1", "special_fun": "virtual market 3出展纪念 赠送"
  },
  {
    "id": "237", "girl": "misaki", "name": "アクア・キャビア(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3604", "tec": "5112", "stm": "4026", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "驚異のスタミナE", "skill3": "閃きのテクニック5", "sell": "2019/9/26", "resell": "2020/7/9", "break": "1", "special_fun": ""
  },
  {
    "id": "238", "girl": "hitomi", "name": "アクア・キャビア(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3544", "tec": "5002", "stm": "4096", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2019/9/26", "resell": "2020/7/9", "break": "1", "special_fun": ""
  },
  {
    "id": "239", "girl": "kasumi", "name": "アクア・キャビア(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3604", "tec": "5112", "stm": "4026", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "驚異のスタミナE", "skill3": "閃きのテクニック5", "sell": "2019/9/26", "resell": "2020/7/9", "break": "1", "special_fun": ""
  },
  {
    "id": "240", "girl": "nagisa", "name": "プリンセス・グレイス(なぎさ)", "zhs_name": "优雅公主(凪咲)", "zht_name": "優雅公主(凪咲)", "en_name": "Princess Grace (Nagisa)", "kr_name": "프린세스 그레이스(나기사)", "type": "pow", "pow": "5112", "tec": "3884", "stm": "4004", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナB", "skill3": "秘められたパワー6", "sell": "2019/10/3", "resell": "2020/6/11 2021/5/13", "break": "1", "special_fun": ""
  },
  {
    "id": "241", "girl": "kokoro", "name": "プリンセス・グレイス(こころ)", "zhs_name": "优雅公主(心)", "zht_name": "優雅公主(心)", "en_name": "Princess Grace (Kokoro)", "kr_name": "프린세스 그레이스(코코로)", "type": "pow", "pow": "5022", "tec": "3794", "stm": "4084", "apl": "200", "skill1": "強烈なプレッシャーA", "skill2": "内から湧き上がるスタミナ4", "skill3": "豪快なスパイク", "sell": "2019/10/3", "resell": "2020/6/11 2021/5/13", "break": "1", "special_fun": ""
  },
  {
    "id": "242", "girl": "helena", "name": "プリンセス・グレイス(エレナ)", "zhs_name": "优雅公主(海莲娜)", "zht_name": "優雅公主(海蓮娜)", "en_name": "Princess Grace (Helena)", "kr_name": "프린세스 그레이스(엘레나)", "type": "pow", "pow": "5112", "tec": "3884", "stm": "4004", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナB", "skill3": "秘められたパワー6", "sell": "2019/10/3", "resell": "2020/6/11 2021/5/13", "break": "1", "special_fun": ""
  },
  {
    "id": "243", "girl": "luna", "name": "おつまみピンチョス(ルナ)", "zhs_name": "拽拽Pinchos(露娜)", "zht_name": "拽拽Pinchos(露娜)", "en_name": "Appetizer Pinchos (Luna)", "kr_name": "애피타이저 핀초(루나)", "type": "pow", "pow": "5122", "tec": "4014", "stm": "3864", "apl": "200", "skill1": "強烈スパイクE", "skill2": "不動のレシーブF", "skill3": "秘められたパワー6", "sell": "2019/10/9", "resell": "2020/6/24 2020/11/5 2021/10/14", "break": "1", "special_fun": "允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "244", "girl": "luna", "name": "ステラ・リブラ(ルナ)", "zhs_name": "星辰‧天秤(露娜)", "zht_name": "星辰・天秤(露娜)", "en_name": "Stellar Libra (Luna)", "kr_name": "스텔라 리브라(루나)", "type": "stm", "pow": "4544", "tec": "3476", "stm": "5322", "apl": "200", "skill1": "強烈スパイクD", "skill2": "リブラ・スタミナ", "skill3": "豪快なスパイク", "sell": "2019/10/15", "resell": "2019/10/31 2020/10/15 2021/9/16 2021/10/15 2022/9/8 2022/10/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现粒子效果(光之舞)【紫色】,生日被害者+1，策划又放飞了自己的亲妈"
  },
  {
    "id": "245_1", "girl": "tamaki", "name": "チャーム・ウィッチ(たまき)", "zhs_name": "魅力・魔女(环)", "zht_name": "魅力・魔女(環)", "en_name": "Charm Witch (Tamaki)", "kr_name": "매혹적인 마녀(타마키)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_2", "girl": "marie", "name": "チャーム・ウィッチ(マリー)", "zhs_name": "魅力・魔女(玛莉)", "zht_name": "魅力・魔女(瑪莉)", "en_name": "Charm Witch (Marie)", "kr_name": "매혹적인 마녀(마리)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/6/6 2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_3", "girl": "fiona", "name": "チャーム・ウィッチ(フィオナ)", "zhs_name": "魅力・魔女(菲欧娜)", "zht_name": "魅力・魔女(菲歐娜)", "en_name": "Charm Witch (Fiona)", "kr_name": "매혹적인 마녀(피오나)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_4", "girl": "nyotengu", "name": "チャーム・ウィッチ(女天狗)", "zhs_name": "魅力・魔女(女天狗)", "zht_name": "魅力・魔女(女天狗)", "en_name": "Charm Witch (Nyotengu)", "kr_name": "매혹적인 마녀(뇨텐구)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2019/11/19 2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_5", "girl": "luna", "name": "チャーム・ウィッチ(ルナ)", "zhs_name": "魅力・魔女(露娜)", "zht_name": "魅力・魔女(露娜)", "en_name": "Charm Witch (Luna)", "kr_name": "매혹적인 마녀(루나)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_6", "girl": "kasumi", "name": "チャーム・ウィッチ(かすみ)", "zhs_name": "魅力・魔女(霞)", "zht_name": "魅力・魔女(霞)", "en_name": "Charm Witch (Kasumi)", "kr_name": "매혹적인 마녀(카스미)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/2/23 2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_7", "girl": "ayane", "name": "チャーム・ウィッチ(あやね)", "zhs_name": "魅力・魔女(绫音)", "zht_name": "魅力・魔女(綾音)", "en_name": "Charm Witch (Ayane)", "kr_name": "매혹적인 마녀(아야네)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/8/5 2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_8", "girl": "helena", "name": "チャーム・ウィッチ(エレナ)", "zhs_name": "魅力・魔女(海莲娜)", "zht_name": "魅力・魔女(海蓮娜)", "en_name": "Charm Witch (Helena)", "kr_name": "매혹적인 마녀(엘레나)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/1/30 2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_9", "girl": "misaki", "name": "チャーム・ウィッチ(みさき)", "zhs_name": "魅力・魔女(海咲)", "zht_name": "魅力・魔女(海咲)", "en_name": "Charm Witch (Misaki)", "kr_name": "매혹적인 마녀(미사키)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/7/7 2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_10", "girl": "nagisa", "name": "チャーム・ウィッチ(なぎさ)", "zhs_name": "魅力・魔女(凪咲)", "zht_name": "魅力・魔女(凪咲)", "en_name": "Charm Witch (Nagisa)", "kr_name": "매혹적인 마녀(나기사)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_11", "girl": "honoka", "name": "チャーム・ウィッチ(ほのか)", "zhs_name": "魅力・魔女(穗香)", "zht_name": "魅力・魔女(穗香)", "en_name": "Charm Witch (Honoka)", "kr_name": "매혹적인 마녀(호노카)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/3/24 2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_12", "girl": "kokoro", "name": "チャーム・ウィッチ(こころ)", "zhs_name": "魅力・魔女(心)", "zht_name": "魅力・魔女(心)", "en_name": "Charm Witch (Kokoro)", "kr_name": "매혹적인 마녀(코코로)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2019/12/1 2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_13", "girl": "momiji", "name": "チャーム・ウィッチ(紅葉)", "zhs_name": "魅力・魔女(红叶)", "zht_name": "魅力・魔女(紅葉)", "en_name": "Charm Witch (Momiji)", "kr_name": "매혹적인 마녀(모미지)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/9/20 2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_14", "girl": "hitomi", "name": "チャーム・ウィッチ(ヒトミ)", "zhs_name": "魅力・魔女(瞳)", "zht_name": "魅力・魔女(瞳)", "en_name": "Charm Witch (Hitomi)", "kr_name": "매혹적인 마녀(히토미)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/5/25 2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_15", "girl": "leifang", "name": "チャーム・ウィッチ(レイファン)", "zhs_name": "魅力・魔女(丽凤)", "zht_name": "魅力・魔女(麗鳳)", "en_name": "Charm Witch (Leifang)", "kr_name": "매혹적인 마녀(레이팡)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "245_16", "girl": "kanna", "name": "チャーム・ウィッチ(カンナ)", "zhs_name": "魅力・魔女(神无)", "zht_name": "魅力・魔女(神無)", "en_name": "Charm Witch (Kanna)", "kr_name": "매혹적인 마녀(칸나)", "type": "stm", "pow": "3674", "tec": "4366", "stm": "5002", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/10/17", "resell": "2020/10/29 2021/10/8 2022/10/20", "break": "1", "special_fun": "帽子可以单独设定显示或者隐藏"
  },
  {
    "id": "246", "girl": "honoka", "name": "ミスティ・リリー(ほのか)", "zhs_name": "神秘・百合(穗香)", "zht_name": "神秘・百合(穗香)", "en_name": "Misty Lily (Honoka)", "kr_name": "미스티 릴리(호노카)", "type": "apl", "pow": "4586", "tec": "3826", "stm": "4114", "apl": "550", "skill1": "強烈スパイクE", "skill2": "観客総立ちC", "skill3": "隠しきれない魅力5", "sell": "2019/10/24", "resell": "2020/7/2 2021/7/14", "break": "1", "special_fun": ""
  },
  {
    "id": "247", "girl": "ayane", "name": "ミスティ・リリー(あやね)", "zhs_name": "神秘・百合(绫音)", "zht_name": "神秘・百合(綾音)", "en_name": "Misty Lily (Ayane)", "kr_name": "미스티 릴리(아야네)", "type": "apl", "pow": "4396", "tec": "3806", "stm": "4224", "apl": "550", "skill1": "強烈なプレッシャーD", "skill2": "隠しきれない魅力4", "skill3": "豪快なスパイク", "sell": "2019/10/24", "resell": "2020/7/2 2021/7/14", "break": "1", "special_fun": ""
  },
  {
    "id": "248", "girl": "fiona", "name": "ミスティ・リリー(フィオナ)", "zhs_name": "神秘・百合(菲欧娜)", "zht_name": "神秘・百合(菲歐娜)", "en_name": "Misty Lily (Fiona)", "kr_name": "미스티 릴리(피오나)", "type": "apl", "pow": "4586", "tec": "3826", "stm": "4114", "apl": "550", "skill1": "強烈スパイクE", "skill2": "観客総立ちC", "skill3": "隠しきれない魅力5", "sell": "2019/10/24", "resell": "2020/7/2 2021/7/14", "break": "1", "special_fun": ""
  },
  {
    "id": "249", "girl": "nagisa", "name": "恋色いろは(なぎさ)", "zhs_name": "恋色伊吕波", "zht_name": "戀色伊呂波(凪咲)", "en_name": "Maple Romance (Nagisa)", "kr_name": "사랑빛 이로하(나기사)", "type": "tec", "pow": "3544", "tec": "5042", "stm": "4156", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "灼熱のダンスB", "skill3": "閃きのテクニック4", "sell": "2019/10/31", "resell": "2020/10/29 2021/11/2 2022/9/29", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现落叶，喷水会使叶子颜色变化"
  },
  {
    "id": "250", "girl": "tamaki", "name": "恋色いろは(たまき)", "zhs_name": "恋色伊吕波", "zht_name": "戀色伊呂波(環)", "en_name": "Maple Romance (Tamaki)", "kr_name": "사랑빛 이로하(타마키)", "type": "tec", "pow": "3544", "tec": "5042", "stm": "4156", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "灼熱のダンスB", "skill3": "閃きのテクニック4", "sell": "2019/10/31", "resell": "2020/10/29 2021/11/2 2022/9/29", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现落叶，喷水会使叶子颜色变化"
  },
  {
    "id": "251", "girl": "momiji", "name": "恋色いろは(紅葉)", "zhs_name": "恋色伊吕波", "zht_name": "戀色伊呂波(紅葉)", "en_name": "Maple Romance (Momiji)", "kr_name": "사랑빛 이로하(모미지)", "type": "tec", "pow": "3544", "tec": "5042", "stm": "4156", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "灼熱のダンスB", "skill3": "閃きのテクニック4", "sell": "2019/10/31", "resell": "2020/10/29 2021/11/2 2022/9/29", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现落叶，喷水会使叶子颜色变化"
  },
  {
    "id": "252", "girl": "nyotengu", "name": "恋色いろは(女天狗)", "zhs_name": "恋色伊吕波(女天狗)", "zht_name": "戀色伊呂波(女天狗)", "en_name": "Maple Romance (Nyotengu)", "kr_name": "사랑빛 이로하(뇨텐구)", "type": "tec", "pow": "3574", "tec": "4962", "stm": "4106", "apl": "200", "skill1": "高度な心理戦B", "skill2": "閃きのテクニック5", "skill3": "可憐なフェイント", "sell": "2019/10/31", "resell": "2020/10/29 2021/11/2 2022/9/29", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现落叶，喷水会使叶子颜色变化"
  },
  {
    "id": "253", "girl": "nagisa", "name": "旗袍・青龍(なぎさ)", "zhs_name": "旗袍・青龙(凪咲)", "zht_name": "旗袍・青龍(凪咲)", "en_name": "Blue Dragon Cheongsam (Nagisa)", "kr_name": "치파오(청룡)(나기사)", "type": "pow", "pow": "5032", "tec": "3864", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー6", "sell": "2019/11/7", "resell": "2020/4/30 2020/8/20 2020/12/7 2021/1/1 2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "254", "girl": "misaki", "name": "旗袍・白虎(みさき)", "zhs_name": "旗袍・白虎(海咲)", "zht_name": "旗袍・白虎(海咲)", "en_name": "White Tiger Cheongsam (Honoka)", "kr_name": "치파오(백호)(미사키)", "type": "pow", "pow": "5032", "tec": "3864", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー6", "sell": "2019/11/7", "resell": "2020/4/30 2020/12/7 2021/1/1 2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "255", "girl": "honoka", "name": "旗袍・白虎(ほのか)", "zhs_name": "旗袍・白虎(穗香)", "zht_name": "旗袍・白虎(穗香)", "en_name": "White Tiger Cheongsam (Misaki)", "kr_name": "치파오(백호)(호노카)", "type": "pow", "pow": "5032", "tec": "3864", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー6", "sell": "2019/11/7", "resell": "2020/4/30 2020/12/7 2021/1/1 2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "256", "girl": "helena", "name": "旗袍・玄武(エレナ)", "zhs_name": "旗袍・玄武(海莲娜)", "zht_name": "旗袍・玄武(海蓮娜)", "en_name": "Black Tortoise Cheongsam (Helena)", "kr_name": "치파오(현무)(엘레나)", "type": "pow", "pow": "4942", "tec": "3794", "stm": "4164", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "内から湧き上がるスタミナ5", "skill3": "豪快なスパイク", "sell": "2019/11/7", "resell": "2020/12/7 2021/1/1 2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "257", "girl": "fiona", "name": "こもれびハミング(フィオナ)", "zhs_name": "树荫光斑蜂鸟(菲欧娜)", "zht_name": "樹蔭光斑蜂鳥(菲歐娜)", "en_name": "Sunlight Humming (Fiona)", "kr_name": "햇살 속의 허밍(피오나)", "type": "stm", "pow": "4344", "tec": "3596", "stm": "5102", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2019/11/7", "resell": "2020/6/7 2020/12/7 2021/8/27 2022/1/19 2022/9/8", "break": "1", "special_fun": ""
  },
  {
    "id": "258", "girl": "kokoro", "name": "こもれびハミング(こころ)", "zhs_name": "树荫光斑蜂鸟(心)", "zht_name": "樹蔭光斑蜂鳥(心)", "en_name": "Sunlight Humming (Kokoro)", "kr_name": "햇살 속의 허밍(코코로)", "type": "stm", "pow": "4364", "tec": "3856", "stm": "4922", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "灼熱のダンスC", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/11/7", "resell": "2020/6/7 2020/12/7 2021/8/27 2022/1/19 2022/9/8", "break": "1", "special_fun": ""
  },
  {
    "id": "259", "girl": "momiji", "name": "こもれびハミング(紅葉)", "zhs_name": "树荫光斑蜂鸟(红叶)", "zht_name": "樹蔭光斑蜂鳥(紅葉)", "en_name": "Sunlight Humming (Momiji)", "kr_name": "햇살 속의 허밍(모미지)", "type": "stm", "pow": "4364", "tec": "3856", "stm": "4922", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "灼熱のダンスC", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/11/7", "resell": "2020/6/7 2020/12/7 2021/8/27 2022/1/19 2022/9/8", "break": "1", "special_fun": ""
  },
  {
    "id": "260", "girl": "kasumi", "name": "こもれびハミング(かすみ)", "zhs_name": "树荫光斑蜂鸟(霞)", "zht_name": "樹蔭光斑蜂鳥(霞)", "en_name": "Sunlight Humming (Kasumi)", "kr_name": "햇살 속의 허밍(카스미)", "type": "stm", "pow": "4364", "tec": "3856", "stm": "4922", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "灼熱のダンスC", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/11/7", "resell": "2020/6/7 2020/12/7 2021/8/27 2022/1/19 2022/9/8", "break": "1", "special_fun": ""
  },
  {
    "id": "261", "girl": "tamaki", "name": "ゆるふわパーカー(たまき)", "zhs_name": "轻柔连帽衫(环)", "zht_name": "輕柔連帽衫(環)", "en_name": "Soft 'n Fluffy Parka (Tamaki)", "kr_name": "부드러운 파카(타마키)", "type": "stm", "pow": "4014", "tec": "4176", "stm": "4952", "apl": "200", "skill1": "高度な心理戦C", "skill2": "灼熱のダンスC", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/11/7", "resell": "2020/12/7 2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "262", "girl": "luna", "name": "ゆるふわパーカー(ルナ)", "zhs_name": "轻柔连帽衫(露娜)", "zht_name": "輕柔連帽衫(露娜)", "en_name": "Soft 'n Fluffy Parka (Luna)", "kr_name": "부드러운 파카(루나)", "type": "stm", "pow": "4024", "tec": "4106", "stm": "4912", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2019/11/7", "resell": "2020/12/7 2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "263", "girl": "nyotengu", "name": "ゆるふわパーカー(女天狗)", "zhs_name": "轻柔连帽衫(女天狗)", "zht_name": "輕柔連帽衫(女天狗)", "en_name": "Soft 'n Fluffy Parka (Nyotengu)", "kr_name": "부드러운 파카(뇨텐구)", "type": "stm", "pow": "4014", "tec": "4176", "stm": "4952", "apl": "200", "skill1": "高度な心理戦C", "skill2": "灼熱のダンスC", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/11/7", "resell": "2020/12/7 2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "264", "girl": "hitomi", "name": "ゆるふわパーカー(ヒトミ)", "zhs_name": "轻柔连帽衫(瞳)", "zht_name": "輕柔連帽衫(瞳)", "en_name": "Soft 'n Fluffy Parka (Hitomi)", "kr_name": "부드러운 파카(히토미)", "type": "stm", "pow": "4014", "tec": "4176", "stm": "4952", "apl": "200", "skill1": "高度な心理戦C", "skill2": "灼熱のダンスC", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/11/7", "resell": "2020/12/7 2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "265", "girl": "marie", "name": "春彩のスクールウェア(マリー)", "zhs_name": "春色校服(玛莉)", "zht_name": "春色校服(瑪莉)", "en_name": "Springtime Schoolwear (Marie)", "kr_name": "화사한 봄철 학생복(마리)", "type": "tec", "pow": "4174", "tec": "4862", "stm": "3606", "apl": "200", "skill1": "高度な心理戦C", "skill2": "内から湧き上がるスタミナ5", "skill3": "可憐なフェイント", "sell": "2019/11/7", "resell": "2020/4/14 2020/10/15 2020/12/7 2021/4/8 2021/8/20 2022/4/21 2023/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "266", "girl": "leifang", "name": "春彩のスクールウェア(レイファン)", "zhs_name": "春色校服(丽凤)", "zht_name": "春色校服(麗鳳)", "en_name": "Springtime Schoolwear (Leifang)", "kr_name": "화사한 봄철 학생복(레이팡)", "type": "tec", "pow": "4114", "tec": "4982", "stm": "3646", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "閃きのテクニック6", "sell": "2019/11/7", "resell": "2020/4/14 2020/10/15 2020/12/7 2021/4/8 2021/8/20 2022/4/21 2023/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "267", "girl": "ayane", "name": "春彩のスクールウェア(あやね)", "zhs_name": "春色校服(绫音)", "zht_name": "春色校服(綾音)", "en_name": "Springtime Schoolwear (Ayane)", "kr_name": "화사한 봄철 학생복(아야네)", "type": "tec", "pow": "4114", "tec": "4982", "stm": "3646", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "閃きのテクニック6", "sell": "2019/11/7", "resell": "2020/4/14 2020/10/15 2020/12/7 2021/4/8 2021/8/20 2022/4/21 2023/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "268", "girl": "kanna", "name": "春彩のスクールウェア(カンナ)", "zhs_name": "春色校服(神无)", "zht_name": "春色校服(神無)", "en_name": "Springtime Schoolwear (Kanna)", "kr_name": "화사한 봄철 학생복(칸나)", "type": "tec", "pow": "4114", "tec": "4982", "stm": "3646", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "閃きのテクニック6", "sell": "2019/11/7", "resell": "2020/4/14 2020/10/15 2020/12/7 2021/4/8 2021/8/20 2022/4/21 2023/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "269_1", "girl": "honoka", "name": "メロウ・プルマージュ(ほのか)", "zhs_name": "玉柔羽衣(穗香)", "zht_name": "玉柔羽衣(穗香)", "en_name": "Mellow Plumage (Honoka)", "kr_name": "멜로우 플루메이지(호노카)", "type": "tec", "pow": "3944", "tec": "4952", "stm": "3696", "apl": "200", "skill1": "高度な心理戦F", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "2020/3/24", "break": "1", "special_fun": "游戏2周年庆服装，官方公告数值有错误(TEC 4852) 实际TEC为4952"
  },
  {
    "id": "269_2", "girl": "marie", "name": "メロウ・プルマージュ(マリー)", "zhs_name": "玉柔羽衣(玛莉)", "zht_name": "玉柔羽衣(瑪莉)", "en_name": "Mellow Plumage (Marie)", "kr_name": "멜로우 플루메이지(마리)", "type": "tec", "pow": "3944", "tec": "4952", "stm": "3696", "apl": "200", "skill1": "高度な心理戦F", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "2020/6/6", "break": "1", "special_fun": "游戏2周年庆服装，官方公告数值有错误(TEC 4852) 实际TEC为4952"
  },
  {
    "id": "269_3", "girl": "kokoro", "name": "メロウ・プルマージュ(こころ)", "zhs_name": "玉柔羽衣(心)", "zht_name": "玉柔羽衣(心)", "en_name": "Mellow Plumage (Kokoro)", "kr_name": "멜로우 플루메이지(코코로)", "type": "tec", "pow": "3944", "tec": "4952", "stm": "3696", "apl": "200", "skill1": "高度な心理戦F", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "2019/12/1", "break": "1", "special_fun": "游戏2周年庆服装，官方公告数值有错误(TEC 4852) 实际TEC为4952"
  },
  {
    "id": "269_4", "girl": "hitomi", "name": "メロウ・プルマージュ(ヒトミ)", "zhs_name": "玉柔羽衣(瞳)", "zht_name": "玉柔羽衣(瞳)", "en_name": "Mellow Plumage (Hitomi)", "kr_name": "멜로우 플루메이지(히토미)", "type": "tec", "pow": "3944", "tec": "4952", "stm": "3696", "apl": "200", "skill1": "高度な心理戦F", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "2020/5/25", "break": "1", "special_fun": "游戏2周年庆服装，官方公告数值有错误(TEC 4852) 实际TEC为4952"
  },
  {
    "id": "269_5", "girl": "misaki", "name": "メロウ・プルマージュ(みさき)", "zhs_name": "玉柔羽衣(海咲)", "zht_name": "玉柔羽衣(海咲)", "en_name": "Mellow Plumage (Misaki)", "kr_name": "멜로우 플루메이지(미사키)", "type": "tec", "pow": "3944", "tec": "4952", "stm": "3696", "apl": "200", "skill1": "高度な心理戦F", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "2020/7/7", "break": "1", "special_fun": "游戏2周年庆服装，官方公告数值有错误(TEC 4852) 实际TEC为4952"
  },
  {
    "id": "269_6", "girl": "luna", "name": "メロウ・プルマージュ(ルナ)", "zhs_name": "玉柔羽衣(露娜)", "zht_name": "玉柔羽衣(露娜)", "en_name": "Mellow Plumage (Luna)", "kr_name": "멜로우 플루메이지(루나)", "type": "tec", "pow": "3944", "tec": "4952", "stm": "3696", "apl": "200", "skill1": "高度な心理戦F", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "", "break": "1", "special_fun": "游戏2周年庆服装，官方公告数值有错误(TEC 4852) 实际TEC为4952"
  },
  {
    "id": "269_7", "girl": "fiona", "name": "メロウ・プルマージュ(フィオナ)", "zhs_name": "玉柔羽衣(菲欧娜)", "zht_name": "玉柔羽衣(菲歐娜)", "en_name": "Mellow Plumage (Fiona)", "kr_name": "멜로우 플루메이지(피오나)", "type": "tec", "pow": "3944", "tec": "4952", "stm": "3696", "apl": "200", "skill1": "高度な心理戦F", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "", "break": "1", "special_fun": "游戏2周年庆服装，官方公告数值有错误(TEC 4852) 实际TEC为4952"
  },
  {
    "id": "269_8", "girl": "kanna", "name": "メロウ・プルマージュ(カンナ)", "zhs_name": "玉柔羽衣(神无)", "zht_name": "玉柔羽衣(神無)", "en_name": "Mellow Plumage (Kanna)", "kr_name": "멜로우 플루메이지(칸나)", "type": "tec", "pow": "3944", "tec": "4952", "stm": "3696", "apl": "200", "skill1": "高度な心理戦F", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "", "break": "1", "special_fun": "游戏2周年庆服装，官方公告数值有错误(TEC 4852) 实际TEC为4952"
  },
  {
    "id": "270_1", "girl": "kasumi", "name": "グロリアス・プルマージュ(かすみ)", "zhs_name": "辉煌羽衣(霞)", "zht_name": "輝煌羽衣(霞)", "en_name": "Glorious Plumage (Kasumi)", "kr_name": "글로리어스 플루메이지(카스미)", "type": "tec", "pow": "3814", "tec": "4832", "stm": "3946", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "2020/2/23", "break": "1", "special_fun": "游戏2周年庆服装"
  },
  {
    "id": "270_2", "girl": "ayane", "name": "グロリアス・プルマージュ(あやね)", "zhs_name": "辉煌羽衣(绫音)", "zht_name": "輝煌羽衣(綾音)", "en_name": "Glorious Plumage (Ayane)", "kr_name": "글로리어스 플루메이지(아야네)", "type": "tec", "pow": "3814", "tec": "4832", "stm": "3946", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "2020/8/5", "break": "1", "special_fun": "游戏2周年庆服装"
  },
  {
    "id": "270_3", "girl": "nyotengu", "name": "グロリアス・プルマージュ(女天狗)", "zhs_name": "辉煌羽衣(女天狗)", "zht_name": "輝煌羽衣(女天狗)", "en_name": "Glorious Plumage (Nyotengu)", "kr_name": "글로리어스 플루메이지(뇨텐구)", "type": "tec", "pow": "3814", "tec": "4832", "stm": "3946", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "", "break": "1", "special_fun": "游戏2周年庆服装"
  },
  {
    "id": "270_4", "girl": "momiji", "name": "グロリアス・プルマージュ(紅葉)", "zhs_name": "辉煌羽衣(红叶)", "zht_name": "輝煌羽衣(紅葉)", "en_name": "Glorious Plumage (Momiji)", "kr_name": "글로리어스 플루메이지(모미지)", "type": "tec", "pow": "3814", "tec": "4832", "stm": "3946", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "2020/9/20", "break": "1", "special_fun": "游戏2周年庆服装"
  },
  {
    "id": "270_5", "girl": "helena", "name": "グロリアス・プルマージュ(エレナ)", "zhs_name": "辉煌羽衣(海莲娜)", "zht_name": "輝煌羽衣(海蓮娜)", "en_name": "Glorious Plumage (Helena)", "kr_name": "글로리어스 플루메이지(엘레나)", "type": "tec", "pow": "3814", "tec": "4832", "stm": "3946", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "2020/1/30", "break": "1", "special_fun": "游戏2周年庆服装"
  },
  {
    "id": "270_6", "girl": "tamaki", "name": "グロリアス・プルマージュ(たまき)", "zhs_name": "辉煌羽衣(环)", "zht_name": "輝煌羽衣(環)", "en_name": "Glorious Plumage (Tamaki)", "kr_name": "글로리어스 플루메이지(타마키)", "type": "tec", "pow": "3814", "tec": "4832", "stm": "3946", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "", "break": "1", "special_fun": "游戏2周年庆服装"
  },
  {
    "id": "270_7", "girl": "leifang", "name": "グロリアス・プルマージュ(レイファン)", "zhs_name": "辉煌羽衣(丽凤)", "zht_name": "輝煌羽衣(麗鳳)", "en_name": "Glorious Plumage (Leifang)", "kr_name": "글로리어스 플루메이지(레이팡)", "type": "tec", "pow": "3814", "tec": "4832", "stm": "3946", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "", "break": "1", "special_fun": "游戏2周年庆服装"
  },
  {
    "id": "270_8", "girl": "nagisa", "name": "グロリアス・プルマージュ(なぎさ)", "zhs_name": "辉煌羽衣(凪咲)", "zht_name": "輝煌羽衣(凪咲)", "en_name": "Glorious Plumage (Nagisa)", "kr_name": "글로리어스 플루메이지(나기사)", "type": "tec", "pow": "3814", "tec": "4832", "stm": "3946", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "乙姫のテクニック", "skill3": "可憐なフェイント", "sell": "2019/11/14", "resell": "", "break": "1", "special_fun": "游戏2周年庆服装"
  },
  {
    "id": "271", "girl": "nyotengu", "name": "ジュエル・トパーズ(女天狗)", "zhs_name": "珍宝・黄玉(女天狗)", "zht_name": "珍寶‧黃玉(女天狗)", "en_name": "Jewel Topaz (Nyotengu)", "kr_name": "주얼 토파즈(뇨텐구)", "type": "stm", "pow": "4614", "tec": "3406", "stm": "5322", "apl": "200", "skill1": "強烈スパイクE", "skill2": "トパーズ・スタミナ", "skill3": "豪快なスパイク", "sell": "2019/11/19", "resell": "2020/10/29 2020/11/19 2021/11/19 2022/11/19", "break": "1", "special_fun": "第二套宝石主题生日。红黄绿 策划一家人就是要整整齐齐，半个月前，前脚刚复刻去年生日。后脚马上今年生日保底就加入去年生日，。5单脸不黑到底2件打包带走，半个月前抽的意义是什么。白给5单的钱？"
  },
  {
    "id": "103_8", "girl": "nagisa", "name": "ファースト・ルージュ(なぎさ)", "zhs_name": "嫣红桂冠(凪咲)", "zht_name": "嫣紅桂冠(凪咲)", "en_name": "First Rouge (Nagisa)", "kr_name": "퍼스트 루주(나기사)", "type": "pow", "pow": "4852", "tec": "3954", "stm": "4044", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2019/11/23", "resell": "2020/11/24 2023/5/19", "break": "1", "special_fun": "[2周年庆复刻池新增] 游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "103_9", "girl": "kanna", "name": "ファースト・ルージュ(カンナ)", "zhs_name": "嫣红桂冠(神无)", "zht_name": "嫣紅桂冠(神無)", "en_name": "First Rouge (Kanna)", "kr_name": "퍼스트 루주(칸나)", "type": "pow", "pow": "4852", "tec": "3954", "stm": "4044", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2019/11/23", "resell": "2020/3/5 2020/11/24 2023/5/19", "break": "1", "special_fun": "[2周年庆复刻池新增] 游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "105_7", "girl": "fiona", "name": "プレミア・ナイト(フィオナ)", "zhs_name": "典藏之夜(菲欧娜)", "zht_name": "典藏之夜(菲歐娜)", "en_name": "Premier Night (Fiona)", "kr_name": "프리미어 나이트(피오나)", "type": "pow", "pow": "4782", "tec": "4004", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2019/11/23", "resell": "2020/11/24 2023/5/19", "break": "1", "special_fun": "[2周年庆复刻池新增] 游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "105_8", "girl": "monica", "name": "プレミア・ナイト(モニカ)", "zhs_name": "典藏之夜(莫妮卡)", "zht_name": "典藏之夜(莫妮卡)", "en_name": "Premier Night (Monica)", "kr_name": "프리미어 나이트(모니카)", "type": "pow", "pow": "4782", "tec": "4004", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2019/11/23", "resell": "2020/3/5 2020/11/24 2023/5/19", "break": "1", "special_fun": "[2周年庆复刻池新增] 游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "272", "girl": "monica", "name": "プレイスユアベット(モニカ)", "zhs_name": "下注(莫妮卡)", "zht_name": "下注(莫妮卡)", "en_name": "Place-Your-Bet (Monica)", "kr_name": "플레이스 유어 베팅(모니카)", "type": "pow", "pow": "5002", "tec": "4014", "stm": "3984", "apl": "200", "skill1": "強烈スパイクC", "skill2": "高度な心理戦D", "skill3": "秘められたパワー6", "sell": "2019/11/23", "resell": "2020/5/22 2020/9/3", "break": "1", "special_fun": ""
  },
  {
    "id": "273", "girl": "luna", "name": "プレイスユアベット(ルナ)", "zhs_name": "下注(露娜)", "zht_name": "下注(露娜)", "en_name": "Place-Your-Bet (Luna)", "kr_name": "플레이스 유어 베팅(루나)", "type": "pow", "pow": "4912", "tec": "3924", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー6", "skill3": "豪快なスパイク", "sell": "2019/11/23", "resell": "2020/5/22 2020/9/3", "break": "1", "special_fun": ""
  },
  {
    "id": "c0", "girl": "all", "name": "第１回水着コンテスト「キュート」", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "none", "pow": "0", "tec": "0", "stm": "0", "apl": "0", "skill1": "", "skill2": "", "skill3": "", "sell": "2019/11/23", "resell": "N/A", "break": "1", "special_fun": "帽子可以隐藏。第一次服装设计比赛 得奖作品。作为礼包3000付费钻 两件打包销售 仅外形无属性。Design by しんじこ"
  },
  {
    "id": "c1", "girl": "all", "name": "第１回水着コンテスト「セクシー」", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "none", "pow": "0", "tec": "0", "stm": "0", "apl": "0", "skill1": "", "skill2": "", "skill3": "", "sell": "2019/11/23", "resell": "N/A", "break": "1", "special_fun": "第一次服装设计比赛 得奖作品。作为礼包3000付费钻 两件打包销售 仅外形无属性。Design by morotomo"
  },
  {
    "id": "274_1", "girl": "marie", "name": "そよかぜのロンド(マリー)", "zhs_name": "微风回旋曲(玛莉)", "zht_name": "微風迴旋曲(瑪莉)", "en_name": "Breezy Dance (Marie)", "kr_name": "산들바람 론도(마리)", "type": "pow", "pow": "4952", "tec": "3994", "stm": "4054", "apl": "200", "skill1": "強烈スパイクE", "skill2": "驚異のスタミナE", "skill3": "秘められたパワー6", "sell": "2019/11/29", "resell": "2020/12/4 2021/5/6 2023/7/5", "break": "1", "special_fun": ""
  },
  {
    "id": "274_2", "girl": "hitomi", "name": "そよかぜのロンド(ヒトミ)", "zhs_name": "微风回旋曲(瞳)", "zht_name": "微風迴旋曲(瞳)", "en_name": "Breezy Dance (Hitomi)", "kr_name": "산들바람 론도(히토미)", "type": "pow", "pow": "4952", "tec": "3994", "stm": "4054", "apl": "200", "skill1": "強烈スパイクE", "skill2": "驚異のスタミナE", "skill3": "秘められたパワー6", "sell": "2019/11/29", "resell": "2020/12/4 2021/5/6 2023/7/5", "break": "1", "special_fun": ""
  },
  {
    "id": "274_3", "girl": "leifang", "name": "そよかぜのロンド(レイファン)", "zhs_name": "微风回旋曲(丽凤)", "zht_name": "微風迴旋曲(麗鳳)", "en_name": "Breezy Dance (Leifang)", "kr_name": "산들바람 론도(레이팡)", "type": "pow", "pow": "4952", "tec": "3994", "stm": "4054", "apl": "200", "skill1": "強烈スパイクE", "skill2": "驚異のスタミナE", "skill3": "秘められたパワー6", "sell": "2019/11/29", "resell": "2020/12/4 2021/5/6 2023/7/5", "break": "1", "special_fun": ""
  },
  {
    "id": "274_4", "girl": "kanna", "name": "そよかぜのロンド(カンナ)", "zhs_name": "微风回旋曲(神无)", "zht_name": "微風迴旋曲(神無)", "en_name": "Breezy Dance (Kanna)", "kr_name": "산들바람 론도(칸나)", "type": "pow", "pow": "4932", "tec": "3834", "stm": "4134", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2019/11/29", "resell": "2020/12/4 2021/5/6 2023/7/5", "break": "1", "special_fun": ""
  },
  {
    "id": "275", "girl": "kokoro", "name": "ジュエル・ラピスラズリ(こころ)", "zhs_name": "珍宝‧青金石(心)", "zht_name": "珍寶・青金石(心)", "en_name": "Jewel Lapis Lazuli (Kokoro)", "kr_name": "주얼 라피스 라즐리(코코로)", "type": "stm", "pow": "3376", "tec": "4644", "stm": "5322", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ラピスラズリ・スタミナ", "skill3": "可憐なフェイント", "sell": "2019/12/1", "resell": "2020/10/29 2020/12/1 2021/12/1 2022/12/1", "break": "1", "special_fun": "是川澄绫子声优太贵，还是KT策划被黑长直绿了。策划恶意针对角色出的什么垃圾！草泥马的黑长直做错了什么，不是背锅绿茶婊就是被当作打击报复对象。"
  },
  {
    "id": "276", "girl": "kasumi", "name": "プラチナ・ネモフィラ(かすみ)", "zhs_name": "白金粉蝶花(霞)", "zht_name": "白金粉蝶花(霞)", "en_name": "Platinum Nemophila (Kasumi)", "kr_name": "플래티넘 네모필라(카스미)", "type": "tec", "pow": "3904", "tec": "4942", "stm": "3796", "apl": "200", "skill1": "高度な心理戦E", "skill2": "内から湧き上がるスタミナ6", "skill3": "可憐なフェイント", "sell": "2019/12/5", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "277", "girl": "ayane", "name": "プラチナ・フィルギャ(あやね)", "zhs_name": "白金费尔加(绫音)", "zht_name": "白金守伴者(綾音)", "en_name": "Platinum Fylgja (Ayane)", "kr_name": "플래티넘 필갸(아야네)", "type": "tec", "pow": "4094", "tec": "5042", "stm": "3606", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "驚異のスタミナD", "skill3": "閃きのテクニック6", "sell": "2019/12/5", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "278", "girl": "sayuri", "name": "ミルキーララバイ(さゆり)", "zhs_name": "温柔摇篮曲(小百合)", "zht_name": "溫柔搖籃曲(小百合)", "en_name": "Milky Lullaby (Sayuri)", "kr_name": "밀키 럴러바이(사유리)", "type": "stm", "pow": "3596", "tec": "4344", "stm": "5102", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦B", "skill3": "内から湧き上がるスタミナ3", "sell": "2019/12/5", "resell": "2020/3/31 2022/12/5", "break": "1", "special_fun": ""
  },
  {
    "id": "279", "girl": "fiona", "name": "しらゆきのあさり(フィオナ)", "zhs_name": "白雪之贝(菲欧娜)", "zht_name": "白雪之貝(菲歐娜)", "en_name": "SnowWhiteSet(Fiona)", "kr_name": "백설조개잡이(피오나)", "type": "tec", "pow": "4014", "tec": "5072", "stm": "3656", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "高度な心理戦C", "skill3": "閃きのテクニック6", "sell": "2019/12/11", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "280", "girl": "kokoro", "name": "しらゆきのあさり(こころ)", "zhs_name": "白雪之贝(心)", "zht_name": "白雪之貝(心)", "en_name": "SnowWhiteSet(Kokoro)", "kr_name": "백설조개잡이(코코로)", "type": "tec", "pow": "4014", "tec": "5072", "stm": "3656", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "高度な心理戦C", "skill3": "閃きのテクニック6", "sell": "2019/12/11", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "281", "girl": "helena", "name": "まよなかのあさり(エレナ)", "zhs_name": "深宵之贝(海莲娜)", "zht_name": "深宵之貝(海蓮娜)", "en_name": "DuskSet(Helena)", "kr_name": "자정조개잡이(엘레나)", "type": "tec", "pow": "4044", "tec": "4922", "stm": "3676", "apl": "200", "skill1": "高度な心理戦D", "skill2": "閃きのテクニック5", "skill3": "可憐なフェイント", "sell": "2019/12/11", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "282_1", "girl": "fiona", "name": "ホーリースノウ(フィオナ)", "zhs_name": "圣洁之雪(菲欧娜)", "zht_name": "聖潔之雪(菲歐娜)", "en_name": "Holy Snow (Fiona)", "kr_name": "홀리 스노우(피오나)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/12/16 2020/12/22 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_2", "girl": "monica", "name": "ホーリースノウ(モニカ)", "zhs_name": "圣洁之雪(莫妮卡)", "zht_name": "聖潔之雪(莫妮卡)", "en_name": "Holy Snow (Monica)", "kr_name": "홀리 스노우", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/12/16 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_3", "girl": "misaki", "name": "ホーリースノウ(みさき)", "zhs_name": "圣洁之雪(海咲)", "zht_name": "聖潔之雪(海咲)", "en_name": "Holy Snow (Misaki)", "kr_name": "홀리 스노우(미사키)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/7/7 2020/12/16 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_4", "girl": "marie", "name": "ホーリースノウ(マリー)", "zhs_name": "圣洁之雪(玛莉)", "zht_name": "聖潔之雪(瑪莉)", "en_name": "Holy Snow (Marie)", "kr_name": "홀리 스노우(마리)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/6/6 2020/12/16 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_5", "girl": "honoka", "name": "ホーリースノウ(ほのか)", "zhs_name": "圣洁之雪(穗香)", "zht_name": "聖潔之雪(穗香)", "en_name": "Holy Snow (Honoka)", "kr_name": "홀리 스노우(호노카)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/3/24 2020/12/16 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_6", "girl": "kasumi", "name": "ホーリースノウ(かすみ)", "zhs_name": "圣洁之雪(霞)", "zht_name": "聖潔之雪(霞)", "en_name": "Holy Snow (Kasumi)", "kr_name": "홀리 스노우(카스미)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/2/23 2020/12/16 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_7", "girl": "hitomi", "name": "ホーリースノウ(ヒトミ)", "zhs_name": "圣洁之雪(瞳)", "zht_name": "聖潔之雪(瞳)", "en_name": "Holy Snow (Hitomi)", "kr_name": "홀리 스노우(히토미)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/5/25 2020/12/16 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_8", "girl": "helena", "name": "ホーリースノウ(エレナ)", "zhs_name": "圣洁之雪(海莲娜)", "zht_name": "聖潔之雪(海蓮娜)", "en_name": "Holy Snow (Helena)", "kr_name": "홀리 스노우(엘레나)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/1/30 2020/12/16 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_9", "girl": "leifang", "name": "ホーリースノウ(レイファン)", "zhs_name": "圣洁之雪(丽凤)", "zht_name": "聖潔之雪(麗鳳)", "en_name": "Holy Snow (Leifang)", "kr_name": "홀리 스노우(레이팡)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/12/16 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_10", "girl": "tamaki", "name": "ホーリースノウ(たまき)", "zhs_name": "圣洁之雪(环)", "zht_name": "聖潔之雪(環)", "en_name": "Holy Snow (Tamaki)", "kr_name": "홀리 스노우(타마키)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/12/22 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_11", "girl": "nagisa", "name": "ホーリースノウ(なぎさ)", "zhs_name": "圣洁之雪(凪咲)", "zht_name": "聖潔之雪(凪咲)", "en_name": "Holy Snow (Nagisa)", "kr_name": "홀리 스노우(나기사)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/12/22 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_12", "girl": "nyotengu", "name": "ホーリースノウ(女天狗)", "zhs_name": "圣洁之雪(女天狗)", "zht_name": "聖潔之雪(女天狗)", "en_name": "Holy Snow (Nyotengu)", "kr_name": "홀리 스노우(뇨텐구)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/12/22 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_13", "girl": "ayane", "name": "ホーリースノウ(あやね)", "zhs_name": "圣洁之雪(绫音)", "zht_name": "聖潔之雪(綾音)", "en_name": "Holy Snow (Ayane)", "kr_name": "홀리 스노우(아야네)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/8/5 2020/12/22 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_14", "girl": "kokoro", "name": "ホーリースノウ(こころ)", "zhs_name": "圣洁之雪(心)", "zht_name": "聖潔之雪(心)", "en_name": "Holy Snow (Kokoro)", "kr_name": "홀리 스노우(코코로)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/12/22 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_15", "girl": "luna", "name": "ホーリースノウ(ルナ)", "zhs_name": "圣洁之雪(露娜)", "zht_name": "聖潔之雪(露娜)", "en_name": "Holy Snow (Luna)", "kr_name": "홀리 스노우(루나)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/12/22 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_16", "girl": "momiji", "name": "ホーリースノウ(紅葉)", "zhs_name": "圣洁之雪(红叶)", "zht_name": "聖潔之雪(紅葉)", "en_name": "Holy Snow (Momiji)", "kr_name": "홀리 스노우(모미지)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/9/20 2020/12/22 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "282_17", "girl": "kanna", "name": "ホーリースノウ(カンナ)", "zhs_name": "圣洁之雪(神无)", "zht_name": "聖潔之雪(神無)", "en_name": "Holy Snow (Kanna)", "kr_name": "홀리 스노우(칸나)", "type": "pow", "pow": "4952", "tec": "3696", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "雪華のパワー", "sell": "2019/12/17", "resell": "2020/12/22 2022/12/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现飘雪效果 爆衣有碎冰声)"
  },
  {
    "id": "111_14", "girl": "fiona", "name": "フレーズノエル(フィオナ)", "zhs_name": "草莓圣诞(菲欧娜)", "zht_name": "草莓聖誕(菲歐娜)", "en_name": "Noël aux Fraises (Fiona)", "kr_name": "프레이즈 노엘(피오나)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2019/12/20", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_15", "girl": "nagisa", "name": "フレーズノエル(なぎさ)", "zhs_name": "草莓圣诞(凪咲)", "zht_name": "草莓聖誕(凪咲)", "en_name": "Noël aux Fraises (Nagisa)", "kr_name": "프레이즈 노엘(나기사)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2019/12/20", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_16", "girl": "kanna", "name": "フレーズノエル(カンナ)", "zhs_name": "草莓圣诞(神无)", "zht_name": "草莓聖誕(神無)", "en_name": "Noël aux Fraises (Kanna)", "kr_name": "프레이즈 노엘(칸나)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2019/12/20", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_17", "girl": "monica", "name": "フレーズノエル(モニカ)", "zhs_name": "草莓圣诞(莫妮卡)", "zht_name": "草莓圣诞(莫妮卡)", "en_name": "Noël aux Fraises (Monica)", "kr_name": "프레이즈 노엘(모니카)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2019/12/20", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "283", "girl": "tamaki", "name": "振袖・山瑠璃(たまき)", "zhs_name": "振袖·山琉璃(环)", "zht_name": "振袖‧山琉璃(環)", "en_name": "Yamaruri Kimono (Tamaki)", "kr_name": "후리소데(산유리)(타마키)", "type": "stm", "pow": "3836", "tec": "4394", "stm": "4912", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "高度な心理戦B", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/12/26", "resell": "2022/1/1 2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "284", "girl": "hitomi", "name": "振袖・春菘(ヒトミ)", "zhs_name": "振袖·春菘(瞳)", "zht_name": "振袖‧春菘(瞳)", "en_name": "Spring's Bells Kimono (Hitomi)", "kr_name": "후리소데(춘련)(히토미)", "type": "stm", "pow": "3786", "tec": "4414", "stm": "4942", "apl": "200", "skill1": "灼熱のダンスD", "skill2": "裏の裏を突くフェイントE", "skill3": "内から湧き上がるスタミナ6", "sell": "2019/12/26", "resell": "2022/1/1 2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "285", "girl": "leifang", "name": "振袖・唐紅(レイファン)", "zhs_name": "振袖·唐红(丽凤)", "zht_name": "振袖‧唐紅(麗鳳)", "en_name": "Crimson Kimono (Leifang)", "kr_name": "후리소데(진다홍)(레이팡)", "type": "stm", "pow": "3556", "tec": "4344", "stm": "5142", "apl": "200", "skill1": "高度な心理戦A", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2019/12/26", "resell": "2022/1/1 2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "286", "girl": "sayuri", "name": "キュア・エンジェル(さゆり)", "zhs_name": "治愈天使(小百合)", "zht_name": "治愈天使(小百合)", "en_name": "Cure Angel (Sayuri)", "kr_name": "큐어 엔젤(사유리)", "type": "tec", "pow": "3814", "tec": "4802", "stm": "4126", "apl": "200", "skill1": "高度な心理戦B", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2019/12/26", "resell": "2020/3/31 2022/12/5", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以隐藏"
  },
  {
    "id": "287", "girl": "monica", "name": "ジュエル・ガーネット(モニカ)", "zhs_name": "珍宝・石榴石(莫妮卡)", "zht_name": "珍寶・石榴石(莫妮卡)", "en_name": "Jewel Garnet (Monica)", "kr_name": "주얼 가넷(모니카)", "type": "stm", "pow": "3326", "tec": "4694", "stm": "5322", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ガーネット・スタミナ", "skill3": "可憐なフェイント", "sell": "2020/1/1", "resell": "2020/10/29 2021/1/1 2023/1/1", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现红色粒子效果(光之舞)"
  },
  {
    "id": "288", "girl": "monica", "name": "ステラ・カプリコーン(モニカ)", "zhs_name": "星辰‧魔羯(莫妮卡)", "zht_name": "星辰・摩羯(莫妮卡)", "en_name": "Stellar Capricorn (Monica)", "kr_name": "스텔라 캐프리콘(모니카)", "type": "tec", "pow": "3914", "tec": "5322", "stm": "3706", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "カプリコーン・テクニック", "skill3": "可憐なフェイント", "sell": "2020/1/1", "resell": "2021/1/1 2021/9/16 2022/9/8 2023/1/1", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现红色粒子效果(光之舞)"
  },
  {
    "id": "289", "girl": "marie", "name": "瑞雲の千早(マリー)", "zhs_name": "瑞云千早(玛莉)", "zht_name": "瑞雲千早(瑪莉)", "en_name": "Auspicious Shrine Robe (Marie)", "kr_name": "서운의 치하야(마리)", "type": "tec", "pow": "3794", "tec": "4732", "stm": "4116", "apl": "200", "skill1": "高度な心理戦E", "skill2": "閃きのテクニック5", "skill3": "可憐なフェイント", "sell": "2020/1/2", "resell": "2020/11/26 2021/1/4 2021/12/29 2023/1/5", "break": "1", "special_fun": ""
  },
  {
    "id": "290", "girl": "nagisa", "name": "瑞雲の千早(なぎさ)", "zhs_name": "瑞云千早(凪咲)", "zht_name": "瑞雲千早(凪咲)", "en_name": "Auspicious Shrine Robe (Nagisa)", "kr_name": "서운의 치하야(나기사)", "type": "tec", "pow": "3924", "tec": "4642", "stm": "4176", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦B", "skill3": "閃きのテクニック6", "sell": "2020/1/2", "resell": "2020/11/26 2021/1/4 2021/12/29 2023/1/5", "break": "1", "special_fun": ""
  },
  {
    "id": "291", "girl": "kanna", "name": "瑞雲の千早(カンナ)", "zhs_name": "瑞云千早(神无)", "zht_name": "瑞雲千早(神無)", "en_name": "Auspicious Shrine Robe (Kanna)", "kr_name": "서운의 치하야(칸나)", "type": "tec", "pow": "3924", "tec": "4642", "stm": "4176", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦B", "skill3": "閃きのテクニック6", "sell": "2020/1/2", "resell": "2020/11/26 2021/1/4 2021/12/29 2023/1/5", "break": "1", "special_fun": ""
  },
  {
    "id": "292", "girl": "misaki", "name": "幻燈朱雀(みさき)", "zhs_name": "幻灯朱雀(海咲)", "zht_name": "幻燈朱雀(海咲)", "en_name": "Vermilion Bird Mirage (Misaki)", "kr_name": "환등주작(미사키)", "type": "stm", "pow": "4514", "tec": "3606", "stm": "4922", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2020/1/9", "resell": "2022/5/18", "break": "1", "special_fun": ""
  },
  {
    "id": "293", "girl": "nyotengu", "name": "幻燈黒竜(女天狗)", "zhs_name": "幻灯黑龙(女天狗)", "zht_name": "幻燈黑龍(女天狗)", "en_name": "Black Dragon Mirage (Nyotengu)", "kr_name": "환등흑룡(뇨텐구)", "type": "pow", "pow": "5152", "tec": "3734", "stm": "4114", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーD", "skill3": "秘められたパワー6", "sell": "2020/1/9", "resell": "2022/5/18", "break": "1", "special_fun": ""
  },
  {
    "id": "294", "girl": "honoka", "name": "えいりあんハート(ほのか)", "zhs_name": "外星人之心(穗香)", "zht_name": "外星人之心(穗香)", "en_name": "Alien Heart (Honoka)", "kr_name": "에일리언 하트(호노카)", "type": "tec", "pow": "3714", "tec": "4702", "stm": "4226", "apl": "200", "skill1": "高度な心理戦E", "skill2": "閃きのテクニック5", "skill3": "可憐なフェイント", "sell": "2020/1/16", "resell": "2020/7/16 2020/12/3", "break": "1", "special_fun": "触摸妹子可以改变胸前显示的图案，不同位置改变速度不同。配套头饰亦可以触摸点灯 / 发射动感光波"
  },
  {
    "id": "295", "girl": "luna", "name": "えいりあんハート(ルナ)", "zhs_name": "外星人之心(露娜)", "zht_name": "外星人之心(露娜)", "en_name": "Alien Heart (Luna)", "kr_name": "에일리언 하트(루나)", "type": "tec", "pow": "3624", "tec": "4872", "stm": "4246", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "驚異のスタミナC", "skill3": "閃きのテクニック6", "sell": "2020/1/16", "resell": "2020/7/16 2020/12/3", "break": "1", "special_fun": "触摸妹子可以改变胸前显示的图案，不同位置改变速度不同。配套头饰亦可以触摸点灯 / 发射动感光波"
  },
  {
    "id": "296", "girl": "monica", "name": "シークレットクラス(モニカ)", "zhs_name": "秘密课堂(莫妮卡)", "zht_name": "秘密課堂(莫妮卡)", "en_name": "Secret Class (Monica)", "kr_name": "시크릿 클래스(모니카)", "type": "pow", "pow": "5002", "tec": "3824", "stm": "3916", "apl": "200", "skill1": "強烈スパイクB", "skill2": "灼熱のダンスC", "skill3": "秘められたパワー6", "sell": "2020/1/22", "resell": "2020/9/10 2020/11/28 2022/1/24 2022/4/25", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "297", "girl": "tamaki", "name": "シークレットクラス(たまき)", "zhs_name": "秘密课堂(环)", "zht_name": "秘密課堂(環)", "en_name": "Secret Class (Tamaki)", "kr_name": "시크릿 클래스(타마키)", "type": "pow", "pow": "5002", "tec": "3824", "stm": "3916", "apl": "200", "skill1": "強烈スパイクB", "skill2": "灼熱のダンスC", "skill3": "秘められたパワー6", "sell": "2020/1/22", "resell": "2020/9/10 2020/11/28 2022/1/24 2022/4/25", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "298", "girl": "momiji", "name": "シークレットクラス(紅葉)", "zhs_name": "秘密课堂(红叶)", "zht_name": "秘密課堂(紅葉)", "en_name": "Secret Class (Momiji)", "kr_name": "시크릿 클래스(모미지)", "type": "pow", "pow": "4842", "tec": "3874", "stm": "3926", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2020/1/22", "resell": "2020/9/10 2020/11/28 2022/1/24 2022/4/25", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "299", "girl": "kasumi", "name": "シークレットクラス(かすみ)", "zhs_name": "秘密课堂(霞)", "zht_name": "秘密課堂(霞)", "en_name": "Secret Class (Kasumi)", "kr_name": "시크릿 클래스(카스미)", "type": "pow", "pow": "5002", "tec": "3824", "stm": "3916", "apl": "200", "skill1": "強烈スパイクB", "skill2": "灼熱のダンスC", "skill3": "秘められたパワー6", "sell": "2020/1/22", "resell": "2020/9/10 2020/11/28 2022/1/24 2022/4/25", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "300_1", "girl": "misaki", "name": "ライザ・お気に入りの普段着(みさき)", "zhs_name": "莱莎・喜欢的日常装束(海咲)", "zht_name": "萊莎‧喜歡的日常裝束(海咲)", "en_name": "Ryza's Favorite Outfit (Misaki)", "kr_name": "라이자・좋아하는 평상복(미사키)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2020/1/29", "resell": "2021/1/19 2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ ～常暗の女王と秘密の隠れ家～(莱莎的炼金工房)联动服装 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_2", "girl": "luna", "name": "ライザ・お気に入りの普段着(ルナ)", "zhs_name": "莱莎・喜欢的日常装束(露娜)", "zht_name": "萊莎‧喜歡的日常裝束(露娜)", "en_name": "Ryza's Favorite Outfit (Luna)", "kr_name": "라이자・좋아하는 평상복(루나)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2020/1/29", "resell": "2021/1/19 2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ ～常暗の女王と秘密の隠れ家～(莱莎的炼金工房)联动服装 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_3", "girl": "tamaki", "name": "ライザ・お気に入りの普段着(たまき)", "zhs_name": "莱莎・喜欢的日常装束(环)", "zht_name": "萊莎‧喜歡的日常裝束(環)", "en_name": "Ryza's Favorite Outfit (Tamaki)", "kr_name": "라이자・좋아하는 평상복(타마키)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2020/1/29", "resell": "2021/1/19 2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ ～常暗の女王と秘密の隠れ家～(莱莎的炼金工房)联动服装 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_4", "girl": "fiona", "name": "ライザ・お気に入りの普段着(フィオナ)", "zhs_name": "莱莎・喜欢的日常装束(菲欧娜)", "zht_name": "萊莎‧喜歡的日常裝束(菲歐娜)", "en_name": "Ryza's Favorite Outfit (Fiona)", "kr_name": "라이자・좋아하는 평상복(피오나)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2020/1/29", "resell": "2021/1/19 2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ ～常暗の女王と秘密の隠れ家～(莱莎的炼金工房)联动服装 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_5", "girl": "nagisa", "name": "ライザ・お気に入りの普段着(なぎさ)", "zhs_name": "莱莎・喜欢的日常装束(凪咲)", "zht_name": "萊莎‧喜歡的日常裝束(凪咲)", "en_name": "Ryza's Favorite Outfit (Nagisa)", "kr_name": "라이자・좋아하는 평상복(나기사)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2020/1/29", "resell": "2021/1/19 2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ ～常暗の女王と秘密の隠れ家～(莱莎的炼金工房)联动服装 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_6", "girl": "kanna", "name": "ライザ・お気に入りの普段着(カンナ)", "zhs_name": "莱莎・喜欢的日常装束(神无)", "zht_name": "萊莎‧喜歡的日常裝束(神無)", "en_name": "Ryza's Favorite Outfit (Kanna)", "kr_name": "라이자・좋아하는 평상복(칸나)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2020/1/29", "resell": "2021/1/19 2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ ～常暗の女王と秘密の隠れ家～(莱莎的炼金工房)联动服装 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_7", "girl": "monica", "name": "ライザ・お気に入りの普段着(モニカ)", "zhs_name": "莱莎・喜欢的日常装束(莫妮卡)", "zht_name": "萊莎‧喜歡的日常裝束(莫妮卡)", "en_name": "Ryza's Favorite Outfit (Monica)", "kr_name": "라이자・좋아하는 평상복(모니카)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2020/1/29", "resell": "2021/1/19 2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ ～常暗の女王と秘密の隠れ家～(莱莎的炼金工房)联动服装 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "301", "girl": "helena", "name": "ジュエル・ガーネット(エレナ)", "zhs_name": "珍宝・石榴石(海莲娜)", "zht_name": "珍寶・石榴石(海蓮娜)", "en_name": "Jewel Garnet (Helena)", "kr_name": "주얼 가넷(엘레나)", "type": "stm", "pow": "3326", "tec": "4694", "stm": "5322", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ガーネット・スタミナ", "skill3": "可憐なフェイント", "sell": "2020/1/30", "resell": "2020/10/29 2021/1/30 2022/1/30 2023/1/30", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现紫色粒子效果(光之舞)"
  },
  {
    "id": "302", "girl": "kanna", "name": "鬼福招来(カンナ)", "zhs_name": "鬼福招来(神无)", "zht_name": "鬼福招來(神無)", "en_name": "Ogre's Fortune (Kanna)", "kr_name": "귀복초래(칸나)", "type": "apl", "pow": "3796", "tec": "4606", "stm": "4124", "apl": "550", "skill1": "裏の裏を突くフェイントA", "skill2": "観客総立ちF", "skill3": "隠しきれない魅力6", "sell": "2020/2/3", "resell": "2020/12/2 2021/1/28 2022/2/3 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "303", "girl": "ayane", "name": "鬼福招来(あやね)", "zhs_name": "鬼福招来(绫音)", "zht_name": "鬼福招來(綾音)", "en_name": "Ogre's Fortune (Ayane)", "kr_name": "귀복초래(아야네)", "type": "apl", "pow": "3756", "tec": "4446", "stm": "4224", "apl": "550", "skill1": "高度な心理戦E", "skill2": "隠しきれない魅力5", "skill3": "可憐なフェイント", "sell": "2020/2/3", "resell": "2020/12/2 2021/1/28 2022/2/3 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "304", "girl": "leifang", "name": "鬼福招来(レイファン)", "zhs_name": "鬼福招来(丽凤)", "zht_name": "鬼福招來(麗鳳)", "en_name": "Ogre's Fortune (Leifang)", "kr_name": "귀복초래(레이팡)", "type": "apl", "pow": "3796", "tec": "4606", "stm": "4124", "apl": "550", "skill1": "裏の裏を突くフェイントA", "skill2": "観客総立ちF", "skill3": "隠しきれない魅力6", "sell": "2020/2/3", "resell": "2020/12/2 2021/1/28 2022/2/3 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "305", "girl": "fiona", "name": "ジュエル・アメジスト(フィオナ)", "zhs_name": "珍宝・紫水晶(菲欧娜)", "zht_name": "珍寶‧紫水晶(菲歐娜)", "en_name": "Jewel Amethyst (Fiona)", "kr_name": "주얼 자수정(피오나)", "type": "stm", "pow": "3356", "tec": "4664", "stm": "5322", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "アメジスト・スタミナ", "skill3": "可憐なフェイント", "sell": "2020/2/11", "resell": "2020/10/29 2021/2/11 2022/2/11 2023/2/11", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现紫色粒子效果(光之舞) 濡湿会使衣服变色"
  },
  {
    "id": "306_1", "girl": "kasumi", "name": "スイート・ショコラティエ(かすみ)", "zhs_name": "甜心巧克力师(霞)", "zht_name": "甜心巧克力師(霞)", "en_name": "Sweet Chocolatier (Kasumi)", "kr_name": "스위트・쇼콜라티에(카스미)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_2", "girl": "honoka", "name": "スイート・ショコラティエ(ほのか)", "zhs_name": "甜心巧克力师(穗香)", "zht_name": "甜心巧克力師(穗香)", "en_name": "Sweet Chocolatier (Honoka)", "kr_name": "스위트・쇼콜라티에(호노카)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2020/3/24 2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_3", "girl": "marie", "name": "スイート・ショコラティエ(マリー)", "zhs_name": "甜心巧克力师(玛莉)", "zht_name": "甜心巧克力師(瑪莉)", "en_name": "Sweet Chocolatier (Marie)", "kr_name": "스위트・쇼콜라티에(마리)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2020/6/6 2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_4", "girl": "ayane", "name": "スイート・ショコラティエ(あやね)", "zhs_name": "甜心巧克力师(绫音)", "zht_name": "甜心巧克力師(綾音)", "en_name": "Sweet Chocolatier (Ayane)", "kr_name": "스위트・쇼콜라티에(아야네)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2020/8/5 2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_5", "girl": "nyotengu", "name": "スイート・ショコラティエ(女天狗)", "zhs_name": "甜心巧克力师(女天狗)", "zht_name": "甜心巧克力師(女天狗)", "en_name": "Sweet Chocolatier (Nyotengu)", "kr_name": "스위트・쇼콜라티에(뇨텐구)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_6", "girl": "kokoro", "name": "スイート・ショコラティエ(こころ)", "zhs_name": "甜心巧克力师(心)", "zht_name": "甜心巧克力師(心)", "en_name": "Sweet Chocolatier (Kokoro)", "kr_name": "스위트・쇼콜라티에(코코로)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_7", "girl": "hitomi", "name": "スイート・ショコラティエ(ヒトミ)", "zhs_name": "甜心巧克力师(瞳)", "zht_name": "甜心巧克力師(瞳)", "en_name": "Sweet Chocolatier (Hitomi)", "kr_name": "스위트・쇼콜라티에(히토미)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2020/5/25 2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_8", "girl": "momiji", "name": "スイート・ショコラティエ(紅葉)", "zhs_name": "甜心巧克力师(红叶)", "zht_name": "甜心巧克力師(紅葉)", "en_name": "Sweet Chocolatier (Momiji)", "kr_name": "스위트・쇼콜라티에(모미지)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2020/9/20 2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_9", "girl": "helena", "name": "スイート・ショコラティエ(エレナ)", "zhs_name": "甜心巧克力师(海莲娜)", "zht_name": "甜心巧克力師(海蓮娜)", "en_name": "Sweet Chocolatier (Helena)", "kr_name": "스위트・쇼콜라티에(엘레나)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_10", "girl": "misaki", "name": "スイート・ショコラティエ(みさき)", "zhs_name": "甜心巧克力师(海咲)", "zht_name": "甜心巧克力師(海咲)", "en_name": "Sweet Chocolatier (Misaki)", "kr_name": "스위트・쇼콜라티에(미사키)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2020/7/7 2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_11", "girl": "luna", "name": "スイート・ショコラティエ(ルナ)", "zhs_name": "甜心巧克力师(露娜)", "zht_name": "甜心巧克力師(露娜)", "en_name": "Sweet Chocolatier (Luna)", "kr_name": "스위트・쇼콜라티에(루나)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_12", "girl": "tamaki", "name": "スイート・ショコラティエ(たまき)", "zhs_name": "甜心巧克力师(环)", "zht_name": "甜心巧克力師(環)", "en_name": "Sweet Chocolatier (Tamaki)", "kr_name": "스위트・쇼콜라티에(타마키)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_13", "girl": "leifang", "name": "スイート・ショコラティエ(レイファン)", "zhs_name": "甜心巧克力师(丽凤)", "zht_name": "甜心巧克力師(麗鳳)", "en_name": "Sweet Chocolatier (Leifang)", "kr_name": "스위트・쇼콜라티에(레이팡)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_14", "girl": "fiona", "name": "スイート・ショコラティエ(フィオナ)", "zhs_name": "甜心巧克力师(菲欧娜)", "zht_name": "甜心巧克力師(菲歐娜)", "en_name": "Sweet Chocolatier (Fiona)", "kr_name": "스위트・쇼콜라티에(피오나)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_15", "girl": "nagisa", "name": "スイート・ショコラティエ(なぎさ)", "zhs_name": "甜心巧克力师(凪咲)", "zht_name": "甜心巧克力師(凪咲)", "en_name": "Sweet Chocolatier (Nagisa)", "kr_name": "스위트・쇼콜라티에(나기사)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_16", "girl": "kanna", "name": "スイート・ショコラティエ(カンナ)", "zhs_name": "甜心巧克力师(神无)", "zht_name": "甜心巧克力師(神無)", "en_name": "Sweet Chocolatier (Kanna)", "kr_name": "스위트・쇼콜라티에(칸나)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "306_17", "girl": "monica", "name": "スイート・ショコラティエ(モニカ)", "zhs_name": "甜心巧克力师(莫妮卡)", "zht_name": "甜心巧克力師(莫妮卡)", "en_name": "Sweet Chocolatier (Monica)", "kr_name": "스위트・쇼콜라티에(모니카)", "type": "pow", "pow": "4932", "tec": "3656", "stm": "4104", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナE", "skill3": "ショコラティエのパワー", "sell": "2020/2/13", "resell": "2021/2/17 2022/2/10", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)帽子可以设定隐藏"
  },
  {
    "id": "134_15", "girl": "nagisa", "name": "メルティ・ハート(なぎさ)", "zhs_name": "融化之心(凪咲)", "zht_name": "融化之心(凪咲)", "en_name": "Melty Heart (Nagisa)", "kr_name": "멜티 하트(나기사)", "type": "pow", "pow": "4932", "tec": "3686", "stm": "4024", "apl": "200", "skill1": "強烈スパイクE", "skill2": "とろけるほどのパワー", "skill3": "豪快なスパイク", "sell": "2020/2/20", "resell": "2021/2/10 2022/2/10", "break": "1", "special_fun": "截止20200220 免费力量服装中最强 老角色落泪"
  },
  {
    "id": "134_16", "girl": "kanna", "name": "メルティ・ハート(カンナ)", "zhs_name": "融化之心(神无)", "zht_name": "融化之心(神無)", "en_name": "Melty Heart (Kanna)", "kr_name": "멜티 하트(칸나)", "type": "pow", "pow": "4932", "tec": "3686", "stm": "4024", "apl": "200", "skill1": "強烈スパイクE", "skill2": "とろけるほどのパワー", "skill3": "豪快なスパイク", "sell": "2020/2/20", "resell": "2021/2/10 2022/2/10", "break": "1", "special_fun": "截止20200220 免费力量服装中最强 老角色落泪"
  },
  {
    "id": "134_17", "girl": "monica", "name": "メルティ・ハート(モニカ)", "zhs_name": "融化之心(莫妮卡)", "zht_name": "融化之心(莫妮卡)", "en_name": "Melty Heart (Monica)", "kr_name": "멜티 하트(모니카)", "type": "pow", "pow": "4932", "tec": "3686", "stm": "4024", "apl": "200", "skill1": "強烈スパイクE", "skill2": "とろけるほどのパワー", "skill3": "豪快なスパイク", "sell": "2020/2/20", "resell": "2021/2/10 2022/2/10", "break": "1", "special_fun": "截止20200220 免费力量服装中最强 老角色落泪"
  },
  {
    "id": "307", "girl": "kasumi", "name": "ジュエル・アメジスト(かすみ)", "zhs_name": "珍宝・紫水晶(霞)", "zht_name": "珍寶‧紫水晶(霞)", "en_name": "Jewel Amethyst (Kasumi)", "kr_name": "주얼 자수정(카스미)", "type": "stm", "pow": "3356", "tec": "4664", "stm": "5322", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "アメジスト・スタミナ", "skill3": "可憐なフェイント", "sell": "2020/2/23", "resell": "2020/10/29 2021/2/23 2022/2/23 2023/2/23", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现紫色粒子效果(光之舞) 濡湿会使衣服变色"
  },
  {
    "id": "308", "girl": "hitomi", "name": "やわらか4コマ単行本特典(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3884", "tec": "3336", "stm": "4822", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "灼熱のダンスC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/2/22", "resell": "", "break": "1", "special_fun": "官方漫画单行本特典 需要可以日亚自行购买(1000日元) 兑换码有效期为发布日后1年"
  },
  {
    "id": "309", "girl": "nagisa", "name": "おつまみピンチョス(なぎさ)", "zhs_name": "拽拽Pinchos(凪咲)", "zht_name": "拽拽Pinchos(凪咲)", "en_name": "Appetizer Pinchos (Nagisa)", "kr_name": "애피타이저 핀초(나기사)", "type": "tec", "pow": "3974", "tec": "5142", "stm": "3626", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "驚異のスタミナD", "skill3": "閃きのテクニック6", "sell": "2020/2/27", "resell": "2020/11/5 2021/3/25 2021/10/14", "break": "1", "special_fun": "允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "310", "girl": "monica", "name": "おつまみピンチョス(モニカ)", "zhs_name": "拽拽Pinchos(莫妮卡)", "zht_name": "拽拽Pinchos(莫妮卡)", "en_name": "Appetizer Pinchos (Monica)", "kr_name": "애피타이저 핀초(모니카)", "type": "tec", "pow": "3974", "tec": "5142", "stm": "3626", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "驚異のスタミナD", "skill3": "閃きのテクニック6", "sell": "2020/2/27", "resell": "2020/11/5 2021/10/14", "break": "1", "special_fun": "允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "311_1", "girl": "kasumi", "name": "ホワイト・プリンス(かすみ)", "zhs_name": "白马王子(霞)", "zht_name": "白馬王子(霞)", "en_name": "White Prince (Kasumi)", "kr_name": "화이트 프린스(카스미)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2020/3/5", "resell": "2021/3/18 2023/3/9", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "311_2", "girl": "marie", "name": "ホワイト・プリンス(マリー)", "zhs_name": "白马王子(玛莉)", "zht_name": "白馬王子(瑪莉)", "en_name": "White Prince (Marie)", "kr_name": "화이트 프린스(마리)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2020/3/5", "resell": "2020/6/6 2021/3/18 2023/3/9", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "311_3", "girl": "nyotengu", "name": "ホワイト・プリンス(女天狗)", "zhs_name": "白马王子(女天狗)", "zht_name": "白馬王子(女天狗)", "en_name": "White Prince (Nyotengu)", "kr_name": "화이트 프린스(뇨텐구)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2020/3/5", "resell": "2021/3/18 2023/3/9", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "311_4", "girl": "kokoro", "name": "ホワイト・プリンス(こころ)", "zhs_name": "白马王子(心)", "zht_name": "白馬王子(心)", "en_name": "White Prince (Kokoro)", "kr_name": "화이트 프린스(코코로)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2020/3/5", "resell": "2021/3/18 2023/3/9", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "311_5", "girl": "hitomi", "name": "ホワイト・プリンス(ヒトミ)", "zhs_name": "白马王子(瞳)", "zht_name": "白馬王子(瞳)", "en_name": "White Prince (Hitomi)", "kr_name": "화이트 프린스(히토미)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2020/3/5", "resell": "2020/5/25 2021/3/18 2023/3/9", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "311_6", "girl": "momiji", "name": "ホワイト・プリンス(紅葉)", "zhs_name": "白马王子(红叶)", "zht_name": "白馬王子(紅葉)", "en_name": "White Prince (Momiji)", "kr_name": "화이트 프린스(모미지)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2020/3/5", "resell": "2021/3/18 2023/3/9", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "311_7", "girl": "tamaki", "name": "ホワイト・プリンス(たまき)", "zhs_name": "白马王子(环)", "zht_name": "白馬王子(環)", "en_name": "White Prince (Tamaki)", "kr_name": "화이트 프린스(타마키)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2020/3/5", "resell": "2021/3/18 2023/3/9", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "311_8", "girl": "fiona", "name": "ホワイト・プリンス(フィオナ)", "zhs_name": "白马王子(菲欧娜)", "zht_name": "白馬王子(菲歐娜)", "en_name": "White Prince (Fiona)", "kr_name": "화이트 프린스(피오나)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2020/3/5", "resell": "2021/3/18 2023/3/9", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "311_9", "girl": "nagisa", "name": "ホワイト・プリンス(なぎさ)", "zhs_name": "白马王子(凪咲)", "zht_name": "白馬王子(凪咲)", "en_name": "White Prince (Nagisa)", "kr_name": "화이트 프린스(나기사)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2020/3/5", "resell": "2021/3/18 2023/3/9", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "142_15", "girl": "nagisa", "name": "ウィズ・ユー(なぎさ)", "zhs_name": "与你同在(凪咲)", "zht_name": "與你同在(凪咲)", "en_name": "With You (Nagisa)", "kr_name": "위드유(나기사)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2020/3/11", "resell": "2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_16", "girl": "kanna", "name": "ウィズ・ユー(カンナ)", "zhs_name": "与你同在(神无)", "zht_name": "與你同在(神無)", "en_name": "With You (Kanna)", "kr_name": "위드유(칸나)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2020/3/11", "resell": "2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "142_17", "girl": "monica", "name": "ウィズ・ユー(モニカ)", "zhs_name": "与你同在(莫妮卡)", "zht_name": "與你同在(莫妮卡)", "en_name": "With You (Monica)", "kr_name": "위드유(모니카)", "type": "stm", "pow": "4384", "tec": "3886", "stm": "4772", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2020/3/11", "resell": "2021/3/11 2022/3/10", "break": "1", "special_fun": ""
  },
  {
    "id": "312", "girl": "sayuri", "name": "ほほえみ日和(さゆり)", "zhs_name": "微笑晴天(小百合)", "zht_name": "微笑晴天(小百合)", "en_name": "Smile Weather(Sayuri)", "kr_name": "스마일 데이(사유리)", "type": "stm", "pow": "3336", "tec": "4564", "stm": "5242", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "裏の裏を突くフェイントE", "skill3": "内から湧き上がるスタミナ6", "sell": "2020/3/17", "resell": "2020/5/20 2021/6/24", "break": "1", "special_fun": "头巾可以设置隐藏，部分发型不支持头巾(解决穿模的办法就是 消灭可能穿模的模型)"
  },
  {
    "id": "313", "girl": "honoka", "name": "ほほえみ日和(ほのか)", "zhs_name": "微笑晴天(穗香)", "zht_name": "微笑晴天(穗香)", "en_name": "Smile Weather (Honoka)", "kr_name": "스마일 데이(호노카)", "type": "stm", "pow": "3486", "tec": "4514", "stm": "5042", "apl": "200", "skill1": "灼熱のダンスB", "skill2": "閃きのテクニック3", "skill3": "熱烈なエール", "sell": "2020/3/17", "resell": "2020/5/20 2021/6/24", "break": "1", "special_fun": "头巾可以设置隐藏，部分发型不支持头巾(解决穿模的办法就是 消灭可能穿模的模型)"
  },
  {
    "id": "314", "girl": "honoka", "name": "ジュエル・アクアマリン(ほのか)", "zhs_name": "珍宝・海蓝宝石(穗香)", "zht_name": "珍寶‧海藍寶石(穗香)", "en_name": "Jewel Aquamarine (Honoka)", "kr_name": "주얼 아쿠아마린(호노카)", "type": "pow", "pow": "5322", "tec": "3764", "stm": "4114", "apl": "200", "skill1": "強烈スパイクE", "skill2": "アクアマリン・パワー", "skill3": "豪快なスパイク", "sell": "2020/3/24", "resell": "2020/10/29 2021/3/24 2022/3/24 2023/3/24", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现蓝色粒子效果(光之舞)终于宝石装不再是stm服盛宴了。"
  },
  {
    "id": "178_16", "girl": "sayuri", "name": "ふわもこフォーム(さゆり)", "zhs_name": "蓬松泡沫(小百合)", "zht_name": "蓬鬆泡沫(小百合)", "en_name": "Bubbly Foam (Sayuri)", "kr_name": "부드러운 거품 (사유리)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2020/3/25", "resell": "2020/9/26 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞 本周无回想"
  },
  {
    "id": "178_17", "girl": "monica", "name": "ふわもこフォーム(モニカ)", "zhs_name": "蓬松泡沫(莫妮卡)", "zht_name": "蓬鬆泡沫(莫妮卡)", "en_name": "Bubbly Foam (Monica)", "kr_name": "부드러운 거품 (모니카)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2020/3/25", "resell": "2020/9/26 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞 本周无回想"
  },
  {
    "id": "178_18", "girl": "kanna", "name": "ふわもこフォーム(カンナ)", "zhs_name": "蓬松泡沫(神无)", "zht_name": "蓬鬆泡沫(神無)", "en_name": "Bubbly Foam (Kanna)", "kr_name": "부드러운 거품 (칸나)", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2020/3/25", "resell": "2020/9/26 2021/10/29 2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞 本周无回想"
  },
  {
    "id": "315_1", "girl": "marie", "name": "アリスギア・バーラタ(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3706", "tec": "4264", "stm": "5172", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントD", "skill3": "バーラタのスタミナ", "sell": "2020/3/30", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(大剑/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉"
  },
  {
    "id": "315_2", "girl": "ayane", "name": "アリスギア・バーラタ(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3706", "tec": "4264", "stm": "5172", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントD", "skill3": "バーラタのスタミナ", "sell": "2020/3/30", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(大剑/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉"
  },
  {
    "id": "315_3", "girl": "kokoro", "name": "アリスギア・バーラタ(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3706", "tec": "4264", "stm": "5172", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントD", "skill3": "バーラタのスタミナ", "sell": "2020/3/30", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(大剑/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉"
  },
  {
    "id": "315_4", "girl": "hitomi", "name": "アリスギア・バーラタ(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3706", "tec": "4264", "stm": "5172", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントD", "skill3": "バーラタのスタミナ", "sell": "2020/3/30", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(大剑/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉"
  },
  {
    "id": "315_5", "girl": "misaki", "name": "アリスギア・バーラタ(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3706", "tec": "4264", "stm": "5172", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントD", "skill3": "バーラタのスタミナ", "sell": "2020/3/30", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(大剑/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉"
  },
  {
    "id": "315_6", "girl": "leifang", "name": "アリスギア・バーラタ(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3706", "tec": "4264", "stm": "5172", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントD", "skill3": "バーラタのスタミナ", "sell": "2020/3/30", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(大剑/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉"
  },
  {
    "id": "315_7", "girl": "fiona", "name": "アリスギア・バーラタ(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3706", "tec": "4264", "stm": "5172", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントD", "skill3": "バーラタのスタミナ", "sell": "2020/3/30", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(大剑/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉"
  },
  {
    "id": "315_8", "girl": "nagisa", "name": "アリスギア・バーラタ(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3706", "tec": "4264", "stm": "5172", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントD", "skill3": "バーラタのスタミナ", "sell": "2020/3/30", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(大剑/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉"
  },
  {
    "id": "315_9", "girl": "kanna", "name": "アリスギア・バーラタ(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3706", "tec": "4264", "stm": "5172", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントD", "skill3": "バーラタのスタミナ", "sell": "2020/3/30", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(大剑/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉"
  },
  {
    "id": "316", "girl": "sayuri", "name": "ジュエル・アクアマリン(さゆり)", "zhs_name": "珍宝・海蓝宝石(小百合)", "zht_name": "珍寶・海藍寶石(小百合)", "en_name": "Jewel Aquamarine (Sayuri)", "kr_name": "주얼 아쿠아마린(사유리)", "type": "tec", "pow": "3376", "tec": "5322", "stm": "4244", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "アクアマリン・テクニック", "skill3": "可憐なフェイント", "sell": "2020/3/31", "resell": "2020/10/29 2021/3/31 2022/3/31 2023/3/31", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现红色粒子效果(光之舞)【A技能与SSR饰品技能冲突！】KT：我们这是为了游戏平衡，不爽不要用"
  },
  {
    "id": "317", "girl": "sayuri", "name": "ステラ・アリエス(さゆり)", "zhs_name": "星辰・白羊(小百合)", "zht_name": "星辰・白羊(小百合)", "en_name": "Stellar Aries (Sayuri)", "kr_name": "스텔라 아리에스(사유리)", "type": "stm", "pow": "4044", "tec": "3976", "stm": "5322", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "アリエス・スタミナ", "skill3": "可憐なフェイント", "sell": "2020/3/31", "resell": "2021/3/31 2021/9/16 2022/3/31 2022/9/8 2023/3/31", "break": "1", "special_fun": "论nt和坑钱我脱裤魔就没服过谁，复制粘贴改色上架速度第一快，就是两件生日一起卖"
  },
  {
    "id": "318_1", "girl": "kasumi", "name": "アリスギア・明鏡止水(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3556", "tec": "5072", "stm": "4114", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦D", "skill3": "明鏡止水のテクニック", "sell": "2020/4/6", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(光刀/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉。活动拍照场景 不满觉偷看胖次会被电子干扰【呵呵】"
  },
  {
    "id": "318_2", "girl": "honoka", "name": "アリスギア・明鏡止水(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3556", "tec": "5072", "stm": "4114", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦D", "skill3": "明鏡止水のテクニック", "sell": "2020/4/6", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(光刀/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉。活动拍照场景 不满觉偷看胖次会被电子干扰【呵呵】"
  },
  {
    "id": "318_3", "girl": "nyotengu", "name": "アリスギア・明鏡止水(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3556", "tec": "5072", "stm": "4114", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦D", "skill3": "明鏡止水のテクニック", "sell": "2020/4/6", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(光刀/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉。活动拍照场景 不满觉偷看胖次会被电子干扰【呵呵】"
  },
  {
    "id": "318_4", "girl": "momiji", "name": "アリスギア・明鏡止水(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3556", "tec": "5072", "stm": "4114", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦D", "skill3": "明鏡止水のテクニック", "sell": "2020/4/6", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(光刀/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉。活动拍照场景 不满觉偷看胖次会被电子干扰【呵呵】"
  },
  {
    "id": "318_5", "girl": "helena", "name": "アリスギア・明鏡止水(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3556", "tec": "5072", "stm": "4114", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦D", "skill3": "明鏡止水のテクニック", "sell": "2020/4/6", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(光刀/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉。活动拍照场景 不满觉偷看胖次会被电子干扰【呵呵】"
  },
  {
    "id": "318_6", "girl": "luna", "name": "アリスギア・明鏡止水(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3556", "tec": "5072", "stm": "4114", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦D", "skill3": "明鏡止水のテクニック", "sell": "2020/4/6", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(光刀/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉。活动拍照场景 不满觉偷看胖次会被电子干扰【呵呵】"
  },
  {
    "id": "318_7", "girl": "tamaki", "name": "アリスギア・明鏡止水(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3556", "tec": "5072", "stm": "4114", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦D", "skill3": "明鏡止水のテクニック", "sell": "2020/4/6", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(光刀/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉。活动拍照场景 不满觉偷看胖次会被电子干扰【呵呵】"
  },
  {
    "id": "318_8", "girl": "monica", "name": "アリスギア・明鏡止水(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3556", "tec": "5072", "stm": "4114", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦D", "skill3": "明鏡止水のテクニック", "sell": "2020/4/6", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(光刀/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉。活动拍照场景 不满觉偷看胖次会被电子干扰【呵呵】"
  },
  {
    "id": "318_9", "girl": "sayuri", "name": "アリスギア・明鏡止水(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3556", "tec": "5072", "stm": "4114", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦D", "skill3": "明鏡止水のテクニック", "sell": "2020/4/6", "resell": "2022/7/6", "break": "1", "special_fun": "『アリスギア』联动服装，附带2个专属小道具(光刀/枪)，满觉后可以切换为 机甲状态。允许和本次的所有联动服装互相成为狗粮素材满觉。活动拍照场景 不满觉偷看胖次会被电子干扰【呵呵】"
  },
  {
    "id": "319", "girl": "misaki", "name": "サンセットフィッシュ(みさき)", "zhs_name": "日暮之鱼(海咲)", "zht_name": "日暮之魚(海咲)", "en_name": "Sunset Fish (Misaki)", "kr_name": "선셋 피시(미사키)", "type": "pow", "pow": "5002", "tec": "3874", "stm": "3766", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "プラチナアタッカー", "skill3": "豪快なスパイク", "sell": "2020/4/14", "resell": "2020/8/18 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "320", "girl": "helena", "name": "サンセットフィッシュ(エレナ)", "zhs_name": "日暮之鱼(海莲娜)", "zht_name": "日暮之魚(海蓮娜)", "en_name": "Sunset Fish (Helena)", "kr_name": "선셋 피시(엘레나)", "type": "pow", "pow": "5002", "tec": "3874", "stm": "3766", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "プラチナアタッカー", "skill3": "豪快なスパイク", "sell": "2020/4/14", "resell": "2020/8/18 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "321", "girl": "ayane", "name": "トワイライトフィッシュ(あやね)", "zhs_name": "拂晓之鱼(绫音)", "zht_name": "拂曉之魚(綾音)", "en_name": "Twilight Fish (Ayane)", "kr_name": "트와일라이트 피시(아야네)", "type": "pow", "pow": "5162", "tec": "3894", "stm": "3686", "apl": "200", "skill1": "強烈スパイクB", "skill2": "高度な心理戦B", "skill3": "秘められたパワー6", "sell": "2020/4/14", "resell": "2020/8/18 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "322", "girl": "fiona", "name": "トワイライトフィッシュ(フィオナ)", "zhs_name": "拂晓之鱼(菲欧娜)", "zht_name": "拂曉之魚(菲歐娜)", "en_name": "Twilight Fish (Fiona)", "kr_name": "트와일라이트 피시(피오나)", "type": "pow", "pow": "5162", "tec": "3894", "stm": "3686", "apl": "200", "skill1": "強烈スパイクB", "skill2": "高度な心理戦B", "skill3": "秘められたパワー6", "sell": "2020/4/14", "resell": "2020/8/18 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "323_1", "girl": "misaki", "name": "恋風天舞・藍(みさき)", "zhs_name": "恋风天舞・蓝(海咲)", "zht_name": "戀風天舞‧藍(海咲)", "en_name": "Indigo Love Dance (Misaki)", "kr_name": "연풍천무(남색)(미사키)", "type": "tec", "pow": "3516", "tec": "5222", "stm": "4004", "apl": "200", "skill1": "高度な心理戦E", "skill2": "驚異のスタミナA", "skill3": "恋のテクニック", "sell": "2020/4/21", "resell": "2021/4/28 2022/4/13", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉 本周无回想"
  },
  {
    "id": "323_2", "girl": "monica", "name": "恋風天舞・藍(モニカ)", "zhs_name": "恋风天舞・蓝(莫妮卡)", "zht_name": "戀風天舞‧藍(莫妮卡)", "en_name": "Indigo Love Dance (Monica)", "kr_name": "연풍천무(남색)(모니카)", "type": "tec", "pow": "3516", "tec": "5222", "stm": "4004", "apl": "200", "skill1": "高度な心理戦E", "skill2": "驚異のスタミナA", "skill3": "恋のテクニック", "sell": "2020/4/21", "resell": "2021/4/28 2022/4/13", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉 本周无回想"
  },
  {
    "id": "323_3", "girl": "tamaki", "name": "恋風天舞・藍(たまき)", "zhs_name": "恋风天舞・蓝(环)", "zht_name": "戀風天舞‧藍(環)", "en_name": "Indigo Love Dance (Tamaki)", "kr_name": "연풍천무(남색)(타마키)", "type": "tec", "pow": "3516", "tec": "5222", "stm": "4004", "apl": "200", "skill1": "高度な心理戦E", "skill2": "驚異のスタミナA", "skill3": "恋のテクニック", "sell": "2020/4/21", "resell": "2021/4/28 2022/4/13", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉 本周无回想"
  },
  {
    "id": "323_4", "girl": "kasumi", "name": "恋風天舞・藍(かすみ)", "zhs_name": "恋风天舞・蓝(霞)", "zht_name": "戀風天舞‧藍(霞)", "en_name": "Indigo Love Dance (Kasumi)", "kr_name": "연풍천무(남색)(카스미)", "type": "tec", "pow": "3516", "tec": "5222", "stm": "4004", "apl": "200", "skill1": "高度な心理戦E", "skill2": "驚異のスタミナA", "skill3": "恋のテクニック", "sell": "2020/4/21", "resell": "2021/4/28 2022/4/13", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉 本周无回想"
  },
  {
    "id": "324_1", "girl": "nyotengu", "name": "恋風天舞・緋(女天狗)", "zhs_name": "恋风天舞・绯(女天狗)", "zht_name": "戀風天舞‧緋(女天狗)", "en_name": "Scarlet Love Dance (Nyotengu)", "kr_name": "연풍천무(주홍색)(뇨텐구)", "type": "tec", "pow": "3496", "tec": "5042", "stm": "4204", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "灼熱のダンスB", "skill3": "恋のテクニック", "sell": "2020/4/21", "resell": "2021/4/28 2022/4/13", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉 本周无回想"
  },
  {
    "id": "324_2", "girl": "momiji", "name": "恋風天舞・緋(紅葉)", "zhs_name": "恋风天舞・绯(红叶)", "zht_name": "戀風天舞‧緋(紅葉)", "en_name": "Scarlet Love Dance (Momiji)", "kr_name": "연풍천무(주홍색)(모미지)", "type": "tec", "pow": "3496", "tec": "5042", "stm": "4204", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "灼熱のダンスB", "skill3": "恋のテクニック", "sell": "2020/4/21", "resell": "2021/4/28 2022/4/13", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉 本周无回想"
  },
  {
    "id": "324_3", "girl": "ayane", "name": "恋風天舞・緋(あやね)", "zhs_name": "恋风天舞・绯(绫音)", "zht_name": "戀風天舞‧緋(綾音)", "en_name": "Scarlet Love Dance (Ayane)", "kr_name": "연풍천무(주홍색)(아야네)", "type": "tec", "pow": "3496", "tec": "5042", "stm": "4204", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "灼熱のダンスB", "skill3": "恋のテクニック", "sell": "2020/4/21", "resell": "2021/4/28 2022/4/13", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉 本周无回想"
  },
  {
    "id": "324_4", "girl": "fiona", "name": "恋風天舞・緋(フィオナ)", "zhs_name": "恋风天舞・绯(菲欧娜)", "zht_name": "戀風天舞‧緋(菲歐娜)", "en_name": "Scarlet Love Dance (Fiona)", "kr_name": "연풍천무(주홍색)(피오나)", "type": "tec", "pow": "3496", "tec": "5042", "stm": "4204", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "灼熱のダンスB", "skill3": "恋のテクニック", "sell": "2020/4/21", "resell": "2021/4/28 2022/4/13", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉 本周无回想"
  },
  {
    "id": "325", "girl": "leifang", "name": "ジュエル・ダイヤモンド(レイファン)", "zhs_name": "珍宝・钻石(丽凤)", "zht_name": "珍寶・鑽石(麗鳳)", "en_name": "Jewel Diamond (Leifang)", "kr_name": "주얼 다이아몬드(레이팡)", "type": "stm", "pow": "3296", "tec": "4724", "stm": "5322", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ダイヤモンド・スタミナ", "skill3": "可憐なフェイント", "sell": "2020/4/23", "resell": "2020/10/29 2022/4/23 2023/4/23", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现白色粒子效果(光之舞)恭喜dmm版本的雷芳 成功靠真爱金主逆天改命 成为技巧系霸王"
  },
  {
    "id": "326", "girl": "patty", "name": "ホロホロ・デイズ(パティ)", "zhs_name": "漫步・白昼(派蒂)", "zht_name": "漫步・白晝(派蒂)", "en_name": "Star Outfit Gacha (Patty)", "kr_name": "하늘하늘 데이즈(패티)", "type": "pow", "pow": "5132", "tec": "3436", "stm": "4174", "apl": "200 ", "skill1": "強烈スパイクD", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー3", "sell": "2020/4/30", "resell": "2020/7/31 2023/4/30", "break": "1", "special_fun": ""
  },
  {
    "id": "327", "girl": "nagisa", "name": "ジュエル・エメラルド(なぎさ)", "zhs_name": "珍宝・翡翠(凪咲)", "zht_name": "珍寶・翡翠(凪咲)", "en_name": "Jewel Emerald (Nagisa)", "kr_name": "주얼 에메랄드(나기사)", "type": "stm", "pow": "4684", "tec": "3336", "stm": "5322", "apl": "200", "skill1": "強烈スパイクE", "skill2": "エメラルド・スタミナ", "skill3": "豪快なスパイク", "sell": "2020/5/5", "resell": "2020/10/29 2021/5/5 2022/5/5 2023/5/5", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现绿色粒子效果(光之舞)"
  },
  {
    "id": "328_1", "girl": "misaki", "name": "桃宴桜舞(みさき)", "zhs_name": "桃宴樱舞(海咲)", "zht_name": "桃宴櫻舞(海咲)", "en_name": "Peach Party Sakura Dance (Misaki)", "kr_name": "도연앵무(미사키)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/18", "resell": "2020/7/7 2021/5/27", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_2", "girl": "tamaki", "name": "桃宴桜舞(たまき)", "zhs_name": "桃宴樱舞(环)", "zht_name": "桃宴櫻舞(環)", "en_name": "Peach Party Sakura Dance (Tamaki)", "kr_name": "도연앵무(타마키)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/18", "resell": "2021/5/27", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_3", "girl": "fiona", "name": "桃宴桜舞(フィオナ)", "zhs_name": "桃宴樱舞(菲欧娜)", "zht_name": "桃宴櫻舞(菲歐娜)", "en_name": "Peach Party Sakura Dance (Fiona)", "kr_name": "도연앵무(피오나)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/18", "resell": "2021/5/27", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_4", "girl": "monica", "name": "桃宴桜舞(モニカ)", "zhs_name": "桃宴樱舞(莫妮卡)", "zht_name": "桃宴櫻舞(莫妮卡)", "en_name": "Peach Party Sakura Dance (Monica)", "kr_name": "도연앵무(모니카)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/18", "resell": "2021/5/27", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_5", "girl": "kasumi", "name": "桃宴桜舞(かすみ)", "zhs_name": "桃宴樱舞(霞)", "zht_name": "桃宴櫻舞(霞)", "en_name": "Peach Party Sakura Dance (Kasumi)", "kr_name": "도연앵무(카스미)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/18", "resell": "2021/5/27", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_6", "girl": "ayane", "name": "桃宴桜舞(あやね)", "zhs_name": "桃宴樱舞(绫音)", "zht_name": "桃宴櫻舞(綾音)", "en_name": "Peach Party Sakura Dance (Ayane)", "kr_name": "도연앵무(아야네)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/18", "resell": "2020/8/5 2021/5/27", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_7", "girl": "kokoro", "name": "桃宴桜舞(こころ)", "zhs_name": "桃宴樱舞(心)", "zht_name": "桃宴櫻舞(心)", "en_name": "Peach Party Sakura Dance (Kokoro)", "kr_name": "도연앵무(코코로)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/18", "resell": "2021/5/27", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_8", "girl": "hitomi", "name": "桃宴桜舞(ヒトミ)", "zhs_name": "桃宴樱舞(瞳)", "zht_name": "桃宴櫻舞(瞳)", "en_name": "Peach Party Sakura Dance (Hitomi)", "kr_name": "도연앵무(히토미)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/18", "resell": "2021/5/27", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_9", "girl": "leifang", "name": "桃宴桜舞(レイファン)", "zhs_name": "桃宴樱舞(丽凤)", "zht_name": "桃宴櫻舞(麗鳳)", "en_name": "Peach Party Sakura Dance (Leifang)", "kr_name": "도연앵무(레이팡)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/18", "resell": "2021/5/27", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_10", "girl": "marie", "name": "桃宴桜舞(マリー)", "zhs_name": "桃宴樱舞(玛莉)", "zht_name": "桃宴櫻舞(瑪莉)", "en_name": "Peach Party Sakura Dance (Marie)", "kr_name": "도연앵무(마리)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/23", "resell": "2021/6/3", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_11", "girl": "nagisa", "name": "桃宴桜舞(なぎさ)", "zhs_name": "桃宴樱舞(凪咲)", "zht_name": "桃宴櫻舞(凪咲)", "en_name": "Peach Party Sakura Dance (Nagisa)", "kr_name": "도연앵무(나기사)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/23", "resell": "2021/6/3", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_12", "girl": "honoka", "name": "桃宴桜舞(ほのか)", "zhs_name": "桃宴樱舞(穗香)", "zht_name": "桃宴櫻舞(穗香)", "en_name": "Peach Party Sakura Dance (Honoka)", "kr_name": "도연앵무(호노카)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/23", "resell": "2021/6/3", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_13", "girl": "sayuri", "name": "桃宴桜舞(さゆり)", "zhs_name": "桃宴樱舞(小百合)", "zht_name": "桃宴櫻舞(小百合)", "en_name": "Peach Party Sakura Dance (Sayuri)", "kr_name": "도연앵무(사유리)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/23", "resell": "2021/6/3", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_14", "girl": "luna", "name": "桃宴桜舞(ルナ)", "zhs_name": "桃宴樱舞(露娜)", "zht_name": "桃宴櫻舞(露娜)", "en_name": "Peach Party Sakura Dance (Luna)", "kr_name": "도연앵무(루나)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/23", "resell": "2021/6/3", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_15", "girl": "nyotengu", "name": "桃宴桜舞(女天狗)", "zhs_name": "桃宴樱舞(女天狗)", "zht_name": "桃宴櫻舞(女天狗)", "en_name": "Peach Party Sakura Dance (Nyotengu)", "kr_name": "도연앵무(뇨텐구)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/23", "resell": "2021/6/3", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_16", "girl": "kanna", "name": "桃宴桜舞(カンナ)", "zhs_name": "桃宴樱舞(神无)", "zht_name": "桃宴櫻舞(神無)", "en_name": "Peach Party Sakura Dance (Kanna)", "kr_name": "도연앵무(칸나)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/23", "resell": "2021/6/3", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_17", "girl": "momiji", "name": "桃宴桜舞(紅葉)", "zhs_name": "桃宴樱舞(红叶)", "zht_name": "桃宴櫻舞(紅葉)", "en_name": "Peach Party Sakura Dance (Momiji)", "kr_name": "도연앵무(모미지)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/23", "resell": "2020/9/20 2021/6/3", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_18", "girl": "helena", "name": "桃宴桜舞(エレナ)", "zhs_name": "桃宴樱舞(海莲娜)", "zht_name": "桃宴櫻舞(海蓮娜)", "en_name": "Peach Party Sakura Dance (Helena)", "kr_name": "도연앵무(엘레나)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2020/5/23", "resell": "2021/6/3", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "329", "girl": "hitomi", "name": "ジュエル・エメラルド(ヒトミ)", "zhs_name": "珍宝・翡翠(瞳)", "zht_name": "珍寶・翡翠(瞳)", "en_name": "Jewel Emerald (Hitomi)", "kr_name": "주얼 에메랄드(히토미)", "type": "pow", "pow": "5322", "tec": "3714", "stm": "4164", "apl": "200", "skill1": "強烈スパイクE", "skill2": "エメラルド・パワー", "skill3": "豪快なスパイク", "sell": "2020/5/25", "resell": "2020/10/29 2021/5/25 2022/5/25 2023/5/25", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现绿色粒子效果(光之舞)"
  },
  {
    "id": "330", "girl": "patty", "name": "シャイニー・パフューム(パティ)", "zhs_name": "璀璨・香薰(派蒂)", "zht_name": "璀璨・香薰(派蒂)", "en_name": "Shiny Perfume (Patty)", "kr_name": "샤이니 퍼퓸(패티)", "type": "stm", "pow": "4504", "tec": "3466", "stm": "5072", "apl": "200", "skill1": "強烈スパイクC", "skill2": "内から湧き上がるスタミナ4", "skill3": "豪快なスパイク", "sell": "2020/5/28", "resell": "2020/7/31 2023/4/30", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "331_1", "girl": "sayuri", "name": "ベルベットタイム・パール(さゆり)", "zhs_name": "丝绒时光・珍珠(小百合)", "zht_name": "絲絨時光‧珍珠(小百合)", "en_name": "Velvet Time: Pearl (Sayuri)", "kr_name": "벨벳 타임(펄)(사유리)", "type": "pow", "pow": "5072", "tec": "3366", "stm": "4204", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "内から湧き上がるスタミナ4", "skill3": "豪快なスパイク", "sell": "2020/5/28", "resell": "2020/12/1", "break": "1", "special_fun": ""
  },
  {
    "id": "331_2", "girl": "monica", "name": "ベルベットタイム・ローズ(モニカ)", "zhs_name": "丝绒时光・蔷薇(莫妮卡)", "zht_name": "絲絨時光‧薔薇(莫妮卡)", "en_name": "Velvet Time: Rose (Monica)", "kr_name": "벨벳 타임(로즈)(모니카)", "type": "pow", "pow": "5212", "tec": "3486", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "灼熱のダンスB", "skill3": "内から湧き上がるスタミナ4", "sell": "2020/5/28", "resell": "2020/12/1", "break": "1", "special_fun": ""
  },
  {
    "id": "331_3", "girl": "helena", "name": "ベルベットタイム・ローズ(エレナ)", "zhs_name": "丝绒时光・蔷薇(海莲娜)", "zht_name": "絲絨時光‧薔薇(海蓮娜)", "en_name": "Velvet Time: Rose (Helena)", "kr_name": "벨벳 타임(로즈)(엘레나)", "type": "pow", "pow": "5212", "tec": "3486", "stm": "4044", "apl": "200", "skill1": "強烈スパイクD", "skill2": "灼熱のダンスB", "skill3": "内から湧き上がるスタミナ4", "sell": "2020/5/28", "resell": "2020/12/1", "break": "1", "special_fun": ""
  },
  {
    "id": "332_1", "girl": "nyotengu", "name": "ルミネイトチューブ(女天狗)", "zhs_name": "荧光管(女天狗)", "zht_name": "熒光管(女天狗)", "en_name": "Luminary Tube Dress (Nyotengu)", "kr_name": "루미네이트 튜브(뇨텐구)", "type": "stm", "pow": "4454", "tec": "3626", "stm": "4962", "apl": "200", "skill1": "強烈スパイクA", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2020/6/4", "resell": "2021/6/17 2022/6/23", "break": "1", "special_fun": ""
  },
  {
    "id": "332_2", "girl": "honoka", "name": "ルミネイトチューブ(ほのか)", "zhs_name": "荧光管(穗香)", "zht_name": "熒光管(穗香)", "en_name": "Luminary Tube Dress (Honoka)", "kr_name": "루미네이트 튜브(호노카)", "type": "stm", "pow": "4594", "tec": "3396", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "強烈スパイクF", "skill3": "内から湧き上がるスタミナ3", "sell": "2020/6/4", "resell": "2021/6/17 2022/6/23", "break": "1", "special_fun": ""
  },
  {
    "id": "332_3", "girl": "tamaki", "name": "ルミネイトチューブ(たまき)", "zhs_name": "荧光管(环)", "zht_name": "熒光管(環)", "en_name": "Luminary Tube Dress (Tamaki)", "kr_name": "루미네이트 튜브(타마키)", "type": "stm", "pow": "4594", "tec": "3396", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "強烈スパイクF", "skill3": "内から湧き上がるスタミナ3", "sell": "2020/6/4", "resell": "2021/6/17 2022/6/23", "break": "1", "special_fun": ""
  },
  {
    "id": "333", "girl": "marie", "name": "ジュエル・パール(マリー)", "zhs_name": "珍宝・珍珠(玛莉)", "zht_name": "珍寶‧珍珠(瑪莉)", "en_name": "Jewel Pearl (Marie)", "kr_name": "주얼 진주(마리)", "type": "tec", "pow": "3764", "tec": "5322", "stm": "3856", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "パール・テクニック", "skill3": "可憐なフェイント", "sell": "2020/6/6", "resell": "2020/10/29 2021/6/6 2022/6/6", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现淡粉色粒子效果(光之舞)。去年玛丽生日策划重病入脑科医院，今日出院。恭喜玛丽酱翻身。双绿卡+强力技能一雪耻辱"
  },
  {
    "id": "334_1", "girl": "kanna", "name": "レイニーフロッグ(カンナ)", "zhs_name": "雨蛙(神无)", "zht_name": "雨蛙(神無)", "en_name": "Rainy Frog (Kanna)", "kr_name": "레이니 프로그(칸나)", "type": "tec", "pow": "3466", "tec": "4982", "stm": "4194", "apl": "200", "skill1": "灼熱のダンスD", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2020/6/11", "resell": "2023/6/21", "break": "1", "special_fun": ""
  },
  {
    "id": "334_2", "girl": "marie", "name": "レイニーフロッグ(マリー)", "zhs_name": "雨蛙(玛莉)", "zht_name": "雨蛙(瑪莉)", "en_name": "Rainy Frog (Marie)", "kr_name": "레이니 프로그(마리)", "type": "tec", "pow": "3606", "tec": "5112", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "強烈なプレッシャーC", "skill3": "内から湧き上がるスタミナ3", "sell": "2020/6/11", "resell": "2023/6/21", "break": "1", "special_fun": ""
  },
  {
    "id": "334_3", "girl": "hitomi", "name": "レイニーフロッグ(ヒトミ)", "zhs_name": "雨蛙(瞳)", "zht_name": "雨蛙(瞳)", "en_name": "Rainy Frog (Hitomi)", "kr_name": "레이니 프로그(히토미)", "type": "tec", "pow": "3606", "tec": "5112", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "強烈なプレッシャーC", "skill3": "内から湧き上がるスタミナ3", "sell": "2020/6/11", "resell": "2023/6/21", "break": "1", "special_fun": ""
  },
  {
    "id": "334_4", "girl": "misaki", "name": "レイニーフロッグ(みさき)", "zhs_name": "雨蛙(海咲)", "zht_name": "雨蛙(海咲)", "en_name": "Rainy Frog (Misaki)", "kr_name": "레이니 프로그(미사키)", "type": "tec", "pow": "3606", "tec": "5112", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "強烈なプレッシャーC", "skill3": "内から湧き上がるスタミナ3", "sell": "2020/6/11", "resell": "2023/6/21", "break": "1", "special_fun": ""
  },
  {
    "id": "335", "girl": "monica", "name": "おつまみシュリンプ(モニカ)", "zhs_name": "拽拽衬衫(莫妮卡)", "zht_name": "", "en_name": "Appetizer Shrimp (Monica)", "kr_name": "에피타이저 쉬림프(모니카)", "type": "tec", "pow": "3426", "tec": "5162", "stm": "4054", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2020/6/17", "resell": "2021/7/21", "break": "1", "special_fun": "第二波可拉扯交互的衣服、允许多部分拉扯"
  },
  {
    "id": "336", "girl": "fiona", "name": "おつまみシュリンプ(フィオナ)", "zhs_name": "拽拽衬衫(菲欧娜)", "zht_name": "", "en_name": "Appetizer Shrimp (Fiona)", "kr_name": "에피타이저 쉬림프(피오나)", "type": "tec", "pow": "3486", "tec": "5212", "stm": "4044", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "驚異のスタミナE", "skill3": "閃きのテクニック6", "sell": "2020/6/17", "resell": "2021/7/21", "break": "1", "special_fun": "第二波可拉扯交互的衣服、允许多部分拉扯"
  },
  {
    "id": "337", "girl": "honoka", "name": "おつまみピンチョス(ほのか)", "zhs_name": "拽拽Pinchos(穗香)", "zht_name": "拽拽Pinchos(穗香)", "en_name": "Appetizer Pinchos (Honoka)", "kr_name": "애피타이저 핀초(호노카)", "type": "stm", "pow": "3776", "tec": "4124", "stm": "5142", "apl": "200", "skill1": "鉄壁のレシーブB", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2020/6/24", "resell": "2020/11/29 2021/10/14", "break": "1", "special_fun": "允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "338", "girl": "leifang", "name": "おつまみピンチョス(レイファン)", "zhs_name": "拽拽Pinchos(丽凤)", "zht_name": "拽拽Pinchos(麗鳳)", "en_name": "Appetizer Pinchos (Leifang)", "kr_name": "애피타이저 핀초(레이팡)", "type": "stm", "pow": "3776", "tec": "4124", "stm": "5142", "apl": "200", "skill1": "鉄壁のレシーブB", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2020/6/24", "resell": "2020/11/29 2021/10/14", "break": "1", "special_fun": "允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "339", "girl": "marie", "name": "スイートビターベリー(マリー)", "zhs_name": "甜涩浆果(玛莉)", "zht_name": "甜澀漿果(瑪莉)", "en_name": "Sweet Bitter Berry (Marie)", "kr_name": "스위트 비터 베리(마리)", "type": "stm", "pow": "3796", "tec": "4314", "stm": "4932", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2020/7/2", "resell": "2020/11/30 2021/6/10 2022/4/28 2023/4/20", "break": "1", "special_fun": ""
  },
  {
    "id": "340", "girl": "kasumi", "name": "スイートミルクベリー(かすみ)", "zhs_name": "奶甜浆果(霞)", "zht_name": "奶甜漿果(霞)", "en_name": "Sweet Milk Berry (Kasumi)", "kr_name": "스위트 밀크 베리(카스미)", "type": "stm", "pow": "3546", "tec": "4344", "stm": "5152", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "内から湧き上がるスタミナ3", "skill3": "可憐なフェイント", "sell": "2020/7/2", "resell": "2020/11/30 2021/6/10 2022/4/28 2023/4/20", "break": "1", "special_fun": ""
  },
  {
    "id": "341", "girl": "kokoro", "name": "スイートミルクベリー(こころ)", "zhs_name": "奶甜浆果(心)", "zht_name": "奶甜漿果(心)", "en_name": "Sweet Milk Berry (Kokoro)", "kr_name": "스위트 밀크 베리(코코로)", "type": "stm", "pow": "3546", "tec": "4344", "stm": "5152", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "内から湧き上がるスタミナ3", "skill3": "可憐なフェイント", "sell": "2020/7/2", "resell": "2020/11/30 2021/6/10 2022/4/28 2023/4/20", "break": "1", "special_fun": ""
  },
  {
    "id": "342", "girl": "misaki", "name": "ジュエル・ルビー(みさき)", "zhs_name": "珍宝・红宝石(海咲)", "zht_name": "珍寶‧紅寶石(海咲)", "en_name": "Jewel Ruby (Misaki)", "kr_name": "주얼 루비(미사키)", "type": "stm", "pow": "4654", "tec": "3366", "stm": "5322", "apl": "200", "skill1": "強烈スパイクE", "skill2": "ルビー・スタミナ", "skill3": "豪快なスパイク", "sell": "2020/7/7", "resell": "2020/10/29 2022/7/7 2023/7/7", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现金色粒子效果(光之舞) 策划出院了，设计师却喝假酒了，这衣服跟宝石主题有什么关系？确定不是花仙子主题？配色真的绝了！"
  },
  {
    "id": "343", "girl": "luna", "name": "メディカル・エックス(ルナ)", "zhs_name": "医疗・X(露娜)", "zht_name": "醫療・X(露娜)", "en_name": "Medical X (Luna)", "kr_name": "메디컬 엑스(루나)", "type": "tec", "pow": "3546", "tec": "5042", "stm": "4054", "apl": "200", "skill1": "高度な心理戦E", "skill2": "内から湧き上がるスタミナ4", "skill3": "可憐なフェイント", "sell": "2020/7/9", "resell": "2020/11/27 2023/5/19", "break": "1", "special_fun": "服装拥有透视效果，觉醒等级越高透视范围越大。帽子可设定隐藏"
  },
  {
    "id": "344", "girl": "sayuri", "name": "メディカル・エックス(さゆり)", "zhs_name": "医疗・X(小百合)", "zht_name": "醫療・X(小百合)", "en_name": "Medical X (Sayuri)", "kr_name": "메디컬 엑스(사유리)", "type": "tec", "pow": "3226", "tec": "5312", "stm": "4204", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "高度な心理戦B", "skill3": "閃きのテクニック5", "sell": "2020/7/9", "resell": "2020/11/27 2023/5/19", "break": "1", "special_fun": "服装拥有透视效果，觉醒等级越高透视范围越大。帽子可设定隐藏"
  },
  {
    "id": "345", "girl": "honoka", "name": "メディカル・エックス(ほのか)", "zhs_name": "医疗・X(穗香)", "zht_name": "醫療・X(穗香)", "en_name": "Medical X (Honoka)", "kr_name": "메디컬 엑스(호노카)", "type": "tec", "pow": "3226", "tec": "5312", "stm": "4204", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "高度な心理戦B", "skill3": "閃きのテクニック5", "sell": "2020/7/9", "resell": "2020/11/27 2023/5/19", "break": "1", "special_fun": "服装拥有透视效果，觉醒等级越高透视范围越大。帽子可设定隐藏"
  },
  {
    "id": "346", "girl": "nyotengu", "name": "メディカル・エックス(女天狗)", "zhs_name": "医疗・X(女天狗)", "zht_name": "醫療・X(女天狗)", "en_name": "Medical X (Nyotengu)", "kr_name": "메디컬 엑스(뇨텐구)", "type": "tec", "pow": "3226", "tec": "5312", "stm": "4204", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "高度な心理戦B", "skill3": "閃きのテクニック5", "sell": "2020/7/9", "resell": "2020/11/27 2023/5/19", "break": "1", "special_fun": "服装拥有透视效果，觉醒等级越高透视范围越大。帽子可设定隐藏"
  },
  {
    "id": "347_1", "girl": "kasumi", "name": "宇崎ちゃん・SUGOI DEKAI (かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_2", "girl": "honoka", "name": "宇崎ちゃん・SUGOI DEKAI (ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_3", "girl": "marie", "name": "宇崎ちゃん・SUGOI DEKAI (マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_4", "girl": "ayane", "name": "宇崎ちゃん・SUGOI DEKAI (あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_5", "girl": "nyotengu", "name": "宇崎ちゃん・SUGOI DEKAI (女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_6", "girl": "kokoro", "name": "宇崎ちゃん・SUGOI DEKAI (こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_7", "girl": "hitomi", "name": "宇崎ちゃん・SUGOI DEKAI (ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_8", "girl": "momiji", "name": "宇崎ちゃん・SUGOI DEKAI (紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_9", "girl": "helena", "name": "宇崎ちゃん・SUGOI DEKAI (エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_10", "girl": "misaki", "name": "宇崎ちゃん・SUGOI DEKAI (みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_11", "girl": "luna", "name": "宇崎ちゃん・SUGOI DEKAI (ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_12", "girl": "tamaki", "name": "宇崎ちゃん・SUGOI DEKAI (たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_13", "girl": "leifang", "name": "宇崎ちゃん・SUGOI DEKAI (レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_14", "girl": "fiona", "name": "宇崎ちゃん・SUGOI DEKAI (フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_15", "girl": "nagisa", "name": "宇崎ちゃん・SUGOI DEKAI (なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_16", "girl": "kanna", "name": "宇崎ちゃん・SUGOI DEKAI (カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_17", "girl": "monica", "name": "宇崎ちゃん・SUGOI DEKAI (モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "347_18", "girl": "sayuri", "name": "宇崎ちゃん・SUGOI DEKAI (さゆり)", "zhs_name": "艳阳绿叶(小百合)", "zht_name": "", "en_name": "Sunshine Leaf (Sayuri)", "kr_name": "선샤인 리프(사유리)", "type": "pow", "pow": "5022", "tec": "3526", "stm": "4194", "apl": "200", "skill1": "強烈スパイクE", "skill2": "強烈なプレッシャーB", "skill3": "SUGOIスタミナ", "sell": "2020/7/16", "resell": "", "break": "1", "special_fun": "SUGOI DEKAI联动服装。自带首饰可设定隐藏。最大觉醒时可使用胸垫增大。允许和本次的所有联动服装互相成为狗粮素材满觉。附带额外100经验 墙壁play回想。"
  },
  {
    "id": "348_1", "girl": "momiji", "name": "ダークプリズン(紅葉)", "zhs_name": "黑狱(红叶)", "zht_name": "暗黑監獄(紅葉)", "en_name": "Dark Prison (Momiji)", "kr_name": "다크프리즌(모미지)", "type": "tec", "pow": "3466", "tec": "4962", "stm": "4214", "apl": "200", "skill1": "高度な心理戦A", "skill2": "プラチナアタッカー", "skill3": "可憐なフェイント", "sell": "2020/7/23", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "348_2", "girl": "misaki", "name": "ダークプリズン(みさき)", "zhs_name": "黑狱(海咲)", "zht_name": "暗黑監獄(海咲)", "en_name": "Dark Prison (Misaki)", "kr_name": "다크프리즌(미사키)", "type": "tec", "pow": "3526", "tec": "5232", "stm": "3984", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "灼熱のダンスC", "skill3": "閃きのテクニック3", "sell": "2020/7/23", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "348_3", "girl": "leifang", "name": "ダークプリズン(レイファン)", "zhs_name": "黑狱(丽凤)", "zht_name": "暗黑監獄(麗鳳)", "en_name": "Dark Prison (Leifang)", "kr_name": "다크프리즌(레이팡)", "type": "tec", "pow": "3526", "tec": "5232", "stm": "3984", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "灼熱のダンスC", "skill3": "閃きのテクニック3", "sell": "2020/7/23", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "349", "girl": "patty", "name": "ジュエル・ルビー(パティ)", "zhs_name": "珍宝・红宝石(派蒂)", "zht_name": "珍寶‧紅寶石(派蒂)", "en_name": "Jewel Ruby (Patty)", "kr_name": "주얼 루비(패티)", "type": "stm", "pow": "4704", "tec": "3316", "stm": "5322", "apl": "200", "skill1": "強烈スパイクE", "skill2": "ルビー・スタミナ", "skill3": "豪快なスパイク", "sell": "2020/7/31", "resell": "2020/10/29 2021/7/31 2022/7/31 2023/7/31", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现金色粒子效果(光之舞) 。破案了，misaki生日诡异的外形主题和金黄的智商配色，原来是patty生日改色啊。"
  },
  {
    "id": "350", "girl": "patty", "name": "ステラ・レオ(パティ)", "zhs_name": "星辰・狮子(派蒂)", "zht_name": "星辰·獅子(派蒂)", "en_name": "Stellar Leo (Patty)", "kr_name": "스텔라 레오(패티)", "type": "pow", "pow": "5322", "tec": "3984", "stm": "3894", "apl": "200", "skill1": "強烈スパイクD", "skill2": "レオ・パワー", "skill3": "豪快なスパイク", "sell": "2020/7/31", "resell": "2021/7/31 2021/9/16 2022/7/31 2022/9/8 2023/7/31", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现粒子效果(光之舞) 服装拥有炸裂效果(碎片满天飞)"
  },
  {
    "id": "351", "girl": "nagisa", "name": "ソーダ・フロート(なぎさ)", "zhs_name": "苏打浮浮(凪咲)", "zht_name": "蘇打浮浮(凪咲)", "en_name": "Soda Float (Nagisa)", "kr_name": "소다 플로트(나기사)", "type": "stm", "pow": "3416", "tec": "4484", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "内から湧き上がるスタミナ4", "skill3": "可憐なフェイント", "sell": "2020/7/31", "resell": "2021/2/4", "break": "1", "special_fun": ""
  },
  {
    "id": "352", "girl": "marie", "name": "レモン・フロート(マリー)", "zhs_name": "柠檬浮浮(玛莉)", "zht_name": "檸檬浮浮(瑪莉)", "en_name": "Lemon Float (Marie)", "kr_name": "레몬 플로트(마리)", "type": "stm", "pow": "3696", "tec": "4214", "stm": "5232", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "完璧なレシーブA", "skill3": "内から湧き上がるスタミナ6", "sell": "2020/7/31", "resell": "2021/2/4", "break": "1", "special_fun": ""
  },
  {
    "id": "353", "girl": "kanna", "name": "レモン・フロート(カンナ)", "zhs_name": "柠檬浮浮(神无)", "zht_name": "檸檬浮浮(神無)", "en_name": "Lemon Float (Kanna)", "kr_name": "레몬 플로트(칸나)", "type": "stm", "pow": "3696", "tec": "4214", "stm": "5232", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "完璧なレシーブA", "skill3": "内から湧き上がるスタミナ6", "sell": "2020/7/31", "resell": "2021/2/4", "break": "1", "special_fun": ""
  },
  {
    "id": "354", "girl": "ayane", "name": "ジュエル・ペリドット(あやね)", "zhs_name": "珍宝・橄榄石(绫音)", "zht_name": "珍寶‧橄欖石(綾音)", "en_name": "Jewel Peridot (Ayane)", "kr_name": "주얼 페리도트(아야네)", "type": "stm", "pow": "3326", "tec": "4694", "stm": "5322", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ペリドット・スタミナ", "skill3": "可憐なフェイント", "sell": "2020/8/5", "resell": "2020/10/29 2021/8/5 2022/8/5 2023/8/5", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现紫色粒子效果(光之舞)"
  },
  {
    "id": "355_1", "girl": "misaki", "name": "レイズザセイル(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4314", "tec": "3606", "stm": "5222", "apl": "200", "skill1": "灼熱のダンスA", "skill2": "驚異のスタミナC", "skill3": "順風満帆のスタミナ", "sell": "2020/8/7", "resell": "2020/12/5 2021/8/12 2022/8/10", "break": "1", "special_fun": ""
  },
  {
    "id": "355_2", "girl": "nyotengu", "name": "レイズザセイル(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4314", "tec": "3606", "stm": "5222", "apl": "200", "skill1": "灼熱のダンスA", "skill2": "驚異のスタミナC", "skill3": "順風満帆のスタミナ", "sell": "2020/8/7", "resell": "2020/12/5 2021/8/12 2022/8/10", "break": "1", "special_fun": ""
  },
  {
    "id": "355_3", "girl": "helena", "name": "レイズザセイル(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4314", "tec": "3606", "stm": "5222", "apl": "200", "skill1": "灼熱のダンスA", "skill2": "驚異のスタミナC", "skill3": "順風満帆のスタミナ", "sell": "2020/8/7", "resell": "2020/12/5 2021/8/12 2022/8/10", "break": "1", "special_fun": ""
  },
  {
    "id": "355_4", "girl": "luna", "name": "レイズザセイル(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3506", "tec": "5172", "stm": "4064", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "驚異のスタミナC", "skill3": "順風満帆のテクニック", "sell": "2020/8/7", "resell": "2020/12/5 2021/8/12 2022/8/10", "break": "1", "special_fun": ""
  },
  {
    "id": "355_5", "girl": "ayane", "name": "レイズザセイル(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3506", "tec": "5172", "stm": "4064", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "驚異のスタミナC", "skill3": "順風満帆のテクニック", "sell": "2020/8/7", "resell": "2020/12/5 2021/8/12 2022/8/10", "break": "1", "special_fun": ""
  },
  {
    "id": "355_6", "girl": "sayuri", "name": "レイズザセイル(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3506", "tec": "5172", "stm": "4064", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "驚異のスタミナC", "skill3": "順風満帆のテクニック", "sell": "2020/8/7", "resell": "2020/12/5 2021/8/12 2022/8/10", "break": "1", "special_fun": ""
  },
  {
    "id": "355_7", "girl": "tamaki", "name": "レイズザセイル(たまき)", "zhs_name": "扬帆", "zht_name": "", "en_name": "Raise The Sail", "kr_name": "레이즈 더 세일", "type": "pow", "pow": "5172", "tec": "3506", "stm": "4064", "apl": "200", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナC", "skill3": "順風満帆のパワー", "sell": "2020/8/7", "resell": "2020/12/5 2021/8/12 2022/8/10", "break": "1", "special_fun": ""
  },
  {
    "id": "355_8", "girl": "fiona", "name": "レイズザセイル(フィオナ)", "zhs_name": "扬帆", "zht_name": "", "en_name": "Raise The Sail", "kr_name": "레이즈 더 세일", "type": "pow", "pow": "5172", "tec": "3506", "stm": "4064", "apl": "200", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナC", "skill3": "順風満帆のパワー", "sell": "2020/8/7", "resell": "2020/12/5 2021/8/12 2022/8/10", "break": "1", "special_fun": ""
  },
  {
    "id": "355_9", "girl": "momiji", "name": "レイズザセイル(紅葉)", "zhs_name": "扬帆", "zht_name": "", "en_name": "Raise The Sail", "kr_name": "레이즈 더 세일", "type": "pow", "pow": "5172", "tec": "3506", "stm": "4064", "apl": "200", "skill1": "強烈スパイクA", "skill2": "驚異のスタミナC", "skill3": "順風満帆のパワー", "sell": "2020/8/7", "resell": "2020/12/5 2021/8/12 2022/8/10", "break": "1", "special_fun": ""
  },
  {
    "id": "356", "girl": "ayane", "name": "やわらかエンジンTシャツ(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3546", "tec": "4872", "stm": "3924", "apl": "200", "skill1": "高度な心理戦D", "skill2": "驚異のスタミナF", "skill3": "閃きのテクニック3", "sell": "2020/8/18", "resell": "2021/8/14", "break": "1", "special_fun": "日服追加steam平台登陆入口。任务赠送"
  },
  {
    "id": "357", "girl": "hitomi", "name": "サンセットフィッシュ(ヒトミ)", "zhs_name": "日暮之鱼(瞳)", "zht_name": "日暮之魚(瞳)", "en_name": "Sunset Fish (Hitomi)", "kr_name": "선셋 피시(히토미)", "type": "tec", "pow": "3636", "tec": "5162", "stm": "3944", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "灼熱のダンスE", "skill3": "閃きのテクニック6", "sell": "2020/8/18", "resell": "2022/1/13 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "358", "girl": "honoka", "name": "サンセットフィッシュ(ほのか)", "zhs_name": "日暮之鱼(穗香)", "zht_name": "日暮之魚(穗香)", "en_name": "Sunset Fish (Honoka)", "kr_name": "선셋 피시(호노카)", "type": "tec", "pow": "3636", "tec": "5162", "stm": "3944", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "灼熱のダンスE", "skill3": "閃きのテクニック6", "sell": "2020/8/18", "resell": "2022/1/13 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "359", "girl": "monica", "name": "サンセットフィッシュ(モニカ)", "zhs_name": "日暮之鱼(莫妮卡)", "zht_name": "日暮之魚(莫妮卡)", "en_name": "Sunset Fish (Monica)", "kr_name": "선셋 피시(모니카)", "type": "tec", "pow": "3636", "tec": "5162", "stm": "3944", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "灼熱のダンスE", "skill3": "閃きのテクニック6", "sell": "2020/8/18", "resell": "2022/1/13 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "360", "girl": "kanna", "name": "サンセットフィッシュ(カンナ)", "zhs_name": "日暮之鱼(神无)", "zht_name": "日暮之魚(神無)", "en_name": "Sunset Fish (Kanna)", "kr_name": "선셋 피시(칸나)", "type": "tec", "pow": "3636", "tec": "5162", "stm": "3944", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "灼熱のダンスE", "skill3": "閃きのテクニック6", "sell": "2020/8/18", "resell": "2022/1/13 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "361", "girl": "leifang", "name": "サンセットフィッシュ(レイファン)", "zhs_name": "日暮之鱼(丽凤)", "zht_name": "日暮之魚(麗鳳)", "en_name": "Sunset Fish (Leifang)", "kr_name": "선셋 피시(레이팡)", "type": "tec", "pow": "3636", "tec": "5162", "stm": "3944", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "灼熱のダンスE", "skill3": "閃きのテクニック6", "sell": "2020/8/18", "resell": "2022/1/13 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "362", "girl": "kasumi", "name": "トワイライトフィッシュ(かすみ)", "zhs_name": "拂晓之鱼(霞)", "zht_name": "拂曉之魚(霞)", "en_name": "Twilight Fish (Kasumi)", "kr_name": "트와일라이트 피시(카스미)", "type": "tec", "pow": "3716", "tec": "4942", "stm": "3984", "apl": "200", "skill1": "天才的な先読みB", "skill2": "閃きのテクニック3", "skill3": "熱烈なエール", "sell": "2020/8/18", "resell": "2022/1/13 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "363", "girl": "marie", "name": "トワイライトフィッシュ(マリー)", "zhs_name": "拂晓之鱼(玛莉)", "zht_name": "拂曉之魚(瑪莉)", "en_name": "Twilight Fish (Marie)", "kr_name": "트와일라이트 피시(마리)", "type": "tec", "pow": "3716", "tec": "4942", "stm": "3984", "apl": "200", "skill1": "天才的な先読みB", "skill2": "閃きのテクニック3", "skill3": "熱烈なエール", "sell": "2020/8/18", "resell": "2022/1/13 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "364", "girl": "nagisa", "name": "トワイライトフィッシュ(なぎさ)", "zhs_name": "拂晓之鱼(凪咲)", "zht_name": "拂曉之魚(凪咲)", "en_name": "Twilight Fish (Nagisa)", "kr_name": "트와일라이트 피시(나기사)", "type": "tec", "pow": "3716", "tec": "4942", "stm": "3984", "apl": "200", "skill1": "天才的な先読みB", "skill2": "閃きのテクニック3", "skill3": "熱烈なエール", "sell": "2020/8/18", "resell": "2022/1/13 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "365", "girl": "kokoro", "name": "トワイライトフィッシュ(こころ)", "zhs_name": "拂晓之鱼(心)", "zht_name": "拂曉之魚(心)", "en_name": "Twilight Fish (Kokoro)", "kr_name": "트와일라이트 피시(코코로)", "type": "tec", "pow": "3716", "tec": "4942", "stm": "3984", "apl": "200", "skill1": "天才的な先読みB", "skill2": "閃きのテクニック3", "skill3": "熱烈なエール", "sell": "2020/8/18", "resell": "2022/1/13 2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "366", "girl": "tamaki", "name": "ジュエル・ペリドット(たまき)", "zhs_name": "珍宝・橄榄石(环)", "zht_name": "珍寶‧橄欖石(環)", "en_name": "Jewel Peridot (Tamaki)", "kr_name": "주얼 페리도트(타마키)", "type": "stm", "pow": "4674", "tec": "3346", "stm": "5322", "apl": "200", "skill1": "強烈スパイクE", "skill2": "ペリドット・スタミナ", "skill3": "豪快なスパイク", "sell": "2020/8/19", "resell": "2020/10/29 2021/8/19 2022/8/19", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现绿色粒子效果(光之舞) 。充值成功，SSR饰品技能冲突已消除。"
  },
  {
    "id": "367", "girl": "tsukushi", "name": "ビーアンビシャス(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3784", "tec": "5262", "stm": "3696", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "驚異のスタミナE", "skill3": "閃きのテクニック3", "sell": "2020/8/26", "resell": "2020/10/24", "break": "1", "special_fun": "为什么同样的外衣，脱掉裤子，换上花边过膝袜就贵了好几千呢（滑稽）"
  },
  {
    "id": "225_17", "girl": "sayuri", "name": "すずかぜロマンチカ(さゆり)", "zhs_name": "凉风罗曼(小百合)", "zht_name": "涼風羅曼(小百合)", "en_name": "Breeze Romantika (Sayuri)", "kr_name": "산들바람 로맨티카(사유리)", "type": "tec", "pow": "3586", "tec": "5002", "stm": "4054", "apl": "200", "skill1": "鉄壁のレシーブA", "skill2": "閃きのテクニック3", "skill3": "熱烈なエール", "sell": "2020/8/27", "resell": "2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_18", "girl": "monica", "name": "すずかぜロマンチカ(モニカ)", "zhs_name": "凉风罗曼(莫妮卡)", "zht_name": "涼風羅曼(莫妮卡)", "en_name": "Breeze Romantika (Monica)", "kr_name": "산들바람 로맨티카(모니카)", "type": "tec", "pow": "3486", "tec": "5102", "stm": "4154", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "高度な心理戦D", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/8/27", "resell": "2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "368", "girl": "fiona", "name": "ヴィーナス・ケージ(フィオナ)", "zhs_name": "维纳斯之栅(菲欧娜)", "zht_name": "", "en_name": "Venus Cage (Fiona)", "kr_name": "비너스 케이지(피오나)", "type": "stm", "pow": "3556", "tec": "4394", "stm": "5092", "apl": "200", "skill1": "高度な心理戦B", "skill2": "内から湧き上がるスタミナ3", "skill3": "可憐なフェイント", "sell": "2020/9/3", "resell": "2021/4/22 2022/1/28", "break": "1", "special_fun": ""
  },
  {
    "id": "369", "girl": "helena", "name": "ヴィーナス・ケージ(エレナ)", "zhs_name": "维纳斯之栅(海莲娜)", "zht_name": "", "en_name": "Venus Cage (Helena)", "kr_name": "비너스 케이지(엘레나)", "type": "stm", "pow": "3346", "tec": "4674", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "裏の裏を突くフェイントD", "skill3": "内から湧き上がるスタミナ6", "sell": "2020/9/3", "resell": "2021/4/22 2022/1/28", "break": "1", "special_fun": ""
  },
  {
    "id": "370", "girl": "kasumi", "name": "ヴィーナス・ケージ(かすみ)", "zhs_name": "维纳斯之栅(霞)", "zht_name": "", "en_name": "Venus Cage (Kasumi)", "kr_name": "비너스 케이지(카스미)", "type": "stm", "pow": "3346", "tec": "4674", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "裏の裏を突くフェイントD", "skill3": "内から湧き上がるスタミナ6", "sell": "2020/9/3", "resell": "2021/4/22 2022/1/28", "break": "1", "special_fun": ""
  },
  {
    "id": "371", "girl": "hitomi", "name": "シークレットクラス(ヒトミ)", "zhs_name": "秘密课堂(瞳)", "zht_name": "", "en_name": "Secret Class (Hitomi)", "kr_name": "시크릿 클래스(히토미)", "type": "pow", "pow": "4942", "tec": "3874", "stm": "3826", "apl": "200", "skill1": "圧倒的な気迫C", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2020/9/10", "resell": "2020/12/6 2022/4/21", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "372", "girl": "ayane", "name": "シークレットクラス(あやね)", "zhs_name": "秘密课堂(绫音)", "zht_name": "", "en_name": "Secret Class (Ayane)", "kr_name": "시크릿 클래스(아야네)", "type": "pow", "pow": "5102", "tec": "3824", "stm": "3816", "apl": "200", "skill1": "圧倒的な気迫B", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー5", "sell": "2020/9/10", "resell": "2020/12/6 2022/4/21", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "373", "girl": "misaki", "name": "シークレットクラス(みさき)", "zhs_name": "秘密课堂(海咲)", "zht_name": "", "en_name": "Secret Class (Misaki)", "kr_name": "시크릿 클래스(미사키)", "type": "pow", "pow": "5102", "tec": "3824", "stm": "3816", "apl": "200", "skill1": "圧倒的な気迫B", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー5", "sell": "2020/9/10", "resell": "2020/12/6 2022/4/21", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "374", "girl": "nagisa", "name": "シークレットクラス(なぎさ)", "zhs_name": "秘密课堂(凪咲)", "zht_name": "", "en_name": "Secret Class (Nagisa)", "kr_name": "시크릿 클래스(나기사)", "type": "pow", "pow": "5102", "tec": "3824", "stm": "3816", "apl": "200", "skill1": "圧倒的な気迫B", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー5", "sell": "2020/9/10", "resell": "2020/12/6 2022/4/21", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "375", "girl": "kanna", "name": "ジュエル・サファイア(カンナ)", "zhs_name": "珍宝・蓝宝石(神无)", "zht_name": "珍寶‧藍寶石(神無)", "en_name": "Jewel Sapphire (Kanna)", "kr_name": "주얼 사파이어(칸나)", "type": "stm", "pow": "4714", "tec": "3306", "stm": "5322", "apl": "200", "skill1": "強烈スパイクE", "skill2": "サファイア・スタミナ", "skill3": "豪快なスパイク", "sell": "2020/9/15", "resell": "2020/10/29 2021/9/15 2022/9/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现橙色粒子效果(光之舞) "
  },
  {
    "id": "376", "girl": "tsukushi", "name": "シンデレラハート(つくし)", "zhs_name": "灰姑娘之心(筑紫)", "zht_name": "灰姑娘之心(筑紫)", "en_name": "Cinderella Heart (Tsukushi)", "kr_name": "신데렐라 하트(츠쿠시)", "type": "stm", "pow": "3416", "tec": "4564", "stm": "5062", "apl": "200", "skill1": "高度な心理戦E", "skill2": "内から湧き上がるスタミナ4", "skill3": "可憐なフェイント", "sell": "2020/9/17", "resell": "2020/10/24", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "377", "girl": "nyotengu", "name": "ベルベットタイム・ルージュ(女天狗)", "zhs_name": "丝绒时光・胭脂(女天狗)", "zht_name": "絲絨時光‧胭脂(女天狗)", "en_name": "Velvet Time: Rouge (Nyotengu)", "kr_name": "벨벳 타임(루주)(뇨텐구)", "type": "tec", "pow": "3366", "tec": "5072", "stm": "4204", "apl": "200", "skill1": "天才的な先読みB", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2020/9/17", "resell": "2021/7/9 2022/9/18 2023/4/20", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "378", "girl": "honoka", "name": "ベルベットタイム・ローズ(ほのか)", "zhs_name": "丝绒时光・蔷薇(穗香)", "zht_name": "絲絨時光‧薔薇(穗香)", "en_name": "Velvet Time: Rose (Honoka)", "kr_name": "벨벳 타임(로즈)(호노카)", "type": "tec", "pow": "3486", "tec": "5212", "stm": "4044", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦C", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/9/17", "resell": "2021/7/9 2022/9/18 2023/4/20", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "379", "girl": "luna", "name": "ベルベットタイム・ローズ(ルナ)", "zhs_name": "丝绒时光・蔷薇(露娜)", "zht_name": "絲絨時光‧薔薇(露娜)", "en_name": "Velvet Time: Rose (Luna)", "kr_name": "벨벳 타임(로즈)(루나)", "type": "tec", "pow": "3486", "tec": "5212", "stm": "4044", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦C", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/9/17", "resell": "2021/7/9 2022/9/18 2023/4/20", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "380", "girl": "momiji", "name": "ジュエル・サファイア(紅葉)", "zhs_name": "珍宝・蓝宝石(红叶)", "zht_name": "", "en_name": "Jewel Sapphire (Momiji)", "kr_name": "주얼 사파이어(모미지)", "type": "tec", "pow": "3476", "tec": "5322", "stm": "4144", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "サファイア・テクニック", "skill3": "可憐なフェイント", "sell": "2020/9/20", "resell": "2020/10/29 2021/9/20 2022/9/20", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现蓝色粒子效果(光之舞)"
  },
  {
    "id": "381", "girl": "patty", "name": "純白のスリットワンピ(パティ)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/9/23", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。能不能不要再炒冷饭了，1个季度做不出1件新衣服丢不丢人？"
  },
  {
    "id": "382", "girl": "marie", "name": "純白のスリットワンピ(マリー)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/9/23", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。能不能不要再炒冷饭了，1个季度做不出1件新衣服丢不丢人？"
  },
  {
    "id": "383", "girl": "tamaki", "name": "純白のスリットワンピ(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3684", "tec": "4126", "stm": "5232", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ3", "skill3": "可憐なフェイント", "sell": "2020/9/23", "resell": "", "break": "1", "special_fun": "能不能不要再炒冷饭了，1个季度做不出1件新衣服丢不丢人？"
  },
  {
    "id": "384_1", "girl": "helena", "name": "デスチャ・シトリーコスチューム(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_2", "girl": "kokoro", "name": "デスチャ・シトリーコスチューム(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_3", "girl": "marie", "name": "デスチャ・シトリーコスチューム(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_4", "girl": "honoka", "name": "デスチャ・シトリーコスチューム(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_5", "girl": "misaki", "name": "デスチャ・シトリーコスチューム(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_6", "girl": "kasumi", "name": "デスチャ・シトリーコスチューム(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_7", "girl": "ayane", "name": "デスチャ・シトリーコスチューム(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_8", "girl": "hitomi", "name": "デスチャ・シトリーコスチューム(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_9", "girl": "nyotengu", "name": "デスチャ・シトリーコスチューム(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_10", "girl": "momiji", "name": "デスチャ・シトリーコスチューム(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_11", "girl": "kanna", "name": "デスチャ・シトリーコスチューム(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_12", "girl": "leifang", "name": "デスチャ・シトリーコスチューム(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_13", "girl": "monica", "name": "デスチャ・シトリーコスチューム(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_14", "girl": "nagisa", "name": "デスチャ・シトリーコスチューム(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_15", "girl": "fiona", "name": "デスチャ・シトリーコスチューム(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_16", "girl": "tamaki", "name": "デスチャ・シトリーコスチューム(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_17", "girl": "luna", "name": "デスチャ・シトリーコスチューム(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_18", "girl": "sayuri", "name": "デスチャ・シトリーコスチューム(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "384_19", "girl": "patty", "name": "デスチャ・シトリーコスチューム(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3636", "stm": "4004", "apl": "200", "skill1": "強烈スパイクC", "skill2": "シトリーのパワー", "skill3": "豪快なスパイク", "sell": "2020/9/29", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装，可使用其他天命之子联动服装/联动觉醒石觉醒。附带额外100经验回想,满觉CG增加求抱抱的剧情。截至登场时免费力量刷分衣服的天花板,19人超级大毒池。6步保底随机3选1。"
  },
  {
    "id": "385", "girl": "leifang", "name": "デスチャ・リザコスチューム(レイファン)", "zhs_name": "命运之子・丽莎服装(丽凤)", "zht_name": "命運之子‧麗莎服裝(麗鳳)", "en_name": "Destiny Child Lisa Costume (Leifang)", "kr_name": "데스티니 차일드 리자 코스튬(레이팡)", "type": "stm", "pow": "4524", "tec": "3436", "stm": "5182", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "強烈スパイクF", "skill3": "リザのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "386", "girl": "nagisa", "name": "デスチャ・リザコスチューム(なぎさ)", "zhs_name": "命运之子・丽莎服装(凪咲)", "zht_name": "命運之子‧麗莎服裝(凪咲)", "en_name": "Destiny Child Lisa Costume (Nagisa)", "kr_name": "데스티니 차일드 리자 코스튬(나기사)", "type": "stm", "pow": "4524", "tec": "3436", "stm": "5182", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "強烈スパイクF", "skill3": "リザのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "387", "girl": "ayane", "name": "デスチャ・リザコスチューム(あやね)", "zhs_name": "命运之子・丽莎服装(绫音)", "zht_name": "命運之子‧麗莎服裝(綾音)", "en_name": "Destiny Child Lisa Costume (Ayane)", "kr_name": "데스티니 차일드 리자 코스튬(아야네)", "type": "stm", "pow": "4524", "tec": "3436", "stm": "5182", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "強烈スパイクF", "skill3": "リザのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "388", "girl": "monica", "name": "デスチャ・リザコスチューム(モニカ)", "zhs_name": "命运之子・丽莎服装(莫妮卡)", "zht_name": "命運之子‧麗莎服裝(莫妮卡)", "en_name": "Destiny Child Lisa Costume (Monica)", "kr_name": "데스티니 차일드 리자 코스튬(모니카)", "type": "stm", "pow": "4524", "tec": "3436", "stm": "5182", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "強烈スパイクF", "skill3": "リザのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "389", "girl": "luna", "name": "デスチャ・ダビコスチューム(ルナ)", "zhs_name": "命运之子・妲比服装(露娜)", "zht_name": "命運之子‧妲比服裝(露娜)", "en_name": "Destiny Child Davi Costume (Luna)", "kr_name": "데스티니 차일드 다비 코스튬(루나)", "type": "stm", "pow": "4454", "tec": "3546", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "強烈スパイクD", "skill3": "ダビのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "390", "girl": "honoka", "name": "デスチャ・ダビコスチューム(ほのか)", "zhs_name": "命运之子・妲比服装(穗香)", "zht_name": "命運之子‧妲比服裝(穗香)", "en_name": "Destiny Child Davi Costume (Honoka)", "kr_name": "데스티니 차일드 다비 코스튬(호노카)", "type": "stm", "pow": "4454", "tec": "3546", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "強烈スパイクD", "skill3": "ダビのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "391", "girl": "kanna", "name": "デスチャ・ダビコスチューム(カンナ)", "zhs_name": "命运之子・妲比服装(神无)", "zht_name": "命運之子‧妲比服裝(神無)", "en_name": "Destiny Child Davi Costume (Kanna)", "kr_name": "데스티니 차일드 다비 코스튬(칸나)", "type": "stm", "pow": "4454", "tec": "3546", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "強烈スパイクD", "skill3": "ダビのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "392", "girl": "kokoro", "name": "デスチャ・モナコスチューム(こころ)", "zhs_name": "命运之子・莫娜服装(心)", "zht_name": "命運之子‧莫娜服裝(心)", "en_name": "Destiny Child Mona Costume (Kokoro)", "kr_name": "데스티니 차일드 모나 코스튬(코코로)", "type": "stm", "pow": "4434", "tec": "3576", "stm": "5132", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "強烈スパイクC", "skill3": "モナのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "393", "girl": "sayuri", "name": "デスチャ・モナコスチューム(さゆり)", "zhs_name": "命运之子・莫娜服装(小百合)", "zht_name": "命運之子‧莫娜服裝(小百合)", "en_name": "Destiny Child Mona Costume (Sayuri)", "kr_name": "데스티니 차일드 모나 코스튬(사유리)", "type": "stm", "pow": "4434", "tec": "3576", "stm": "5132", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "強烈スパイクC", "skill3": "モナのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "394", "girl": "nyotengu", "name": "デスチャ・モナコスチューム(女天狗)", "zhs_name": "命运之子・莫娜服装(女天狗)", "zht_name": "命運之子‧莫娜服裝(女天狗)", "en_name": "Destiny Child Mona Costume (Nyotengu)", "kr_name": "데스티니 차일드 모나 코스튬(뇨텐구)", "type": "stm", "pow": "4434", "tec": "3576", "stm": "5132", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "強烈スパイクC", "skill3": "モナのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "395", "girl": "helena", "name": "デスチャ・モナコスチューム(エレナ)", "zhs_name": "命运之子・莫娜服装(海莲娜)", "zht_name": "命運之子‧莫娜服裝(海蓮娜)", "en_name": "Destiny Child Mona Costume (Helena)", "kr_name": "데스티니 차일드 모나 코스튬(엘레나)", "type": "stm", "pow": "4434", "tec": "3576", "stm": "5132", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "強烈スパイクC", "skill3": "モナのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "396", "girl": "hitomi", "name": "デスチャ・イブコスチューム(ヒトミ)", "zhs_name": "命运之子・夏娃服装(瞳)", "zht_name": "命運之子‧夏娃服裝(瞳)", "en_name": "Destiny Child Eve Costume (Hitomi)", "kr_name": "데스티니 차일드 이브 코스튬(히토미)", "type": "stm", "pow": "4584", "tec": "3456", "stm": "5102", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "強烈スパイクB", "skill3": "イブのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "397", "girl": "fiona", "name": "デスチャ・イブコスチューム(フィオナ)", "zhs_name": "命运之子・夏娃服装(菲欧娜)", "zht_name": "命運之子‧夏娃服裝(菲歐娜)", "en_name": "Destiny Child Eve Costume (Fiona)", "kr_name": "데스티니 차일드 이브 코스튬(피오나)", "type": "stm", "pow": "4584", "tec": "3456", "stm": "5102", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "強烈スパイクB", "skill3": "イブのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "398", "girl": "patty", "name": "デスチャ・イブコスチューム(パティ)", "zhs_name": "命运之子・夏娃服装(派蒂)", "zht_name": "命運之子‧夏娃服裝(派蒂)", "en_name": "Destiny Child Eve Costume (Patty)", "kr_name": "데스티니 차일드 이브 코스튬(패티)", "type": "stm", "pow": "4584", "tec": "3456", "stm": "5102", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "強烈スパイクB", "skill3": "イブのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "399", "girl": "momiji", "name": "デスチャ・イブコスチューム(紅葉)", "zhs_name": "命运之子・夏娃服装(红叶)", "zht_name": "命運之子‧夏娃服裝(紅葉)", "en_name": "Destiny Child Eve Costume (Momiji)", "kr_name": "데스티니 차일드 이브 코스튬(모미지)", "type": "stm", "pow": "4584", "tec": "3456", "stm": "5102", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "強烈スパイクB", "skill3": "イブのスタミナ", "sell": "2020/10/7", "resell": "", "break": "1", "special_fun": "Destiny Child 天命之子 第2次联动服装（冷饭），可使用其他天命之子联动服装/联动觉醒石觉醒"
  },
  {
    "id": "400", "girl": "luna", "name": "ジュエル・オパール(ルナ)", "zhs_name": "珍宝・蛋白石(露娜)", "zht_name": "珍寶‧蛋白石(露娜)", "en_name": "Jewel Opal (Luna)", "kr_name": "주얼 오팔(루나)", "type": "tec", "pow": "3436", "tec": "5322", "stm": "4184", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "オパール・テクニック", "skill3": "可憐なフェイント", "sell": "2020/10/15", "resell": "2020/10/29 2021/10/15 2022/10/15", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现白色粒子效果(光之舞)。"
  },
  {
    "id": "401", "girl": "misaki", "name": "秋麗のスクールウェア(みさき)", "zhs_name": "秋季校服(海咲)", "zht_name": "秋季校服(海咲)", "en_name": "Autumn Schoolwear (Misaki)", "kr_name": "아름다운 가을 학생복(미사키)", "type": "pow", "pow": "5032", "tec": "3616", "stm": "3994", "apl": "200", "skill1": "不動のレシーブF", "skill2": "秘められたパワー3", "skill3": "熱烈なエール", "sell": "2020/10/15", "resell": "2020/11/25 2021/2/25 2021/9/9 2022/11/30", "break": "1", "special_fun": ""
  },
  {
    "id": "402", "girl": "patty", "name": "秋麗のスクールウェア(パティ)", "zhs_name": "秋季校服(派蒂)", "zht_name": "秋季校服(派蒂)", "en_name": "Autumn Schoolwear (Patty)", "kr_name": "아름다운 가을 학생복(패티)", "type": "pow", "pow": "4972", "tec": "3536", "stm": "4234", "apl": "200", "skill1": "強烈スパイクD", "skill2": "圧倒的な気迫E", "skill3": "秘められたパワー6", "sell": "2020/10/15", "resell": "2020/11/25 2021/2/25 2021/9/9 2022/11/30", "break": "1", "special_fun": ""
  },
  {
    "id": "403", "girl": "fiona", "name": "秋麗のスクールウェア(フィオナ)", "zhs_name": "秋季校服(菲欧娜)", "zht_name": "秋季校服(菲歐娜)", "en_name": "Autumn Schoolwear (Fiona)", "kr_name": "아름다운 가을 학생복(피오나)", "type": "pow", "pow": "4972", "tec": "3536", "stm": "4234", "apl": "200", "skill1": "強烈スパイクD", "skill2": "圧倒的な気迫E", "skill3": "秘められたパワー6", "sell": "2020/10/15", "resell": "2020/11/25 2021/2/25 2021/9/9 2022/11/30", "break": "1", "special_fun": ""
  },
  {
    "id": "404", "girl": "kokoro", "name": "秋麗のスクールウェア(こころ)", "zhs_name": "秋季校服(心)", "zht_name": "秋季校服(心)", "en_name": "Autumn Schoolwear (Kokoro)", "kr_name": "아름다운 가을 학생복(코코로)", "type": "pow", "pow": "4972", "tec": "3536", "stm": "4234", "apl": "200", "skill1": "強烈スパイクD", "skill2": "圧倒的な気迫E", "skill3": "秘められたパワー6", "sell": "2020/10/15", "resell": "2020/11/25 2021/2/25 2021/9/9 2022/11/30", "break": "1", "special_fun": ""
  },
  {
    "id": "405_1", "girl": "kasumi", "name": "ブラッディ・キッス(かすみ)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_2", "girl": "honoka", "name": "ブラッディ・キッス(ほのか)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_3", "girl": "marie", "name": "ブラッディ・キッス(マリー)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_4", "girl": "ayane", "name": "ブラッディ・キッス(あやね)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_5", "girl": "nyotengu", "name": "ブラッディ・キッス(女天狗)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_6", "girl": "kokoro", "name": "ブラッディ・キッス(こころ)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_7", "girl": "hitomi", "name": "ブラッディ・キッス(ヒトミ)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_8", "girl": "momiji", "name": "ブラッディ・キッス(紅葉)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_9", "girl": "helena", "name": "ブラッディ・キッス(エレナ)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_10", "girl": "misaki", "name": "ブラッディ・キッス(みさき)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_11", "girl": "luna", "name": "ブラッディ・キッス(ルナ)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_12", "girl": "tamaki", "name": "ブラッディ・キッス(たまき)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_13", "girl": "leifang", "name": "ブラッディ・キッス(レイファン)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_14", "girl": "fiona", "name": "ブラッディ・キッス(フィオナ)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_15", "girl": "nagisa", "name": "ブラッディ・キッス(なぎさ)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_16", "girl": "kanna", "name": "ブラッディ・キッス(カンナ)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_17", "girl": "monica", "name": "ブラッディ・キッス(モニカ)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_18", "girl": "sayuri", "name": "ブラッディ・キッス(さゆり)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "405_19", "girl": "patty", "name": "ブラッディ・キッス(パティ)", "zhs_name": "血腥之吻", "zht_name": "", "en_name": "Bloody Kiss", "kr_name": "블러디 키스", "type": "tec", "pow": "3556", "tec": "4982", "stm": "4104", "apl": "200", "skill1": "高度な心理戦E", "skill2": "吸血鬼のテクニック", "skill3": "可憐なフェイント", "sell": "2020/10/22", "resell": "2021/10/3 2023/8/4", "break": "1", "special_fun": "可切换到红眼吸血鬼皮肤。附带10经验回想"
  },
  {
    "id": "406", "girl": "tsukushi", "name": "ステラ・スコルピオン(つくし)", "zhs_name": "星辰‧天蝎(筑紫)", "zht_name": "", "en_name": "Stellar Scorpion (Tsukushi)", "kr_name": "스텔라 스콜피온(츠쿠시)", "type": "tec", "pow": "3626", "tec": "5322", "stm": "3994", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "スコルピオン・テクニック", "skill3": "可憐なフェイント", "sell": "2020/10/24", "resell": "2021/9/16 2021/10/24 2022/9/8 2022/10/24", "break": "1", "special_fun": "SSR饰品技能冲突！贴图换色坑一波。使用天狗扇 扇动的时候 会出现黄色粒子效果(光之舞)。"
  },
  {
    "id": "407", "girl": "tsukushi", "name": "ジュエル・オパール(つくし)", "zhs_name": "珍宝・蛋白石(筑紫)", "zht_name": "珍寶‧蛋白石(筑紫)", "en_name": "Jewel Opal (Tsukushi)", "kr_name": "주얼 오팔(츠쿠시)", "type": "stm", "pow": "3376", "tec": "4644", "stm": "5322", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "オパール・スタミナ", "skill3": "可憐なフェイント", "sell": "2020/10/24", "resell": "2021/10/24 2022/10/24", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现白色粒子效果(光之舞)。"
  },
  {
    "id": "408", "girl": "kanna", "name": "恋色いろは(カンナ)", "zhs_name": "恋色伊吕波(神无)", "zht_name": "戀色伊呂波(神無)", "en_name": "Maple Romance (Kanna)", "kr_name": "사랑빛 이로하(칸나)", "type": "tec", "pow": "3944", "tec": "4932", "stm": "3766", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2020/10/29", "resell": "2021/11/2 2022/9/29", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现落叶，喷水会使叶子颜色变化"
  },
  {
    "id": "409", "girl": "kasumi", "name": "恋色いろは(かすみ)", "zhs_name": "恋色伊吕波(霞)", "zht_name": "戀色伊呂波(霞)", "en_name": "Maple Romance (Kasumi)", "kr_name": "사랑빛 이로하(카스미)", "type": "tec", "pow": "3544", "tec": "5042", "stm": "4156", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "灼熱のダンスB", "skill3": "閃きのテクニック4", "sell": "2020/10/29", "resell": "2021/11/2 2022/9/29", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现落叶，喷水会使叶子颜色变化"
  },
  {
    "id": "410", "girl": "ayane", "name": "恋色いろは(あやね)", "zhs_name": "恋色伊吕波(绫音)", "zht_name": "戀色伊呂波(綾音)", "en_name": "Maple Romance (Ayane)", "kr_name": "사랑빛 이로하(아야네)", "type": "tec", "pow": "3544", "tec": "5042", "stm": "4156", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "灼熱のダンスB", "skill3": "閃きのテクニック4", "sell": "2020/10/29", "resell": "2021/11/2 2022/9/29", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现落叶，喷水会使叶子颜色变化"
  },
  {
    "id": "411", "girl": "monica", "name": "恋色いろは(モニカ)", "zhs_name": "恋色伊吕波(莫妮卡)", "zht_name": "戀色伊呂波(莫妮卡)", "en_name": "Maple Romance (Monica)", "kr_name": "사랑빛 이로하(모니카)", "type": "tec", "pow": "3544", "tec": "5042", "stm": "4156", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "灼熱のダンスB", "skill3": "閃きのテクニック4", "sell": "2020/10/29", "resell": "2021/11/2 2022/9/29", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现落叶，喷水会使叶子颜色变化"
  },
  {
    "id": "412", "girl": "marie", "name": "おつまみピンチョス(マリー)", "zhs_name": "拽拽Pinchos(玛莉)", "zht_name": "拽拽Pinchos(瑪莉)", "en_name": "Appetizer Pinchos (Marie)", "kr_name": "애피타이저 핀초(마리)", "type": "stm", "pow": "3386", "tec": "4424", "stm": "5232", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "内から湧き上がるスタミナ5", "skill3": "可憐なフェイント", "sell": "2020/11/5", "resell": "2021/10/14", "break": "1", "special_fun": "允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "413", "girl": "kokoro", "name": "おつまみピンチョス(こころ)", "zhs_name": "拽拽Pinchos(心)", "zht_name": "拽拽Pinchos(心)", "en_name": "Appetizer Pinchos (Kokoro)", "kr_name": "애피타이저 핀초(코코로)", "type": "stm", "pow": "3386", "tec": "4424", "stm": "5232", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "内から湧き上がるスタミナ5", "skill3": "可憐なフェイント", "sell": "2020/11/5", "resell": "2021/10/14", "break": "1", "special_fun": "允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "414", "girl": "helena", "name": "おつまみピンチョス(エレナ)", "zhs_name": "拽拽Pinchos(海莲娜)", "zht_name": "拽拽Pinchos(海蓮娜)", "en_name": "Appetizer Pinchos (Helena)", "kr_name": "애피타이저 핀초(엘레나)", "type": "stm", "pow": "3386", "tec": "4424", "stm": "5232", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "内から湧き上がるスタミナ5", "skill3": "可憐なフェイント", "sell": "2020/11/5", "resell": "2021/10/14", "break": "1", "special_fun": "允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "c2", "girl": "all", "name": "第2回水着コンテスト「キュート」", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "none", "pow": "0", "tec": "0", "stm": "0", "apl": "0", "skill1": "", "skill2": "", "skill3": "", "sell": "2020/11/17", "resell": "N/A", "break": "1", "special_fun": "第二次服装设计比赛 得奖作品。作为礼包3000付费钻 两件打包销售 仅外形无属性。Design by しんじこ"
  },
  {
    "id": "c3", "girl": "all", "name": "第2回水着コンテスト「セクシー」", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "none", "pow": "0", "tec": "0", "stm": "0", "apl": "0", "skill1": "", "skill2": "", "skill3": "", "sell": "2020/11/17", "resell": "N/A", "break": "1", "special_fun": "第二次服装设计比赛 得奖作品。作为礼包3000付费钻 两件打包销售 仅外形无属性。Design by しこるん"
  },
  {
    "id": "415_1", "girl": "kasumi", "name": "エトワールブリエ(かすみ)", "zhs_name": "星光闪耀(霞)", "zht_name": "群星閃耀(霞)", "en_name": "Étoile Briller (Kasumi)", "kr_name": "에투알 브리에(카스미)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_2", "girl": "honoka", "name": "エトワールブリエ(ほのか)", "zhs_name": "星光闪耀(穗香)", "zht_name": "群星閃耀(穗香)", "en_name": "Étoile Briller (Honoka)", "kr_name": "에투알 브리에(호노카)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_3", "girl": "marie", "name": "エトワールブリエ(マリー)", "zhs_name": "星光闪耀(玛莉)", "zht_name": "群星閃耀(瑪莉)", "en_name": "Étoile Briller (Marie)", "kr_name": "에투알 브리에(마리)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_4", "girl": "ayane", "name": "エトワールブリエ(あやね)", "zhs_name": "星光闪耀(绫音)", "zht_name": "群星閃耀(綾音)", "en_name": "Étoile Briller (Ayane)", "kr_name": "에투알 브리에(아야네)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_5", "girl": "nyotengu", "name": "エトワールブリエ(女天狗)", "zhs_name": "星光闪耀(女天狗)", "zht_name": "群星閃耀(女天狗)", "en_name": "Étoile Briller (Nyotengu)", "kr_name": "에투알 브리에(뇨텐구)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_6", "girl": "kokoro", "name": "エトワールブリエ(こころ)", "zhs_name": "星光闪耀(心)", "zht_name": "群星閃耀(心)", "en_name": "Étoile Briller (Kokoro)", "kr_name": "에투알 브리에(코코로)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_7", "girl": "hitomi", "name": "エトワールブリエ(ヒトミ)", "zhs_name": "星光闪耀(瞳)", "zht_name": "群星閃耀(瞳)", "en_name": "Étoile Briller (Hitomi)", "kr_name": "에투알 브리에(히토미)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_8", "girl": "momiji", "name": "エトワールブリエ(紅葉)", "zhs_name": "星光闪耀(红叶)", "zht_name": "群星閃耀(紅葉)", "en_name": "Étoile Briller (Momiji)", "kr_name": "에투알 브리에(모미지)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_9", "girl": "helena", "name": "エトワールブリエ(エレナ)", "zhs_name": "星光闪耀(海莲娜)", "zht_name": "群星閃耀(海蓮娜)", "en_name": "Étoile Briller (Helena)", "kr_name": "에투알 브리에(엘레나)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_10", "girl": "misaki", "name": "エトワールブリエ(みさき)", "zhs_name": "星光闪耀(海咲)", "zht_name": "群星閃耀(海咲)", "en_name": "Étoile Briller (Misaki)", "kr_name": "에투알 브리에(미사키)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_11", "girl": "luna", "name": "エトワールブリエ(ルナ)", "zhs_name": "星光闪耀(露娜)", "zht_name": "群星閃耀(露娜)", "en_name": "Étoile Briller (Luna)", "kr_name": "에투알 브리에(루나)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_12", "girl": "tamaki", "name": "エトワールブリエ(たまき)", "zhs_name": "星光闪耀(环)", "zht_name": "群星閃耀(環)", "en_name": "Étoile Briller (Tamaki)", "kr_name": "에투알 브리에(타마키)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_13", "girl": "leifang", "name": "エトワールブリエ(レイファン)", "zhs_name": "星光闪耀(丽凤)", "zht_name": "群星閃耀(麗鳳)", "en_name": "Étoile Briller (Leifang)", "kr_name": "에투알 브리에(레이팡)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_14", "girl": "fiona", "name": "エトワールブリエ(フィオナ)", "zhs_name": "星光闪耀(菲欧娜)", "zht_name": "群星閃耀(菲歐娜)", "en_name": "Étoile Briller (Fiona)", "kr_name": "에투알 브리에(피오나)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_15", "girl": "nagisa", "name": "エトワールブリエ(なぎさ)", "zhs_name": "星光闪耀(凪咲)", "zht_name": "群星閃耀(凪咲)", "en_name": "Étoile Briller (Nagisa)", "kr_name": "에투알 브리에(나기사)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_16", "girl": "kanna", "name": "エトワールブリエ(カンナ)", "zhs_name": "星光闪耀(神无)", "zht_name": "群星閃耀(神無)", "en_name": "Étoile Briller (Kanna)", "kr_name": "에투알 브리에(칸나)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_17", "girl": "monica", "name": "エトワールブリエ(モニカ)", "zhs_name": "星光闪耀(莫妮卡)", "zht_name": "群星閃耀(莫妮卡)", "en_name": "Étoile Briller (Monica)", "kr_name": "에투알 브리에(모니카)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_18", "girl": "sayuri", "name": "エトワールブリエ(さゆり)", "zhs_name": "星光闪耀(小百合)", "zht_name": "群星閃耀(小百合)", "en_name": "Étoile Briller (Sayuri)", "kr_name": "에투알 브리에(사유리)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_19", "girl": "patty", "name": "エトワールブリエ(パティ)", "zhs_name": "星光闪耀(派蒂)", "zht_name": "群星閃耀(派蒂)", "en_name": "Étoile Briller (Patty)", "kr_name": "에투알 브리에(패티)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2020/11/17", "resell": "2022/6/1", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "416", "girl": "nyotengu", "name": "ブーケ・カメリア(女天狗)", "zhs_name": "花束・山茶(女天狗)", "zht_name": "花束・山茶(女天狗)", "en_name": "Bouquet Camellia (Nyotengu)", "kr_name": "부케 커멜리어(뇨텐구)", "type": "pow", "pow": "5622", "tec": "3984", "stm": "4094", "apl": "200", "skill1": "強烈スパイクG", "skill2": "白椿のパワー", "skill3": "豪快なスパイク", "sell": "2020/11/19", "resell": "2021/10/22 2021/11/19 2022/11/19", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。属性突破5322上限来到5622。14PP。升级版天使杀球+战术卡。狠狠背刺了第二套宝石生日的属性。KT学了intel的牙膏大法。第1年高主属性 砍技能，第2年加强技能 砍主属性，第3年双提高。"
  },
  {
    "id": "105_9", "girl": "sayuri", "name": "プレミア・ナイト(さゆり)", "zhs_name": "典藏之夜(小百合)", "zht_name": "典藏之夜(小百合)", "en_name": "Premier Night (Sayuri)", "kr_name": "프리미어 나이트(사유리)", "type": "pow", "pow": "4852", "tec": "3676", "stm": "4114", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2020/11/24", "resell": "", "break": "1", "special_fun": "[3周年庆复刻池新增] 游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "105_10", "girl": "patty", "name": "プレミア・ナイト(パティ)", "zhs_name": "典藏之夜(派蒂)", "zht_name": "典藏之夜(派蒂)", "en_name": "Premier Night (Patty)", "kr_name": "프리미어 나이트(패티)", "type": "pow", "pow": "4852", "tec": "3676", "stm": "4114", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2020/11/24", "resell": "", "break": "1", "special_fun": "[3周年庆复刻池新增] 游戏一周年庆服装 满觉醒为变色"
  },
  {
    "id": "417", "girl": "kasumi", "name": "空色のスリットワンピ(かすみ)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "418", "girl": "ayane", "name": "空色のスリットワンピ(あやね)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "419", "girl": "momiji", "name": "空色のスリットワンピ(紅葉)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "420", "girl": "luna", "name": "空色のスリットワンピ(ルナ)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "421", "girl": "fiona", "name": "空色のスリットワンピ(フィオナ)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "422", "girl": "sayuri", "name": "空色のスリットワンピ(さゆり)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "423", "girl": "honoka", "name": "星砂のスリットワンピ(ほのか)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "424", "girl": "kokoro", "name": "星砂のスリットワンピ(こころ)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "425", "girl": "hitomi", "name": "星砂のスリットワンピ(ヒトミ)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "426", "girl": "misaki", "name": "星砂のスリットワンピ(みさき)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "427", "girl": "kanna", "name": "星砂のスリットワンピ(カンナ)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "428", "girl": "nyotengu", "name": "深紅のスリットワンピ(女天狗)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "429", "girl": "helena", "name": "深紅のスリットワンピ(エレナ)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "430", "girl": "leifang", "name": "深紅のスリットワンピ(レイファン)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "431", "girl": "monica", "name": "深紅のスリットワンピ(モニカ)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "432", "girl": "tamaki", "name": "深紅のスリットワンピ(たまき)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "433", "girl": "nagisa", "name": "純白のスリットワンピ(なぎさ)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2020/11/24", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "434", "girl": "nyotengu", "name": "旗袍・玄武(女天狗)", "zhs_name": "旗袍・玄武(女天狗)", "zht_name": "旗袍・玄武(女天狗)", "en_name": "Black Tortoise Cheongsam (Nyotengu)", "kr_name": "치파오(현무)(뇨텐구)", "type": "pow", "pow": "5102", "tec": "3376", "stm": "4164", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2020/11/30", "resell": "2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "435", "girl": "momiji", "name": "旗袍・白虎(紅葉)", "zhs_name": "旗袍・白虎(红叶)", "zht_name": "旗袍・白虎(紅葉)", "en_name": "White Tiger Cheongsam (Momiji)", "kr_name": "치파오(백호)(모미지)", "type": "pow", "pow": "5102", "tec": "3376", "stm": "4164", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2020/11/30", "resell": "2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "436", "girl": "tamaki", "name": "旗袍・青龍(たまき)", "zhs_name": "旗袍・青龙(环)", "zht_name": "旗袍・青龍(環)", "en_name": "Blue Dragon Cheongsam (Tamaki)", "kr_name": "치파오(청룡)(타마키)", "type": "pow", "pow": "5102", "tec": "3376", "stm": "4164", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2020/11/30", "resell": "2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "437", "girl": "marie", "name": "ワイルドウインド(マリー)", "zhs_name": "狂风(玛莉)", "zht_name": "狂風(瑪莉)", "en_name": "Wild Wind (Marie)", "kr_name": "와일드 윈드(마리)", "type": "tec", "pow": "3476", "tec": "5062", "stm": "4104", "apl": "200", "skill1": "高度な心理戦B", "skill2": "閃きのテクニック6", "skill3": "可憐なフェイント", "sell": "2020/11/30", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "438", "girl": "kanna", "name": "ワイルドウインド(カンナ)", "zhs_name": "狂风(神无)", "zht_name": "狂風(神無)", "en_name": "Wild Wind (Kanna)", "kr_name": "와일드 윈드(칸나)", "type": "tec", "pow": "3476", "tec": "5062", "stm": "4104", "apl": "200", "skill1": "高度な心理戦B", "skill2": "閃きのテクニック6", "skill3": "可憐なフェイント", "sell": "2020/11/30", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "439", "girl": "patty", "name": "ワイルドウインド(パティ)", "zhs_name": "狂风(派蒂)", "zht_name": "狂風(派蒂)", "en_name": "Wild Wind (Patty)", "kr_name": "와일드 윈드(패티)", "type": "tec", "pow": "3476", "tec": "5062", "stm": "4104", "apl": "200", "skill1": "高度な心理戦B", "skill2": "閃きのテクニック6", "skill3": "可憐なフェイント", "sell": "2020/11/30", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "440", "girl": "ayane", "name": "ゆるふわパーカー(あやね)", "zhs_name": "轻柔连帽衫(绫音)", "zht_name": "輕柔連帽衫(綾音)", "en_name": "Soft 'n Fluffy Parka (Ayane)", "kr_name": "부드러운 파카(아야네)", "type": "stm", "pow": "4304", "tec": "3546", "stm": "5192", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2020/11/30", "resell": "2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "441", "girl": "fiona", "name": "ゆるふわパーカー(フィオナ)", "zhs_name": "轻柔连帽衫(菲欧娜)", "zht_name": "輕柔連帽衫(菲歐娜)", "en_name": "Soft 'n Fluffy Parka (Fiona)", "kr_name": "부드러운 파카(피오나)", "type": "stm", "pow": "4304", "tec": "3546", "stm": "5192", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2020/11/30", "resell": "2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "442", "girl": "sayuri", "name": "ゆるふわパーカー(さゆり)", "zhs_name": "轻柔连帽衫(小百合)", "zht_name": "輕柔連帽衫(小百合)", "en_name": "Soft 'n Fluffy Parka (Sayuri)", "kr_name": "부드러운 파카(사유리)", "type": "stm", "pow": "4304", "tec": "3546", "stm": "5192", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2020/11/30", "resell": "2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "443", "girl": "luna", "name": "シークレットハート(ルナ)", "zhs_name": "秘密之心(露娜)", "zht_name": "祕密的心(露娜)", "en_name": "Secret Heart (Luna)", "kr_name": "시크릿 하트(루나)", "type": "tec", "pow": "3426", "tec": "5162", "stm": "4054", "apl": "200", "skill1": "鉄壁のレシーブD", "skill2": "閃きのテクニック3", "skill3": "熱烈なエール", "sell": "2020/11/30", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "444", "girl": "kokoro", "name": "ブーケ・カトレア(こころ)", "zhs_name": "花束・卡特兰(心)", "zht_name": "花束・卡特蘭(心)", "en_name": "Bouquet Cattleya (Kokoro)", "kr_name": "부케 카틀레야(코코로)", "type": "pow", "pow": "5622", "tec": "3934", "stm": "4144", "apl": "200", "skill1": "強烈スパイクG", "skill2": "カトレアのパワー", "skill3": "豪快なスパイク", "sell": "2020/12/1", "resell": "2021/10/22 2021/12/1 2022/12/1", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。心若在，梦就在，人世间还有真爱~看强度，策划脑癌，只不过今年治愈出来。"
  },
  {
    "id": "445", "girl": "helena", "name": "クリムゾン・フェザー(エレナ)", "zhs_name": "深红羽翼(海莲娜)", "zht_name": "深紅羽翼(海蓮娜)", "en_name": "Crimson Feather (Helena)", "kr_name": "크림슨 페더(엘레나)", "type": "pow", "pow": "5042", "tec": "3506", "stm": "4094", "apl": "200", "skill1": "圧倒的な気迫A", "skill2": "秘められたパワー6", "skill3": "豪快なスパイク", "sell": "2020/12/3", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "446", "girl": "kokoro", "name": "ブロッサム・フェザー(こころ)", "zhs_name": "花簇羽翼(心)", "zht_name": "花簇羽翼(心)", "en_name": "Blossom Feather (Kokoro)", "kr_name": "블로섬 페더(코코로)", "type": "pow", "pow": "5042", "tec": "3506", "stm": "4094", "apl": "200", "skill1": "圧倒的な気迫A", "skill2": "秘められたパワー6", "skill3": "豪快なスパイク", "sell": "2020/12/3", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "447", "girl": "misaki", "name": "ブロッサム・フェザー(みさき)", "zhs_name": "花簇羽翼(海咲)", "zht_name": "花簇羽翼(海咲)", "en_name": "Blossom Feather (Misaki)", "kr_name": "블로섬 페더(미사키)", "type": "pow", "pow": "5042", "tec": "3506", "stm": "4094", "apl": "200", "skill1": "圧倒的な気迫A", "skill2": "秘められたパワー6", "skill3": "豪快なスパイク", "sell": "2020/12/3", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "448", "girl": "honoka", "name": "しらゆきのあさり(ほのか)", "zhs_name": "白雪之贝(穗香)", "zht_name": "白雪之貝(穗香)", "en_name": "Snow White Set (Honoka)", "kr_name": "백설 조개잡이(호노카)", "type": "stm", "pow": "4184", "tec": "3646", "stm": "5212", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2020/12/3", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "449", "girl": "leifang", "name": "ゆうづきのあさり(レイファン)", "zhs_name": "夕月之贝(丽凤)", "zht_name": "夕月之貝(麗鳳)", "en_name": "Evening Moon Set (Leifang)", "kr_name": "저녁달 조개잡이(레이팡)", "type": "stm", "pow": "4184", "tec": "3646", "stm": "5212", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2020/12/3", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "450", "girl": "nagisa", "name": "まよなかのあさり(なぎさ)", "zhs_name": "深宵之贝(凪咲)", "zht_name": "深宵之貝(凪咲)", "en_name": "Dusk Set (Nagisa)", "kr_name": "자정 조개잡이(나기사)", "type": "stm", "pow": "4184", "tec": "3646", "stm": "5212", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2020/12/3", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "451", "girl": "kasumi", "name": "春彩のスクールウェア(かすみ)", "zhs_name": "春色校服(霞)", "zht_name": "春色校服(霞)", "en_name": "Springtime Schoolwear (Kasumi)", "kr_name": "화사한 봄철 학생복(카스미)", "type": "tec", "pow": "3566", "tec": "4952", "stm": "4124", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2020/12/3", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "452", "girl": "hitomi", "name": "春彩のスクールウェア(ヒトミ)", "zhs_name": "春色校服(瞳)", "zht_name": "春色校服(瞳)", "en_name": "Springtime Schoolwear (Hitomi)", "kr_name": "화사한 봄철 학생복(히토미)", "type": "tec", "pow": "3566", "tec": "4952", "stm": "4124", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2020/12/3", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "453", "girl": "monica", "name": "春彩のスクールウェア(モニカ)", "zhs_name": "春色校服(莫妮卡)", "zht_name": "春色校服(莫妮卡)", "en_name": "Springtime Schoolwear (Monica)", "kr_name": "화사한 봄철 학생복(모니카)", "type": "tec", "pow": "3566", "tec": "4952", "stm": "4124", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2020/12/3", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "454_1", "girl": "luna", "name": "三國志14・貂蝉(ルナ)", "zhs_name": "三国志14・貂蝉(露娜)", "zht_name": "三國志14・貂蟬(露娜)", "en_name": "RTK 14: Diao Chan (Luna)", "kr_name": "삼국지 14・초선(루나)", "type": "stm", "pow": "3594", "tec": "4376", "stm": "5272", "apl": "200", "skill1": "高度な心理戦F", "skill2": "貂蝉(三國志14)のスタミナ", "skill3": "可憐なフェイント", "sell": "2020/12/9", "resell": "2021/5/20", "break": "1", "special_fun": "三国志14联动服装。附带回想。KT你是真的懒，自家联动居然只做了巨乳身型的模型。卡片池垃圾，奖励垃圾。三国志制作团队在你们内部的待遇地位是有多差？10号我不玩2077 玩你个冷饭三国志14？P技能说明貂蝉的体力是真的棒！"
  },
  {
    "id": "454_2", "girl": "sayuri", "name": "三國志14・貂蝉(さゆり)", "zhs_name": "三国志14・貂蝉(小百合)", "zht_name": "三國志14・貂蟬(小百合)", "en_name": "RTK 14: Diao Chan (Sayuri)", "kr_name": "삼국지 14・초선(사유리)", "type": "stm", "pow": "3594", "tec": "4376", "stm": "5272", "apl": "200", "skill1": "高度な心理戦F", "skill2": "貂蝉(三國志14)のスタミナ", "skill3": "可憐なフェイント", "sell": "2020/12/9", "resell": "2021/5/20", "break": "1", "special_fun": "三国志14联动服装。附带回想。KT你是真的懒，自家联动居然只做了巨乳身型的模型。卡片池垃圾，奖励垃圾。三国志制作团队在你们内部的待遇地位是有多差？10号我不玩2077 玩你个冷饭三国志14？P技能说明貂蝉的体力是真的棒！"
  },
  {
    "id": "454_3", "girl": "honoka", "name": "三國志14・貂蝉(ほのか)", "zhs_name": "三国志14・貂蝉(穗香)", "zht_name": "三國志14・貂蟬(穗香)", "en_name": "RTK 14: Diao Chan (Honoka)", "kr_name": "삼국지 14・초선(호노카)", "type": "stm", "pow": "3594", "tec": "4376", "stm": "5272", "apl": "200", "skill1": "高度な心理戦F", "skill2": "貂蝉(三國志14)のスタミナ", "skill3": "可憐なフェイント", "sell": "2020/12/9", "resell": "2021/5/20", "break": "1", "special_fun": "三国志14联动服装。附带回想。KT你是真的懒，自家联动居然只做了巨乳身型的模型。卡片池垃圾，奖励垃圾。三国志制作团队在你们内部的待遇地位是有多差？10号我不玩2077 玩你个冷饭三国志14？P技能说明貂蝉的体力是真的棒！"
  },
  {
    "id": "455_1", "girl": "kasumi", "name": "ノエル・シャルマン(かすみ)", "zhs_name": "圣诞・魅惑(霞)", "zht_name": "聖誕・魅惑(霞)", "en_name": "Noel Charmant (Kasumi)", "kr_name": "노엘 샤르망(카스미)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_2", "girl": "honoka", "name": "ノエル・シャルマン(ほのか)", "zhs_name": "圣诞・魅惑(穗香)", "zht_name": "聖誕・魅惑(穗香)", "en_name": "Noel Charmant (Honoka)", "kr_name": "노엘 샤르망(호노카)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_3", "girl": "marie", "name": "ノエル・シャルマン(マリー)", "zhs_name": "圣诞・魅惑(玛莉)", "zht_name": "聖誕・魅惑(瑪莉)", "en_name": "Noel Charmant (Marie)", "kr_name": "노엘 샤르망(마리)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_4", "girl": "ayane", "name": "ノエル・シャルマン(あやね)", "zhs_name": "圣诞・魅惑(绫音)", "zht_name": "聖誕・魅惑(綾音)", "en_name": "Noel Charmant (Ayane)", "kr_name": "노엘 샤르망(아야네)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_5", "girl": "nyotengu", "name": "ノエル・シャルマン(女天狗)", "zhs_name": "圣诞・魅惑(女天狗)", "zht_name": "聖誕・魅惑(女天狗)", "en_name": "Noel Charmant (Nyotengu)", "kr_name": "노엘 샤르망(뇨텐구)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_6", "girl": "kokoro", "name": "ノエル・シャルマン(こころ)", "zhs_name": "圣诞・魅惑(心)", "zht_name": "聖誕・魅惑(心)", "en_name": "Noel Charmant (Kokoro)", "kr_name": "노엘 샤르망(코코로)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_7", "girl": "hitomi", "name": "ノエル・シャルマン(ヒトミ)", "zhs_name": "圣诞・魅惑(瞳)", "zht_name": "聖誕・魅惑(瞳)", "en_name": "Noel Charmant (Hitomi)", "kr_name": "노엘 샤르망(히토미)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_8", "girl": "momiji", "name": "ノエル・シャルマン(紅葉)", "zhs_name": "圣诞・魅惑(红叶)", "zht_name": "聖誕・魅惑(紅葉)", "en_name": "Noel Charmant (Momiji)", "kr_name": "노엘 샤르망(모미지)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_9", "girl": "helena", "name": "ノエル・シャルマン(エレナ)", "zhs_name": "圣诞・魅惑(海莲娜)", "zht_name": "聖誕・魅惑(海蓮娜)", "en_name": "Noel Charmant (Helena)", "kr_name": "노엘 샤르망(엘레나)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_10", "girl": "misaki", "name": "ノエル・シャルマン(みさき)", "zhs_name": "圣诞・魅惑(海咲)", "zht_name": "聖誕・魅惑(海咲)", "en_name": "Noel Charmant (Misaki)", "kr_name": "노엘 샤르망(미사키)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_11", "girl": "luna", "name": "ノエル・シャルマン(ルナ)", "zhs_name": "圣诞・魅惑(露娜)", "zht_name": "聖誕・魅惑(露娜)", "en_name": "Noel Charmant (Luna)", "kr_name": "노엘 샤르망(루나)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_12", "girl": "tamaki", "name": "ノエル・シャルマン(たまき)", "zhs_name": "圣诞・魅惑(环)", "zht_name": "聖誕・魅惑(環)", "en_name": "Noel Charmant (Tamaki)", "kr_name": "노엘 샤르망(타마키)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_13", "girl": "leifang", "name": "ノエル・シャルマン(レイファン)", "zhs_name": "圣诞・魅惑(丽凤)", "zht_name": "聖誕・魅惑(麗鳳)", "en_name": "Noel Charmant (Leifang)", "kr_name": "노엘 샤르망(레이팡)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_14", "girl": "fiona", "name": "ノエル・シャルマン(フィオナ)", "zhs_name": "圣诞・魅惑(菲欧娜)", "zht_name": "聖誕・魅惑(菲歐娜)", "en_name": "Noel Charmant (Fiona)", "kr_name": "노엘 샤르망(피오나)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_15", "girl": "nagisa", "name": "ノエル・シャルマン(なぎさ)", "zhs_name": "圣诞・魅惑(凪咲)", "zht_name": "聖誕・魅惑(凪咲)", "en_name": "Noel Charmant (Nagisa)", "kr_name": "노엘 샤르망(나기사)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_16", "girl": "kanna", "name": "ノエル・シャルマン(カンナ)", "zhs_name": "圣诞・魅惑(神无)", "zht_name": "聖誕・魅惑(神無)", "en_name": "Noel Charmant (Kanna)", "kr_name": "노엘 샤르망(칸나)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_17", "girl": "monica", "name": "ノエル・シャルマン(モニカ)", "zhs_name": "圣诞・魅惑(莫妮卡)", "zht_name": "聖誕・魅惑(莫妮卡)", "en_name": "Noel Charmant (Monica)", "kr_name": "노엘 샤르망(모니카)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_18", "girl": "sayuri", "name": "ノエル・シャルマン(さゆり)", "zhs_name": "圣诞・魅惑(小百合)", "zht_name": "聖誕・魅惑(小百合)", "en_name": "Noel Charmant (Sayuri)", "kr_name": "노엘 샤르망(사유리)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_19", "girl": "patty", "name": "ノエル・シャルマン(パティ)", "zhs_name": "圣诞・魅惑(派蒂)", "zht_name": "聖誕・魅惑(派蒂)", "en_name": "Noel Charmant (Patty)", "kr_name": "노엘 샤르망(패티)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2020/12/16", "resell": "2021/12/23 2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_18", "girl": "sayuri", "name": "フレーズノエル(さゆり)", "zhs_name": "草莓圣诞(小百合)", "zht_name": "草莓聖誕(小百合)", "en_name": "Noël aux Fraises (Sayuri)", "kr_name": "프레이즈 노엘(사유리)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2020/12/23", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "111_19", "girl": "patty", "name": "フレーズノエル(パティ)", "zhs_name": "草莓圣诞(派蒂)", "zht_name": "草莓聖誕(派蒂)", "en_name": "Noël aux Fraises (Patty)", "kr_name": "프레이즈 노엘(패티)", "type": "stm", "pow": "4264", "tec": "3646", "stm": "4732", "apl": "200", "skill1": "強烈なプレッシャーF", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2020/12/23", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "456", "girl": "lobelia", "name": "フィエルテ・ミディ(ロベリア)", "zhs_name": "自信·迷笛(萝贝莉娅)", "zht_name": "自信・迷笛(蘿貝莉婭)", "en_name": "Fierte Midi (Lobelia)", "kr_name": "피에르테 미디(로벨리아)", "type": "stm", "pow": "3696", "tec": "4384", "stm": "5062", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "高度な心理戦D", "skill3": "内から湧き上がるスタミナ4", "sell": "2020/12/25", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "457", "girl": "momiji", "name": "振袖・綾錦(紅葉)", "zhs_name": "振袖・绫锦(红叶)", "zht_name": "振袖・綾錦(紅葉)", "en_name": "Ayanishiki Kimono (Momiji)", "kr_name": "후리소데(능라)(모미지)", "type": "stm", "pow": "3566", "tec": "4374", "stm": "5102", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "内から湧き上がるスタミナ6", "skill3": "可憐なフェイント", "sell": "2020/12/28", "resell": "2022/1/1 2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "458", "girl": "fiona", "name": "振袖・姫紫苑(フィオナ)", "zhs_name": "振袖・姬紫苑(菲欧娜)", "zht_name": "振袖・姬紫苑(菲歐娜)", "en_name": "Hime-Shion Kimono (Fiona)", "kr_name": "후리소데(옹굿나물)(피오나)", "type": "stm", "pow": "3896", "tec": "4354", "stm": "4892", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "高度な心理戦D", "skill3": "内から湧き上がるスタミナ3", "sell": "2020/12/28", "resell": "2022/1/1 2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "459", "girl": "nagisa", "name": "振袖・墨彩(なぎさ)", "zhs_name": "振袖·墨彩(凪咲)", "zht_name": "振袖・墨彩(凪咲)", "en_name": "Bokusai Kimono (Nagisa)", "kr_name": "후리소데(묵화)(나기사)", "type": "stm", "pow": "3836", "tec": "4344", "stm": "4962", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "灼熱のダンスB", "skill3": "内から湧き上がるスタミナ3", "sell": "2020/12/28", "resell": "2022/1/1 2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "460", "girl": "monica", "name": "ブーケ・シンビジウム(モニカ)", "zhs_name": "花束・大花蕙兰(莫妮卡)", "zht_name": "花束・大花蕙蘭(莫妮卡)", "en_name": "Bouquet Cymbidium (Monica)", "kr_name": "부케 심비디엄(모니카)", "type": "tec", "pow": "4172", "tec": "5364", "stm": "4164", "apl": "200", "skill1": "裏の裏を突くフェイントG", "skill2": "シンビジウムのテクニック", "skill3": "可憐なフェイント", "sell": "2021/1/1", "resell": "2021/10/22 2023/1/1", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。别问为什么技巧不是5622，问就是量子纠缠导致削弱。"
  },
  {
    "id": "461", "girl": "hitomi", "name": "巫女舞(ヒトミ)", "zhs_name": "巫女舞(瞳)", "zht_name": "巫女舞(瞳)", "en_name": "Shrine Maiden's Dance (Hitomi)", "kr_name": "무녀의 춤(히토미)", "type": "tec", "pow": "3426", "tec": "5132", "stm": "4084", "apl": "200", "skill1": "天才的な先読みD", "skill2": "閃きのテクニック6", "skill3": "熱烈なエール", "sell": "2021/1/4", "resell": "2022/12/28", "break": "1", "special_fun": "就这老衣服换人炒冷饭？明年是不是另外一套千早巫女服换人再翻炒一次？"
  },
  {
    "id": "462", "girl": "misaki", "name": "巫女舞(みさき)", "zhs_name": "巫女舞(海咲)", "zht_name": "巫女舞(海咲)", "en_name": "Shrine Maiden's Dance (Misaki)", "kr_name": "무녀의 춤(미사키)", "type": "tec", "pow": "3616", "tec": "4952", "stm": "4174", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "驚異のスタミナE", "skill3": "閃きのテクニック5", "sell": "2021/1/4", "resell": "2022/12/28", "break": "1", "special_fun": "就这老衣服换人炒冷饭？嗯，还是挺香的。"
  },
  {
    "id": "463", "girl": "sayuri", "name": "巫女舞(さゆり)", "zhs_name": "巫女舞(小百合)", "zht_name": "巫女舞(小百合)", "en_name": "Shrine Maiden's Dance (Sayuri)", "kr_name": "무녀의 춤(사유리)", "type": "tec", "pow": "3616", "tec": "4952", "stm": "4174", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "驚異のスタミナE", "skill3": "閃きのテクニック5", "sell": "2021/1/4", "resell": "2022/12/28", "break": "1", "special_fun": "就这老衣服换人炒冷饭？明年是不是另外一套千早巫女服换人再翻炒一次？"
  },
  {
    "id": "355_10", "girl": "tsukushi", "name": "レイズザセイル(つくし)", "zhs_name": "扬帆(筑紫)", "zht_name": "揚帆(筑紫)", "en_name": "Raise The Sail (Tsukushi)", "kr_name": "레이즈 더 세일(츠쿠시)", "type": "pow", "pow": "4962", "tec": "3586", "stm": "4194", "apl": "200", "skill1": "強烈スパイクB", "skill2": "驚異のスタミナB", "skill3": "順風満帆のパワー", "sell": "2021/1/12", "resell": "", "break": "1", "special_fun": "冷饭，本周连复刻池都懒得开了。"
  },
  {
    "id": "355_11", "girl": "honoka", "name": "レイズザセイル(ほのか)", "zhs_name": "扬帆(穗香)", "zht_name": "揚帆(穗香)", "en_name": "Raise The Sail (Honoka)", "kr_name": "레이즈 더 세일(호노카)", "type": "pow", "pow": "4962", "tec": "3586", "stm": "4194", "apl": "200", "skill1": "強烈スパイクB", "skill2": "驚異のスタミナB", "skill3": "順風満帆のパワー", "sell": "2021/1/12", "resell": "", "break": "1", "special_fun": "冷饭，本周连复刻池都懒得开了。"
  },
  {
    "id": "355_12", "girl": "leifang", "name": "レイズザセイル(レイファン)", "zhs_name": "扬帆(丽凤)", "zht_name": "揚帆(麗鳳)", "en_name": "Raise The Sail (Leifang)", "kr_name": "레이즈 더 세일(레이팡)", "type": "pow", "pow": "5102", "tec": "3426", "stm": "4114", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "順風満帆のパワー", "skill3": "豪快なスパイク", "sell": "2021/1/12", "resell": "", "break": "1", "special_fun": "冷饭，本周连复刻池都懒得开了。"
  },
  {
    "id": "300_8", "girl": "marie", "name": "ライザ・お気に入りの普段着(マリー)", "zhs_name": "莱莎・喜欢的日常装束", "zht_name": "", "en_name": "Ryza's Favorite Outfit", "kr_name": "라이자・좋아하는 평상복", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2021/1/19", "resell": "2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_9", "girl": "kasumi", "name": "ライザ・お気に入りの普段着(かすみ)", "zhs_name": "莱莎・喜欢的日常装束", "zht_name": "", "en_name": "Ryza's Favorite Outfit", "kr_name": "라이자・좋아하는 평상복", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2021/1/19", "resell": "2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_10", "girl": "nyotengu", "name": "ライザ・お気に入りの普段着(女天狗)", "zhs_name": "莱莎・喜欢的日常装束", "zht_name": "", "en_name": "Ryza's Favorite Outfit", "kr_name": "라이자・좋아하는 평상복", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2021/1/19", "resell": "2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_11", "girl": "hitomi", "name": "ライザ・お気に入りの普段着(ヒトミ)", "zhs_name": "莱莎・喜欢的日常装束", "zht_name": "", "en_name": "Ryza's Favorite Outfit", "kr_name": "라이자・좋아하는 평상복", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2021/1/19", "resell": "2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_12", "girl": "momiji", "name": "ライザ・お気に入りの普段着(紅葉)", "zhs_name": "莱莎・喜欢的日常装束", "zht_name": "", "en_name": "Ryza's Favorite Outfit", "kr_name": "라이자・좋아하는 평상복", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2021/1/19", "resell": "2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_13", "girl": "sayuri", "name": "ライザ・お気に入りの普段着(さゆり)", "zhs_name": "莱莎・喜欢的日常装束", "zht_name": "", "en_name": "Ryza's Favorite Outfit", "kr_name": "라이자・좋아하는 평상복", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2021/1/19", "resell": "2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_14", "girl": "patty", "name": "ライザ・お気に入りの普段着(パティ)", "zhs_name": "莱莎・喜欢的日常装束", "zht_name": "", "en_name": "Ryza's Favorite Outfit", "kr_name": "라이자・좋아하는 평상복", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2021/1/19", "resell": "2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_15", "girl": "tsukushi", "name": "ライザ・お気に入りの普段着(つくし)", "zhs_name": "莱莎・喜欢的日常装束", "zht_name": "", "en_name": "Ryza's Favorite Outfit", "kr_name": "라이자・좋아하는 평상복", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2021/1/19", "resell": "2022/2/24 2023/3/22", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "464", "girl": "fiona", "name": "はいからブルーマー(フィオナ)", "zhs_name": "时髦体操裤(菲欧娜)", "zht_name": "時髦體操褲(菲歐娜)", "en_name": "Stylish Bloomers (Fiona)", "kr_name": "하이 컬러 블루머(피오나)", "type": "tec", "pow": "3586", "tec": "4962", "stm": "4094", "apl": "200", "skill1": "天才的な先読みC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2021/1/28", "resell": "2021/9/16 2023/6/27", "break": "1", "special_fun": ""
  },
  {
    "id": "465", "girl": "momiji", "name": "はいからブルーマー(紅葉)", "zhs_name": "时髦体操裤(红叶)", "zht_name": "時髦體操褲(紅葉)", "en_name": "Stylish Bloomers (Momiji)", "kr_name": "하이 컬러 블루머(모미지)", "type": "tec", "pow": "3656", "tec": "4882", "stm": "4204", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "灼熱のダンスD", "skill3": "閃きのテクニック3", "sell": "2021/1/28", "resell": "2021/9/16 2023/6/27", "break": "1", "special_fun": ""
  },
  {
    "id": "466", "girl": "kanna", "name": "はいからブルーマー(カンナ)", "zhs_name": "时髦体操裤(神无)", "zht_name": "時髦體操褲(神無)", "en_name": "Stylish Bloomers (Kanna)", "kr_name": "하이 컬러 블루머(칸나)", "type": "tec", "pow": "3656", "tec": "4882", "stm": "4204", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "灼熱のダンスD", "skill3": "閃きのテクニック3", "sell": "2021/1/28", "resell": "2021/9/16 2023/6/27", "break": "1", "special_fun": ""
  },
  {
    "id": "467", "girl": "lobelia", "name": "ブルーエルフィン(ロベリア)", "zhs_name": "蓝色小精灵(萝贝莉娅)", "zht_name": "藍色妖精(蘿貝莉婭)", "en_name": "Blue Elfin (Lobelia)", "kr_name": "블루 엘핀(로벨리아)", "type": "tec", "pow": "3356", "tec": "4922", "stm": "4364", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック6", "skill3": "可憐なフェイント", "sell": "2021/1/28", "resell": "", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "468", "girl": "helena", "name": "ブーケ・シンビジウム(エレナ)", "zhs_name": "花束・大花蕙兰(海莲娜)", "zht_name": "花束・大花蕙蘭(海蓮娜)", "en_name": "Bouquet Cymbidium (Helena)", "kr_name": "부케 심비디엄(엘레나)", "type": "tec", "pow": "4122", "tec": "5364", "stm": "4214", "apl": "200", "skill1": "裏の裏を突くフェイントG", "skill2": "シンビジウムのテクニック", "skill3": "可憐なフェイント", "sell": "2021/1/30", "resell": "2021/10/22 2022/1/30 2023/1/30", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。别问为什么技巧不是5622，问就是量子纠缠导致削弱。"
  },
  {
    "id": "469", "girl": "ayane", "name": "くつろぎニット(あやね)", "zhs_name": "休闲针织衫(绫音)", "zht_name": "寬鬆毛衣(綾音)", "en_name": "Relaxing Knit (Ayane)", "kr_name": "느긋한 니트(아야네)", "type": "tec", "pow": "3596", "tec": "5002", "stm": "4044", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2021/2/4", "resell": "2021/9/24", "break": "1", "special_fun": ""
  },
  {
    "id": "470", "girl": "tamaki", "name": "くつろぎニット(たまき)", "zhs_name": "休闲针织衫(环)", "zht_name": "寬鬆毛衣(環)", "en_name": "Relaxing Knit (Tamaki)", "kr_name": "느긋한 니트(타마키)", "type": "tec", "pow": "3686", "tec": "4852", "stm": "4204", "apl": "200", "skill1": "完璧なレシーブB", "skill2": "高度な心理戦D", "skill3": "プラチナレシーバー", "sell": "2021/2/4", "resell": "2021/9/24", "break": "1", "special_fun": ""
  },
  {
    "id": "471_1", "girl": "kasumi", "name": "プルミエ・ランデブー(かすみ)", "zhs_name": "初次约会(霞)", "zht_name": "初次相約(霞)", "en_name": "Premier Rendezvous (Kasumi)", "kr_name": "프리미에르 랑데부(카스미)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_2", "girl": "honoka", "name": "プルミエ・ランデブー(ほのか)", "zhs_name": "初次约会(穗香)", "zht_name": "初次相約(穗香)", "en_name": "Premier Rendezvous (Honoka)", "kr_name": "프리미에르 랑데부(호노카)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_3", "girl": "marie", "name": "プルミエ・ランデブー(マリー)", "zhs_name": "初次约会(玛莉)", "zht_name": "初次相約(瑪莉)", "en_name": "Premier Rendezvous (Marie)", "kr_name": "프리미에르 랑데부(마리)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_4", "girl": "ayane", "name": "プルミエ・ランデブー(あやね)", "zhs_name": "初次约会(绫音)", "zht_name": "初次相約(綾音)", "en_name": "Premier Rendezvous (Ayane)", "kr_name": "프리미에르 랑데부(아야네)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_5", "girl": "nyotengu", "name": "プルミエ・ランデブー(女天狗)", "zhs_name": "初次约会(女天狗)", "zht_name": "初次相約(女天狗)", "en_name": "Premier Rendezvous (Nyotengu)", "kr_name": "프리미에르 랑데부(뇨텐구)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_6", "girl": "kokoro", "name": "プルミエ・ランデブー(こころ)", "zhs_name": "初次约会(心)", "zht_name": "初次相約(心)", "en_name": "Premier Rendezvous (Kokoro)", "kr_name": "프리미에르 랑데부(코코로)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_7", "girl": "hitomi", "name": "プルミエ・ランデブー(ヒトミ)", "zhs_name": "初次约会(瞳)", "zht_name": "初次相約(瞳)", "en_name": "Premier Rendezvous (Hitomi)", "kr_name": "프리미에르 랑데부(히토미)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_8", "girl": "momiji", "name": "プルミエ・ランデブー(紅葉)", "zhs_name": "初次约会(红叶)", "zht_name": "初次相約(紅葉)", "en_name": "Premier Rendezvous (Momiji)", "kr_name": "프리미에르 랑데부(모미지)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_9", "girl": "helena", "name": "プルミエ・ランデブー(エレナ)", "zhs_name": "初次约会(海莲娜)", "zht_name": "初次相約(海蓮娜)", "en_name": "Premier Rendezvous (Helena)", "kr_name": "프리미에르 랑데부(엘레나)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_10", "girl": "misaki", "name": "プルミエ・ランデブー(みさき)", "zhs_name": "初次约会(海咲)", "zht_name": "初次相約(海咲)", "en_name": "Premier Rendezvous (Misaki)", "kr_name": "프리미에르 랑데부(미사키)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_11", "girl": "luna", "name": "プルミエ・ランデブー(ルナ)", "zhs_name": "初次约会(露娜)", "zht_name": "初次相約(露娜)", "en_name": "Premier Rendezvous (Luna)", "kr_name": "프리미에르 랑데부(루나)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_12", "girl": "tamaki", "name": "プルミエ・ランデブー(たまき)", "zhs_name": "初次约会(环)", "zht_name": "初次相約(環)", "en_name": "Premier Rendezvous (Tamaki)", "kr_name": "프리미에르 랑데부(타마키)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_13", "girl": "leifang", "name": "プルミエ・ランデブー(レイファン)", "zhs_name": "初次约会(丽凤)", "zht_name": "初次相約(麗鳳)", "en_name": "Premier Rendezvous (Leifang)", "kr_name": "프리미에르 랑데부(레이팡)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_14", "girl": "fiona", "name": "プルミエ・ランデブー(フィオナ)", "zhs_name": "初次约会(菲欧娜)", "zht_name": "初次相約(菲歐娜)", "en_name": "Premier Rendezvous (Fiona)", "kr_name": "프리미에르 랑데부(피오나)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_15", "girl": "nagisa", "name": "プルミエ・ランデブー(なぎさ)", "zhs_name": "初次约会(凪咲)", "zht_name": "初次相約(凪咲)", "en_name": "Premier Rendezvous (Nagisa)", "kr_name": "프리미에르 랑데부(나기사)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_16", "girl": "kanna", "name": "プルミエ・ランデブー(カンナ)", "zhs_name": "初次约会(神无)", "zht_name": "初次相約(神無)", "en_name": "Premier Rendezvous (Kanna)", "kr_name": "프리미에르 랑데부(칸나)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_17", "girl": "monica", "name": "プルミエ・ランデブー(モニカ)", "zhs_name": "初次约会(莫妮卡)", "zht_name": "初次相約(莫妮卡)", "en_name": "Premier Rendezvous (Monica)", "kr_name": "프리미에르 랑데부(모니카)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_18", "girl": "sayuri", "name": "プルミエ・ランデブー(さゆり)", "zhs_name": "初次约会(小百合)", "zht_name": "初次相約(小百合)", "en_name": "Premier Rendezvous (Sayuri)", "kr_name": "프리미에르 랑데부(사유리)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_19", "girl": "patty", "name": "プルミエ・ランデブー(パティ)", "zhs_name": "初次约会(派蒂)", "zht_name": "初次相約(派蒂)", "en_name": "Premier Rendezvous (Patty)", "kr_name": "프리미에르 랑데부(패티)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_20", "girl": "tsukushi", "name": "プルミエ・ランデブー(つくし)", "zhs_name": "初次约会(筑紫)", "zht_name": "初次相約(筑紫)", "en_name": "Premier Rendezvous (Tsukushi)", "kr_name": "프리미에르 랑데부(츠쿠시)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2021/2/10", "resell": "2022/2/17 2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "472", "girl": "fiona", "name": "ブーケ・フリージア(フィオナ)", "zhs_name": "花束・小苍兰(菲欧娜)", "zht_name": "花束・小蒼蘭(菲歐娜)", "en_name": "Bouquet Freesia (Fiona)", "kr_name": "부케 프리지어(피오나)", "type": "tec", "pow": "4092", "tec": "5364", "stm": "4244", "apl": "200", "skill1": "裏の裏を突くフェイントG", "skill2": "フリージアのテクニック", "skill3": "可憐なフェイント", "sell": "2021/2/11", "resell": "2021/10/22 2022/2/11 2023/2/11", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。别问为什么技巧不是5622，问就是量子纠缠导致削弱。"
  },
  {
    "id": "473", "girl": "nagisa", "name": "シャノワール(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4284", "tec": "3626", "stm": "5132", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "プラチナアタッカー", "skill3": "豪快なスパイク", "sell": "2021/2/17", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "474", "girl": "marie", "name": "シャノワール(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4394", "tec": "3676", "stm": "5072", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "強烈スパイクD", "skill3": "内から湧き上がるスタミナ6", "sell": "2021/2/17", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "475", "girl": "kasumi", "name": "ブーケ・フリージア(かすみ)", "zhs_name": "花束・小苍兰(霞)", "zht_name": "花束・小蒼蘭(霞)", "en_name": "Bouquet Freesia (Kasumi)", "kr_name": "부케 프리지어(카스미)", "type": "tec", "pow": "4142", "tec": "5364", "stm": "4194", "apl": "200", "skill1": "裏の裏を突くフェイントG", "skill2": "フリージアのテクニック", "skill3": "可憐なフェイント", "sell": "2021/2/23", "resell": "2021/10/22 2022/2/23 2023/2/23", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。别问为什么技巧不是5622，问就是量子纠缠导致削弱。"
  },
  {
    "id": "476", "girl": "tsukushi", "name": "はじけるチャップス(つくし)", "zhs_name": "炸裂皮裤(筑紫)", "zht_name": "", "en_name": "Bursting Chaps (Tsukushi)", "kr_name": "팝핑 챕스(츠쿠시)", "type": "tec", "pow": "3516", "tec": "5012", "stm": "4114", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック5", "skill3": "可憐なフェイント", "sell": "2021/2/25", "resell": "2022/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "477", "girl": "honoka", "name": "はじけるチャップス(ほのか)", "zhs_name": "炸裂皮裤", "zht_name": "", "en_name": "Bursting Chaps", "kr_name": "팝핑 챕스", "type": "tec", "pow": "3536", "tec": "5242", "stm": "3964", "apl": "200", "skill1": "高度な心理戦C", "skill2": "驚異のスタミナD", "skill3": "閃きのテクニック6", "sell": "2021/2/25", "resell": "2022/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "478", "girl": "sayuri", "name": "はじけるチャップス(さゆり)", "zhs_name": "炸裂皮裤", "zht_name": "", "en_name": "Bursting Chaps", "kr_name": "팝핑 챕스", "type": "tec", "pow": "3536", "tec": "5242", "stm": "3964", "apl": "200", "skill1": "高度な心理戦C", "skill2": "驚異のスタミナD", "skill3": "閃きのテクニック6", "sell": "2021/2/25", "resell": "2022/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "479", "girl": "kokoro", "name": "コード・ルージュ(こころ)", "zhs_name": "代号‧嫣红(心)", "zht_name": "代號・嫣紅(心)", "en_name": "Code Rouge (Kokoro)", "kr_name": "코드 루즈(코코로)", "type": "pow", "pow": "5032", "tec": "3536", "stm": "4074", "apl": "200", "skill1": "強烈スパイクF", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2021/3/4", "resell": "2021/11/9 2023/5/11", "break": "1", "special_fun": ""
  },
  {
    "id": "480", "girl": "helena", "name": "コード・ルージュ(エレナ)", "zhs_name": "代号‧嫣红(海莲娜)", "zht_name": "代號・嫣紅(海蓮娜)", "en_name": "Code Rouge (Helena)", "kr_name": "코드 루즈(엘레나)", "type": "pow", "pow": "5202", "tec": "3576", "stm": "3964", "apl": "200", "skill1": "強烈スパイクD", "skill2": "強烈なプレッシャーF", "skill3": "秘められたパワー4", "sell": "2021/3/4 2023/5/11", "resell": "2021/11/9", "break": "1", "special_fun": ""
  },
  {
    "id": "481", "girl": "patty", "name": "コード・ルージュ(パティ)", "zhs_name": "代号‧嫣红(派蒂)", "zht_name": "代號・嫣紅(派蒂)", "en_name": "Code Rouge (Patty)", "kr_name": "코드 루즈(패티)", "type": "pow", "pow": "5202", "tec": "3576", "stm": "3964", "apl": "200", "skill1": "強烈スパイクD", "skill2": "強烈なプレッシャーF", "skill3": "秘められたパワー4", "sell": "2021/3/4 2023/5/11", "resell": "2021/11/9", "break": "1", "special_fun": ""
  },
  {
    "id": "482_1", "girl": "kasumi", "name": "ぬくもりマフラー(かすみ)", "zhs_name": "温暖围巾(霞)", "zht_name": "溫馨圍巾(霞)", "en_name": "Scarf of Warmth (Kasumi)", "kr_name": "따스한 머플러(카스미)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_2", "girl": "honoka", "name": "ぬくもりマフラー(ほのか)", "zhs_name": "温暖围巾(穗香)", "zht_name": "溫馨圍巾(穗香)", "en_name": "Scarf of Warmth (Honoka)", "kr_name": "따스한 머플러(호노카)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_3", "girl": "marie", "name": "ぬくもりマフラー(マリー)", "zhs_name": "温暖围巾(玛莉)", "zht_name": "溫馨圍巾(瑪莉)", "en_name": "Scarf of Warmth (Marie)", "kr_name": "따스한 머플러(마리)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_4", "girl": "ayane", "name": "ぬくもりマフラー(あやね)", "zhs_name": "温暖围巾(绫音)", "zht_name": "溫馨圍巾(綾音)", "en_name": "Scarf of Warmth (Ayane)", "kr_name": "따스한 머플러(아야네)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_5", "girl": "nyotengu", "name": "ぬくもりマフラー(女天狗)", "zhs_name": "温暖围巾(女天狗)", "zht_name": "溫馨圍巾(女天狗)", "en_name": "Scarf of Warmth (Nyotengu)", "kr_name": "따스한 머플러(뇨텐구)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_6", "girl": "kokoro", "name": "ぬくもりマフラー(こころ)", "zhs_name": "温暖围巾(心)", "zht_name": "溫馨圍巾(心)", "en_name": "Scarf of Warmth (Kokoro)", "kr_name": "따스한 머플러(코코로)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_7", "girl": "hitomi", "name": "ぬくもりマフラー(ヒトミ)", "zhs_name": "温暖围巾(瞳)", "zht_name": "溫馨圍巾(瞳)", "en_name": "Scarf of Warmth (Hitomi)", "kr_name": "따스한 머플러(히토미)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_8", "girl": "momiji", "name": "ぬくもりマフラー(紅葉)", "zhs_name": "温暖围巾(红叶)", "zht_name": "溫馨圍巾(紅葉)", "en_name": "Scarf of Warmth (Momiji)", "kr_name": "따스한 머플러(모미지)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_9", "girl": "helena", "name": "ぬくもりマフラー(エレナ)", "zhs_name": "温暖围巾(海莲娜)", "zht_name": "溫馨圍巾(海蓮娜)", "en_name": "Scarf of Warmth (Helena)", "kr_name": "따스한 머플러(엘레나)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_10", "girl": "misaki", "name": "ぬくもりマフラー(みさき)", "zhs_name": "温暖围巾(海咲)", "zht_name": "溫馨圍巾(海咲)", "en_name": "Scarf of Warmth (Misaki)", "kr_name": "따스한 머플러(미사키)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_11", "girl": "luna", "name": "ぬくもりマフラー(ルナ)", "zhs_name": "温暖围巾(露娜)", "zht_name": "溫馨圍巾(露娜)", "en_name": "Scarf of Warmth (Luna)", "kr_name": "따스한 머플러(루나)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_12", "girl": "tamaki", "name": "ぬくもりマフラー(たまき)", "zhs_name": "温暖围巾(环)", "zht_name": "溫馨圍巾(環)", "en_name": "Scarf of Warmth (Tamaki)", "kr_name": "따스한 머플러(타마키)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_13", "girl": "leifang", "name": "ぬくもりマフラー(レイファン)", "zhs_name": "温暖围巾(丽凤)", "zht_name": "溫馨圍巾(麗鳳)", "en_name": "Scarf of Warmth (Leifang)", "kr_name": "따스한 머플러(레이팡)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_14", "girl": "fiona", "name": "ぬくもりマフラー(フィオナ)", "zhs_name": "温暖围巾(菲欧娜)", "zht_name": "溫馨圍巾(菲歐娜)", "en_name": "Scarf of Warmth (Fiona)", "kr_name": "따스한 머플러(피오나)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_15", "girl": "nagisa", "name": "ぬくもりマフラー(なぎさ)", "zhs_name": "温暖围巾(凪咲)", "zht_name": "溫馨圍巾(凪咲)", "en_name": "Scarf of Warmth (Nagisa)", "kr_name": "따스한 머플러(나기사)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_16", "girl": "kanna", "name": "ぬくもりマフラー(カンナ)", "zhs_name": "温暖围巾(神无)", "zht_name": "溫馨圍巾(神無)", "en_name": "Scarf of Warmth (Kanna)", "kr_name": "따스한 머플러(칸나)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_17", "girl": "monica", "name": "ぬくもりマフラー(モニカ)", "zhs_name": "温暖围巾(莫妮卡)", "zht_name": "溫馨圍巾(莫妮卡)", "en_name": "Scarf of Warmth (Monica)", "kr_name": "따스한 머플러(모니카)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_18", "girl": "sayuri", "name": "ぬくもりマフラー(さゆり)", "zhs_name": "温暖围巾(小百合)", "zht_name": "溫馨圍巾(小百合)", "en_name": "Scarf of Warmth (Sayuri)", "kr_name": "따스한 머플러(사유리)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_19", "girl": "patty", "name": "ぬくもりマフラー(パティ)", "zhs_name": "温暖围巾(派蒂)", "zht_name": "溫馨圍巾(派蒂)", "en_name": "Scarf of Warmth (Patty)", "kr_name": "따스한 머플러(패티)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "482_20", "girl": "tsukushi", "name": "ぬくもりマフラー(つくし)", "zhs_name": "温暖围巾(筑紫)", "zht_name": "溫馨圍巾(筑紫)", "en_name": "Scarf of Warmth (Tsukushi)", "kr_name": "따스한 머플러(츠쿠시)", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/3/11", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "483", "girl": "luna", "name": "パステルスイート(ルナ)", "zhs_name": "甜美粉彩(露娜)", "zht_name": "粉彩甜點(露娜)", "en_name": "Pastel Sweet (Luna)", "kr_name": "파스텔 스위트(루나)", "type": "stm", "pow": "3526", "tec": "4344", "stm": "5172", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "内から湧き上がるスタミナ3", "skill3": "可憐なフェイント", "sell": "2021/3/18", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "484", "girl": "sayuri", "name": "パステルスイート(さゆり)", "zhs_name": "甜美粉彩(小百合)", "zht_name": "粉彩甜點(小百合)", "en_name": "Pastel Sweet (Sayuri)", "kr_name": "파스텔 스위트(사유리)", "type": "stm", "pow": "3716", "tec": "4374", "stm": "5052", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "裏の裏を突くフェイントF", "skill3": "内から湧き上がるスタミナ4", "sell": "2021/3/18", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "485", "girl": "tsukushi", "name": "パステルスイート(つくし)", "zhs_name": "甜美粉彩(筑紫)", "zht_name": "粉彩甜點(筑紫)", "en_name": "Pastel Sweet (Tsukushi)", "kr_name": "파스텔 스위트(츠쿠시)", "type": "stm", "pow": "3716", "tec": "4374", "stm": "5052", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "裏の裏を突くフェイントF", "skill3": "内から湧き上がるスタミナ4", "sell": "2021/3/18", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "486", "girl": "honoka", "name": "ブーケ・ラーレ(ほのか)", "zhs_name": "花束・郁金香(穗香)", "zht_name": "花束・鬱金香(穗香)", "en_name": "Bouquet Lale (Honoka)", "kr_name": "부케 라레(호노카)", "type": "stm", "pow": "4764", "tec": "3714", "stm": "5622", "apl": "200", "skill1": "強烈スパイクG", "skill2": "ラーレのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/3/24", "resell": "2021/10/22 2022/3/24 2023/3/24", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。懂了，强度看策划心情，平衡不存在的，安息吧明年再来。"
  },
  {
    "id": "487", "girl": "monica", "name": "ラビットジョーカー(モニカ)", "zhs_name": "兔子小丑(莫妮卡)", "zht_name": "兔女郎鬼牌(莫妮卡)", "en_name": "Rabbit Joker (Monica)", "kr_name": "래빗 조커(모니카)", "type": "stm", "pow": "3506", "tec": "4314", "stm": "5222", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "内から湧き上がるスタミナ6", "skill3": "可憐なフェイント", "sell": "2021/3/25", "resell": "2023/3/2", "break": "1", "special_fun": ""
  },
  {
    "id": "488", "girl": "kasumi", "name": "ラビットジョーカー(かすみ)", "zhs_name": "兔子小丑(霞)", "zht_name": "兔女郎鬼牌(霞)", "en_name": "Rabbit Joker (Kasumi)", "kr_name": "래빗 조커(카스미)", "type": "stm", "pow": "3636", "tec": "4394", "stm": "5112", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "高度な心理戦C", "skill3": "内から湧き上がるスタミナ4", "sell": "2021/3/25", "resell": "2023/3/2", "break": "1", "special_fun": ""
  },
  {
    "id": "489", "girl": "nyotengu", "name": "ラビットジョーカー(女天狗)", "zhs_name": "兔子小丑(女天狗)", "zht_name": "兔女郎鬼牌(女天狗)", "en_name": "Rabbit Joker (Nyotengu)", "kr_name": "래빗 조커(뇨텐구)", "type": "stm", "pow": "3636", "tec": "4394", "stm": "5112", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "高度な心理戦C", "skill3": "内から湧き上がるスタミナ4", "sell": "2021/3/25", "resell": "2023/3/2", "break": "1", "special_fun": ""
  },
  {
    "id": "490", "girl": "sayuri", "name": "ブーケ・ラーレ(さゆり)", "zhs_name": "花束・郁金香(小百合)", "zht_name": "花束・鬱金香(小百合)", "en_name": "Bouquet Lale (Sayuri)", "kr_name": "부케 라레(사유리)", "type": "stm", "pow": "3734", "tec": "4744", "stm": "5622", "apl": "200", "skill1": "裏の裏を突くフェイントG", "skill2": "ラーレのスタミナ", "skill3": "可憐なフェイント", "sell": "2021/3/31", "resell": "2021/10/22 2022/3/31 2023/3/31", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。懂了，强度看策划心情，平衡不存在的，安息吧明年再来。"
  },
  {
    "id": "491", "girl": "misaki", "name": "エンドルフィン・スカイ(みさき)", "zhs_name": "安多芬天体(海咲)", "zht_name": "安多芬天體(海咲)", "en_name": "Endorphin Sky (Misaki)", "kr_name": "엔돌핀 스카이(미사키)", "type": "pow", "pow": "4812", "tec": "3566", "stm": "4264", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "秘められたパワー6", "skill3": "豪快なスパイク", "sell": "2021/4/1", "resell": "2023/7/5", "break": "1", "special_fun": ""
  },
  {
    "id": "492", "girl": "patty", "name": "エンドルフィン・ハート(パティ)", "zhs_name": "安多芬之心(派蒂)", "zht_name": "安多芬之心(派蒂)", "en_name": "Endorphin Heart (Patty)", "kr_name": "엔돌핀 하트(패티)", "type": "pow", "pow": "4952", "tec": "3606", "stm": "4184", "apl": "200", "skill1": "強烈スパイクC", "skill2": "灼熱のダンスF", "skill3": "秘められたパワー5", "sell": "2021/4/1", "resell": "2023/7/5", "break": "1", "special_fun": ""
  },
  {
    "id": "493", "girl": "nanami", "name": "トワイライトタイム(ななみ)", "zhs_name": "暮光时刻(七海)", "zht_name": "暮光時刻(七海)", "en_name": "Twilight Time (Nanami)", "kr_name": "트와일라잇 타임(나나미)", "type": "stm", "pow": "4264", "tec": "3956", "stm": "4922", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "灼熱のダンスD", "skill3": "内から湧き上がるスタミナ6", "sell": "2021/4/1", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "494", "girl": "leifang", "name": "はいからブロッサム(レイファン)", "zhs_name": "洋式制服之花(丽凤)", "zht_name": "", "en_name": "Stylish Blossom (Leifang)", "kr_name": "하이 컬러 블로섬(레이팡)", "type": "stm", "pow": "4274", "tec": "3696", "stm": "5072", "apl": "200", "skill1": "灼熱のダンスD", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2021/4/8", "resell": "2021/9/3", "break": "1", "special_fun": ""
  },
  {
    "id": "495", "girl": "nagisa", "name": "はいからブロッサム(なぎさ)", "zhs_name": "洋式制服之花(凪咲)", "zht_name": "", "en_name": "Stylish Blossom (Nagisa)", "kr_name": "하이 컬러 블로섬(나기사)", "type": "stm", "pow": "4464", "tec": "3686", "stm": "4992", "apl": "200", "skill1": "灼熱のダンスB", "skill2": "圧倒的な気迫C", "skill3": "内から湧き上がるスタミナ4", "sell": "2021/4/8", "resell": "2021/9/3", "break": "1", "special_fun": ""
  },
  {
    "id": "496", "girl": "tsukushi", "name": "まじかるヴィーナス(つくし)", "zhs_name": "魔法维纳斯(筑紫)", "zht_name": "", "en_name": "Magical Venus (Tsukushi)", "kr_name": "매지컬 비너스(츠쿠시)", "type": "apl", "pow": "3786", "tec": "4486", "stm": "4154", "apl": "550", "skill1": "高度な心理戦C", "skill2": "隠しきれない魅力5", "skill3": "可憐なフェイント", "sell": "2021/4/15", "resell": "2022/6/16", "break": "1", "special_fun": "附带小道具魔法棒，爆衣时有闪烁效果，头部饰品可设定隐藏。"
  },
  {
    "id": "497", "girl": "kokoro", "name": "まじかるヴィーナス(こころ)", "zhs_name": "魔法维纳斯(海咲・心)", "zht_name": "", "en_name": "Magical Venus (Misaki・kokoro)", "kr_name": "매지컬 비너스(미사키・코코로)", "type": "apl", "pow": "3806", "tec": "4556", "stm": "4164", "apl": "550", "skill1": "裏の裏を突くフェイントF", "skill2": "高度な心理戦B", "skill3": "隠しきれない魅力4", "sell": "2021/4/15", "resell": "2022/6/16", "break": "1", "special_fun": "附带小道具魔法棒，爆衣时有闪烁效果，头部饰品可设定隐藏。"
  },
  {
    "id": "498", "girl": "misaki", "name": "まじかるヴィーナス(みさき)", "zhs_name": "魔法维纳斯(海咲・心)", "zht_name": "", "en_name": "Magical Venus (Misaki・kokoro)", "kr_name": "매지컬 비너스(미사키・코코로)", "type": "apl", "pow": "3806", "tec": "4556", "stm": "4164", "apl": "550", "skill1": "裏の裏を突くフェイントF", "skill2": "高度な心理戦B", "skill3": "隠しきれない魅力4", "sell": "2021/4/15", "resell": "2022/6/16", "break": "1", "special_fun": "附带小道具魔法棒，爆衣时有闪烁效果，头部饰品可设定隐藏。"
  },
  {
    "id": "499", "girl": "nanami", "name": "ブーケ・アルストロメリア(ななみ)", "zhs_name": "花束・水仙百合(七海)", "zht_name": "花束‧水仙百合(七海)", "en_name": "Bouquet Alstroemeria (Nanami)", "kr_name": "부케 알스트로메리아(나나미)", "type": "pow", "pow": "5622", "tec": "4014", "stm": "4064", "apl": "200", "skill1": "強烈スパイクG", "skill2": "アルストロメリアのパワー", "skill3": "豪快なスパイク", "sell": "2021/4/16", "resell": "2021/10/22 2022/4/16 2023/4/16", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。新角色破天荒的生日只抽1件衣服，没有宝石生日导致连戒指都没有，来不及做改色？（滑稽）"
  },
  {
    "id": "500", "girl": "tamaki", "name": "プランタン・ロゼ(たまき)", "zhs_name": "春天玫瑰(环)", "zht_name": "", "en_name": "Printemps Rose (Tamaki)", "kr_name": "쁘렝땅 로즈(타마키)", "type": "pow", "pow": "5172", "tec": "3486", "stm": "3984", "apl": "200", "skill1": "圧倒的な気迫D", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2021/4/22", "resell": "2022/3/3", "break": "1", "special_fun": ""
  },
  {
    "id": "501", "girl": "ayane", "name": "プランタン・ロゼ(あやね)", "zhs_name": "春天玫瑰", "zht_name": "", "en_name": "Printemps Rose", "kr_name": "쁘렝땅 로즈", "type": "pow", "pow": "5082", "tec": "3566", "stm": "4094", "apl": "200", "skill1": "強烈スパイクA", "skill2": "不動のレシーブB", "skill3": "秘められたパワー3", "sell": "2021/4/22", "resell": "2022/3/3", "break": "1", "special_fun": ""
  },
  {
    "id": "502", "girl": "hitomi", "name": "プランタン・ロゼ(ヒトミ)", "zhs_name": "春天玫瑰", "zht_name": "", "en_name": "Printemps Rose", "kr_name": "쁘렝땅 로즈", "type": "pow", "pow": "5082", "tec": "3566", "stm": "4094", "apl": "200", "skill1": "強烈スパイクA", "skill2": "不動のレシーブB", "skill3": "秘められたパワー3", "sell": "2021/4/22", "resell": "2022/3/3", "break": "1", "special_fun": ""
  },
  {
    "id": "503", "girl": "leifang", "name": "ブーケ・アルストロメリア(レイファン)", "zhs_name": "花束・水仙百合(丽凤)", "zht_name": "花束・水仙百合(麗鳳)", "en_name": "Bouquet Alstroemeria (Leifang)", "kr_name": "부케 알스트로메리아(레이팡)", "type": "tec", "pow": "4222", "tec": "5364", "stm": "4114", "apl": "200", "skill1": "裏の裏を突くフェイントG", "skill2": "アルストロメリアのテクニック", "skill3": "可憐なフェイント", "sell": "2021/4/23", "resell": "2021/10/22 2022/4/23 2023/4/23", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。别问为什么技巧不是5622，问就是量子纠缠导致削弱。雷芳双tec的ssr饰品成为最大赢家。"
  },
  {
    "id": "504_1", "girl": "marie", "name": "レイク・エルヴン(マリー)", "zhs_name": "精灵湖", "zht_name": "", "en_name": "Lake Elven", "kr_name": "레이크 엘븐", "type": "tec", "pow": "3576", "tec": "5082", "stm": "3984", "apl": "200", "skill1": "高度な心理戦B", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2021/4/28", "resell": "2023/2/16", "break": "1", "special_fun": "我相信kt的人一定不认识塞蕾斯汀"
  },
  {
    "id": "504_2", "girl": "helena", "name": "レイク・エルヴン(エレナ)", "zhs_name": "精灵湖", "zht_name": "", "en_name": "Lake Elven", "kr_name": "레이크 엘븐", "type": "tec", "pow": "3576", "tec": "5082", "stm": "3984", "apl": "200", "skill1": "高度な心理戦B", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2021/4/28", "resell": "2023/2/16", "break": "1", "special_fun": "我相信kt的人一定不认识塞蕾斯汀"
  },
  {
    "id": "504_3", "girl": "tamaki", "name": "レイク・エルヴン(たまき)", "zhs_name": "精灵湖", "zht_name": "", "en_name": "Lake Elven", "kr_name": "레이크 엘븐", "type": "tec", "pow": "3576", "tec": "5082", "stm": "3984", "apl": "200", "skill1": "高度な心理戦B", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2021/4/28", "resell": "2023/2/16", "break": "1", "special_fun": "我相信kt的人一定不认识塞蕾斯汀"
  },
  {
    "id": "504_4", "girl": "fiona", "name": "レイク・エルヴン(フィオナ)", "zhs_name": "精灵湖", "zht_name": "", "en_name": "Lake Elven", "kr_name": "레이크 엘븐", "type": "tec", "pow": "3576", "tec": "5082", "stm": "3984", "apl": "200", "skill1": "高度な心理戦B", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2021/4/28", "resell": "2023/2/16", "break": "1", "special_fun": "我相信kt的人一定不认识塞蕾斯汀"
  },
  {
    "id": "504_5", "girl": "patty", "name": "レイク・エルヴン(パティ)", "zhs_name": "精灵湖", "zht_name": "", "en_name": "Lake Elven", "kr_name": "레이크 엘븐", "type": "tec", "pow": "3576", "tec": "5082", "stm": "3984", "apl": "200", "skill1": "高度な心理戦B", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2021/4/28", "resell": "2023/2/16", "break": "1", "special_fun": "我相信kt的人一定不认识塞蕾斯汀"
  },
  {
    "id": "505", "girl": "nagisa", "name": "ブーケ・カーネーション(なぎさ)", "zhs_name": "花束・康乃馨(凪咲)", "zht_name": "花束．康乃馨(凪咲)", "en_name": "Bouquet Carnation (Nagisa)", "kr_name": "부케(카네이션)(나기사)", "type": "pow", "pow": "5622", "tec": "3994", "stm": "4084", "apl": "200", "skill1": "強烈スパイクG", "skill2": "カーネーションのパワー", "skill3": "豪快なスパイク", "sell": "2021/5/5", "resell": "2021/10/22 2022/5/5 2023/5/5", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。"
  },
  {
    "id": "506", "girl": "honoka", "name": "こもれびハミング(ほのか)", "zhs_name": "树荫光斑蜂鸟(穗香)", "zht_name": "", "en_name": "Sunlight Humming (Honoka)", "kr_name": "햇살 속의 허밍(호노카)", "type": "stm", "pow": "4444", "tec": "3656", "stm": "4942", "apl": "200", "skill1": "圧倒的な気迫F", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2021/5/6", "resell": "2022/9/8", "break": "1", "special_fun": ""
  },
  {
    "id": "507", "girl": "monica", "name": "こもれびハミング(モニカ)", "zhs_name": "树荫光斑蜂鸟(露娜・莫妮卡)", "zht_name": "", "en_name": "Sunlight Humming (Luna・monica)", "kr_name": "햇살 속의 허밍(루나・모니카)", "type": "stm", "pow": "4384", "tec": "3716", "stm": "5042", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "灼熱のダンスE", "skill3": "内から湧き上がるスタミナ3", "sell": "2021/5/6", "resell": "2022/9/8", "break": "1", "special_fun": ""
  },
  {
    "id": "508", "girl": "luna", "name": "こもれびハミング(ルナ)", "zhs_name": "树荫光斑蜂鸟(露娜・莫妮卡)", "zht_name": "", "en_name": "Sunlight Humming (Luna・monica)", "kr_name": "햇살 속의 허밍(루나・모니카)", "type": "stm", "pow": "4384", "tec": "3716", "stm": "5042", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "灼熱のダンスE", "skill3": "内から湧き上がるスタミナ3", "sell": "2021/5/6", "resell": "2022/9/8", "break": "1", "special_fun": ""
  },
  {
    "id": "509", "girl": "nyotengu", "name": "ほしぞらきんぎょ(女天狗)", "zhs_name": "星空金鱼(女天狗)", "zht_name": "", "en_name": "Starry Night Goldfish (Nyotengu)", "kr_name": "금붕어(별하늘)(뇨텐구)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈なプレッシャーA", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2021/5/13", "resell": "2022/5/6 2023/4/13", "break": "1", "special_fun": ""
  },
  {
    "id": "510", "girl": "kanna", "name": "おまつりきんぎょ(カンナ)", "zhs_name": "祭典金鱼(神无)", "zht_name": "", "en_name": "Festival Goldfish (Kanna)", "kr_name": "금붕어(축제)(칸나)", "type": "pow", "pow": "5132", "tec": "3416", "stm": "4094", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "プラチナアタッカー", "skill3": "豪快なスパイク", "sell": "2021/5/13", "resell": "2022/5/6 2023/4/13", "break": "1", "special_fun": ""
  },
  {
    "id": "511", "girl": "nanami", "name": "ミッドナイトライト(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4474", "tec": "3416", "stm": "5152", "apl": "200", "skill1": "強烈スパイクD", "skill2": "ミッドナイトのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/13", "resell": "", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)。手部装饰可隐藏"
  },
  {
    "id": "512", "girl": "luna", "name": "トワイライトフィッシュ(ルナ)", "zhs_name": "拂晓之鱼(露娜)", "zht_name": "", "en_name": "Twilight Fish (Luna)", "kr_name": "트와일라이트 피시(루나)", "type": "stm", "pow": "4284", "tec": "3756", "stm": "5002", "apl": "200", "skill1": "圧倒的な気迫C", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2021/5/20", "resell": "2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "513", "girl": "nagisa", "name": "サンセットフィッシュ(なぎさ)", "zhs_name": "日暮之鱼", "zht_name": "", "en_name": "Sunset Fish", "kr_name": "선셋 피시", "type": "stm", "pow": "4124", "tec": "3766", "stm": "5152", "apl": "200", "skill1": "不動のレシーブD", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2021/5/20", "resell": "2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "514", "girl": "momiji", "name": "サンセットフィッシュ(紅葉)", "zhs_name": "日暮之鱼", "zht_name": "", "en_name": "Sunset Fish", "kr_name": "선셋 피시", "type": "stm", "pow": "4124", "tec": "3766", "stm": "5152", "apl": "200", "skill1": "不動のレシーブD", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2021/5/20", "resell": "2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "515", "girl": "hitomi", "name": "ブーケ・カーネーション(ヒトミ)", "zhs_name": "花束・康乃馨(瞳)", "zht_name": "", "en_name": "Bouquet Carnation (Hitomi)", "kr_name": "부케 카네이션(히토미)", "type": "stm", "pow": "4814", "tec": "3664", "stm": "5622", "apl": "200", "skill1": "強烈スパイクG", "skill2": "カーネーションのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/25", "resell": "2021/10/22 2022/5/25 2023/5/25", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。"
  },
  {
    "id": "c4", "girl": "All", "name": "ヴィーナスナイン", "type": "none", "pow": "0", "tec": "0", "stm": "0", "apl": "0", "skill1": "", "skill2": "", "skill3": "", "sell": "2021/5/27", "resell": "N/A", "break": "1", "special_fun": "岛主商店新外形服装。作为礼包3000付费钻 衣服+11红票+棒球小道具（3姿势） 打包销售 仅外形无属性。"
  },
  {
    "id": "516", "girl": "tsukushi", "name": "星砂のスリットワンピ(つくし)", "zhs_name": "各个女孩的SSR泳装“开叉连衣裙”", "zht_name": "", "en_name": "Each Girl's SSR Swimsuit “Slit One-Piece”", "kr_name": "각 캐릭터의SSR 수영복 「슬릿 원피스」", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2021/5/27", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "517_1", "girl": "kasumi", "name": "ソレイユクーシャン(かすみ)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_2", "girl": "honoka", "name": "ソレイユクーシャン(ほのか)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_3", "girl": "marie", "name": "ソレイユクーシャン(マリー)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_4", "girl": "ayane", "name": "ソレイユクーシャン(あやね)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_5", "girl": "nyotengu", "name": "ソレイユクーシャン(女天狗)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_6", "girl": "kokoro", "name": "ソレイユクーシャン(こころ)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_7", "girl": "hitomi", "name": "ソレイユクーシャン(ヒトミ)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_8", "girl": "momiji", "name": "ソレイユクーシャン(紅葉)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_9", "girl": "helena", "name": "ソレイユクーシャン(エレナ)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_10", "girl": "misaki", "name": "ソレイユクーシャン(みさき)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_11", "girl": "luna", "name": "ソレイユクーシャン(ルナ)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_12", "girl": "tamaki", "name": "ソレイユクーシャン(たまき)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_13", "girl": "leifang", "name": "ソレイユクーシャン(レイファン)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_14", "girl": "fiona", "name": "ソレイユクーシャン(フィオナ)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_15", "girl": "nagisa", "name": "ソレイユクーシャン(なぎさ)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_16", "girl": "kanna", "name": "ソレイユクーシャン(カンナ)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_17", "girl": "monica", "name": "ソレイユクーシャン(モニカ)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_18", "girl": "sayuri", "name": "ソレイユクーシャン(さゆり)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_19", "girl": "patty", "name": "ソレイユクーシャン(パティ)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_20", "girl": "tsukushi", "name": "ソレイユクーシャン(つくし)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/5/27", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "517_21", "girl": "lobelia", "name": "ソレイユクーシャン(ロベリア)", "zhs_name": "夕阳", "zht_name": "", "en_name": "Soleil Couchant", "kr_name": "솔레이 쿠숑", "type": "stm", "pow": "4364", "tec": "3456", "stm": "5222", "apl": "200", "skill1": "強烈スパイクC", "skill2": "ソレイユのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/6/3", "resell": "2023/6/1", "break": "1", "special_fun": "使用天狗扇 会出现黄色和紫色的粒子效果(光之舞)。允许和本次的所有服装互相成为狗粮素材满觉。3.5周年庆服装"
  },
  {
    "id": "328_19", "girl": "lobelia", "name": "桃宴桜舞(ロベリア)", "zhs_name": "桃宴樱舞", "zht_name": "", "en_name": "Peach Party Sakura Dance", "kr_name": "도연앵무", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2021/6/3", "resell": "", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_20", "girl": "patty", "name": "桃宴桜舞(パティ)", "zhs_name": "桃宴樱舞(派蒂)", "zht_name": "桃宴櫻舞(派蒂)", "en_name": "Peach Party Sakura Dance (Patty)", "kr_name": "도연앵무(패티)", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2021/6/3", "resell": "", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "328_21", "girl": "tsukushi", "name": "桃宴桜舞(つくし)", "zhs_name": "桃宴樱舞", "zht_name": "", "en_name": "Peach Party Sakura Dance", "kr_name": "도연앵무", "type": "pow", "pow": "4872", "tec": "3606", "stm": "4114", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "咲き誇るパワー", "skill3": "豪快なスパイク", "sell": "2021/6/3", "resell": "", "break": "1", "special_fun": "使用天狗扇 会出现花瓣飞舞效果。允许和本次的所有服装互相成为狗粮素材满觉。2.5周年庆服装"
  },
  {
    "id": "518", "girl": "marie", "name": "ブーケ・ローゼン(マリー)", "zhs_name": "花束・玫瑰(玛莉)", "zht_name": "", "en_name": "Bouquet Rose (Marie)", "kr_name": "부케 로즈(마리)", "type": "stm", "pow": "3684", "tec": "4794", "stm": "5622", "apl": "200", "skill1": "裏の裏を突くフェイントG", "skill2": "ローゼンのスタミナ", "skill3": "可憐なフェイント", "sell": "2021/6/6", "resell": "2021/10/22 2022/6/6", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。懂了，明年再出技巧生日，玛丽第2年生日用3年。"
  },
  {
    "id": "519", "girl": "lobelia", "name": "シークレット・レポート(ロベリア)", "zhs_name": "秘密报告(萝贝莉娅)", "zht_name": "", "en_name": "Secret Report (Lobelia)", "kr_name": "시크릿 리포트(로벨리아)", "type": "tec", "pow": "3476", "tec": "5072", "stm": "4094", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2021/6/10", "resell": "2022/11/10", "break": "1", "special_fun": ""
  },
  {
    "id": "520", "girl": "fiona", "name": "シークレット・レポート(フィオナ)", "zhs_name": "秘密报告(菲欧娜・海莲娜)", "zht_name": "", "en_name": "Secret Report (Fiona・helena)", "kr_name": "시크릿 리포트(피오나・엘레나)", "type": "tec", "pow": "3556", "tec": "5202", "stm": "3984", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "高度な心理戦D", "skill3": "閃きのテクニック6", "sell": "2021/6/10", "resell": "2022/11/10", "break": "1", "special_fun": ""
  },
  {
    "id": "521", "girl": "helena", "name": "シークレット・レポート(エレナ)", "zhs_name": "秘密报告(菲欧娜・海莲娜)", "zht_name": "", "en_name": "Secret Report (Fiona・helena)", "kr_name": "시크릿 리포트(피오나・엘레나)", "type": "tec", "pow": "3556", "tec": "5202", "stm": "3984", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "高度な心理戦D", "skill3": "閃きのテクニック6", "sell": "2021/6/10", "resell": "2022/11/10", "break": "1", "special_fun": ""
  },
  {
    "id": "522", "girl": "nanami", "name": "ジュエル・ダイヤモンド(ななみ)", "zhs_name": "珍宝・钻石(七海)", "zht_name": "", "en_name": "Jewel Diamond (Nanami)", "kr_name": "주얼 다이아몬드(나나미)", "type": "stm", "pow": "4694", "tec": "3326", "stm": "5322", "apl": "200", "skill1": "強烈スパイクE", "skill2": "ダイヤモンド・スタミナ", "skill3": "豪快なスパイク", "sell": "2021/6/17", "resell": "2022/4/16 2023/4/16", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现白色粒子效果(光之舞)。非生日开生日限定关卡，移除免费钻石奖励，戒指回想都没有。旧生日改个颜色拆开抽还作为封面排名流行超特大加成，好时代来临了。作田P新人上位这么顶，你萌死了呢"
  },
  {
    "id": "523", "girl": "lobelia", "name": "ジュエル・パール(ロベリア)", "zhs_name": "珍宝・珍珠(萝贝莉娅)", "zht_name": "", "en_name": "Jewel Pearl (Lobelia)", "kr_name": "주얼 진주(로벨리아)", "type": "tec", "pow": "3416", "tec": "5322", "stm": "4204", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "パール・テクニック", "skill3": "可憐なフェイント", "sell": "2021/6/17", "resell": "2022/6/25 2023/6/25", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现淡粉色粒子效果(光之舞)。非生日开生日限定关卡，移除免费钻石奖励，戒指回想都没有。旧生日改个颜色拆开抽还作为封面排名流行超特大加成，好时代来临了。作田P新人上位这么顶，你萌死了呢"
  },
  {
    "id": "334_5", "girl": "ayane", "name": "レイニーフロッグ(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "4526", "tec": "3776", "stm": "4124", "apl": "550", "skill1": "強烈スパイクC", "skill2": "隠しきれない魅力3", "skill3": "豪快なスパイク", "sell": "2021/6/17", "resell": "2022/6/8 2023/6/21", "break": "1", "special_fun": ""
  },
  {
    "id": "334_6", "girl": "leifang", "name": "レイニーフロッグ(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "4566", "tec": "3816", "stm": "4144", "apl": "550", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫B", "skill3": "隠しきれない魅力5", "sell": "2021/6/17", "resell": "2022/6/8 2023/6/21", "break": "1", "special_fun": ""
  },
  {
    "id": "334_7", "girl": "kokoro", "name": "レイニーフロッグ(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "4566", "tec": "3816", "stm": "4144", "apl": "550", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫B", "skill3": "隠しきれない魅力5", "sell": "2021/6/17", "resell": "2022/6/8 2023/6/21", "break": "1", "special_fun": ""
  },
  {
    "id": "524", "girl": "nagisa", "name": "ほやほやエプロン(なぎさ)", "zhs_name": "暖呼呼围裙(凪咲)", "zht_name": "", "en_name": "Toasty Apron (Nagisa)", "kr_name": "따끈따끈한 앞치마(나기사)", "type": "pow", "pow": "5112", "tec": "3496", "stm": "4034", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "秘められたパワー5", "skill3": "熱烈なエール", "sell": "2021/6/24", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "525", "girl": "marie", "name": "ほやほやエプロン(マリー)", "zhs_name": "暖呼呼围裙(玛莉・神无)", "zht_name": "", "en_name": "Toasty Apron (Marie・kanna)", "kr_name": "따끈따끈한 앞치마(마리・칸나)", "type": "pow", "pow": "5042", "tec": "3526", "stm": "4174", "apl": "200", "skill1": "強烈スパイクB", "skill2": "強烈なプレッシャーC", "skill3": "秘められたパワー4", "sell": "2021/6/24", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "526", "girl": "kanna", "name": "ほやほやエプロン(カンナ)", "zhs_name": "暖呼呼围裙(玛莉・神无)", "zht_name": "", "en_name": "Toasty Apron (Marie・kanna)", "kr_name": "따끈따끈한 앞치마(마리・칸나)", "type": "pow", "pow": "5042", "tec": "3526", "stm": "4174", "apl": "200", "skill1": "強烈スパイクB", "skill2": "強烈なプレッシャーC", "skill3": "秘められたパワー4", "sell": "2021/6/24", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "527", "girl": "lobelia", "name": "ブーケ・ローゼン(ロベリア)", "zhs_name": "花束・玫瑰(萝贝莉娅)", "zht_name": "", "en_name": "Bouquet Rose (Lobelia)", "kr_name": "부케 로즈(로벨리아)", "type": "stm", "pow": "3664", "tec": "4814", "stm": "5622", "apl": "200", "skill1": "裏の裏を突くフェイントG", "skill2": "ローゼンのスタミナ", "skill3": "可憐なフェイント", "sell": "2021/6/25", "resell": "2021/10/22 2022/6/25 2023/6/25", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。"
  },
  {
    "id": "528", "girl": "lobelia", "name": "空色のスリットワンピ(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2021/7/1", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "529_1", "girl": "kasumi", "name": "スイートスポット(かすみ)", "zhs_name": "甜蜜点(霞)", "zht_name": "甜蜜點(霞)", "en_name": "Sweet Spot (Kasumi)", "kr_name": "스위트 스팟(카스미)", "type": "stm", "pow": "3546", "tec": "4294", "stm": "5202", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "スイートなスタミナ", "skill3": "熱烈なエール", "sell": "2021/7/1", "resell": "2023/7/13", "break": "1", "special_fun": ""
  },
  {
    "id": "529_2", "girl": "honoka", "name": "スイートスポット(ほのか)", "zhs_name": "甜蜜点(穗香)", "zht_name": "甜蜜點(霞)", "en_name": "Sweet Spot (Honoka)", "kr_name": "스위트 스팟(호노카)", "type": "stm", "pow": "3546", "tec": "4294", "stm": "5202", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "スイートなスタミナ", "skill3": "熱烈なエール", "sell": "2021/7/1", "resell": "2023/7/13", "break": "1", "special_fun": ""
  },
  {
    "id": "529_3", "girl": "tamaki", "name": "スイートスポット(たまき)", "zhs_name": "甜蜜点(环)", "zht_name": "甜蜜點(環)", "en_name": "Sweet Spot (Tamaki)", "kr_name": "스위트 스팟(타마키)", "type": "stm", "pow": "3546", "tec": "4294", "stm": "5202", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "スイートなスタミナ", "skill3": "熱烈なエール", "sell": "2021/7/1", "resell": "2023/7/13", "break": "1", "special_fun": ""
  },
  {
    "id": "529_4", "girl": "fiona", "name": "スイートスポット(フィオナ)", "zhs_name": "甜蜜点(菲欧娜)", "zht_name": "甜蜜點(菲歐娜)", "en_name": "Sweet Spot (Fiona)", "kr_name": "스위트 스팟(피오나)", "type": "stm", "pow": "3546", "tec": "4294", "stm": "5202", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "スイートなスタミナ", "skill3": "熱烈なエール", "sell": "2021/7/1", "resell": "2023/7/13", "break": "1", "special_fun": ""
  },
  {
    "id": "529_5", "girl": "sayuri", "name": "スイートスポット(さゆり)", "zhs_name": "甜蜜点(小百合)", "zht_name": "甜蜜點(小百合)", "en_name": "Sweet Spot (Sayuri)", "kr_name": "스위트 스팟(사유리)", "type": "stm", "pow": "3546", "tec": "4294", "stm": "5202", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "スイートなスタミナ", "skill3": "熱烈なエール", "sell": "2021/7/1", "resell": "2023/7/13", "break": "1", "special_fun": ""
  },
  {
    "id": "530", "girl": "misaki", "name": "ブーケ・ハイビスカス(みさき)", "zhs_name": "花束・扶桑(海咲)", "zht_name": "", "en_name": "Bouquet Hibiscus (Misaki)", "kr_name": "부케 히비스커스(미사키)", "type": "pow", "pow": "5622", "tec": "4004", "stm": "4074", "apl": "200", "skill1": "強烈スパイクG", "skill2": "ハイビスカスのパワー", "skill3": "豪快なスパイク", "sell": "2021/7/7", "resell": "2021/10/22 2022/7/7 2023/7/7", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。游戏唯一女主角终于回到应有的强度，抽就完事了。"
  },
  {
    "id": "531", "girl": "monica", "name": "ミルキー・プラム(モニカ)", "zhs_name": "奶白布霖(莫妮卡)", "zht_name": "", "en_name": "Milky Plum (Monica)", "kr_name": "밀키 플럼(모니카)", "type": "apl", "pow": "3726", "tec": "4526", "stm": "4174", "apl": "550", "skill1": "高度な心理戦B", "skill2": "隠しきれない魅力5", "skill3": "可憐なフェイント", "sell": "2021/7/9", "resell": "2022/7/21", "break": "1", "special_fun": ""
  },
  {
    "id": "532", "girl": "patty", "name": "ピンキー・プラム(パティ)", "zhs_name": "粉嫩布霖(派蒂)", "zht_name": "", "en_name": "Pinky Plum (Patty)", "kr_name": "핑키 플럼(패티)", "type": "apl", "pow": "3816", "tec": "4586", "stm": "4124", "apl": "550", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦D", "skill3": "隠しきれない魅力6", "sell": "2021/7/9", "resell": "2022/7/21", "break": "1", "special_fun": ""
  },
  {
    "id": "533", "girl": "elise", "name": "モノクローム・ウィズ(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3804", "tec": "5172", "stm": "3766", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "高度な心理戦C", "skill3": "閃きのテクニック3", "sell": "2021/7/14", "resell": "", "break": "1", "special_fun": "你们找的是Alice，跟我elise有什么关系（滑稽）。FF7re联动（伪）2女主都到位了"
  },
  {
    "id": "534", "girl": "kokoro", "name": "ミスティ・リリー(こころ)", "zhs_name": "神秘・百合(心)", "zht_name": "", "en_name": "Misty Lily (Kokoro)", "kr_name": "미스티 릴리(코코로)", "type": "tec", "pow": "3526", "tec": "5132", "stm": "3984", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "閃きのテクニック5", "skill3": "可憐なフェイント", "sell": "2021/7/14", "resell": "2022/7/14 2023/4/27", "break": "1", "special_fun": ""
  },
  {
    "id": "535", "girl": "tsukushi", "name": "ミスティ・リリー(つくし)", "zhs_name": "神秘・百合(筑紫)", "zht_name": "", "en_name": "Misty Lily (Tsukushi)", "kr_name": "미스티 릴리(츠쿠시)", "type": "tec", "pow": "3616", "tec": "5032", "stm": "4094", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "灼熱のダンスB", "skill3": "閃きのテクニック4", "sell": "2021/7/14", "resell": "2022/7/14 2023/4/27", "break": "1", "special_fun": ""
  },
  {
    "id": "536", "girl": "patty", "name": "おつまみシュリンプ(パティ)", "zhs_name": "拽拽衬衫(派蒂)", "zht_name": "", "en_name": "Appetizer Shrimp (Patty)", "kr_name": "에피타이저 쉬림프(패티)", "type": "stm", "pow": "3626", "tec": "4264", "stm": "5152", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2021/7/21", "resell": "", "break": "1", "special_fun": "可拉扯交互的衣服、允许多部分拉扯"
  },
  {
    "id": "537", "girl": "ayane", "name": "おつまみシュリンプ(あやね)", "zhs_name": "拽拽衬衫(绫音・女天狗)", "zht_name": "", "en_name": "Appetizer Shrimp (Ayane・nyotengu)", "kr_name": "에피타이저 쉬림프(아야네・뇨텐구)", "type": "stm", "pow": "3666", "tec": "4414", "stm": "5062", "apl": "200", "skill1": "灼熱のダンスD", "skill2": "裏の裏を突くフェイントB", "skill3": "内から湧き上がるスタミナ6", "sell": "2021/7/21", "resell": "", "break": "1", "special_fun": "可拉扯交互的衣服、允许多部分拉扯"
  },
  {
    "id": "538", "girl": "nyotengu", "name": "おつまみシュリンプ(女天狗)", "zhs_name": "拽拽衬衫(绫音・女天狗)", "zht_name": "", "en_name": "Appetizer Shrimp (Ayane・nyotengu)", "kr_name": "에피타이저 쉬림프(아야네・뇨텐구)", "type": "stm", "pow": "3666", "tec": "4414", "stm": "5062", "apl": "200", "skill1": "灼熱のダンスD", "skill2": "裏の裏を突くフェイントB", "skill3": "内から湧き上がるスタミナ6", "sell": "2021/7/21", "resell": "", "break": "1", "special_fun": "可拉扯交互的衣服、允许多部分拉扯"
  },
  {
    "id": "539_1", "girl": "misaki", "name": "ムーリングライン(みさき)", "zhs_name": "锚绳", "zht_name": "", "en_name": "Mulling Line", "kr_name": "물링 라인", "type": "pow", "pow": "5122", "tec": "3516", "stm": "4004", "apl": "200", "skill1": "不動のレシーブD", "skill2": "秘められたパワー3", "skill3": "熱烈なエール", "sell": "2021/7/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "539_2", "girl": "honoka", "name": "ムーリングライン(ほのか)", "zhs_name": "锚绳", "zht_name": "", "en_name": "Mulling Line", "kr_name": "물링 라인", "type": "pow", "pow": "5122", "tec": "3516", "stm": "4004", "apl": "200", "skill1": "不動のレシーブD", "skill2": "秘められたパワー3", "skill3": "熱烈なエール", "sell": "2021/7/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "539_3", "girl": "hitomi", "name": "ムーリングライン(ヒトミ)", "zhs_name": "锚绳", "zht_name": "", "en_name": "Mulling Line", "kr_name": "물링 라인", "type": "pow", "pow": "5122", "tec": "3516", "stm": "4004", "apl": "200", "skill1": "不動のレシーブD", "skill2": "秘められたパワー3", "skill3": "熱烈なエール", "sell": "2021/7/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "539_4", "girl": "momiji", "name": "ムーリングライン(紅葉)", "zhs_name": "锚绳", "zht_name": "", "en_name": "Mulling Line", "kr_name": "물링 라인", "type": "pow", "pow": "5122", "tec": "3516", "stm": "4004", "apl": "200", "skill1": "不動のレシーブD", "skill2": "秘められたパワー3", "skill3": "熱烈なエール", "sell": "2021/7/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "539_5", "girl": "luna", "name": "ムーリングライン(ルナ)", "zhs_name": "锚绳", "zht_name": "", "en_name": "Mulling Line", "kr_name": "물링 라인", "type": "pow", "pow": "5122", "tec": "3516", "stm": "4004", "apl": "200", "skill1": "不動のレシーブD", "skill2": "秘められたパワー3", "skill3": "熱烈なエール", "sell": "2021/7/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "539_6", "girl": "tamaki", "name": "ムーリングライン(たまき)", "zhs_name": "锚绳", "zht_name": "", "en_name": "Mulling Line", "kr_name": "물링 라인", "type": "pow", "pow": "5122", "tec": "3516", "stm": "4004", "apl": "200", "skill1": "不動のレシーブD", "skill2": "秘められたパワー3", "skill3": "熱烈なエール", "sell": "2021/7/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "539_7", "girl": "fiona", "name": "ムーリングライン(フィオナ)", "zhs_name": "锚绳", "zht_name": "", "en_name": "Mulling Line", "kr_name": "물링 라인", "type": "pow", "pow": "5122", "tec": "3516", "stm": "4004", "apl": "200", "skill1": "不動のレシーブD", "skill2": "秘められたパワー3", "skill3": "熱烈なエール", "sell": "2021/7/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "539_8", "girl": "monica", "name": "ムーリングライン(モニカ)", "zhs_name": "锚绳", "zht_name": "", "en_name": "Mulling Line", "kr_name": "물링 라인", "type": "pow", "pow": "5122", "tec": "3516", "stm": "4004", "apl": "200", "skill1": "不動のレシーブD", "skill2": "秘められたパワー3", "skill3": "熱烈なエール", "sell": "2021/7/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "539_9", "girl": "sayuri", "name": "ムーリングライン(さゆり)", "zhs_name": "锚绳", "zht_name": "", "en_name": "Mulling Line", "kr_name": "물링 라인", "type": "pow", "pow": "5122", "tec": "3516", "stm": "4004", "apl": "200", "skill1": "不動のレシーブD", "skill2": "秘められたパワー3", "skill3": "熱烈なエール", "sell": "2021/7/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "540", "girl": "patty", "name": "ブーケ・ハイビスカス(パティ)", "zhs_name": "花束・扶桑(派蒂)", "zht_name": "", "en_name": "Bouquet Hibiscus (Patty)", "kr_name": "부케 히비스커스(패티)", "type": "pow", "pow": "5622", "tec": "3914", "stm": "4164", "apl": "200", "skill1": "強烈スパイクG", "skill2": "ハイビスカスのパワー", "skill3": "豪快なスパイク", "sell": "2021/7/31", "resell": "2021/10/22 2022/7/31 2023/7/31", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。"
  },
  {
    "id": "225_19", "girl": "tsukushi", "name": "すずかぜロマンチカ(つくし)", "zhs_name": "凉风罗曼(筑紫)", "zht_name": "", "en_name": "Breeze Romantika (Tsukushi)", "kr_name": "산들바람 로맨티카(츠쿠시)", "type": "tec", "pow": "3566", "tec": "5062", "stm": "4014", "apl": "200", "skill1": "鉄壁のレシーブF", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2021/8/4", "resell": "2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "225_20", "girl": "lobelia", "name": "すずかぜロマンチカ(ロベリア)", "zhs_name": "凉风罗曼(萝贝莉娅)", "zht_name": "", "en_name": "Breeze Romantika (Lobelia)", "kr_name": "산들바람 로맨티카(로벨리아)", "type": "tec", "pow": "3616", "tec": "5032", "stm": "4094", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "高度な心理戦E", "skill3": "閃きのテクニック3", "sell": "2021/8/4", "resell": "2022/7/28", "break": "1", "special_fun": ""
  },
  {
    "id": "541", "girl": "elise", "name": "ロートヴァイン(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3936", "tec": "4284", "stm": "4822", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "ロートヴァインのスタミナ", "skill3": "熱烈なエール", "sell": "2021/8/4", "resell": "", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "542", "girl": "ayane", "name": "ブーケ・リシアンサス(あやね)", "zhs_name": "花束・洋桔梗(绫音)", "zht_name": "", "en_name": "Bouquet Lisianthus (Ayane)", "kr_name": "부케 리시안셔스(아야네)", "type": "tec", "pow": "4192", "tec": "5364", "stm": "4144", "apl": "200", "skill1": "裏の裏を突くフェイントG", "skill2": "リシアンサスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/8/5", "resell": "2021/10/22 2022/8/5 2023/8/5", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。"
  },
  {
    "id": "355_13", "girl": "kasumi", "name": "レイズザセイル(かすみ)", "zhs_name": "扬帆(霞)", "zht_name": "", "en_name": "Raise The Sail (Kasumi)", "kr_name": "레이즈 더 세일(카스미)", "type": "stm", "pow": "3616", "tec": "4294", "stm": "5132", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "順風満帆のスタミナ", "skill3": "可憐なフェイント", "sell": "2021/8/12", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "355_14", "girl": "kokoro", "name": "レイズザセイル(こころ)", "zhs_name": "扬帆(心)", "zht_name": "", "en_name": "Raise The Sail (Kokoro)", "kr_name": "레이즈 더 세일(코코로)", "type": "stm", "pow": "3676", "tec": "4434", "stm": "5032", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "灼熱のダンスD", "skill3": "順風満帆のスタミナ", "sell": "2021/8/12", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "543", "girl": "tamaki", "name": "ブーケ・リシアンサス(たまき)", "zhs_name": "花束・洋桔梗(环)", "zht_name": "", "en_name": "Bouquet Lisianthus (Tamaki)", "kr_name": "부케 리시안셔스(타마키)", "type": "pow", "pow": "5622", "tec": "3954", "stm": "4124", "apl": "200", "skill1": "強烈スパイクG", "skill2": "リシアンサスのパワー", "skill3": "豪快なスパイク", "sell": "2021/8/19", "resell": "2021/10/22 2022/8/19", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。"
  },
  {
    "id": "544", "girl": "elise", "name": "平穏世代の韋駄天達・ピサラ(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3466", "tec": "4564", "stm": "5212", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ピサラのスタミナ", "skill3": "可憐なフェイント", "sell": "2021/8/20", "resell": "", "break": "1", "special_fun": "首次氪金服加入联动。作田P发大财！允许和同活动的其他修女限定服装互相成为狗粮素材满觉"
  },
  {
    "id": "545_1", "girl": "marie", "name": "平穏世代の韋駄天達・ギル(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3486", "tec": "5122", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦C", "skill3": "ギルのテクニック", "sell": "2021/8/20", "resell": "", "break": "0", "special_fun": "平穏世代の韋駄天達联动服装，预热3个月结果极其敷衍的服装以及活动。服装无满破效果"
  },
  {
    "id": "545_2", "girl": "ayane", "name": "平穏世代の韋駄天達・ギル(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3486", "tec": "5122", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦C", "skill3": "ギルのテクニック", "sell": "2021/8/20", "resell": "", "break": "0", "special_fun": "平穏世代の韋駄天達联动服装，预热3个月结果极其敷衍的服装以及活动。服装无满破效果"
  },
  {
    "id": "545_3", "girl": "hitomi", "name": "平穏世代の韋駄天達・ギル(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3486", "tec": "5122", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦C", "skill3": "ギルのテクニック", "sell": "2021/8/20", "resell": "", "break": "0", "special_fun": "平穏世代の韋駄天達联动服装，预热3个月结果极其敷衍的服装以及活动。服装无满破效果"
  },
  {
    "id": "545_4", "girl": "momiji", "name": "平穏世代の韋駄天達・ギル(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3486", "tec": "5122", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦C", "skill3": "ギルのテクニック", "sell": "2021/8/20", "resell": "", "break": "0", "special_fun": "平穏世代の韋駄天達联动服装，预热3个月结果极其敷衍的服装以及活动。服装无满破效果"
  },
  {
    "id": "545_5", "girl": "helena", "name": "平穏世代の韋駄天達・ギル(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3486", "tec": "5122", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦C", "skill3": "ギルのテクニック", "sell": "2021/8/20", "resell": "", "break": "0", "special_fun": "平穏世代の韋駄天達联动服装，预热3个月结果极其敷衍的服装以及活动。服装无满破效果"
  },
  {
    "id": "545_6", "girl": "monica", "name": "平穏世代の韋駄天達・ギル(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3486", "tec": "5122", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦C", "skill3": "ギルのテクニック", "sell": "2021/8/20", "resell": "", "break": "0", "special_fun": "平穏世代の韋駄天達联动服装，预热3个月结果极其敷衍的服装以及活动。服装无满破效果"
  },
  {
    "id": "546_1", "girl": "misaki", "name": "黒炎のラビリンス(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3536", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2021/8/20", "resell": "", "break": "1", "special_fun": "老衣服换个颜色就好意思拿出来当联动？"
  },
  {
    "id": "546_2", "girl": "honoka", "name": "黒炎のラビリンス(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3536", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2021/8/20", "resell": "", "break": "1", "special_fun": "老衣服换个颜色就好意思拿出来当联动？"
  },
  {
    "id": "546_3", "girl": "nyotengu", "name": "黒炎のラビリンス(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3536", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2021/8/20", "resell": "", "break": "1", "special_fun": "老衣服换个颜色就好意思拿出来当联动？"
  },
  {
    "id": "546_4", "girl": "luna", "name": "黒炎のラビリンス(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3536", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2021/8/20", "resell": "", "break": "1", "special_fun": "老衣服换个颜色就好意思拿出来当联动？"
  },
  {
    "id": "546_5", "girl": "leifang", "name": "黒炎のラビリンス(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3536", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2021/8/20", "resell": "", "break": "1", "special_fun": "老衣服换个颜色就好意思拿出来当联动？"
  },
  {
    "id": "546_6", "girl": "nagisa", "name": "黒炎のラビリンス(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3536", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2021/8/20", "resell": "", "break": "1", "special_fun": "老衣服换个颜色就好意思拿出来当联动？"
  },
  {
    "id": "546_7", "girl": "sayuri", "name": "黒炎のラビリンス(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3536", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2021/8/20", "resell": "", "break": "1", "special_fun": "老衣服换个颜色就好意思拿出来当联动？"
  },
  {
    "id": "546_8", "girl": "tsukushi", "name": "黒炎のラビリンス(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3536", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2021/8/20", "resell": "", "break": "1", "special_fun": "老衣服换个颜色就好意思拿出来当联动？"
  },
  {
    "id": "546_9", "girl": "lobelia", "name": "黒炎のラビリンス(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3536", "stm": "4064", "apl": "200", "skill1": "強烈なプレッシャーD", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2021/8/20", "resell": "", "break": "1", "special_fun": "老衣服换个颜色就好意思拿出来当联动？"
  },
  {
    "id": "545_7", "girl": "kasumi", "name": "平穏世代の韋駄天達・ギル(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3486", "tec": "5122", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦C", "skill3": "ギルのテクニック", "sell": "2021/8/27", "resell": "", "break": "0", "special_fun": "平穏世代の韋駄天達联动服装，预热3个月结果极其敷衍的服装以及活动。服装无满破效果"
  },
  {
    "id": "545_8", "girl": "kokoro", "name": "平穏世代の韋駄天達・ギル(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3486", "tec": "5122", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦C", "skill3": "ギルのテクニック", "sell": "2021/8/27", "resell": "", "break": "0", "special_fun": "平穏世代の韋駄天達联动服装，预热3个月结果极其敷衍的服装以及活动。服装无满破效果"
  },
  {
    "id": "545_9", "girl": "tamaki", "name": "平穏世代の韋駄天達・ギル(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3486", "tec": "5122", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦C", "skill3": "ギルのテクニック", "sell": "2021/8/27", "resell": "", "break": "0", "special_fun": "平穏世代の韋駄天達联动服装，预热3个月结果极其敷衍的服装以及活动。服装无满破效果"
  },
  {
    "id": "545_10", "girl": "fiona", "name": "平穏世代の韋駄天達・ギル(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3486", "tec": "5122", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦C", "skill3": "ギルのテクニック", "sell": "2021/8/27", "resell": "", "break": "0", "special_fun": "平穏世代の韋駄天達联动服装，预热3个月结果极其敷衍的服装以及活动。服装无满破效果"
  },
  {
    "id": "545_11", "girl": "kanna", "name": "平穏世代の韋駄天達・ギル(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3486", "tec": "5122", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦C", "skill3": "ギルのテクニック", "sell": "2021/8/27", "resell": "", "break": "0", "special_fun": "平穏世代の韋駄天達联动服装，预热3个月结果极其敷衍的服装以及活动。服装无满破效果"
  },
  {
    "id": "545_12", "girl": "patty", "name": "平穏世代の韋駄天達・ギル(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3486", "tec": "5122", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦C", "skill3": "ギルのテクニック", "sell": "2021/8/27", "resell": "", "break": "0", "special_fun": "平穏世代の韋駄天達联动服装，预热3个月结果极其敷衍的服装以及活动。服装无满破效果"
  },
  {
    "id": "547", "girl": "elise", "name": "ブーケ・ダリア(エリーゼ)", "zhs_name": "花束・大丽花(伊莉丝)", "zht_name": "", "en_name": "Bouquet Dahlia (Elise)", "kr_name": "부케 달리아(엘리제)", "type": "tec", "pow": "4152", "tec": "5364", "stm": "4184", "apl": "200", "skill1": "裏の裏を突くフェイントG", "skill2": "ダリアのテクニック", "skill3": "可憐なフェイント", "sell": "2021/9/3", "resell": "2021/10/22 2022/9/3", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。生日拆开卖，作田发大财。"
  },
  {
    "id": "548_1", "girl": "misaki", "name": "たまゆら花火(みさき)", "zhs_name": "玉响烟花(海咲)", "zht_name": "", "en_name": "Fleeting Fireworks (Misaki)", "kr_name": "찰나의 불꽃놀이(미사키)", "type": "stm", "pow": "4194", "tec": "3646", "stm": "5202", "apl": "200", "skill1": "強烈スパイクB", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2021/9/3", "resell": "2023/7/20", "break": "1", "special_fun": ""
  },
  {
    "id": "548_2", "girl": "momiji", "name": "たまゆら花火(紅葉)", "zhs_name": "玉响烟花(红叶・小百合)", "zht_name": "", "en_name": "Fleeting Fireworks (Momiji・sayuri)", "kr_name": "찰나의 불꽃놀이(모미지・사유리)", "type": "stm", "pow": "4274", "tec": "3726", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "強烈スパイクD", "skill3": "内から湧き上がるスタミナ3", "sell": "2021/9/3", "resell": "2023/7/20", "break": "1", "special_fun": ""
  },
  {
    "id": "548_3", "girl": "sayuri", "name": "たまゆら花火(さゆり)", "zhs_name": "玉响烟花(红叶・小百合)", "zht_name": "", "en_name": "Fleeting Fireworks (Momiji・sayuri)", "kr_name": "찰나의 불꽃놀이(모미지・사유리)", "type": "stm", "pow": "4274", "tec": "3726", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "強烈スパイクD", "skill3": "内から湧き上がるスタミナ3", "sell": "2021/9/3", "resell": "2023/7/20", "break": "1", "special_fun": ""
  },
  {
    "id": "549", "girl": "nanami", "name": "秋麗のスクールウェア(ななみ)", "zhs_name": "秋季校服(七海)", "zht_name": "秋季校服(七海)", "en_name": "Autumn Schoolwear (Nanami)", "kr_name": "아름다운 가을 학생복(나나미)", "type": "pow", "pow": "4972", "tec": "3536", "stm": "4234", "apl": "200", "skill1": "強烈スパイクD", "skill2": "圧倒的な気迫E", "skill3": "秘められたパワー6", "sell": "2021/9/9", "resell": "2022/11/30", "break": "1", "special_fun": ""
  },
  {
    "id": "550", "girl": "tsukushi", "name": "秋麗のスクールウェア(つくし)", "zhs_name": "秋季校服(筑紫)", "zht_name": "秋季校服(筑紫)", "en_name": "Autumn Schoolwear (Tsukushi)", "kr_name": "아름다운 가을 학생복(츠쿠시)", "type": "pow", "pow": "4972", "tec": "3536", "stm": "4234", "apl": "200", "skill1": "強烈スパイクD", "skill2": "圧倒的な気迫E", "skill3": "秘められたパワー6", "sell": "2021/9/9", "resell": "2022/11/30", "break": "1", "special_fun": ""
  },
  {
    "id": "551", "girl": "luna", "name": "秋麗のスクールウェア(ルナ)", "zhs_name": "秋季校服(露娜)", "zht_name": "秋季校服(露娜)", "en_name": "Autumn Schoolwear (Luna)", "kr_name": "아름다운 가을 학생복(루나)", "type": "pow", "pow": "5032", "tec": "3616", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "秘められたパワー6", "skill3": "豪快なスパイク", "sell": "2021/9/9", "resell": "2022/11/30", "break": "1", "special_fun": ""
  },
  {
    "id": "552", "girl": "kanna", "name": "ブーケ・ダリア(カンナ)", "zhs_name": "花束・大丽花(神无)", "zht_name": "", "en_name": "Bouquet Dahlia (Kanna)", "kr_name": "부케 달리아(칸나)", "type": "pow", "pow": "5622", "tec": "3924", "stm": "4154", "apl": "200", "skill1": "強烈スパイクG", "skill2": "ダリアのパワー", "skill3": "豪快なスパイク", "sell": "2021/9/15", "resell": "2021/10/22 2022/9/15", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。"
  },
  {
    "id": "332_4", "girl": "helena", "name": "ルミネイトチューブ(エレナ)", "zhs_name": "荧光管(海莲娜)", "zht_name": "", "en_name": "Luminary Tube Dress (Helena)", "kr_name": "루미네이트 튜브(엘레나)", "type": "tec", "pow": "3526", "tec": "5102", "stm": "4014", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "閃きのテクニック6", "skill3": "可憐なフェイント", "sell": "2021/9/16", "resell": "2022/6/23", "break": "1", "special_fun": ""
  },
  {
    "id": "332_5", "girl": "ayane", "name": "ルミネイトチューブ(あやね)", "zhs_name": "荧光管(绫音)", "zht_name": "", "en_name": "Luminary Tube Dress (Ayane)", "kr_name": "루미네이트 튜브(아야네)", "type": "tec", "pow": "3586", "tec": "5072", "stm": "4084", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "驚異のスタミナA", "skill3": "閃きのテクニック3", "sell": "2021/9/16", "resell": "2022/6/23", "break": "1", "special_fun": ""
  },
  {
    "id": "553", "girl": "nanami", "name": "ステラ・アリエス(ななみ)", "zhs_name": "星辰‧白羊(七海)", "zht_name": "", "en_name": "Stellar Aries (Nanami)", "kr_name": "스텔라 아리에스(나나미)", "type": "pow", "pow": "5322", "tec": "3764", "stm": "4114", "apl": "200", "skill1": "強烈スパイクC", "skill2": "アリエス・パワー", "skill3": "豪快なスパイク", "sell": "2021/9/16", "resell": "2022/4/16 2022/9/8 2023/4/16", "break": "1", "special_fun": "生日拆开卖，作田发大财。愿者上钩。"
  },
  {
    "id": "554", "girl": "lobelia", "name": "ステラ・カンケル(ロベリア)", "zhs_name": "星辰・巨蟹(萝贝莉娅)", "zht_name": "", "en_name": "Stellar Cancer (Lobelia)", "kr_name": "스텔라 캔서(로벨리아)", "type": "stm", "pow": "3766", "tec": "4254", "stm": "5322", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "カンケル・スタミナ", "skill3": "可憐なフェイント", "sell": "2021/9/16", "resell": "2022/6/25 2022/9/8 2023/6/25", "break": "1", "special_fun": "生日拆开卖，作田发大财。愿者上钩。"
  },
  {
    "id": "555", "girl": "momiji", "name": "ブーケ・ダリア(紅葉)", "zhs_name": "花束・大丽花(红叶)", "zht_name": "", "en_name": "Bouquet Dahlia (Momiji)", "kr_name": "부케 달리아(모미지)", "type": "stm", "pow": "3704", "tec": "4774", "stm": "5622", "apl": "200", "skill1": "裏の裏を突くフェイントG", "skill2": "ダリアのスタミナ", "skill3": "可憐なフェイント", "sell": "2021/9/20", "resell": "2021/10/22 2022/9/20", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。"
  },
  {
    "id": "556_1", "girl": "hitomi", "name": "スパークリングブルー(ヒトミ)", "zhs_name": "闪亮靛蓝(瞳)", "zht_name": "閃亮靛藍(瞳)", "en_name": "Sparkling Blue (Hitomi)", "kr_name": "스파클링 블루(히토미)", "type": "stm", "pow": "4284", "tec": "3586", "stm": "5172", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "内から湧き上がるスタミナ3", "skill3": "豪快なスパイク", "sell": "2021/9/24", "resell": "2023/1/18", "break": "1", "special_fun": ""
  },
  {
    "id": "556_2", "girl": "fiona", "name": "スパークリングブルー(フィオナ)", "zhs_name": "闪亮靛蓝(菲欧娜)", "zht_name": "閃亮靛藍(菲歐娜)", "en_name": "Sparkling Blue (Fiona)", "kr_name": "스파클링 블루(피오나)", "type": "stm", "pow": "4284", "tec": "3586", "stm": "5172", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "内から湧き上がるスタミナ3", "skill3": "豪快なスパイク", "sell": "2021/9/24", "resell": "2023/1/18", "break": "1", "special_fun": ""
  },
  {
    "id": "556_3", "girl": "nagisa", "name": "スパークリングブルー(なぎさ)", "zhs_name": "闪亮靛蓝(凪咲)", "zht_name": "閃亮靛藍(凪咲)", "en_name": "Sparkling Blue (Nagisa)", "kr_name": "스파클링 블루(나기사)", "type": "stm", "pow": "4284", "tec": "3586", "stm": "5172", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "内から湧き上がるスタミナ3", "skill3": "豪快なスパイク", "sell": "2021/9/24", "resell": "2023/1/18", "break": "1", "special_fun": ""
  },
  {
    "id": "556_4", "girl": "monica", "name": "スパークリングブルー(モニカ)", "zhs_name": "闪亮靛蓝(莫妮卡)", "zht_name": "閃亮靛藍(莫妮卡)", "en_name": "Sparkling Blue (Monica)", "kr_name": "스파클링 블루(모니카)", "type": "stm", "pow": "4284", "tec": "3586", "stm": "5172", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "内から湧き上がるスタミナ3", "skill3": "豪快なスパイク", "sell": "2021/9/24", "resell": "2023/1/18", "break": "1", "special_fun": ""
  },
  {
    "id": "556_5", "girl": "nanami", "name": "スパークリングブルー(ななみ)", "zhs_name": "闪亮靛蓝(七海)", "zht_name": "閃亮靛藍(七海)", "en_name": "Sparkling Blue (Nanami)", "kr_name": "스파클링 블루(나나미)", "type": "stm", "pow": "4284", "tec": "3586", "stm": "5172", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "内から湧き上がるスタミナ3", "skill3": "豪快なスパイク", "sell": "2021/9/24", "resell": "2023/1/18", "break": "1", "special_fun": ""
  },
  {
    "id": "557", "girl": "nanami", "name": "純白のスリットワンピ(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2021/10/1", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "558_1", "girl": "kasumi", "name": "月影(かすみ)", "zhs_name": "月下魅影(霞)", "zht_name": "月下魅影(霞)", "en_name": "Moonlight Shadow (Kasumi)", "kr_name": "월영(카스미)", "type": "tec", "pow": "3516", "tec": "5022", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "月影のテクニック", "skill3": "熱烈なエール", "sell": "2021/10/3", "resell": "2022/10/27", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。穿越过去给steam国际服当所谓的独占原创，原来还可以塞回来当冷饭用啊。"
  },
  {
    "id": "558_2", "girl": "marie", "name": "月影(マリー)", "zhs_name": "月下魅影(玛莉)", "zht_name": "月下魅影(瑪莉)", "en_name": "Moonlight Shadow (Marie)", "kr_name": "월영(마리)", "type": "tec", "pow": "3516", "tec": "5022", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "月影のテクニック", "skill3": "熱烈なエール", "sell": "2021/10/3", "resell": "2022/10/27", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。穿越过去给steam国际服当所谓的独占原创，原来还可以塞回来当冷饭用啊。"
  },
  {
    "id": "558_3", "girl": "ayane", "name": "月影(あやね)", "zhs_name": "月下魅影(绫音)", "zht_name": "月下魅影(綾音)", "en_name": "Moonlight Shadow (Ayane)", "kr_name": "월영(아야네)", "type": "tec", "pow": "3516", "tec": "5022", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "月影のテクニック", "skill3": "熱烈なエール", "sell": "2021/10/3", "resell": "2022/10/27", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。穿越过去给steam国际服当所谓的独占原创，原来还可以塞回来当冷饭用啊。"
  },
  {
    "id": "558_4", "girl": "nyotengu", "name": "月影(女天狗)", "zhs_name": "月下魅影(女天狗)", "zht_name": "月下魅影(女天狗)", "en_name": "Moonlight Shadow (Nyotengu)", "kr_name": "월영(뇨텐구)", "type": "tec", "pow": "3516", "tec": "5022", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "月影のテクニック", "skill3": "熱烈なエール", "sell": "2021/10/3", "resell": "2022/10/27", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。穿越过去给steam国际服当所谓的独占原创，原来还可以塞回来当冷饭用啊。"
  },
  {
    "id": "558_5", "girl": "kokoro", "name": "月影(こころ)", "zhs_name": "月下魅影(心)", "zht_name": "月下魅影(心)", "en_name": "Moonlight Shadow (Kokoro)", "kr_name": "월영(코코로)", "type": "tec", "pow": "3516", "tec": "5022", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "月影のテクニック", "skill3": "熱烈なエール", "sell": "2021/10/3", "resell": "2022/10/27", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。穿越过去给steam国际服当所谓的独占原创，原来还可以塞回来当冷饭用啊。"
  },
  {
    "id": "558_6", "girl": "momiji", "name": "月影(紅葉)", "zhs_name": "月下魅影(红叶)", "zht_name": "月下魅影(紅葉)", "en_name": "Moonlight Shadow (Momiji)", "kr_name": "월영(모미지)", "type": "tec", "pow": "3516", "tec": "5022", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "月影のテクニック", "skill3": "熱烈なエール", "sell": "2021/10/3", "resell": "2022/10/27", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。穿越过去给steam国际服当所谓的独占原创，原来还可以塞回来当冷饭用啊。"
  },
  {
    "id": "558_7", "girl": "misaki", "name": "月影(みさき)", "zhs_name": "月下魅影(海咲)", "zht_name": "月下魅影(海咲)", "en_name": "Moonlight Shadow (Misaki)", "kr_name": "월영(미사키)", "type": "tec", "pow": "3516", "tec": "5022", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "月影のテクニック", "skill3": "熱烈なエール", "sell": "2021/10/3", "resell": "2022/10/27", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。穿越过去给steam国际服当所谓的独占原创，原来还可以塞回来当冷饭用啊。"
  },
  {
    "id": "558_8", "girl": "luna", "name": "月影(ルナ)", "zhs_name": "月下魅影(露娜)", "zht_name": "月下魅影(露娜)", "en_name": "Moonlight Shadow (Luna)", "kr_name": "월영(루나)", "type": "tec", "pow": "3516", "tec": "5022", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "月影のテクニック", "skill3": "熱烈なエール", "sell": "2021/10/3", "resell": "2022/10/27", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。穿越过去给steam国际服当所谓的独占原创，原来还可以塞回来当冷饭用啊。"
  },
  {
    "id": "558_9", "girl": "tamaki", "name": "月影(たまき)", "zhs_name": "月下魅影(环)", "zht_name": "月下魅影(環)", "en_name": "Moonlight Shadow (Tamaki)", "kr_name": "월영(타마키)", "type": "tec", "pow": "3516", "tec": "5022", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "月影のテクニック", "skill3": "熱烈なエール", "sell": "2021/10/3", "resell": "2022/10/27", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。穿越过去给steam国际服当所谓的独占原创，原来还可以塞回来当冷饭用啊。"
  },
  {
    "id": "558_10", "girl": "leifang", "name": "月影(レイファン)", "zhs_name": "月下魅影(丽凤)", "zht_name": "月下魅影(麗鳳)", "en_name": "Moonlight Shadow (Leifang)", "kr_name": "월영(레이팡)", "type": "tec", "pow": "3516", "tec": "5022", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "月影のテクニック", "skill3": "熱烈なエール", "sell": "2021/10/3", "resell": "2022/10/27", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。穿越过去给steam国际服当所谓的独占原创，原来还可以塞回来当冷饭用啊。"
  },
  {
    "id": "558_11", "girl": "sayuri", "name": "月影(さゆり)", "zhs_name": "月下魅影(小百合)", "zht_name": "月下魅影(小百合)", "en_name": "Moonlight Shadow (Sayuri)", "kr_name": "월영(사유리)", "type": "tec", "pow": "3516", "tec": "5022", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "月影のテクニック", "skill3": "熱烈なエール", "sell": "2021/10/3", "resell": "2022/10/27", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。穿越过去给steam国际服当所谓的独占原创，原来还可以塞回来当冷饭用啊。"
  },
  {
    "id": "558_12", "girl": "nanami", "name": "月影(ななみ)", "zhs_name": "月下魅影(七海)", "zht_name": "月下魅影(七海)", "en_name": "Moonlight Shadow (Nanami)", "kr_name": "월영(나나미)", "type": "tec", "pow": "3516", "tec": "5022", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "月影のテクニック", "skill3": "熱烈なエール", "sell": "2021/10/3", "resell": "2022/10/27", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。穿越过去给steam国际服当所谓的独占原创，原来还可以塞回来当冷饭用啊。"
  },
  {
    "id": "559", "girl": "patty", "name": "エンシェントオアシス(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5002", "tec": "3596", "stm": "4044", "apl": "200", "skill1": "不動のレシーブC", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2021/10/8", "resell": "2023/5/4", "break": "1", "special_fun": ""
  },
  {
    "id": "560", "girl": "nyotengu", "name": "エンシェントオアシス(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "4932", "tec": "3626", "stm": "4184", "apl": "200", "skill1": "強烈スパイクF", "skill2": "驚異のスタミナD", "skill3": "秘められたパワー3", "sell": "2021/10/8", "resell": "2023/5/4", "break": "1", "special_fun": ""
  },
  {
    "id": "561", "girl": "fiona", "name": "エンシェントオアシス(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "4932", "tec": "3626", "stm": "4184", "apl": "200", "skill1": "強烈スパイクF", "skill2": "驚異のスタミナD", "skill3": "秘められたパワー3", "sell": "2021/10/8", "resell": "2023/5/4", "break": "1", "special_fun": ""
  },
  {
    "id": "562", "girl": "kanna", "name": "おつまみピンチョス(カンナ)", "zhs_name": "拽拽Pinchos(神无)", "zht_name": "拽拽Pinchos(神無)", "en_name": "Appetizer Pinchos (Kanna)", "kr_name": "애피타이저 핀초(칸나)", "type": "tec", "pow": "3496", "tec": "5102", "stm": "4044", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "閃きのテクニック5", "skill3": "可憐なフェイント", "sell": "2021/10/14", "resell": "", "break": "1", "special_fun": "允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "563", "girl": "kasumi", "name": "おつまみピンチョス(かすみ)", "zhs_name": "拽拽Pinchos(霞)", "zht_name": "拽拽Pinchos(霞)", "en_name": "Appetizer Pinchos (Kasumi)", "kr_name": "애피타이저 핀초(카스미)", "type": "tec", "pow": "3566", "tec": "5152", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "驚異のスタミナC", "skill3": "閃きのテクニック6", "sell": "2021/10/14", "resell": "", "break": "1", "special_fun": "允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "564", "girl": "tsukushi", "name": "おつまみピンチョス(つくし)", "zhs_name": "拽拽Pinchos(筑紫)", "zht_name": "拽拽Pinchos(筑紫)", "en_name": "Appetizer Pinchos (Tsukushi)", "kr_name": "애피타이저 핀초(츠쿠시)", "type": "tec", "pow": "3566", "tec": "5152", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "驚異のスタミナC", "skill3": "閃きのテクニック6", "sell": "2021/10/14", "resell": "", "break": "1", "special_fun": "允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "565", "girl": "luna", "name": "ブーケ・コスモス(ルナ)", "zhs_name": "花束・秋英属(露娜)", "zht_name": "", "en_name": "Bouquet Cosmos (Luna)", "kr_name": "부케 코스모스(루나)", "type": "stm", "pow": "4794", "tec": "3684", "stm": "5622", "apl": "200", "skill1": "強烈スパイクG", "skill2": "コスモスのスタミナ", "skill3": "豪快なスパイク", "sell": "2021/10/15", "resell": "2021/10/22 2022/10/15", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。"
  },
  {
    "id": "566", "girl": "momiji", "name": "プラチナ・ひので(紅葉)", "zhs_name": "白金日出(红叶)", "zht_name": "", "en_name": "Platinum Sunrise (Momiji)", "kr_name": "플래티넘 해돋이(모미지)", "type": "stm", "pow": "3926", "tec": "4224", "stm": "4892", "apl": "200", "skill1": "高度な心理戦D", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2021/10/22", "resell": "2022/11/10", "break": "1", "special_fun": "KT你这一下白金 一下プラチナ 是读过书的一下上班 一下不上班吗"
  },
  {
    "id": "567", "girl": "honoka", "name": "プラチナ・デルフィニウム(ほのか)", "zhs_name": "白金翠雀(穗香)", "zht_name": "白金翠雀(穗香)", "en_name": "Platinum Delphinium (Honoka)", "kr_name": "플래티넘 델피니움(호노카)", "type": "stm", "pow": "3476", "tec": "4374", "stm": "5192", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "内から湧き上がるスタミナ4", "skill3": "可憐なフェイント", "sell": "2021/10/22", "resell": "2022/11/10", "break": "1", "special_fun": "KT你这一下白金 一下プラチナ 是读过书的一下上班 一下不上班吗"
  },
  {
    "id": "568", "girl": "tsukushi", "name": "ブーケ・コスモス(つくし)", "zhs_name": "花束・秋英属(筑紫)", "zht_name": "", "en_name": "Bouquet Cosmos (Tsukushi)", "kr_name": "부케 코스모스(츠쿠시)", "type": "tec", "pow": "4072", "tec": "5364", "stm": "4264", "apl": "200", "skill1": "裏の裏を突くフェイントG", "skill2": "コスモスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/10/24", "resell": "2022/10/24", "break": "1", "special_fun": "第三套花语主题生日，附带花瓣飘落效果。哎。生日排最后拿到手的时候别人已经下一年了。"
  },
  {
    "id": "178_19", "girl": "patty", "name": "ふわもこフォーム(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2021/10/29", "resell": "2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_20", "girl": "tsukushi", "name": "ふわもこフォーム(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2021/10/29", "resell": "2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "178_21", "girl": "lobelia", "name": "ふわもこフォーム(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5112", "tec": "3634", "stm": "4154", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "ふわもこのパワー", "skill3": "豪快なスパイク", "sell": "2021/10/29", "resell": "2022/9/24", "break": "1", "special_fun": "使用喷水道具可以减少身上覆盖的泡沫。使用普通天狗扇可以看见泡沫飞舞"
  },
  {
    "id": "569", "girl": "leifang", "name": "恋色いろは(レイファン)", "zhs_name": "恋色伊吕波(丽凤)", "zht_name": "戀色伊呂波(麗鳳)", "en_name": "Maple Romance (Leifang)", "kr_name": "사랑빛 이로하(레이팡)", "type": "stm", "pow": "4414", "tec": "3576", "stm": "5052", "apl": "200", "skill1": "不動のレシーブE", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2021/11/2", "resell": "2022/9/29", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现落叶，喷水会使叶子颜色变化"
  },
  {
    "id": "570", "girl": "misaki", "name": "恋色いろは(みさき)", "zhs_name": "恋色伊吕波(海咲)", "zht_name": "戀色伊呂波(海咲)", "en_name": "Maple Romance (Misaki)", "kr_name": "사랑빛 이로하(미사키)", "type": "stm", "pow": "4274", "tec": "3666", "stm": "5202", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "強烈スパイクB", "skill3": "内から湧き上がるスタミナ6", "sell": "2021/11/2", "resell": "2022/9/29", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现落叶，喷水会使叶子颜色变化"
  },
  {
    "id": "571", "girl": "koharu", "name": "もてなし小町(こはる)", "zhs_name": "好客美女(小春)", "zht_name": "接待美人(小春)", "en_name": "Hospitable Beauty (Koharu)", "kr_name": "환대하는 여인(코하루)", "type": "stm", "pow": "4384", "tec": "3656", "stm": "5102", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫F", "skill3": "内から湧き上がるスタミナ3", "sell": "2021/11/2", "resell": "", "break": "1", "special_fun": "果奶的眼睛+玛丽的嘴和脸。这么做新角色的吗，我上我也行。"
  },
  {
    "id": "572", "girl": "hitomi", "name": "はいからブルーマー(ヒトミ)", "zhs_name": "时髦体操裤(瞳)", "zht_name": "時髦體操褲(瞳)", "en_name": "Stylish Bloomers (Hitomi)", "kr_name": "하이 컬러 블루머(히토미)", "type": "pow", "pow": "5072", "tec": "3476", "stm": "4094", "apl": "200", "skill1": "強烈スパイクD", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2021/11/9", "resell": "2022/10/13", "break": "1", "special_fun": ""
  },
  {
    "id": "573", "girl": "nagisa", "name": "はいからブルーマー(なぎさ)", "zhs_name": "时髦体操裤(凪咲)", "zht_name": "時髦體操褲(凪咲)", "en_name": "Stylish Bloomers (Nagisa)", "kr_name": "하이 컬러 블루머(나기사)", "type": "pow", "pow": "5022", "tec": "3546", "stm": "4174", "apl": "200", "skill1": "強烈スパイクB", "skill2": "不動のレシーブE", "skill3": "秘められたパワー3", "sell": "2021/11/9", "resell": "2022/10/13", "break": "1", "special_fun": ""
  },
  {
    "id": "574_1", "girl": "kasumi", "name": "花鳥風月(かすみ)", "zhs_name": "花鸟风月(霞)", "zht_name": "花鳥風月(霞)", "en_name": "Beauty of Nature (Kasumi)", "kr_name": "화조풍월(카스미)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_2", "girl": "honoka", "name": "花鳥風月(ほのか)", "zhs_name": "花鸟风月(穗香)", "zht_name": "花鳥風月(穗香)", "en_name": "Beauty of Nature (Honoka)", "kr_name": "화조풍월(호노카)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_3", "girl": "marie", "name": "花鳥風月(マリー)", "zhs_name": "花鸟风月(玛莉)", "zht_name": "花鳥風月(瑪莉)", "en_name": "Beauty of Nature (Marie)", "kr_name": "화조풍월(마리)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_4", "girl": "ayane", "name": "花鳥風月(あやね)", "zhs_name": "花鸟风月(绫音)", "zht_name": "花鳥風月(綾音)", "en_name": "Beauty of Nature (Ayane)", "kr_name": "화조풍월(아야네)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_5", "girl": "nyotengu", "name": "花鳥風月(女天狗)", "zhs_name": "花鸟风月(女天狗)", "zht_name": "花鳥風月(女天狗)", "en_name": "Beauty of Nature (Nyotengu)", "kr_name": "화조풍월(뇨텐구)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_6", "girl": "kokoro", "name": "花鳥風月(こころ)", "zhs_name": "花鸟风月(心)", "zht_name": "花鳥風月(心)", "en_name": "Beauty of Nature (Kokoro)", "kr_name": "화조풍월(코코로)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_7", "girl": "hitomi", "name": "花鳥風月(ヒトミ)", "zhs_name": "花鸟风月(瞳)", "zht_name": "花鳥風月(瞳)", "en_name": "Beauty of Nature (Hitomi)", "kr_name": "화조풍월(히토미)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_8", "girl": "momiji", "name": "花鳥風月(紅葉)", "zhs_name": "花鸟风月(红叶)", "zht_name": "花鳥風月(紅葉)", "en_name": "Beauty of Nature (Momiji)", "kr_name": "화조풍월(모미지)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_9", "girl": "helena", "name": "花鳥風月(エレナ)", "zhs_name": "花鸟风月(海莲娜)", "zht_name": "花鳥風月(海蓮娜)", "en_name": "Beauty of Nature (Helena)", "kr_name": "화조풍월(엘레나)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_10", "girl": "misaki", "name": "花鳥風月(みさき)", "zhs_name": "花鸟风月(海咲)", "zht_name": "花鳥風月(海咲)", "en_name": "Beauty of Nature (Misaki)", "kr_name": "화조풍월(미사키)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_11", "girl": "luna", "name": "花鳥風月(ルナ)", "zhs_name": "花鸟风月(露娜)", "zht_name": "花鳥風月(露娜)", "en_name": "Beauty of Nature (Luna)", "kr_name": "화조풍월(루나)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_12", "girl": "tamaki", "name": "花鳥風月(たまき)", "zhs_name": "花鸟风月(环)", "zht_name": "花鳥風月(環)", "en_name": "Beauty of Nature (Tamaki)", "kr_name": "화조풍월(타마키)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_13", "girl": "leifang", "name": "花鳥風月(レイファン)", "zhs_name": "花鸟风月(丽凤)", "zht_name": "花鳥風月(麗鳳)", "en_name": "Beauty of Nature (Leifang)", "kr_name": "화조풍월(레이팡)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_14", "girl": "fiona", "name": "花鳥風月(フィオナ)", "zhs_name": "花鸟风月(菲欧娜)", "zht_name": "花鳥風月(菲歐娜)", "en_name": "Beauty of Nature (Fiona)", "kr_name": "화조풍월(피오나)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_15", "girl": "nagisa", "name": "花鳥風月(なぎさ)", "zhs_name": "花鸟风月(凪咲)", "zht_name": "花鳥風月(凪咲)", "en_name": "Beauty of Nature (Nagisa)", "kr_name": "화조풍월(나기사)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_16", "girl": "kanna", "name": "花鳥風月(カンナ)", "zhs_name": "花鸟风月(神无)", "zht_name": "花鳥風月(神無)", "en_name": "Beauty of Nature (Kanna)", "kr_name": "화조풍월(칸나)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_17", "girl": "monica", "name": "花鳥風月(モニカ)", "zhs_name": "花鸟风月(莫妮卡)", "zht_name": "花鳥風月(莫妮卡)", "en_name": "Beauty of Nature (Monica)", "kr_name": "화조풍월(모니카)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_18", "girl": "sayuri", "name": "花鳥風月(さゆり)", "zhs_name": "花鸟风月(小百合)", "zht_name": "花鳥風月(小百合)", "en_name": "Beauty of Nature (Sayuri)", "kr_name": "화조풍월(사유리)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_19", "girl": "patty", "name": "花鳥風月(パティ)", "zhs_name": "花鸟风月(派蒂)", "zht_name": "花鳥風月(派蒂)", "en_name": "Beauty of Nature (Patty)", "kr_name": "화조풍월(패티)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_20", "girl": "tsukushi", "name": "花鳥風月(つくし)", "zhs_name": "花鸟风月(筑紫)", "zht_name": "花鳥風月(筑紫)", "en_name": "Beauty of Nature (Tsukushi)", "kr_name": "화조풍월(츠쿠시)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_21", "girl": "lobelia", "name": "花鳥風月(ロベリア)", "zhs_name": "花鸟风月(萝贝莉娅)", "zht_name": "花鳥風月(蘿貝莉婭)", "en_name": "Beauty of Nature (Lobelia)", "kr_name": "화조풍월(로벨리아)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_22", "girl": "nanami", "name": "花鳥風月(ななみ)", "zhs_name": "花鸟风月(七海)", "zht_name": "花鳥風月(七海)", "en_name": "Beauty of Nature (Nanami)", "kr_name": "화조풍월(나나미)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2021/11/17", "resell": "2022/11/22", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "575", "girl": "nyotengu", "name": "ドルチェ・メーレ(女天狗)", "zhs_name": "甜美・苹果(女天狗)", "zht_name": "甜美‧蘋果(女天狗)", "en_name": "Dolce Mela (Nyotengu)", "kr_name": "돌체 멜레(뇨텐구)", "type": "pow", "pow": "5622", "tec": "3914", "stm": "4164", "apl": "200", "skill1": "W・疲れ知らずの猛攻G", "skill2": "リンゴのパワー", "skill3": "豪快なスパイク", "sell": "2021/11/19", "resell": "2022/11/4 2022/11/19", "break": "1", "special_fun": "第四年生日服，拥有双效果技能。"
  },
  {
    "id": "576", "girl": "patty", "name": "トロピカルチューン(パティ)", "zhs_name": "热带曲调(派蒂)", "zht_name": "熱帶旋律(派蒂)", "en_name": "Tropical Tune (Patty)", "kr_name": "트로피컬 튠(패티)", "type": "stm", "pow": "4244", "tec": "3606", "stm": "5192", "apl": "200", "skill1": "強烈スパイクF", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2021/11/25", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "577", "girl": "misaki", "name": "トロピカルチューン(みさき)", "zhs_name": "热带曲调(海咲)", "zht_name": "熱帶旋律(海咲)", "en_name": "Tropical Tune (Misaki)", "kr_name": "트로피컬 튠(미사키)", "type": "stm", "pow": "4314", "tec": "3686", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "強烈なプレッシャーD", "skill3": "内から湧き上がるスタミナ4", "sell": "2021/11/25", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "578", "girl": "monica", "name": "トロピカルチューン(モニカ)", "zhs_name": "热带曲调(莫妮卡)", "zht_name": "熱帶旋律(莫妮卡)", "en_name": "Tropical Tune (Monica)", "kr_name": "트로피컬 튠(모니카)", "type": "stm", "pow": "4314", "tec": "3686", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "強烈なプレッシャーD", "skill3": "内から湧き上がるスタミナ4", "sell": "2021/11/25", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "579", "girl": "kokoro", "name": "ドルチェ・オランジュ(こころ)", "zhs_name": "甜美・桔子(心)", "zht_name": "甜美‧柑橘(心)", "en_name": "Dolce Orange (Kokoro)", "kr_name": "돌체 오란쥬(코코로)", "type": "pow", "pow": "5622", "tec": "3864", "stm": "4214", "apl": "200", "skill1": "W・疲れ知らずの猛攻G", "skill2": "ミカンのパワー", "skill3": "豪快なスパイク", "sell": "2021/12/1", "resell": "2022/11/4", "break": "1", "special_fun": "第四年生日服，拥有双效果技能。"
  },
  {
    "id": "580", "girl": "koharu", "name": "恋夢ごこち(こはる)", "zhs_name": "神魂颠倒(小春)", "zht_name": "戀夢陶醉(小春)", "en_name": "Dreamy State of Mind (Koharu)", "kr_name": "황홀한 사랑(코하루)", "type": "pow", "pow": "4952", "tec": "3386", "stm": "4304", "apl": "200", "skill1": "圧倒的な気迫B", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2021/12/2", "resell": "", "break": "1", "special_fun": "可以获得特殊CG，满觉醒后CG有变化(换衣服中可以睁眼看见泳装滑落的效果)"
  },
  {
    "id": "581", "girl": "fiona", "name": "ブロッサム・フェザー(フィオナ)", "zhs_name": "花簇羽翼(菲欧娜)", "zht_name": "花簇羽翼(菲歐娜)", "en_name": "Blossom Feather (Fiona)", "kr_name": "블로섬 페더(피오나)", "type": "pow", "pow": "5132", "tec": "3436", "stm": "4074", "apl": "200", "skill1": "強烈なプレッシャーE", "skill2": "秘められたパワー4", "skill3": "熱烈なエール", "sell": "2021/12/2", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "582", "girl": "ayane", "name": "クリムゾン・フェザー(あやね)", "zhs_name": "深红羽翼(绫音)", "zht_name": "深紅羽翼(綾音)", "en_name": "Crimson Feather (Ayane)", "kr_name": "크림슨 페더(아야네)", "type": "pow", "pow": "5052", "tec": "3596", "stm": "4094", "apl": "200", "skill1": "強烈スパイクC", "skill2": "圧倒的な気迫B", "skill3": "秘められたパワー3", "sell": "2021/12/2", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "583", "girl": "nyotengu", "name": "うすかわたけのこ(女天狗)", "zhs_name": "薄皮竹笋(女天狗)", "zht_name": "薄皮竹筍(女天狗)", "en_name": "Thin Towel Wrap (Nyotengu)", "kr_name": "박막 죽순(뇨텐구)", "type": "stm", "pow": "4284", "tec": "3526", "stm": "5232", "apl": "200", "skill1": "圧倒的な気迫C", "skill2": "内から湧き上がるスタミナ5", "skill3": "豪快なスパイク", "sell": "2021/12/9", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "584", "girl": "hitomi", "name": "うすかわたけのこ(ヒトミ)", "zhs_name": "薄皮竹笋(瞳)", "zht_name": "薄皮竹筍(瞳)", "en_name": "Thin Towel Wrap (Hitomi)", "kr_name": "박막 죽순(히토미)", "type": "stm", "pow": "4304", "tec": "3726", "stm": "5112", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "強烈スパイクD", "skill3": "内から湧き上がるスタミナ4", "sell": "2021/12/9", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "585", "girl": "nanami", "name": "うすかわたけのこ(ななみ)", "zhs_name": "薄皮竹笋(七海)", "zht_name": "薄皮竹筍(七海)", "en_name": "Thin Towel Wrap (Nanami)", "kr_name": "박막 죽순(나나미)", "type": "stm", "pow": "4304", "tec": "3726", "stm": "5112", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "強烈スパイクD", "skill3": "内から湧き上がるスタミナ4", "sell": "2021/12/9", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "586_1", "girl": "kasumi", "name": "ルミナス・ベル(かすみ)", "zhs_name": "发光铃铛(霞)", "zht_name": "光輝之鐘(霞)", "en_name": "Luminous Bell (Kasumi)", "kr_name": "루미너스 벨(카스미)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_2", "girl": "honoka", "name": "ルミナス・ベル(ほのか)", "zhs_name": "发光铃铛(穗香)", "zht_name": "光輝之鐘(穗香)", "en_name": "Luminous Bell (Honoka)", "kr_name": "루미너스 벨(호노카)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_3", "girl": "marie", "name": "ルミナス・ベル(マリー)", "zhs_name": "发光铃铛(玛莉)", "zht_name": "光輝之鐘(瑪莉)", "en_name": "Luminous Bell (Marie)", "kr_name": "루미너스 벨(마리)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_4", "girl": "ayane", "name": "ルミナス・ベル(あやね)", "zhs_name": "发光铃铛(绫音)", "zht_name": "光輝之鐘(綾音)", "en_name": "Luminous Bell (Ayane)", "kr_name": "루미너스 벨(아야네)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_5", "girl": "nyotengu", "name": "ルミナス・ベル(女天狗)", "zhs_name": "发光铃铛(女天狗)", "zht_name": "光輝之鐘(女天狗)", "en_name": "Luminous Bell (Nyotengu)", "kr_name": "루미너스 벨(뇨텐구)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_6", "girl": "kokoro", "name": "ルミナス・ベル(こころ)", "zhs_name": "发光铃铛(心)", "zht_name": "光輝之鐘(心)", "en_name": "Luminous Bell (Kokoro)", "kr_name": "루미너스 벨(코코로)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_7", "girl": "hitomi", "name": "ルミナス・ベル(ヒトミ)", "zhs_name": "发光铃铛(瞳)", "zht_name": "光輝之鐘(瞳)", "en_name": "Luminous Bell (Hitomi)", "kr_name": "루미너스 벨(히토미)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_8", "girl": "momiji", "name": "ルミナス・ベル(紅葉)", "zhs_name": "发光铃铛(红叶)", "zht_name": "光輝之鐘(紅葉)", "en_name": "Luminous Bell (Momiji)", "kr_name": "루미너스 벨(모미지)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_9", "girl": "helena", "name": "ルミナス・ベル(エレナ)", "zhs_name": "发光铃铛(海莲娜)", "zht_name": "光輝之鐘(海蓮娜)", "en_name": "Luminous Bell (Helena)", "kr_name": "루미너스 벨(엘레나)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_10", "girl": "misaki", "name": "ルミナス・ベル(みさき)", "zhs_name": "发光铃铛(海咲)", "zht_name": "光輝之鐘(海咲)", "en_name": "Luminous Bell (Misaki)", "kr_name": "루미너스 벨(미사키)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_11", "girl": "luna", "name": "ルミナス・ベル(ルナ)", "zhs_name": "发光铃铛(露娜)", "zht_name": "光輝之鐘(露娜)", "en_name": "Luminous Bell (Luna)", "kr_name": "루미너스 벨(루나)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_12", "girl": "tamaki", "name": "ルミナス・ベル(たまき)", "zhs_name": "发光铃铛(环)", "zht_name": "光輝之鐘(環)", "en_name": "Luminous Bell (Tamaki)", "kr_name": "루미너스 벨(타마키)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_13", "girl": "leifang", "name": "ルミナス・ベル(レイファン)", "zhs_name": "发光铃铛(丽凤)", "zht_name": "光輝之鐘(麗鳳)", "en_name": "Luminous Bell (Leifang)", "kr_name": "루미너스 벨(레이팡)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_14", "girl": "fiona", "name": "ルミナス・ベル(フィオナ)", "zhs_name": "发光铃铛(菲欧娜)", "zht_name": "光輝之鐘(菲歐娜)", "en_name": "Luminous Bell (Fiona)", "kr_name": "루미너스 벨(피오나)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_15", "girl": "nagisa", "name": "ルミナス・ベル(なぎさ)", "zhs_name": "发光铃铛(凪咲)", "zht_name": "光輝之鐘(凪咲)", "en_name": "Luminous Bell (Nagisa)", "kr_name": "루미너스 벨(나기사)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_16", "girl": "kanna", "name": "ルミナス・ベル(カンナ)", "zhs_name": "发光铃铛(神无)", "zht_name": "光輝之鐘(神無)", "en_name": "Luminous Bell (Kanna)", "kr_name": "루미너스 벨(칸나)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_17", "girl": "monica", "name": "ルミナス・ベル(モニカ)", "zhs_name": "发光铃铛(莫妮卡)", "zht_name": "光輝之鐘(莫妮卡)", "en_name": "Luminous Bell (Monica)", "kr_name": "루미너스 벨(모니카)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_18", "girl": "sayuri", "name": "ルミナス・ベル(さゆり)", "zhs_name": "发光铃铛(小百合)", "zht_name": "光輝之鐘(小百合)", "en_name": "Luminous Bell (Sayuri)", "kr_name": "루미너스 벨(사유리)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_19", "girl": "patty", "name": "ルミナス・ベル(パティ)", "zhs_name": "发光铃铛(派蒂)", "zht_name": "光輝之鐘(派蒂)", "en_name": "Luminous Bell (Patty)", "kr_name": "루미너스 벨(패티)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_20", "girl": "tsukushi", "name": "ルミナス・ベル(つくし)", "zhs_name": "发光铃铛(筑紫)", "zht_name": "光輝之鐘(筑紫)", "en_name": "Luminous Bell (Tsukushi)", "kr_name": "루미너스 벨(츠쿠시)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_21", "girl": "lobelia", "name": "ルミナス・ベル(ロベリア)", "zhs_name": "发光铃铛(萝贝莉娅)", "zht_name": "光輝之鐘(蘿貝莉婭)", "en_name": "Luminous Bell (Lobelia)", "kr_name": "루미너스 벨(로벨리아)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "586_22", "girl": "nanami", "name": "ルミナス・ベル(ななみ)", "zhs_name": "发光铃铛(七海)", "zht_name": "光輝之鐘(七海)", "en_name": "Luminous Bell (Nanami)", "kr_name": "루미너스 벨(나나미)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2021/12/16", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "587", "girl": "koharu", "name": "ドルチェ・オランジュ(こはる)", "zhs_name": "甜美·桔子(小春)", "zht_name": "甜美‧柑橘(小春)", "en_name": "Dolce Orange (Koharu)", "kr_name": "돌체 오란쥬(코하루)", "type": "pow", "pow": "5622", "tec": "3884", "stm": "4194", "apl": "200", "skill1": "W・疲れ知らずの猛攻G", "skill2": "ミカンのパワー", "skill3": "豪快なスパイク", "sell": "2021/12/22", "resell": "2022/11/4 2022/12/1 2022/12/22", "break": "1", "special_fun": "第四年生日服，拥有双效果技能。"
  },
  {
    "id": "455_20", "girl": "tsukushi", "name": "ノエル・シャルマン(つくし)", "zhs_name": "圣诞‧魅惑(筑紫)", "zht_name": "聖誕‧魅惑(筑紫)", "en_name": "Noel Charmant (Tsukushi)", "kr_name": "노엘 샤르망(츠쿠시)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2021/12/23", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "455_21", "girl": "lobelia", "name": "ノエル・シャルマン(ロベリア)", "zhs_name": "圣诞‧魅惑(萝贝莉娅)", "zht_name": "聖誕‧魅惑(蘿貝莉婭)", "en_name": "Noel Charmant (Lobelia)", "kr_name": "노엘 샤르망(로벨리아)", "type": "pow", "pow": "4782", "tec": "3616", "stm": "4244", "apl": "200", "skill1": "圧倒的な気迫E", "skill2": "シャルマンパワー", "skill3": "豪快なスパイク", "sell": "2021/12/23", "resell": "2022/12/21", "break": "1", "special_fun": ""
  },
  {
    "id": "588_1", "girl": "ayane", "name": "来光神楽(あやね)", "zhs_name": "来光神乐(绫音)", "zht_name": "來光神樂(綾音)", "en_name": "Sunrise Dance (Ayane)", "kr_name": "라이코우 카구라(아야네)", "type": "stm", "pow": "4174", "tec": "3616", "stm": "5252", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2021/12/29", "resell": "2023/1/12", "break": "1", "special_fun": ""
  },
  {
    "id": "588_2", "girl": "nyotengu", "name": "来光神楽(女天狗)", "zhs_name": "来光神乐(女天狗)", "zht_name": "來光神樂(女天狗)", "en_name": "Sunrise Dance (Nyotengu)", "kr_name": "라이코우 카구라(뇨텐구)", "type": "stm", "pow": "4174", "tec": "3616", "stm": "5252", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2021/12/29", "resell": "2023/1/12", "break": "1", "special_fun": ""
  },
  {
    "id": "588_3", "girl": "momiji", "name": "来光神楽(紅葉)", "zhs_name": "来光神乐(红叶)", "zht_name": "來光神樂(紅葉)", "en_name": "Sunrise Dance (Momiji)", "kr_name": "라이코우 카구라(모미지)", "type": "stm", "pow": "4174", "tec": "3616", "stm": "5252", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2021/12/29", "resell": "2023/1/12", "break": "1", "special_fun": ""
  },
  {
    "id": "588_4", "girl": "helena", "name": "来光神楽(エレナ)", "zhs_name": "来光神乐(海莲娜)", "zht_name": "來光神樂(海蓮娜)", "en_name": "Sunrise Dance (Helena)", "kr_name": "라이코우 카구라(엘레나)", "type": "stm", "pow": "4174", "tec": "3616", "stm": "5252", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2021/12/29", "resell": "2023/1/12", "break": "1", "special_fun": ""
  },
  {
    "id": "588_5", "girl": "tamaki", "name": "来光神楽(たまき)", "zhs_name": "来光神乐(环)", "zht_name": "來光神樂(環)", "en_name": "Sunrise Dance (Tamaki)", "kr_name": "라이코우 카구라(타마키)", "type": "stm", "pow": "4174", "tec": "3616", "stm": "5252", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2021/12/29", "resell": "2023/1/12", "break": "1", "special_fun": ""
  },
  {
    "id": "589", "girl": "monica", "name": "ドルチェ・フランボワーズ(モニカ)", "zhs_name": "甜美・覆盆子(莫妮卡)", "zht_name": "甜美‧覆盆子(莫妮卡)", "en_name": "Dolce Framboise (Monica)", "kr_name": "돌체 프랑부아즈(모니카)", "type": "tec", "pow": "3874", "tec": "5622", "stm": "4204", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "ラズベリーのテクニック", "skill3": "可憐なフェイント", "sell": "2022/1/1", "resell": "2022/11/4 2023/1/1", "break": "1", "special_fun": "第四年生日服，拥有双效果技能。"
  },
  {
    "id": "590", "girl": "nanami", "name": "振袖・東雲(ななみ)", "zhs_name": "振袖·东云(七海)", "zht_name": "振袖‧東雲(七海)", "en_name": "Dawn Kimono (Nanami)", "kr_name": "후리소데(새벽)(나나미)", "type": "pow", "pow": "5052", "tec": "3566", "stm": "4024", "apl": "200", "skill1": "強烈スパイクB", "skill2": "プラチナアタッカー", "skill3": "豪快なスパイク", "sell": "2022/1/1", "resell": "2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "591", "girl": "patty", "name": "振袖・陽光(パティ)", "zhs_name": "振袖·阳光(派蒂)", "zht_name": "振袖‧陽光(派蒂)", "en_name": "Sunshine Kimono (Patty)", "kr_name": "후리소데(햇살)(패티)", "type": "pow", "pow": "5002", "tec": "3556", "stm": "4184", "apl": "200", "skill1": "強烈スパイクF", "skill2": "不動のレシーブF", "skill3": "秘められたパワー3", "sell": "2022/1/1", "resell": "2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "592", "girl": "lobelia", "name": "振袖・花一華(ロベリア)", "zhs_name": "振袖·花一华(萝贝莉娅)", "zht_name": "振袖‧花一華(蘿貝莉婭)", "en_name": "Windflower Kimono (Lobelia)", "kr_name": "후리소데(아네모네)(로벨리아)", "type": "pow", "pow": "5002", "tec": "3556", "stm": "4184", "apl": "200", "skill1": "強烈スパイクF", "skill2": "不動のレシーブF", "skill3": "秘められたパワー3", "sell": "2022/1/1", "resell": "2023/1/1", "break": "0", "special_fun": ""
  },
  {
    "id": "588_6", "girl": "kasumi", "name": "来光神楽(かすみ)", "zhs_name": "来光神乐(霞)", "zht_name": "來光神樂(霞)", "en_name": "Sunrise Dance (Kasumi)", "kr_name": "라이코우 카구라(카스미)", "type": "stm", "pow": "4174", "tec": "3616", "stm": "5252", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2022/1/6", "resell": "2023/1/12", "break": "1", "special_fun": ""
  },
  {
    "id": "588_7", "girl": "kokoro", "name": "来光神楽(こころ)", "zhs_name": "来光神乐(心)", "zht_name": "來光神樂(心)", "en_name": "Sunrise Dance (Kokoro)", "kr_name": "라이코우 카구라(코코로)", "type": "stm", "pow": "4174", "tec": "3616", "stm": "5252", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2022/1/6", "resell": "2023/1/12", "break": "1", "special_fun": ""
  },
  {
    "id": "588_8", "girl": "misaki", "name": "来光神楽(みさき)", "zhs_name": "来光神乐(海咲)", "zht_name": "來光神樂(海咲)", "en_name": "Sunrise Dance (Misaki)", "kr_name": "라이코우 카구라(미사키)", "type": "stm", "pow": "4174", "tec": "3616", "stm": "5252", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2022/1/6", "resell": "2023/1/12", "break": "1", "special_fun": ""
  },
  {
    "id": "588_9", "girl": "leifang", "name": "来光神楽(レイファン)", "zhs_name": "来光神乐(丽凤)", "zht_name": "來光神樂(麗鳳)", "en_name": "Sunrise Dance (Leifang)", "kr_name": "라이코우 카구라(나나미)", "type": "stm", "pow": "4174", "tec": "3616", "stm": "5252", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2022/1/6", "resell": "2023/1/12", "break": "1", "special_fun": ""
  },
  {
    "id": "588_10", "girl": "nanami", "name": "来光神楽(ななみ)", "zhs_name": "来光神乐(七海)", "zht_name": "來光神樂(七海)", "en_name": "Sunrise Dance (Nanami)", "kr_name": "", "type": "stm", "pow": "4174", "tec": "3616", "stm": "5252", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2022/1/6", "resell": "2023/1/12", "break": "1", "special_fun": ""
  },
  {
    "id": "593", "girl": "elise", "name": "トワイライトフィッシュ(エリーゼ)", "zhs_name": "拂晓之鱼(伊莉丝)", "zht_name": "拂曉之魚(伊莉絲)", "en_name": "Twilight Fish (Elise)", "kr_name": "트와일라이트 피시(엘리제)", "type": "tec", "pow": "3536", "tec": "5132", "stm": "4074", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "鉄壁のレシーブE", "skill3": "閃きのテクニック4", "sell": "2022/1/13", "resell": "2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "594", "girl": "tsukushi", "name": "トワイライトフィッシュ(つくし)", "zhs_name": "拂晓之鱼(筑紫)", "zht_name": "拂曉之魚(筑紫)", "en_name": "Twilight Fish (Tsukushi)", "kr_name": "트와일라이트 피시(츠쿠시)", "type": "tec", "pow": "3536", "tec": "5132", "stm": "4074", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "鉄壁のレシーブE", "skill3": "閃きのテクニック4", "sell": "2022/1/13", "resell": "2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "595", "girl": "sayuri", "name": "トワイライトフィッシュ(さゆり)", "zhs_name": "拂晓之鱼(小百合)", "zht_name": "拂曉之魚(小百合)", "en_name": "Twilight Fish (Sayuri)", "kr_name": "트와일라이트 피시(사유리)", "type": "tec", "pow": "3496", "tec": "5172", "stm": "3974", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "閃きのテクニック6", "skill3": "可憐なフェイント", "sell": "2022/1/13", "resell": "2022/8/25", "break": "1", "special_fun": ""
  },
  {
    "id": "596_1", "girl": "kasumi", "name": "よむ・オフィスウェア(かすみ)", "zhs_name": "Yom‧办公室服装(霞)", "zht_name": "Yom‧OL裝(霞)", "en_name": "Yom・Office Wear (Kasumi)", "kr_name": "Yom・사무복(카스미)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_2", "girl": "honoka", "name": "よむ・オフィスウェア(ほのか)", "zhs_name": "Yom‧办公室服装(穗香)", "zht_name": "Yom‧OL裝(穗香)", "en_name": "Yom・Office Wear (Honoka)", "kr_name": "Yom・사무복(호노카)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_3", "girl": "marie", "name": "よむ・オフィスウェア(マリー)", "zhs_name": "Yom‧办公室服装(玛莉)", "zht_name": "Yom‧OL裝(瑪莉)", "en_name": "Yom・Office Wear (Marie)", "kr_name": "Yom・사무복(마리)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_4", "girl": "ayane", "name": "よむ・オフィスウェア(あやね)", "zhs_name": "Yom‧办公室服装(绫音)", "zht_name": "Yom‧OL裝(綾音)", "en_name": "Yom・Office Wear (Ayane)", "kr_name": "Yom・사무복(아야네)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_5", "girl": "nyotengu", "name": "よむ・オフィスウェア(女天狗)", "zhs_name": "Yom‧办公室服装(女天狗)", "zht_name": "Yom‧OL裝(女天狗)", "en_name": "Yom・Office Wear (Nyotengu)", "kr_name": "Yom・사무복(뇨텐구)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_6", "girl": "kokoro", "name": "よむ・オフィスウェア(こころ)", "zhs_name": "Yom‧办公室服装(心)", "zht_name": "Yom‧OL裝(心)", "en_name": "Yom・Office Wear (Kokoro)", "kr_name": "Yom・사무복(코코로)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_7", "girl": "hitomi", "name": "よむ・オフィスウェア(ヒトミ)", "zhs_name": "Yom‧办公室服装(瞳)", "zht_name": "Yom‧OL裝(瞳)", "en_name": "Yom・Office Wear (Hitomi)", "kr_name": "Yom・사무복(히토미)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_8", "girl": "momiji", "name": "よむ・オフィスウェア(紅葉)", "zhs_name": "Yom‧办公室服装(红叶)", "zht_name": "Yom‧OL裝(紅葉)", "en_name": "Yom・Office Wear (Momiji)", "kr_name": "Yom・사무복(모미지)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_9", "girl": "helena", "name": "よむ・オフィスウェア(エレナ)", "zhs_name": "Yom‧办公室服装(海莲娜)", "zht_name": "Yom‧OL裝(海蓮娜)", "en_name": "Yom・Office Wear (Helena)", "kr_name": "Yom・사무복(엘레나)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_10", "girl": "misaki", "name": "よむ・オフィスウェア(みさき)", "zhs_name": "Yom‧办公室服装(海咲)", "zht_name": "Yom‧OL裝(海咲)", "en_name": "Yom・Office Wear (Misaki)", "kr_name": "Yom・사무복(미사키)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_11", "girl": "luna", "name": "よむ・オフィスウェア(ルナ)", "zhs_name": "Yom‧办公室服装(露娜)", "zht_name": "Yom‧OL裝(露娜)", "en_name": "Yom・Office Wear (Luna)", "kr_name": "Yom・사무복(루나)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_12", "girl": "tamaki", "name": "よむ・オフィスウェア(たまき)", "zhs_name": "Yom‧办公室服装(环)", "zht_name": "Yom‧OL裝(環)", "en_name": "Yom・Office Wear (Tamaki)", "kr_name": "Yom・사무복(타마키)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_13", "girl": "leifang", "name": "よむ・オフィスウェア(レイファン)", "zhs_name": "Yom‧办公室服装(丽凤)", "zht_name": "Yom‧OL裝(麗鳳)", "en_name": "Yom・Office Wear (Leifang)", "kr_name": "Yom・사무복(레이팡)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_14", "girl": "fiona", "name": "よむ・オフィスウェア(フィオナ)", "zhs_name": "Yom‧办公室服装(菲欧娜)", "zht_name": "Yom‧OL裝(菲歐娜)", "en_name": "Yom・Office Wear (Fiona)", "kr_name": "Yom・사무복(피오나)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_15", "girl": "nagisa", "name": "よむ・オフィスウェア(なぎさ)", "zhs_name": "Yom‧办公室服装(凪咲)", "zht_name": "Yom‧OL裝(凪咲)", "en_name": "Yom・Office Wear (Nagisa)", "kr_name": "Yom・사무복(나기사)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_16", "girl": "kanna", "name": "よむ・オフィスウェア(カンナ)", "zhs_name": "Yom‧办公室服装(神无)", "zht_name": "Yom‧OL裝(神無)", "en_name": "Yom・Office Wear (Kanna)", "kr_name": "Yom・사무복(칸나)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_17", "girl": "monica", "name": "よむ・オフィスウェア(モニカ)", "zhs_name": "Yom‧办公室服装(莫妮卡)", "zht_name": "Yom‧OL裝(莫妮卡)", "en_name": "Yom・Office Wear (Monica)", "kr_name": "Yom・사무복(모니카)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_18", "girl": "sayuri", "name": "よむ・オフィスウェア(さゆり)", "zhs_name": "Yom‧办公室服装(小百合)", "zht_name": "Yom‧OL裝(小百合)", "en_name": "Yom・Office Wear (Sayuri)", "kr_name": "Yom・사무복(사유리)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_19", "girl": "patty", "name": "よむ・オフィスウェア(パティ)", "zhs_name": "Yom‧办公室服装(派蒂)", "zht_name": "Yom‧OL裝(派蒂)", "en_name": "Yom・Office Wear (Patty)", "kr_name": "Yom・사무복(패티)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_20", "girl": "tsukushi", "name": "よむ・オフィスウェア(つくし)", "zhs_name": "Yom‧办公室服装(筑紫)", "zht_name": "Yom‧OL裝(筑紫)", "en_name": "Yom・Office Wear (Tsukushi)", "kr_name": "Yom・사무복(츠쿠시)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_21", "girl": "lobelia", "name": "よむ・オフィスウェア(ロベリア)", "zhs_name": "Yom‧办公室服装(萝贝莉娅)", "zht_name": "Yom‧OL裝(蘿貝莉婭)", "en_name": "Yom・Office Wear (Lobelia)", "kr_name": "Yom・사무복(로벨리아)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_22", "girl": "nanami", "name": "よむ・オフィスウェア(ななみ)", "zhs_name": "Yom‧办公室服装(七海)", "zht_name": "Yom‧OL裝(七海)", "en_name": "Yom・Office Wear (Nanami)", "kr_name": "Yom・사무복(나나미)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "596_23", "girl": "elise", "name": "よむ・オフィスウェア(エリーゼ)", "zhs_name": "Yom‧办公室服装(伊莉丝)", "zht_name": "Yom‧OL裝(伊莉絲)", "en_name": "Yom・Office Wear (Elise)", "kr_name": "Yom・사무복(엘리제)", "type": "stm", "pow": "3646", "tec": "4354", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "高度な心理戦F", "skill3": "オフィスウェアのスタミナ", "sell": "2022/1/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "597", "girl": "tina", "name": "ドリーム・チェイサー(ティナ)", "zhs_name": "追梦者(蒂娜)", "zht_name": "追夢者(蒂娜)", "en_name": "Dream Chaser (Tina)", "kr_name": "드림 체이서(티나)", "type": "pow", "pow": "5152", "tec": "3406", "stm": "4184", "apl": "200", "skill1": "強烈スパイクA", "skill2": "圧倒的な気迫B", "skill3": "秘められたパワー3", "sell": "2022/1/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "598", "girl": "monica", "name": "ヴィーナス・ケージ(モニカ)", "zhs_name": "维纳斯之栅(莫妮卡)", "zht_name": "維納斯之柵(莫妮卡)", "en_name": "Venus Cage (Monica)", "kr_name": "비너스 케이지(모니카)", "type": "pow", "pow": "5062", "tec": "3486", "stm": "4094", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "秘められたパワー6", "skill3": "熱烈なエール", "sell": "2022/1/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "599", "girl": "hitomi", "name": "ヴィーナス・ケージ(ヒトミ)", "zhs_name": "维纳斯之栅(瞳)", "zht_name": "維納斯之柵(瞳)", "en_name": "Venus Cage (Hitomi)", "kr_name": "비너스 케이지(히토미)", "type": "pow", "pow": "5132", "tec": "3546", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "強烈なプレッシャーA", "skill3": "秘められたパワー5", "sell": "2022/1/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "600", "girl": "misaki", "name": "ヴィーナス・ケージ(みさき)", "zhs_name": "维纳斯之栅(海咲)", "zht_name": "維納斯之柵(海咲)", "en_name": "Venus Cage (Misaki)", "kr_name": "비너스 케이지(미사키)", "type": "pow", "pow": "5132", "tec": "3546", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "強烈なプレッシャーA", "skill3": "秘められたパワー5", "sell": "2022/1/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "601", "girl": "helena", "name": "ドルチェ・フランボワーズ(エレナ)", "zhs_name": "甜美·覆盆子(海莲娜)", "zht_name": "甜美‧覆盆子(海蓮娜)", "en_name": "Dolce Framboise (Helena)", "kr_name": "돌체 프랑부아즈(엘레나)", "type": "tec", "pow": "3904", "tec": "5622", "stm": "4174", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "ラズベリーのテクニック", "skill3": "可憐なフェイント", "sell": "2022/1/30", "resell": "2022/11/4 2023/1/30", "break": "1", "special_fun": ""
  },
  {
    "id": "602", "girl": "elise", "name": "深紅のスリットワンピ(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2022/2/1", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "603_1", "girl": "marie", "name": "ひだまりプロムナード(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4364", "tec": "3476", "stm": "5202", "apl": "200", "skill1": "圧倒的な気迫F", "skill2": "内から湧き上がるスタミナ3", "skill3": "豪快なスパイク", "sell": "2022/2/3", "resell": "2022/11/22 2023/6/8", "break": "1", "special_fun": ""
  },
  {
    "id": "603_2", "girl": "kanna", "name": "ひだまりプロムナード(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4324", "tec": "3656", "stm": "5162", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "強烈なプレッシャーC", "skill3": "内から湧き上がるスタミナ6", "sell": "2022/2/3", "resell": "2022/11/22 2023/6/8", "break": "1", "special_fun": ""
  },
  {
    "id": "603_3", "girl": "lobelia", "name": "ひだまりプロムナード(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4324", "tec": "3656", "stm": "5162", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "強烈なプレッシャーC", "skill3": "内から湧き上がるスタミナ6", "sell": "2022/2/3", "resell": "2022/11/22 2023/6/8", "break": "1", "special_fun": ""
  },
  {
    "id": "604_1", "girl": "kasumi", "name": "シュガー・パフューム(かすみ)", "zhs_name": "砂糖·芳香(霞)", "zht_name": "甜蜜香氛(霞)", "en_name": "Sugar Perfume (Kasumi)", "kr_name": "슈가 퍼퓸(카스미)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_2", "girl": "honoka", "name": "シュガー・パフューム(ほのか)", "zhs_name": "砂糖·芳香(穗香)", "zht_name": "甜蜜香氛(穗香)", "en_name": "Sugar Perfume (Honoka)", "kr_name": "슈가 퍼퓸(호노카)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_3", "girl": "marie", "name": "シュガー・パフューム(マリー)", "zhs_name": "砂糖·芳香(玛莉)", "zht_name": "甜蜜香氛(瑪莉)", "en_name": "Sugar Perfume (Marie)", "kr_name": "슈가 퍼퓸(마리)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_4", "girl": "ayane", "name": "シュガー・パフューム(あやね)", "zhs_name": "砂糖·芳香(绫音)", "zht_name": "甜蜜香氛(綾音)", "en_name": "Sugar Perfume (Ayane)", "kr_name": "슈가 퍼퓸(아야네)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_5", "girl": "nyotengu", "name": "シュガー・パフューム(女天狗)", "zhs_name": "砂糖·芳香(女天狗)", "zht_name": "甜蜜香氛(女天狗)", "en_name": "Sugar Perfume (Nyotengu)", "kr_name": "슈가 퍼퓸(뇨텐구)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_6", "girl": "kokoro", "name": "シュガー・パフューム(こころ)", "zhs_name": "砂糖·芳香(心)", "zht_name": "甜蜜香氛(心)", "en_name": "Sugar Perfume (Kokoro)", "kr_name": "슈가 퍼퓸(코코로)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_7", "girl": "hitomi", "name": "シュガー・パフューム(ヒトミ)", "zhs_name": "砂糖·芳香(瞳)", "zht_name": "甜蜜香氛(瞳)", "en_name": "Sugar Perfume (Hitomi)", "kr_name": "슈가 퍼퓸(히토미)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_8", "girl": "momiji", "name": "シュガー・パフューム(紅葉)", "zhs_name": "砂糖·芳香(红叶)", "zht_name": "甜蜜香氛(紅葉)", "en_name": "Sugar Perfume (Momiji)", "kr_name": "슈가 퍼퓸(모미지)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_9", "girl": "helena", "name": "シュガー・パフューム(エレナ)", "zhs_name": "砂糖·芳香(海莲娜)", "zht_name": "甜蜜香氛(海蓮娜)", "en_name": "Sugar Perfume (Helena)", "kr_name": "슈가 퍼퓸(엘레나)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_10", "girl": "misaki", "name": "シュガー・パフューム(みさき)", "zhs_name": "砂糖·芳香(海咲)", "zht_name": "甜蜜香氛(海咲)", "en_name": "Sugar Perfume (Misaki)", "kr_name": "슈가 퍼퓸(미사키)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_11", "girl": "luna", "name": "シュガー・パフューム(ルナ)", "zhs_name": "砂糖·芳香(露娜)", "zht_name": "甜蜜香氛(露娜)", "en_name": "Sugar Perfume (Luna)", "kr_name": "슈가 퍼퓸(루나)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_12", "girl": "tamaki", "name": "シュガー・パフューム(たまき)", "zhs_name": "砂糖·芳香(环)", "zht_name": "甜蜜香氛(環)", "en_name": "Sugar Perfume (Tamaki)", "kr_name": "슈가 퍼퓸(타마키)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_13", "girl": "leifang", "name": "シュガー・パフューム(レイファン)", "zhs_name": "砂糖·芳香(丽凤)", "zht_name": "甜蜜香氛(麗鳳)", "en_name": "Sugar Perfume (Leifang)", "kr_name": "슈가 퍼퓸(레이팡)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_14", "girl": "fiona", "name": "シュガー・パフューム(フィオナ)", "zhs_name": "砂糖·芳香(菲欧娜)", "zht_name": "甜蜜香氛(菲歐娜)", "en_name": "Sugar Perfume (Fiona)", "kr_name": "슈가 퍼퓸(피오나)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_15", "girl": "nagisa", "name": "シュガー・パフューム(なぎさ)", "zhs_name": "砂糖·芳香(凪咲)", "zht_name": "甜蜜香氛(凪咲)", "en_name": "Sugar Perfume (Nagisa)", "kr_name": "슈가 퍼퓸(나기사)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_16", "girl": "kanna", "name": "シュガー・パフューム(カンナ)", "zhs_name": "砂糖·芳香(神无)", "zht_name": "甜蜜香氛(神無)", "en_name": "Sugar Perfume (Kanna)", "kr_name": "슈가 퍼퓸(칸나)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_17", "girl": "monica", "name": "シュガー・パフューム(モニカ)", "zhs_name": "砂糖·芳香(莫妮卡)", "zht_name": "甜蜜香氛(莫妮卡)", "en_name": "Sugar Perfume (Monica)", "kr_name": "슈가 퍼퓸(모니카)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_18", "girl": "sayuri", "name": "シュガー・パフューム(さゆり)", "zhs_name": "砂糖·芳香(小百合)", "zht_name": "甜蜜香氛(小百合)", "en_name": "Sugar Perfume (Sayuri)", "kr_name": "슈가 퍼퓸(사유리)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_19", "girl": "patty", "name": "シュガー・パフューム(パティ)", "zhs_name": "砂糖·芳香(派蒂)", "zht_name": "甜蜜香氛(派蒂)", "en_name": "Sugar Perfume (Patty)", "kr_name": "슈가 퍼퓸(패티)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_20", "girl": "tsukushi", "name": "シュガー・パフューム(つくし)", "zhs_name": "砂糖·芳香(筑紫)", "zht_name": "甜蜜香氛(筑紫)", "en_name": "Sugar Perfume (Tsukushi)", "kr_name": "슈가 퍼퓸(츠쿠시)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_21", "girl": "lobelia", "name": "シュガー・パフューム(ロベリア)", "zhs_name": "砂糖·芳香(萝贝莉娅)", "zht_name": "甜蜜香氛(蘿貝莉婭)", "en_name": "Sugar Perfume (Lobelia)", "kr_name": "슈가 퍼퓸(로벨리아)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_22", "girl": "nanami", "name": "シュガー・パフューム(ななみ)", "zhs_name": "砂糖·芳香(七海)", "zht_name": "甜蜜香氛(七海)", "en_name": "Sugar Perfume (Nanami)", "kr_name": "슈가 퍼퓸(나나미)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "604_23", "girl": "elise", "name": "シュガー・パフューム(エリーゼ)", "zhs_name": "砂糖·芳香(伊莉丝)", "zht_name": "甜蜜香氛(伊莉絲)", "en_name": "Sugar Perfume (Elise)", "kr_name": "슈가 퍼퓸(엘리제)", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2022/2/10", "resell": "2023/2/9", "break": "1", "special_fun": ""
  },
  {
    "id": "605", "girl": "fiona", "name": "ドルチェ・ストロベリー(フィオナ)", "zhs_name": "甜美·草莓(菲欧娜)", "zht_name": "甜美‧草莓(菲歐娜)", "en_name": "Dolce Strawberry (Fiona)", "kr_name": "돌체 스트로베리(피오나)", "type": "tec", "pow": "3924", "tec": "5622", "stm": "4154", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "イチゴのテクニック", "skill3": "可憐なフェイント", "sell": "2022/2/11", "resell": "2022/11/4 2023/2/11", "break": "1", "special_fun": ""
  },
  {
    "id": "471_21", "girl": "lobelia", "name": "プルミエ・ランデブー(ロベリア)", "zhs_name": "初次约会(萝贝莉娅)", "zht_name": "初次相約(蘿貝莉婭)", "en_name": "Premier Rendezvous (Lobelia)", "kr_name": "프리미에르 랑데부(로벨리아)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2022/2/17", "resell": "2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_22", "girl": "nanami", "name": "プルミエ・ランデブー(ななみ)", "zhs_name": "初次约会(七海)", "zht_name": "初次相約(七海)", "en_name": "Premier Rendezvous (Nanami)", "kr_name": "프리미에르 랑데부(나나미)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2022/2/17", "resell": "2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "471_23", "girl": "elise", "name": "プルミエ・ランデブー(エリーゼ)", "zhs_name": "初次约会(伊莉丝)", "zht_name": "初次相約(伊莉絲)", "en_name": "Premier Rendezvous (Elise)", "kr_name": "프리미에르 랑데부(엘리제)", "type": "pow", "pow": "5042", "tec": "3596", "stm": "4004", "apl": "200", "skill1": "強烈スパイクF", "skill2": "ランデブーのパワー", "skill3": "熱烈なエール", "sell": "2022/2/17", "resell": "2023/2/2", "break": "1", "special_fun": ""
  },
  {
    "id": "606", "girl": "kasumi", "name": "ドルチェ・ストロベリー(かすみ)", "zhs_name": "甜美·草莓(霞)", "zht_name": "甜美‧草莓(霞)", "en_name": "Dolce Strawberry (Kasumi)", "kr_name": "돌체 스트로베리(카스미)", "type": "tec", "pow": "3894", "tec": "5622", "stm": "4184", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "イチゴのテクニック", "skill3": "可憐なフェイント", "sell": "2022/2/23", "resell": "2022/11/4 2023/2/23", "break": "1", "special_fun": ""
  },
  {
    "id": "607_1", "girl": "kokoro", "name": "ソフィー・いつものあたし(こころ)", "zhs_name": "苏菲·平时的我(心)", "zht_name": "蘇菲・平時的我(心)", "en_name": "Usual Self Sophie (Kokoro)", "kr_name": "소피・평소의 나(코코로)", "type": "tec", "pow": "3794", "tec": "5042", "stm": "3806", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ソフィーのテクニック", "skill3": "可憐なフェイント", "sell": "2022/2/24", "resell": "2023/3/22", "break": "1", "special_fun": ""
  },
  {
    "id": "607_2", "girl": "misaki", "name": "ソフィー・いつものあたし(みさき)", "zhs_name": "苏菲·平时的我(海咲)", "zht_name": "蘇菲・平時的我(海咲)", "en_name": "Usual Self Sophie (Misaki)", "kr_name": "소피・평소의 나(미사키)", "type": "tec", "pow": "3794", "tec": "5042", "stm": "3806", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ソフィーのテクニック", "skill3": "可憐なフェイント", "sell": "2022/2/24", "resell": "2023/3/22", "break": "1", "special_fun": ""
  },
  {
    "id": "607_3", "girl": "leifang", "name": "ソフィー・いつものあたし(レイファン)", "zhs_name": "苏菲·平时的我(丽凤)", "zht_name": "蘇菲・平時的我(麗鳳)", "en_name": "Usual Self Sophie (Leifang)", "kr_name": "소피・평소의 나(레이팡)", "type": "tec", "pow": "3794", "tec": "5042", "stm": "3806", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ソフィーのテクニック", "skill3": "可憐なフェイント", "sell": "2022/2/24", "resell": "2023/3/22", "break": "1", "special_fun": ""
  },
  {
    "id": "607_4", "girl": "fiona", "name": "ソフィー・いつものあたし(フィオナ)", "zhs_name": "苏菲·平时的我(菲欧娜)", "zht_name": "蘇菲・平時的我(菲歐娜)", "en_name": "Usual Self Sophie (Fiona)", "kr_name": "소피・평소의 나(피오나)", "type": "tec", "pow": "3794", "tec": "5042", "stm": "3806", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ソフィーのテクニック", "skill3": "可憐なフェイント", "sell": "2022/2/24", "resell": "2023/3/22", "break": "1", "special_fun": ""
  },
  {
    "id": "607_5", "girl": "nanami", "name": "ソフィー・いつものあたし(ななみ)", "zhs_name": "苏菲·平时的我(七海)", "zht_name": "蘇菲・平時的我(七海)", "en_name": "Usual Self Sophie (Nanami)", "kr_name": "소피・평소의 나(피오나)", "type": "tec", "pow": "3794", "tec": "5042", "stm": "3806", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ソフィーのテクニック", "skill3": "可憐なフェイント", "sell": "2022/2/24", "resell": "2023/3/22", "break": "1", "special_fun": ""
  },
  {
    "id": "608_1", "girl": "honoka", "name": "プラフタ・オリジナル(ほのか)", "zhs_name": "普拉芙妲·初始(穗香)", "zht_name": "普拉芙妲・初始(穗香)", "en_name": "Plachta Original (Honoka)", "kr_name": "플라흐타・오리지널(호노카)", "type": "tec", "pow": "3684", "tec": "5162", "stm": "3796", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "プラフタのテクニック", "skill3": "熱烈なエール", "sell": "2022/2/24", "resell": "2023/3/22", "break": "1", "special_fun": ""
  },
  {
    "id": "608_2", "girl": "luna", "name": "プラフタ・オリジナル(ルナ)", "zhs_name": "普拉芙妲·初始(露娜)", "zht_name": "普拉芙妲・初始(露娜)", "en_name": "Plachta Original (Luna)", "kr_name": "플라흐타・오리지널(루나)", "type": "tec", "pow": "3684", "tec": "5162", "stm": "3796", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "プラフタのテクニック", "skill3": "熱烈なエール", "sell": "2022/2/24", "resell": "2023/3/22", "break": "1", "special_fun": ""
  },
  {
    "id": "608_3", "girl": "tamaki", "name": "プラフタ・オリジナル(たまき)", "zhs_name": "普拉芙妲·初始(环)", "zht_name": "普拉芙妲・初始(環)", "en_name": "Plachta Original (Tamaki)", "kr_name": "플라흐타・오리지널(타마키)", "type": "tec", "pow": "3684", "tec": "5162", "stm": "3796", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "プラフタのテクニック", "skill3": "熱烈なエール", "sell": "2022/2/24", "resell": "2023/3/22", "break": "1", "special_fun": ""
  },
  {
    "id": "608_4", "girl": "monica", "name": "プラフタ・オリジナル(モニカ)", "zhs_name": "普拉芙妲·初始(莫妮卡)", "zht_name": "普拉芙妲・初始(莫妮卡)", "en_name": "Plachta Original (Monica)", "kr_name": "플라흐타・오리지널(모니카)", "type": "tec", "pow": "3684", "tec": "5162", "stm": "3796", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "プラフタのテクニック", "skill3": "熱烈なエール", "sell": "2022/2/24", "resell": "2023/3/22", "break": "1", "special_fun": ""
  },
  {
    "id": "608_5", "girl": "elise", "name": "プラフタ・オリジナル(エリーゼ)", "zhs_name": "普拉芙妲·初始(伊莉丝)", "zht_name": "普拉芙妲・初始(伊莉絲)", "en_name": "Plachta Original (Elise)", "kr_name": "플라흐타・오리지널(엘리제)", "type": "tec", "pow": "3684", "tec": "5162", "stm": "3796", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "プラフタのテクニック", "skill3": "熱烈なエール", "sell": "2022/2/24", "resell": "2023/3/22", "break": "1", "special_fun": ""
  },
  {
    "id": "609_1", "girl": "honoka", "name": "モーモ・ビキニ(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "3706", "tec": "4506", "stm": "4214", "apl": "550", "skill1": "裏の裏を突くフェイントD", "skill2": "隠しきれない魅力3", "skill3": "可憐なフェイント", "sell": "2022/3/3", "resell": "2022/11/23 2023/2/22 2023/7/13", "break": "1", "special_fun": ""
  },
  {
    "id": "609_2", "girl": "luna", "name": "モーモ・ビキニ(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "3706", "tec": "4506", "stm": "4214", "apl": "550", "skill1": "裏の裏を突くフェイントD", "skill2": "隠しきれない魅力3", "skill3": "可憐なフェイント", "sell": "2022/3/3", "resell": "2022/11/23 2023/2/22 2023/7/13", "break": "1", "special_fun": ""
  },
  {
    "id": "609_3", "girl": "sayuri", "name": "モーモ・ビキニ(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "3706", "tec": "4506", "stm": "4214", "apl": "550", "skill1": "裏の裏を突くフェイントD", "skill2": "隠しきれない魅力3", "skill3": "可憐なフェイント", "sell": "2022/3/3", "resell": "2022/11/23 2023/2/22 2023/7/13", "break": "1", "special_fun": ""
  },
  {
    "id": "609_4", "girl": "tsukushi", "name": "モーモ・ビキニ(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "3706", "tec": "4506", "stm": "4214", "apl": "550", "skill1": "裏の裏を突くフェイントD", "skill2": "隠しきれない魅力3", "skill3": "可憐なフェイント", "sell": "2022/3/3", "resell": "2022/11/23 2023/2/22 2023/7/13", "break": "1", "special_fun": ""
  },
  {
    "id": "609_5", "girl": "elise", "name": "モーモ・ビキニ(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "3706", "tec": "4506", "stm": "4214", "apl": "550", "skill1": "裏の裏を突くフェイントD", "skill2": "隠しきれない魅力3", "skill3": "可憐なフェイント", "sell": "2022/3/3", "resell": "2022/11/23 2023/2/22 2023/7/13", "break": "1", "special_fun": ""
  },
  {
    "id": "311_10", "girl": "ayane", "name": "ホワイト・プリンス(あやね)", "zhs_name": "白马王子(绫音)", "zht_name": "白馬王子(綾音)", "en_name": "White Prince (Ayane)", "kr_name": "화이트 프린스(아야네)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2022/3/10", "resell": "", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "311_11", "girl": "misaki", "name": "ホワイト・プリンス(みさき)", "zhs_name": "白马王子(海咲)", "zht_name": "白馬王子(海咲)", "en_name": "White Prince (Misaki)", "kr_name": "화이트 프린스(미사키)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2022/3/10", "resell": "", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "311_12", "girl": "monica", "name": "ホワイト・プリンス(モニカ)", "zhs_name": "白马王子(莫妮卡)", "zht_name": "白馬王子(莫妮卡)", "en_name": "White Prince (Monica)", "kr_name": "화이트 프린스(모니카)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2022/3/10", "resell": "", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "311_13", "girl": "lobelia", "name": "ホワイト・プリンス(ロベリア)", "zhs_name": "白马王子(萝贝莉娅)", "zht_name": "白馬王子(蘿貝莉婭)", "en_name": "White Prince (Lobelia)", "kr_name": "화이트 프린스(로벨리아)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2022/3/10", "resell": "", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "311_14", "girl": "nanami", "name": "ホワイト・プリンス(ななみ)", "zhs_name": "白马王子(七海)", "zht_name": "白馬王子(七海)", "en_name": "White Prince (Nanami)", "kr_name": "화이트 프린스(나나미)", "type": "tec", "pow": "3596", "tec": "5122", "stm": "3924", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック4", "skill3": "可憐なフェイント", "sell": "2022/3/10", "resell": "", "break": "1", "special_fun": "附带100经验回想。"
  },
  {
    "id": "610", "girl": "tina", "name": "葛城・忍転身(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5122", "tec": "3446", "stm": "4074", "apl": "200", "skill1": "強烈スパイクE", "skill2": "葛城のパワー", "skill3": "豪快なスパイク", "sell": "2022/3/17", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "611", "girl": "tsukushi", "name": "半蔵忍装束(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3506", "stm": "4194", "apl": "200", "skill1": "強烈スパイクD", "skill2": "圧倒的な気迫D", "skill3": "半蔵のパワー", "sell": "2022/3/17", "resell": "", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "612", "girl": "kanna", "name": "紅蓮隊忍装束(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3506", "stm": "4194", "apl": "200", "skill1": "強烈スパイクD", "skill2": "圧倒的な気迫D", "skill3": "紅蓮隊のパワー", "sell": "2022/3/17", "resell": "", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "613", "girl": "lobelia", "name": "月閃忍装束(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3764", "tec": "5042", "stm": "3936", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "天才的な先読みD", "skill3": "月閃のテクニック", "sell": "2022/3/17", "resell": "", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "614", "girl": "nanami", "name": "月閃忍装束(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3764", "tec": "5042", "stm": "3936", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "天才的な先読みD", "skill3": "月閃のテクニック", "sell": "2022/3/17", "resell": "", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "615", "girl": "monica", "name": "蛇女忍装束(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3506", "stm": "4194", "apl": "200", "skill1": "強烈スパイクD", "skill2": "圧倒的な気迫D", "skill3": "蛇女忍のパワー", "sell": "2022/3/17", "resell": "", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "616", "girl": "patty", "name": "蛇女忍装束(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3506", "stm": "4194", "apl": "200", "skill1": "強烈スパイクD", "skill2": "圧倒的な気迫D", "skill3": "蛇女忍のパワー", "sell": "2022/3/17", "resell": "", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "617", "girl": "sayuri", "name": "巫神楽忍装束(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3764", "tec": "5042", "stm": "3936", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "天才的な先読みD", "skill3": "巫神楽のテクニック", "sell": "2022/3/17", "resell": "", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "618", "girl": "elise", "name": "巫神楽忍装束(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3764", "tec": "5042", "stm": "3936", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "天才的な先読みD", "skill3": "巫神楽のテクニック", "sell": "2022/3/17", "resell": "", "break": "1", "special_fun": "服装拥有炸裂效果(碎片满天飞)「シノビマスター 閃乱カグラ NEW LINK」联动服装 附带额外CG 10经验一个KT你也是做的出来噢"
  },
  {
    "id": "619", "girl": "misaki", "name": "シノマス水着・飛鳥（みさき）", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4144", "tec": "3616", "stm": "5282", "apl": "200", "skill1": "強烈スパイクC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/3/23", "resell": "", "break": "1", "special_fun": "「シノビマスター 閃乱カグラ NEW LINK」联动服装"
  },
  {
    "id": "620", "girl": "tamaki", "name": "シノマス水着・叢（たまき）", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4144", "tec": "3616", "stm": "5282", "apl": "200", "skill1": "強烈スパイクC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/3/23", "resell": "", "break": "1", "special_fun": "「シノビマスター 閃乱カグラ NEW LINK」联动服装"
  },
  {
    "id": "621", "girl": "nagisa", "name": "シノマス水着・両備（なぎさ）", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4144", "tec": "3616", "stm": "5282", "apl": "200", "skill1": "強烈スパイクC", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/3/23", "resell": "", "break": "1", "special_fun": "「シノビマスター 閃乱カグラ NEW LINK」联动服装"
  },
  {
    "id": "622", "girl": "honoka", "name": "ドルチェ・マンゴー(ほのか)", "zhs_name": "甜美·芒果(穗香)", "zht_name": "甜美・芒果(穗香)", "en_name": "Dolce Mango (Honoka)", "kr_name": "돌체 망고(호노카)", "type": "pow", "pow": "5622", "tec": "3934", "stm": "4144", "apl": "200", "skill1": "W・疲れ知らずの猛攻G", "skill2": "マンゴーのパワー", "skill3": "豪快なスパイク", "sell": "2022/3/24", "resell": "2022/11/4 2023/3/24", "break": "1", "special_fun": ""
  },
  {
    "id": "623_1", "girl": "kasumi", "name": "はじけるラヴァー(かすみ)", "zhs_name": "奔放的恋人(霞)", "zht_name": "奔放戀人(霞)", "en_name": "Bursting Lover (Kasumi)", "kr_name": "팝핑 러버(카스미)", "type": "apl", "pow": "4546", "tec": "3686", "stm": "4194", "apl": "550", "skill1": "強烈スパイクE", "skill2": "隠しきれない魅力6", "skill3": "豪快なスパイク", "sell": "2022/3/29", "resell": "2022/11/24 2023/3/16", "break": "1", "special_fun": ""
  },
  {
    "id": "623_2", "girl": "nyotengu", "name": "はじけるラヴァー(女天狗)", "zhs_name": "奔放的恋人(女天狗)", "zht_name": "奔放戀人(女天狗)", "en_name": "Bursting Lover (Nyotengu)", "kr_name": "팝핑 러버(뇨텐구)", "type": "apl", "pow": "4546", "tec": "3686", "stm": "4194", "apl": "550", "skill1": "強烈スパイクE", "skill2": "隠しきれない魅力6", "skill3": "豪快なスパイク", "sell": "2022/3/29", "resell": "2022/11/24 2023/3/16", "break": "1", "special_fun": ""
  },
  {
    "id": "623_3", "girl": "momiji", "name": "はじけるラヴァー(紅葉)", "zhs_name": "奔放的恋人(红叶)", "zht_name": "奔放戀人(紅葉)", "en_name": "Bursting Lover (Momiji)", "kr_name": "팝핑 러버(모미지)", "type": "apl", "pow": "4546", "tec": "3686", "stm": "4194", "apl": "550", "skill1": "強烈スパイクE", "skill2": "隠しきれない魅力6", "skill3": "豪快なスパイク", "sell": "2022/3/29", "resell": "2022/11/24 2023/3/16", "break": "1", "special_fun": ""
  },
  {
    "id": "623_4", "girl": "monica", "name": "はじけるラヴァー(モニカ)", "zhs_name": "奔放的恋人(莫妮卡)", "zht_name": "奔放戀人(莫妮卡)", "en_name": "Bursting Lover (Monica)", "kr_name": "팝핑 러버(모니카)", "type": "apl", "pow": "4546", "tec": "3686", "stm": "4194", "apl": "550", "skill1": "強烈スパイクE", "skill2": "隠しきれない魅力6", "skill3": "豪快なスパイク", "sell": "2022/3/29", "resell": "2022/11/24 2023/3/16", "break": "1", "special_fun": ""
  },
  {
    "id": "623_5", "girl": "elise", "name": "はじけるラヴァー(エリーゼ)", "zhs_name": "奔放的恋人(伊莉丝)", "zht_name": "奔放戀人(伊莉絲)", "en_name": "Bursting Lover (Elise)", "kr_name": "팝핑 러버(엘리제)", "type": "apl", "pow": "4546", "tec": "3686", "stm": "4194", "apl": "550", "skill1": "強烈スパイクE", "skill2": "隠しきれない魅力6", "skill3": "豪快なスパイク", "sell": "2022/3/29", "resell": "2022/11/24 2023/3/16", "break": "1", "special_fun": ""
  },
  {
    "id": "624", "girl": "sayuri", "name": "ドルチェ・マンゴー(さゆり)", "zhs_name": "甜美·芒果(小百合)", "zht_name": "甜美・芒果(小百合)", "en_name": "Dolce Mango (Sayuri)", "kr_name": "돌체 망고(사유리)", "type": "tec", "pow": "3884", "tec": "5622", "stm": "4194", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "マンゴーのテクニック", "skill3": "可憐なフェイント", "sell": "2022/3/31", "resell": "2022/11/4 2023/3/31", "break": "1", "special_fun": ""
  },
  {
    "id": "625", "girl": "amy", "name": "バイナリー・コネクト(エイミー)", "zhs_name": "二进制·连接(艾米)", "zht_name": "二進位連結(愛咪)", "en_name": "Binary Connect (Amy)", "kr_name": "바이너리 커넥트(에이미)", "type": "tec", "pow": "3566", "tec": "5122", "stm": "4054", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "高度な心理戦F", "skill3": "閃きのテクニック6", "sell": "2022/4/4", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "626", "girl": "patty", "name": "ゆるふわパーカー(パティ)", "zhs_name": "轻柔连帽衫(派蒂)", "zht_name": "輕柔連帽衫(派蒂)", "en_name": "Soft 'n Fluffy Parka (Patty)", "kr_name": "부드러운 파카(패티)", "type": "tec", "pow": "3476", "tec": "5152", "stm": "4014", "apl": "200", "skill1": "鉄壁のレシーブB", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2022/4/5", "resell": " 2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "627", "girl": "leifang", "name": "ゆるふわパーカー(レイファン)", "zhs_name": "轻柔连帽衫(丽凤)", "zht_name": "輕柔連帽衫(麗鳳)", "en_name": "Soft 'n Fluffy Parka (Leifang)", "kr_name": "부드러운 파카(레이팡)", "type": "tec", "pow": "3546", "tec": "5102", "stm": "4094", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "驚異のスタミナD", "skill3": "閃きのテクニック4", "sell": "2022/4/5", "resell": "2022/12/8", "break": "1", "special_fun": ""
  },
  {
    "id": "628", "girl": "hitomi", "name": "ワイルドウインド(ヒトミ)", "zhs_name": "狂风(瞳)", "zht_name": "狂風(瞳)", "en_name": "Wild Wind (Hitomi)", "kr_name": "와일드 윈드(히토미)", "type": "stm", "pow": "3576", "tec": "4334", "stm": "5132", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "内から湧き上がるスタミナ5", "skill3": "可憐なフェイント", "sell": "2022/4/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "629", "girl": "nyotengu", "name": "ワイルドウインド(女天狗)", "zhs_name": "狂风(女天狗)", "zht_name": "狂風(女天狗)", "en_name": "Wild Wind (Nyotengu)", "kr_name": "와일드 윈드(뇨텐구)", "type": "stm", "pow": "3636", "tec": "4274", "stm": "5232", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "天才的な先読みF", "skill3": "内から湧き上がるスタミナ3", "sell": "2022/4/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "630", "girl": "misaki", "name": "ワイルドウインド(みさき)", "zhs_name": "狂风(海咲)", "zht_name": "狂風(海咲)", "en_name": "Wild Wind (Misaki)", "kr_name": "와일드 윈드(미사키)", "type": "stm", "pow": "3636", "tec": "4274", "stm": "5232", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "天才的な先読みF", "skill3": "内から湧き上がるスタミナ3", "sell": "2022/4/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "631", "girl": "nanami", "name": "ドルチェ・メローネ(ななみ)", "zhs_name": "甜美·蜜瓜(七海)", "zht_name": "甜美・甜瓜(七海)", "en_name": "Dolce Melone (Nanami)", "kr_name": "돌체 메로네(나나미)", "type": "pow", "pow": "5622", "tec": "3844", "stm": "4234", "apl": "200", "skill1": "W・疲れ知らずの猛攻G", "skill2": "メロンのパワー", "skill3": "豪快なスパイク", "sell": "2022/4/16", "resell": "2022/11/4 2023/4/16", "break": "1", "special_fun": ""
  },
  {
    "id": "632", "girl": "honoka", "name": "春彩のスクールウェア(ほのか)", "zhs_name": "春色校服(穗香)", "zht_name": "春色校服(穗香)", "en_name": "Springtime Schoolwear (Honoka)", "kr_name": "화사한 봄철 학생복(호노카)", "type": "pow", "pow": "4982", "tec": "4114", "stm": "3646", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー6", "sell": "2022/4/21", "resell": "2023/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "633", "girl": "kokoro", "name": "春彩のスクールウェア(こころ)", "zhs_name": "春色校服(心)", "zht_name": "春色校服(心)", "en_name": "Springtime Schoolwear (Kokoro)", "kr_name": "화사한 봄철 학생복(코코로)", "type": "pow", "pow": "4982", "tec": "4114", "stm": "3646", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー6", "sell": "2022/4/21", "resell": "2023/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "634", "girl": "fiona", "name": "春彩のスクールウェア(フィオナ)", "zhs_name": "春色校服(菲欧娜)", "zht_name": "春色校服(菲歐娜)", "en_name": "Springtime Schoolwear (Fiona)", "kr_name": "화사한 봄철 학생복(피오나)", "type": "pow", "pow": "4982", "tec": "4114", "stm": "3646", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー6", "sell": "2022/4/21", "resell": "2023/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "635", "girl": "patty", "name": "春彩のスクールウェア(パティ)", "zhs_name": "春色校服(派蒂)", "zht_name": "春色校服(派蒂)", "en_name": "Springtime Schoolwear (Patty)", "kr_name": "화사한 봄철 학생복(패티)", "type": "pow", "pow": "4982", "tec": "4114", "stm": "3646", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー6", "sell": "2022/4/21", "resell": "2023/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "636", "girl": "lobelia", "name": "春彩のスクールウェア(ロベリア)", "zhs_name": "春色校服(萝贝莉娅)", "zht_name": "春色校服(蘿貝莉婭)", "en_name": "Springtime Schoolwear (Lobelia)", "kr_name": "화사한 봄철 학생복(로벨리아)", "type": "pow", "pow": "4982", "tec": "4114", "stm": "3646", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー6", "sell": "2022/4/21", "resell": "2023/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "637", "girl": "nanami", "name": "春彩のスクールウェア(ななみ)", "zhs_name": "春色校服(七海)", "zht_name": "春色校服(七海)", "en_name": "Springtime Schoolwear (Nanami)", "kr_name": "화사한 봄철 학생복(나나미)", "type": "pow", "pow": "4982", "tec": "4114", "stm": "3646", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー6", "sell": "2022/4/21", "resell": "2023/3/29", "break": "1", "special_fun": ""
  },
  {
    "id": "638", "girl": "leifang", "name": "ドルチェ・メローネ(レイファン)", "zhs_name": "甜美·蜜瓜(丽凤)", "zht_name": "甜美・甜瓜(麗鳳)", "en_name": "Dolce Melone (Leifang)", "kr_name": "돌체 메로네(레이팡)", "type": "tec", "pow": "3834", "tec": "5622", "stm": "4244", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "メロンのテクニック", "skill3": "可憐なフェイント", "sell": "2022/4/23", "resell": "2022/11/4 2023/4/23", "break": "1", "special_fun": ""
  },
  {
    "id": "639_1", "girl": "hitomi", "name": "オービット・アンタレス(ヒトミ)", "zhs_name": "轨道・心宿二(小百合・莫妮卡・瞳)", "zht_name": "", "en_name": "Orbit Antares (Sayuri・monica・hitomi)", "kr_name": "오르빗 안타레스(사유리・모니카・히토미)", "type": "stm", "pow": "4234", "tec": "3586", "stm": "5222", "apl": "200", "skill1": "不動のレシーブB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/4/28", "resell": "2022/11/29", "break": "1", "special_fun": ""
  },
  {
    "id": "639_2", "girl": "monica", "name": "オービット・アンタレス(モニカ)", "zhs_name": "轨道・心宿二(小百合・莫妮卡・瞳)", "zht_name": "", "en_name": "Orbit Antares (Sayuri・monica・hitomi)", "kr_name": "오르빗 안타레스(사유리・모니카・히토미)", "type": "stm", "pow": "4234", "tec": "3586", "stm": "5222", "apl": "200", "skill1": "不動のレシーブB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/4/28", "resell": "2022/11/29", "break": "1", "special_fun": ""
  },
  {
    "id": "639_3", "girl": "sayuri", "name": "オービット・アンタレス(さゆり)", "zhs_name": "轨道・心宿二(小百合・莫妮卡・瞳)", "zht_name": "", "en_name": "Orbit Antares (Sayuri・monica・hitomi)", "kr_name": "오르빗 안타레스(사유리・모니카・히토미)", "type": "stm", "pow": "4234", "tec": "3586", "stm": "5222", "apl": "200", "skill1": "不動のレシーブB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/4/28", "resell": "2022/11/29", "break": "1", "special_fun": ""
  },
  {
    "id": "640_1", "girl": "helena", "name": "オービット・シリウス(エレナ)", "zhs_name": "轨道・天狼星(海莲娜・环)", "zht_name": "", "en_name": "Orbit Sirius (Helena・tamaki)", "kr_name": "오르빗 시리우스(엘레나・타마키)", "type": "stm", "pow": "4234", "tec": "3586", "stm": "5222", "apl": "200", "skill1": "不動のレシーブB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/4/28", "resell": "2022/11/29", "break": "1", "special_fun": ""
  },
  {
    "id": "640_2", "girl": "tamaki", "name": "オービット・シリウス(たまき)", "zhs_name": "轨道・天狼星(海莲娜・环)", "zht_name": "", "en_name": "Orbit Sirius (Helena・tamaki)", "kr_name": "오르빗 시리우스(엘레나・타마키)", "type": "stm", "pow": "4234", "tec": "3586", "stm": "5222", "apl": "200", "skill1": "不動のレシーブB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/4/28", "resell": "2022/11/29", "break": "1", "special_fun": ""
  },
  {
    "id": "641", "girl": "tina", "name": "バーレスク・クイーン(ティナ)", "zhs_name": "诙谐女王(蒂娜)", "zht_name": "詼諧女王(蒂娜)", "en_name": "Queen of Burlesque (Tina)", "kr_name": "벌레스크 퀸(티나)", "type": "stm", "pow": "4564", "tec": "3356", "stm": "5122", "apl": "200", "skill1": "強烈スパイクD", "skill2": "バーレスクのスタミナ", "skill3": "熱烈なエール", "sell": "2022/4/28", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "642", "girl": "nagisa", "name": "ドルチェ・バナーヌ(なぎさ)", "zhs_name": "甜美·香蕉(凪咲)", "zht_name": "甜美・香蕉(凪咲)", "en_name": "Dolce Banane (Nagisa)", "kr_name": "돌체 바나누(나기사)", "type": "pow", "pow": "5622", "tec": "3874", "stm": "4204", "apl": "200", "skill1": "W・疲れ知らずの猛攻G", "skill2": "バナナのパワー", "skill3": "豪快なスパイク", "sell": "2022/5/5", "resell": "2022/11/4 2023/5/5", "break": "1", "special_fun": ""
  },
  {
    "id": "639_4", "girl": "fiona", "name": "オービット・アンタレス(フィオナ)", "zhs_name": "轨道・心宿二(菲欧娜・筑紫・海咲)", "zht_name": "", "en_name": "Orbit Antares (Fiona・tsukushi・misaki)", "kr_name": "오르빗 안타레스(피오나・츠쿠시・미사키)", "type": "stm", "pow": "4234", "tec": "3586", "stm": "5222", "apl": "200", "skill1": "不動のレシーブB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/5/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "639_5", "girl": "tsukushi", "name": "オービット・アンタレス(つくし)", "zhs_name": "轨道・心宿二(菲欧娜・筑紫・海咲)", "zht_name": "", "en_name": "Orbit Antares (Fiona・tsukushi・misaki)", "kr_name": "오르빗 안타레스(피오나・츠쿠시・미사키)", "type": "stm", "pow": "4234", "tec": "3586", "stm": "5222", "apl": "200", "skill1": "不動のレシーブB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/5/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "640_3", "girl": "ayane", "name": "オービット・シリウス(あやね)", "zhs_name": "轨道・天狼星(绫音・露娜)", "zht_name": "", "en_name": "Orbit Sirius (Ayane・luna)", "kr_name": "오르빗 시리우스(아야네・루나)", "type": "stm", "pow": "4234", "tec": "3586", "stm": "5222", "apl": "200", "skill1": "不動のレシーブB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/5/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "640_4", "girl": "luna", "name": "オービット・シリウス(ルナ)", "zhs_name": "轨道・天狼星(绫音・露娜)", "zht_name": "", "en_name": "Orbit Sirius (Ayane・luna)", "kr_name": "오르빗 시리우스(아야네・루나)", "type": "stm", "pow": "4234", "tec": "3586", "stm": "5222", "apl": "200", "skill1": "不動のレシーブB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/5/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "640_5", "girl": "nanami", "name": "オービット・シリウス(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4234", "tec": "3586", "stm": "5222", "apl": "200", "skill1": "不動のレシーブB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/5/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "643", "girl": "koharu", "name": "けなげなキューピッド(こはる)", "zhs_name": "勇敢丘比特(小春)", "zht_name": "勇敢丘比特(小春)", "en_name": "Heroic Cupid (Koharu)", "kr_name": "기특한 큐피드(코하루)", "type": "pow", "pow": "4992", "tec": "3586", "stm": "4064", "apl": "200", "skill1": "強烈スパイクB", "skill2": "秘められたパワー3", "skill3": "豪快なスパイク", "sell": "2022/5/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "644", "girl": "nagisa", "name": "いたずらキューピッド(なぎさ)", "zhs_name": "淘气丘比特(凪咲)", "zht_name": "淘氣丘比特(凪咲)", "en_name": "Naughty Cupid (Nagisa)", "kr_name": "장난꾸러기 큐피드(나기사)", "type": "pow", "pow": "5102", "tec": "3596", "stm": "4044", "apl": "200", "skill1": "強烈スパイクA", "skill2": "強烈なプレッシャーC", "skill3": "秘められたパワー4", "sell": "2022/5/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "645", "girl": "lobelia", "name": "いたずらキューピッド(ロベリア)", "zhs_name": "淘气丘比特(萝贝莉娅)", "zht_name": "淘氣丘比特(蘿貝莉婭)", "en_name": "Naughty Cupid (Lobelia)", "kr_name": "장난꾸러기 큐피드(로벨리아)", "type": "pow", "pow": "5102", "tec": "3596", "stm": "4044", "apl": "200", "skill1": "強烈スパイクA", "skill2": "強烈なプレッシャーC", "skill3": "秘められたパワー4", "sell": "2022/5/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "646", "girl": "koharu", "name": "旗袍・青龍(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3516", "tec": "5162", "stm": "3964", "apl": "200", "skill1": "高度な心理戦B", "skill2": "閃きのテクニック5", "skill3": "可憐なフェイント", "sell": "2022/5/18", "resell": "2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "647", "girl": "kanna", "name": "旗袍・玄武(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5232", "stm": "4014", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "鉄壁のレシーブD", "skill3": "閃きのテクニック5", "sell": "2022/5/18", "resell": "2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "648", "girl": "monica", "name": "旗袍・玄武(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5232", "stm": "4014", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "鉄壁のレシーブD", "skill3": "閃きのテクニック5", "sell": "2022/5/18", "resell": "2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "649", "girl": "fiona", "name": "旗袍・白虎(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3616", "tec": "4952", "stm": "4174", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "灼熱のダンスC", "skill3": "閃きのテクニック3", "sell": "2022/5/18", "resell": "2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "650", "girl": "elise", "name": "旗袍・白虎(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3616", "tec": "4952", "stm": "4174", "apl": "200", "skill1": "裏の裏を突くフェイントA", "skill2": "灼熱のダンスC", "skill3": "閃きのテクニック3", "sell": "2022/5/18", "resell": "2023/7/27", "break": "0", "special_fun": ""
  },
  {
    "id": "c5", "girl": "all", "name": "国際版第1回水着コンテスト「キュート」", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "none", "pow": "0", "tec": "0", "stm": "0", "apl": "0", "skill1": "", "skill2": "", "skill3": "", "sell": "2022/5/24", "resell": "N/A", "break": "1", "special_fun": "steam第一次服装设计比赛 得奖作品。作为礼包3000付费钻 两件打包销售 仅外形无属性。Design by OGC"
  },
  {
    "id": "c6", "girl": "all", "name": "国際版第1回水着コンテスト「セクシー」", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "none", "pow": "0", "tec": "0", "stm": "0", "apl": "0", "skill1": "", "skill2": "", "skill3": "", "sell": "2022/5/24", "resell": "N/A", "break": "1", "special_fun": "steam第一次服装设计比赛 得奖作品。作为礼包3000付费钻 两件打包销售 仅外形无属性。Design by AKAKO"
  },
  {
    "id": "651_1", "girl": "kasumi", "name": "バニー・クロック(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_2", "girl": "honoka", "name": "バニー・クロック(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_3", "girl": "marie", "name": "バニー・クロック(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_4", "girl": "ayane", "name": "バニー・クロック(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_5", "girl": "nyotengu", "name": "バニー・クロック(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_6", "girl": "kokoro", "name": "バニー・クロック(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_7", "girl": "hitomi", "name": "バニー・クロック(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_8", "girl": "momiji", "name": "バニー・クロック(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_9", "girl": "helena", "name": "バニー・クロック(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_10", "girl": "misaki", "name": "バニー・クロック(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_11", "girl": "luna", "name": "バニー・クロック(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_12", "girl": "tamaki", "name": "バニー・クロック(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_13", "girl": "leifang", "name": "バニー・クロック(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_14", "girl": "fiona", "name": "バニー・クロック(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_15", "girl": "nagisa", "name": "バニー・クロック(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_16", "girl": "kanna", "name": "バニー・クロック(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_17", "girl": "monica", "name": "バニー・クロック(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_18", "girl": "sayuri", "name": "バニー・クロック(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_19", "girl": "patty", "name": "バニー・クロック(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_20", "girl": "tsukushi", "name": "バニー・クロック(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_21", "girl": "lobelia", "name": "バニー・クロック(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_22", "girl": "nanami", "name": "バニー・クロック(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_23", "girl": "elise", "name": "バニー・クロック(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "651_24", "girl": "koharu", "name": "バニー・クロック(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2022/5/24", "resell": "2023/6/1", "break": "1", "special_fun": ""
  },
  {
    "id": "652", "girl": "hitomi", "name": "ドルチェ・バナーヌ(ヒトミ)", "zhs_name": "甜美·香蕉(瞳)", "zht_name": "甜美・香蕉(瞳)", "en_name": "Dolce Banane (Hitomi)", "kr_name": "돌체 바나누(히토미)", "type": "pow", "pow": "5622", "tec": "3894", "stm": "4184", "apl": "200", "skill1": "W・疲れ知らずの猛攻G", "skill2": "バナナのパワー", "skill3": "豪快なスパイク", "sell": "2022/5/25", "resell": "2022/11/4 2023/5/25", "break": "1", "special_fun": ""
  },
  {
    "id": "415_20", "girl": "tsukushi", "name": "エトワールブリエ(つくし)", "zhs_name": "星光闪耀(筑紫)", "zht_name": "群星閃耀(筑紫)", "en_name": "Étoile Briller (Tsukushi)", "kr_name": "에투알 브리에(츠쿠시)", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2022/6/1", "resell": "", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_21", "girl": "lobelia", "name": "エトワールブリエ(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2022/6/1", "resell": "", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "415_22", "girl": "nanami", "name": "エトワールブリエ(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3864", "tec": "4872", "stm": "3856", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "エトワールのテクニック", "skill3": "可憐なフェイント", "sell": "2022/6/1", "resell": "", "break": "1", "special_fun": "游戏3周年庆服装，头饰可隐藏。8步池登场，允许8件换指定的1件。"
  },
  {
    "id": "653", "girl": "koharu", "name": "星砂のスリットワンピ(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2022/6/1", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "654", "girl": "marie", "name": "ドルチェ・チェリー(マリー)", "zhs_name": "甜美·樱桃(玛莉)", "zht_name": "甜美・櫻桃(瑪莉)", "en_name": "Dolce Cherry (Marie)", "kr_name": "돌체 체리(마리)", "type": "tec", "pow": "3854", "tec": "5622", "stm": "4224", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "サクランボのテクニック", "skill3": "可憐なフェイント", "sell": "2022/6/6", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "655_1", "girl": "kasumi", "name": "レイニードロップ(かすみ)", "zhs_name": "雨滴(霞)", "zht_name": "雨滴(霞)", "en_name": "Rainy Drop (Kasumi)", "kr_name": "레이니 드롭(카스미)", "type": "pow", "pow": "5052", "tec": "3486", "stm": "4104", "apl": "200", "skill1": "圧倒的な気迫C", "skill2": "秘められたパワー6", "skill3": "豪快なスパイク", "sell": "2022/6/8", "resell": "2022/11/25 2023/6/15", "break": "1", "special_fun": ""
  },
  {
    "id": "655_2", "girl": "misaki", "name": "レイニードロップ(みさき)", "zhs_name": "雨滴(海咲)", "zht_name": "雨滴(海咲)", "en_name": "Rainy Drop (Misaki)", "kr_name": "레이니 드롭(미사키)", "type": "pow", "pow": "5052", "tec": "3486", "stm": "4104", "apl": "200", "skill1": "圧倒的な気迫C", "skill2": "秘められたパワー6", "skill3": "豪快なスパイク", "sell": "2022/6/8", "resell": "2022/11/25 2023/6/15", "break": "1", "special_fun": ""
  },
  {
    "id": "655_3", "girl": "fiona", "name": "レイニードロップ(フィオナ)", "zhs_name": "雨滴(菲欧娜)", "zht_name": "雨滴(菲歐娜)", "en_name": "Rainy Drop (Fiona)", "kr_name": "레이니 드롭(피오나)", "type": "pow", "pow": "5052", "tec": "3486", "stm": "4104", "apl": "200", "skill1": "圧倒的な気迫C", "skill2": "秘められたパワー6", "skill3": "豪快なスパイク", "sell": "2022/6/8", "resell": "2022/11/25 2023/6/15", "break": "1", "special_fun": ""
  },
  {
    "id": "655_4", "girl": "patty", "name": "レイニードロップ(パティ)", "zhs_name": "雨滴(派蒂)", "zht_name": "雨滴(派蒂)", "en_name": "Rainy Drop (Patty)", "kr_name": "레이니 드롭(패티)", "type": "pow", "pow": "5052", "tec": "3486", "stm": "4104", "apl": "200", "skill1": "圧倒的な気迫C", "skill2": "秘められたパワー6", "skill3": "豪快なスパイク", "sell": "2022/6/8", "resell": "2022/11/25 2023/6/15", "break": "1", "special_fun": ""
  },
  {
    "id": "655_5", "girl": "koharu", "name": "レイニードロップ(こはる)", "zhs_name": "雨滴(小春)", "zht_name": "雨滴(小春)", "en_name": "Rainy Drop (Koharu)", "kr_name": "레이니 드롭(코하루)", "type": "pow", "pow": "5052", "tec": "3486", "stm": "4104", "apl": "200", "skill1": "圧倒的な気迫C", "skill2": "秘められたパワー6", "skill3": "豪快なスパイク", "sell": "2022/6/8", "resell": "2022/11/25 2023/6/15", "break": "1", "special_fun": ""
  },
  {
    "id": "656", "girl": "marie", "name": "まじかるヴィーナス(マリー)", "zhs_name": "魔法维纳斯(玛莉)", "zht_name": "魔法維納斯(瑪莉)", "en_name": "Magical Venus (Marie)", "kr_name": "매지컬 비너스(마리)", "type": "stm", "pow": "4284", "tec": "3596", "stm": "5162", "apl": "200", "skill1": "強烈スパイクD", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/6/16", "resell": "2022/11/28", "break": "1", "special_fun": "附带小道具魔法棒，爆衣时有闪烁效果，头部饰品可设定隐藏。"
  },
  {
    "id": "657", "girl": "honoka", "name": "まじかるヴィーナス(ほのか)", "zhs_name": "魔法维纳斯(穗香)", "zht_name": "魔法維納斯(穗香)", "en_name": "Magical Venus (Honoka)", "kr_name": "매지컬 비너스(호노카)", "type": "stm", "pow": "4174", "tec": "3766", "stm": "5202", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "強烈なプレッシャーC", "skill3": "内から湧き上がるスタミナ6", "sell": "2022/6/16", "resell": "2022/11/28", "break": "1", "special_fun": "附带小道具魔法棒，爆衣时有闪烁效果，头部饰品可设定隐藏。"
  },
  {
    "id": "658", "girl": "nagisa", "name": "まじかるヴィーナス(なぎさ)", "zhs_name": "魔法维纳斯(凪咲)", "zht_name": "魔法維納斯(凪咲)", "en_name": "Magical Venus (Nagisa)", "kr_name": "매지컬 비너스(나기사)", "type": "stm", "pow": "4174", "tec": "3766", "stm": "5202", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "強烈なプレッシャーC", "skill3": "内から湧き上がるスタミナ6", "sell": "2022/6/16", "resell": "2022/11/28", "break": "1", "special_fun": "附带小道具魔法棒，爆衣时有闪烁效果，头部饰品可设定隐藏。"
  },
  {
    "id": "659", "girl": "amy", "name": "ドルチェ・チェリー(エイミー)", "zhs_name": "甜美·樱桃(艾米)", "zht_name": "甜美・櫻桃(愛咪)", "en_name": "Dolce Cherry (Amy)", "kr_name": "돌체 체리(에이미)", "type": "tec", "pow": "3864", "tec": "5622", "stm": "4214", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "サクランボのテクニック", "skill3": "可憐なフェイント", "sell": "2022/6/18", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "660", "girl": "elise", "name": "ジュエル・サファイア(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3316", "tec": "4704", "stm": "5322", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "サファイア・スタミナ", "skill3": "可憐なフェイント", "sell": "2022/6/23", "resell": "2022/9/3", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现粒子效果(光之舞) "
  },
  {
    "id": "661", "girl": "koharu", "name": "ジュエル・ラピスラズリ(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5322", "tec": "3664", "stm": "4214", "apl": "200", "skill1": "強烈スパイクE", "skill2": "ラピスラズリ・パワー", "skill3": "豪快なスパイク", "sell": "2022/6/23", "resell": "2022/12/22", "break": "1", "special_fun": "使用天狗扇 扇动的时候 会出现粒子效果(光之舞) "
  },
  {
    "id": "662", "girl": "kanna", "name": "スイートビターベリー(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5032", "tec": "3536", "stm": "4074", "apl": "200", "skill1": "不動のレシーブE", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2022/6/23", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "663", "girl": "momiji", "name": "スイートミルクベリー(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5102", "tec": "3596", "stm": "4044", "apl": "200", "skill1": "強烈スパイクB", "skill2": "圧倒的な気迫E", "skill3": "秘められたパワー4", "sell": "2022/6/23", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "664", "girl": "misaki", "name": "スイートミルクベリー(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5102", "tec": "3596", "stm": "4044", "apl": "200", "skill1": "強烈スパイクB", "skill2": "圧倒的な気迫E", "skill3": "秘められたパワー4", "sell": "2022/6/23", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "665", "girl": "lobelia", "name": "ドルチェ・チェリー(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3944", "tec": "5622", "stm": "4134", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "サクランボのテクニック", "skill3": "可憐なフェイント", "sell": "2022/6/25", "resell": "2022/11/4 2023/6/25", "break": "1", "special_fun": ""
  },
  {
    "id": "666_1", "girl": "kasumi", "name": "アリスギア・プラチナライン(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_2", "girl": "honoka", "name": "アリスギア・プラチナライン(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_3", "girl": "marie", "name": "アリスギア・プラチナライン(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_4", "girl": "ayane", "name": "アリスギア・プラチナライン(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_5", "girl": "nyotengu", "name": "アリスギア・プラチナライン(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_6", "girl": "kokoro", "name": "アリスギア・プラチナライン(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_7", "girl": "hitomi", "name": "アリスギア・プラチナライン(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_8", "girl": "momiji", "name": "アリスギア・プラチナライン(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_9", "girl": "helena", "name": "アリスギア・プラチナライン(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_10", "girl": "misaki", "name": "アリスギア・プラチナライン(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_11", "girl": "luna", "name": "アリスギア・プラチナライン(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_12", "girl": "tamaki", "name": "アリスギア・プラチナライン(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_13", "girl": "leifang", "name": "アリスギア・プラチナライン(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_14", "girl": "fiona", "name": "アリスギア・プラチナライン(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_15", "girl": "nagisa", "name": "アリスギア・プラチナライン(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_16", "girl": "kanna", "name": "アリスギア・プラチナライン(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_17", "girl": "monica", "name": "アリスギア・プラチナライン(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_18", "girl": "sayuri", "name": "アリスギア・プラチナライン(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_19", "girl": "patty", "name": "アリスギア・プラチナライン(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_20", "girl": "tsukushi", "name": "アリスギア・プラチナライン(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_21", "girl": "lobelia", "name": "アリスギア・プラチナライン(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_22", "girl": "nanami", "name": "アリスギア・プラチナライン(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_23", "girl": "elise", "name": "アリスギア・プラチナライン(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "666_24", "girl": "koharu", "name": "アリスギア・プラチナライン(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5142", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "驚異のスタミナC", "skill3": "プラチナラインのテクニック", "sell": "2022/6/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "667_1", "girl": "patty", "name": "アリスギア・バーラタCS(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3586", "tec": "4334", "stm": "5122", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "バーラタCSのスタミナ", "skill3": "熱烈なエール", "sell": "2022/7/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "667_2", "girl": "koharu", "name": "アリスギア・バーラタCS(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3586", "tec": "4334", "stm": "5122", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "バーラタCSのスタミナ", "skill3": "熱烈なエール", "sell": "2022/7/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "667_3", "girl": "lobelia", "name": "アリスギア・バーラタCS(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3586", "tec": "4334", "stm": "5122", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "バーラタCSのスタミナ", "skill3": "熱烈なエール", "sell": "2022/7/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "668_1", "girl": "elise", "name": "アリスギア・明鏡止水CS(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3596", "tec": "4274", "stm": "5172", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "明鏡止水CSのスタミナ", "skill3": "熱烈なエール", "sell": "2022/7/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "668_2", "girl": "nanami", "name": "アリスギア・明鏡止水CS(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3596", "tec": "4274", "stm": "5172", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "明鏡止水CSのスタミナ", "skill3": "熱烈なエール", "sell": "2022/7/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "668_3", "girl": "tsukushi", "name": "アリスギア・明鏡止水CS(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3596", "tec": "4274", "stm": "5172", "apl": "200", "skill1": "灼熱のダンスC", "skill2": "明鏡止水CSのスタミナ", "skill3": "熱烈なエール", "sell": "2022/7/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "669", "girl": "misaki", "name": "ドルチェ・パイン(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3964", "stm": "4114", "apl": "200", "skill1": "W・疲れ知らずの猛攻G", "skill2": "パイナップルのパワー", "skill3": "豪快なスパイク", "sell": "2022/7/7", "resell": "2022/11/4 2023/7/7", "break": "1", "special_fun": ""
  },
  {
    "id": "670", "girl": "nyotengu", "name": "プランタン・ロゼ(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3496", "tec": "5132", "stm": "4014", "apl": "200", "skill1": "鉄壁のレシーブB", "skill2": "閃きのテクニック6", "skill3": "熱烈なエール", "sell": "2022/7/14", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "671", "girl": "helena", "name": "プランタン・ロゼ(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3576", "tec": "5082", "stm": "4084", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "灼熱のダンスC", "skill3": "閃きのテクニック3", "sell": "2022/7/14", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "672", "girl": "amy", "name": "メイデン・コード(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3626", "tec": "4304", "stm": "5112", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "メイデンのスタミナ", "skill3": "熱烈なエール", "sell": "2022/7/14", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "673_1", "girl": "kokoro", "name": "なみうちマリン(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3536", "tec": "4304", "stm": "5202", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2022/7/21", "resell": "2022/11/27", "break": "1", "special_fun": ""
  },
  {
    "id": "673_2", "girl": "leifang", "name": "なみうちマリン(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3666", "tec": "4254", "stm": "5222", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "灼熱のダンスC", "skill3": "内から湧き上がるスタミナ4", "sell": "2022/7/21", "resell": "2022/11/27", "break": "1", "special_fun": ""
  },
  {
    "id": "673_3", "girl": "koharu", "name": "なみうちマリン(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3666", "tec": "4254", "stm": "5222", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "灼熱のダンスC", "skill3": "内から湧き上がるスタミナ4", "sell": "2022/7/21", "resell": "2022/11/27", "break": "1", "special_fun": ""
  },
  {
    "id": "674_1", "girl": "honoka", "name": "ロコモコ・バケーション(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5142", "tec": "3456", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/7/28", "resell": "", "break": "1", "special_fun": "附带小道具【尤克里里】，3种彩绘皮肤贴纸"
  },
  {
    "id": "674_2", "girl": "hitomi", "name": "ロコモコ・バケーション(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5142", "tec": "3456", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/7/28", "resell": "", "break": "1", "special_fun": "附带小道具【尤克里里】，3种彩绘皮肤贴纸"
  },
  {
    "id": "674_3", "girl": "misaki", "name": "ロコモコ・バケーション(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5142", "tec": "3456", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/7/28", "resell": "", "break": "1", "special_fun": "附带小道具【尤克里里】，3种彩绘皮肤贴纸"
  },
  {
    "id": "674_4", "girl": "tamaki", "name": "ロコモコ・バケーション(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5142", "tec": "3456", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/7/28", "resell": "", "break": "1", "special_fun": "附带小道具【尤克里里】，3种彩绘皮肤贴纸"
  },
  {
    "id": "674_5", "girl": "sayuri", "name": "ロコモコ・バケーション(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5142", "tec": "3456", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/7/28", "resell": "", "break": "1", "special_fun": "附带小道具【尤克里里】，3种彩绘皮肤贴纸"
  },
  {
    "id": "675", "girl": "patty", "name": "ドルチェ・パイン(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3944", "stm": "4134", "apl": "200", "skill1": "W・疲れ知らずの猛攻G", "skill2": "パイナップルのパワー", "skill3": "豪快なスパイク", "sell": "2022/7/31", "resell": "2022/11/4 2023/7/31", "break": "1", "special_fun": ""
  },
  {
    "id": "674_6", "girl": "luna", "name": "ロコモコ・バケーション(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5142", "tec": "3456", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/8/4", "resell": "", "break": "1", "special_fun": "附带小道具【尤克里里】，3种彩绘皮肤贴纸"
  },
  {
    "id": "674_7", "girl": "monica", "name": "ロコモコ・バケーション(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5142", "tec": "3456", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/8/4", "resell": "", "break": "1", "special_fun": "附带小道具【尤克里里】，3种彩绘皮肤贴纸"
  },
  {
    "id": "674_8", "girl": "patty", "name": "ロコモコ・バケーション(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5142", "tec": "3456", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/8/4", "resell": "", "break": "1", "special_fun": "附带小道具【尤克里里】，3种彩绘皮肤贴纸"
  },
  {
    "id": "674_9", "girl": "nanami", "name": "ロコモコ・バケーション(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5142", "tec": "3456", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/8/4", "resell": "", "break": "1", "special_fun": "附带小道具【尤克里里】，3种彩绘皮肤贴纸"
  },
  {
    "id": "674_10", "girl": "elise", "name": "ロコモコ・バケーション(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5142", "tec": "3456", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/8/4", "resell": "", "break": "1", "special_fun": "附带小道具【尤克里里】，3种彩绘皮肤贴纸"
  },
  {
    "id": "676", "girl": "ayane", "name": "ドルチェ・ピーチ(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3914", "tec": "5622", "stm": "4164", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "モモのテクニック", "skill3": "可憐なフェイント", "sell": "2022/8/5", "resell": "2022/11/4 2023/8/5", "break": "1", "special_fun": ""
  },
  {
    "id": "677_1", "girl": "marie", "name": "ほうかごペンギン(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4254", "tec": "3606", "stm": "5182", "apl": "200", "skill1": "強烈スパイクD", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2022/8/10", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "677_2", "girl": "fiona", "name": "ほうかごペンギン(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4254", "tec": "3606", "stm": "5182", "apl": "200", "skill1": "強烈スパイクD", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2022/8/10", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "677_3", "girl": "kanna", "name": "ほうかごペンギン(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4254", "tec": "3606", "stm": "5182", "apl": "200", "skill1": "強烈スパイクD", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2022/8/10", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "677_4", "girl": "lobelia", "name": "ほうかごペンギン(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4254", "tec": "3606", "stm": "5182", "apl": "200", "skill1": "強烈スパイクD", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2022/8/10", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "677_5", "girl": "koharu", "name": "ほうかごペンギン(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4254", "tec": "3606", "stm": "5182", "apl": "200", "skill1": "強烈スパイクD", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2022/8/10", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "623_6", "girl": "tina", "name": "はじけるラヴァー(ティナ)", "zhs_name": "奔放的恋人(蒂娜)", "zht_name": "奔放戀人(蒂娜)", "en_name": "Bursting Lover (Tina)", "kr_name": "팝핑 러버(티나)", "type": "apl", "pow": "4596", "tec": "3676", "stm": "4154", "apl": "550", "skill1": "圧倒的な気迫C", "skill2": "隠しきれない魅力5", "skill3": "豪快なスパイク", "sell": "2022/8/18", "resell": "2022/11/27", "break": "1", "special_fun": ""
  },
  {
    "id": "623_7", "girl": "sayuri", "name": "はじけるラヴァー(さゆり)", "zhs_name": "奔放的恋人(小百合)", "zht_name": "奔放戀人(小百合)", "en_name": "Bursting Lover (Sayuri)", "kr_name": "팝핑 러버(사유리)", "type": "apl", "pow": "4676", "tec": "3626", "stm": "4244", "apl": "550", "skill1": "強烈スパイクD", "skill2": "強烈なプレッシャーE", "skill3": "隠しきれない魅力4", "sell": "2022/8/18", "resell": "2022/11/27", "break": "1", "special_fun": ""
  },
  {
    "id": "623_8", "girl": "nanami", "name": "はじけるラヴァー(ななみ)", "zhs_name": "奔放的恋人(七海)", "zht_name": "奔放戀人(七海)", "en_name": "Bursting Lover (Nanami)", "kr_name": "팝핑 러버(나나미)", "type": "apl", "pow": "4676", "tec": "3626", "stm": "4244", "apl": "550", "skill1": "強烈スパイクD", "skill2": "強烈なプレッシャーE", "skill3": "隠しきれない魅力4", "sell": "2022/8/18", "resell": "2022/11/27", "break": "1", "special_fun": ""
  },
  {
    "id": "678", "girl": "tamaki", "name": "ドルチェ・ピーチ(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3974", "stm": "4104", "apl": "200", "skill1": "W・疲れ知らずの猛攻G", "skill2": "モモのパワー", "skill3": "豪快なスパイク", "sell": "2022/8/19", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "679", "girl": "shandy", "name": "キッス・イン・ザ・ダーク(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3406", "stm": "4154", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫C", "skill3": "秘められたパワー4", "sell": "2022/8/24", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "680", "girl": "kasumi", "name": "ブルーハワイ(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5012", "tec": "3456", "stm": "4174", "apl": "200", "skill1": "灼熱のダンスD", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/8/25", "resell": "2023/7/20", "break": "1", "special_fun": ""
  },
  {
    "id": "681", "girl": "fiona", "name": "ピーチシロップ(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5102", "tec": "3556", "stm": "4084", "apl": "200", "skill1": "強烈スパイクB", "skill2": "不動のレシーブC", "skill3": "秘められたパワー4", "sell": "2022/8/25", "resell": "2023/7/20", "break": "1", "special_fun": ""
  },
  {
    "id": "682", "girl": "tina", "name": "深紅のスリットワンピ(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2022/9/1", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "548_4", "girl": "ayane", "name": "たまゆら花火(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4344", "tec": "3556", "stm": "5142", "apl": "200", "skill1": "圧倒的な気迫D", "skill2": "内から湧き上がるスタミナ3", "skill3": "豪快なスパイク", "sell": "2022/9/1", "resell": "2022/11/28 2023/7/20", "break": "1", "special_fun": ""
  },
  {
    "id": "548_5", "girl": "monica", "name": "たまゆら花火(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4414", "tec": "3616", "stm": "5112", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "強烈スパイクC", "skill3": "内から湧き上がるスタミナ6", "sell": "2022/9/1", "resell": "2022/11/28 2023/7/20", "break": "1", "special_fun": ""
  },
  {
    "id": "548_6", "girl": "tsukushi", "name": "たまゆら花火(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4414", "tec": "3616", "stm": "5112", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "強烈スパイクC", "skill3": "内から湧き上がるスタミナ6", "sell": "2022/9/1", "resell": "2022/11/28 2023/7/20", "break": "1", "special_fun": ""
  },
  {
    "id": "683", "girl": "elise", "name": "ドルチェ・レザン(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3844", "tec": "5622", "stm": "4234", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "ブドウのテクニック", "skill3": "可憐なフェイント", "sell": "2022/9/3", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "529_6", "girl": "momiji", "name": "スイートスポット(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3516", "tec": "5142", "stm": "3984", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "閃きのテクニック6", "skill3": "熱烈なエール", "sell": "2022/9/8", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "529_7", "girl": "nyotengu", "name": "スイートスポット(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3546", "tec": "5052", "stm": "4144", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "天才的な先読みE", "skill3": "閃きのテクニック3", "sell": "2022/9/8", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "529_8", "girl": "luna", "name": "スイートスポット(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3546", "tec": "5052", "stm": "4144", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "天才的な先読みE", "skill3": "閃きのテクニック3", "sell": "2022/9/8", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "684", "girl": "elise", "name": "ステラ・ウィルゴ(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3456", "tec": "5322", "stm": "4164", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "ウィルゴ・テクニック", "skill3": "可憐なフェイント", "sell": "2022/9/8", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "685", "girl": "koharu", "name": "ステラ・カプリコーン(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4374", "tec": "3646", "stm": "5322", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "カプリコーン・スタミナ", "skill3": "豪快なスパイク", "sell": "2022/9/8", "resell": "2022/12/22", "break": "1", "special_fun": ""
  },
  {
    "id": "686", "girl": "kanna", "name": "ドルチェ・レザン(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3984", "stm": "4094", "apl": "200", "skill1": "W・疲れ知らずの猛攻G", "skill2": "ブドウのパワー", "skill3": "豪快なスパイク", "sell": "2022/9/15", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "687_1", "girl": "kasumi", "name": "ツール・ド・ヴィーナス(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3516", "tec": "5102", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "ペダリングのテクニック", "skill3": "可憐なフェイント", "sell": "2022/9/18", "resell": "", "break": "1", "special_fun": "附带大道具【动感单车】，会随时间湿身,允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "687_2", "girl": "marie", "name": "ツール・ド・ヴィーナス(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3516", "tec": "5102", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "ペダリングのテクニック", "skill3": "可憐なフェイント", "sell": "2022/9/18", "resell": "", "break": "1", "special_fun": "附带大道具【动感单车】，会随时间湿身,允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "687_3", "girl": "hitomi", "name": "ツール・ド・ヴィーナス(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3516", "tec": "5102", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "ペダリングのテクニック", "skill3": "可憐なフェイント", "sell": "2022/9/18", "resell": "", "break": "1", "special_fun": "附带大道具【动感单车】，会随时间湿身,允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "687_4", "girl": "misaki", "name": "ツール・ド・ヴィーナス(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3516", "tec": "5102", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "ペダリングのテクニック", "skill3": "可憐なフェイント", "sell": "2022/9/18", "resell": "", "break": "1", "special_fun": "附带大道具【动感单车】，会随时间湿身,允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "687_5", "girl": "tamaki", "name": "ツール・ド・ヴィーナス(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3516", "tec": "5102", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "ペダリングのテクニック", "skill3": "可憐なフェイント", "sell": "2022/9/18", "resell": "", "break": "1", "special_fun": "附带大道具【动感单车】，会随时间湿身,允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "687_6", "girl": "nagisa", "name": "ツール・ド・ヴィーナス(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3516", "tec": "5102", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "ペダリングのテクニック", "skill3": "可憐なフェイント", "sell": "2022/9/18", "resell": "", "break": "1", "special_fun": "附带大道具【动感单车】，会随时间湿身,允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "687_7", "girl": "monica", "name": "ツール・ド・ヴィーナス(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3516", "tec": "5102", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "ペダリングのテクニック", "skill3": "可憐なフェイント", "sell": "2022/9/18", "resell": "", "break": "1", "special_fun": "附带大道具【动感单车】，会随时间湿身,允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "687_8", "girl": "patty", "name": "ツール・ド・ヴィーナス(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3516", "tec": "5102", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "ペダリングのテクニック", "skill3": "可憐なフェイント", "sell": "2022/9/18", "resell": "", "break": "1", "special_fun": "附带大道具【动感单车】，会随时间湿身,允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "687_9", "girl": "nanami", "name": "ツール・ド・ヴィーナス(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3516", "tec": "5102", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "ペダリングのテクニック", "skill3": "可憐なフェイント", "sell": "2022/9/18", "resell": "", "break": "1", "special_fun": "附带大道具【动感单车】，会随时间湿身,允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "687_10", "girl": "tina", "name": "ツール・ド・ヴィーナス(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3516", "tec": "5102", "stm": "4024", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "ペダリングのテクニック", "skill3": "可憐なフェイント", "sell": "2022/9/18", "resell": "", "break": "1", "special_fun": "附带大道具【动感单车】，会随时间湿身,允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "688", "girl": "momiji", "name": "ドルチェ・レザン(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3954", "tec": "5622", "stm": "4124", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "ブドウのテクニック", "skill3": "可憐なフェイント", "sell": "2022/9/20", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "689", "girl": "leifang", "name": "うすかわたけのこ(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5102", "tec": "3436", "stm": "4104", "apl": "200", "skill1": "圧倒的な気迫B", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/9/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "690", "girl": "koharu", "name": "うすかわたけのこ(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5052", "tec": "3516", "stm": "4174", "apl": "200", "skill1": "強烈スパイクC", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー4", "sell": "2022/9/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "691", "girl": "shandy", "name": "エックス・ワイ・ズィー(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4274", "tec": "3616", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "X・Y・Zのスタミナ", "skill3": "熱烈なエール", "sell": "2022/9/29", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "692_1", "girl": "kokoro", "name": "オープンユアハート(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4274", "tec": "3526", "stm": "5242", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/10/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "692_2", "girl": "honoka", "name": "オープンユアハート(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4374", "tec": "3606", "stm": "5162", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "圧倒的な気迫B", "skill3": "内から湧き上がるスタミナ4", "sell": "2022/10/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "692_3", "girl": "sayuri", "name": "オープンユアハート(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4374", "tec": "3606", "stm": "5162", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "圧倒的な気迫B", "skill3": "内から湧き上がるスタミナ4", "sell": "2022/10/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "693", "girl": "amy", "name": "クロックワーク(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3506", "tec": "5162", "stm": "3974", "apl": "200", "skill1": "裏の裏を突くフェイントB", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2022/10/13", "resell": "2022/11/26", "break": "1", "special_fun": ""
  },
  {
    "id": "694", "girl": "momiji", "name": "クロックワーク(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3566", "tec": "5102", "stm": "4074", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "鉄壁のレシーブB", "skill3": "閃きのテクニック5", "sell": "2022/10/13", "resell": "2022/11/26", "break": "1", "special_fun": ""
  },
  {
    "id": "695", "girl": "fiona", "name": "クロックワーク(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3566", "tec": "5102", "stm": "4074", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "鉄壁のレシーブB", "skill3": "閃きのテクニック5", "sell": "2022/10/13", "resell": "2022/11/26", "break": "1", "special_fun": ""
  },
  {
    "id": "696", "girl": "luna", "name": "ドルチェ・マローネ(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3954", "stm": "4124", "apl": "200", "skill1": "W・疲れ知らずの猛攻G", "skill2": "マロンのパワー", "skill3": "豪快なスパイク", "sell": "2022/10/15", "resell": "2022/11/4", "break": "1", "special_fun": ""
  },
  {
    "id": "697_1", "girl": "kasumi", "name": "レディ・ファンタズマ(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_2", "girl": "honoka", "name": "レディ・ファンタズマ(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_3", "girl": "marie", "name": "レディ・ファンタズマ(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_4", "girl": "ayane", "name": "レディ・ファンタズマ(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_5", "girl": "nyotengu", "name": "レディ・ファンタズマ(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_6", "girl": "kokoro", "name": "レディ・ファンタズマ(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_7", "girl": "hitomi", "name": "レディ・ファンタズマ(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_8", "girl": "momiji", "name": "レディ・ファンタズマ(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_9", "girl": "helena", "name": "レディ・ファンタズマ(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_10", "girl": "misaki", "name": "レディ・ファンタズマ(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_11", "girl": "luna", "name": "レディ・ファンタズマ(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_12", "girl": "tamaki", "name": "レディ・ファンタズマ(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_13", "girl": "leifang", "name": "レディ・ファンタズマ(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_14", "girl": "fiona", "name": "レディ・ファンタズマ(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_15", "girl": "nagisa", "name": "レディ・ファンタズマ(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_16", "girl": "kanna", "name": "レディ・ファンタズマ(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_17", "girl": "monica", "name": "レディ・ファンタズマ(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_18", "girl": "sayuri", "name": "レディ・ファンタズマ(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_19", "girl": "patty", "name": "レディ・ファンタズマ(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_20", "girl": "tsukushi", "name": "レディ・ファンタズマ(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_21", "girl": "lobelia", "name": "レディ・ファンタズマ(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_22", "girl": "nanami", "name": "レディ・ファンタズマ(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_23", "girl": "elise", "name": "レディ・ファンタズマ(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_24", "girl": "koharu", "name": "レディ・ファンタズマ(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_25", "girl": "tina", "name": "レディ・ファンタズマ(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "697_26", "girl": "amy", "name": "レディ・ファンタズマ(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5042", "tec": "3486", "stm": "4114", "apl": "200", "skill1": "強烈スパイクD", "skill2": "幻影のパワー", "skill3": "熱烈なエール", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": "附带大道具【哥特式黑色雨伞】,允许和本次的所有服装互相成为狗粮素材满觉。万圣节美术组终于想起来自己还有份工作。"
  },
  {
    "id": "698", "girl": "shandy", "name": "桂花陳酒(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5212", "tec": "3416", "stm": "4014", "apl": "200", "skill1": "強烈スパイクE", "skill2": "桂花のパワー", "skill3": "豪快なスパイク", "sell": "2022/10/20", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "699", "girl": "tsukushi", "name": "ドルチェ・マローネ(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3824", "tec": "5622", "stm": "4254", "apl": "200", "skill1": "W・洗練された技巧G", "skill2": "マロンのテクニック", "skill3": "可憐なフェイント", "sell": "2022/10/24", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "558_13", "girl": "hitomi", "name": "月影(ヒトミ)", "zhs_name": "月下魅影(瞳)", "zht_name": "月下魅影(瞳)", "en_name": "Moonlight Shadow (Hitomi)", "kr_name": "월영(히토미)", "type": "stm", "pow": "4434", "tec": "3536", "stm": "5072", "apl": "200", "skill1": "強烈スパイクC", "skill2": "月影のスタミナ", "skill3": "豪快なスパイク", "sell": "2022/10/27", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "558_14", "girl": "helena", "name": "月影(エレナ)", "zhs_name": "月下魅影(海莲娜)", "zht_name": "月下魅影(海蓮娜)", "en_name": "Moonlight Shadow (Helena)", "kr_name": "월영(엘레나)", "type": "stm", "pow": "4434", "tec": "3536", "stm": "5072", "apl": "200", "skill1": "強烈スパイクC", "skill2": "月影のスタミナ", "skill3": "豪快なスパイク", "sell": "2022/10/27", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "558_15", "girl": "nagisa", "name": "月影(なぎさ)", "zhs_name": "月下魅影(凪咲)", "zht_name": "月下魅影(凪咲)", "en_name": "Moonlight Shadow (Nagisa)", "kr_name": "월영(나기사)", "type": "stm", "pow": "4434", "tec": "3536", "stm": "5072", "apl": "200", "skill1": "強烈スパイクC", "skill2": "月影のスタミナ", "skill3": "豪快なスパイク", "sell": "2022/10/27", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "700", "girl": "amy", "name": "純白のスリットワンピ(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2022/11/1", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "701", "girl": "kanna", "name": "シャノワール(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4344", "tec": "3586", "stm": "5112", "apl": "200", "skill1": "不動のレシーブB", "skill2": "内から湧き上がるスタミナ5", "skill3": "熱烈なエール", "sell": "2022/11/4", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "702", "girl": "lobelia", "name": "シャノワール(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4234", "tec": "3686", "stm": "5222", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "強烈スパイクE", "skill3": "内から湧き上がるスタミナ3", "sell": "2022/11/4", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "703", "girl": "nyotengu", "name": "シークレット・レポート(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5152", "tec": "3616", "stm": "3974", "apl": "200", "skill1": "圧倒的な気迫D", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2022/11/10", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "704", "girl": "marie", "name": "シークレット・レポート(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5152", "tec": "3616", "stm": "3974", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫E", "skill3": "秘められたパワー3", "sell": "2022/11/10", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "705", "girl": "tamaki", "name": "シークレット・レポート(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5152", "tec": "3616", "stm": "3974", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫E", "skill3": "秘められたパワー3", "sell": "2022/11/10", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "706_1", "girl": "kasumi", "name": "デア・マリーナ(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_2", "girl": "honoka", "name": "デア・マリーナ(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_3", "girl": "marie", "name": "デア・マリーナ(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_4", "girl": "ayane", "name": "デア・マリーナ(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_5", "girl": "nyotengu", "name": "デア・マリーナ(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_6", "girl": "kokoro", "name": "デア・マリーナ(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_7", "girl": "hitomi", "name": "デア・マリーナ(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_8", "girl": "momiji", "name": "デア・マリーナ(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_9", "girl": "helena", "name": "デア・マリーナ(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_10", "girl": "misaki", "name": "デア・マリーナ(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_11", "girl": "luna", "name": "デア・マリーナ(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_12", "girl": "tamaki", "name": "デア・マリーナ(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_13", "girl": "leifang", "name": "デア・マリーナ(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_14", "girl": "fiona", "name": "デア・マリーナ(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_15", "girl": "nagisa", "name": "デア・マリーナ(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_16", "girl": "kanna", "name": "デア・マリーナ(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_17", "girl": "monica", "name": "デア・マリーナ(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_18", "girl": "sayuri", "name": "デア・マリーナ(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_19", "girl": "patty", "name": "デア・マリーナ(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_20", "girl": "tsukushi", "name": "デア・マリーナ(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_21", "girl": "lobelia", "name": "デア・マリーナ(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_22", "girl": "nanami", "name": "デア・マリーナ(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_23", "girl": "elise", "name": "デア・マリーナ(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_24", "girl": "koharu", "name": "デア・マリーナ(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_25", "girl": "tina", "name": "デア・マリーナ(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "706_26", "girl": "amy", "name": "デア・マリーナ(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5032", "stm": "4134", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "デア・マリーナのテクニック", "skill3": "可憐なフェイント", "sell": "2022/11/16", "resell": "", "break": "1", "special_fun": "附带金色羽毛飘落效果,5周年庆服装。"
  },
  {
    "id": "707", "girl": "nyotengu", "name": "メイクアップ・シャルキー(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "4004", "stm": "4074", "apl": "200", "skill1": "強烈スパイクH", "skill2": "シャルキーのパワー&スタミナ", "skill3": "豪快なスパイク", "sell": "2022/11/19", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "574_23", "girl": "elise", "name": "화조풍월(엘리제)(エリーゼ)", "zhs_name": "화조풍월(호노카)", "zht_name": "花鳥風月(伊莉丝)", "en_name": "Beauty of Nature (Elise)", "kr_name": "화조풍월(엘리제)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2022/11/22", "resell": "", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_24", "girl": "koharu", "name": "花鳥風月(こはる)", "zhs_name": "花鸟风月(小春)", "zht_name": "花鳥風月(小春)", "en_name": "Beauty of Nature (Koharu)", "kr_name": "화조풍월(코하루)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2022/11/22", "resell": "", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_25", "girl": "tina", "name": "花鳥風月(ティナ)", "zhs_name": "花鸟风月(蒂娜)", "zht_name": "花鳥風月(蒂娜)", "en_name": "Beauty of Nature (Tina)", "kr_name": "화조풍월(티나)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2022/11/22", "resell": "", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "574_26", "girl": "amy", "name": "花鳥風月(エイミー)", "zhs_name": "花鸟风月(艾米)", "zht_name": "花鳥風月(愛咪)", "en_name": "Beauty of Nature (Amy)", "kr_name": "화조풍월(에이미)", "type": "pow", "pow": "4992", "tec": "3506", "stm": "4144", "apl": "200", "skill1": "強烈スパイクD", "skill2": "花鳥風月のパワー", "skill3": "豪快なスパイク", "sell": "2022/11/22", "resell": "", "break": "1", "special_fun": "4周年庆服装"
  },
  {
    "id": "708", "girl": "ayane", "name": "秋麗のスクールウェア(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5062", "tec": "3536", "stm": "4044", "apl": "200", "skill1": "強烈なプレッシャーC", "skill2": "秘められたパワー4", "skill3": "熱烈なエール", "sell": "2022/11/30", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "709", "girl": "koharu", "name": "秋麗のスクールウェア(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "4972", "tec": "3536", "stm": "4234", "apl": "200", "skill1": "強烈スパイクB", "skill2": "強烈なプレッシャーE", "skill3": "秘められたパワー6", "sell": "2022/11/30", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "710", "girl": "amy", "name": "秋麗のスクールウェア(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5032", "tec": "3616", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "強烈なプレッシャーE", "skill3": "秘められたパワー6", "sell": "2022/11/30", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "711", "girl": "misaki", "name": "ブリリアント・スター(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5122", "tec": "3426", "stm": "4094", "apl": "200", "skill1": "強烈スパイクE", "skill2": "綺羅星のスタミナ", "skill3": "熱烈なエール", "sell": "2022/11/30", "resell": "", "break": "1", "special_fun": "第5年True color系列氪金衣服。初回抽取10连解锁女神石板付费路线。"
  },
  {
    "id": "712", "girl": "kokoro", "name": "メイクアップ・サポーネ(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3954", "stm": "4124", "apl": "200", "skill1": "強烈スパイクH", "skill2": "サポーネのパワー&スタミナ", "skill3": "豪快なスパイク", "sell": "2022/12/1", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "713", "girl": "tina", "name": "メイクアップ・サポーネ(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3894", "stm": "4184", "apl": "200", "skill1": "強烈スパイクH", "skill2": "サポーネのパワー&スタミナ", "skill3": "豪快なスパイク", "sell": "2022/12/6", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "714", "girl": "lobelia", "name": "トワイライトフィッシュ(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4324", "tec": "3576", "stm": "5142", "apl": "200", "skill1": "不動のレシーブE", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2022/12/8", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "715", "girl": "patty", "name": "サンセットフィッシュ(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4444", "tec": "3646", "stm": "5052", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "圧倒的な気迫C", "skill3": "内から湧き上がるスタミナ3", "sell": "2022/12/8", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "716", "girl": "nanami", "name": "サンセットフィッシュ(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4444", "tec": "3646", "stm": "5052", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "圧倒的な気迫C", "skill3": "内から湧き上がるスタミナ3", "sell": "2022/12/8", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "717_1", "girl": "kasumi", "name": "レインディア・ギフト(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_2", "girl": "honoka", "name": "レインディア・ギフト(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_3", "girl": "marie", "name": "レインディア・ギフト(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_4", "girl": "ayane", "name": "レインディア・ギフト(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_5", "girl": "nyotengu", "name": "レインディア・ギフト(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_6", "girl": "kokoro", "name": "レインディア・ギフト(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_7", "girl": "hitomi", "name": "レインディア・ギフト(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_8", "girl": "momiji", "name": "レインディア・ギフト(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_9", "girl": "helena", "name": "レインディア・ギフト(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_10", "girl": "misaki", "name": "レインディア・ギフト(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_11", "girl": "luna", "name": "レインディア・ギフト(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_12", "girl": "tamaki", "name": "レインディア・ギフト(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_13", "girl": "leifang", "name": "レインディア・ギフト(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_14", "girl": "fiona", "name": "レインディア・ギフト(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_15", "girl": "nagisa", "name": "レインディア・ギフト(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_16", "girl": "kanna", "name": "レインディア・ギフト(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_17", "girl": "monica", "name": "レインディア・ギフト(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_18", "girl": "sayuri", "name": "レインディア・ギフト(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_19", "girl": "patty", "name": "レインディア・ギフト(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_20", "girl": "tsukushi", "name": "レインディア・ギフト(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_21", "girl": "lobelia", "name": "レインディア・ギフト(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_22", "girl": "nanami", "name": "レインディア・ギフト(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_23", "girl": "elise", "name": "レインディア・ギフト(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_24", "girl": "koharu", "name": "レインディア・ギフト(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_25", "girl": "tina", "name": "レインディア・ギフト(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "717_26", "girl": "amy", "name": "レインディア・ギフト(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3606", "tec": "4274", "stm": "5162", "apl": "200", "skill1": "鉄壁のレシーブC", "skill2": "レインディアのスタミナ", "skill3": "熱烈なエール", "sell": "2022/12/15", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。"
  },
  {
    "id": "586_23", "girl": "elise", "name": "ルミナス・ベル(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2022/12/21", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "586_24", "girl": "tina", "name": "ルミナス・ベル(ティナ)", "zhs_name": "发光铃铛(蒂娜)", "zht_name": "光輝之鐘(蒂娜)", "en_name": "Luminous Bell (Tina)", "kr_name": "루미너스 벨(티나)", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2022/12/21", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "586_25", "girl": "amy", "name": "ルミナス・ベル(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3536", "tec": "5082", "stm": "4024", "apl": "200", "skill1": "高度な心理戦E", "skill2": "ルミナスのテクニック", "skill3": "可憐なフェイント", "sell": "2022/12/21", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "718", "girl": "koharu", "name": "メイクアップ・サポーネ(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3974", "stm": "4104", "apl": "200", "skill1": "強烈スパイクH", "skill2": "サポーネのパワー&スタミナ", "skill3": "豪快なスパイク", "sell": "2022/12/22", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "719_1", "girl": "nyotengu", "name": "暁光の錦(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4354", "tec": "3566", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2022/12/28", "resell": "", "break": "1", "special_fun": "附带小道具【金扇子】。"
  },
  {
    "id": "719_2", "girl": "tamaki", "name": "暁光の錦(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4354", "tec": "3566", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2022/12/28", "resell": "", "break": "1", "special_fun": "附带小道具【金扇子】。"
  },
  {
    "id": "719_3", "girl": "leifang", "name": "暁光の錦(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4354", "tec": "3566", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2022/12/28", "resell": "", "break": "1", "special_fun": "附带小道具【金扇子】。"
  },
  {
    "id": "719_4", "girl": "nagisa", "name": "暁光の錦(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4354", "tec": "3566", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2022/12/28", "resell": "", "break": "1", "special_fun": "附带小道具【金扇子】。"
  },
  {
    "id": "719_5", "girl": "patty", "name": "暁光の錦(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4354", "tec": "3566", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2022/12/28", "resell": "", "break": "1", "special_fun": "附带小道具【金扇子】。"
  },
  {
    "id": "719_6", "girl": "koharu", "name": "暁光の錦(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4354", "tec": "3566", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2022/12/28", "resell": "", "break": "1", "special_fun": "附带小道具【金扇子】。"
  },
  {
    "id": "720", "girl": "monica", "name": "メイクアップ・キュイール(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3984", "tec": "5622", "stm": "4094", "apl": "200", "skill1": "裏の裏を突くフェイントH", "skill2": "キュイールのテクニック&スタミナ", "skill3": "可憐なフェイント", "sell": "2023/1/1", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "719_7", "girl": "marie", "name": "暁光の錦(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4354", "tec": "3566", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2023/1/5", "resell": "", "break": "1", "special_fun": "附带小道具【金扇子】。"
  },
  {
    "id": "719_8", "girl": "momiji", "name": "暁光の錦(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4354", "tec": "3566", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2023/1/5", "resell": "", "break": "1", "special_fun": "附带小道具【金扇子】。"
  },
  {
    "id": "719_9", "girl": "kanna", "name": "暁光の錦(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4354", "tec": "3566", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2023/1/5", "resell": "", "break": "1", "special_fun": "附带小道具【金扇子】。"
  },
  {
    "id": "719_10", "girl": "lobelia", "name": "暁光の錦(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4354", "tec": "3566", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2023/1/5", "resell": "", "break": "1", "special_fun": "附带小道具【金扇子】。"
  },
  {
    "id": "719_11", "girl": "nanami", "name": "暁光の錦(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4354", "tec": "3566", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2023/1/5", "resell": "", "break": "1", "special_fun": "附带小道具【金扇子】。"
  },
  {
    "id": "719_12", "girl": "amy", "name": "暁光の錦(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4354", "tec": "3566", "stm": "5122", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "内から湧き上がるスタミナ6", "skill3": "豪快なスパイク", "sell": "2023/1/5", "resell": "", "break": "1", "special_fun": "附带小道具【金扇子】。"
  },
  {
    "id": "588_11", "girl": "fiona", "name": "来光神楽(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3506", "tec": "5052", "stm": "4084", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2023/1/12", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "588_12", "girl": "monica", "name": "来光神楽(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3506", "tec": "5052", "stm": "4084", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2023/1/12", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "588_13", "girl": "koharu", "name": "来光神楽(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3506", "tec": "5052", "stm": "4084", "apl": "200", "skill1": "高度な心理戦C", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2023/1/12", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "556_6", "girl": "shandy", "name": "スパークリングブルー(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5012", "tec": "3546", "stm": "4084", "apl": "200", "skill1": "強烈スパイクA", "skill2": "秘められたパワー3", "skill3": "熱烈なエール", "sell": "2023/1/18", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "556_7", "girl": "kasumi", "name": "スパークリングブルー(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5062", "tec": "3626", "stm": "4054", "apl": "200", "skill1": "強烈スパイクF", "skill2": "不動のレシーブC", "skill3": "秘められたパワー4", "sell": "2023/1/18", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "556_8", "girl": "honoka", "name": "スパークリングブルー(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5062", "tec": "3626", "stm": "4054", "apl": "200", "skill1": "強烈スパイクF", "skill2": "不動のレシーブC", "skill3": "秘められたパワー4", "sell": "2023/1/18", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "721_1", "girl": "ayane", "name": "ダークネスクイーン(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5102", "stm": "4064", "apl": "200", "skill1": "天才的な先読みE", "skill2": "魔王のテクニック", "skill3": "熱烈なエール", "sell": "2023/1/26", "resell": "", "break": "1", "special_fun": "使用天狗扇,扇动的时候会出现火焰粒子效果(火焰之舞)。"
  },
  {
    "id": "721_2", "girl": "nyotengu", "name": "ダークネスクイーン(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5102", "stm": "4064", "apl": "200", "skill1": "天才的な先読みE", "skill2": "魔王のテクニック", "skill3": "熱烈なエール", "sell": "2023/1/26", "resell": "", "break": "1", "special_fun": "使用天狗扇,扇动的时候会出现火焰粒子效果(火焰之舞)。"
  },
  {
    "id": "721_3", "girl": "helena", "name": "ダークネスクイーン(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5102", "stm": "4064", "apl": "200", "skill1": "天才的な先読みE", "skill2": "魔王のテクニック", "skill3": "熱烈なエール", "sell": "2023/1/26", "resell": "", "break": "1", "special_fun": "使用天狗扇,扇动的时候会出现火焰粒子效果(火焰之舞)。"
  },
  {
    "id": "721_4", "girl": "luna", "name": "ダークネスクイーン(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5102", "stm": "4064", "apl": "200", "skill1": "天才的な先読みE", "skill2": "魔王のテクニック", "skill3": "熱烈なエール", "sell": "2023/1/26", "resell": "", "break": "1", "special_fun": "使用天狗扇,扇动的时候会出现火焰粒子效果(火焰之舞)。"
  },
  {
    "id": "721_5", "girl": "tamaki", "name": "ダークネスクイーン(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5102", "stm": "4064", "apl": "200", "skill1": "天才的な先読みE", "skill2": "魔王のテクニック", "skill3": "熱烈なエール", "sell": "2023/1/26", "resell": "", "break": "1", "special_fun": "使用天狗扇,扇动的时候会出现火焰粒子效果(火焰之舞)。"
  },
  {
    "id": "721_6", "girl": "sayuri", "name": "ダークネスクイーン(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5102", "stm": "4064", "apl": "200", "skill1": "天才的な先読みE", "skill2": "魔王のテクニック", "skill3": "熱烈なエール", "sell": "2023/1/26", "resell": "", "break": "1", "special_fun": "使用天狗扇,扇动的时候会出现火焰粒子效果(火焰之舞)。"
  },
  {
    "id": "721_7", "girl": "patty", "name": "ダークネスクイーン(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5102", "stm": "4064", "apl": "200", "skill1": "天才的な先読みE", "skill2": "魔王のテクニック", "skill3": "熱烈なエール", "sell": "2023/1/26", "resell": "", "break": "1", "special_fun": "使用天狗扇,扇动的时候会出现火焰粒子效果(火焰之舞)。"
  },
  {
    "id": "721_8", "girl": "tsukushi", "name": "ダークネスクイーン(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5102", "stm": "4064", "apl": "200", "skill1": "天才的な先読みE", "skill2": "魔王のテクニック", "skill3": "熱烈なエール", "sell": "2023/1/26", "resell": "", "break": "1", "special_fun": "使用天狗扇,扇动的时候会出现火焰粒子效果(火焰之舞)。"
  },
  {
    "id": "721_9", "girl": "elise", "name": "ダークネスクイーン(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5102", "stm": "4064", "apl": "200", "skill1": "天才的な先読みE", "skill2": "魔王のテクニック", "skill3": "熱烈なエール", "sell": "2023/1/26", "resell": "", "break": "1", "special_fun": "使用天狗扇,扇动的时候会出现火焰粒子效果(火焰之舞)。"
  },
  {
    "id": "721_10", "girl": "shandy", "name": "ダークネスクイーン(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "5102", "stm": "4064", "apl": "200", "skill1": "天才的な先読みE", "skill2": "魔王のテクニック", "skill3": "熱烈なエール", "sell": "2023/1/26", "resell": "", "break": "1", "special_fun": "使用天狗扇,扇动的时候会出现火焰粒子效果(火焰之舞)。"
  },
  {
    "id": "722", "girl": "helena", "name": "メイクアップ・キュイール(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4014", "tec": "5622", "stm": "4064", "apl": "200", "skill1": "裏の裏を突くフェイントH", "skill2": "キュイールのテクニック&スタミナ", "skill3": "可憐なフェイント", "sell": "2023/1/30", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "723", "girl": "shandy", "name": "空色のスリットワンピ(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3724", "tec": "4266", "stm": "5152", "apl": "200", "skill1": "驚異のスタミナD", "skill2": "裏の裏を突くフェイントC", "skill3": "内から湧き上がるスタミナ5", "sell": "2023/2/1", "resell": "N/A", "break": "1", "special_fun": "【新常驻池】使用白券或常驻确定券 2:1兑换 新常驻池白券 或 新常驻确定券。新常驻池的白券池[星期一 4:00]轮换角色。"
  },
  {
    "id": "724_1", "girl": "kasumi", "name": "恋文ヲトメ(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_2", "girl": "honoka", "name": "恋文ヲトメ(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_3", "girl": "marie", "name": "恋文ヲトメ(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_4", "girl": "ayane", "name": "恋文ヲトメ(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_5", "girl": "nyotengu", "name": "恋文ヲトメ(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_6", "girl": "kokoro", "name": "恋文ヲトメ(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_7", "girl": "hitomi", "name": "恋文ヲトメ(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_8", "girl": "momiji", "name": "恋文ヲトメ(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_9", "girl": "helena", "name": "恋文ヲトメ(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_10", "girl": "misaki", "name": "恋文ヲトメ(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_11", "girl": "luna", "name": "恋文ヲトメ(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_12", "girl": "tamaki", "name": "恋文ヲトメ(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_13", "girl": "leifang", "name": "恋文ヲトメ(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_14", "girl": "fiona", "name": "恋文ヲトメ(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_15", "girl": "nagisa", "name": "恋文ヲトメ(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_16", "girl": "kanna", "name": "恋文ヲトメ(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_17", "girl": "monica", "name": "恋文ヲトメ(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_18", "girl": "sayuri", "name": "恋文ヲトメ(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_19", "girl": "patty", "name": "恋文ヲトメ(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_20", "girl": "tsukushi", "name": "恋文ヲトメ(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_21", "girl": "lobelia", "name": "恋文ヲトメ(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_22", "girl": "nanami", "name": "恋文ヲトメ(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_23", "girl": "elise", "name": "恋文ヲトメ(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_24", "girl": "koharu", "name": "恋文ヲトメ(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_25", "girl": "tina", "name": "恋文ヲトメ(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_26", "girl": "amy", "name": "恋文ヲトメ(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "724_27", "girl": "shandy", "name": "恋文ヲトメ(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3476", "stm": "4034", "apl": "200", "skill1": "強烈スパイクB", "skill2": "ヲトメのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/2", "resell": "", "break": "1", "special_fun": "允许和本次的所有服装互相成为狗粮素材满觉。开发：我来装一波文青 バカンス短し 恋せよ女神（假期苦短，及时恋爱吧少女）作田：我建议改成イベント短し 课金せよオーナー （活动苦短，及时氪金吧岛主）"
  },
  {
    "id": "604_24", "girl": "koharu", "name": "シュガー・パフューム(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2023/2/9", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "604_25", "girl": "tina", "name": "シュガー・パフューム(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2023/2/9", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "604_26", "girl": "amy", "name": "シュガー・パフューム(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2023/2/9", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "604_27", "girl": "shandy", "name": "シュガー・パフューム(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5172", "tec": "3506", "stm": "3964", "apl": "200", "skill1": "不動のレシーブC", "skill2": "パフュームのパワー", "skill3": "熱烈なエール", "sell": "2023/2/9", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "725", "girl": "fiona", "name": "メイクアップ・ネージュ(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3994", "tec": "5622", "stm": "4084", "apl": "200", "skill1": "裏の裏を突くフェイントH", "skill2": "ネージュのテクニック&スタミナ", "skill3": "可憐なフェイント", "sell": "2023/2/11", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "504_6", "girl": "kokoro", "name": "レイク・エルヴン(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4344", "tec": "3566", "stm": "5132", "apl": "200", "skill1": "強烈スパイクA", "skill2": "内から湧き上がるスタミナ3", "skill3": "豪快なスパイク", "sell": "2023/2/16", "resell": "", "break": "1", "special_fun": "我相信kt的人一定不认识塞蕾斯汀"
  },
  {
    "id": "504_7", "girl": "hitomi", "name": "レイク・エルヴン(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4404", "tec": "3646", "stm": "5092", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "強烈スパイクC", "skill3": "内から湧き上がるスタミナ4", "sell": "2023/2/16", "resell": "", "break": "1", "special_fun": "我相信kt的人一定不认识塞蕾斯汀"
  },
  {
    "id": "504_8", "girl": "nagisa", "name": "レイク・エルヴン(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4404", "tec": "3646", "stm": "5092", "apl": "200", "skill1": "灼熱のダンスE", "skill2": "強烈スパイクC", "skill3": "内から湧き上がるスタミナ4", "sell": "2023/2/16", "resell": "", "break": "1", "special_fun": "我相信kt的人一定不认识塞蕾斯汀"
  },
  {
    "id": "726", "girl": "koharu", "name": "ブーケ・カトレア(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4784", "tec": "3694", "stm": "5622", "apl": "200", "skill1": "強烈スパイクG", "skill2": "カトレアのスタミナ", "skill3": "豪快なスパイク", "sell": "2023/2/16", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "727", "girl": "tina", "name": "ブーケ・カトレア(ティナ)", "zhs_name": "花束・卡特兰(蒂娜)", "zht_name": "花束‧卡特蘭(蒂娜)", "en_name": "Bouquet Cattleya (Tina)", "kr_name": "부케 카틀레야(티나)", "type": "pow", "pow": "5622", "tec": "3944", "stm": "4134", "apl": "200", "skill1": "強烈スパイクG", "skill2": "カトレアのパワー", "skill3": "豪快なスパイク", "sell": "2023/2/16", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "728", "girl": "yukino", "name": "ライク・ラブ・チェリッシュ(ゆきの)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5202", "tec": "3446", "stm": "4094", "apl": "200", "skill1": "強烈スパイクA", "skill2": "圧倒的な気迫E", "skill3": "秘められたパワー6", "sell": "2023/2/21", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "729", "girl": "sayuri", "name": "えいりあんハート(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3516", "stm": "4094", "apl": "200", "skill1": "圧倒的な気迫C", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー6", "sell": "2023/2/22", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "730", "girl": "tsukushi", "name": "えいりあんハート(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5102", "tec": "3456", "stm": "4084", "apl": "200", "skill1": "強烈なプレッシャーB", "skill2": "秘められたパワー4", "skill3": "熱烈なエール", "sell": "2023/2/22", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "731", "girl": "elise", "name": "えいりあんハート(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3516", "stm": "4094", "apl": "200", "skill1": "圧倒的な気迫C", "skill2": "驚異のスタミナC", "skill3": "秘められたパワー6", "sell": "2023/2/22", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "732", "girl": "kasumi", "name": "メイクアップ・ネージュ(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3974", "tec": "5622", "stm": "4104", "apl": "200", "skill1": "裏の裏を突くフェイントH", "skill2": "ネージュのテクニック&スタミナ", "skill3": "可憐なフェイント", "sell": "2023/2/23", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "733", "girl": "misaki", "name": "ラビットジョーカー(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4294", "tec": "3566", "stm": "5182", "apl": "200", "skill1": "灼熱のダンスD", "skill2": "内から湧き上がるスタミナ6", "skill3": "熱烈なエール", "sell": "2023/3/2", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "734", "girl": "momiji", "name": "ラビットジョーカー(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4414", "tec": "3626", "stm": "5102", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "圧倒的な気迫E", "skill3": "内から湧き上がるスタミナ4", "sell": "2023/3/2", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "735", "girl": "tamaki", "name": "ラビットジョーカー(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4414", "tec": "3626", "stm": "5102", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "圧倒的な気迫E", "skill3": "内から湧き上がるスタミナ4", "sell": "2023/3/2", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "736", "girl": "shandy", "name": "メイクアップ・コスタ(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3914", "stm": "4164", "apl": "200", "skill1": "強烈スパイクH", "skill2": "コスタのパワー&スタミナ", "skill3": "豪快なスパイク", "sell": "2023/3/3", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "482_21", "girl": "lobelia", "name": "ぬくもりマフラー(ロベリア)", "zhs_name": "温暖围巾", "zht_name": "", "en_name": "Scarf of Warmth", "kr_name": "따스한 머플러", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2023/3/9", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "482_22", "girl": "nanami", "name": "ぬくもりマフラー(ななみ)", "zhs_name": "温暖围巾", "zht_name": "", "en_name": "Scarf of Warmth", "kr_name": "따스한 머플러", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2023/3/9", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "482_23", "girl": "elise", "name": "ぬくもりマフラー(エリーゼ)", "zhs_name": "温暖围巾", "zht_name": "", "en_name": "Scarf of Warmth", "kr_name": "따스한 머플러", "type": "tec", "pow": "3596", "tec": "5042", "stm": "4004", "apl": "200", "skill1": "高度な心理戦F", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2023/3/9", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "737_1", "girl": "ayane", "name": "ボルテージハート(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "3686", "tec": "4546", "stm": "4194", "apl": "550", "skill1": "裏の裏を突くフェイントB", "skill2": "隠しきれない魅力4", "skill3": "熱烈なエール", "sell": "2023/3/16", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "737_2", "girl": "leifang", "name": "ボルテージハート(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "3686", "tec": "4546", "stm": "4194", "apl": "550", "skill1": "裏の裏を突くフェイントB", "skill2": "隠しきれない魅力4", "skill3": "熱烈なエール", "sell": "2023/3/16", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "737_3", "girl": "fiona", "name": "ボルテージハート(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "3686", "tec": "4546", "stm": "4194", "apl": "550", "skill1": "裏の裏を突くフェイントB", "skill2": "隠しきれない魅力4", "skill3": "熱烈なエール", "sell": "2023/3/16", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "737_4", "girl": "nanami", "name": "ボルテージハート(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "3686", "tec": "4546", "stm": "4194", "apl": "550", "skill1": "裏の裏を突くフェイントB", "skill2": "隠しきれない魅力4", "skill3": "熱烈なエール", "sell": "2023/3/16", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "737_5", "girl": "amy", "name": "ボルテージハート(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "3686", "tec": "4546", "stm": "4194", "apl": "550", "skill1": "裏の裏を突くフェイントB", "skill2": "隠しきれない魅力4", "skill3": "熱烈なエール", "sell": "2023/3/16", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "300_16", "girl": "honoka", "name": "ライザ・お気に入りの普段着(ほのか)", "zhs_name": "莱莎·喜欢的日常装束(穗香)", "zht_name": "萊莎‧喜歡的日常裝束(穗香)", "en_name": "Ryza's Favorite Outfit (Honoka)", "kr_name": "라이자・좋아하는 평상복(호노카)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2023/3/22", "resell": "", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_17", "girl": "ayane", "name": "ライザ・お気に入りの普段着(あやね)", "zhs_name": "莱莎·喜欢的日常装束(绫音)", "zht_name": "萊莎‧喜歡的日常裝束(綾音)", "en_name": "Ryza's Favorite Outfit (Ayane)", "kr_name": "라이자・좋아하는 평상복(아야네)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2023/3/22", "resell": "", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_18", "girl": "kokoro", "name": "ライザ・お気に入りの普段着(こころ)", "zhs_name": "莱莎·喜欢的日常装束(心)", "zht_name": "萊莎‧喜歡的日常裝束(心)", "en_name": "Ryza's Favorite Outfit (Kokoro)", "kr_name": "라이자・좋아하는 평상복(코코로)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2023/3/22", "resell": "", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_19", "girl": "helena", "name": "ライザ・お気に入りの普段着(エレナ)", "zhs_name": "莱莎·喜欢的日常装束(海莲娜)", "zht_name": "萊莎‧喜歡的日常裝束(海蓮娜)", "en_name": "Ryza's Favorite Outfit (Helena)", "kr_name": "라이자・좋아하는 평상복(엘레나)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2023/3/22", "resell": "", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_20", "girl": "leifang", "name": "ライザ・お気に入りの普段着(レイファン)", "zhs_name": "莱莎·喜欢的日常装束(丽凤)", "zht_name": "萊莎‧喜歡的日常裝束(麗鳳)", "en_name": "Ryza's Favorite Outfit (Leifang)", "kr_name": "라이자・좋아하는 평상복(레이팡)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2023/3/22", "resell": "", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_21", "girl": "lobelia", "name": "ライザ・お気に入りの普段着(ロベリア)", "zhs_name": "莱莎·喜欢的日常装束(萝贝莉娅)", "zht_name": "萊莎‧喜歡的日常裝束(蘿貝莉婭)", "en_name": "Ryza's Favorite Outfit (Lobelia)", "kr_name": "라이자・좋아하는 평상복(로벨리아)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2023/3/22", "resell": "", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_22", "girl": "nanami", "name": "ライザ・お気に入りの普段着(ななみ)", "zhs_name": "莱莎·喜欢的日常装束(七海)", "zht_name": "萊莎‧喜歡的日常裝束(七海)", "en_name": "Ryza's Favorite Outfit (Nanami)", "kr_name": "라이자・좋아하는 평상복(나나미)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2023/3/22", "resell": "", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_23", "girl": "elise", "name": "ライザ・お気に入りの普段着(エリーゼ)", "zhs_name": "莱莎·喜欢的日常装束(伊莉丝)", "zht_name": "萊莎‧喜歡的日常裝束(伊莉絲)", "en_name": "Ryza's Favorite Outfit (Elise)", "kr_name": "라이자・좋아하는 평상복(엘리제)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2023/3/22", "resell": "", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_24", "girl": "koharu", "name": "ライザ・お気に入りの普段着(こはる)", "zhs_name": "莱莎·喜欢的日常装束(小春)", "zht_name": "萊莎‧喜歡的日常裝束(小春)", "en_name": "Ryza's Favorite Outfit (Koharu)", "kr_name": "라이자・좋아하는 평상복(코하루)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2023/3/22", "resell": "", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_25", "girl": "tina", "name": "ライザ・お気に入りの普段着(ティナ)", "zhs_name": "莱莎·喜欢的日常装束(蒂娜)", "zht_name": "萊莎‧喜歡的日常裝束(蒂娜)", "en_name": "Ryza's Favorite Outfit (Tina)", "kr_name": "라이자・좋아하는 평상복(티나)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2023/3/22", "resell": "", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_26", "girl": "amy", "name": "ライザ・お気に入りの普段着(エイミー)", "zhs_name": "莱莎・喜欢的日常装束(艾米)", "zht_name": "萊莎‧喜歡的日常裝束(愛咪)", "en_name": "Ryza's Favorite Outfit(Amy)", "kr_name": "라이자・좋아하는 평상복(에이미)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2023/3/22", "resell": "", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "300_27", "girl": "shandy", "name": "ライザ・お気に入りの普段着(シャンディ)", "zhs_name": "莱莎・喜欢的日常装束(?)", "zht_name": "萊莎‧喜歡的日常裝束(?)", "en_name": "Ryza's Favorite Outfit(Shandy)", "kr_name": "라이자・좋아하는 평상복(?)", "type": "tec", "pow": "3594", "tec": "4942", "stm": "4206", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "ライザのテクニック", "skill3": "可憐なフェイント", "sell": "2023/3/22", "resell": "", "break": "1", "special_fun": "ライザのアトリエ２～失われた伝承と秘密の妖精～(莱莎的炼金工房2)联动服装（冷饭） 附带专属拍照姿势 帽子可以设定隐藏"
  },
  {
    "id": "738", "girl": "honoka", "name": "メイクアップ・コスタ(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "4014", "stm": "4064", "apl": "200", "skill1": "強烈スパイクH", "skill2": "コスタのパワー&スタミナ", "skill3": "豪快なスパイク", "sell": "2023/3/24", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "739", "girl": "helena", "name": "シークレットクラス(エレナ)", "zhs_name": "秘密课堂(海莲娜)", "zht_name": "", "en_name": "Secret Class (Helena)", "kr_name": "시크릿 클래스(엘레나)", "type": "tec", "pow": "3466", "tec": "5062", "stm": "4114", "apl": "200", "skill1": "鉄壁のレシーブD", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2023/3/29", "resell": "", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "740", "girl": "nyotengu", "name": "シークレットクラス(女天狗)", "zhs_name": "秘密课堂(女天狗)", "zht_name": "", "en_name": "Secret Class (Nyotengu)", "kr_name": "시크릿 클래스(뇨텐구)", "type": "tec", "pow": "3516", "tec": "5152", "stm": "4074", "apl": "200", "skill1": "鉄壁のレシーブE", "skill2": "天才的な先読みC", "skill3": "閃きのテクニック6", "sell": "2023/3/29", "resell": "", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "741", "girl": "patty", "name": "シークレットクラス(パティ)", "zhs_name": "秘密课堂(派蒂)", "zht_name": "", "en_name": "Secret Class (Patty)", "kr_name": "시크릿 클래스(패티)", "type": "tec", "pow": "3516", "tec": "5152", "stm": "4074", "apl": "200", "skill1": "鉄壁のレシーブE", "skill2": "天才的な先読みC", "skill3": "閃きのテクニック6", "sell": "2023/3/29", "resell": "", "break": "1", "special_fun": "服装拥有濡湿透视效果，觉醒等级越高透视范围越大"
  },
  {
    "id": "742", "girl": "marie", "name": "トゥインクル・ローズ(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3446", "tec": "5122", "stm": "4074", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "サーバントのスタミナ", "skill3": "熱烈なエール", "sell": "2023/3/29", "resell": "", "break": "1", "special_fun": "FBI open the door！联动服装,有机会成为龙王的狱友共进牢饭。第5年True color系列氪金衣服。初回抽取10连解锁女神石板付费路线。作田：回归初心没有新发型。"
  },
  {
    "id": "743", "girl": "sayuri", "name": "メイクアップ・コスタ(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3924", "tec": "5622", "stm": "4154", "apl": "200", "skill1": "裏の裏を突くフェイントH", "skill2": "コスタのテクニック&スタミナ", "skill3": "可憐なフェイント", "sell": "2023/3/31", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "744", "girl": "kasumi", "name": "はいからブルーマー(かすみ)", "zhs_name": "时髦体操裤(霞)", "zht_name": "", "en_name": "Stylish Bloomers (Kasumi)", "kr_name": "하이 컬러 블루머(카스미)", "type": "stm", "pow": "3576", "tec": "4394", "stm": "5072", "apl": "200", "skill1": "高度な心理戦B", "skill2": "内から湧き上がるスタミナ3", "skill3": "可憐なフェイント", "sell": "2023/4/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "745", "girl": "misaki", "name": "はいからブルーマー(みさき)", "zhs_name": "时髦体操裤(海咲)", "zht_name": "", "en_name": "Stylish Bloomers (Misaki)", "kr_name": "하이 컬러 블루머(미사키)", "type": "stm", "pow": "3556", "tec": "4474", "stm": "5112", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "高度な心理戦C", "skill3": "内から湧き上がるスタミナ4", "sell": "2023/4/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "746", "girl": "koharu", "name": "はいからブルーマー(こはる)", "zhs_name": "时髦体操裤(小春)", "zht_name": "", "en_name": "Stylish Bloomers (Koharu)", "kr_name": "하이 컬러 블루머(코하루)", "type": "stm", "pow": "3556", "tec": "4474", "stm": "5112", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "高度な心理戦C", "skill3": "内から湧き上がるスタミナ4", "sell": "2023/4/6", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "747", "girl": "ayane", "name": "おまつりきんぎょ(あやね)", "zhs_name": "祭典金鱼(绫音)", "zht_name": "", "en_name": "Festival Goldfish (Ayane)", "kr_name": "금붕어(축제)(아야네)", "type": "pow", "pow": "5082", "tec": "3456", "stm": "4104", "apl": "200", "skill1": "圧倒的な気迫A", "skill2": "秘められたパワー4", "skill3": "豪快なスパイク", "sell": "2023/4/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "748", "girl": "nagisa", "name": "ほしぞらきんぎょ(なぎさ)", "zhs_name": "星空金鱼(凪咲)", "zht_name": "", "en_name": "Starry Night Goldfish (Nagisa)", "kr_name": "금붕어(별하늘)(나기사)", "type": "pow", "pow": "5202", "tec": "3516", "stm": "4024", "apl": "200", "skill1": "強烈スパイクD", "skill2": "圧倒的な気迫C", "skill3": "秘められたパワー5", "sell": "2023/4/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "749", "girl": "lobelia", "name": "ほしぞらきんぎょ(ロベリア)", "zhs_name": "星空金鱼(萝贝莉娅)", "zht_name": "", "en_name": "Starry Night Goldfish (Lobelia)", "kr_name": "금붕어(별하늘)(로벨리아)", "type": "pow", "pow": "5202", "tec": "3516", "stm": "4024", "apl": "200", "skill1": "強烈スパイクD", "skill2": "圧倒的な気迫C", "skill3": "秘められたパワー5", "sell": "2023/4/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "750", "girl": "yukino", "name": "ネオンナイトパンサー(ゆきの)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4364", "tec": "3546", "stm": "5132", "apl": "200", "skill1": "驚異のスタミナB", "skill2": "パンサーのスタミナ", "skill3": "熱烈なエール", "sell": "2023/4/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "751", "girl": "nanami", "name": "メイクアップ・ブルーム(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3904", "stm": "4174", "apl": "200", "skill1": "強烈スパイクH", "skill2": "ブルームのパワー&スタミナ", "skill3": "豪快なスパイク", "sell": "2023/4/16", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "752", "girl": "momiji", "name": "おやすみましまろ(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4374", "tec": "3586", "stm": "5082", "apl": "200", "skill1": "強烈スパイクF", "skill2": "内から湧き上がるスタミナ3", "skill3": "熱烈なエール", "sell": "2023/4/20", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "753", "girl": "fiona", "name": "おやすみましまろ(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4394", "tec": "3606", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "強烈スパイクC", "skill3": "内から湧き上がるスタミナ4", "sell": "2023/4/20", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "754", "girl": "monica", "name": "おやすみましまろ(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4394", "tec": "3606", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナF", "skill2": "強烈スパイクC", "skill3": "内から湧き上がるスタミナ4", "sell": "2023/4/20", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "755", "girl": "leifang", "name": "メイクアップ・ブルーム(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3934", "tec": "5622", "stm": "4144", "apl": "200", "skill1": "裏の裏を突くフェイントH", "skill2": "ブルームのテクニック&スタミナ", "skill3": "可憐なフェイント", "sell": "2023/4/23", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "756_1", "girl": "honoka", "name": "トロピカル・パイレーツ(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3436", "tec": "5172", "stm": "4034", "apl": "200", "skill1": "天才的な先読みF", "skill2": "パイレーツのスタミナ", "skill3": "熱烈なエール", "sell": "2023/4/27", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "756_2", "girl": "hitomi", "name": "トロピカル・パイレーツ(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3436", "tec": "5172", "stm": "4034", "apl": "200", "skill1": "天才的な先読みF", "skill2": "パイレーツのスタミナ", "skill3": "熱烈なエール", "sell": "2023/4/27", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "756_3", "girl": "sayuri", "name": "トロピカル・パイレーツ(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3436", "tec": "5172", "stm": "4034", "apl": "200", "skill1": "天才的な先読みF", "skill2": "パイレーツのスタミナ", "skill3": "熱烈なエール", "sell": "2023/4/27", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "756_4", "girl": "elise", "name": "トロピカル・パイレーツ(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3436", "tec": "5172", "stm": "4034", "apl": "200", "skill1": "天才的な先読みF", "skill2": "パイレーツのスタミナ", "skill3": "熱烈なエール", "sell": "2023/4/27", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "756_5", "girl": "tina", "name": "トロピカル・パイレーツ(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3436", "tec": "5172", "stm": "4034", "apl": "200", "skill1": "天才的な先読みF", "skill2": "パイレーツのスタミナ", "skill3": "熱烈なエール", "sell": "2023/4/27", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "756_6", "girl": "amy", "name": "トロピカル・パイレーツ(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3436", "tec": "5172", "stm": "4034", "apl": "200", "skill1": "天才的な先読みF", "skill2": "パイレーツのスタミナ", "skill3": "熱烈なエール", "sell": "2023/4/27", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "756_7", "girl": "kokoro", "name": "トロピカル・パイレーツ(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3436", "tec": "5172", "stm": "4034", "apl": "200", "skill1": "天才的な先読みF", "skill2": "パイレーツのスタミナ", "skill3": "熱烈なエール", "sell": "2023/5/4", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "756_8", "girl": "misaki", "name": "トロピカル・パイレーツ(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3436", "tec": "5172", "stm": "4034", "apl": "200", "skill1": "天才的な先読みF", "skill2": "パイレーツのスタミナ", "skill3": "熱烈なエール", "sell": "2023/5/4", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "756_9", "girl": "luna", "name": "トロピカル・パイレーツ(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3436", "tec": "5172", "stm": "4034", "apl": "200", "skill1": "天才的な先読みF", "skill2": "パイレーツのスタミナ", "skill3": "熱烈なエール", "sell": "2023/5/4", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "756_10", "girl": "tamaki", "name": "トロピカル・パイレーツ(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3436", "tec": "5172", "stm": "4034", "apl": "200", "skill1": "天才的な先読みF", "skill2": "パイレーツのスタミナ", "skill3": "熱烈なエール", "sell": "2023/5/4", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "756_11", "girl": "monica", "name": "トロピカル・パイレーツ(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3436", "tec": "5172", "stm": "4034", "apl": "200", "skill1": "天才的な先読みF", "skill2": "パイレーツのスタミナ", "skill3": "熱烈なエール", "sell": "2023/5/4", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "756_12", "girl": "shandy", "name": "トロピカル・パイレーツ(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3436", "tec": "5172", "stm": "4034", "apl": "200", "skill1": "天才的な先読みF", "skill2": "パイレーツのスタミナ", "skill3": "熱烈なエール", "sell": "2023/5/4", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "757", "girl": "nagisa", "name": "メイクアップ・シダー(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3964", "stm": "4114", "apl": "200", "skill1": "強烈スパイクH", "skill2": "シダーのパワー&スタミナ", "skill3": "豪快なスパイク", "sell": "2023/5/5", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "758_1", "girl": "marie", "name": "プリマ・スワン(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5072", "tec": "3536", "stm": "4034", "apl": "200", "skill1": "強烈なプレッシャーA", "skill2": "秘められたパワー4", "skill3": "熱烈なエール", "sell": "2023/5/11", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "758_2", "girl": "kanna", "name": "プリマ・スワン(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5072", "tec": "3536", "stm": "4034", "apl": "200", "skill1": "強烈なプレッシャーA", "skill2": "秘められたパワー4", "skill3": "熱烈なエール", "sell": "2023/5/11", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "759_1", "girl": "nagisa", "name": "プリマ・レイク(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "圧倒的な気迫C", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2023/5/11", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "759_2", "girl": "lobelia", "name": "プリマ・レイク(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "圧倒的な気迫C", "skill2": "秘められたパワー5", "skill3": "豪快なスパイク", "sell": "2023/5/11", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "174_16", "girl": "tsukushi", "name": "ハーフセイル(つくし)", "zhs_name": "半帆(筑紫)", "zht_name": "半帆(筑紫)", "en_name": "Half Sail (Tsukushi)", "kr_name": "절반의 돛(츠쿠시)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2023/5/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "174_17", "girl": "nanami", "name": "ハーフセイル(ななみ)", "zhs_name": "半帆(七海)", "zht_name": "半帆(七海)", "en_name": "Half Sail (Nanami)", "kr_name": "절반의 돛(나나미)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2023/5/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "174_18", "girl": "koharu", "name": "ハーフセイル(こはる)", "zhs_name": "半帆(小春)", "zht_name": "半帆(小春)", "en_name": "Half Sail (Koharu)", "kr_name": "절반의 돛(코하루)", "type": "tec", "pow": "4144", "tec": "4962", "stm": "3536", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "閃きのテクニック5", "skill3": "熱烈なエール", "sell": "2023/5/19", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "760", "girl": "hitomi", "name": "メイクアップ・シダー(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3934", "stm": "4114", "apl": "200", "skill1": "強烈スパイクH", "skill2": "シダーのパワー&スタミナ", "skill3": "豪快なスパイク", "sell": "2023/5/25", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "761_1", "girl": "kasumi", "name": "スリップストリーム(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_2", "girl": "honoka", "name": "スリップストリーム(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_3", "girl": "marie", "name": "スリップストリーム(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_4", "girl": "ayane", "name": "スリップストリーム(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_5", "girl": "nyotengu", "name": "スリップストリーム(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_6", "girl": "kokoro", "name": "スリップストリーム(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_7", "girl": "hitomi", "name": "スリップストリーム(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_8", "girl": "momiji", "name": "スリップストリーム(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_9", "girl": "helena", "name": "スリップストリーム(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_10", "girl": "misaki", "name": "スリップストリーム(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_11", "girl": "luna", "name": "スリップストリーム(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_12", "girl": "tamaki", "name": "スリップストリーム(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_13", "girl": "leifang", "name": "スリップストリーム(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_14", "girl": "fiona", "name": "スリップストリーム(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_15", "girl": "nagisa", "name": "スリップストリーム(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_16", "girl": "kanna", "name": "スリップストリーム(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_17", "girl": "monica", "name": "スリップストリーム(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_18", "girl": "sayuri", "name": "スリップストリーム(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_19", "girl": "patty", "name": "スリップストリーム(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_20", "girl": "tsukushi", "name": "スリップストリーム(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_21", "girl": "lobelia", "name": "スリップストリーム(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_22", "girl": "nanami", "name": "スリップストリーム(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_23", "girl": "elise", "name": "スリップストリーム(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_24", "girl": "koharu", "name": "スリップストリーム(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_25", "girl": "tina", "name": "スリップストリーム(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_26", "girl": "amy", "name": "スリップストリーム(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "761_27", "girl": "shandy", "name": "スリップストリーム(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "強烈スパイクB", "skill2": "スリップストリームのパワー", "skill3": "熱烈なエール", "sell": "2023/5/26", "resell": "", "break": "1", "special_fun": "5.5周年庆服装。可以切换服装颜色，最大觉醒时外套可脱。附带额外剧情、大道具【颁奖台】【赛车】。"
  },
  {
    "id": "c9", "girl": "All", "name": "国際版第2回水着コンテスト「優勝１」", "type": "none", "pow": "0", "tec": "0", "stm": "0", "apl": "0", "skill1": "", "skill2": "", "skill3": "", "sell": "2023/5/26", "resell": "N/A", "break": "1", "special_fun": "steam第二次服装设计比赛 得奖作品。作为礼包3000付费钻 两件打包销售 仅外形无属性。Design by Ponytaillll"
  },
  {
    "id": "c10", "girl": "All", "name": "国際版第2回水着コンテスト「優勝2」", "type": "none", "pow": "0", "tec": "0", "stm": "0", "apl": "0", "skill1": "", "skill2": "", "skill3": "", "sell": "2023/5/26", "resell": "N/A", "break": "1", "special_fun": "steam第二次服装设计比赛 得奖作品。作为礼包3000付费钻 两件打包销售 仅外形无属性。Design by 煤矿矿主"
  },
  {
    "id": "651_25", "girl": "tina", "name": "バニー・クロック(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2023/6/1", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "651_26", "girl": "amy", "name": "バニー・クロック(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2023/6/1", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "651_27", "girl": "shandy", "name": "バニー・クロック(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3456", "tec": "4364", "stm": "5222", "apl": "200", "skill1": "裏の裏を突くフェイントD", "skill2": "不思議なウサギのスタミナ", "skill3": "可憐なフェイント", "sell": "2023/6/1", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "762", "girl": "marie", "name": "メイクアップ・ノブレス(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3964", "tec": "5622", "stm": "4114", "apl": "200", "skill1": "裏の裏を突くフェイントH", "skill2": "ノブレスのテクニック＆スタミナ", "skill3": "可憐なフェイント", "sell": "2023/6/6", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。附带新待机姿势【show me the money】"
  },
  {
    "id": "763_1", "girl": "kokoro", "name": "グレイス・リリー(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "4596", "tec": "3656", "stm": "4174", "apl": "550", "skill1": "強烈スパイクC", "skill2": "隠しきれない魅力3", "skill3": "豪快なスパイク", "sell": "2023/6/8", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "763_2", "girl": "misaki", "name": "グレイス・リリー(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "4596", "tec": "3656", "stm": "4174", "apl": "550", "skill1": "強烈スパイクC", "skill2": "隠しきれない魅力3", "skill3": "豪快なスパイク", "sell": "2023/6/8", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "763_3", "girl": "fiona", "name": "グレイス・リリー(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "4596", "tec": "3656", "stm": "4174", "apl": "550", "skill1": "強烈スパイクC", "skill2": "隠しきれない魅力3", "skill3": "豪快なスパイク", "sell": "2023/6/8", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "763_4", "girl": "koharu", "name": "グレイス・リリー(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "4596", "tec": "3656", "stm": "4174", "apl": "550", "skill1": "強烈スパイクC", "skill2": "隠しきれない魅力3", "skill3": "豪快なスパイク", "sell": "2023/6/8", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "763_5", "girl": "amy", "name": "グレイス・リリー(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "apl", "pow": "4596", "tec": "3656", "stm": "4174", "apl": "550", "skill1": "強烈スパイクC", "skill2": "隠しきれない魅力3", "skill3": "豪快なスパイク", "sell": "2023/6/8", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "331_7", "girl": "shandy", "name": "ベルベットタイム・ライラック(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3476", "tec": "4962", "stm": "4204", "apl": "200", "skill1": "裏の裏を突くフェイントC", "skill2": "閃きのテクニック4", "skill3": "熱烈なエール", "sell": "2023/6/15", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "331_8", "girl": "ayane", "name": "ベルベットタイム・ローズ(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "高度な心理戦D", "skill3": "閃きのテクニック3", "sell": "2023/6/15", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "331_9", "girl": "hitomi", "name": "ベルベットタイム・ローズ(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5242", "tec": "3406", "stm": "3994", "apl": "200", "skill1": "裏の裏を突くフェイントF", "skill2": "高度な心理戦D", "skill3": "閃きのテクニック3", "sell": "2023/6/15", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "764", "girl": "amy", "name": "メイクアップ・ノブレス(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "4004", "tec": "5622", "stm": "4074", "apl": "200", "skill1": "裏の裏を突くフェイントH", "skill2": "ノブレスのテクニック＆スタミナ", "skill3": "可憐なフェイント", "sell": "2023/6/18", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "765_1", "girl": "kasumi", "name": "スキニー・シャーク(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4314", "tec": "3616", "stm": "5112", "apl": "200", "skill1": "強烈スパイクB", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2023/6/21", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "765_2", "girl": "nyotengu", "name": "スキニー・シャーク(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4314", "tec": "3616", "stm": "5112", "apl": "200", "skill1": "強烈スパイクB", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2023/6/21", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "765_3", "girl": "tamaki", "name": "スキニー・シャーク(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4314", "tec": "3616", "stm": "5112", "apl": "200", "skill1": "強烈スパイクB", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2023/6/21", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "765_4", "girl": "patty", "name": "スキニー・シャーク(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4314", "tec": "3616", "stm": "5112", "apl": "200", "skill1": "強烈スパイクB", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2023/6/21", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "765_5", "girl": "nanami", "name": "スキニー・シャーク(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4314", "tec": "3616", "stm": "5112", "apl": "200", "skill1": "強烈スパイクB", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2023/6/21", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "766", "girl": "lobelia", "name": "メイクアップ・ノブレス(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3884", "tec": "5622", "stm": "4194", "apl": "200", "skill1": "裏の裏を突くフェイントH", "skill2": "ノブレスのテクニック＆スタミナ", "skill3": "可憐なフェイント", "sell": "2023/6/25", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "767_1", "girl": "kasumi", "name": "にしざーさん・コスチューム(かすみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_2", "girl": "honoka", "name": "にしざーさん・コスチューム(ほのか)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_3", "girl": "marie", "name": "にしざーさん・コスチューム(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_4", "girl": "kokoro", "name": "にしざーさん・コスチューム(こころ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_5", "girl": "helena", "name": "にしざーさん・コスチューム(エレナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_6", "girl": "misaki", "name": "にしざーさん・コスチューム(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_7", "girl": "luna", "name": "にしざーさん・コスチューム(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_8", "girl": "tamaki", "name": "にしざーさん・コスチューム(たまき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_9", "girl": "leifang", "name": "にしざーさん・コスチューム(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_10", "girl": "nagisa", "name": "にしざーさん・コスチューム(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_11", "girl": "patty", "name": "にしざーさん・コスチューム(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_12", "girl": "lobelia", "name": "にしざーさん・コスチューム(ロベリア)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_13", "girl": "koharu", "name": "にしざーさん・コスチューム(こはる)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "768", "girl": "yukino", "name": "西沢5㍉・ギャルコーデ(ゆきの)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5222", "tec": "3396", "stm": "4024", "apl": "200", "skill1": "強烈スパイクE", "skill2": "ギャルのスタミナ", "skill3": "豪快なスパイク", "sell": "2023/6/27", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。最大觉醒时可以卷起上衣（1段爆衣）。可切到更大胆的比基尼style（2段爆衣），但是在这个普通比基尼狗都不穿的游戏，也就这样吧。"
  },
  {
    "id": "767_14", "girl": "ayane", "name": "にしざーさん・コスチューム(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_15", "girl": "nyotengu", "name": "にしざーさん・コスチューム(女天狗)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_16", "girl": "hitomi", "name": "にしざーさん・コスチューム(ヒトミ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_17", "girl": "momiji", "name": "にしざーさん・コスチューム(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_18", "girl": "fiona", "name": "にしざーさん・コスチューム(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_19", "girl": "kanna", "name": "にしざーさん・コスチューム(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_20", "girl": "monica", "name": "にしざーさん・コスチューム(モニカ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_21", "girl": "sayuri", "name": "にしざーさん・コスチューム(さゆり)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_22", "girl": "tsukushi", "name": "にしざーさん・コスチューム(つくし)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_23", "girl": "nanami", "name": "にしざーさん・コスチューム(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_24", "girl": "elise", "name": "にしざーさん・コスチューム(エリーゼ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_25", "girl": "tina", "name": "にしざーさん・コスチューム(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_26", "girl": "amy", "name": "にしざーさん・コスチューム(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "767_27", "girl": "shandy", "name": "にしざーさん・コスチューム(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5182", "tec": "3496", "stm": "4064", "apl": "200", "skill1": "強烈スパイクF", "skill2": "圧倒的な気迫D", "skill3": "にしざーさんのスタミナ", "sell": "2023/7/5", "resell": "", "break": "1", "special_fun": "「西沢5㍉」联动服装。允许和本次的所有联动服装互相成为狗粮素材满觉。无马作田P精心去掉了8换1机制,设计了池内角色分布,本非洲人3.3%抽了650发只有2.28%。前方8步地狱，量力而行！附带100经验回想。"
  },
  {
    "id": "769", "girl": "misaki", "name": "メイクアップ・マーレ(みさき)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3924", "stm": "4154", "apl": "200", "skill1": "強烈スパイクH", "skill2": "マーレのパワー＆スタミナ", "skill3": "豪快なスパイク", "sell": "2023/7/7", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "609_6", "girl": "momiji", "name": "モーモ・ビキニ(紅葉)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3416", "tec": "5092", "stm": "4134", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2023/7/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "609_7", "girl": "leifang", "name": "モーモ・ビキニ(レイファン)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3416", "tec": "5092", "stm": "4134", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2023/7/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "609_8", "girl": "fiona", "name": "モーモ・ビキニ(フィオナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3416", "tec": "5092", "stm": "4134", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2023/7/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "609_9", "girl": "nanami", "name": "モーモ・ビキニ(ななみ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3416", "tec": "5092", "stm": "4134", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2023/7/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "609_10", "girl": "shandy", "name": "モーモ・ビキニ(シャンディ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3416", "tec": "5092", "stm": "4134", "apl": "200", "skill1": "驚異のスタミナE", "skill2": "閃きのテクニック3", "skill3": "可憐なフェイント", "sell": "2023/7/13", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "548_7", "girl": "marie", "name": "たまゆら花火(マリー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4194", "tec": "3646", "stm": "5202", "apl": "200", "skill1": "強烈スパイクB", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2023/7/20", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "548_8", "girl": "nagisa", "name": "たまゆら花火(なぎさ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4274", "tec": "3726", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "強烈スパイクD", "skill3": "内から湧き上がるスタミナ3", "sell": "2023/7/20", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "548_9", "girl": "kanna", "name": "たまゆら花火(カンナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4274", "tec": "3726", "stm": "5142", "apl": "200", "skill1": "驚異のスタミナC", "skill2": "強烈スパイクD", "skill3": "内から湧き上がるスタミナ3", "sell": "2023/7/20", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "770", "girl": "tina", "name": "ジュエル・ラピスラズリ(ティナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "4724", "tec": "3296", "stm": "5322", "apl": "200", "skill1": "強烈スパイクE", "skill2": "ラピスラズリ・スタミナ", "skill3": "豪快なスパイク", "sell": "2023/7/20", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "771", "girl": "amy", "name": "ジュエル・パール(エイミー)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "stm", "pow": "3346", "tec": "4674", "stm": "5322", "apl": "200", "skill1": "裏の裏を突くフェイントE", "skill2": "パール・スタミナ", "skill3": "可憐なフェイント", "sell": "2023/7/20", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "772_1", "girl": "kasumi", "name": "百花献瑞(かすみ)", "zhs_name": "百花献瑞(霞)", "zht_name": "百花獻瑞(霞)", "en_name": "Auspicious Blossom (Kasumi)", "kr_name": "백화헌서(카스미)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_2", "girl": "honoka", "name": "百花献瑞(ほのか)", "zhs_name": "百花献瑞(穗香)", "zht_name": "百花獻瑞(穗香)", "en_name": "Auspicious Blossom (Honoka)", "kr_name": "백화헌서(호노카)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_3", "girl": "marie", "name": "百花献瑞(マリー)", "zhs_name": "百花献瑞(玛莉)", "zht_name": "百花獻瑞(瑪莉)", "en_name": "Auspicious Blossom (Marie)", "kr_name": "백화헌서(마리)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_4", "girl": "ayane", "name": "百花献瑞(あやね)", "zhs_name": "百花献瑞(绫音)", "zht_name": "百花獻瑞(綾音)", "en_name": "Auspicious Blossom (Ayane)", "kr_name": "백화헌서(아야네)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_5", "girl": "nyotengu", "name": "百花献瑞(女天狗)", "zhs_name": "百花献瑞(女天狗)", "zht_name": "百花獻瑞(女天狗)", "en_name": "Auspicious Blossom (Nyotengu)", "kr_name": "백화헌서(뇨텐구)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_6", "girl": "kokoro", "name": "百花献瑞(こころ)", "zhs_name": "百花献瑞(心)", "zht_name": "百花獻瑞(心)", "en_name": "Auspicious Blossom (Kokoro)", "kr_name": "백화헌서(코코로)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_7", "girl": "hitomi", "name": "百花献瑞(ヒトミ)", "zhs_name": "百花献瑞(瞳)", "zht_name": "百花獻瑞(瞳)", "en_name": "Auspicious Blossom (Hitomi)", "kr_name": "백화헌서(히토미)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_8", "girl": "momiji", "name": "百花献瑞(紅葉)", "zhs_name": "百花献瑞(红叶)", "zht_name": "百花獻瑞(紅葉)", "en_name": "Auspicious Blossom (Momiji)", "kr_name": "백화헌서(모미지)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_9", "girl": "helena", "name": "百花献瑞(エレナ)", "zhs_name": "百花献瑞(海莲娜)", "zht_name": "百花獻瑞(海蓮娜)", "en_name": "Auspicious Blossom (Helena)", "kr_name": "백화헌서(엘레나)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_10", "girl": "misaki", "name": "百花献瑞(みさき)", "zhs_name": "百花献瑞(海咲)", "zht_name": "百花獻瑞(海咲)", "en_name": "Auspicious Blossom (Misaki)", "kr_name": "백화헌서(미사키)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_11", "girl": "luna", "name": "百花献瑞(ルナ)", "zhs_name": "百花献瑞(露娜)", "zht_name": "百花獻瑞(露娜)", "en_name": "Auspicious Blossom (Luna)", "kr_name": "백화헌서(루나)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_12", "girl": "tamaki", "name": "百花献瑞(たまき)", "zhs_name": "百花献瑞(环)", "zht_name": "百花獻瑞(環)", "en_name": "Auspicious Blossom (Tamaki)", "kr_name": "백화헌서(타마키)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_13", "girl": "leifang", "name": "百花献瑞(レイファン)", "zhs_name": "百花献瑞(丽凤)", "zht_name": "百花獻瑞(麗鳳)", "en_name": "Auspicious Blossom (Leifang)", "kr_name": "백화헌서(레이팡)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_14", "girl": "fiona", "name": "百花献瑞(フィオナ)", "zhs_name": "百花献瑞(菲欧娜)", "zht_name": "百花獻瑞(菲歐娜)", "en_name": "Auspicious Blossom (Fiona)", "kr_name": "백화헌서(피오나)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_15", "girl": "nagisa", "name": "百花献瑞(なぎさ)", "zhs_name": "百花献瑞(凪咲)", "zht_name": "百花獻瑞(凪咲)", "en_name": "Auspicious Blossom (Nagisa)", "kr_name": "백화헌서(나기사)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_16", "girl": "kanna", "name": "百花献瑞(カンナ)", "zhs_name": "百花献瑞(神无)", "zht_name": "百花獻瑞(神無)", "en_name": "Auspicious Blossom (Kanna)", "kr_name": "백화헌서(칸나)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_17", "girl": "monica", "name": "百花献瑞(モニカ)", "zhs_name": "百花献瑞(莫妮卡)", "zht_name": "百花獻瑞(莫妮卡)", "en_name": "Auspicious Blossom (Monica)", "kr_name": "백화헌서(모니카)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_18", "girl": "sayuri", "name": "百花献瑞(さゆり)", "zhs_name": "百花献瑞(小百合)", "zht_name": "百花獻瑞(小百合)", "en_name": "Auspicious Blossom (Sayuri)", "kr_name": "백화헌서(사유리)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_19", "girl": "patty", "name": "百花献瑞(パティ)", "zhs_name": "百花献瑞(派蒂)", "zht_name": "百花獻瑞(派蒂)", "en_name": "Auspicious Blossom (Patty)", "kr_name": "백화헌서(패티)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_20", "girl": "tsukushi", "name": "百花献瑞(つくし)", "zhs_name": "百花献瑞(筑紫)", "zht_name": "百花獻瑞(筑紫)", "en_name": "Auspicious Blossom (Tsukushi)", "kr_name": "백화헌서(츠쿠시)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_21", "girl": "lobelia", "name": "百花献瑞(ロベリア)", "zhs_name": "百花献瑞(萝贝莉娅)", "zht_name": "百花獻瑞(蘿貝莉婭)", "en_name": "Auspicious Blossom (Lobelia)", "kr_name": "백화헌서(로벨리아)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_22", "girl": "nanami", "name": "百花献瑞(ななみ)", "zhs_name": "百花献瑞(七海)", "zht_name": "百花獻瑞(七海)", "en_name": "Auspicious Blossom (Nanami)", "kr_name": "백화헌서(나나미)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_23", "girl": "elise", "name": "百花献瑞(エリーゼ)", "zhs_name": "百花献瑞(伊莉丝)", "zht_name": "百花獻瑞(伊莉絲)", "en_name": "Auspicious Blossom (Elise)", "kr_name": "백화헌서(엘리제)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_24", "girl": "koharu", "name": "百花献瑞(こはる)", "zhs_name": "百花献瑞(小春)", "zht_name": "百花獻瑞(小春)", "en_name": "Auspicious Blossom (Koharu)", "kr_name": "백화헌서(코하루)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "772_25", "girl": "tina", "name": "百花献瑞(ティナ)", "zhs_name": "百花献瑞(蒂娜)", "zht_name": "百花獻瑞(蒂娜)", "en_name": "Auspicious Blossom (Tina)", "kr_name": "백화헌서(티나)", "type": "pow", "pow": "5132", "tec": "3466", "stm": "4044", "apl": "200", "skill1": "強烈スパイクC", "skill2": "百花献瑞のパワー", "skill3": "豪快なスパイク", "sell": "2023/7/27", "resell": "", "break": "1", "special_fun": "允许和本次的所有联动服装互相成为狗粮素材满觉。看看5个池的角色分布，单池力量主力的人数绝对不超过2，6步1.1%无8换1。昨天还升级了用户协议，跑路倒闭的话退1年内的课金点数。就问你用心不用心？"
  },
  {
    "id": "773", "girl": "patty", "name": "メイクアップ・マーレ(パティ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5622", "tec": "3984", "stm": "4094", "apl": "200", "skill1": "強烈スパイクH", "skill2": "マーレのパワー＆スタミナ", "skill3": "豪快なスパイク", "sell": "2023/7/31", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  },
  {
    "id": "774", "girl": "sayuri", "name": "ワンダーランド(さゆり)", "zhs_name": "仙境(小百合)", "zht_name": "奇幻國度(小百合)", "en_name": "Wonderland (Sayuri)", "kr_name": "원더랜드(사유리)", "type": "pow", "pow": "5102", "tec": "3526", "stm": "4014", "apl": "200", "skill1": "強烈スパイクF", "skill2": "プラチナアタッカー", "skill3": "豪快なスパイク", "sell": "2023/8/4", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "775", "girl": "honoka", "name": "ワンダーランド(ほのか)", "zhs_name": "仙境(穗香)", "zht_name": "奇幻國度(穗香)", "en_name": "Wonderland (Honoka)", "kr_name": "원더랜드(호노카)", "type": "pow", "pow": "5022", "tec": "3616", "stm": "4104", "apl": "200", "skill1": "強烈スパイクA", "skill2": "灼熱のダンスC", "skill3": "秘められたパワー3", "sell": "2023/8/4", "resell": "", "break": "1", "special_fun": ""
  },
  {
    "id": "776", "girl": "lobelia", "name": "ワンダーランド(ロベリア)", "zhs_name": "仙境(萝贝莉娅)", "zht_name": "奇幻國度(蘿貝莉婭)", "en_name": "Wonderland (Lobelia)", "kr_name": "원더랜드(로벨리아)", "type": "pow", "pow": "5022", "tec": "3616", "stm": "4104", "apl": "200", "skill1": "強烈スパイクA", "skill2": "灼熱のダンスC", "skill3": "秘められたパワー3", "sell": "2023/8/4", "resell": "", "break": "1", "special_fun": ""
  },
  {
  "id": "777", "girl": "luna", "name": "プレシャス・シャイン(ルナ)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "pow", "pow": "5122", "tec": "3436", "stm": "4084", "apl": "200", "skill1": "強烈スパイクE", "skill2": "月兎のスタミナ", "skill3": "熱烈なエール", "sell": "2023/8/4", "resell": "", "break": "1", "special_fun": "第5年True color系列氪金衣服。初回抽取10连解锁女神石板付费路线。新发型Luna股大涨，Marie荣获最丢人True color。"
  },
  {
    "id": "778", "girl": "ayane", "name": "メイクアップ・ローレル(あやね)", "zhs_name": "", "zht_name": "", "en_name": "", "kr_name": "", "type": "tec", "pow": "3914", "tec": "5622", "stm": "4164", "apl": "200", "skill1": "裏の裏を突くフェイントH", "skill2": "ローレルのテクニック＆スタミナ", "skill3": "可憐なフェイント", "sell": "2023/8/5", "resell": "", "break": "1", "special_fun": "第五年生日服，附带更改唇彩功能和小道具【色香のリップ】。拥有双效果技能。"
  }
]

test_ssrs = [
  {
    "id": "338", "girl": "leifang", "name": "おつまみピンチョス(レイファン)", "zhs_name": "拽拽Pinchos(丽凤)", "zht_name": "拽拽Pinchos(麗鳳)", "en_name": "Appetizer Pinchos (Leifang)", "kr_name": "애피타이저 핀초(레이팡)", "type": "stm", "pow": "3776", "tec": "4124", "stm": "5142", "apl": "200", "skill1": "鉄壁のレシーブB", "skill2": "内から湧き上がるスタミナ4", "skill3": "熱烈なエール", "sell": "2020/6/24", "resell": "2020/11/29 2021/10/14", "break": "1", "special_fun": "允许拉扯的衣服，觉醒等级影响可以拉扯的部位"
  },
  {
    "id": "339", "girl": "marie", "name": "スイートビターベリー(マリー)", "zhs_name": "甜涩浆果(玛莉)", "zht_name": "甜澀漿果(瑪莉)", "en_name": "Sweet Bitter Berry (Marie)", "kr_name": "스위트 비터 베리(마리)", "type": "stm", "pow": "3796", "tec": "4314", "stm": "4932", "apl": "200", "skill1": "驚異のスタミナA", "skill2": "プラチナレシーバー", "skill3": "熱烈なエール", "sell": "2020/7/2", "resell": "2020/11/30 2021/6/10 2022/4/28 2023/4/20", "break": "1", "special_fun": ""
  },
  {
    "id": "340", "girl": "kasumi", "name": "スイートミルクベリー(かすみ)", "zhs_name": "奶甜浆果(霞)", "zht_name": "奶甜漿果(霞)", "en_name": "Sweet Milk Berry (Kasumi)", "kr_name": "스위트 밀크 베리(카스미)", "type": "stm", "pow": "3546", "tec": "4344", "stm": "5152", "apl": "200", "skill1": "灼熱のダンスF", "skill2": "内から湧き上がるスタミナ3", "skill3": "可憐なフェイント", "sell": "2020/7/2", "resell": "2020/11/30 2021/6/10 2022/4/28 2023/4/20", "break": "1", "special_fun": ""
  },
]

def insert_skills(skills):
    for skill in skills:
        
        skill_data = {
            "name" : skill["zhs_name"], 
            "effect" : skill["zhs_effect"], 
            "skill_type" : skill["type"],
            "skill_property" : skill["property"].upper()            
                      }
        if skill["type"] == "P" :
            skill_data["pp"] = skill["pp_type"]
        r1 = requests.post("http://127.0.0.1:5000/skills/", data=skill_data)
        print(r1.text)
        

def insert_girls(girls):
    for girl in girls:        
        month, day = girl["birthday"].split("/")
        girl_data = {
            "name" : girl["cname"],             
            "type" : girl["type"].upper(),            
            "birthday": datetime.date(2023,int(month),int(day)),
            "pow": int(girl["pow"]),
            "stm": int(girl["stm"]),
            "tec": int(girl["tec"]),
            "apl": int(girl["apl"]),
            "acc_head": girl["ACC_head"],
            "acc_face": girl["ACC_face"],
            "acc_hand": girl["ACC_hand"]
        }
        r = requests.post("http://127.0.0.1:5000/girls/", data=girl_data)
        print(r.text)        

def get_skill_dict(skills):
  skill_dict = {}
  for skill in skills:
    skill_dict[skill["name"]] = skill["cname"]
  return skill_dict

def get_girl_dict(girls):
  girl_dict = {}
  for girl in girls:
    girl_dict[girl["ename"]] = girl["cname"]
  return girl_dict

def insert_ssrs(ssrs):
    skill_dict = get_skill_dict(skills)
    girl_dict = get_girl_dict(girls)
    print(girl_dict)
    for ssr in ssrs:
      # if "zhs_name" in ssr and ssr["girl"] in girl_dict:                
     if "zhs_name" in ssr and girl_dict.get(ssr["girl"]):            
        ssr_data = {
            "name" : ssr["zhs_name"],             
            "type" : ssr["type"].upper(), 
            "girl" : girl_dict[ssr["girl"]],
            "pow": int(ssr["pow"]),
            "stm": int(ssr["stm"]),
            "tec": int(ssr["tec"]),
            "apl": int(ssr["apl"]),
            "skill1": skill_dict[ssr["skill1"]] if ssr["skill1"] else "",
            "skill2": skill_dict[ssr["skill2"]] if ssr["skill2"] else "",
            "skill3": skill_dict[ssr["skill3"]] if ssr["skill3"] else "",
            "Malfunction": ssr["break"],
            "notes":ssr["special_fun"]
        }
        r = requests.post("http://127.0.0.1:5000/ssrs/", data=ssr_data)
        print(r.text)        
     else:
       print(ssr)    




if __name__ == "__main__":
    # insert_skills(skills)
    # insert_girls(girls)
    insert_ssrs(ssrs)
    

