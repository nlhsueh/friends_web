from django.db import models

# Create your models here.
  
class Season(models.Model):
  season_number = models.IntegerField() # 第幾季
  description = models.TextField(max_length=1500) # 該季主要劇情描述

  def __str__(self):
    #  d = self.description[0,20]
     return f"Season {self.season_number}: {self.description}"         

class Episode(models.Model):

  season = models.ForeignKey(Season, models.CASCADE) # 所連接的季
  ep_number = models.IntegerField() # 第幾集
  ep_title = models.CharField(max_length=255) # 集標題
  eng_plot = models.TextField(null=True, max_length=2000) # 該集英文描述
  tw_plot = models.TextField(null=True, max_length=2000) # 該集中文描述

  def __str__(self):
    # 例如：EP1-1: Pilot
    return f"EP{self.season.season_number}-{self.ep_number}: {self.ep_title}"  

class Cast (models.Model):
  name = models.CharField(max_length=50)
  img_url = models.CharField(max_length=250)
  introduction = models.TextField(max_length=2000)

  def __str__(self):
    return (self.name)