import karelia, time

def update():
    global score
    global lastUpdateTime
    if time.time() - lastUpdateTime > 15:
        score *= 0.9
        if score > 10:
            karelia.changeNick(':fire::fire::fire::fire:')
        if score > 10:
            karelia.changeNick(':fire::fire::fire:')
        elif score > 5:
            karelia.changeNick(':fire::fire:')
        elif score > 1:
            karelia.changeNick(':fire:')
        else:
            karelia.changeNick('embers')
            
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
