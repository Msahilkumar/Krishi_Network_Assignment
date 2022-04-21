from datetime import datetime 


def timeStamp(output):
    for post in output :
        year =  int(post['created_at'][0:4:1])
        month = int(post['created_at'][5:7:1])
        day =   int(post['created_at'][8:10:1])
        hour =  int(post['created_at'][11:13:1])
        minute =int(post['created_at'][14:16:1])
        timdel=datetime.now()-datetime(year,month,day,hour,minute)
        print(timdel)
        print(timdel.days,timdel.seconds)
        timestamp = ''
        if timdel.days > 30:
            if timdel.days//30==1:
                timestamp+='1 month'
            else :
                timestamp+= f'{timdel.days//30} months'
        elif timdel.days > 1:
            timestamp+=f'{timdel.days} days'
        elif timdel.days==1:
            timestamp+='1 day'
        elif timdel.days==0:
            if timdel.seconds//3600 ==0:
                if timdel.seconds//60 > 1:
                    timestamp+=f'{timdel.seconds//60} minutes'
                else :
                     timestamp+='1 minute'
            elif timdel.seconds//3600 ==1:
                timestamp+='1 hour'
            else :
                timestamp+=f'{timdel.seconds//3600} hours'
        post['timestamp'] = timestamp+' ago'
    return output