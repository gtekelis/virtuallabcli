from Modules import Sunny_Web_Box2

def matSetQmode(field3):
    pw="A0079#aCg90D1f@8"
    swb = Sunny_Web_Box2.SunnyWebBoxHTTP("147.102.30.65", password=pw)
    keySB3000 = "WRTM0U88:2130253427"

    #data = -1

    def SetData(value):
        dat=swb.setParameter([{'key':keySB3000, 'channels':value}]);

    if field3 == '0':
        data = 'PFCnst'
        #sendFormValue(data)
    elif field3 == '1':
        data = 'VArCtlVol'
        #sendFormValue(data)

    #data = field3 #"0.85" #sys.argv[1]


    
    #def sendFormValue( data ):
    #    print "Set-point =" ,data
    #    channels1 = [{'meta' : 'Q-VArMod', 'name' : 'Q-VArMod',   'value' : data}]
    #    #channels1 = [{'meta' : 'PF-PF', 'name' : 'PF-PF',   'value' : data}]
    #    SetData(channels1)
    #    #return
          
    print "Set-point =" ,data
    channels1 = [{'meta' : 'Q-VArMod', 'name' : 'Q-VArMod',   'value' : data}]
    #channels1 = [{'meta' : 'PF-PF', 'name' : 'PF-PF',   'value' : data}]
    SetData(channels1)
    #return

    return('MatSetQmode executed successfuly, data sent is: ' + field3)