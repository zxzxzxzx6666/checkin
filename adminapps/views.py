from django.shortcuts import render ,redirect
from django.http import HttpResponse ,JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from adminapps.models import announceTable ,announceCard ,calendarTable ,groupAccountTable ,groupTable ,clockinTable
from datetime import date
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
import datetime
import json

# 登入頁面
def index(request):
    return render(request, 'adminapps/index.html')

# 登入判斷
def login(request):
    # 若有登入直接導向公告欄
    if request.user.is_authenticated:
        return redirect('/announce')
    # 進行驗證
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    # 驗證成功導向公告欄，失敗則回登入頁面
    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('/announce')
    else:
        return redirect('/')

# 儀表板（尚未開發）
# 若沒有登入則會重新導向登入頁面
@login_required(login_url='/')
def charts(request):
    return render(request, 'adminapps/charts.html')

# 公布欄（開發中）
# 若沒有登入則會重新導向登入頁面
@login_required(login_url='/')
def announce(request):
    user = request.user
    groupObject = groupAccountTable.objects.filter(isDelete="0",account = user)
    group = groupObject[0].group
    return render(request, 'adminapps/announce.html',locals())

# 公告後台管理（開發中）
#若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def backstage(request):
    return render(request, 'adminapps/backstage.html')

# 儀表板後台管理（尚未開發）
# 若沒有登入則會重新導向登入頁面
@login_required(login_url='/')
def backstaged(request):
    return render(request, 'adminapps/backstaged.html')

# 公告內容與資料庫取資料（開發完成）
# 若沒有登入則會重新導向登入頁面
@login_required(login_url='/')
def announce_main(request):
    user = request.user
    groupObject = groupAccountTable.objects.filter(isDelete="0",account = user)
    group = groupObject[0].group
    if user.is_superuser:
        list1 = announceTable.objects.filter(isDelete="0" ).order_by('-id')
    else:
        list1 = announceTable.objects.filter(isDelete="0" , group = group).order_by('-id')
    list2 = []
    for item in list1:
        # 取得資料欄位
        list2.append([item.id,item.sort,item.title ,item.date,item.pageview,item.content,item.group])
    return JsonResponse({'data': list2})

# 公告內容與資料庫取資料（開發完成）
# 若沒有登入則會重新導向登入頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def backstage_main(request):
    user = request.user
    groupObject = groupAccountTable.objects.filter(isDelete="0",account = user)
    group = groupObject[0].group
    list1 = announceTable.objects.filter(isDelete="0").order_by('-id')
    list2 = []
    try:
        group = request.session['announcegroup']
        list1 = announceTable.objects.filter(isDelete="0" , group = group).order_by('-id')
    except:
        print("announcegroup except")
    
    for item in list1:
        # 取得資料欄位
        list2.append([item.id,item.sort,item.title ,item.date,item.pageview,item.content,item.group])
    return JsonResponse({'data': list2})

# 取得session 與重新導向
# 若沒有登入則會重新導向登入頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def MannounceGroupSession(request):
    # 若有登入直接導向公告欄
    group = request.POST.get("group")
    request.session['announcegroup']=group
    #紀錄group session
    request.session.set_expiry(0)
    return JsonResponse({'': ''})


# 公告內容（卡片）與資料庫取資料（開發完成）
# 若沒有登入則會重新導向登入頁面
@login_required(login_url='/')
def announce_card(request):
    #取得group
    user = request.user
    groupObject = groupAccountTable.objects.filter(isDelete="0",account = user)
    group = groupObject[0].group
    if user.is_superuser:
        try:
            group = request.session['announcegroup']
        except:
            print("announcegroup card wrong")

    #篩選group資料
    list1 = announceCard.objects.filter(group = group)
    list2 = []
    for item in list1:
        list2.append([item.card1,item.card2,item.card3,item.card4,item.card5,item.card6,item.card7,item.card8])
    return JsonResponse({'data': list2})

# 公告內容（開發完成）
# 若沒有登入則會重新導向登入頁面
@login_required(login_url='/')
def announceContent(request,id):#將變數引入
    # 將變數帶入dict 可直接從前端抓取 抓取方式 {{id.title}}
    content = {'id':id}
    return render(request, 'adminapps/announceContent.html',content)

# 公告內容管理頁面（開發中）
#若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def MannounceContent(request):
    return render(request, 'adminapps/MannounceContent.html')

#若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def MannounceAdd(request):
    return render(request, 'adminapps/MannounceAdd.html')

