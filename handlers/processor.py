from winreg import QueryInfoKey, QueryValue, QueryValueEx
from aiogram import types, Dispatcher
# from keyboards import callback_data, choice, action_callback 
from create_bot import dp, bot
from aiogram.types import Message, CallbackQuery
import re
import random

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emojis
import handlers.processor
chey_hod = ''

X = "\U0000274C"
O = "\U00002B55"
win = 0

def key_board(list: list): 
    choice = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=list[0], callback_data="1"),
                InlineKeyboardButton(text=list[1], callback_data="2"),
                InlineKeyboardButton(text=list[2], callback_data="3"),
            ],
            [
                InlineKeyboardButton(text=list[3], callback_data="4"),
                InlineKeyboardButton(text=list[4], callback_data="5"),
                InlineKeyboardButton(text=list[5], callback_data="6"),
            ],
            [
                InlineKeyboardButton(text=list[6], callback_data="7"),
                InlineKeyboardButton(text=list[7], callback_data="8"),
                InlineKeyboardButton(text=list[8], callback_data="9"),
            ],
            [
                InlineKeyboardButton(text=f"{list[-1]}", callback_data=f"{list[-1]}"),
            ]
        ]
    )
    return choice


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    global list, win
    list = ['\U00002753', '\U00002753', '\U00002753', '\U00002753', '\U00002753', '\U00002753', '\U00002753', '\U00002753', '\U00002753', 'Узнать чей первый ход']
    win = 0
    await bot.send_message(message.from_user.id, "Привет! Узнай чей ход!", reply_markup=key_board(list))
    
    

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    global list, win
    list = ['\U00002753', '\U00002753', '\U00002753', '\U00002753', '\U00002753', '\U00002753', '\U00002753', '\U00002753', '\U00002753', 'Узнать чей первый ход']
    win = 0
    await message.reply(f"Просто играем! \U0001F600")
    await bot.send_message(message.from_user.id, "Узнай чей ход!", reply_markup=key_board(list))
    
def check_win(list: list, win):
        if (list[0] == list[1] == list[2] == O) or (list[3] == list[4] == list[5] == O) or (list[6] == list[7] == list[8] == O) or (list[0] == list[3] == list[6] == O) or (list[1] == list[4] == list[7] == O) or (list[2] == list[5] == list[8] == O) or (list[0] == list[4] == list[8] == O) or (list[2] == list[4] == list[6] == O):
            list[-1] = f"Победил {O}! \U0001F3C6"
            win = 1
            
        elif (list[0] == list[1] == list[2] == X) or (list[3] == list[4] == list[5] == X) or (list[6] == list[7] == list[8] == X) or (list[0] == list[3] == list[6] == X) or (list[1] == list[4] == list[7] == X) or (list[2] == list[5] == list[8] == X) or (list[0] == list[4] == list[8] == X) or (list[2] == list[4] == list[6] == X):
            list[-1] = f"Победил {X} ! \U0001F3C6" 
            win = 1
        return (list, win)   

def change_player(list:list, chey_hod):
    global O, X
    if chey_hod == O:
        list[-1] = f'Ход {X}'
        chey_hod = X
    elif chey_hod == X:
        list[-1] = f'Ход {O}'
        chey_hod = O
    return (list, chey_hod)  

