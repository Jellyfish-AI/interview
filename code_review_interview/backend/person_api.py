
from main.models import Person
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
        company = self.request.user.company

        return Person.objects.filter(company=company)