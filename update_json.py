import json

# --- RUNES ---
with open('data/runes.json', 'r', encoding='utf-8') as f:
    runes = json.load(f)

tc_map = {
    'El': '艾爾', 'Eld': '艾德', 'Tir': '特爾', 'Nef': '那夫', 'Eth': '艾斯', 'Ith': '伊司',
    'Tal': '塔爾', 'Ral': '拉爾', 'Ort': '歐特', 'Thul': '索爾', 'Amn': '安姆', 'Sol': '索爾',
    'Shael': '夏', 'Dol': '多爾', 'Hel': '海爾', 'Io': '埃歐', 'Lum': '盧姆', 'Ko': '寇',
    'Fal': '法爾', 'Lem': '藍姆', 'Pul': '普爾', 'Um': '烏姆', 'Mal': '馬爾', 'Ist': '伊司',
    'Gul': '古爾', 'Vex': '伐克斯', 'Ohm': '歐姆', 'Lo': '羅', 'Sur': '瑟', 'Ber': '貝',
    'Jah': '喬', 'Cham': '查姆', 'Zod': '薩德'
}

new_runes = []
for r in runes:
    new_r = {
        'id': r['id'],
        'name_en': r.get('name_en', r.get('name', '')),
        'name_sc': r.get('name_sc', r.get('name_zh', '')),
        'name_tc': tc_map.get(r.get('name', r.get('name_en', '')), r.get('name_zh', '')),
        'level': r['level']
    }
    new_runes.append(new_r)

with open('data/runes.json', 'w', encoding='utf-8') as f:
    json.dump(new_runes, f, ensure_ascii=False, indent=2)

# --- RUNEWORDS ---
with open('data/runewords.json', 'r', encoding='utf-8') as f:
    rws = json.load(f)

base_map = {
    '武器': '武器', '盔甲': '鎧甲', '头盔': '頭盔', '盾牌': '盾牌',
    '剑': '劍', '斧': '斧', '长柄': '長柄', '远程': '遠程',
    '法杖': '法杖', '钉头锤': '釘頭錘', '匕首': '匕首', '拳刃': '拳刃',
    '权杖': '權杖', '锤': '錘', '长柄/剑': '長柄/劍', '剑/锤/斧': '劍/錘/斧', '近战武器': '近戰武器', '头盔/盾牌': '頭盔/盾牌'
}

rw_tc = {
    "Ancient's Pledge": '遠古之誓', 'Beast': '野獸', 'Black': '黑色', 'Blood': '血液',
    'Bone': '骨骸', 'Bramble': '棘刺', 'Brand': '烙印', 'Breath of the Dying': '死亡呼吸',
    'Call to Arms': '戰爭召喚', 'Chaos': '渾沌', 'Chains of Honor': '榮耀之鍊', 'Crescent Moon': '新月',
    'Death': '死亡', 'Delirium': '迪勒瑞姆', 'Destruction': '毀滅', 'Doom': '末日',
    'Dragon': '龍', 'Dream': '夢境', 'Duress': '强制', 'Edge': '邊緣', 'Enigma': '謎團',
    'Enlightenment': '啟蒙', 'Eternity': '永恆', 'Exile': '流亡', 'Faith': '信仰',
    'Famine': '饑荒', 'Fortitude': '剛毅', 'Fury': '狂怒', 'Gloom': '幽暗', 'Grief': '悔恨',
    'Hand of Justice': '正義之手', 'Harmony': '和諧', 'Heart of the Oak': '橡樹之心', 'Heavenly' : '天堂',
    'Holy Thunder': '神聖雷擊', 'Honor': '榮耀', 'Ice': '冰強', 'Infinity': '無限',
    'Insight': '眼光', "King's Grace": '國王之慈悲', 'Kingslayer': '弒君者', 'Last Wish': '最後的願望',
    'Lawbringer': '執法者', 'Leaf': '葉子', 'Lionheart': '獅子心', 'Lore': '學識',
    "Lycander's": '萊肯德之', 'Malice': '惡意', 'Melody': '旋律', 'Memory': '記憶',
    'Mist': '迷霧', 'Myth': '神話', 'Nadir': '最低點', 'Oath': '誓言', 'Obedience': '遵從',
    'Passion': '熱情', 'Pattern': '圖案', 'Peace': '和平', 'Phoenix': '鳳凰', 'Plague': '瘟疫',
    'Principle': '原則', 'Prudence': '謹慎', 'Radiance': '光輝', 'Rain': '雨', 'Rift': '裂縫',
    'Sanctuary': '聖域', 'Silence': '沈默', 'Smoke': '煙霧', 'Spirit': '精神', 'Splendor': '燦爛',
    'Stealth': '隱密', 'Steel': '鋼鐵', 'Stone': '石塊', 'Strength': '力量', 'Treachery': '背信',
    'Unbending Will': '不屈意志', 'Venom': '毒液', 'Voice of Reason': '理性之聲', 'Wealth': '財富',
    'White': '白色', 'Wind': '風', 'Wrath': '憤怒', 'Zephyr': '微風', 'Flickering Flame': '搖曳之焰',
    'Obsidian': '黑曜石', 'Hustle': '疾速', 'Mosaic': '鑲嵌', 'Metamorphosis': '變形',
    'Bulwark': '防禦', 'Cure': '治療', 'Ground': '大地', 'Hearth': '爐火', 'Temper': '脾氣',
    'Void': '虛空', 'Ritual': '祭儀', 'Coven': '巫團', 'Authority': '權威', 'Vigilance': '警惕',
    'Hysteria': '歇斯底里', 'Mania': '狂躁'
}


for rw in rws:
    if 'name_zh' in rw:
        rw['name_sc'] = rw.pop('name_zh')
    
    rw['name_en'] = rw.get('name_en', rw.get('name', ''))
    rw['name_tc'] = rw_tc.get(rw.get('name', ''), rw.get('name_sc', ''))
    
    if 'base_types_zh' in rw:
        rw['base_types_sc'] = rw.pop('base_types_zh')
        
    bt_tc = []
    for b in rw.get('base_types_sc', []):
        bt_tc.append(base_map.get(b, b))
    rw['base_types_tc'] = bt_tc

with open('data/runewords.json', 'w', encoding='utf-8') as f:
    json.dump(rws, f, ensure_ascii=False, indent=2)

print("Done updating runewords.json and runes.json")
