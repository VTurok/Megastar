from rest_framework import viewsets

from library.models import Writer
from library.serializers import *



# Create your views here.
class WritersBooksViewSet(viewsets.ModelViewSet):
    serializer_class = WritersBooksSerializer
    filter_fields = ("id",)

    def get_queryset(self):
        queryset = Writer.objects.all()
        return queryset