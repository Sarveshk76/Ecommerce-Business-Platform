from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Ecommerce Business Platform"
admin.site.site_title = "Your Admin Portal"
admin.site.index_title = "Welcome to Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("common/", include("common.urls")),
    path('inventory/', include("inventory.urls")),
    path('order/', include("order.urls")),
    path('delivery/', include("delivery.urls")),
    path('seller/', include("seller.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
