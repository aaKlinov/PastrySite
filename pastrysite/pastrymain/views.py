
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout

from .models import *
from .forms import *
from .utils import *


class PastryHome(DataMixin, ListView):
    model = Recipes
    template_name = 'pastrymain/index.html'
    context_object_name = 'recipes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Recipes.objects.filter(is_published=True).select_related('category')
     

# def index(request):
#     recipes = Recipes.objects.all()
#     context = {'recipes': recipes,
#                'title': 'Главная страница',
#                'category_selected': 0,
#                }
#     return render(request, 'pastrymain/index.html', context=context)

def about(request):
    return render(request, 'pastrymain/about.html', {'title': 'О сайте'})

class AddRecipe(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddRecipeForm
    template_name = 'pastrymain/add_recipe.html'
    success_url = reverse_lazy('main')
    login_url = reverse_lazy('main')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление рецепта")
        return dict(list(context.items()) + list(c_def.items()))

def contact(request):
    return HttpResponse("Contact")

# def login(request):
#     return HttpResponse("Login")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')


class ShowRecipes(DataMixin, DetailView):
    model = Recipes
    template_name = 'pastrymain/recipes.html'
    slug_url_kwarg = 'recipes_slug'
    context_object_name = 'recipes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['recipes'])
        return dict(list(context.items()) + list(c_def.items()))

# def show_recipes(request, recipes_slug):
#     recipes = get_object_or_404(Recipes, slug=recipes_slug)

#     context = {'recipes': recipes,
#                'title': recipes.title,
#                'category_selected': recipes.category_id,
#                }
    
#     return render (request, 'pastrymain/recipes.html', context=context)

# def show_category(request, category_slug):
#     recipes = Recipes.objects.filter(category__slug=category_slug)

#     if len(recipes) == 0:
#         raise Http404

#     context = {'recipes': recipes,
#                'title': 'Отображение по категориям',
#                'category_selected': category_slug,
#                }
#     return render(request, 'pastrymain/index.html', context=context)


class RecipeCategory(DataMixin, ListView):
    model = Recipes
    template_name = 'pastrymain/index.html'
    context_object_name = 'recipes'
    allow_empty = False

    def get_queryset(self):
        return Recipes.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        read_categories = Categories.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(read_categories.name),
                                        category_selected=read_categories.pk)
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'pastrymain/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'pastrymain/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self) -> str:
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('login')