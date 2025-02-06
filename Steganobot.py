import telebot
from telebot import types
from stegano import *

bot = telebot.TeleBot("")






def shifr(message):
    try:
        secret = exifHeader.hide("photo.jpg", "photoshifr.jpg", message.text)
        img = open('photoshifr.jpg', 'rb')
        bot.send_document(message.chat.id, img)
    except Exception:
        bot.send_message(message.chat.id, text="Что то пошло не так, попробуйте ещё раз")
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Расшифровать")
    btn2 = types.KeyboardButton("Зашифровать")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот созданый для стеганографии".format(message.from_user), reply_markup=markup)
    start = open('start.jpg', 'rb')
    bot.send_photo(message.chat.id, start)
    

@bot.message_handler(content_types=['text', 'photo', 'document'])
def func(message):
    if(message.text == "Зашифровать"):
        def handle_photo(message):
            try:
                chat_id = message.chat.id
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                with open("photo.jpg", 'wb') as new_file:
                    new_file.write(downloaded_file)
                bot.register_next_step_handler(bot.reply_to(message, 'Напишите сообщение'), shifr)
            except AttributeError:
                bot.send_message(message.chat.id, text="Вы отправили не фото")
            except Exception :
                bot.send_message(message.chat.id, text="Что то пошло не так, попробуйте ещё раз")
        bot.register_next_step_handler(bot.send_message(message.chat.id, text="Отправьте фото формата 'jpg' без сжатия"), handle_photo)
    if(message.text == "Расшифровать"):
        def handle_photo12(message):
            try: 
                chat_id = message.chat.id
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                with open("photo1.jpg", 'wb') as new_file:
                    new_file.write(downloaded_file)
                result = exifHeader.reveal("photo1.jpg")
                bot.send_message(message.chat.id, result)
            except ValueError:
                bot.send_message(message.chat.id, text="Зашифрованное фото является не поддерживаемым форматом")
            except AttributeError:
                bot.send_message(message.chat.id, text="Вы отправили не фото")
            except Exception :
                bot.send_message(message.chat.id, text="Что то пошло не так, попробуйте ещё раз")
        bot.register_next_step_handler(bot.send_message(message.chat.id, text="Отправьте фото"), handle_photo12)
                















bot.polling(none_stop=True, interval=0)