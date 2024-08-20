from django.shortcuts import render
from  .addressBookForm import UploadForm
from .buddiesForm import UploadForm2
from  .models import AddressBook, BuddyInfo

def index(request):
    # if this is a POST request we need to process the form data
    print(request)
    submitted = False

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            submitted = True

    else:
        form = UploadForm()  # Create an instance of the form

    return render(request, "index.html", {'form': form, 'submitted': submitted})

def buddies(request):

    # if this is a POST request we need to process the form data
    print(request)
    submitted = False

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadForm2(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_buddy = form.save(commit=False)
            new_buddy.Address_book = form.cleaned_data['Address_book']
            new_buddy.save()
            submitted = True

    else:
        form = UploadForm2()  # Create an instance of the form


     # Retrieve all address books
    address_books = AddressBook.objects.all()
    context={'address_books': address_books,'form': form, 'submitted': submitted}

    # You can pass address_books to your template for iteration

    return render(request, "buddyinfo.html", context)

def message_page(request):
    return render(request, 'message.html')





