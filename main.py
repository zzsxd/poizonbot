#####################################
#            Created by             #
#               zzsxd               #
#####################################
config_name = 'secrets.json'
#####################################
import os
import telebot
import platform
from config_parser import ConfigParser
from frontend import Bot_inline_btns
from backend import TempUserData


def main():
    @bot.message_handler(commands=['start'])
    def start_message(message):
        buttons = Bot_inline_btns()
        user_id = message.chat.id
        bot.send_message(message.chat.id, 'Привет, дорогой покупатель! Мы 95Shop предоставляем услугу заказов товаров '
                                          'с китайских маркетплейсов 🧯\n'
                                          '• Низкие комиссии\n'
                                          '• Частые скидки\n'
                                          '• Доставка 5-10 дней\n', reply_markup=buttons.start_btns())
        temp_user_data.temp_data(user_id)[user_id][0] = 4

    @bot.message_handler(content_types=['text'])
    def text(message):
        user_id = message.chat.id
        code = temp_user_data.temp_data(user_id)[user_id][0]
        buttons = Bot_inline_btns()
        if code == 0:
            yan = int(message.text)
            rub = yan * 13.5
            commission = 20 / 100 * rub
            result = rub + commission + 400
            bot.send_message(message.chat.id, f'Цена товара: {result}₽')
            temp_user_data.temp_data(user_id)[user_id][0] = 4
        elif code == 1:
            yan = int(message.text)
            rub = yan * 13.5
            commission = 20 / 100 * rub
            result = rub + commission + 300
            bot.send_message(message.chat.id, f'Цена товара: {result}₽')
            temp_user_data.temp_data(user_id)[user_id][0] = 4
        elif code == 2:
            yan = int(message.text)
            rub = yan * 13.5
            commission = 20 / 100 * rub
            result = rub + commission + 200
            bot.send_message(message.chat.id, f'Цена товара: {result}₽')
            temp_user_data.temp_data(user_id)[user_id][0] = 4
        elif code == 3:
            bot.send_message(message.chat.id, 'Поздравляем! Вы получаете скидку 200₽ на любой заказ!')
            temp_user_data.temp_data(user_id)[user_id][0] = 4
        elif code == 4:
            if message.text == 'Заказать с Poizon🧯':
                bot.send_message(message.chat.id, 'Для заказа товара с пойзон напишите модератору @virtosvskiwork')
            elif message.text == 'Рассчитать стоимость💸':
                bot.send_message(message.chat.id, 'Выберите тип товара', reply_markup=buttons.cost_btns())
            elif message.text == 'Скидки💯':
                bot.send_message(message.chat.id, 'Проверьте свои знания брендов и получите небольшой бонус!')
                bot.send_message(message.chat.id, '1. В каком году был основан бренд Nike?',
                                 reply_markup=buttons.test_questone_btns())
            elif message.text == 'Заказать с TaoBao/1688🇨🇳':
                bot.send_message(message.chat.id,
                                 'Для заказа товара с таобао/1688 напишите модератору @virtosvskiwork\n'
                                 'Внимательно проверяйте отзывы продавца на китайском марктеплейсе!\n'
                                 'Сроки могут увеличиться на пару дней')
            elif message.text == 'Помощь❓':
                bot.send_message(message.chat.id, 'Если вы хотите задать вопрос -> @virtosvskiwork')
            elif message.text == 'Отзывы📝':
                bot.send_message(message.chat.id, 'Отзывы о заказах вы можете прочитать в нашем канале\n'
                                                       'https://t.me/s95hop')


    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        buttons = Bot_inline_btns()
        user_id = call.message.chat.id
        code = temp_user_data.temp_data(user_id)[user_id][0]
        buttons = Bot_inline_btns()
        if call.data == 'boots':  # or call.data == 'shoes' or call.data == 'trousers' or call.data == 'accessory':
            bot.send_message(call.message.chat.id, 'Введите цену в Юанях (¥)')
            temp_user_data.temp_data(user_id)[user_id][0] = 0
        elif call.data == 'shoes' or call.data == 'trousers':
            bot.send_message(call.message.chat.id, 'Введите цену в Юанях (¥)')
            temp_user_data.temp_data(user_id)[user_id][0] = 1
        elif call.data == 'accessory':
            bot.send_message(call.message.chat.id, 'Введите цену в Юанях (¥)')
            temp_user_data.temp_data(user_id)[user_id][0] = 2
        elif call.data == 'not_true1' or call.data == 'not_true2' or call.data == 'not_true3':
            bot.send_message(call.message.chat.id, 'Ответ не верный!')
        elif call.data == 'true1':
            bot.send_message(call.message.chat.id, 'Правильно! 1/5')
            bot.send_message(call.message.chat.id, '2. Как зовут основателя бренда Adidas?',
                             reply_markup=buttons.test_questsecond_btns())
        elif call.data == 'not_true4' or call.data == 'not_true5' or call.data == 'not_true6':
            bot.send_message(call.message.chat.id, 'Ответ не верный!')
        elif call.data == 'true2':
            bot.send_message(call.message.chat.id, 'Правильно! 2/5')
            bot.send_message(call.message.chat.id, '3. Самая популярная модель кроссовок Adidas?',
                             reply_markup=buttons.test_questthird_btns())
        elif call.data == 'not_true7' or call.data == 'not_true8' or call.data == 'not_true9':
            bot.send_message(call.message.chat.id, 'Ответ не верный!')
        elif call.data == 'true3':
            bot.send_message(call.message.chat.id, 'Правильно! 3/5')
            bot.send_message(call.message.chat.id, '4. Кто основатель бренда Rick Owens?',
                             reply_markup=buttons.test_questfour_btns())
        elif call.data == 'not_true10' or call.data == 'not_true11' or call.data == 'not_true12':
            bot.send_message(call.message.chat.id, 'Ответ не верный!')
        elif call.data == 'true4':
            bot.send_message(call.message.chat.id, 'Правильно! 4/5')
            bot.send_message(call.message.chat.id, '5. Ваши любимые кроссовки?')
            temp_user_data.temp_data(user_id)[user_id][0] = 3
    bot.polling(none_stop=True)


if '__main__' == __name__:
    os_type = platform.system()
    work_dir = os.path.dirname(os.path.realpath(__file__))
    config = ConfigParser(f'{work_dir}/{config_name}', os_type)
    temp_user_data = TempUserData()
    bot = telebot.TeleBot(config.get_config()['tg_api'])
    main()
