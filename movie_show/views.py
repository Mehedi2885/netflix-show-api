from rest_framework import filters
from rest_framework.response import Response

from .models import MovieShow
from .serializers import MovieShowSerializers, TotalMovieTvSerializers
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class MovieViewPagination(LimitOffsetPagination):
    """Class view for defining pagination"""
    default_limit = 5
    max_limit = 10


# example:: search and sort: http://127.0.0.1:8000/movie/title/?search=friends&search_fields=title for more granular search and sort
# example:: ordering, search and sort http://127.0.0.1:8000/movie/title/?limit=5&ordering=release_year&search=friends&search_fields=title
class MovieDynamicSearchFilter(filters.SearchFilter, ):
    """
    Dynamic search field class, ex: ip:port/movie/name/?search=friends&search_fields=title
    or ip:port/movie/name/?limit=5&ordering=release_year&search=friends&search_fields=title
    """

    def get_search_fields(self, view, request):
        # Provide search field value and list of search_field
        return request.GET.getlist('search_fields', [])


class MovieViewSet(ModelViewSet):
    """MovieViewSet for search, filter, sort, pagination and update"""
    queryset = MovieShow.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = MovieShowSerializers
    filter_backends = (MovieDynamicSearchFilter, filters.OrderingFilter,)
    pagination_class = MovieViewPagination
    ordering_fields = ['release_year']
    http_method_names = ('get', 'put', 'patch')


# http://127.0.0.1:8000/movie/summary/ to see total movie, tv show and their percentage
class Total_movie_tv_show(APIView):
    """APIView for total movie summary like total movie, tv_show and their percentage"""
    serializer_class = TotalMovieTvSerializers
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        try:
            total_show = MovieShow.objects.all().count()
            total_tv_show = MovieShow.objects.filter(type__icontains='TV Show').count()
            total_movie = MovieShow.objects.filter(type__icontains='Movie').count()
            tv_show_percent = "{} %".format(round((100 * total_tv_show) / total_show))
            movie_percent = "{} %".format(round((100 * total_movie) / total_show))

            return Response({'total_movie': total_movie, 'total_tv_show': total_tv_show, 'total_show': total_show,
                             'tv_show_percent': tv_show_percent, 'movie_percent': movie_percent})
        except TypeError as te:
            Response({'TypeError': te})


class MovieInCountry(APIView, APIException):
    """
    APIView to see any types of movie in a country and their related percentage
    Provide data in url as string like ip:port/movie/country/country_name,movie or show type/
    eg. ip:port/movie/country/United States,Movie/
    """
    queryset = MovieShow.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        total_show = self.queryset.count()
        list_params = kwargs['country'].split(',')
        country = list_params[0]
        show_type = list_params[1]
        is_country = self.queryset.filter(country__icontains=country)
        if is_country:
            movie_in_count = self.queryset.filter(country__icontains=country, type__icontains=show_type).count()
            movie_in_country = "Movie in {}: {}".format(country, movie_in_count)
            movie_percent = "percentage {:.2f} %".format((100 * movie_in_count) / total_show)
            return Response(
                {'Total movie or TV Show': movie_in_country, 'Total movie or TV Show percent': movie_percent})
        else:
            raise APIException('No such data')
