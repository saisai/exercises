from django.db import models

# Create your models here.

class Jobs_db(models.Model):

    title = models.CharField(max_length=500)
    link = models.TextField()
    time = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateField(null=True, blank=True)


    def search(self, data):
        return Jobs_db.objects.filter(title=data)
        #result = []
        #for p in Jobs_db.objects.raw('SELECT title FROM jobs_db WHERE title = %s',[data.upper()]):
            #result.append(p)
        #return result
        #return "test from jobs_db %s" % data

    def __str__(self):
        return '%s %s %s %s' % (self.title, self.link, self.time, self.created_date)

    class Meta:
        db_table = "jobs_db"
        ordering = ['id']
