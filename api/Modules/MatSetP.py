from Modules import Sunny_Web_Box2

def matSetP():
    pw="A0079#aCg90D1f@8"
    swb = Sunny_Web_Box2.SunnyWebBoxHTTP("147.102.30.65", password=pw)
    keySB3000 = "WRTM0U88:2130253427"

    def SetData(value):
        dat=swb.setParameter([{'key':keySB3000, 'channels':value}]);

    data = "520" #sys.argv[1]
    #print "Set-point =" ,data

    channels1 = [{'meta' : 'P-W', 'name' : 'P-W',   'value' : data}]
    SetData(channels1)
    return('MatSetP executed successfuly')