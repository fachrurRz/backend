

from kenalan.models import (
    Token, Kenalan, KenalanStatus, DetailKenalan
)

from kenalan.serializers import( 
    TokenSerializer, KenalanSerializer,
    KenalanStatusSerializer, DetailKenalanSerializer,
)

from rest_framework import generics, permissions, exceptions

from account.permissions import(
    IsPmbAdmin,
    IsDetailKenalanOwner,
    IsKenalanOwner,
    is_maba,
    is_elemen,
)


class TokenList(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = (permissions.IsAdminUser,)


'''
Kenalan Views
'''


class KenalanList(generics.ListAPIView):
    serializer_class = KenalanSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if is_maba(self.request.user):
            queryset = Kenalan.objects.all().filter(user_maba=self.request.user)
        elif is_elemen(self.request.user):
            queryset = Kenalan.objects.all().filter(user_elemen=self.request.user)
        else:
            queryset = Kenalan.objects.all()

        return queryset


class KenalanDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KenalanSerializer
    permission_classes = (IsKenalanOwner,)
    queryset = Kenalan.objects.all()



class KenalanStatusList(generics.ListAPIView):
    queryset = KenalanStatus.objects.all()
    serializer_class = KenalanStatusSerializer
    permission_classes = (IsPmbAdmin,)


class KenalanStatusDetail(generics.RetrieveAPIView):
    queryset = KenalanStatus.objects.all()
    serializer_class = KenalanStatusSerializer
    permission_classes = (IsPmbAdmin,)


class DetailKenalanList(generics.ListAPIView):
    queryset = DetailKenalan.objects.all()
    serializer_class = DetailKenalanSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if is_maba(self.request.user):
            queryset = DetailKenalan.objects.all().filter(kenalan__user_maba=self.request.user)
        elif is_elemen(self.request.user):
            queryset = DetailKenalan.objects.all().filter(kenalan__user_elemen=self.request.user)
        else:
            queryset = DetailKenalan.objects.all()
        return queryset


class DetailKenalanDetail(generics.RetrieveUpdateAPIView):
    queryset = DetailKenalan.objects.all()
    serializer_class = DetailKenalanSerializer
    permission_classes = (IsDetailKenalanOwner,)

