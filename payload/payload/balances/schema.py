import graphene
from graphene_django.types import DjangoObjectType
from payload.payload.balances.models import Category, Balance


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class BalanceType(DjangoObjectType):
    class Meta:
        model = Balance


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_balances = graphene.List(BalanceType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_balancess(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Balance.objects.select_related('category').all()