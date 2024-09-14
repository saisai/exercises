import re

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from manytomany.models import Publication, Article

def add():
    p1 = Publication(title='The Python Journal')
    p1.save()

    p2 = Publication(title='Science News')
    p2.save()

    p3 = Publication(title="Science Weekly")
    p3.save()

p1 = Publication(title='The Python Journal')
p1.save()

p2 = Publication(title='Science News')
p2.save()

p3 = Publication(title="Science Weekly")
p3.save()
p1 = Publication(title='The Python Journal')
p1.save()

a1 = Article(headline='Django lets you build Web apps easily')
a1.save()
a1.publications.add(p1)



a2 = Article(headline='NASA uses Python')
a2.save()
a2.publications.add(p1, p2)
a2.publications.add(p2)

new_publication = a2.publications.create(title='Highlights for Children')

print(a1.publications.all())

print(a2.publications.all())

print(p2.article_set.all())
print(p1.article_set.all())

print(Publication.objects.get(id=4).article_set.all())

print(Article.objects.filter(publications__id=1))

print(Article.objects.filter(publications__pk=1))

print(
Article.objects.filter(publications=1)
)

print(
Article.objects.filter(publications=p1)
)

print(
Article.objects.filter(publications__title__startswith="Science")
)

print(
Article.objects.filter(publications__title__startswith="Science").distinct()
)

print(
Article.objects.filter(publications__title__startswith="Science").count()
)

print(
Article.objects.filter(publications__title__startswith="Science").distinct().count()
)

print(
Article.objects.filter(publications__in=[1,2]).distinct()
)

print(
Article.objects.filter(publications__in=[p1,p2]).distinct()
)

print(
Publication.objects.filter(id=1)
)

print(
Publication.objects.filter(pk=1)
)

print(
Publication.objects.filter(article__headline__startswith="NASA")
)

t = Publication.objects.filter(article__headline__startswith="NASA")
print(str(t.query))

print(Publication.objects.filter(article__id=1))
tt = Publication.objects.filter(article__id=1)
print(str(tt.query))

ttt = Publication.objects.filter(article__pk=1)
print(str(ttt.query))

t4 = Publication.objects.filter(article=1)
print(str(t4.query))

t5 = Publication.objects.filter(article=a1)
print(str(t5.query))

t6 = Publication.objects.filter(article__in=[1,2]).distinct()
print(str(t6.query))

t7 = Publication.objects.filter(article__in=[a1,a2]).distinct()
print(str(t7.query))

t8 = Article.objects.exclude(publications=p2)
print(str(t8.query))

p1.delete()
print(Publication.objects.all())
a1 = Article.objects.get(pk=1)

print(a1.publications.all())

a2.delete()
Article.objects.all()
p2.article_set.all()


a4 = Article(headline='NASA finds intelligent life on Earth')
a4.save()
p2.article_set.add(a4)
p2.article_set.all()
a4.publications.all()

new_article = p2.article_set.create(headline='Oxygen-free diet works wonders')
p2.article_set.all()
a5 = p2.article_set.all()[1]
a5.publications.all()

a4.publications.remove(p2)
p2.article_set.all()
a4.publications.all()

p2.article_set.remove(a5)
p2.article_set.all()
a5.publications.all()

p2.article_set.clear()
p2.article_set.all()