from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome_iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao_iexact=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(
            PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(
            PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(
            PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrive(self, request, *args, **kwargs):
        return super(
            PontoTuristicoViewSet, self).retrive(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(
            PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(
            PontoTuristicoViewSet, self).partial_update(
            request, *args, **kwargs)
