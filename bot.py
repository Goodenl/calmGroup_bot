# make cofig file with TOKEN

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
    bot.send_message(message.chat.id, "Фото загружено!\n" + "(" + message.photo[0].file_id + ")")
    bot.get_file(message.photo[0].file_id)
    file_id["photo"].append(message.photo[0].file_id)


@bot.message_handler(content_types=["video"])
def getPhotoFile(message):
    bot.send_message(message.chat.id, "Видео загружено!\n" + "(" + message.video.file_id + ")")
    bot.get_file(message.video.file_id)
    file_id["video"].append(message.video.file_id)

@bot.message_handler(content_types=["document"])
def getPhotoFile(message):
    bot.send_message(message.chat.id, "Документ загружено!\n" + "(" + message.document.file_id + ")")
    bot.get_file(message.document.file_id)
    file_id["document"].append(message.document.file_id)

@bot.message_handler(content_types=["audio"])
def getPhotoFile(message):
    bot.send_message(message.chat.id, "Аудио загружено!\n" + "(" + message.audio.file_id + ")")
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
        bot.send_message(message.chat.id, "Пс, зайди ко мне...")

@bot.message_handler(commands=["load"])     # load file_id from file_id_arr.py
def loadInGroup(message):
    if message.chat.type == 'group':

        with open("file_id_arr.json", "r") as json_data:
            arr_data = json.load(json_data)
            json_data.close()

        if arr_data["photo"]:
            for i in range(len(arr_data["photo"])):
                bot.send_photo(message.chat.id, arr_data["photo"][i])
        if arr_data["video"]:
            for i in range(len(arr_data["video"])):
                bot.send_video(message.chat.id, arr_data["video"][i])
        if arr_data["document"]:
            for i in range(len(arr_data["document"])):
                bot.send_document(message.chat.id, arr_data["document"][i])
        if arr_data["audio"]:
            for i in range(len(arr_data["audio"])):
                bot.send_audio(message.chat.id, arr_data["audio"][i])
    else:
        pass

@bot.message_handler(commands=["help"])
def helplessUser(message):
    if message.chat.type == "group":
        bot.send_message(message.chat.id, "Дорогой, "+ message.from_user.first_name +", наверное ты не знаешь как загружать файлы? Зайди ко мне в личный чатик и отправь команду \"/help\", тогда я тебе расскажу ;)")
    elif message.chat.type == "private":
        bot.send_message(message.chat.id, "Ты понимаешь куда ты попал, салага?! Здесь тебе не место где ты просто можешь ходить по чатам.\nЗначит слушай меня, здесь главное не ошибиться, иначе полетят все сервера с твоими голыми фоточками.\nБери свои фотки, музыку и прочее барахло которое нужно загрузить и аккуратно, слышишь, аккуратно ложи в этот чат. Потом, чтобы подтвердить, введи команду /upload, тогда все твои фоточки будут в порядке, сынок.")

@bot.message_handler(commands=["test"])
def testCheckAndOther(message):
    if message.from_user.id == 396224978:
        bot.send_message(message.chat.id, "Буду любить тебя кибер-папочка, Гуден =)")
    else:
        bot.send_message(message.chat.id, "Отвали, извращенец!")
    bot.send_message(message.chat.id, message.chat.type)
    with open("file_id_arr.json", "r") as json_data:
        arr_data = json.load(json_data)
        json_data.close()
    bot.send_message(message.chat.id, arr_data)


# run
bot.polling(none_stop=True)
