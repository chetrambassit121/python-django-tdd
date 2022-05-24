# from django.shortcuts import render
# from django.http import HttpResponse


# def home_page(request):
#     return HttpResponse('<html><title>To-Do lists</title></html>')



# def home_page(request):
#     return render(request, 'home.html')













# from django.http import HttpResponse
# from django.shortcuts import render

# def home_page(request):
#     if request.method == 'POST':
#         return HttpResponse(request.POST['item_text'])
#     return render(request, 'home.html')





















# from django.http import HttpResponse
# from django.shortcuts import render

# def home_page(request):
#     return render(request, 'home.html', {
#         'new_item_text': request.POST.get('item_text', ''),
#     })
# ................................





# from django.shortcuts import render
# from lists.models import Item

# def home_page(request):
#     if request.method == 'POST':
#         new_item_text = request.POST['item_text']  
#         Item.objects.create(text=new_item_text)  
#     else:
#         new_item_text = ''  

#     return render(request, 'home.html', {
#         'new_item_text': new_item_text,  
#     })
# .......................................





# from django.shortcuts import redirect, render
# from lists.models import Item

# def home_page(request):
#     if request.method == 'POST':
#         Item.objects.create(text=request.POST['item_text'])
#         return redirect('/')

#     return render(request, 'home.html')
# ..............................................



from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})