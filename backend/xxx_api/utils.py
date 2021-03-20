from django.db.models import Model
from xxx_api.consts import GENERAL_COLUMN_DIGITS, GENERAL_COLUMN_PREFIX


def is_exists_model_field(clazz: Model, field_name):
    """対象のDjangoモデルに指定したフィールドが存在するかどうかをチェックします

    :param clazz: {Model}
    :param field_name:  {str}
    :return: {bool}
    """
    return field_name in set(x.name for x in clazz._meta.fields)


def do_index_to_column_name(index):
    """インデックスを汎用カラム名に変換します

    :param index: {int}
    :return: {str}
    """
    zero_index_str = str(index).zfill(GENERAL_COLUMN_DIGITS)
    return f"{GENERAL_COLUMN_PREFIX}{zero_index_str}"
