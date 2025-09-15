from django.db import models


class Team(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=64)


class Person(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)


class JiraIssue(models.Model):

    id = models.AutoField(primary_key=True)
    jira_id = models.UUIDField(editable=False)

    title = models.TextField()
    assignee = models.ForeignKey(Person, related_name='assigned_jira_issues', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL)
