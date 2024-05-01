from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from rest_framework import permissions
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, *args, **kwargs):
        """Returns a list of APIView features"""
        return Response({"message": "Hello!"})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method": "PUT"})
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method": "PATCH"})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "Delete"})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code"
        ]

        return Response({"message": "Hello!", "a_viewset": a_viewset})
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            return Response({"message": message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Retrieve a hello message"""
        return Response({"http_method": "GET"})
    
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle partial updating of an object"""
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({"http_method": "DELETE"})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
