from Rest.api.viewsets import userviewsets
from rest_framework import routers
  
router = routers.DefaultRouter()
router.register(r'Rest', userviewsets, basename ='Rest_api')