# announce 新增資料
#若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Mannounce_Add(request):
    sort = request.POST.get('sortText')
    title = request.POST.get('titleText')
    time = request.POST.get('timeText')
    content = request.POST.get('contentText')
    pageview = request.POST.get('pageviewText')
    group = request.POST.get('group')
    data = announceTable(
        sort=sort, 
        title=title,
        date = time,
        content = content,
        pageview = pageview,
        group = group,
    )
    data.save()


    return JsonResponse({'': ''})

# announceDelete 取得資料
#若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def MannounceDelete(request,id):
    content = {'id':id}
    return render(request, 'adminapps/MannounceDelete.html',content)

# 管理介面 公告新增
#若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Mannounce_Update(request):
    # 定義post變數
    sort = request.POST.get('sortText')
    title = request.POST.get('titleText')
    time = request.POST.get('timeText')
    content = request.POST.get('contentText')
    pageview = request.POST.get('pageviewText')
    id = request.POST.get('idText')
    # 更新資料
    item = announceTable.objects.filter(id=id)
    item.update(sort=sort)
    item.update(title=title)
    item.update(date=time)
    item.update(content=content)
    item.update(pageview=pageview)
    # item.id,item.sort,item.title ,item.date,item.pageview,item.content
    return JsonResponse({'': ''})
    
# 管理介面 公告刪除
#若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Mannounce_Delete(request):
    id = request.POST.get('idText')
    item = announceTable.objects.filter(id=id)
    item.update(isDelete="1")
    # item.id,item.sort,item.title ,item.date,item.pageview,item.content
    return JsonResponse({'':''})

#若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def MannounceCard_Update(request):
    card = request.POST.get('card')
    name = request.POST.get('name')
    value = request.POST.get('value')
    item = announceCard.objects.filter(id=1)
    item2 = announceCard.objects.filter(id=2)
    if card == 'card1':
        item.update(card1=name)
        item2.update(card1=value)
    if card == 'card2':
        item.update(card2=name)
        item2.update(card2=value)
    if card == 'card3':
        item.update(card3=name)
        item2.update(card3=value)
    if card == 'card4':
        item.update(card4=name)
        item2.update(card4=value)
    if card == 'card5':
        item.update(card5=name)
        item2.update(card5=value)
    if card == 'card6':
        item.update(card6=name)
        item2.update(card6=value)
    if card == 'card7':
        item.update(card7=name)
        item2.update(card7=value)
    if card == 'card8':
        item.update(card8=name)
        item2.update(card8=value)
    return JsonResponse({'':''})

@login_required(login_url='/')
def calendar(request):
    return render(request, 'adminapps/calendar.html')

#若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def backstageC(request):
    return render(request, 'adminapps/backstageC.html')

# 重新導入目前的行事曆到資料庫 (行事曆資料不會更新到javascript變數)
# 若不是superuser則重新導向進入公告頁面
# @user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
# def Mcalendar_renew(request):
#     # 刪除所有的欄位
#     calendarTable.objects.all().delete()
#     # 新增一個row的function
#     def insert(calendarTable,title,start,end,allDay,backgroundColor,borderColor):
#         data = calendarTable(
#             title = title,
#             start = start,
#             end = end,
#             allDay = allDay,
#             backgroundColor = backgroundColor,
#             borderColor = borderColor,
#         )
#         data.save()
#     # 接收post資料
#     calendardict = json.loads(request.POST.get("calendardict"))
#     # 每個for迴圈傳送一行資料
#     for i in calendardict:
#         keys = calendardict[i].keys()
#         title = calendardict[i]['title'] if 'title' in keys else ''
#         start = calendardict[i]['start'] if 'start' in keys else ''
#         end = calendardict[i]['end'] if 'end' in keys else ''
#         allDay = calendardict[i]['allDay'] if 'allDay' in keys else ''
#         backgroundColor = calendardict[i]['backgroundColor'] if 'backgroundColor' in keys else ''
#         borderColor = calendardict[i]['borderColor'] if 'borderColor' in keys else ''
#         insert(calendarTable,title,start,end,allDay,backgroundColor,borderColor)

#     return JsonResponse({'':''})

# 行事曆內容
@login_required(login_url='/')
def calendar_main(request):
    user = request.user
    groupObject = groupAccountTable.objects.filter(isDelete="0",account = user)
    group = groupObject[0].group

    list1 = calendarTable.objects.filter(isDelete="0", group = group)
    list2 = []
    for item in list1:
        # 取得資料欄位
        list2.append({
            'title':item.title,
            'start':item.start,
            'end':item.end ,
            'backgroundColor':item.backgroundColor,
            'borderColor':item.borderColor,
            'allDay':item.allDay,
            'id':item.id,
            'content':item.content,
            'url':item.urlForStu
            })
    return JsonResponse({'data': list2})

