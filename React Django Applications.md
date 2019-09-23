# React Django Applications

## General Process

1. start project

2. create app

3. add app to settings

4. create models

5. create Serializers.py

   1. ModelSerializer: creates a Serializer from a certain model in a Serializer class and a class meta.

6. create api.py

   1. import model, serializer and  from rest_framework import viewsets, permissions.

   2. viewsets allows to create a full CRUD api without having to specify explicit methods for functionality by using routers.

   3. ````python
      class LeadViewset(viewsets.ModelViewset):
          queryset = Lead.object.all()
          permission_classes = [
              permissions.AllowAny
          ]
          serializer_class = LeadSerializer
      ````

7. Change URLs:

   1. In project urls include leads.url
   2. No admin needed so admin URL won't be needed
   3. In leads urls include routers.DefaultRouter and register 'api/leads' and urlpatterns = router.urls
   4. to test the router CRUD use postman and runserver
   5. 