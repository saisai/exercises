from datetime import datetime
from operator import attrgetter

from django.db.models import (
    CharField,
    Count,
    DateTimeField,
    F,
    Max,
    OuterRef,
    Subquery,
    Value,
)
from django.db.models.functions import Upper
from django.test import TestCase

from .models import (
    Article,
    Author,
    ChildArticle,
    OrderedByExpression,
    OrderedByExpressionChild,
    OrderedByExpressionGrandChild,
    OrderedByFArticle,
    Reference,
)


class OrderingTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.a1 = Article.objects.create(
            headline="Article 1", pub_date=datetime(2005, 7, 26)
        )
        cls.a2 = Article.objects.create(
            headline="Article 2", pub_date=datetime(2005, 7, 27)
        )
        cls.a3 = Article.objects.create(
            headline="Article 3", pub_date=datetime(2005, 7, 27)
        )
        cls.a4 = Article.objects.create(
            headline="Article 4", pub_date=datetime(2005, 7, 28)
        )
        cls.author_1 = Author.objects.create(name="Name 1")
        cls.author_2 = Author.objects.create(name="Name 2")
        for i in range(2):
            Author.objects.create()
            
    def assertQuerysetEqualReversible(self, queryset, sequence):
        self.assertSequenceEqual(queryset, sequence)
        self.assertSequenceEqual(queryset.reverse(), list(reversed(sequence)))

    def test_orders_nulls_first_on_filtered_subquery(self):
        Article.objects.filter(headline="Article 1").update(author=self.author_1)
        Article.objects.filter(headline="Article 2").update(author=self.author_1)
        Article.objects.filter(headline="Article 4").update(author=self.author_2)
        Author.objects.filter(name__isnull=True).delete()
        author_3 = Author.objects.create(name="Name 3")
        article_subquery = (
            Article.objects.filter(
                author=OuterRef("pk"),
                headline__icontains="Article",
            )
            .order_by()
            .values("author")
            .annotate(
                last_date=Max("pub_date"),
            )
            .values("last_date")
        )
        
        cc = Author.objects.annotate(
                last_date=Subquery(article_subquery, output_field=DateTimeField())
            ).order_by(F("last_date").asc(nulls_first=True)).distinct()
        
        print(str(cc.query))
                
        
        #print("article_subquery ", article_subquery)
        self.assertQuerysetEqualReversible(
            Author.objects.annotate(
                last_date=Subquery(article_subquery, output_field=DateTimeField())
            )
            .order_by(F("last_date").asc(nulls_first=True))
            .distinct(),
            [author_3, self.author_1, self.author_2],
        )
        
    

