from django.urls import path

from . import views 

urlpatterns = [
    path('homeseller/',views.homeseller,name="sellerhome"),
    # path('add_product/',views.add_product,name="add_product"),
    # path('update/<int:pk>/', views.ProductUpdateview.as_view() , name='product_update'),
    # path('delete/<int:pk>/',views.ProductDeleteView.as_view() , name = 'produst_delete'),
    path('signup/', views.signup_User, name="signup1"),
    path('home/',views.homebuyer,name="buyer_home"),

    path('login_user/',views.login_user,name="login_user"),
    path('',views.home,name="seller_home"),
    path('add_product/', views.add_product, name="add_product"),
    path('update/<int:pk>/', views.ProductUpdateview.as_view() , name='product_update'),
    path('delete/<int:pk>/',views.ProductDeleteView.as_view() , name = 'produst_delete'),
    path('logout_user/', views.logout_user, name ='logout_user'),
    path('profile_user/', views.profile_user, name ='profile'),
    path('update_pro/', views.updateprofile , name='update_pro'),
    path('next/',views.next,name='next_user'),
    path('cart1/', views.buyer_cart, name="buyer_cart1"),
    path('cartsave/',views.cart_save, name = 'cart_save1'),
    path('cartdelete/<int:id>/',views.delcart,name='delcart'),
    path('order/<int:cart_id>',views.order_now,name="order_now"),
    path('order_see/',views.order_view,name="order_see"),
    path('commentbuyer1/',views.commentbuyer,name="commentbuyer1"),
    path('seecomment/',views.commentsee,name="commentsee"),
    path('order_del/<int:id>/',views.order_del,name="oredre_del"),
    path('login_user2/',views.login_user2,name="login_user2"),


]
