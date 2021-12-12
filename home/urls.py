from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
    path('actualités', views.actuality, name="actuality"),
    path('pageArticle/<str:pk>/', views.pageArticle, name="pageArticle"),

    ]




pages = [
    'dashboard',
    'about',
    'contact'
]

for page in pages:
    urlpatterns.append(
        path(
            page,
            views.PageView.as_view(template_name=f"home/{page}.html"),
            name=page
        )
    )
