import karelia, time, math

longestStreak = 5100
karelia.botName = 'embers'
karelia.shortHelp = "/me monitors activity levels in the room"
karelia.helpMessage = ["/me monitors activity levels in the room. Made by @PouncySilverkitten"]

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
    try:

        while True:
            if time.time() - lastUpdateTime > 15:
                score *= 0.75
                lastUpdateTime = time.time()
                score = round(score, 2)
            
                if score > 20:
                    newNick = ':fire::fire::fire::fire:'
                if score > 10:
                    newNick = ':fire::fire::fire:'
                elif score > 5:
                    newNick = ':fire::fire:'
                elif score >= 1:
                    newNick = ':fire:'
                else:
                    newNick = 'embers'
                    currentStreak = time.time() - currentStreakStart
                    if currentStreak > longestStreak:
                        karelia.send("Congratulations, a new record was set at {0}m {1}s of flame!".format(math.floor(currentStreak/60),round((currentStreak%60))))
                        longestStreak = currentStreak
                    currentStreakStart = time.time()
                    
                
                lastScore = score
                
                if newNick != nick: karelia.changeNick(newNick)
                nick = newNick
            
            message = karelia.parse()
            karelia.spoof(message,"embers")
            if message['type'] == 'send-event':# and not 'bot' in message['data']['sender']['id']:
                if message['data']['content'] == "/me stokes the embers":
                    karelia.send("/me are glowing",message['data']['id'])
                    score += 1
                else:
                    print(message['data']['content'])
                score += 1
                if 'inferno' in message['data']['content']:
                    karelia.changeNick(':fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire:')
                    time.sleep(10)
                        
                               
    except KareliaException as e:
        karelia.log(e, message)
    except Exception as e:
        karelia.log(e, message)
        karelia.disconnect(conn)
    finally:
        time.sleep(10)
