from rest_framework.views import APIView
from .serializers import *
import json
import collections
import psycopg2
from rest_framework.response import Response
from rest_framework import status
from pymongo import MongoClient
from .tasks import *


class ConvertTableDataToJsonApi(APIView):

    serializer_class = DBCredSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            host = serializer.validated_data.get('db_host')
            db_name = serializer.validated_data.get('db_name')
            user = serializer.validated_data.get('db_user')
            passwd = serializer.validated_data.get('db_password')
            table = serializer.validated_data.get('db_table')
            conn_string = "host={} dbname={} user={} password={}".format(host,db_name,user,passwd)
            try:
                #establish a connection with postgreSql
                conn = psycopg2.connect(conn_string)
            except:
                return Response(
                    {'Error': 'Invalid Credentials OR Database name'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            try:
                cursor = conn.cursor()
                query = ("SELECT * FROM {}").format(table)
                cursor.execute(query)
            except:
                return Response(
                    {'Error': 'Table not existed'},
                    status=status.HTTP_404_NOT_FOUND
                )

            #fetch rows and colnames from table
            colnames = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            conn.close()

            #run async task
            ConvertDBRowsToJson.delay(rows,colnames,db_name)

            return Response({
                'success':"Task completed Successfully"
            },status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)