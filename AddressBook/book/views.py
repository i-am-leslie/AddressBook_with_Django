from django.shortcuts import render
from  .addressBookForm import UploadForm
from  .models import AddressBook, BuddyInfo

def index(request):
    # if this is a POST request we need to process the form data
    print("first")
    print(request)
    submitted = False

    if request.method == 'POST':
        print("Second")
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
     # Retrieve all address books
    address_books = AddressBook.objects.all()
    buddies= BuddyInfo.objects.all()

    
    # You can pass address_books to your template for iteration

    return render(request, "buddyinfo.html", {'address_books': address_books, buddies:'buddies'})





