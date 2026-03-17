from models import Client

def context_client(request):
    if request.user.is_authenticated:
        try:
            client = Client.objects.get(user=request.user)
            name = client.first_name
        except:
            name = None

    else:
        name = None

    return {
        "Cliente": name,
        "Cliente Activo": request.user.is_authenticated
    }