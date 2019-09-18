from rest_framework import serializers, viewsets

from .models import PersonalJob


class PersonalJobSerializer(serializers.HyperlinkedModelSerializer):
    # Inner class nested inside PersonalNoteSerializer
    class Meta:
        model = PersonalNote
        fields = ('title', 'company', 'description')


class PersonalJobViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalJobSerializer
    queryset = PersonalNote.objects.all()
