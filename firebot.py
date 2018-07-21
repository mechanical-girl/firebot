import karelia, time, math

firebot = karelia.newBot('embers', 'xkcd')
longestStreak = 5100

firebot.stockResponses['shortHelp'] = "/me monitors activity levels in the room"
firebot.stockResponses['longHelp'] = "/me monitors activity levels in the room. Made by @PouncySilverkitten"

currentStreakStart = time.time()

lastScore = 0
score = 0
lastUpdateTime = time.time()

firebot.connect()

while True:
    try:
        while True:
            if firebot.parse()['type'] == 'send-event':
                score += 1
            
            if time.time() - lastUpdateTime > 15:
                score *=0.75
                lastUpdateTime = time.time()
                score = round(score, 2)

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
                        firebot.send("Congratulations, a new record was set at {0}m {1}s of flame!".format(math.floor(currentStreak/60),round(currentStreak%60)))
                        longestStreak = currentStreak
                    currentStreakStart = time.time()
                    
                
                lastScore = score
                
                if newNick != firebot.names[0]: firebot.changeNick(newNick)
                nick = newNick

    except:
        firebot.log('firebot.log')
        firebot.disconnect()
    finally:
        time.sleep(10)
        firebot.connect()
