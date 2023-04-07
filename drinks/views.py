from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(requests):
    #get all the drinks
    drinks = Drink.objects.all()

    #Serialize them
    serializer = DrinkSerializer(drinks, many=True)

    #return the json
    return JsonResponse(serializer.data)