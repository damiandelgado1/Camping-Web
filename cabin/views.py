from django.shortcuts import render

from .models import Cabin

# Show all Cabin
def cabins_list(request):
    cabins = Cabin.objects.all()

    context = {
        'cabins': cabins
    }

    return render(request, "cabin/cabin_list.html", context)

# Show description and details of the Cabin
def cabin_detail(request, id):
    cabin = Cabin.objects.get(pk=id)

    context = {
        'cabin': cabin
    }

    return render(request, "cabin/cabin_detail.html", context)