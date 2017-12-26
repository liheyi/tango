import random

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():

    #  First, we will create lists of dictionries containing the pages
    #+ we want to add into each category
    #  Then we will create a dictionary of dictionaries for our categories.
    #  This might seem a little bit confusing, but it allows us to iterate
    #+ through each data structure, and add the data to our models.
    python_pages = [
        {
         'title': "Official Python Tutorial",
         'url': "https://docs.python.org/3.5/tutorial/index.html",
         'views': random.randint(50, 100),
         'likes': random.randint(20, 50)
        },

        {
         'title': "How to Think like a Computer Scientist",
         'url': "http://greenteapress.com/wp/think-python-2e/",
         'views': random.randint(50, 100),
         'likes': random.randint(20, 50)
        },

        {
         'title': "Learn Python in 10 Minutes",
         'url': "https://www.stavros.io/tutorials/python/",
         'views': random.randint(50, 100),
         'likes': random.randint(20, 50)
        }
    ]

    django_pages = [
        {
         'title': "Official Django Tutorial",
         'url': "https://docs.djangoproject.com/en/1.11/",
         'views': random.randint(50, 100),
         'likes': random.randint(20, 50)
        },

        {
         'title': "Django Rocks",
         'url': "https://www.djangorocks.com/",
         'views': random.randint(50, 100),
         'likes': random.randint(20, 50)
        },

        {
         'title': "How to Tango with Django 1.9",
         'url': "https://leanpub.com/tangowithdjango19/",
         'views': random.randint(50, 100),
         'likes': random.randint(20, 50)
        }
    ]

    other_pages = [
        {
         'title': "Official Bottle Tutorial",
         'url': "http://www.bottlepy.org/docs/dev/tutorial.html",
         'views': random.randint(50, 100),
         'likes': random.randint(20, 50)
        },

        {
         'title': "Official Flask Tutorial",
         'url': "http://flask.pocoo.org/docs/0.12/",
         'views': random.randint(50, 100),
         'likes': random.randint(20, 50)
        },

        {
         'title': "Official Tornado Tutorial",
         'url': "http://www.tornadoweb.org/en/stable/",
         'views': random.randint(50, 100),
         'likes': random.randint(20, 50)
        }
    ]

    cats = {
            "Python": {
             "pages": python_pages,
             "views": random.randint(100, 255),
             "likes": random.randint(50, 150)
            },

            "Django": {
             "pages": django_pages,
             "views": random.randint(100, 255),
             "likes": random.randint(50, 150)
            },

            "Other Frameworks": {
             "pages": other_pages,
             "views": random.randint(100, 255),
             "likes": random.randint(50, 150)
            }
        }

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    #  The code below goes through the "cats" dictionary,
    #+ then adds each category, and the add
    #+ all the associated pages for that category.

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"], p["likes"])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1} ".format(str(c), str(p)))

# Define the function that fill the pages for each category.


def add_page(cat, title, url, views, likes):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.likes = likes
    p.save()
    return p

# Define the funciton that fill the category.


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


# Start execution here.
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
