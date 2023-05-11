from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.viewsets import (
    InventoryViewSet, PharmacyViewSet, ReportingManagerViewSet, SalesRepresentativeViewSet, DoctorViewSet, GeoTagViewSet,
    StoreViewSet, ProductViewSet,CategoryViewSet, CompetitorProductViewSet, DistributorViewSet, OrderViewSet, OrderItemViewSet, WorkingViewSet
)
from django.conf import settings  
from django.conf.urls.static import static  

router = routers.DefaultRouter()
router.register(r'sales-representatives', SalesRepresentativeViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'products', ProductViewSet)
router.register(r'competitorproducts', CompetitorProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'reporting-managers', ReportingManagerViewSet)
router.register(r'pharmacies', PharmacyViewSet)
router.register(r'distributors', DistributorViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'working', WorkingViewSet)
router.register(r'geotags', GeoTagViewSet)

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('sentry-debug/', trigger_error),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
