from django.db import models

# Create your models here.
class Theme(models.Model):
    theme_id = models.IntegerField()
    theme_name = models.CharField(max_length=300)
    def __str__(self):
        return self.theme_name

class LegoSet(models.Model):
    set_id = models.IntegerField()
    name = models.CharField(max_length=500)
    piece_count = models.IntegerField()
    price = models.FloatField()
    theme_id = models.ForeignKey(Theme, on_delete=models.CASCADE)
    status = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Customer(models.Model):
    lego_rewards_id  = models.IntegerField()
    name = models.CharField(max_length=500)
    set_id = models.ForeignKey(LegoSet, on_delete=models.CASCADE)
    budget = models.FloatField()
    def __str__(self):
        return self.name

class Reviews(models.Model):
    review_id = models.IntegerField()
    set_id = models.ForeignKey(LegoSet, on_delete=models.CASCADE)
    lego_rewards_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=1500)
    rating = models.IntegerField()
    def __str__(self):
        return self.review_id