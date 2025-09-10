
from code_review_interview.backend.models import Team, Person, JiraIssue
from rest_framework import generics, serializers
from rest_framework.response import Response


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Team
        fields = [
            'id',
            'name',
        ]
    

class JiraIssueSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    team = TeamSerializer()

    class Meta:
        model = JiraIssue
        fields = [
            'id',
            'team',
        ]


class GetJiraIssuesView(generics.ListAPIView):
    serializer_class = JiraIssueSerializer

    def get_queryset(self):
        return JiraIssue.objects.all().select_related('team')
    

class PersonSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'team',
        ]
    

class GetPeopleView(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get(self):
        people = Person.objects.all()

        for person in people:
            issue_count_by_team = {}
            for issue in person.assigned_issues:
                team_id = issue.team.id
                if team_id not in issue_count_by_team:
                    issue_count_by_team[team_id] = 0
                issue_count_by_team[team_id] += 1

            max_issue_count = 0
            allocated_team_id = None
            for team_id, issue_count in issue_count_by_team.items():
                if issue_count > max_issue_count:
                    max_issue_count = issue_count
                    allocated_team_id = team_id

            person.team = Team.objects.get(id=allocated_team_id)

        serialized_data = self.serializer_class(people, many=True).data
        return Response(serialized_data)
