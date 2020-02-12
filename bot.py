import telebot
import config
import time
import json

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

thour = time.localtime()
corr_time = str(thour[3]) +":"+ str(thour[4])

file_id = []

with open('file_id_arr.json', 'r') as json_data:
    arr_data = json.load(json_data)

# get file_id & add in array

@bot.message_handler(content_types=["photo"])
def getPhotoFile(message):
    bot.send_message(message.chat.id, message.photo[2].file_id)
    bot.get_file(message.photo[2].file_id)
    file_id.append(message.photo[2].file_id)

@bot.message_handler(content_types=["video"])
def getPhotoFile(message):
    bot.send_message(message.chat.id, message.video.file_id)
    bot.get_file(message.video.file_id)
    file_id.append(message.video.file_id)

@bot.message_handler(content_types=["document"])
def getPhotoFile(message):
    bot.send_message(message.chat.id, message.document.file_id)
    bot.get_file(message.document.file_id)
    file_id.append(message.document.file_id)

@bot.message_handler(content_types=["audio"])
def getPhotoFile(message):
    bot.send_message(message.chat.id, message.audio.file_id)
    bot.get_file(message.audio.file_id)
    file_id.append(message.audio.file_id)

@bot.message_handler(commands=["upload"])   # load file_id in file_id_arr.py
def loadFile(message):
    with open("file_id_arr.json", "w") as fw:
        json.dump(file_id, fw, indent=4)

@bot.message_handler(commands=["delete"])
def deleteFile(message):
    json_arr = open("file_id_arr.json", "r")
    bot.send_message(message.chat.id, "Выберите файл:")
    for i in arr_data:
        bot.send_message(message.chat.id, "<a href = 'https://api.telegram.org/file/bot"+config.TOKEN+"/"+i + "'>"+id+"</a>\n".format(message.from_user),
    		parse_mode = 'html')

    bot.message_handler(content_types=["text"])
    def selectFile(message):
        i = message.chat.text
        print(arr_data[i])

@bot.message_handler(commands=["start"])
def answer(message):

    if message.chat.type == 'private':

        if message.text.lower() == 'добрый день':

            bot.send_sticker(message.chat.id, config.STICKER["Yey"])
            bot.send_message(message.chat.id, "Еей, добрый.")

        else:
            bot.send_sticker(message.chat.id, config.STICKER["Hmm"])
            bot.send_message(message.chat.id, "Тяк, я тебя не понял!")

    else:
        thour = time.localtime()
        print(str(thour.tm_hour)+":"+str(thour.tm_min))

# run
bot.polling(none_stop=True)
