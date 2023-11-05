import ujson
import os

with open("text.json", 'r') as json_file:
    json_data = json_file.read()
    json_dict = ujson.loads(json_data)

print(json_dict)

# 複雑なデータ構造の辞書を定義
#complex_data = {
#    "name": "Complex Example",
#    "version": 1.0,
#    "description": "A complex JSON example with nested structures.",
#    "contributors": [
#        {"name": "Alice", "email": "alice@example.com"},
#        {"name": "Bob", "email": "bob@example.com"}
#    ],
#    "data": {
#        "items": [
#            {
#                "id": 1,
#                "type": "data point",
#                "attributes": {
#                    "length": 5.1,
#                    "width": 3.5,
#                    "height": 1.2
#                },
#                "tags": ["example", "sample", "item1"]
#            },
#            {
#                "id": 2,
#                "type": "data point",
#                "attributes": {
#                    "length": 6.2,
#                    "width": 2.4,
#                    "height": 2.3
#                },
#                "tags": ["example", "sample", "item2"]
#            }
#        ],
#        "metrics": {
#            "count": 2,
#            "size": "medium"
#        }
#    },
#    "status": "active",
#    "is_public": True
#}
#
## JSON文字列に変換（整形された形式）
#json_str = ujson.dumps(complex_data, indent=4)
#
## JSON文字列をファイルに書き込む
#with open("text.json", "w") as json_file:
#    json_file.write(json_str)
#

