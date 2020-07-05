from rest_framework import serializers
from .models import subModel

from .models_insert import createSubModel

class serializationClass(serializers.ModelSerializer):
    class Meta:
        model = subModel
        fields = ['subject_id','subject_name','teacher_name','start_time','end_time']

class createSubSerialize(serializers.ModelSerializer):
    class Meta:
        model = createSubModel
        fields = [
        'teacher_name',
        'created_by',
        # 'timestamp',
        'subject_name',
        'subject_id',
        'start_time',
        'end_time',
        'easy',
        'medium',
        'hard',
        'backward',
        'scoring_method',
        'show_score'
        ]
        # fields = ['sub_id','sub_name','sub_teacher','sub_start','sub_stop']