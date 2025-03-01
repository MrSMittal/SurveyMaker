from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Survey, Question, Response
from .serializers import SurveySerializer, QuestionSerializer, ResponseSerializer

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title']
    ordering_fields = ['id']

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['survey']

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['question', 'user']
