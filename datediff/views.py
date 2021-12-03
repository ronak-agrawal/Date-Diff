__author__ = 'Ronak'
from .models import *

def get_diff(request):
    id = request['id']
    obj = Dates.objects.get(id=id)
    if obj.diff:
        return obj.diff
    else:
        obj.diff = obj.calculateDiff()
        obj.save()
        return obj.diff