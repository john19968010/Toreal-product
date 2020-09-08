from django.shortcuts import render, redirect, HttpResponse
from .models import Card ,User



def index(request):
	if 'email' in request.session:
		return redirect('user/')
	else:
		return render(request,"index.html")

def member_login(request):                            	#登入頁
	if 'email' in request.session:
		return redirect('/')
	else:
		return render(request,"member_login.html")

def member_profile(request):	                       	#新會員基本資料初始
	
	return render(request,"member_profile.html")

def score(request):								#配對分數頁面初始
	if 'email' in request.session:
		return render(request,"member_score.html")
	else:
		return redirect('/')
		

def image(request):
	if 'email' in request.session:
		e = request.session['email'] 
		check = User.objects.get(email = e)

	return render(request,"image.html",locals())

def user_page(request):                                 #個人頁面初始
	if 'email' in request.session:
		e = request.session['email'] 
		check = User.objects.get(email = e)
		print('---------------使用者: {} 登入-----------------'.format(check.fullname))
		return render(request,"user_page.html",{'check':check})
	else:
		return redirect('/')

def user_loc(request):                                  #打卡區初始
	if 'email' in request.session:
		check = User.objects.all()
		return render(request,"user_loc.html",locals())
	else:
		return redirect('/')

def user_pw_info(request):                            	#修改密碼初始
	if 'email' in request.session:
		return render(request,"user_pw_info.html")
	else:
		return redirect('/')


def user_info(request):                                 #會員資料修改初始
	if 'email' in request.session:
		e = request.session['email'] #
		check = User.objects.get(email = e)
		if check.gender == 'M':
			check.gender = '男'
		else:
			check.gender = '女'
		if check.find_gender == 'M':
			check.find_gender = '找男生'
		elif check.find_gender == 'F':
			check.find_gender = '找女生'
		else :
			check.find_gender = '不拘'
		return render(request,"user_info.html",{'check':check})
	else:
		return redirect('/')

#-------------------------------------------------------------------------------

def logout(request):                          #登出用
	if 'email' in request.session:
		e = request.session['email']
		check = User.objects.get(email = e)	                              
		del request.session['email']
		request.session.flush()
		print('---------------使用者: {} 登出-----------------'.format(check.fullname))		
		return redirect('/')


def score1(request):
	if 'email' in request.session:
		e = request.session['email']
		Fir = User.objects.get(email = e)	 
		
		if request.method == 'POST':
			sec = request.POST.get('sec')
			data = User.objects.all()
			for i in data:
				
				if sec in i.fullname:
					Sec = i	
				
					count = 0
					if Fir.test[0] == Sec.test[0]:
						count += 10
					if Fir.test[1] == Sec.test[1]:
						count += 10
					if Fir.test[2] == Sec.test[2]:
						count += 10
					if Fir.test[3] == Sec.test[3]:
						count += 10
					if abs(int(Fir.test[4]) - int(Sec.test[4])) <= 3:
						count += 10
					if abs(int(Fir.test[4]) - int(Sec.test[4])) > 3 and abs(int(Fir.test[4]) - int(Sec.test[4])) <= 6:
						count += 5
					if abs(int(Fir.test[4]) - int(Sec.test[4])) > 6 and abs(int(Fir.test[4]) - int(Sec.test[4])) <= 9:
						count += 1
					if Fir.test[5] == Sec.test[5]:
						count += 10
					if Fir.test[6] == Sec.test[6]:
						count += 10
					if Fir.test[7] == Sec.test[7]:
						count += 10
					if Fir.test[8] == Sec.test[8]:
						count += 10
					if Fir.test[9] == Sec.test[9]:
						count += 10
					if Fir.test[10] == Sec.test[10]:
						count += 10
					count = (count / 110) * 100
					num = round(count, 2)
			
					return render(request,"member_score.html",{'score':num})
				
				if sec not in i.fullname:
					return render(request,"member_score.html",{'score':'他或她不是我們的會員唷'})
		
		



def user(request):	                                      #登入頁function
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		check = User.objects.get(email = email)	
		checkbox = request.POST.get('check')
		if check.email == email and check.password == password:
			request.session['email']= check.email
			return redirect('user/')
		else:
			return render(request,"member_login.html",{'name':'帳號或密碼錯誤'})


def profile(request):	                       	          #會員基本資料頁一
	if request.method == 'POST':
		fullname = request.POST.get('fullname')
		nickname = request.POST.get('nickname')
		gender = request.POST.get('gender')
		find_gender = request.POST.get('find_gender')
		age = request.POST.get('age')
		height = request.POST.get('height')
		county = request.POST.get('county')
		district = request.POST.get('district')
		email = request.POST.get('email')  
		image = request.FILES.get('image')                      
		password = request.POST.get('password')
		data = User(
			fullname=fullname, 
			nickname=nickname,  
			gender=gender,
			find_gender = find_gender,
			age = age,
			height = height,
			county = county,
			district = district,
			email = email,
			image = image,                                      
			password = password,				
		)
		
	e = []
	check = User.objects.all()
	for i in check:
		e.append(i.email)
	if data.email in e:
		return render(request,"member_profile.html",{'name':'E-mail已註冊！ 請重新輸入'})
	else:
		data.save()
		request.session['email']= email
		return render(request,"test.html")
#------------------------------------------------------------------------------------------

def info_update(request):                         #修改會員資料更新

	return redirect('user/')                      #導回使用者頁面

def pw_update(request):
	if 'email' in request.session:
		if request.method == 'POST':
			e = request.session['email'] 
			check = User.objects.get(email = e)
			old_password = request.POST.get('old＿password')         #get html輸入的舊密碼
			if old_password != check.password:
				return render(request,"user_pw_info.html",{'name':'密碼錯誤'})
			else:
				password = request.POST.get('password')
				check_password = request.POST.get('check_password')
				check.password = password   #將check.password 換成get到的新密碼
				check.save()                # save
				return redirect('user/') 
		return redirect('/')
	else:
		return redirect('/')	

def test(request):                                #心理測驗
	if 'email' in request.session:
		if request.method == 'GET':
			test = request.GET.get('test') 
			return render(request,"myself.html")
	else:
		return redirect('/')





def myself(request):                            #自評表
	if 'email' in request.session:
		if request.method == 'GET':
			pass
			return redirect('user/')
	else:
		return redirect('/')

def msg(request):                                 #訊息
	e = request.session['email'] 
	check = User.objects.get(email = e)
	if 'email' in request.session:
		if request.method == 'GET':
			i = request.GET.get('userid')
			userid = User.objects.get(id = i)
			return render(request,"user_loc.html")
		if request.method == 'POST':

			
			pass
	return redirect('loc/')

def image_upload(request):
	if 'email' in request.session:
		e = request.session['email'] 
		check = User.objects.get(email = e)
		if request.method == 'GET':

			return redirect('user/')


