from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from contact.models import ContactModel
from contact.api.serializers import ContactSerializer

class ContactListCreateApiView(ListCreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroy(RetrieveUpdateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "pk"