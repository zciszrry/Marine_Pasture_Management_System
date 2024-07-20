# 智慧渔业可视化系统

## 项目概述

### 开发背景
中国在全球渔业养殖中具有重要地位。然而，目前我国水产养殖系统存在一系列问题。国外采用现代水质传感器技术和在线监控系统来全面监控养殖环境，并通过自动化养殖设备实现环境控制，提高效率，对环境起到积极作用。为了应对这些问题，中国在十四五发展计划中计划构建“物联网+海洋牧场”，通过物联网、大数据、云计算等现代信息技术，建立全面、实时、智能的养殖监控系统，精确控制养殖环境，提高效率，减少病害的发生。

### 项目目标
完成智慧可视化系统，包括以下模块：
- **数据处理与分析模块**：处理和分析数据，生成可视化所需的数据，支持数据上传和导出功能。
- **可视化展示模块**：将处理后的数据以图形化方式展示，包括地图和天气数据，并实现视频播放功能。
- **报警与通知模块**：在数据异常时及时向用户发送报警信息。
- **用户信息模块**：用户通过手机号或账号密码注册登录系统，查看可视化系统，不同用户权限不同。

### 开发环境
- 编程语言: Python 3.9
- 数据库管理系统: MySQL 8.0.32
- 后端框架: Django 4.2.13
- 操作系统: Windows 11

## 安装步骤

### 克隆仓库
```bash
git clone <repository-url>
cd <repository-name>
```

### 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # 在Windows上使用 `venv\Scripts\activate`
```

### 安装依赖
```bash
pip install -r requirements.txt

```

### 数据库设置
确保已安装MySQL，并创建所需数据库。
更新settings.py中的数据库配置：
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 运行迁移
```bash
python manage.py makemigrations
python manage.py migrate
```

### 创建超级用户
```bash
python manage.py createsuperuser
```

### 启动服务器
```bash
python manage.py runserver
```

## 系统功能

### 数据处理与分析模块
- 收集和处理水文数据，包括水温、盐度、溶解氧等。
- 支持历史数据存储和实时监控数据处理。
- 数据分析和统计功能，生成可视化所需的数据。

### 可视化展示模块
- 使用ECharts等前端框架展示数据图表。
- 集成地图API（如高德地图、百度地图）展示地理数据。
- 实时天气数据展示和视频播放功能。

### 报警与通知模块
- 实时监控数据异常，发送邮件或短信通知用户。
- 用户可自定义报警阈值和报警方式。

### 用户信息模块
- 用户注册、登录和权限管理。
- 安全措施如验证码等，保护用户信息。

## 数据库设计

### 用户表
- 存储用户信息，包括用户名、密码、手机号等。

### 设备表
- 存储设备信息，包括设备ID、类型、状态等。

### 鱼类表
- 存储鱼类信息，包括鱼类类型、数量、时间等。

### 水文数据表
- 存储水文数据，包括水温、盐度、溶解氧等。

### 其他表
- 详细设计请参考项目中的数据库模型定义。

## 测试
### 前端测试
使用Puppeteer进行前端功能测试，测试代码示例如下：
```bash
const puppeteer = require('puppeteer');

describe('Main Info Page', () => {
    let browser;
    let page;

    beforeAll(async () => {
        browser = await puppeteer.launch({ headless: true });
        page = await browser.newPage();
    });

    afterAll(async () => {
        await browser.close();
    });

    it('should load hydro data and update the DOM', async () => {
        await page.goto('http://127.0.0.1:8000/app01/info');
        await page.waitForSelector('#hydroDataContainer .data-field');
        const hydroDataContainer = await page.$eval('#hydroDataContainer', el => el.innerText);
        expect(hydroDataContainer).toContain('溶解氧 (mg/L)');
    });
});
```

### 后端测试
使用Django自带的测试框架，示例如下：
```bash
from django.test import TestCase
from .models import Staff, Account, FishGroup

class StaffModelTest(TestCase):
    def setUp(self):
        Staff.objects.create(name="John Doe", position="Manager", gender="M", age=35, phone_number="1234567890")

    def test_staff_creation(self):
        staff = Staff.objects.get(name="John Doe")
        self.assertEqual(staff.position, "Manager")
```

## 贡献
欢迎对本项目做出贡献，请遵循以下步骤：

- Fork 本仓库
- 创建 feature 分支 (git checkout -b feature/AmazingFeature)
- 提交更改 (git commit -m 'Add some AmazingFeature')
- 推送到分支 (git push origin feature/AmazingFeature)
- 打开 Pull Request

## 许可证
该项目使用 MIT 许可证，详情请参见 LICENSE 文件。


## 联系方式
如有任何问题或建议，请通过 18086215842@163.com 联系我们。




