import telebot
import config
import time
import json

bot = telebot.TeleBot(config.TOKEN)

thour = time.localtime()
corr_time = str(thour[3]) +":"+ str(thour[4])

file_id = dict(photo = [], video = [], document = [], audio = [])

# get file_id & add in array

@bot.message_handler(content_types=["photo"])
def getPhotoFile(message):
    bot.send_message(message.chat.id, message.photo[2].file_id)
    bot.get_file(message.photo[2].file_id)
    file_id["photo"].append(message.photo[2].file_id)

@bot.message_handler(content_types=["video"])
def getPhotoFile(message):
    bot.send_message(message.chat.id, message.video.file_id)
    bot.get_file(message.video.file_id)
    file_id["video"].append(message.video.file_id)

@bot.message_handler(content_types=["document"])
def getPhotoFile(message):
    bot.send_message(message.chat.id, message.document.file_id)
    bot.get_file(message.document.file_id)
    file_id["document"].append(message.document.file_id)

@bot.message_handler(content_types=["audio"])
def getPhotoFile(message):
    bot.send_message(message.chat.id, message.audio.file_id)
    bot.get_file(message.audio.file_id)
    file_id["audio"].append(message.audio.file_id)

@bot.message_handler(commands=["upload"])   # upload file_id in file_id_arr.py
def uploadFile(message):
    if message.chat.type == 'private':
        with open("file_id_arr.json", "w") as fw:
            json.dump(file_id, fw, indent=4)
            fw.close()
        bot.send_message(message.chat.id, "Успешно загружено!")
    else:
        pass

@bot.message_handler(commands=["load"])     # load file_id from file_id_arr.py
def loadInGroup(message):
    if message.chat.type == 'group':
        bot.send_message(message.chat.id, "Вот ваши изображения:")

        with open("file_id_arr.json", "r") as json_data:
            arr_data = json.load(json_data)

        for i in range(len(arr_data["photo"])):
            bot.send_photo(message.chat.id, arr_data["photo"][i])
    else:
        bot.send_message(message.chat.id, "Пс, зайди ко мне...")

@bot.message_handler(commands=["test"])
def testCheckAndOther(message):
    if message.from_user.id == 396224978:
        bot.send_message(message.chat.id, "Буду любить тебя кибер-папочка, Гуден =)")
    else:
        bot.send_message(message.chat.id, "Отвали, извращенец!")
    bot.send_message(message.chat.id, message.chat.type)

# run
bot.polling(none_stop=True)
