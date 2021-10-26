from rest_framework import serializers

class DBCredSerializer(serializers.Serializer):
    db_host = serializers.CharField(max_length=250,required=True)
    db_name = serializers.CharField(max_length=250,required=True)
    db_user = serializers.CharField(max_length=250,required=True)
    db_password = serializers.CharField(max_length=250,required=True)
    db_table = serializers.CharField(max_length=250,required=True)




