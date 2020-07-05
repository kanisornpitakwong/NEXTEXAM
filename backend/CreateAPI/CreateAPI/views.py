from .serialization import serializationClass
from .models import subModel
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models_insert import createSubModel
from .serialization import createSubSerialize
from rest_framework import status

@api_view(['GET'])
def showSub(request):
    if request.method == 'GET' :
        results = subModel.objects.all()
        serialize = serializationClass(results, many = True)
        return Response(serialize.data)

@api_view(['POST'])
def saveSub(request):
    if request.method == 'POST':
        saveSerialize = createSubSerialize(data=request.data)
        if saveSerialize.is_valid():
            saveSerialize.save()
            return Response(saveSerialize.data, status = status.HTTP_201_CREATED)
            return Response(saveSerialize.data, status = status.HTTP_400_BAD_REQUEST)

# def insertSub(request):
#     if request.method == "POST":
#         teacher_name = request.POST.get('teacher_name')
#         created_by = request.POST.get('created_by')
#         subject_name = request.POST.get('subject_name')
#         subject_id = request.POST.get('subject_id')
#         start_time = request.POST.get('start_time')
#         end_time = request.POST.get('end_time')
#         easy = request.POST.get('easy')
#         medium = request.POST.get('medium')
#         hard = request.POST.get('hard')
#         backward = request.POST.get('backward')
#         scoring_method = request.POST.get('scoring_method')
#         show_score = request.POST.get('show_score')
#         data = {
#             'teacher_name':teacher_name,
#             'created_by':created_by,
#             'subject_name':subject_name,
#             'subject_id':subject_id,
#             'start_time':start_time,
#             'end_time':end_time,
#             'easy':easy,
#             'medium':medium,
#             'hard':hard,
#             'backward':backward,
#             'scoring_method':scoring_method,
#             'show_score':show_score
#         }
#         headers = {
#             'Content-Type' : 'application/json'
#         }
#         read = requests.post('http://127.0.0.1:8000/InsertSubject', json = data, headers = headers)
#         return render(request, 'teacher/create/index.vue')
#     else:
#         return render(request, 'teacher/create/index.vue')

