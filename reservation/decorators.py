from reservation.models import Reservation
from django.http import Http404
from django.core.exceptions import PermissionDenied

def client_can_modify_or_delete_reservation(function):
    def wrap(request, *args, **kwargs):
        try:
            reserv = Reservation.objects.get(pk=kwargs["pk"])
        except:
            raise Http404

        if request.client == reserv.created_by:
            return function(request, *args, **kwargs)

        raise PermissionDenied

    return wrap