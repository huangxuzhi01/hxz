import requests
import json
import MySQLdb
from qmapp.config import database1,sqls1
from qmapp.idcard import get_id_card, get_bankcard, cur_time
from qmapp.photo import font, back, auth, hand
import time

headers1 = {
        "appKey":"QmWallet",
        "channel":"360PT",
        "device":"android",
        "deviceNo":"864553037531939",
        'Content-Type': 'application/json;charset=UTF-8'}

def checkUserExists(mobile,qm_env):
    #输入注册手机号，点击下一步#
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/user/checkUserExists".format(URL)
    data = {"mobile":mobile}
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers1)
    print("checkUserExists" + resp.text)

def getValidateCode(mobile,qm_env):
    #获取验证码#
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/user/getValidateCode".format(URL)
    data = {"type":"1","mobile":mobile}
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers1)
    print("getValidateCode" + resp.text)

def checkVerifyCode(mobile,qm_env):
    #输入完验证码#
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/user/checkVerifyCode".format(URL)
    data = {"mobile":mobile,"verifyCode":"000000"}
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers1)
    print("checkVerifyCode" + resp.text)

def register_contract(qm_env):
    #进入设置密码页#
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/contract/register".format(URL)
    resp = requests.get(url=url, headers=headers1)
    print("contract/register" + resp.text)

def register(mobile,qm_env):
    #设置密码，点击完成注册#
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/user/register".format(URL)
    data = {"registrationId":"100d8559093950df9c6","channelCode":"360PT","password":"111111","mobile":mobile}
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers1)
    print("register" + resp.text)

def login(mobile,qm_env):
    #输入登录密码，点击下一步#
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/user/login".format(URL)
    data = {"loginIp":"","loginDevice":"","password":"111111","mobile":mobile,"loginArea":""}
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers1)
    print("login" + resp.text)
    resp_json = resp.json()
    sessionid = resp_json.get('data')['sessionId']
    print("sessionid ={0}".format(sessionid))
    return sessionid


def analisis(sessionid,qm_env):
    #点击手机授权#
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/api/qmwallet/analisis".format(URL)
    data = {
        "imei":"864553037531939",
        "bizCode":"1014",#手机授权为1014
        "module":"auth"}
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("analisis" + resp.text)


def locatingInfo(sessionid,qm_env):
    #点击手机授权后，获取手机定位信息#
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/user/locatingInfo".format(URL)
    data = {
        "detailedAddress":"",
        "province":"",
        "longitudeAndLatitude":"113.33058097688816,23.11644206741667"
    }

    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("locatingInfo" + resp.text)

