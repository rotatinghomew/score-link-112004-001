# 跨赛卷等值与晋级占位

赛区口试的原始交卷、校准试评和席位往来。分数范围为 0 至 100；轮次在赛道内解释，参考卷和名额在赛道政策中登记。 数据均为合成。

CSV 使用 UTF-8、首行字段名，`-` 表示来源未填；JSON 使用原生布尔、字符串及数字。没有另行给定时，`seq` 只用于还原各条来件的先后，不是业务日期。

## 来源说明

- `links.csv`：锚点答卷只供试评。有效列的 0 表示作废；同地点共用评阅环境。
- `entries.csv`：原分不含锚点。序号是有效分相同时的优先顺序（小值优先），与录入顺序无关。
- `appeals.json`：复核的候选分仅用于未裁决时；anchor 指定原锚点行，裁定后的有效状态替代旧状态。
- `offers.csv`：邀请回执通过同一邀请编号关联；pending、accepted、declined、expired 分别为已发未答、接受、谢绝和到期。

## 数据清单

- `policies.json`：配置对象。
- `links.csv`：`id`, `paper_a`, `paper_b`, `score_a`, `score_b`, `location`, `valid`。
- `entries.csv`：`person`, `track`, `round`, `region`, `paper`, `score`, `tiebreak`。
- `appeals.json`：记录数组。
- `offers.csv`：`seq`, `offer`, `person`, `state`。

## 本地检查

使用 Python 3.11 标准库，无需安装第三方依赖。构建检查和来源契约测试：

```sh
python3 -m compileall -q tests
python3 -m unittest discover -s tests -v
```
