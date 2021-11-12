from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view"""
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_api_view = [
            'Use HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_api_view})


