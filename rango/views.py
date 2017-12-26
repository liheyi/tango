from django.shortcuts import render
from rango.models import Category
from rango.models import Page

def index(request):

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    cats_list = Category.objects.order_by("-likes")[:5]

    #  Place the list in our context_dict dictionary
    #+ that will be passed to the template engine.
    context_dict = {'categories': cats_list}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)

    # A single statement.
    # But as a novice,
    # I don't know what it means.
    # return render(request,
    #               'rango/index.html',
    #               {'categories': Category.objects.order_by("-likes")[:5]})


def about(request):

    return render(request, 'rango/about.html', {})


def show_category(request, category_name_slug):

    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a 'DoesNotExist' exception.
        # So the .get() method return one model instance or raise an exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # Note that filter() method will return
        # a list of page objects or an empty list.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages

        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for you.
        context_dict['pages'] = None
        context_dict['category'] = None

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)
