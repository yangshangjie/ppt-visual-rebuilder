# PPT Visual Rebuilder User Guide

> A production-grade, human-in-the-loop workflow for high-fidelity PPT visual reconstruction and editable PPTX generation.

## 术语说明

本文第一次出现关键概念时采用中文加英文括注，后续统一使用中文表达：

- 手搓 PPT（Hand-crafted structural PPT prototype）
- 拼图（Style mosaic）
- 单页高清视觉稿（High-fidelity slide visual）
- 反推（Reverse engineering）
- 人工确认节点（Human approval gates）
- 可编辑 PPTX 重建（Editable PPTX reconstruction）

## 1. 这个 Skill 是做什么的

`ppt-visual-rebuilder` 用于一套受控的 PPT 视觉生产流程：

1. 反推 PPT 内容结构
2. 生成整套 PPT 风格拼图
3. 人工确认视觉方向
4. 扩展逐页单页高清视觉稿
5. 修正中文错字、数字、页码、Dashboard 模块
6. 最终确认后，重建可编辑 PPTX

它不是“让 AI 从零自由发挥做 PPT”。正确用法是：先用 GPT 整理内容，再制作一版手搓 PPT 锁定结构，确认没问题后，再交给 Codex 用这个 skill 做视觉化和后续复刻。

## 2. 推荐完整工作流

### 第一步：用 GPT 整理资料，生成 PPT 框架

先把你的需求、文档、产品资料、销售材料、会议纪要、截图、表格等交给 GPT，让它整理出 PPT 框架。

目标是先确定：

- 讲什么
- 分几章
- 每页讲什么
- 每页承担什么作用
- 哪些页面需要图表、流程、产品图或截图

不要一开始就生成 PPT 文件。

### 第二步：自己制作一版手搓 PPT

根据 GPT 生成的框架，自己手搓一份基础 PPT。

手搓的目的不是为了好看，而是为了给 AI 限定结构：

- 哪页是封面
- 哪页是目录
- 哪页是章节页
- 哪页是痛点页
- 哪页是方案架构
- 哪页是流程图
- 哪页是驾驶舱
- 哪页是价值页
- 哪页是实施计划
- 哪页是结尾页

手搓 PPT 要重点控制：

- 页数
- 页序
- 标题
- 核心观点
- 模块数量
- 图表位置
- 关键产品名、数字、术语
- 必须保留的截图和素材

### 第三步：反复让 GPT 优化手搓 PPT

把手搓 PPT 或逐页截图交给 GPT，让它帮你检查：

- 汇报逻辑是否顺
- 每页标题是否有力
- 信息量是否合适
- 哪些页需要拆分或合并
- 哪些页缺少结论
- 哪些页需要强化视觉表达

你根据建议继续手动调整 PPT。

### 第四步：确认 PPT 骨架

进入 Codex 前，先确认手搓 PPT 已经稳定：

- 页面数量确定
- 页面顺序确定
- 每页结构确定
- 关键文字和数字确定
- 需要保留的产品图、截图、品牌元素准备好

如果骨架还不稳定，不建议进入视觉 拼图 阶段。

## 3. Skill 包里有哪些文件

当前 skill 包采用仓库相对路径组织。

核心文件：

- [SKILL.md](../SKILL.md)  
  Skill 主说明，包含触发场景、强制 人工确认节点、输出路径、反幻觉规则。

- [workflow.md](../references/workflow.md)  
  详细工作流说明，适合执行端到端流程时参考。

- [prompts.md](../references/prompts.md)  
  正式提示词库。需要复制提示词时优先看这个文件。

- [validation_checklist.md](../references/validation_checklist.md)  
  各阶段验收标准，包括大纲、拼图、单页、中文、Dashboard、最终 PPTX。

- [overlay_text.py](../scripts/overlay_text.py) 
  中文错字和关键文字的确定性覆盖修复脚本。

- [examples](../examples/)  
  示例目录，包含原始需求、大纲、拼图提示词、单页提示词、PPTX 重建提示词示例。

## 4. 正式执行时优先使用 prompts.md

手册里的提示词只是说明用，真正执行时优先复制：

[prompts.md](../references/prompts.md)

里面已经包含：

- GPT 资料整理成 PPT 框架
- GPT 优化手搓 PPT
- Codex 反推手搓 PPT 大纲
- 生成 3 版 PPT 拼图
- 拼图不满意时重做
- 拼图确认后扩展逐页视觉稿
- 批量生成逐页视觉稿
- 按截图重做某一页
- 修正中文错字
- 禁止处理试用水印
- 进入 PPTX 复刻

## 5. Codex 调用方式

当手搓 PPT 已经确认后，可以这样开始：

```text
$ppt-visual-rebuilder
请阅读我上传的手搓 PPT，反推完整 PPT 大纲和逐页内容。

每页请包含：
1. 标题
2. 核心观点
3. 正文要点
4. 视觉建议
5. 需要保留的关键文字、数字、产品名或截图
6. 无法识别、需要我确认的内容

当前阶段不要生成 PPT 文件，也不要生成视觉 拼图。
请先输出大纲，等我确认后再继续。
```

## 6. 必须遵守的人工确认节点

这个 skill 不能一路自动生成到底，必须在关键节点停下来。

### 节点 1：大纲确认

Codex 反推大纲后，你需要检查：

- 章节是否正确
- 页数是否正确
- 页序是否正确
- 每页标题是否正确
- 核心观点是否准确
- 有没有漏页
- 有没有理解错业务含义

确认后再说：

```text
大纲确认，继续生成视觉 拼图。
```

### 节点 2：拼图确认

Codex 生成多版拼图 后，你需要选择方向。

如果不满意，可以说：

