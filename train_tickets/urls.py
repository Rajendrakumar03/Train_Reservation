from django.urls import path
from .views import PurchaseTicketAPI,ReceiptDetailAPI,UserBySectionAPI,RemoveUser,ModifySeatAPI,Registration

urlpatterns = [
    path('register/',Registration.as_view({'post':'post'}),name='register'),

    path('purchase/', PurchaseTicketAPI.as_view({'get':'get','post':'post'}),name='purchase_ticket'),
    path('receipt/',ReceiptDetailAPI.as_view({'get':'get'}),name='receipt_detail'),
    path('users/section/',UserBySectionAPI.as_view({'get':'get'}),name='user_by_section'),
    path('users/',UserBySectionAPI.as_view({'get':'get_all_users'}),name='users_list'),

    path('remove/user/',RemoveUser.as_view({'delete':'destroy'}),name='remove_user'),
    path('modify/seat/',ModifySeatAPI.as_view({'put':'update'}),name='modify_seat'),

]
