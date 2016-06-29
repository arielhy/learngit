import glob,os,sys
import xml.etree.ElementTree as ET
from building_height_check import read_xml,decimal_to_hex_long,decimal_to_hex_lat
#This script is dedicated for map testing.
def GetDistance( lng1,  lat1,  lng2,  lat2):
    EARTH_RADIUS = 6378.137 
    from math import asin,sin,cos,radians,pow,sqrt
    radLat1 = radians(lat1)
    radLat2 = radians(lat2)
    a = radLat1 - radLat2 
    b = radians(lng1) - radians(lng2)
    s = 2 * asin(sqrt(pow(sin(a/2),2) + cos(radLat1)*cos(radLat2)*pow(sin(b/2),2))) 
    s = s * EARTH_RADIUS
#   s = round(s * 10000) / 10000
    d=s*1000
    return d

if __name__ == '__main__':
    version = sys.argv[1]
    os.system('mkdir '+version+'_width')
    path = '/mapsstorage_gfs/earthcore/'+version
    name_space = "{http://www.nokia.com/ec/featureTile/v0-3}"
    country_ls = sys.argv[2]
    for d in os.listdir(path):
        if len(d) == 3 and d in country_ls:
            f = open('./'+version+'_width'+os.path.sep+d+'.txt','w')
            for xf in glob.glob(path+os.path.sep+d+os.path.sep+'*.xml'):
                doc = read_xml(xf)
                for info in doc.iter(name_space+'polyline'):
                    ls1 = []
                    ls2 = []
                    for i in info.findall(name_space+'point'):
                        lon = float(i.attrib['longitude'])
                        lat = float(i.attrib['latitude'])
                        ls1.append(lon)
                        ls2.append(lat)
                    j = 0
                    for j in range(len(ls1)-1):
                        l = GetDistance(ls1[j], ls2[j], ls1[j+1], ls2[j+1])
                        j += 1
                        if l < 3:
                            lo = decimal_to_hex_long(ls1[j])
                            la = decimal_to_hex_lat(ls2[j])
                            f.write(lo+' '+la+' '+'16'+' '+str(l)+'\n')
            f.close()
