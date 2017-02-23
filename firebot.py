import karelia, time

def update():
    global score
    global lastUpdateTime
    if time.time() - lastUpdateTime > 15:
        score *= 0.9
        print(score)
        lastUpdateTime = time.time()
        
karelia.botName = 'embers'

karelia.shortHelp = ''
karelia.helpMessage = []

room = input('Room: &')
print("Connecting...")
conn = karelia.connectTo(room)
print("Connected.")

score = 0
lastUpdateTime = time.time()

newNick = karelia.botName

while True:
    try:
        message = karelia.parse()
        if message['type'] == 'send-event' and not 'bot' in message['data']['sender']['id']:
            print(score)
            if message['data']['content'] == "/me stokes the embers":
                karelia.send("/me are glowing",message['data']['id'])
                
            score += 1
            if score > 20:
                newNick = ':fire::fire::fire::fire:'
            if score > 10:
                newNick = ':fire::fire::fire:'
            elif score > 5:
                newNick = ':fire::fire:'
            elif score > 1:
                newNick = ':fire:'
            else:
                newNick = 'embers'
                
        if newNick != karelia.botName: karelia.changeNick(newNick)
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
