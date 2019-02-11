import time, datetime
import telepot
from telepot.loop import MessageLoop
import subprocess as sub
now = datetime.datetime.now()

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    #myip=(([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)),s.getsockname()[0], s.close())for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]

    print ('Received: %s' % command)

    if command == "/start":
        telegram_bot.sendMessage(chat_id, "r : Full reboot \n k : Kodi reboot ")
    elif command == 'r' or command == 'R':
        telegram_bot.sendMessage (chat_id, str("Dastgha ta 10 saniye digar khamosh roshan mishavad"))
        time.sleep(10)
        sub.call(["./bash_scripts/rpi-rebooter.sh"])
    elif command == 'k' or command == 'K':
        telegram_bot.sendMessage(chat_id, str("kodi  ta 10 saniye digar khamosh roshan mishavad"))
        time.sleep(10)
        sub.call(["./bash_scripts/kodi_rebooter.sh"])

telegram_bot = telepot.Bot('542706718:AAHCqNduhKVtv5QWHXfx0GpiE3A8ILiWppY')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')

while 1:
    time.sleep(10)
