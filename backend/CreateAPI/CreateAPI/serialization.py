from rest_framework import serializers
from .models import subModel

from .models_insert import createSubModel

class serializationClass(serializers.ModelSerializer):
    class Meta:
        model = subModel
        fields = ['sub_id','sub_name','sub_teacher','sub_start','sub_stop']

class createSubSerialize(serializers.ModelSerializer):
    class Meta:
        model = createSubModel
        fields = ['sub_id','sub_name','sub_teacher','sub_start','sub_stop']