import requests
from django.shortcuts import render,HttpResponse,redirect
from app01.models import Staff
from app01.models import Account
from app01.models import HydrologicInfo
from app01.models import FishGroup
from app01.models import NetCage
from app01.models import Sensor
from app01.models import Fish
from app01.models import Device
from . import models
from .utils.error import *
import hashlib
import numpy as np
from scipy.stats import gaussian_kde
from .utils import getHomeData
from django.db.models import Sum
from django.db.models import Count
from collections import defaultdict
from datetime import date

# Create your views here.

# 默认参数 request

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(pwd.encode())
        pwd = md5.hexdigest()

        try:
            user=Account.objects.get(username=uname,password=pwd)
            request.session['username']=user.username
            return redirect('/app01/home')
        except:
            return errorResponse(request, '用户名或密码错误')

def registry(request):
    if request.method=='GET':
        return render(request,'registry.html')
    else:
        uname=request.POST.get('username')
        staff_id=request.POST.get('staff_id')
        pwd=request.POST.get('password')
        # print(uname,staff_id,pwd)
        try:
            Staff.objects.get(id=staff_id)
        except:
            return errorResponse(request,'非本公司职员无法注册')
        try:
            Account.objects.get(username=uname)
        except:
            md5=hashlib.md5()
            md5.update(pwd.encode())
            pwd=md5.hexdigest()
            Account.objects.create(id=int(staff_id),username=uname,password=pwd)
            return redirect('/app01/login')

        return errorResponse(request, '该用户名已经被注册')

def control(request):
    # 获取所有信息
    data_list=Staff.objects.all()
    # print(data_list)
    return render(request,"control.html",{"data_list":data_list})

def logout(request):
    request.session.clear()
    return redirect('login')

def home(request):
    uname=request.session.get('username')
    user=Account.objects.get(username=uname)
    staffinfo=Staff.objects.get(id=user.id)
    y,m,d=getHomeData.getNowTime()
    return render(request,'index.html',{
        'staffInfo':staffinfo,
        'userInfo':user,
        'dateInfo':{'year':y,'month':m,'day':d},
    })


# Create your views here.
def account_list(request):

    account_list = Account.objects.all()

    return render(request, "account_list.html", {"account_list": account_list})

def account_add(request):
    if request.method == "GET":
        return render(request, "account_add.html")

    # 获取用户提交的部门数据
    account_id = request.POST.get("account_id")
    uname = request.POST.get("username")
    pwd = request.POST.get("password")

    md5 = hashlib.md5()
    md5.update(pwd.encode())
    pwd = md5.hexdigest()

    # 保存到数据库
    Account.objects.create(id=account_id,username=uname,password=pwd)

    return redirect("/app01/account/list/")

def account_delete(request):

    id = request.GET.get('id')
    Account.objects.filter(id=id).delete()

    # 重定向回部门列表
    return redirect("/app01/account/list/")


def account_edit(request, nid):
    """部门编辑"""

    if request.method == "GET":
        # 根据nid,获取数据
        row_object = Account.objects.filter(id=nid).first()
        return render(request, 'account_edit.html', {"row_object": row_object})

    # 如果是POST请求,保存修改
    # id = request.POST.get("id")
    uname = request.POST.get("username")
    pwd = request.POST.get("password")

    md5 = hashlib.md5()
    md5.update(pwd.encode())
    pwd = md5.hexdigest()

    Account.objects.filter(id=nid).update(username=uname,password=pwd)

    # 重定向回部门列表
    return redirect('/app01/account/list/')

def staff_list(request):

    staff_list = Staff.objects.all()

    return render(request, "staff_list.html", {"staff_list": staff_list})

# from django import forms
# class StaffModelForm(forms.ModelForm):
#     class Meta:
#         model=Staff
#         fields=["id", "username", "position"]
#
#
# def staff_add(request):
#     if request.method == "GET":
#         form = StaffModelForm()
#     return render(request, "staff_add.html", {"form": form})

def data(request):
    return render(request, "index2.html" )

def info(request):
    return render(request, "main_info.html" )

def center(request):
    return render(request, "intelligence_center.html" )


def water(request):
    # 水质信息+环境评分（最新）
    latest_hydrologic_info = HydrologicInfo.objects.latest('monitoring_time')
    latest_environment_score = latest_hydrologic_info.calculate_environment_score()

    # 绘制总数-时间折线
    fish_groups = FishGroup.objects.all().order_by('time')
    fish_data = [{'time': fg.time.strftime('%Y-%m-%d'), 'number': int(fg.number)} for fg in fish_groups]

    # 鱼群各种类数量
    fish_groups = FishGroup.objects.values('type').annotate(total_number=Sum('number'))
    fish_data_type = [{'type': fg['type'], 'total_number': fg['total_number']} for fg in fish_groups]

    # 传感器
    NetCage_data =NetCage.objects.first()
    Sensor_data =Sensor.objects.first()

    # 鱼群重量信息
    fish_weights = list(Fish.objects.values_list('weight', flat=True))

    # 使用核密度估计 (Kernel Density Estimation) 计算概率密度函数
    kde = gaussian_kde(fish_weights)
    weight_min = min(fish_weights)
    weight_max = max(fish_weights)
    x_values = np.linspace(weight_min, weight_max, 1000)
    density_values = kde(x_values)

    # 归一化使得面积为1
    density_values /= np.trapz(density_values, x_values)

    # 计算鱼群总数
    total_fish_groups = FishGroup.objects.count()

    # 计算鱼种类总数
    fish_species = Fish.objects.values('type').distinct()
    total_fish_species = fish_species.count()

    # 计算总设备数
    total_devices = Device.objects.count()

    # 查询不同设备种类的数量
    category_counts = Device.objects.values('category').annotate(count=Count('category'))
    # 获取设备种类的总数
    total_categories = category_counts.count()

    # 查询所有鱼群数据，按时间顺序排列
    fish_groups = FishGroup.objects.order_by('type', '-time')

    # 初始化一个字典来存储每种鱼群类型对应的最新数量和时间
    fish_type_dict = {}

    # 遍历每条鱼群数据，更新每种鱼群类型对应的最新数量和时间
    for fish_group in fish_groups:
        if fish_group.type in fish_type_dict:
            # 如果鱼类型在字典中，比较日期并更新数量和时间
            if fish_group.time > fish_type_dict[fish_group.type]['time']:
                fish_type_dict[fish_group.type] = {
                    'number': int(fish_group.number),
                    'time': fish_group.time
                }
        else:
            # 如果鱼类型不在字典中，添加类型和数量到字典中
            fish_type_dict[fish_group.type] = {
                'number': int(fish_group.number),
                'time': fish_group.time
            }

    # 求和所有鱼群类型对应的最新数量
    total_latest_fish = sum(item['number'] for item in fish_type_dict.values())

    context = {
        "latest_hydrologic_info": latest_hydrologic_info,
        "latest_environment_score": latest_environment_score,
        'fish_data': fish_data,
        'fish_data_type': fish_data_type,
        'netcage_data': NetCage_data,
        'sensor_data':Sensor_data,
        'x_values': x_values.tolist(),
        'density_values': density_values.tolist(),
        'total_fish_groups': total_fish_groups,
        'total_fish_species': total_fish_species,
        'total_devices': total_devices,
        'total_categories': total_categories,
        'total_latest_fish': total_latest_fish
    }
    return render(request, "water.html", context)

#git,分支B2
#git,分支C4