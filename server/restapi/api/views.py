from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Answer
from .serializer import AnswerSerializer
from .document_search import search_in_document
# Create your views here.

@api_view(['POST'])
def find_answer(request):
    print(request.data)
    print(request.data.get('text'))
    question = request.data.get('text')
    answer = search_in_document(question)
    return Response(AnswerSerializer({'text':answer}).data)