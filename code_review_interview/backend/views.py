
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
            'title',
            'team',
        ]


class GetJiraIssuesView(generics.ListAPIView):
    serializer_class = JiraIssueSerializer

    def get_queryset(self):
        return JiraIssue.objects.all().select_related('team')
    

class EngineerTypeSerializer(serializers.Serializer):
    key = serializers.CharField()
    label = serializers.CharField()
    color = serializers.CharField()
    

class PersonSerializer(serializers.ModelSerializer):
    team = TeamSerializer(allow_null=True)
    engineer_type = EngineerTypeSerializer(source="engineer_type_data")

    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'team',
            'engineer_type',
        ]
    

class GetPeopleView(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get(self):
        people = Person.objects.all()

        if not people.exists():
            return Response(status=404)

        for person in people:
            issue_count_by_team = {}
            for issue in person.assigned_jira_issues.all():
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
            
            if allocated_team_id:
                person.team = Team.objects.get(id=allocated_team_id)

            if person.engineer_type == 'FRONTEND':
                engineer_type_label = 'Frontend'
                engineer_type_color = "#0f73ff"
            elif person.engineer_type == 'BACKEND':
                engineer_type_label = 'Backend'
                engineer_type_color = "#ff6b0f"
            elif person.engineer_type == 'FULLSTACK':
                engineer_type_label = 'Fullstack'
                engineer_type_color = "#4dd826"
            elif person.engineer_type == 'INFRA':
                engineer_type_label = 'Infrastructure'
                engineer_type_color = "#ffcb0f"
            else:
                engineer_type_label = 'Non-Engineer'
                engineer_type_color = "#8d8d8d"

            person.engineer_type_data = {
                "key": person.engineer_type or "NONE",
                "label": engineer_type_label,
                "color": engineer_type_color
            }

        serialized_data = self.serializer_class(people, many=True).data
        return Response(serialized_data)