# 取得session 與重新導向
# 若沒有登入則會重新導向登入頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def McalendarGroupSession(request):
    # 若有登入直接導向公告欄
    group = request.POST.get("group")
    request.session['calendargroup']=group
    #紀錄group session
    request.session.set_expiry(0)
    return JsonResponse({'': ''})
# 行事曆內容
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Mcalendar_main(request):
    try:
        group = request.session['calendargroup']
    except:
        group = ""
        print("Mcalendar_main group error")
    
    list1 = calendarTable.objects.filter(isDelete="0" , group = group).order_by('-start')
    list2 = []
    for item in list1:
        # 取得資料欄位
        list2.append({
            'id':item.id,
            'title':item.title,
            'start':item.start,
            'end':item.end ,
            'backgroundColor':item.backgroundColor,
            'borderColor':item.borderColor,
            'allDay':item.allDay,
            'url':item.url,
            'content':item.content,
            'group':item.group,
            })
    return JsonResponse({'data': list2})

@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def McalendarDelete(request,id):
    content = {'id':id} 
    return render(request, "adminapps/McalendarDelete.html",content)

# 管理介面 行事曆新增
#若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Mcalendar_Update(request):
    # 定義post變數
    id = request.POST.get('idText')
    titleText = request.POST.get('titleText')
    startText = request.POST.get('startText')
    endText = request.POST.get('endText')
    contentText = request.POST.get('contentText')
    alldayText = request.POST.get('alldayText')
    colorText = request.POST.get('colorText')
    # 更新資料
    item = calendarTable.objects.filter(id=id)
    item.update(title = titleText)
    item.update(start = startText)
    item.update(end  = endText)
    item.update(content = contentText)
    item.update(allDay = alldayText)
    item.update(backgroundColor = colorText)
    item.update(borderColor = colorText)
    # item.id,item.sort,item.title ,item.date,item.pageview,item.content
    return JsonResponse({'': ''})  

# 課表刪除
# 若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Mcalendar_Delete(request):
    id = request.POST.get('idText')
    item = calendarTable.objects.filter(id=id)
    item.update(isDelete="1")
    
    return JsonResponse({'':''})


@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def McalendarAdd(request):
    return render(request, "adminapps/McalendarAdd.html")

# 課表新增資料
# 若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Mcalendar_Add(request):
    # 定義post變數
    titleText = request.POST.get('titleText')
    startText = request.POST.get('startText')
    endText = request.POST.get('endText')
    contentText = request.POST.get('contentText')
    alldayText = request.POST.get('alldayText')
    colorText = request.POST.get('colorText')
    group = request.POST.get('group')
    id = calendarTable.objects.order_by('-id')[0].id
    url = r"/McalendarDelete/"+str(int(id)+1)
    urlForStu = r"/calendarContent/"+str(int(id)+1)

    data = calendarTable(
        title =titleText, 
        start =startText,
        end = endText,
        content = contentText,
        allDay = alldayText,
        backgroundColor = colorText,
        borderColor = colorText,
        url = url,
        urlForStu = urlForStu,
        group = group
    )
    data.save()
    return JsonResponse({'': ''})

# 課表內容頁面
@login_required(login_url='/')
def calendarContent(request,id):
    content = {"id":id}
    return render(request, 'adminapps/calendarContent.html',content)

#打卡主頁面
@login_required(login_url='/')
def clockin(request):
    return render(request, "adminapps/clockin.html")

#打卡新增請假頁面
@login_required(login_url='/')
def clockinLeaveAdd(request):
    return render(request, "adminapps/clockinLeaveAdd.html")

#打卡個人出勤頁面
@login_required(login_url='/')
def clockinAttendance(request):
    return render(request, "adminapps/clockinAttendance.html")

#打卡個人請假頁面
@login_required(login_url='/')
def clockinLeave(request):
    return render(request, "adminapps/clockinLeave.html")

#打卡管理頁面
@login_required(login_url='/')
def backstageClock(request):
    return render(request, "adminapps/backstageClock.html")

# 打卡管理出席頁面
# 若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def MclockinAttendanceDel(request):
    return render(request, "adminapps/MclockinAttendanceDel.html")

# 打卡管理請假頁面
# 若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def MclockinLeaveDel(request):
    return render(request, "adminapps/MclockinLeaveDel.html")

@login_required(login_url='/')
def clockin_chickin(request):
    inget = request.POST.get('in')
    timenow = datetime.datetime.today()
    today = timenow.strftime("20%y-%m-%d")
    user = request.user
    groupObject = groupAccountTable.objects.filter(isDelete="0",account = user)
    group = groupObject[0].group
    list1 = clockinTable.objects.all()
    print(list1)
    # list2 = []
    # for item in list1:
    #     # 取得資料欄位
    #     list2.append([item.today])
    
    # print(today)
    # print(request.user)
    # print(request.user.id)
    # print(list2)
    return JsonResponse({'': ''})

