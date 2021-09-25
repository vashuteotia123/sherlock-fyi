
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from quest import views as quest_view
from quiz import views as quiz_view

urlpatterns = [
	path('admin/', admin.site.urls),
	# path('register/', quest_view.register, name='register'),
	# path('faq/', quiz_view.faq, name='faq'),
	# path('profile/edit/', quest_view.edit, name='edit'),
	path('login/', auth_views.LoginView.as_view(template_name='quest/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='quest/logout.html'), name='logout'),
	# path('profile/', quest_view.profile, name='profile'),
	# path('profile/password/', quest_view.change_password, name='change_password'),
	path('question/', quiz_view.question, name='question'),
	path('', quest_view.home, name='home'),
	path('quiz/', quiz_view.quiz, name='quiz'),
	path('leaderboard/', quiz_view.leaderboard, name='leaderboard'),
	path('completed/', quiz_view.completed, name='completed'),
    path('tinymce/', include('tinymce.urls')),
	path('map/', quiz_view.map, name='map'),
	path('ckeditor/',include('ckeditor_uploader.urls'))
]