@dp.callback_query_handler(lambda c: c.data !='' )
async def callback_func(query: types.CallbackQuery):
    global list, chey_hod, win 
    data = query.data
         
    if data == 'Узнать чей первый ход':
        chey_hod = random.randrange(0,2)
        if chey_hod == 0:
            list[-1] = f'Ход {O}'
            chey_hod = O
        else:
            list[-1] = f'Ход {X}'
            chey_hod = X
        await query.message.edit_text("Сделайте ход", reply_markup=key_board(list))
    

    elif data == '1':
       
        if list[0] == '\U00002753':
            if win == 1 or chey_hod == '':
                await query.answer()
                
            elif win == 0:
                
                list[0] = chey_hod
                list, chey_hod = change_player(list, chey_hod)
                list, win = check_win(list, win)
                if win == 0:
                    if '\U00002753'  in list:
                        await query.message.edit_text(" Сделайте ход ", reply_markup=key_board(list))
                    else: 
                        list[-1] = f"Победила дружба!"
                        await query.message.edit_text("ИГРА ОКОНЧЕНА!!!", reply_markup=key_board(list))
                elif win == 1:
                    await query.message.edit_text("СТОП!!!", reply_markup=key_board(list))
        else:  
            await query.answer()   
        
    elif data == '2':
        
        if list[1] == '\U00002753':
            if win == 1 or chey_hod == '':
                await query.answer()
                
            elif win == 0:
                
                list[1] = chey_hod
                list, chey_hod = change_player(list, chey_hod)
                list, win = check_win(list, win)
                if win == 0:
                    if '\U00002753'  in list:
                        await query.message.edit_text(" Сделайте ход ", reply_markup=key_board(list))
                    else: 
                        list[-1] = f"Победила дружба!"
                        await query.message.edit_text("ИГРА ОКОНЧЕНА!!!", reply_markup=key_board(list))
                elif win == 1:
                    await query.message.edit_text("СТОП!!!", reply_markup=key_board(list)) 
        else:  
            await query.answer()   
       
    elif data == '3':
       
        if list[2] == '\U00002753':
            if win == 1 or chey_hod == '':
                await query.answer()
                
            elif win == 0:
                
                list[2] = chey_hod
                list, chey_hod = change_player(list, chey_hod)
                list, win = check_win(list, win)
                if win == 0:
                    if '\U00002753'  in list:
                        await query.message.edit_text(" Сделайте ход ", reply_markup=key_board(list))
                    else: 
                        list[-1] = f"Победила дружба!"
                        await query.message.edit_text("ИГРА ОКОНЧЕНА!!!", reply_markup=key_board(list))
                elif win == 1:
                    await query.message.edit_text("СТОП!!!", reply_markup=key_board(list))
        else:  
            await query.answer()   
            

    elif data == '4':
        
        if list[3] == '\U00002753':
            if win == 1 or chey_hod == '':
                await query.answer()
                
            elif win == 0:
                list[3] = chey_hod
                list, chey_hod = change_player(list, chey_hod)
                list, win = check_win(list, win)
                if win == 0:
                    if '\U00002753'  in list:
                        await query.message.edit_text(" Сделайте ход ", reply_markup=key_board(list))
                    else: 
                        list[-1] = f"Победила дружба!"
                        await query.message.edit_text("ИГРА ОКОНЧЕНА!!!", reply_markup=key_board(list))
                elif win == 1:
                    await query.message.edit_text("СТОП!!!", reply_markup=key_board(list))
        else:  
            await query.answer()   
           
        
    elif data == '5':
        
        if list[4] == '\U00002753':
            if win == 1 or chey_hod == '':
                await query.answer()
                
            elif win == 0:
                list[4] = chey_hod
                list, chey_hod = change_player(list, chey_hod)
                list, win = check_win(list, win)
                if win == 0:
                    if '\U00002753'  in list:
                        await query.message.edit_text(" Сделайте ход ", reply_markup=key_board(list))
                    else: 
                        list[-1] = f"Победила дружба!"
                        await query.message.edit_text("ИГРА ОКОНЧЕНА!!!", reply_markup=key_board(list))
                elif win == 1:
                    await query.message.edit_text("СТОП!!!", reply_markup=key_board(list))
        else:  
            await query.answer()    
           
    elif data == '6':
        
        if list[5] == '\U00002753':
            if win == 1 or chey_hod == '':
                await query.answer()
                
            elif win == 0:
                list[5] = chey_hod
                list, chey_hod = change_player(list, chey_hod)
                list, win = check_win(list, win)
                if win == 0:
                    if '\U00002753'  in list:
                        await query.message.edit_text(" Сделайте ход ", reply_markup=key_board(list))
                    else: 
                        list[-1] = f"Победила дружба!"
                        await query.message.edit_text("ИГРА ОКОНЧЕНА!!!", reply_markup=key_board(list))
                elif win == 1:
                    await query.message.edit_text("СТОП!!!", reply_markup=key_board(list))
        else:  
            await query.answer()       

    elif data == '7':
        if list[6] == '\U00002753':
            if win == 1 or chey_hod == '':
                await query.answer()
                
            elif win == 0:
                list[6] = chey_hod
                list, chey_hod = change_player(list, chey_hod)
                list, win = check_win(list, win)
                if win == 0:
                    if '\U00002753'  in list:
                        await query.message.edit_text(" Сделайте ход ", reply_markup=key_board(list))
                    else: 
                        list[-1] = f"Победила дружба!"
                        await query.message.edit_text("ИГРА ОКОНЧЕНА!!!", reply_markup=key_board(list))
                elif win == 1:
                    await query.message.edit_text("СТОП!!!", reply_markup=key_board(list))
        else:  
            await query.answer()        

    elif data == '8':
        
        if list[7] == '\U00002753':
            if win == 1 or chey_hod == '':
                await query.answer()
                
            elif win == 0:
                list[7] = chey_hod
                list, chey_hod = change_player(list, chey_hod)
                list, win = check_win(list, win)
                if win == 0:
                    if '\U00002753'  in list:
                        await query.message.edit_text(" Сделайте ход ", reply_markup=key_board(list))
                    else: 
                        list[-1] = f"Победила дружба!"
                        await query.message.edit_text("ИГРА ОКОНЧЕНА!!!", reply_markup=key_board(list))
                elif win == 1:
                    await query.message.edit_text("СТОП!!!", reply_markup=key_board(list))
        else:  
            await query.answer()    
             

    elif data == '9':
        
        if list[8] == '\U00002753':
            if win == 1 or chey_hod == '':
                await query.answer()
                
            elif win == 0:
                list[8] = chey_hod
                list, chey_hod = change_player(list, chey_hod)
                list, win = check_win(list, win)
                if win == 0:
                    await query.message.edit_text(" Сделайте ход ", reply_markup=key_board(list))
                elif win == 1:
                    await query.message.edit_text("СТОП!!!", reply_markup=key_board(list))
        else:  
            await query.answer()    

    elif data != 'Узнать чей первый ход':
        await query.answer()      
