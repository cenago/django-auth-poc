


from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # 🔒 This forces JWT authentication
def protected_view(request):
    return Response({"message": f"Hello {request.user.username}, you are authenticated!"})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
