from rest_framework import serializers
from contact.models import ContactModel

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"
