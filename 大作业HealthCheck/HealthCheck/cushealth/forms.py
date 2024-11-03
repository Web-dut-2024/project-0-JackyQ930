from django import forms
from .models import CustomerHealth

class CustomerHealthForm(forms.ModelForm):
    class Meta:
        model = CustomerHealth
        fields = ['name', 'uId', 'sex', 'health_status', 'content']
        labels = {
            'name': '姓名',
            'uId': '身份证',
            'sex': '性别',
            'health_status': '健康状态',
            'content': '内容',
        }
        help_texts = {
            'name': '请输入您的姓名',
            'uId': '请输入您的身份证号码',
            'sex': '请选择您的性别',
            'health_status': '请选择健康状态',
            'content': '请输入内容（最多150个字）',
        }
