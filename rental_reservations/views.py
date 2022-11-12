from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .models import Rental, Reservation

class RentalListView(generic.ListView):
    model=Rental
    

def rental_detail(request, pk):
  return render(request, 'rental_reservations/rental_detail.html', context= {
    'reservation': get_object_or_404(Rental, pk=pk)
  })
class ReservationListView(generic.ListView):
    model = Reservation
    def get_context_data(self, **kwargs):
       
        rentals = Reservation.objects.prefetch_related("rental_id")
        context = super().get_context_data(**kwargs)
        context["rentals"] = rentals
        context["rentals_count"] = Reservation.objects.prefetch_related("rental_id").count()
        
        return context

def reservation_detail(request, pk):
  return render(request, 'rental_reservations/reservation_detail.html', context= {
    'reservation': get_object_or_404(Reservation, pk=pk)
  })

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_rentals = Rental.objects.all().count()
    num_Reservations = Reservation.objects.all().count()

    # Available books (status = 'a')
   
    # The 'all()' is implied by default.
   

    context = {
        'num_rentals': num_rentals,
        'num_reservations': num_Reservations,
       
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'rental_reservations/index.html', context=context)