def deviceInfo(sessionid,qm_env):
    #点击手机授权后，获取手机设备信息#
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/user/deviceInfo".format(URL)
    data = {
        "sysVersion":"7.1.1",
        "appVersion":"2.3.1.1",
        "phoneType":"OPPO R11",
        "deviceNo":"864553037531939",
        "deviceType":1,
        "isSimCard":0,
        "isSimulator":0,
        "uaAddress":"Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
        "deviceBrand":"OPPO",
        "appList":[
            "备份与恢复","TelemetryJService","com.android.cts.priv.ctsshim","OPPO日志转储器","SampleExtAuthService","Perfdump","CTAutoRegist",
            "号码归属地","com.oppo.oppopowermonitor","电话/短信存储","无线设置","日历存储","媒体存储","FreeFallingMonitor","com.qti.service.colorservice",
            "爱奇艺","com.oppo.helper","WifiRxSensTest","MBN 测试","com.qualcomm.shutdownlistner","com.android.wallpapercropper",
            "com.quicinc.cne.CNEService.CNEServiceApp","美团","游戏加速","优酷视频","com.qualcomm.qti.smcinvokepkgmgr","SmartcardService",
            "com.nearme.sync.App","文件","双卡与移动网络","搜狗输入法OPPO版","外部存储设备","HTML 查看程序","SVI Settings","HealthAuthService",
            "常见问题检测","天气服务","信息服务","下载管理服务","SampleAuthenticatorService","下载管理","联系人黑名单","联系人黑名单存储",
            "MultimediaLocalService","com.qualcomm.qti.telephonyservice","浏览器","搜索应用程序提供商","FidoCryptoService","WifiBackupRestore",
            "蓝牙导入联系人","软件包权限帮助程序","PacProcessor","Content Adaptive Backlight Settings","OPPO 互传","手势体感","微信",
            "com.android.vendors.bridge.softsim","凭证安装","com.android.carrierconfig","org.codeaurora.bluetooth",
            "com.qti.qualcomm.datastatusnotification","开机注册","Android 系统","华为移动服务","电话本","Wfd Service","智能识别陌生号码","电池","信息",
            "MTP 主机","SIM 卡应用程序","com.android.backupconfirm","Dirac控制台","DropboxChmodService","合众e贷财富","立借","DLNA 服务","电子保卡",
            "org.codeaurora.ims","Intent Filter Verification Service","com.nearme.deamon","日历","SecureExtAuthService","com.qualcomm.qcrilmsgtunnel",
            "设置存储","com.android.sharedstoragebackup","打印处理服务","通知管理","录屏大师","电话","主题商店","com.android.frameworks.telresources",
            "FingerprintSensorTest","OppoDiracService","DeliverServer","输入设备","SecureSampleAuthService","com.qualcomm.qti.StatsPollManager",
            "com.qti.dpmserviceapp","Shelper","X-Divert设置","ColorOS 系统","BackupRestoreRemoteService","系统桌面","OppoARService","RadioInfo",
            "防误触模式","Android System WebView","近期任务","壁纸","系统消息","系统升级服务","Android Shared Library","文件加密","电话管理","百变引擎",
            "游戏加速SDK","密钥链","上滑解锁","USB 调试","用户体验计划","Android Services Library","Call Log Backup/Restore","QQ","应用包安装程序",
            "ResMonitor","锁屏杂志","org.codeaurora.btmultisim","com.coloros.findmyphone.utils","Pico TTS","ANT HAL Service","ProxyHandler",
            "时钟（插件）","手电筒","ExSupport","图片特效","工作资料设置","软件更新","相机","帮助与反馈","喜马拉雅","时钟","百度地图","com.android.smspush",
            "Cheetah Mobile CleanMaster SDK","动态壁纸选择器","好易借","Log工具","软件商店","支付保护","去哪儿旅行","网络位置","查找手机服务",
            "CriticalLogService","融360","WLAN 安全检测","存储空间管理器","设置","com.qualcomm.qti.ims","锁屏通知","工程模式","RfTest","安全支付",
            "手势体感服务","长截屏","BTtestmode","LocationServices","音乐","com.android.cts.ctsshim","钉钉","云服务","视频（播放器）",
            "com.qualcomm.qti.tetherservice","文件管理","MdtpService","我的 OPPO","VpnDialogs","应用分身","快应用","录音","微博","语音助手",
            "电话服务","Shell","com.android.wallpaperbackup","存储已屏蔽的号码","用户字典","搜索","SecCamService","ColorEyeProtect",
            "一体化位置信息","语音服务","系统界面","File Info","Bluetooth MIDI Service","OppoTZUpdate","使用说明","更新服务","FidoSuiService",
            "儿童空间","手机淘宝","com.qualcomm.qti.biometrics.voiceprint.service","RfToolkit","OppoGestureService","相册","蓝牙共享",
            "com.qualcomm.timeservice","com.qualcomm.atfwd","com.qualcomm.embms","联系人存储","常驻进程管理","CaptivePortalLogin","手机管家权限管理",
            "WPS Office","唯品会","自动清理","com.qti.editnumber"],
        "ipAddress":"192.168.110.216"}

    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("deviceInfo" + resp.text)

def saveLocalInfo1(sessionid,qm_env):
    #点击手机授权后，获取手机设备信息保存本地#
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/user/saveLocalInfo".format(URL)
    data = {
        "message":"[]",
        "infoType":1
    }
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("saveLocalInfo1" + resp.text)

