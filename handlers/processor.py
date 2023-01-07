from winreg import QueryInfoKey, QueryValue, QueryValueEx
from aiogram import types, Dispatcher
from keyboards import callback_data, choice, action_callback 
from create_bot import dp, bot
from aiogram.types import Message, CallbackQuery
import re
from decimal import Decimal
value = ''
old_value = ''
list = []
list_elemens = []
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    global value
    await bot.send_message(message.from_user.id, "Привет!", reply_markup=choice)
    value = '0'
    

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    global value
    await message.reply("Набери на клавиатуре, что тебе нужно посчитать.")
    await bot.send_message(message.from_user.id, "0", reply_markup=choice)
    value = '0'

@dp.callback_query_handler(lambda c: c.data !='' )
async def callback_func(query: types.CallbackQuery):
    global value, old_value, list, list_oper,list_elemens
    
    data = query.data
      
    if data == 'C':
        value = '0'
    
    elif data == '+':
        if '=' in value:# для контроля ввода знака действия после '='
            value = data
        elif value == '0':
            value = data
        else:
            list = re.split(r"[-|+|*|/]+", value) # для контроля лишней точки
            list_elemens = value.split() # для контроля лишнего знака действия
            if list_elemens[-1] in "+-*/":
                await query.answer()
            else:
                value += f' {data} '
        
    elif data == '-':
        if '=' in value: # для контроля ввода знака действия после '='
            value = data
        elif value == '0':
            value = data
        else:
            list = re.split(r"[-|+|*|/]+", value) # для контроля лишней точки
            list_elemens = value.split() # для контроля лишнего знака действия
            if list_elemens[-1] in "+-*/":
                await query.answer()
            else:
                value += f' {data} '
        
    elif data == '*':
        if '=' in value:# для контроля ввода знака действия после '='
            await query.answer()
        elif value == '0':
            await query.answer()
        else:
            list = re.split(r"[-|+|*|/]+", value) # для контроля лишней точки
            list_elemens = value.split() # для контроля лишнего знака действия
            if list_elemens[-1] in "+-*/":
                await query.answer()
            else:
                value += f' {data} '
        
    elif data == '/':
        if '=' in value: # для контроля ввода знака действия после '='
            await query.answer()
        elif value == '0':
            await query.answer()
        else:
            list = re.split(r"[-|+|*|/]+", value) # для контроля лишней точки
            list_elemens = value.split() # для контроля лишнего знака действия
            if list_elemens[-1] in "+-*/":
                await query.answer()
            else:
                value += f' {data} '
        
        
    elif data == '<':
        value = value[:-1] if len(value) != 1 else '0'
    elif data == '.': 
        list = re.split(r"[-|+|*|/]+", value)
        list_elemens = value.split()
        print(list)
        if list[-1].count('.') != 0: # если в последнем числе есть '.', то вторую не даст поставить
            await query.answer()
        elif list_elemens[-1] in '-+*/': # нельзя ставь точку после знаков действий
            await query.answer()
        else:
            value += data
           
    elif data == '=':
        if '=' in value: # Обработка повторного нажатия "="
            await query.answer()
        else:
            old_value = value
            list_elemens = value.split()
            
            if list_elemens[-1] in '*/-+':
                list_elemens = list_elemens[:-1] # Игнорируем лишний знак действия 
                      
            actions = {
            "*": lambda x, y: str(Decimal(x) * Decimal(y)),
            "/": lambda x, y: str(Decimal(x) / Decimal(y)),
            "+": lambda x, y: str(Decimal(x) + Decimal(y)),
            "-": lambda x, y: str(Decimal(x) - Decimal(y))}
            
            
            list_oper_ind = [i for i,e in enumerate(list_elemens) if e in '*/']
            while list_oper_ind:
                ind_op = list_oper_ind[0]
                a, b, c = list_elemens[ind_op-1:ind_op+2]
                if b == '/' and c == '0':
                    value = 'Ошибка! Делить на 0 нельзя!'
                    await query.message.edit_text("Ошибка! Делить на 0 нельзя!", reply_markup=choice)

                else:
                    list_elemens[ind_op-1:ind_op+2] = [actions[b](a,c)]
                    list_oper_ind = [i for i,e in enumerate(list_elemens) if e in '*/']
                    
            while len(list_elemens) > 1:
                a, b, c = list_elemens[:3]
                list_elemens[:3] = [actions[b](a,c)] 
            
            value = f'{old_value} = {list_elemens[0]}'
            
       
    else:
        if '=' in value:
            value = data
       
        elif value == '0':
            value = data
        
        elif value == 'Привет!':
            value = data
        
        else:
            value += data
    
    if value != old_value:
        if value == " ":
            await query.message.edit_text("0", reply_markup=choice)
            
        else:
            await query.message.edit_text(f"{value}", reply_markup=choice)
            
    # old_value = value
    # if value == 'Ошибка! Делить на 0 нельзя!':
    #     value = '0'



    
