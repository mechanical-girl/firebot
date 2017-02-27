import karelia, time, math

def update():
    global score
    global lastUpdateTime
    if time.time() - lastUpdateTime > 15:
        score *= 0.75
        lastUpdateTime = time.time()
        score = round(score, 2)


longestStreak = 1560
karelia.botName = 'embers'
karelia.shortHelp = "/me monitors activity levels in the room"
karelia.helpMessage = ["/me monitors activity levels in the room. Made by @PouncySilverkitten"]

karelia.shortHelp = ''
karelia.helpMessage = []

room = input('Room: &')
print("Connecting...")
conn = karelia.connectTo(room)
print("Connected.")
currentStreakStart = time.time()

lastScore = 0
score = 0
lastUpdateTime = time.time()

newNick = karelia.botName
nick = newNick

while True:
    update()
    
    if score > 20:
        newNick = ':fire::fire::fire::fire:'
    if score > 10:
        newNick = ':fire::fire::fire:'
    elif score > 5:
        newNick = ':fire::fire:'
    elif score >= 1:
        newNick = ':fire:'
    else:
        newNick = 'embers'
        currentStreak = time.time() - currentStreakStart
        if currentStreak > longestStreak:
            karelia.send("Congratulations, a new record was set at {0}m {1}s of flame!".format(math.floor(currentStreak/60),round((currentStreak%60))))
            longestStreak = currentStreak
        currentStreakStart = time.time()
        
    
    lastScore = score
        
    if newNick != nick: karelia.changeNick(newNick)
    nick = newNick
    
    try:
        message = karelia.parse(False)
        if message['type'] == 'send-event' and not 'bot' in message['data']['sender']['id']:
            if message['data']['content'] == "/me stokes the embers":
                karelia.send("/me are glowing",message['data']['id'])
                score += 1
            score += 1
                
        
    except:
        print("Error: will disconnect and reconnect")
        try: karelia.disconnect(conn)
        except: print("  And everything's on fire!")
            
        time.sleep(10)
        
        print("Connecting...")
        conn = karelia.connectTo(room)
        print("Connected.")
