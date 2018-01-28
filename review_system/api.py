from tastypie.resources import ModelResource
from models import Map
from tastypie.utils.urls import trailing_slash
from django.conf.urls import url
from utils import near_by_places
from utils import find_route

API_BASE_URL = 'api/map/'

location = '22.7304794,75.8708128'
destination = '22.7304794,75.8708128'
radius = 1000


class MapResource(ModelResource):
    class Meta:
        queryset = Map.objects.all()
        resource_name = 'map'

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/find%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('find_route'), name="api_near_by_location"),
            url(r"^(?P<resource_name>%s)/route%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('find_near_by_location'), name="api_find_route")
        ]

    def find_near_by_location(self, request, *args, **kwargs):

        resp = near_by_places(location)
        return self.create_response(request, {
            'resp1': resp,
        })

    def find_route(self, request, *args, **kwargs):

        resp = find_route(location, destination)
        return self.create_response(request, {
            'resp': resp,
        })

    def _post_resp(self, rel_url, data, res_type):
        url = API_BASE_URL + rel_url
        resp = self.api_client.post(
            url,
            # authentication=self.get_credentials(self.user),
            data=data
        )
        res_type(resp)
        return self.deserialize(resp)
