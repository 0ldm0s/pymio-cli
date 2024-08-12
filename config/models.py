# -*- coding: UTF-8 -*-
from mongoengine import *


class SystemConfig(Document):
    id = StringField(primary_key=True)
    val = BinaryField()
    create_at = LongField()
    update_at = LongField()
    meta = {
        "auto_create_index": True,
        "index_background": True,
        "indexes": [
            {"fields": ["#id"], "expireAfterSeconds": 3600},
        ]
    }