def saveLocalInfo2(sessionid,qm_env):
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/user/saveLocalInfo".format(URL)
    data = {
        "message":"[]",
        "infoType":2
    }
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("saveLocalInfo2" + resp.text)

#实名认证拍身份证正反两面
def font_realNameAuth(sessionid,qm_env):
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/amount/realNameAuth".format(URL)
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    data1 = json.dumps(font)
    data2 = json.dumps(back)
    resp1 = requests.post(url=url, data=data1, headers=headers2)
    print("font_realNameAuth" + resp1.text)
    resp2 = requests.post(url=url, data=data2, headers=headers2)
    print("back_realNameAuth" + resp2.text)


#保存身份证信息
def saveRealNameAuth(id_card,sessionid,qm_env):
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/amount/saveRealNameAuth".format(URL)
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }

    data = {
        "idCardAddress":"安徽省合肥市蜀山区望江西路203号金色名郡14幢404室",
        "idNumber":id_card,
        "realName":"朱亚磊",
        "authCode":1001
    }
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("saveRealNameAuth" + resp.text)

#人脸识别
def faceIdAuth(sessionid,qm_env):
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/amount/faceIdAuth".format(URL)
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    data = json.dumps(auth)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("faceIdAuth" + resp.text)

#手持身份证照片
def handIdCard(sessionid,qm_env):
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/amount/handIdCard".format(URL)
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    data = json.dumps(hand)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("handIdCard" + resp.text)

#同步通讯录信息
def addressBookAuth(sessionid,qm_env):
    URL = database1[qm_env][0]['url']
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    url = "http://{0}.hzed.net/fqy-app/amount/addressBookAuth".format(URL)
    data = {
        "authItemCode":"1004",
        "addressBookInfos":"[{\"name\":\"哥哥\",\"phone\":\"15352523652\"}]"
    }
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("addressBookAuth" + resp.text)

#基本信息认证
def baseInfoAuth(sessionid,qm_env):
    URL = database1[qm_env][0]['url']
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    url = "http://{0}.hzed.net/fqy-app/amount/baseInfoAuth".format(URL)
    data = {
        "authId":"1073029863318200003",
        "baseInfos":[
            {"selectId":"1077492101478461450","optionValue":"哥哥"},
            {"selectId":"1077492101478461452","optionValue":"15352523652"},
            {"selectId":"1077492101478461451","optionValue":"6"},
            {"selectId":"1077495311769382914","optionValue":"3"},
            {"selectId":"1077896851613106177","optionValue":"诸葛亮打野吧"},
            {"selectId":"1077492101478461443","optionValue":"440000,440100,440103"},
            {"selectId":"1077492101478461445","optionValue":"珠江新城啊啊啊"},
            {"selectId":"1077492616031481858","optionValue":"4"},
            {"selectId":"1077492101478461449","optionValue":"123455222@163.com"},
            {"selectId":"1151036255723659265","optionValue":"3"},
            {"selectId":"1077492101461684225","optionValue":"5"},
            {"selectId":"1077896851613106178","optionValue":"0"},
            {"selectId":"1127771585674571777","optionValue":"440000,440100,440103"},
            {"selectId":"1127771585716514817","optionValue":"今天天气不错不错"},
            {"selectId":"1077492101478461442","optionValue":"6"},
            {"selectId":"1127771585745874945","optionValue":"2"}]}

    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("baseInfoAuth" + resp.text)

#评估成功
def amountAssessment(sessionid,qm_env):
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/amount/amountAssessment".format(URL)
    data = {
    }
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("amountAssessment" + resp.text)

