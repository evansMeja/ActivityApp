from django.db import models

class ActivityStatus(models.Model):
    status = models.CharField(max_length=50,default="ok")

    def __str__(self):
        return str(self.status)

class ActivityMembers(models.Model):
    activity_user_owner = models.ForeignKey(ActivityStatus,on_delete=models.CASCADE, default=1)
    member_id = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100,blank=True,null=True)
    tz = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return str(self.real_name)


class ActivityPeriods(models.Model):
    activity_period_owner = models.ForeignKey(ActivityMembers,on_delete=models.CASCADE, default=1)
    start_time = models.DateField()
    end_time = models.DateField()

    def __str__(self):
        return str(self.start_time)
