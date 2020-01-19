from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighborhood(models.Model):
    hoodname = models.TextField(max_length=500)
    hoodlocation=models.TextField(max_length=500)
    # admin = models.ForeignKey(Profile,on_delete=models.CASCADE)
    pic=models.ImageField(upload_to='images/')
    description=models.CharField(max_length=500)
    police_count=models.IntegerField(null=True,blank=True)
    police_info=models.TextField(max_length=3000,default='police@info.com')
    occupant = models.ForeignKey(User,on_delete=models.CASCADE)
    health = models.IntegerField()
    health_info = models.TextField(max_length=3000,default = 'Health@gmail.com')


    def __str__(self):
        return self.hoodname

    def create_hood(self):
        '''
        Function for creating a neighborhood
        '''
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def one_hood(cls,id):
        one_hood =  cls.objects.filter(id=id)
        return one_hood

    @classmethod
    def all_hoods(cls):
        '''
        Function to get all neighbourhoods
        '''
        all_hoods = cls.objects.all()
        return all_hoods
    



    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to='pictures/')
    email = models.CharField(max_length=300)
    username=models.TextField(max_length=500)
    hood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    

    def save_profile(self):
        '''
        Function to save a user profile
        '''
        self.save()

    def delete_profile(self):
        '''
        Function to delete a user profile
        '''
        self.delete()

    @classmethod
    def get_occupants(cls,hood_id):
        hood_occupants = cls.objects.filter(hood_id = hood_id)
        return hood_occupants




class Business(models.Model):
    name=models.CharField(max_length=1000)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    bizhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    bizemail=models.CharField(max_length=500)
    bizdescription=models.TextField(blank=True)

    def create_biz(self):
        self.save()

    def delete_biz(self):
        seld.delete()

    @classmethod
    def search_biz(cls,name):
        searched_biz=cls.objects.filter(name__icontains = name).all()
        return searched_biz
    
    @classmethod
    def all_biz(cls,bizhood_id):
        all_biz=cls.objects.filter(bizhood_id = bizhood_id)
        return all_biz

class Posts(models.Model):
    title = models.CharField(max_length=1000)
    post = models.TextField(max_length=3000)
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def post_by_hood(cls,hood_id):
        hoodpost = cls.objects.filter(hood_id = hood_id)
        return hoodpost

