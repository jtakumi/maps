import time
import random,json,datetime

today = datetime.datetime.today()
d= today.strftime("%Y_%m_%d")

while(True):
    print(random.randint(13,200000))
    time.sleep(1)
    """ st=str(t)
    filename="./random_number/random_" + d +"_" + st + ".json"
    with open(filename,"a",encoding='utf-8-sig') as f:
        for i in range(100):
            json.dump(int(random.randint(13,200000)),filename,indent=2,ensure_ascii=False)
            print("No" + i + "written")
      """      
