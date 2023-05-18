from django.urls import path, re_path
from django.views.decorators.cache import cache_page


from .views import *

urlpatterns = [
    path('', PastryHome.as_view(), name='main'),
    path('about/', about, name='about'),
    path('add_recipe', AddRecipe.as_view(), name='add_recipe'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('recipes/<slug:recipes_slug>', ShowRecipes.as_view(), name='recipes'),
    path('category/<slug:category_slug>', RecipeCategory.as_view(), name='category'),
]