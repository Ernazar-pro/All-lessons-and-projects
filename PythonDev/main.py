from aiogram import *

token='6044591045:AAG8_O0J2_ldEGkwsDff3WHcpJMDrYRnrv0'


bot=Bot(token)
disp=Dispatcher(bot)

@disp.message_handler(commands=['start'])
async def start(message):
    name=message['from']['first_name']
    await message.reply(f'Здраствуйте, {name}')
    print(f'{name} нажимал start')

@disp.message_handler(commands=['help'])
async def help(message):
    name=message['from']['first_name']
    await message.reply(f'Здраствуйте это бот, где отправиться файлы, ссылки и др о Python')
    print(f'{name} нажимал help')


if __name__ == '__main__':
    executor.start_polling(disp,skip_updates=True)