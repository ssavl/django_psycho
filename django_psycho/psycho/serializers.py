from rest_framework import serializers

from psycho.models import PsychoMaster, Method


class PsychoMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychoMaster
        fields = ['name', 'img', 'id']


class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Method
        fields = '__all__'


class PsychoMasterDetailSerializer(serializers.ModelSerializer):
    methods = MethodSerializer(many=True)
    
    class Meta:
        model = PsychoMaster
        fields = ['name', 'img', 'id', 'methods']