#获取风控分并检查用户
def genRiskScoreAndCheckUser(sessionid,qm_env):
    headers2 = {
        "appKey": "QmWallet",
        "channel": "360PT",
        "device": "android",
        "deviceNo": "864553037531939",
        "sessionId": sessionid,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/user/genRiskScoreAndCheckUser".format(URL)
    data = {
    }

    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("genRiskScoreAndCheckUser" + resp.text)

#更新渠道库 t_user 和 t_loan_apply 表数据
def update_chanel(mobile, chanel_env):
    datas = database1[chanel_env][0]
    db = MySQLdb.connect(datas['chanel_db_url'], datas['chanel_db_uname'], datas['chanel_db_pwd'], datas['chanel_db_name'], charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sqls1['更新渠道user表用户类型'].format(mobile=mobile))
        cursor.execute(sqls1['更新渠道t_loan_apply表'].format(mobile=mobile,Time=cur_time()))
        db.commit()
    except Exception as e:
        db.rollback()
    cursor.close()
    db.close()

#更新全民库订单表
def update_qm(mobile, qm_env,status):
    datas = database1[qm_env][0]
    db = MySQLdb.connect(datas['qm_db_url'], datas['qm_db_uname'], datas['qm_db_pwd'], datas['qm_db_name'], charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sqls1['查询用户信息'].format(mobile=mobile))
        user_Id = cursor.fetchone()[0]
        cursor.execute(sqls1['更新全民库订单表'].format(userid=user_Id, Time=cur_time(), status=status,))
    except Exception as e:
        db.rollback()
    cursor.close()
    db.commit()
    db.close()

#获取用户id 和 订单号
def get_user_message1(mobile,qm_env):
    msg=[]
    datas = database1[qm_env][0]
    db = MySQLdb.connect(datas['qm_db_url'], datas['qm_db_uname'], datas['qm_db_pwd'], datas['qm_db_name'], charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sqls1['查询用户信息'].format(mobile=mobile))
        user_Id = cursor.fetchone()[0]
        msg.append(user_Id)
        cursor.execute(sqls1['查询全民订单号'].format(userid=user_Id))
        order_no = cursor.fetchone()[0]
        msg.append(order_no)
    except Exception as e:
        db.rollback()
    cursor.close()
    db.commit()
    db.close()
    return msg


#绑定银行卡
def bindCard(mobile,sessionid,id_card,bank_card,qm_env):
    global order_no
    datas = database1[qm_env][0]
    db = MySQLdb.connect(datas['qm_db_url'], datas['qm_db_uname'], datas['qm_db_pwd'], datas['qm_db_name'], charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sqls1['查询用户信息'].format(mobile=mobile))
        user_Id = cursor.fetchone()[0]
        cursor.execute(sqls1['查询全民订单号'].format(userid=user_Id))
        order_no = cursor.fetchone()[0]

    except Exception as e:
        db.rollback()
    db.commit()
    cursor.close()
    db.close()

    headers2 = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
        "sessionId": sessionid
    }
    URL = database1[qm_env][0]['url']
    url1 = "http://{0}.hzed.net/fqy-app/order/bindCardValidateCode".format(URL)
    #url1 ="http://t01.hzed.com:133/fqy-app/order/bindCardValidateCode"
    data1 = {
        "cardId": "",
        "realName": "朱亚磊",
        "idNumber": id_card,
        "cardNo": bank_card,
        "mobile": mobile,
        "cardCode": "ICBC",
        "smsCode": "",
        "cardNameArr": [],
        "needCheck": 1,
        "cardName": "中国工商银行",
        "orderNo": order_no
    }
    data1 = json.dumps(data1)
    resp = requests.post(url=url1, data=data1, headers=headers2)
    print("bindCardValidateCode" + resp.text)


    url = "http://{0}.hzed.net/fqy-app/order/bindCard".format(URL)
    data = {
        "cardId":"",
        "realName":"朱亚磊",
        "idNumber":id_card,
        "cardNo":bank_card,
        "mobile":mobile,
        "cardCode":"ICBC",
        "smsCode":"111111",
        "cardNameArr":[],
        "needCheck":1,
        "cardName":"中国工商银行",
        "orderNo":order_no,
        "bindCardType":1}
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("bindCard" + resp.text)


