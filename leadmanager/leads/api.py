from .models import Lead
from rest_framework import viewsets, permissions
from .Serializers import LeadSerializer

#Lead Viewset 
class LeadViewset(viewsets.ModelViewSet):
    queryset = Lead.object.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer