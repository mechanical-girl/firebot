<<<<<<< HEAD
import karelia, time

def update():
    global score
    global lastUpdateTime
    if time.time() - lastUpdateTime > 15:
        score *= 0.9
            
        lastUpdateTime = time.time()
        
karelia.botName = 'embers'

karelia.shortHelp = ''
karelia.helpMessage = []

room = 'xkcd'
print("Connecting...")
conn = karelia.connectTo(room)
print("Connected.")

score = 0
lastUpdateTime = time.time()

newNick = karelia.botName

while True:
    try:
        message = karelia.parse()
        print("packet received...")
        print(message['type'])
        if message['type'] == 'send-event' and not 'bot' in message['data']['sender']['id']:
            print("packet is message...")
            score += 1
            if score > 10:
                newNick = ':fire::fire::fire::fire:'
            if score > 10:
                newNick = ':fire::fire::fire:'
            elif score > 5:
                newNick = ':fire::fire:'
            elif score > 1:
                newNick = ':fire:'
            else:
                newNick = 'embers'
                
        if newNick is not karelia.botName:
            karelia.botName = newNick
            karelia.changeNick()
        else:
            time.sleep(1)
            
        update()

        
    except:
        print("Error: will disconnect and reconnect")
        try:
            karelia.disconnect(conn)
        except:
            print("  And everything's on fire!")
            
        time.sleep(10)
        
        print("Connecting...")
        conn = karelia.connectTo(room)
        print("Connected.")
=======
import karelia, time

def update():
    global score
    global lastUpdateTime
    if time.time() - lastUpdateTime > 15:
        score *= 0.9
            
        lastUpdateTime = time.time()
        
karelia.botName = 'embers'

karelia.shortHelp = ''
karelia.helpMessage = []

room = 'xkcd'
print("Connecting...")
conn = karelia.connectTo(room)
print("Connected.")

score = 0
lastUpdateTime = time.time()

while True:
    try:
        message = karelia.parse()
        
        if message['type'] == 'send-event' and not 'bot' in message['data']['sender']['id']:
            #print(message)
            score += 1
            if score > 10:
                newNick = ':fire::fire::fire::fire:'
            if score > 10:
                newNick = ':fire::fire::fire:'
            elif score > 5:
                newNick = ':fire::fire:'
            elif score > 1:
                newNick = ':fire:'
        else:
            newNick = 'embers'
            
        if newNick is not karelia.botName:
            karelia.botName = newNick
            karelia.changeNick()
        else:
            time.sleep(1)
            
        update()

        
    except:
        print("Error: will disconnect and reconnect")
        try:
            karelia.disconnect(conn)
        except:
            print("  And everything's on fire!")
            
        time.sleep(10)
        
        print("Connecting...")
        conn = karelia.connectTo(room)
        print("Connected.")
>>>>>>> c09ab532953fcf1c37885cb9955cb7a896c15741