#确认借款
def confirmLoan(sessionid,bank_card,qm_env,period):
    global order_no
    datas = database1[qm_env][0]
    db = MySQLdb.connect(datas['qm_db_url'], datas['qm_db_uname'], datas['qm_db_pwd'], datas['qm_db_name'], charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sqls1['查询用户信息'].format(mobile=mobile))
        user_Id = cursor.fetchone()[0]
        cursor.execute(sqls1['查询全民订单号'].format(userid=user_Id))
        order_no = cursor.fetchone()[0]
    except Exception as e:
        db.rollback()
    db.commit()
    cursor.close()
    db.close()

    headers2 = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
        "sessionId": sessionid
    }
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/order/confirmLoan".format(URL)
    data = {
        "cardNo":bank_card[-4:],
        "orderNo":order_no,
        "periods":period
    }
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("confirmLoan" + resp.text)

#分期购物
def confirmLoan(sessionid,bank_card,qm_env,period):
    global order_no
    datas = database1[qm_env][0]
    db = MySQLdb.connect(datas['qm_db_url'], datas['qm_db_uname'], datas['qm_db_pwd'], datas['qm_db_name'], charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sqls1['查询用户信息'].format(mobile=mobile))
        user_Id = cursor.fetchone()[0]
        cursor.execute(sqls1['查询全民订单号'].format(userid=user_Id))
        order_no = cursor.fetchone()[0]
    except Exception as e:
        db.rollback()
    db.commit()
    cursor.close()
    db.close()

    headers2 = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
        "sessionId": sessionid
    }
    URL = database1[qm_env][0]['url']
    url = "http://{0}.hzed.net/fqy-app/order/confirmLoan".format(URL)
    data = {
        "cardNo":bank_card[-4:],
        "orderNo":order_no,
        "periods":period
    }
    data = json.dumps(data)
    resp = requests.post(url=url, data=data, headers=headers2)
    print("confirmLoan" + resp.text)


def fenqiyi_210(id_card,mobile,chanel_env,qm_env,status):
    checkUserExists(mobile,qm_env)
    getValidateCode(mobile,qm_env)
    checkVerifyCode(mobile,qm_env)
    register_contract(qm_env)
    register(mobile,qm_env)
    sessionid = login(mobile,qm_env)
    analisis(sessionid,qm_env)
    locatingInfo(sessionid,qm_env)
    saveLocalInfo1(sessionid,qm_env)
    deviceInfo(sessionid,qm_env)
    saveLocalInfo2(sessionid,qm_env)
    font_realNameAuth(sessionid,qm_env)
    saveRealNameAuth(id_card, sessionid,qm_env)
    faceIdAuth(sessionid,qm_env)
    # handIdCard(sessionid,qm_env)
    addressBookAuth(sessionid,qm_env)
    baseInfoAuth(sessionid,qm_env)
    amountAssessment(sessionid,qm_env)
    genRiskScoreAndCheckUser(sessionid,qm_env)
    #update_chanel(mobile,chanel_env)
    # update_qm(mobile,qm_env,status)
def fenqiyi_200(id_card,mobile,bank_card,chanel_env,qm_env,status):
    checkUserExists(mobile,qm_env)
    getValidateCode(mobile,qm_env)
    checkVerifyCode(mobile,qm_env)
    register_contract(qm_env)
    register(mobile,qm_env)
    sessionid = login(mobile,qm_env)
    analisis(sessionid,qm_env)
    locatingInfo(sessionid,qm_env)
    saveLocalInfo1(sessionid,qm_env)
    deviceInfo(sessionid,qm_env)
    saveLocalInfo2(sessionid,qm_env)
    font_realNameAuth(sessionid,qm_env)
    saveRealNameAuth(id_card, sessionid,qm_env)
    faceIdAuth(sessionid,qm_env)
    # handIdCard(sessionid,qm_env)
    addressBookAuth(sessionid,qm_env)
    baseInfoAuth(sessionid,qm_env)
    amountAssessment(sessionid,qm_env)
    genRiskScoreAndCheckUser(sessionid,qm_env)
    time.sleep(3)
    bindCard(mobile, sessionid, id_card, bank_card, qm_env)

