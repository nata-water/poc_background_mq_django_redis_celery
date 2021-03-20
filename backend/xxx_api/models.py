from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from django_celery_results.models import TaskResult
import uuid


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class BinaryResource(models.Model):
    """BinaryResource

    * 外部から入力されたバイナリデータを管理します
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=500, null=False)
    # 拡張子
    extension = models.CharField(max_length=100)
    # ファイル種類
    type = models.CharField(max_length=100)
    # ファイルURL
    url = models.URLField(null=True, blank=True)
    binary_data = models.BinaryField()

    def __str__(self):
        return f"{self.name} {self.type} {self.extension}"


class ParseResult(models.Model):
    """ParseResult

    * 非同期ジョブによって解析された結果を管理します
    """

    # celeryタスク結果情報
    # mq_info = models.ForeignKey(
    #     TaskResult,
    #     on_delete=models.CASCADE,
    #     unique=False,
    #     to_field="task_id",
    #     db_column="mq_task_id",
    # )
    # CeleryタスクID
    task_id = models.CharField(max_length=255, null=True, blank=True)
    header = models.CharField(max_length=2000, null=True, blank=True)
    body = models.CharField(max_length=10000, null=True, blank=True)
    # 結果格納先URL情報。  BadPracticeだが致し方なし。
    url = models.URLField(null=True)
    # 格納先テーブル情報。 BadPracticeだが致し方なし。格納先のテーブルポインタ
    table = models.CharField(max_length=100, null=True, blank=True)
    # 横持ちカラム。同様にBadPracticeだが致し方なし。
    column0001 = models.CharField(max_length=1000, null=True, blank=True)
    column0002 = models.CharField(max_length=1000, null=True, blank=True)
    column0003 = models.CharField(max_length=1000, null=True, blank=True)
    column0004 = models.CharField(max_length=1000, null=True, blank=True)
    column0005 = models.CharField(max_length=1000, null=True, blank=True)
    column0006 = models.CharField(max_length=1000, null=True, blank=True)
    column0007 = models.CharField(max_length=1000, null=True, blank=True)
    column0008 = models.CharField(max_length=1000, null=True, blank=True)
    column0009 = models.CharField(max_length=1000, null=True, blank=True)
    column0010 = models.CharField(max_length=1000, null=True, blank=True)
    column0011 = models.CharField(max_length=1000, null=True, blank=True)
    column0012 = models.CharField(max_length=1000, null=True, blank=True)
    column0013 = models.CharField(max_length=1000, null=True, blank=True)
    column0014 = models.CharField(max_length=1000, null=True, blank=True)
    column0015 = models.CharField(max_length=1000, null=True, blank=True)
    column0016 = models.CharField(max_length=1000, null=True, blank=True)
    column0017 = models.CharField(max_length=1000, null=True, blank=True)
    column0018 = models.CharField(max_length=1000, null=True, blank=True)
    column0019 = models.CharField(max_length=1000, null=True, blank=True)
    column0020 = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"ParseResult{self.id} {self.header}"
