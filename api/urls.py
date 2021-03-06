from django.urls import path
from .views import CommentRecordsView, VisualRecordsView, UserRecordView, VideoRecordsView

app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('video/', VideoRecordsView.as_view(), name='videos'),
    path('visual/', VisualRecordsView.as_view(), name='visuals'),
    path('comment/',CommentRecordsView.as_view(), name='comments'),
]