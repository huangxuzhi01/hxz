from django.shortcuts import render
from qmapp.idcard import get_bankcard, get_id_card
from qmapp.wallet import *
from qmapp.fenqiyi import *
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    if request.method == 'POST':
        mobile = request.POST.get('phone', '')
        idNumber = request.POST.get('idcard', '')
        bankCard = request.POST.get('bankcard', '')
        qm_env = request.POST.get('qm_env', '')
        chanel_env = request.POST.get('chanel_env', '')
        period = request.POST.get('period', '')
        status = request.POST.get('status', '')

        print(status)

        if status == '200':
            status_200(idNumber, mobile,bankCard,chanel_env, qm_env, status)
        elif status == '201':
            status_201(idNumber, mobile, bankCard, chanel_env, qm_env, status)
        elif status == '210':
            status_210(idNumber, mobile,chanel_env, qm_env, status)
        elif status == '220':
            status_220(idNumber, mobile, bankCard, chanel_env, qm_env, status)
        else:
            status = '210'
            status_300(
                idNumber,
                mobile,
                bankCard,
                chanel_env,
                qm_env,
                status,
                period)
            status = '300'

        idNumber1 = get_id_card()
        bankCard1 = get_bankcard()
        userid = get_user_message(mobile, qm_env)[0]
        orderno = get_user_message(mobile, qm_env)[1]

        # return HttpResponseRedirect('/index/', {'message':'借款成功!'})
        return render(request,
                      'index.html',
                      {'message': status,
                       'phone': mobile,
                       'idcard': idNumber,
                       'bank': bankCard,
                       'id_number': idNumber1,
                       'bank_card': bankCard1,
                       'userid': userid,
                       'orderno': orderno})
    else:
        idNumber1 = get_id_card()
        bankCard1 = get_bankcard()
        return render(
            request, 'index.html', {
                'id_number': idNumber1, 'bank_card': bankCard1})

def fenqiyi(request):
    if request.method == 'POST':
        mobile = request.POST.get('phone', '')
        idNumber = request.POST.get('idcard', '')
        bankCard = request.POST.get('bankcard', '')
        qm_env = request.POST.get('qm_env', '')
        chanel_env = request.POST.get('chanel_env', '')
        period = request.POST.get('period', '')
        status = request.POST.get('status', '')

        print(status)

        if status == '200':
            fenqiyi_200(idNumber, mobile,bankCard,chanel_env, qm_env, status)
        elif status == '201':
            fenqiyi_201(idNumber, mobile, bankCard, chanel_env, qm_env, status)
        elif status == '210':
            fenqiyi_210(idNumber, mobile,chanel_env, qm_env, status)
        elif status == '220':
            fenqiyi_220(idNumber, mobile, bankCard, chanel_env, qm_env, status)
        else:
            status = '210'
            fenqiyi_300(
                idNumber,
                mobile,
                bankCard,
                chanel_env,
                qm_env,
                status,
                period)
            status = '300'

        idNumber1 = get_id_card()
        bankCard1 = get_bankcard()
        userid = get_user_message1(mobile, qm_env)[0]
        orderno = get_user_message1(mobile, qm_env)[1]

        # return HttpResponseRedirect('/index/', {'message':'借款成功!'})
        return render(request,
                      'fenqiyi.html',
                      {'message': status,
                       'phone': mobile,
                       'idcard': idNumber,
                       'bank': bankCard,
                       'id_number': idNumber1,
                       'bank_card': bankCard1,
                       'userid': userid,
                       'orderno': orderno})
    else:
        idNumber1 = get_id_card()
        bankCard1 = get_bankcard()
        return render(
            request, 'fenqiyi.html', {
                'id_number': idNumber1, 'bank_card': bankCard1})
