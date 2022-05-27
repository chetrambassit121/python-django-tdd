from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from lists.forms import ItemForm
from lists.models import Item, List

from lists.forms import ExistingListItemForm, ItemForm

def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})














# from django.core.exceptions import ValidationError
# from django.shortcuts import redirect, render

# from lists.forms import ItemForm
# from lists.models import Item, List

# def home_page(request):
#     return render(request, 'home.html', {'form': ItemForm()})


# def new_list(request):
#     form = ItemForm(data=request.POST)
#     if form.is_valid():
#         list_ = List.objects.create()
#         Item.objects.create(text=request.POST['text'], list=list_)
#         return redirect(list_)
#     else:
#         return render(request, 'home.html', {"form": form})


# def view_list(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     form = ItemForm()
#     if request.method == 'POST':
#         form = ItemForm(data=request.POST)
#         if form.is_valid():
#             Item.objects.create(text=request.POST['text'], list=list_)
#             return redirect(list_)
#     return render(request, 'list.html', {'list': list_, "form": form})














# from django.core.exceptions import ValidationError
# from django.shortcuts import redirect, render
# from lists.models import Item, List

# def home_page(request):
#     return render(request, 'home.html')


# def new_list(request):
#     list_ = List.objects.create()
#     item = Item(text=request.POST['item_text'], list=list_)
#     try:
#         item.full_clean()
#         item.save()
#     except ValidationError:
#         list_.delete()
#         error = "You can't have an empty list item"
#         return render(request, 'home.html', {"error": error})
#     return redirect(f'/lists/{list_.id}/')


# # def add_item(request, list_id):
# #     list_ = List.objects.get(id=list_id)
# #     Item.objects.create(text=request.POST['item_text'], list=list_)
# #     return redirect(f'/lists/{list_.id}/')


# def view_list(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     if request.method == 'POST':
#         Item.objects.create(text=request.POST['item_text'], list=list_)
#         return redirect(f'/lists/{list_.id}/')
#     return render(request, 'list.html', {'list': list_})













# from django.core.exceptions import ValidationError
# from django.shortcuts import redirect, render
# from lists.models import Item, List

# def home_page(request):
#     return render(request, 'home.html')


# def new_list(request):
#     list_ = List.objects.create()
#     item = Item(text=request.POST['item_text'], list=list_)
#     try:
#         item.full_clean()
#         item.save()
#     except ValidationError:
#         list_.delete()
#         error = "You can't have an empty list item"
#         return render(request, 'home.html', {"error": error})
#     return redirect(f'/lists/{list_.id}/')


# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST['item_text'], list=list_)
#     return redirect(f'/lists/{list_.id}/')


# def view_list(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     return render(request, 'list.html', {'list': list_})















# from django.shortcuts import redirect, render
# from lists.models import Item, List
# from django.core.exceptions import ValidationError

# def home_page(request):
#     return render(request, 'home.html')


# def new_list(request):
#     list_ = List.objects.create()
#     item = Item.objects.create(text=request.POST['item_text'], list=list_)
#     try:
#         item.full_clean()
#     except ValidationError:
#         return render(request, 'home.html')


# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST['item_text'], list=list_)
#     return redirect(f'/lists/{list_.id}/')


# def view_list(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     return render(request, 'list.html', {'list': list_})















# from django.shortcuts import redirect, render
# from lists.models import Item, List

# def home_page(request):
#     return render(request, 'home.html')


# def new_list(request):
#     list_ = List.objects.create()
#     Item.objects.create(text=request.POST['item_text'], list=list_)
#     return redirect(f'/lists/{list_.id}/')


# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST['item_text'], list=list_)
#     return redirect(f'/lists/{list_.id}/')


# def view_list(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     return render(request, 'list.html', {'list': list_})













# from django.shortcuts import redirect, render
# from lists.models import Item

# def home_page(request):
#     if request.method == 'POST':
#         Item.objects.create(text=request.POST['item_text'])
#         return redirect('/lists/the-only-list-in-the-world/')
#     return render(request, 'home.html')


# def view_list(request):
#     items = Item.objects.all()
#     return render(request, 'list.html', {'items': items})














# ........................................
# from django.shortcuts import redirect, render
# from lists.models import Item

# def home_page(request):
#     if request.method == 'POST':
#         Item.objects.create(text=request.POST['item_text'])
#         return redirect('/lists/the-only-list-in-the-world/')

#     items = Item.objects.all()
#     return render(request, 'home.html', {'items': items})









# ...............................................................
# from django.shortcuts import redirect, render
# from lists.models import Item

# def home_page(request):
#     if request.method == 'POST':
#         Item.objects.create(text=request.POST['item_text'])
#         return redirect('/')

#     items = Item.objects.all()
#     return render(request, 'home.html', {'items': items})

