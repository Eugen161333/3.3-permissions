from rest_framework import viewsets, permissions
from .models import Advertisement
from .serializers import AdvertisementSerializer

class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated()]
        return []  # <-- это критически важно: пустой список, а не None

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
