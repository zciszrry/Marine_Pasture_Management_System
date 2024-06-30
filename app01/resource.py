from import_export import resources
from app01.models import Staff,Account
class StaffResource(resources.ModelResource):
    # 此处可写方法以添加更多功能
    class Meta:
        model = Staff
        # fields内的模型字段会被导入导出, exclude内的会被排除在外，如果都不写，默认为模型中的全部字段都要包含。
        fields=[
            'id',
            'name',
            'position',
            'gender',
            'age',
            'phone_number',
            'state',
        ]
        excloud = (

        )
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ('id', 'name')
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ['id']


class AccountResource(resources.ModelResource):
    # 此处可写方法以添加更多功能
    class Meta:
        model = Account
        # fields内的模型字段会被导入导出, exclude内的会被排除在外，如果都不写，默认为模型中的全部字段都要包含。
        fields=[
            'id',
            'username',
            'password',
        ]
        excloud = (

        )
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ('id', 'username')
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ['id']






