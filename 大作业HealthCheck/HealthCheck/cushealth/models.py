from django.db import models


class CustomerHealth(models.Model):
    HEALTH_CHOICES = [
        ("A", "健康"),
        ("B", "亚健康"),
        ("C", "不健康"),
        ("D", "已逝"),
    ]

    name = models.CharField(max_length=100)
    uId = models.CharField(max_length=18, unique=True)  # 身份证号
    sex = models.CharField(max_length=10)
    health_status = models.CharField(max_length=1, choices=HEALTH_CHOICES)
    content = models.CharField(max_length=150, blank=True)  # 内容字段

    def __str__(self):
        return f"{self.name} - {self.uId}"
