from django.db import models

# Create your models here.

# class Staff(models.Model):
#     name=models.CharField(max_length=32)
#     position=models.CharField(max_length=32)

class Staff(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    STATE_CHOICES=(
        ('N','正常'),# normal
        ('A','异常'),# abnormal
    )
    id = models.AutoField(primary_key=True)  # 自增主键
    name = models.CharField(max_length=45, null=True)
    position = models.CharField(max_length=45, null=True)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, null=True)
    age = models.IntegerField(null=True)
    phone_number = models.IntegerField(null=True)
    state = models.CharField(max_length=45,choices=STATE_CHOICES, null=True)

class Account(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)



class FishGroup(models.Model):
    type = models.CharField(max_length=45, null=True)
    number = models.CharField(max_length=45, null=True)
    time = models.DateField(null=True)

    def __str__(self):
        return f"FishGroup {self.id}"

class Fish(models.Model):
    type = models.CharField(max_length=45, null=True)
    weight = models.FloatField(null=True)  # 对应 FLOAT 类型
    length1 = models.FloatField(null=True)
    length2 = models.FloatField(null=True)
    length3 = models.FloatField(null=True)
    height = models.FloatField(null=True)
    width = models.FloatField(null=True)


    def __str__(self):
        return f"Fish {self.id}"


class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=True)
    category = models.CharField(max_length=45, null=True)  # 设备种类名
    type = models.CharField(max_length=45, null=True)
    memory = models.IntegerField(null=True)  # memory 是一个整数
    run_time = models.DateTimeField(null=True)
    next_repair_time = models.DateField(null=True)
    warranty_time = models.DateField(null=True)

    def __str__(self):
        return f"{self.category} {self.device_id} - {self.type}"



class Sensor(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)  # 将device外键字段作为主键
    type = models.CharField(max_length=20)
    battery_level = models.PositiveIntegerField()
    next_repair_time = models.DateTimeField()
    warranty_time = models.DateField()



class HydrologicInfo(models.Model):

    monitoring_time = models.DateField(null=True,blank=True)  # 监测时间
    water_quality_category = models.CharField(max_length=20,null=True,blank=True)  # 水质类别
    water_temperature = models.FloatField(null=True,blank=True)  # 水温（℃）
    pH = models.FloatField(null=True,blank=True)  # pH(无量纲)
    dissolved_oxygen = models.FloatField(null=True,blank=True)  # 溶氧量(mg/L)
    conductivity = models.FloatField(null=True,blank=True)  # 电导率（μS/cm）
    turbidity = models.FloatField(null=True,blank=True)  # 浊度（NTU）
    permanganate_index = models.FloatField(null=True,blank=True)  # 高锰酸盐指数（mg/L）
    ammonia_nitrogen = models.FloatField(null=True,blank=True)  # 氨氮（mg/L）
    total_phosphorus = models.FloatField(null=True,blank=True)  # 总磷（mg/L）
    total_nitrogen = models.FloatField(null=True,blank=True)  # 总氮（mg/L）
    station_condition = models.TextField(null=True,blank=True)  # 站点情况

    def __str__(self):
        return f"Hydrologic Info {self.id} at {self.monitoring_time.strftime('%m-%d')}"

    class Meta:
        verbose_name = 'Hydrologic Information'
        verbose_name_plural = 'Hydrologic Information'

    def calculate_environment_score(self):
        # 假设环境评分的计算是基于一些水质参数的简单加权和
        score = 0
        if self.water_temperature:
            score += self.water_temperature * 0.1
        if self.pH:
            score += self.pH * 0.2
        if self.dissolved_oxygen:
            score += self.dissolved_oxygen * 0.3
        if self.conductivity:
            score += self.conductivity * 0.1
        if self.turbidity:
            score += self.turbidity * 0.1
        if self.permanganate_index:
            score += self.permanganate_index * 0.1
        if self.ammonia_nitrogen:
            score += self.ammonia_nitrogen * 0.05
        if self.total_phosphorus:
            score += self.total_phosphorus * 0.05
        if self.total_nitrogen:
            score += self.total_nitrogen * 0.05

        # 假设原始评分的理论最大值为10
        max_score = 10
        # 将原始评分缩放到0到100之间
        normalized_score = (score / max_score) * 100

        # 确保评分在0到100之间
        normalized_score = max(0, min(100, normalized_score))

        return normalized_score

class NetCage(models.Model):
    id = models.AutoField(primary_key=True)
    width = models.FloatField(null=True)  # 网箱宽度
    length = models.FloatField(null=True)  # 网箱长度
    depth = models.FloatField(null=True)  # 网箱深度
    longitude = models.FloatField(null=True)  # 经度
    latitude = models.FloatField(null=True)  # 纬度

    def __str__(self):
        return f"Net Cage {self.id}"