from django.shortcuts import render
from .models import Treasure
# Create your views here.


def home(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})


def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})


# class Treasure:
#     def __init__(self, name, value, material, location, img_url):
#         self.name = name
#         self.value = value
#         self.material = value
#         self.location = location
#         self.img_url = img_url


treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM", 'example.com/nugget.jpg'),
    Treasure('Fools Gold', 0.00, 'pyrite', "Fool's Falls, CO", 'example.com/fools-gold.jpg'),
    Treasure('Coffee Can', 20.00, 'tin', "Acme, CA", 'example.com/coffee-can.jpg'),
]
