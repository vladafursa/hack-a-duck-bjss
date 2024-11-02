from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Teams
from .serializers import TeamsSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='post',
    request_body=TeamsSerializer,
    responses={201: "User registered successfully!", 400: "Invalid data"}
)
@api_view(['POST'])
def create_team(request):
    serializer = TeamsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@swagger_auto_schema(
    method='get',
    operation_summary="Retrieve all teams",
    responses={
        200: openapi.Response("A list of teams", TeamsSerializer(many=True)),
        400: "Bad Request",
    }
)
@api_view(['GET'])
def teams_list_view(request):
    teams = Teams.objects.all()  # Retrieve all candidate instances
    serializer = TeamsSerializer(teams, many=True)  # Serialize the data
    return Response(serializer.data, status=status.HTTP_200_OK)
