from django.db import models

# 公告表
class announceTable(models.Model):
    sort = models.CharField(max_length=100) #varchart(20)
    title = models.CharField(max_length=225)
    date = models.DateField()
    pageview = models.IntegerField()
    content = models.TextField()
    isDelete = models.BooleanField(default=False)
    group = models.TextField(blank=True)

# 公告側邊表
class announceCard(models.Model):
    card1 = models.CharField(max_length=225)
    card2 = models.CharField(max_length=225)
    card3 = models.CharField(max_length=225)
    card4 = models.CharField(max_length=225)
    card5 = models.CharField(max_length=225)
    card6 = models.CharField(max_length=225)
    card7 = models.CharField(max_length=225)
    card8 = models.CharField(max_length=225)
    isDelete = models.BooleanField(default=False)
    group = models.TextField(blank=True)

# 行事曆表
class calendarTable(models.Model):
    title = models.TextField(blank=True)
    start = models.TextField(blank=True)
    end = models.TextField(blank=True)
    backgroundColor = models.TextField(blank=True)
    borderColor = models.TextField(blank=True)
    allDay = models.TextField(blank=True)
    content = models.TextField(blank=True)
    url = models.TextField(blank=True)
    urlForStu = models.TextField(blank=True)
    isDelete = models.BooleanField(default=False)
    group = models.TextField(blank=True)

# 打卡表
class clockinTable(models.Model):
    today = models.DateField()
    name = models.TextField()
    checkin = models.DateField(blank=True,null=True)
    checkout = models.DateField(blank=True,null=True)
    state = models.TextField(blank=True,null=True)
    shouldin = models.DateField(blank=True,null=True)
    shouldout = models.DateField(blank=True,null=True)
    isDelete = models.BooleanField(default=False,null=True)
    group = models.TextField(blank=True)

# 請假表
class leaveTable(models.Model):
    submitTime = models.DateField()
    name = models.TextField()
    fromTime = models.DateField()
    toTime = models.DateField()
    state = models.TextField()
    content = models.DateField(blank=True)
    check = models.DateField(blank=True)
    isDelete = models.BooleanField(default=False)
    group = models.TextField(blank=True)
#判斷每位學員當天是否請假
class dailyStateTable(models.Model):
    name = models.TextField()
    state = models.TextField()
    fromTime = models.DateField()
    isDelete = models.BooleanField(default=False)
    group = models.TextField(blank=True)
    
# groupAccountTable 群體編成表
class groupAccountTable(models.Model):
    name = models.TextField()
    account = models.TextField()
    group = models.TextField()
    date = models.DateField()
    isDelete = models.BooleanField(default=False)

# 集群名稱
class groupTable(models.Model):
    groupCode = models.TextField()
    name = models.TextField()
    isDelete = models.BooleanField(default=False)