def fenqiyi_201(id_card,mobile,bank_card,chanel_env,qm_env,status):
    checkUserExists(mobile,qm_env)
    getValidateCode(mobile,qm_env)
    checkVerifyCode(mobile,qm_env)
    register_contract(qm_env)
    register(mobile,qm_env)
    sessionid = login(mobile,qm_env)
    analisis(sessionid,qm_env)
    locatingInfo(sessionid,qm_env)
    saveLocalInfo1(sessionid,qm_env)
    deviceInfo(sessionid,qm_env)
    saveLocalInfo2(sessionid,qm_env)
    font_realNameAuth(sessionid,qm_env)
    saveRealNameAuth(id_card, sessionid,qm_env)
    faceIdAuth(sessionid,qm_env)
    # handIdCard(sessionid,qm_env)
    addressBookAuth(sessionid,qm_env)
    baseInfoAuth(sessionid,qm_env)
    amountAssessment(sessionid,qm_env)
    genRiskScoreAndCheckUser(sessionid,qm_env)
    time.sleep(3)
    bindCard(mobile, sessionid, id_card, bank_card, qm_env)
    update_chanel(mobile, chanel_env)
    update_qm(mobile, qm_env, status)

def fenqiyi_220(id_card,mobile,bank_card,chanel_env,qm_env,status):
    checkUserExists(mobile,qm_env)
    getValidateCode(mobile,qm_env)
    checkVerifyCode(mobile,qm_env)
    register_contract(qm_env)
    register(mobile,qm_env)
    sessionid = login(mobile,qm_env)
    analisis(sessionid,qm_env)
    locatingInfo(sessionid,qm_env)
    saveLocalInfo1(sessionid,qm_env)
    deviceInfo(sessionid,qm_env)
    saveLocalInfo2(sessionid,qm_env)
    font_realNameAuth(sessionid,qm_env)
    saveRealNameAuth(id_card, sessionid,qm_env)
    faceIdAuth(sessionid,qm_env)
    # handIdCard(sessionid,qm_env)
    addressBookAuth(sessionid,qm_env)
    baseInfoAuth(sessionid,qm_env)
    amountAssessment(sessionid,qm_env)
    genRiskScoreAndCheckUser(sessionid,qm_env)
    time.sleep(3)
    bindCard(mobile, sessionid, id_card, bank_card, qm_env)
    update_chanel(mobile, chanel_env)
    update_qm(mobile, qm_env, status)


def fenqiyi_300(id_card,mobile,bank_card,chanel_env,qm_env,status,period):
    checkUserExists(mobile, qm_env)
    getValidateCode(mobile, qm_env)
    checkVerifyCode(mobile, qm_env)
    register_contract(qm_env)
    register(mobile, qm_env)
    sessionid = login(mobile, qm_env)
    analisis(sessionid, qm_env)
    locatingInfo(sessionid, qm_env)
    saveLocalInfo1(sessionid, qm_env)
    deviceInfo(sessionid, qm_env)
    saveLocalInfo2(sessionid, qm_env)
    font_realNameAuth(sessionid, qm_env)
    saveRealNameAuth(id_card, sessionid, qm_env)
    faceIdAuth(sessionid, qm_env)
    handIdCard(sessionid, qm_env)
    addressBookAuth(sessionid, qm_env)
    baseInfoAuth(sessionid, qm_env)
    amountAssessment(sessionid, qm_env)
    genRiskScoreAndCheckUser(sessionid, qm_env)
    time.sleep(3)
    update_chanel(mobile, chanel_env)
    update_qm(mobile, qm_env, status)
    bindCard(mobile, sessionid, id_card, bank_card, qm_env)
    confirmLoan(sessionid, bank_card, qm_env, period)


if __name__ == '__main__':
    mobile = 13934239990
    id_card = get_id_card()
    bank_card =get_bankcard()
    chanel_env="chanel_B"
    qm_env = "C"
    period = '3'
    status='210'
    fenqiyi_220(id_card, mobile, bank_card, chanel_env, qm_env, status)

