from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView
)


urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/',TaskDetailView.as_view(), name='task-retrieve-update-delete'),
    # path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    # path('employees/<int:pk>/', EmployeeRetrieveUpdateDeleteView.as_view(), name='employee-retrieve-update-delete'),
    # path('employees/<int:pk>/tasks/', EmployeeTasksListView.as_view(), name='employee-tasks-list'),
]
