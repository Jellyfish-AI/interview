
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
        people = Person.objects.all()

        query = self.request.query_params.get('query', None)
        queried_people = []

        for person in people:
            if query in person.name or query in person.email:
                queried_people.append(person)

        return queried_people