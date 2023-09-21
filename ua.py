import os,random,subprocess
#-----------------------color---------------#
B="\033[1;37m" 
#----------------------logo---------------#
logo = (f"""{B}
MSD DARK
--------------------------------------------
 OWNER     :    MASUD
 FACEBOOK  :    MASUD
 VERSION   :    0.0.1
--------------------------------------------{B}""")

fbcr1 = [ 'MTN', 'AWCC', 'Roshan', 'Zong','Jazz','Etisalat']
fbcr = random.choice(fbcr1)
fban1 = [ 'MessengerLite', 'MobileAdsManagerAndroid', 'Orca-Android', 'FB4A', 'FB4A']
fban = random.choice(fban1)
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
fbpn = random.choice(fbks)
sim_id=''
fbsv = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdv = model
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
fbbv = str(random.randint(10000000, 88888888))
ua = f'[FBAN/{fban};FBAV/{fbav};FBBV/{fbbv};[FBAN/{fban};FBAV/{fbav};FBPN/{fbpn};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbbd};FBDV/{fbdv};FBSV/7.1.2;FBCA/{fbca};FBDM/{fbdm};FB_FW/1;] FBBK/1;]' 
print(logo)
print(ua)
