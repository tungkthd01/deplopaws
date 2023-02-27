from rest_framework import serializers
from main.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Post
        fields = ['title','decription','file']
        
        
    def create(self,validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.decription = validated_data.get('decription', instance.decription)
        instance.file = validated_data.get('file', instance.file)
        return super().update(instance, validated_data)