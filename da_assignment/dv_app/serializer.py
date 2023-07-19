from rest_framework import serializers
from .models import DB_Visual


class DBSerializer(serializers.ModelSerializer):
    class Meta:
        model = DB_Visual
        fields = ('end_year', 'intensity','sector','topic','insight','url','region','start_year',
          'impact','added','published','country','relevance','pestle','source','title','likelihood')