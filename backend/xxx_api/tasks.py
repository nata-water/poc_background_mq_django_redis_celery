from __future__ import absolute_import, unicode_literals
from celery import shared_task


# 重いファイルのアップロード

# 重いファイルの読み込み

@shared_task
def do_something(param: str):
    text_data = "start"
    print("開始します")
    print("終了します")
    return text_data
