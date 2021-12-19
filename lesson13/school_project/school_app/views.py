from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

import json

subjects = [{"id": 1, "name": "Maths"}, {"id": 2, "name": "PE"}]

def hello_world(request):
    return HttpResponse("Hello Michal")

@csrf_exempt
def list_subjects(request):
    if request.method == "GET":
        return JsonResponse(subjects, safe=False, status=200)
    elif request.method == "POST":
        subject = request.body
        print(subject)
        print(type(subject))

        subject_dict = json.loads(subject)

        print(subject_dict)
        print(type(subject_dict))
        subjects.append(subject_dict)
        return JsonResponse(subject_dict, status=200)
    else: 
        return HttpResponseNotFound("Sorry this method is not supported")

@csrf_exempt
def subject_detail(request, pk):
    global subjects

    try:
        subject = next(subject for subject in subjects if subject["id"] == pk)
    except StopIteration:
        return JsonResponse({"status": f"There is no subject with id {pk}"}, status=404)

    if request.method == "GET":
        return JsonResponse(subject)
    elif request.method == "PUT":
        new_subject_bytes = request.body
        new_subject = json.loads(new_subject_bytes)
        new_subject_index = subjects.index(subject)
        subjects[new_subject_index] = new_subject
        return JsonResponse(new_subject, status=201)
    elif request.method == "DELETE":
        subjects = list(filter(lambda subject: subject["id"] != pk, subjects))
        return HttpResponse(status=204)