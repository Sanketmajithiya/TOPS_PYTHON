from rest_framework import serializers
from .models import Blogs

class Blogserializers(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']  