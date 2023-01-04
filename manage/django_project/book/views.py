from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from book.models import *



# Create your views here.
def test_templates(request):
	dir={1:1,2:2}


def index(request):
	# return HttpResponse('ok!')
	context = {'title':'测试模板数据'}
	return render(request, 'book/index.html', context)

def bookList(request):
	books = BookInfo.objects.all()
	context = {'books': books}
	return render(request, 'book/bookList.html', context)

def testproject(request):
	return HttpResponse('测试项目')

def testmodel(request):
	context = {
		'city' : '北京',
		'adict' : {
			'name' : '西游记',
			'author' : '吴承恩'
		},
		'alist': [1, 2, 3, 4, 5],
		'time' : ''
	}
	return render(request, 'book/testmodel.html', context)

class LoginView():

	def	post(self,request):
		username = request.POST.get("username")
		password = request.POST.get("password")


# return render(request,'test_tes.html',dir)