from rest_framework import serializers, viewsets

from .models import PersonalJob


class PersonalJobSerializer(serializers.HyperlinkedModelSerializer):
    # Inner class nested inside PersonalNoteSerializer
    class Meta:
        model = PersonalJob
        fields = ('id', 'title', 'company', 'description')


class PersonalJobViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalJobSerializer
    queryset = PersonalJob.objects.none()

    def create(self, validated_data):
        user = self.request.user
        job = PersonalJob.objects.create(user=user, **validated_data.data)
        return job

    def get_queryset(self):
        user = self.request.user
        print(user)
        if user.is_anonymous:
            return PersonalJob.objects.none()
        return PersonalJob.objects.filter(user=user)
