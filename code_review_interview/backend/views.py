
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
    

class EngineerTypeSerializer(serializers.Serializer):
    key = serializers.CharField()
    label = serializers.CharField()
    color = serializers.CharField()
    

class PersonSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
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

            if person.engineering_area == 'FRONTEND':
                engineering_area_label = 'Frontend'
                engineering_area_color = "#0f73ff"
            elif person.engineering_area == 'BACKEND':
                engineering_area_label = 'Backend'
                engineering_area_color = "#ff6b0f"
            elif person.engineering_area == 'FULLSTACK':
                engineering_area_label = 'Fullstack'
                engineering_area_color = "#4dd826"
            elif person.engineering_area == 'INFRA':
                engineering_area_label = 'Infrastructure'
                engineering_area_color = "#ffcb0f"
            else:
                engineering_area_label = 'Non-Engineer'
                engineering_area_color = "#8d8d8d"

            person.engineer_type_data = {
                "key": person.engineering_area or "NONE",
                "label": engineering_area_label,
                "color": engineering_area_color
            }

        serialized_data = self.serializer_class(people, many=True).data
        return Response(serialized_data)
