from django.shortcuts import render
from .form import ContactForm
from django.contrib import messages
# Create your views here.
def index (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
        if form.has_error(field='email'):
            messages.error(request, 'Duplicate Email Id or Mobile Number')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/index.html', context)

def blog (request):
    return render(request, 'main/blog.html')

# def contact (request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Form submission successful')
#         if form.has_error(field='email'):
#             messages.error(request, 'Duplicate Email Id or Mobile Number')
#     return render(request, 'main/contact.html')
