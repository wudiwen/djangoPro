from django.http import HttpResponse
from app.models import Test

def testdb(request):
    test1 = Test(name='ting')
    test1.save()
    return HttpResponse('数据库djangoday1添加name成功')