from dataclasses import field, fields
from pyexpat import model
from tkinter import E
from rest_framework import serializers
from .models import Eshop

class EshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eshop
        fields = '__all__'