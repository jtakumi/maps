import pandas as pd
import urllib.error
import urllib.request
import json,os
from pygeocoder import Geocoder
import googlemaps

googleapikey='key'
output_path = 'C:/Users/Takum/programing/maps/'
pixel = '640x480'
scale='18'

location = ["国会議事堂","沼津","香港","Seattle","Schloss Neuschwanstein"
            ,"big ben","Mont Saint-Michel","東京都庁","Rio de Janeiro","北京"]

loc_dict = []

def loc_csv():
    df=pd.DataFrame(data=loc_dict)
    #delete duplications
    df=df.drop_duplicates('loc')
    fn="./loc_csv/loc_info.csv"
    #export csv
    df.to_csv(fn)

def dl_image():
    loc = pd.read_csv("./loc_csv/loc_info.csv",index_col="Unnamed: 0")
    #convert to list
    lats = loc['lat'].values.tolist()
    lngs = loc['lng'].values.tolist()
    locs = loc['loc'].values.tolist()
    
    #html setting
    html = ["https://maps.googleapis.com/maps/api/staticmap?center=",
     "&maptype=hybrid",
     "&size=",
     "&sensor=false",
     "&zoom=",
     "&markers=",
     "&key="]

    for lt,lg,lc in zip(lats,lngs,locs):

        axis = str(lt) + "," + str(lg)
        #URL setting
        url = html[0] + axis + html[1] + html[2] + pixel + html[3] + html[4] + scale + html[5] + axis + html[6] + googleapikey
        #photo path
        dst_path = output_path + 'loc_photo/' + str(lc) + ".png"
        #if the photo already exist,no use google map api.
        if os.path.exists(dst_path) is True:
            pass
        else:
            try:
                data = urllib.request.urlopen(url).read()
            #url error
            except urllib.error.URLError as e:
                print(e)
            else:
                with open(dst_path,mode="wb") as f:
                    f.write(data)



def main():
    gmaps = googlemaps.Client(key=googleapikey)
    for i in location:
        address =u"" + i
        fname='loc_info/'+ address + '.json'
        #if the json file already exist, no use google map api.
        if os.path.exists(fname) == True:
            pass
        else:
            try:
                result = gmaps.geocode(address)
            except Exception as e:
                print(e)
            else:  
                lat=result[0]["geometry"]["location"]["lat"]
                lng=result[0]["geometry"]["location"]["lng"]
                format_ad=result[0]["formatted_address"]
                loc_dict.append({'loc':i,'lat':lat,'lng':lng,'formatted_address':format_ad})
                with open(fname,'w',encoding='utf-8-sig') as f:
                    print(json.dumps(result,indent=2,ensure_ascii=False),file=f)
    #make a csv file
    loc_csv()
    #download location photos
    dl_image()


if __name__ == "__main__":
    main()