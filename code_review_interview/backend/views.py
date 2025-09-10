
from code_review_interview.backend.models import Team, Person, JiraIssue
from rest_framework import generics, serializers


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Team
        fields = [
            'id',
            'name',
        ]


class PersonSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Person
        fields = [
            'id',
            'name',
        ]
    

class JiraIssueSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    team = TeamSerializer()
    assignee = PersonSerializer()

    class Meta:
        model = JiraIssue
        fields = [
            'id',
            'team',
            'assignee',
        ]


class GetJiraIssuesView(generics.ListAPIView):
    serializer_class = JiraIssueSerializer

    def get_queryset(self):
        return JiraIssue.objects.all().select_related('team', 'assignee')