```text
第二版方向对，但还不够科技。
请基于第二版加强黑银蓝、AI 中枢、数据驾驶舱、硬件主视觉，重新生成一版。
```

如果满意，可以说：

```text
这版拼图确认，按这版继续扩展逐页高清视觉稿。
```

### 节点 3：逐页生成确认

进入逐页视觉稿前，需要明确生成方式：

```text
确认按这版拼图生成逐页 单页高清视觉稿。
每次只生成一页，关键页让我确认。
```

或者：

```text
确认批量生成全部页面，生成完后我统一检查。
```

### 节点 4：关键页确认

以下页面必须重点检查：

- 封面
- 方案架构页
- 流程页
- 驾驶舱页
- 价值/KPI 页
- 实施计划页
- 结尾页
- 任何使用用户截图的页面

重点检查：

- 中文有没有错字
- 产品名是否正确
- 数字是否正确
- 模块数量是否正确
- 页码是否正确
- 是否新增了未经确认的数据
- 是否出现水印、乱码、假 logo

### 节点 5：PPTX 生成确认

只有当所有逐页视觉稿都确认后，才进入可编辑 PPTX 重建 阶段。

确认语：

```text
所有逐页视觉稿确认，可以开始生成可编辑 PPTX 重建。
请严格参考这些单页高清视觉稿进行复刻。
```

## 7. 输出目录规范

所有用户可见成果必须放在当前项目的 `outputs/` 下。

推荐目录：

```text
outputs/mosaics/
outputs/slides/
outputs/corrected/
outputs/pptx/
```

命名规范：

```text
outputs/mosaics/mosaic-v1.png
outputs/mosaics/mosaic-v2.png
outputs/mosaics/mosaic-v3.png

outputs/slides/slide-01.png
outputs/slides/slide-02.png
outputs/slides/slide-03.png

outputs/corrected/slide-10-corrected.png
outputs/corrected/slide-15-corrected.png

outputs/pptx/final-deck.pptx
```

不要把最终成果只留在图片生成工具的默认目录里。

## 8. 验收标准

正式验收时参考：

[validation_checklist.md](references/validation_checklist.md)

里面包含：

- PPT 大纲验收标准
- 拼图验收标准
- 单页高清视觉稿验收标准
- 中文文字验收标准
- Dashboard / 截图还原页验收标准
- 最终 PPTX 验收标准

简要标准：

- 大纲：页数、页序、标题、核心观点正确。
- 拼图：包含所有页面，页序正确，风格统一。
- 单页：必须是独立高清 16:9，不允许裁切拼图充当成品。
- 中文：标题、产品名、数字、页码必须准确。
- Dashboard：模块数量、区域比例、信息层级必须严格参考截图。
- PPTX：尽量可编辑，渲染检查无错字、遮挡、重叠、溢出。

## 9. 反幻觉约束

使用这个 skill 时必须遵守：

- 不允许新增未经确认的业务数据。
- 不允许新增未经确认的客户名称。
- 不允许新增未经确认的金额、KPI、百分比、服务承诺。
- 无法识别的内容必须标记为“需用户确认”。
- 截图类页面必须严格保留模块数量、区域比例和信息层级。
- 中文标题、关键指标、页码优先保证准确，不要为了视觉效果牺牲文字正确性。

## 10. 中文错字修复方式

AI 生成图片时，中文容易出错，尤其是：

- 销售
- 数字化
- 驾驶舱
- 解决方案
- 企业名称
- 产品名称

如果只是文字错了，画面整体可用，不要反复让图片模型猜字，优先用：

[overlay_text.py](scripts/overlay_text.py)

示例：

```bash
python overlay_text.py \
  --input outputs/slides/slide-15.png \
  --output outputs/corrected/slide-15-corrected.png \
  --box 520,70,1800,220 \
  --text "让AI赋能销售，让数据驱动增长" \
  --font-size 72 \
  --text-color 246,250,255,255 \
  --box-color 0,0,0,255
```

脚本支持：

- 自动检测中文字体
- Windows 优先微软雅黑
- macOS / Linux fallback 到 Noto Sans CJK、SimHei、Arial Unicode 等
- 输入/输出图片
- 修复文字
- 坐标
- 字号
- 文字颜色
- 背景色
- 圆角
- 对齐方式

## 11. 禁止事项

### 不要跳过手搓 PPT

手搓 PPT 是结构母版，没有它，AI 很容易跑偏。

### 不要跳过确认节点

大纲没确认，不生成拼图。  
拼图没确认，不生成单页。  
单页没确认，不生成 PPTX。

### 不要裁切拼图当单页

拼图只是视觉母版，不能裁切后当成逐页高清视觉稿。

### 不要编造数据

看不清就标“需用户确认”，不要自己补客户名、金额、KPI、日期。

### 不要强行去水印

如果是第三方试用水印，不能直接去除。正确做法是使用正式授权导出、提供无水印原图，或重新生成无水印版本。

## 12. 推荐工作节奏

1. GPT 整理资料，生成 PPT 框架
2. 人工手搓 PPT，限定每页结构
3. GPT 反复优化手搓 PPT
4. 人工确认 PPT 骨架
5. Codex 使用 `$ppt-visual-rebuilder` 反推大纲
6. 人工确认大纲
7. Codex 生成多版拼图
8. 人工选择或要求重做视觉方向
9. Codex 逐页生成高清视觉稿
10. 人工复核关键页
11. Codex 修正错字、模块、图表问题
12. 人工确认全部视觉稿
13. Codex 生成可编辑 PPTX 重建

## 13. 一句话总结

这套 skill 的核心不是“让 AI 直接做 PPT”，而是：

**先用 GPT 梳理内容，再用人工手搓 PPT 锁定结构，确认无误后，再让 Codex 按受控流程完成高质量视觉化和后续 PPTX 复刻。**
