from __future__ import absolute_import, unicode_literals
from celery import shared_task, current_task
import uuid
import io
import pandas as pd
from django_celery_results.models import TaskResult

from xxx_api.models import BinaryResource, ParseResult
from xxx_api.utils import do_index_to_column_name, is_exists_model_field


@shared_task
def do_something(param: str):
    text_data = "start"
    print("開始します")
    print("終了します")
    return text_data


@shared_task
def do_parse_resource(resource_id: uuid, spec_task_result=None):
    current_task_id = current_task.request.id
    print("current_task_idです：" + current_task_id)

    # ここでタスクIDをもとにTaskResultからデータを取得しようとしても取得できない
    # current_task_result = TaskResult.objects.get(task_id=current_task_id)
    resource = BinaryResource.objects.get(id=resource_id)
    df = pd.read_excel(io.BytesIO(resource.binary_data))

    for index, row in df.iterrows():
        result = ParseResult()
        result.header = df.columns
        for i in range(row.size):
            field_name = do_index_to_column_name(i + 1)
            if is_exists_model_field(ParseResult, field_name):
                # 結果オブジェクトの各汎用項目を設定する
                result.__setattr__(field_name, row[i])
        # FIXME: 現在実行中のCeleryタスクインスタンスを取得する方法を調べる必要がある
        # result.mq_info.task_id = current_task_id
        result.task_id = current_task_id
        result.save()
    return f"{resource.name}をParseResultに格納しました"
