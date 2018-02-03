from tastypie.resources import ModelResource
from models import Map
from tastypie.utils.urls import trailing_slash
from django.conf.urls import url
from utils import near_by_places
from utils import find_route
from django.shortcuts import redirect
import json

API_BASE_URL = 'api/map/'

# location = '22.7304794,75.8708128'
destination = '22.7304794,75.8708128'


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
        if request:
            body = json.loads(request.body)
            # print body
            location = str(body['lat']) + ',' + str(body['lng'])
            resp = near_by_places(location)
            # print resp
            if resp['status'] == u'OK':
                result = resp['results']
                # print result
                locations = []

                for i in range(10):
                    # print result[i]
                    location = result[i]['geometry']['location']
                    locations.append(location)
                    # print location
                # print locations
                return self.create_response(request, {
                    'status': "sucess",
                    'location': locations
                })

    def find_route(self, request, *args, **kwargs):
        if request:
            body = json.loads(request.body)
            # print body
            location = str(body['lat']) + ',' + str(body['lng'])
            resp = find_route(location, destination)
            if resp:
                print resp
                return self.create_response(request, {
                    'status': "sucess"
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
