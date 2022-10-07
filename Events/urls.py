from django.urls import path
from .views import event_list, create_event, book_ticket, update_event, event_detail

app_name = "Events"

urlpatterns = [
    path('eventlist/',event_list, name='event-list'),
    path('create_event/',create_event, name='create-event'),
    path('ticket/',book_ticket, name='book-ticket' ),
    path('update/',update_event, name='update-event'),
    path('<int:pk>/event_detail/',event_detail, name='event-detail')
]
