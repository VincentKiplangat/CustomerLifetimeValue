from django.db import models

# Create your models here.
class Clv(models.Model):
  # CustomerID = models.CharField(max_length=15)
  age = models.IntegerField()
  price = models.IntegerField()
  lifetime_months = models.IntegerField()
  channel_email = models.BooleanField()
  channel_phone = models.BooleanField()
  reason_signup = models.BooleanField()
  reason_support = models.BooleanField()
  gender_female = models.BooleanField()
  gender_male = models.BooleanField()
  subscription_annual_subscription = models.BooleanField()
  subscription_monthly_subscription = models.BooleanField()
  signup_period_Morning = models.BooleanField()
  signup_period_Night = models.BooleanField()
  signup_period_Noon = models.BooleanField()
  end_period_Morning = models.BooleanField()
  end_period_Night = models.BooleanField()
  end_period_Noon = models.BooleanField()




# ******************************************************************************


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    mode_of_contact = models.CharField('Contact by', max_length=50)
    question_categories = models.CharField('How can we help you?', max_length=50)
    message = models.TextField(max_length=3000)

    def __str__(self):
        return self.email

    # Newsletter
    # ****************************************************************
class NewsletterUser(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email