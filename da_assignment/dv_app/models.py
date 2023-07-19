from django.db import models

# Create your models here.
class DB_Visual(models.Model):
    end_year=models.DateField(blank=True,null=True)
    intensity=models.IntegerField(blank=True,null=True)
    sector=models.CharField(max_length=20,blank=True,null=True)
    topic=models.CharField(max_length=1000,blank=True,null=True)
    insight=models.CharField(max_length=1000,blank=True,null=True)
    url=models.CharField(max_length=1000,blank=True,null=True)
    region=models.CharField(max_length=50,blank=True,null=True)
    start_year=models.DateField(blank=True,null=True)
    impact=models.CharField(max_length=200,blank=True,null=True)
    added=models.DateTimeField(blank=True,null=True)
    published=models.CharField(blank=True,null=True,max_length=40)
    country=models.CharField(max_length=300,blank=True,null=True)
    relevance=models.IntegerField(blank=True,null=True)
    pestle=models.CharField(max_length=200,blank=True,null=True)
    source=models.CharField(max_length=200,blank=True,null=True)
    title=models.CharField(max_length=800,blank=True,null=True)
    likelihood=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f'{self.topic}'


