import json

with open('data/cube_recipes.json', 'r', encoding='utf-8') as f:
    recipes = json.load(f)

# Helper function to convert text safely
def get_tc(text):
    if not text:
        return text
    # Very basic manual conversions for this specific context
    conversions = {
        '符文升级': '符文升級', '低级符文': '低級符文', '中级符文': '中級符文', '高级符文': '高級符文',
        '打孔公式': '打孔公式', '装备打孔': '裝備打孔', '装备升级': '裝備升級', '特殊公式': '特殊公式',
        '合成橙装': '合成橙裝', '宝石升级': '寶石升級', '药水合成': '藥水合成', '武器': '武器',
        '盔甲': '鎧甲', '头盔': '頭盔', '盾牌': '盾牌', '近战武器': '近戰武器', '完美宝石': '完美寶石',
        '任意宝石': '任意寶石', '碎裂宝石': '碎裂寶石', '无瑕疵宝石': '無瑕疵寶石', '法杖': '法杖',
        '护身符': '護身符', '项链': '項鍊', '戒指': '戒指', '珠宝': '珠寶',
        '打孔': '打孔', '升级': '升級', '洗属性': '洗屬性', '洗装备': '洗裝備', '属性随机': '屬性隨機'
    }
    for sc, tc in conversions.items():
        text = text.replace(sc, tc)
    return text

for cat_key, cat_data in recipes.items():
    if 'description' in cat_data:
        cat_data['description_tc'] = get_tc(cat_data['description'])
    
    if 'recipes' in cat_data:
        for r in cat_data['recipes']:
            if 'name_zh' in r:
                r['name_sc'] = r.pop('name_zh')
            r['name_tc'] = get_tc(r.get('name_sc', ''))
            
            # Since formula and result are mixed with english runes, we'll keep it simple
            if 'formula' in r:
                r['formula_tc'] = get_tc(r['formula'])
            if 'result' in r:
                r['result_tc'] = get_tc(r['result'])
            if 'notes' in r:
                r['notes_tc'] = get_tc(r['notes'])
                
    if 'types' in cat_data: # For crafting
        for t in cat_data['types']:
            if 'type_zh' in t:
                t['type_sc'] = t.pop('type_zh')
            t['type_tc'] = get_tc(t.get('type_sc', ''))
            if 'guaranteed_stats' in t:
                t['guaranteed_stats_tc'] = get_tc(t['guaranteed_stats'])
    if 'rules' in cat_data:
        cat_data['rules_tc'] = [get_tc(rule) for rule in cat_data['rules']]

with open('data/cube_recipes.json', 'w', encoding='utf-8') as f:
    json.dump(recipes, f, ensure_ascii=False, indent=2)

print("Done updating cube_recipes.json")
