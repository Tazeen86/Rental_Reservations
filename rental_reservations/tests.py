from django.test import TestCase
import datetime
import uuid
from django.db.models import DateField

from rental_reservations.models import Reservation,Rental

class ReservationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.rental_ = uuid.uuid4()
        cls.rental = Rental.objects.create(id=cls.rental_)
        
        cls.reservation= Reservation.objects.create(check_in=datetime.date.fromisoformat("2022-11-24").strftime("%Y-%m-%d"), check_out=datetime.date.fromisoformat("2022-11-26").strftime("%Y-%m-%d"), rental_id = cls.rental)

    def test_check_in_label(self):
        reservation = Reservation.objects.get(id=self.reservation.id)
        field_label = reservation._meta.get_field('check_in').verbose_name
        self.assertEqual(field_label, 'check in')

    def test_check_out_label(self):
        reservation = Reservation.objects.get(id=self.reservation.id)
        field_label = reservation._meta.get_field('check_out').verbose_name
        self.assertEqual(field_label, 'check out')

    def test_check_in_is_date(self):
        reservation = Reservation.objects.get(id=self.reservation.id)
        is_datetime =  isinstance(reservation._meta.get_field('check_in'),DateField)
   
        self.assertEqual(is_datetime, True)

    def test_check_out_is_date(self):
        reservation = Reservation.objects.get(id=self.reservation.id)
        is_datetime =  isinstance(reservation._meta.get_field('check_out'),DateField)
   
        self.assertEqual(is_datetime, True)

    def test_object_name_is_rental_id_comma_check_in_comma_check_out(self):
        reservation = Reservation.objects.get(id=self.reservation.id)
        expected_object_name = f'{reservation.rental_id}, {reservation.check_in}, {reservation.check_out}'
        self.assertEqual(str(reservation), expected_object_name)

    def test_get_absolute_url(self):
        reservation = Reservation.objects.get(id=self.reservation.id)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(reservation.get_absolute_url(), f'/rental_reservations/reservation/{self.reservation.id}/')