from django.db import models
from django.urls import reverse
import uuid  # Required for unique book instances
from datetime import date

class Rental(models.Model):
    """Model representing a Rental"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular rental")
    name = models.CharField(max_length=200, help_text='Enter a rental property')
    def __str__(self):
        """String for representing the Model object."""
        return f"name: {self.name}"
    def get_absolute_url(self):
        return reverse('rental_detail', args=[str(self.id)])


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular Reservation across rentals")
    check_in = models.DateField(null=True, blank=True)
    check_out=models.DateField(null=True,blank=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author is a string rather than an object because it hasn't been declared yet in the file
    rental_id = models.ForeignKey('Rental', on_delete=models.SET_NULL, null=True)
    
    

    def __str__(self):
        """String for representing the Model object."""
        
        return f"{self.rental_id}, {self.check_in}, {self.check_out}"

    def get_absolute_url(self):
        return reverse('reservation_detail', args=[str(self.id)])