from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Job
from .models import PersonalJob


class Jobtype(DjangoObjectType):
    class Meta:
        model = Job
        interfaces = (graphene.relay.Node, )


class PersonalJobType(DjangoObjectType):
    """Describe which model we want to expose through GraphQL."""
    class Meta:
        model = PersonalJob

        # Describing the data as a node in a graph for GraphQL
        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    """Describe which records we want to show."""
    jobs = graphene.List(Jobtype)
    personaljobs = graphene.List(PersonalJobType)

    def resolve_jobs(self, info):
        return Job.objects.all()

    def resolve_personaljobs(self, info):
        """Decide what jobs to return."""
        user = info.context.user  # Find this with the debugger

        if user.is_anonymous:
            return PersonalJob.objects.none()
        else:
            return PersonalJob.objects.filter(user=user)

# Add a schema and attach to the query
schema = graphene.Schema(query=Query)