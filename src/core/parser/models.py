"""Модуль"""

from dataclasses import dataclass


@dataclass
class EoraInfo:
    case_: str
    description: str


# {
#     "catagory_1": {
#         1: {
#             "case_for": "some case",
#             "description": [
#                 "text1",
#                 "text2",
#             ],
#             "link": "some link",
#         },
#     },
# }
