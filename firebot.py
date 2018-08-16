import karelia
import time
import math
import sys

firebot = karelia.bot(['embers', 'firebot', 'flame'], 'xkcd')
longest_streak = 5100

firebot.stock_responses['short_help'] = "/me monitors activity levels in the room"
firebot.stock_responses['long_help'] = "/me monitors activity levels in the room. Made by @PouncySilverkitten"

streak_start = time.time()

last_score = 0
score = 0
last_update = time.time()

firebot.connect()
firebot.on_kill = sys.exit

while True:
    try:
        while True:
            if firebot.parse().type == 'send-event':
                score += 1

            if time.time() - last_update > 15:
                score *= 0.75
                last_update = time.time()
                score = round(score, 2)

            if score > 20:
                new_nick = ':fire::fire::fire::fire:'
            if score > 10:
                new_nick = ':fire::fire::fire:'
            elif score > 5:
                new_nick = ':fire::fire:'
            elif score >= 1:
                new_nick = ':fire:'
            else:
                new_nick = 'embers'
                current_streak = time.time() - streak_start
                
            if new_nick != firebot.names[0]: firebot.change_nick(new_nick)

    except:
        firebot.log(logfile = 'firebot.log')
        firebot.disconnect()
    finally:
        time.sleep(1)
        firebot.connect()