# 帳號管理頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def backstageAccount(request):
    return render(request, "adminapps/backstageAccount.html")

# 新增帳號
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Maccount_Add(request):
    name = request.POST.get('name')
    account = request.POST.get('account')
    password = request.POST.get('password')
    group = request.POST.get('group')
    user = User.objects.create_user(
        username=account,
        password=password)
    data = groupAccountTable(
        name = name,
        account = account,
        group = group,
        date = datetime.datetime.now()
    )
    save = data.save()
    # 為該學員新增打卡欄位
    for i in range(200):
        today = datetime.date.today()+datetime.timedelta(days=i+1)
        clockindata = clockinTable(
            name = name,
            group = group,
            today = today
        )
        clockindata.save()
    return JsonResponse({'': ''})

@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Maccount_main(request):
    list1 = groupAccountTable.objects.filter(isDelete="0").order_by('-id')
    list2 = []
    for item in list1:
        # 取得資料欄位
        list2.append([item.account,item.name,item.group ,item.date,item.account,item.id])
    return JsonResponse({'data': list2})

# 分群管理頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def backstageGroup(request):
    return render(request, "adminapps/backstageGroup.html")


# 新增群組
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Mgroup_Add(request):
    groupName = request.POST.get('groupName')
    groupCode = request.POST.get('groupCode')
    data = groupTable(
        groupCode=groupCode,
        name=groupName,
    )
    data.save()
    #insert card two row (one for title)
    cardData1 = announceCard(
        card1 = "姓名",
        card2 = "開課日期",
        card3 = "結訓時間",
        card4 = "倒數天數",
        card5 = "已完成訓練",
        card6 = "遲到次數",
        card7 = "曠課次數",
        card8 = "課程完成率",
        group = groupName,
    )
    cardData1.save()

    cardData2 = announceCard(
        card1 = "",
        card2 = "",
        card3 = "",
        card4 = "",
        card5 = "",
        card6 = "",
        card7 = "",
        card8 = "",
        group = groupName,
    )
    cardData2.save()

    return JsonResponse({'':''})


@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Mgroup_main(request):
    list1 = groupTable.objects.filter(isDelete="0").order_by('-id')
    list2 = []
    for item in list1:
        # 取得資料欄位
        list2.append([item.groupCode,item.name,item.id])
    return JsonResponse({'data': list2})

@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def MgroupDelete(request,id):
    content = {'id':id} 
    return render(request, "adminapps/MgroupDelete.html",content)

# 群組新增
# 若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Mgroup_Update(request):
    # 定義post變數
    groupCode = request.POST.get('groupCode')
    groupName = request.POST.get('groupName')
    id = request.POST.get('idText')
    # 更新資料
    item = groupTable.objects.filter(id=id)
    item.update(groupCode=groupCode)
    item.update(name=groupName)    
    return JsonResponse({'': ''})

# 群組刪除
# 若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Mgroup_Delete(request):
    id = request.POST.get('idText')
    item = groupTable.objects.filter(id=id)
    item.update(isDelete="1")
    # item.id,item.sort,item.title ,item.date,item.pageview,item.content
    return JsonResponse({'':''})

@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def MaccountDelete(request,id):
    content = {'id':id} 
    return render(request, "adminapps/MaccountDelete.html",content)

# 個人帳號修改
#若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Maccount_Update(request):
    nameText = request.POST.get('nameText')
    password = request.POST.get('passwordText')
    group = request.POST.get('group')
    accountText = request.POST.get('accountText')
    id = request.POST.get('idText')
    item = groupAccountTable.objects.filter(id=id)
    item.update(group=group)
    item.update(name=nameText)
    if password != '':
        u = User.objects.get(username=accountText)
        u.set_password(password)
        u.save()
    return JsonResponse({'':''})


# 個人帳號刪除
#若不是superuser則重新導向進入公告頁面
@user_passes_test(lambda u: u.is_superuser ,login_url='/announce')
def Maccount_Delete(request):
    id = request.POST.get('idText')
    item = groupAccountTable.objects.filter(id=id)
    item.update(isDelete="1")
    return JsonResponse({'':''})

# user 使用者區分群組
# user = request.user
# groupObject = groupAccountTable.objects.filter(isDelete="0",account = user)
# group = groupObject[0].group
# list1 = announceTable.objects.filter(isDelete="0" , group = group).order_by('-id')
