from django.db import models




class SchoolLevel(models.Model): 
    levelName = models.CharField(max_length=100,null=True)
    subvote = models.IntegerField(null=True)
    def __str__(self):
        return self.levelName
    
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

# the District model
class District(models.Model):
    name = models.CharField(max_length=100)
    votecode = models.CharField(max_length=20, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}, {self.region}"

# the School model
class School(models.Model):
    registration = models.IntegerField( default = 1000, null=True, blank=True)
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    School_level = models.ForeignKey(SchoolLevel, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.name},{self.School_level},{self.region} {self.district}"