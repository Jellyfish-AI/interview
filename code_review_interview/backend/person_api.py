
from backend.person_models import Person
from rest_framework import generics, serializers


class PersonSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'email'
        ]


class GetPeopleView(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()