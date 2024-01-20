from django.db import models

class AddressBook(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'AddressBooks'
    
    def __str__(self):
        return self.name

class BuddyInfo(models.Model):
    name=models.CharField(max_length=255)
    Address=models.TextField()
    Phone_Number=models.IntegerField()
    Address_book= models.ForeignKey(AddressBook,related_name='BuddyInfo',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

