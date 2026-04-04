# D2R WebUI 增强计划 v2：悬停提示、实时匹配、底材百科

## 背景
当前 WebUI 需要增加：实时匹配预览、属性悬停提示、折叠式公式、完整底材百科。
同时需要使用**真实游戏贴图**而非 emoji 图标。

---

## 具体需求

### 全局需求
- **鼠标悬停显示功能**：所有包含物品/装备信息的元素，鼠标悬停后应显示该物品的详细属性浮层。

### 需求 1：符文选择页 — 实时合成结果
- 在「选择材料」标签页中，用户选择符文后，**在当前页面**根据数据库的符文公式，**实时显示可合成的结果**。
- 匹配逻辑：对比用户已选符文与所有符文之语所需符文，计算匹配度。
- 结果展示：已完全匹配的显示在最前面，部分匹配的按匹配度排序。
- 每条结果应包含：符文之语名称、所需符文（标注已有/缺失）、适用底材类型。

### 需求 2：符文之语标签页 — 物品图标 + 属性悬停
- 每种符文之语卡片上，凡装备类型的，**添加物品图标**（使用真实游戏贴图）。
- 鼠标悬停物品图标后，**显示该符文之语的完整属性列表**（如 +2 All Skills、+45% FRW 等）。
- 属性数据来源：从 blizzhackers/d2data 仓库提取并转换为可读文本。

### 需求 3：合成公式标签页 — 折叠分组 + 图标 + 属性悬停
- 按功能将合成公式**分组折叠**（符文升级、打孔、装备升级、合成橙装、特殊、宝石、药水等）。
- 每组标题可点击展开/收起，带 ▶/▼ 指示器。
- 公式中涉及的物品**添加对应图标**。
- 鼠标悬停图标后，**显示该物品的属性信息**。

### 需求 4：底材百科 — 补充完整数据
- 当前底材百科缺乏数据，需要**联网检索**并补充完整的底材信息。
- 数据包含：所有盔甲、武器、盾牌等底材的名称（EN/SC/TC）、最大孔数、防御/伤害范围、力量/敏捷需求、等级需求、品质（普通/进阶/精华）。
- 每个底材行需要**物品图标**。
- 鼠标悬停后**显示物品属性**及推荐用途（适合做什么符文之语）。

---

## 数据来源

### 结构化数据
- **[blizzhackers/d2data](https://github.com/blizzhackers/d2data)** — 社区维护的完整 D2R 游戏数据仓库
  - `json/runes.json` (71KB) — 符文之语属性（含内部属性编码 T1Code/T1Min/T1Max）
  - `json/armor.json` (367KB) — 全部盔甲底材
  - `json/weapons.json` (528KB) — 全部武器底材
  - `json/itemstatcost.json` — 属性编码→人类可读名称映射

### 物品图标
- **diablo2.io** CDN — 使用公开 URL 模式引用物品贴图（本地使用，无版权问题）
  - 符文图标: `https://diablo2.io/styles/zulu/theme/images/icons/{rune_lowercase}2x.png`
  - 物品图标: `https://diablo2.io/styles/zulu/theme/images/items/{item_slug}_ticon.png`
  - slug 规则: 物品英文名去空格小写（如 `Archon Plate` → `archonplate`）

---

## User Review Required

> [!IMPORTANT]
> **图标加载方式**：图标直接从 diablo2.io CDN 加载（热链接）。由于你是本地使用，这没有问题。如果后续需要离线使用，可以额外写一个脚本将所有图标下载到本地 `assets/` 目录。

> [!WARNING]
> **属性数据处理**：blizzhackers/d2data 使用的是游戏内部属性编码（如 `res-cold`、`dmg%`、`swing2`），需要编写转换脚本将其映射为人类可读文本（如 `+30% Cold Resistance`、`+120% Enhanced Damage`、`+15% Increased Attack Speed`）。这需要额外的 `itemstatcost.json` 映射表。是否可以先用手工整理的属性文本（从 wiki 抓取），后续再接入自动化解码？

---

## Proposed Changes

### 步骤 1: 数据准备

#### [NEW] Python 脚本: 从 d2data 提取属性并注入 runewords.json
- 从 `blizzhackers/d2data/json/runes.json` 提取 `T1Code*`/`T1Min*`/`T1Max*`
- 转换为人类可读的 `stats` 数组（英文）
- 注入到我们的 `data/runewords.json`

#### [NEW] [base_items.json](file:///Users/yara/Developer/Games/D2R/data/base_items.json)
- 从 `armor.json` + `weapons.json` 提取关键字段
- 按类别分组，含：name_en/name_sc/name_tc、max_sockets、defense/damage、str_req、level_req、tier
- 添加 `icon_slug` 字段用于构建 diablo2.io 图标 URL

---

### 步骤 2: index.html 重构

#### A. 全局 Tooltip 悬停系统
```css
#tooltip { position:fixed; z-index:9999; ... }  /* 暗黑哥特风格浮层 */
```
- `showTooltip(html, event)` / `hideTooltip()` 全局函数
- 跟随鼠标位置，自动避免边界溢出

#### B. 符文选择页 — 实时合成预览
- 符文网格下方新增 `<div id="matchPreview">`
- 选择符文后实时计算可合成项，按匹配度 100% → 50%+ → <50% 排序
- 每个匹配使用小卡片：含物品图标 + 名称 + 已有/缺失符文

#### C. 符文之语卡片 — 物品图标 + 属性 Tooltip
- 卡片左侧增加 `<img>` 物品图标（从 diablo2.io CDN 加载）
- 鼠标悬停→Tooltip 显示完整属性列表
- 属性文字：蓝色=普通修正，金色=独有属性

#### D. 合成公式 — 折叠分组
- 每个 `recipe-group-title` 改为可点击
- 默认展开，点击切换 ▶/▼ + 隐藏/显示内容区
- 记住展开状态

#### E. 底材百科 — 完整重做
- 左侧分类带物品图标缩略图
- 右侧表格：增加防御/伤害范围列 + 图标列
- 悬停行→Tooltip 显示推荐用途及适合的符文之语

---

## Verification Plan

### Automated Tests
- 检查 `runewords.json` 所有 100 条均有 `stats` 数组
- 检查图标 URL 前 5 个是否可访问 (HTTP 200)
- 浏览器测试：选择符文、切换标签、悬停显示

### Manual Verification
- 用户浏览器操作验证
