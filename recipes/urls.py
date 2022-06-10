from django.urls import path

from recipes.views import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView,
    log_rating,
    shoppingitems_create,
    shoppingitems_delete,
    ShoppingItemsListView,
    RecipeDetailView,
    RecipeListView,
    UserListView
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
    path("", UserListView.as_view(), name="user_list"),
    path("shoppingitems/create/", shoppingitems_create, name="shoppingitems_create"),
    path("shopping_items/delete/", shoppingitems_delete, name="shoppingitems_delete"),
    path("", ShoppingItemsListView.as_view(), name="shoppingitems_list")
]
