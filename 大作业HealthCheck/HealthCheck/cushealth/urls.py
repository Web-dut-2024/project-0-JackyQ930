from django.urls import path
from .views import (
    health_check_list,
    add_health_check,
    edit_health_check,
    delete_health_check,
    search_health_check,
)

urlpatterns = [
    path(
        "health-check/", health_check_list, name="health_check_list"
    ),  # 显示体检记录列表
    path("health-check/add/", add_health_check, name="add_health_check"),  # 添加新记录
    path(
        "health-check/edit/<int:pk>/", edit_health_check, name="edit_health_check"
    ),  # 编辑记录
    path(
        "health-check/delete/<int:pk>/", delete_health_check, name="delete_health_check"
    ),  # 删除记录
    path("add/", add_health_check, name="add_health_check"),
    path("search/", search_health_check, name="search_health_check"),  # 添加查询路径
]
