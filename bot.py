# Подключаем модуль случайных чисел
import random
import datetime
# Подключаем модуль для Телеграма
import telebot
import xlrd, xlwt
import openpyxl

# читаем excel-файл
day = datetime.datetime.today().weekday()

if (day) == 1:
 wb = openpyxl.load_workbook('ponedelnik_02_03_2020.xlsx')

# печатаем список листов
sheets = wb.sheetnames

# получаем активный лист
sheet = wb.active


########################################5А##############################################################################
yrok5A_1 =("1 урок: "+str(sheet['B2'].value + ", " + "кабинет: ")+str(sheet['C3'].value)+'\n')
yrok5A_2 =("2 урок: "+str(sheet['B4'].value + ", " + "кабинет: ")+str(sheet['C5'].value)+'\n')
yrok5A_3 =("3 урок: "+str(sheet['B6'].value + ", " + "кабинет: ")+str(sheet['C7'].value)+'\n')
yrok5A_4 =("4 урок: "+str(sheet['B8'].value + ", " + "кабинет: ")+str(sheet['C9'].value)+'\n')
yrok5A_5 =("5 урок: "+str(sheet['B10'].value + ", " + "кабинет: ")+str(sheet['C11'].value)+'\n')
yrok5A_6 =("6 урок: "+str(sheet['B12'].value + ", " + "кабинет: ")+str(sheet['C13'].value)+'\n')

problem_5A1 = str(sheet['B14'].value)
problem_5A1 = len(problem_5A1)
problem_5A2 = str(sheet['B15'].value)
problem_5A2 = len(problem_5A2)

print("5A")


if(problem_5A1 < 2):
    yrok5А_6=""





yrok5A =yrok5A_1+yrok5A_2+yrok5A_3+yrok5A_4+yrok5A_5+yrok5A_6
#######################################################################################################################




########################################5Б##############################################################################
yrok5B_1 =("1 урок: "+str(sheet['C2'].value + ", " + "кабинет: ")+str(sheet['C3'].value)+'\n')
yrok5B_2 =("2 урок: "+str(sheet['C4'].value + ", " + "кабинет: ")+str(sheet['C5'].value)+'\n')
yrok5B_3 =("3 урок: "+str(sheet['C6'].value + ", " + "кабинет: ")+str(sheet['C7'].value)+'\n')
yrok5B_4 =("4 урок: "+str(sheet['C8'].value + ", " + "кабинет: ")+str(sheet['C9'].value)+'\n')
yrok5B_5 =("5 урок: "+str(sheet['C10'].value + ", " + "кабинет: ")+str(sheet['C11'].value)+'\n')
yrok5B_6 =("6 урок: "+str(sheet['C12'].value + ", " + "кабинет: ")+str(sheet['C13'].value)+'\n')

problem_5B = str(sheet['B12'].value)
problem_5B = len(problem_5B)
print("5Б")
print(problem_5B)


if(problem_5B < 2):
    yrok5B_6=""



yrok5B =yrok5B_1+yrok5B_2+yrok5B_3+yrok5B_4+yrok5B_5+yrok5B_6
#######################################################################################################################




########################################5В##############################################################################


yrok5V_1 =("1 урок: "+str(sheet['D2'].value + ", " + "кабинет: ")+str(sheet['D3'].value)+'\n')
yrok5V_2 =("2 урок: "+str(sheet['D4'].value + ", " + "кабинет: ")+str(sheet['D5'].value)+'\n')
yrok5V_3 =("3 урок: "+str(sheet['D6'].value + ", " + "кабинет: ")+str(sheet['D7'].value)+'\n')
yrok5V_4 =("4 урок: "+str(sheet['D8'].value + ", " + "кабинет: ")+str(sheet['D9'].value)+'\n')
yrok5V_5 =("5 урок: "+str(sheet['D10'].value + ", " + "кабинет: ")+str(sheet['D11'].value)+'\n')
yrok5V_6 =("6 урок: "+str(sheet['D12'].value + ", " + "кабинет: ")+str(sheet['D13'].value)+'\n')


problem_5V = str(sheet['D14'].value)
problem_5V = len(problem_5V)
print("5В")
print(problem_5V)


yrok5V =yrok5V_1+yrok5V_2+yrok5V_3+yrok5V_4+yrok5V_5+yrok5V_6

#######################################################################################################################




########################################5Г##############################################################################


yrok5G_1 =("1 урок: "+str(sheet['E2'].value + ", " + "кабинет: ")+str(sheet['E3'].value)+'\n')
yrok5G_2 =("2 урок: "+str(sheet['E4'].value + ", " + "кабинет: ")+str(sheet['E5'].value)+'\n')
yrok5G_3 =("3 урок: "+str(sheet['E6'].value + ", " + "кабинет: ")+str(sheet['E7'].value)+'\n')
yrok5G_4 =("4 урок: "+str(sheet['E8'].value + ", " + "кабинет: ")+str(sheet['E9'].value)+'\n')
yrok5G_5 =("5 урок: "+str(sheet['E10'].value + ", " + "кабинет: ")+str(sheet['E11'].value)+'\n')
yrok5G_6 =("6 урок: "+str(sheet['E12'].value + ", " + "кабинет: ")+str(sheet['E13'].value)+'\n')


problem_5G = str(sheet['D12'].value)
problem_5G = len(problem_5G)
print("5G")
print(problem_5G)


if(problem_5G < 2):
    yrok5G_6=""



yrok5G =yrok5G_1+yrok5G_2+yrok5G_3+yrok5G_4+yrok5G_5+yrok5G_6

#######################################################################################################################





########################################6А##############################################################################

yrok6A_1 =("1 урок: "+str(sheet['F2'].value + ", " + "кабинет: ")+str(sheet['F3'].value)+'\n')
yrok6A_2 =("2 урок: "+str(sheet['F4'].value + ", " + "кабинет: ")+str(sheet['F5'].value)+'\n')
yrok6A_3 =("3 урок: "+str(sheet['F6'].value + ", " + "кабинет: ")+str(sheet['F7'].value)+'\n')
yrok6A_4 =("4 урок: "+str(sheet['F8'].value + ", " + "кабинет: ")+str(sheet['F9'].value)+'\n')
yrok6A_5 =("5 урок: "+str(sheet['F10'].value + ", " + "кабинет: ")+str(sheet['F11'].value)+'\n')
yrok6A_6 =("6 урок: "+str(sheet['F12'].value + ", " + "кабинет: ")+str(sheet['F13'].value)+'\n')


problem_6A = str(sheet['F12'].value)
problem_6A = len(problem_6A)
print("6A")
print(problem_6A)


if(problem_6A < 2):
    yrok6A_6=""



yrok6A =yrok6A_1+yrok6A_2+yrok6A_3+yrok6A_4+yrok6A_5+yrok6A_6



#######################################################################################################################



########################################6Б##############################################################################


yrok6B_1 =("1 урок: "+str(sheet['G2'].value + ", " + "кабинет: ")+str(sheet['G3'].value)+'\n')
yrok6B_2 =("2 урок: "+str(sheet['G4'].value + ", " + "кабинет: ")+str(sheet['G5'].value)+'\n')
yrok6B_3 =("3 урок: "+str(sheet['G6'].value + ", " + "кабинет: ")+str(sheet['G7'].value)+'\n')
yrok6B_4 =("4 урок: "+str(sheet['G8'].value + ", " + "кабинет: ")+str(sheet['G9'].value)+'\n')
yrok6B_5 =("5 урок: "+str(sheet['G10'].value + ", " + "кабинет: ")+str(sheet['G11'].value)+'\n')
yrok6B_6 =("6 урок: "+str(sheet['G12'].value + ", " + "кабинет: ")+str(sheet['G13'].value)+'\n')


problem_6B = str(sheet['G12'].value)
problem_6B = len(problem_6B)
print("6Б")
print(problem_6B)

if(problem_6B < 2):
    yrok6B_6=""



yrok6B =yrok6B_1+yrok6B_2+yrok6B_3+yrok6B_4+yrok6B_5+yrok6B_6

#######################################################################################################################





########################################6В##############################################################################



yrok6V_1 =("1 урок: "+str(sheet['H2'].value + ", " + "кабинет: ")+str(sheet['H3'].value)+'\n')
yrok6V_2 =("2 урок: "+str(sheet['H4'].value + ", " + "кабинет: ")+str(sheet['H5'].value)+'\n')
yrok6V_3 =("3 урок: "+str(sheet['H6'].value + ", " + "кабинет: ")+str(sheet['H7'].value)+'\n')
yrok6V_4 =("4 урок: "+str(sheet['H8'].value + ", " + "кабинет: ")+str(sheet['H9'].value)+'\n')
yrok6V_5 =("5 урок: "+str(sheet['H10'].value + ", " + "кабинет: ")+str(sheet['H11'].value)+'\n')
yrok6V_6 =("6 урок: "+str(sheet['H12'].value + ", " + "кабинет: ")+str(sheet['H13'].value)+'\n')


problem_6V = str(sheet['H12'].value)
problem_6V = len(problem_6V)
print("6В")
print(problem_6V)

if(problem_6V < 2):
    yrok6V_6=""



yrok6V =yrok6V_1+yrok6V_2+yrok6V_3+yrok6V_4+yrok6V_5+yrok6V_6

#######################################################################################################################



########################################6Г##############################################################################



yrok6G_1 =("1 урок: "+str(sheet['I2'].value + ", " + "кабинет: ")+str(sheet['I3'].value)+'\n')
yrok6G_2 =("2 урок: "+str(sheet['I4'].value + ", " + "кабинет: ")+str(sheet['I5'].value)+'\n')
yrok6G_3 =("3 урок: "+str(sheet['I6'].value + ", " + "кабинет: ")+str(sheet['I7'].value)+'\n')
yrok6G_4 =("4 урок: "+str(sheet['I8'].value + ", " + "кабинет: ")+str(sheet['I9'].value)+'\n')
yrok6G_5 =("5 урок: "+str(sheet['I10'].value + ", " + "кабинет: ")+str(sheet['I11'].value)+'\n')
yrok6G_6 =("6 урок: "+str(sheet['I12'].value + ", " + "кабинет: ")+str(sheet['I13'].value)+'\n')


problem_6G = str(sheet['I12'].value)
problem_6G = len(problem_6G)
print("6Г")
print(problem_6G)


if(problem_6G < 2):
    yrok6G_6=""



yrok6G =yrok6G_1+yrok6G_2+yrok6G_3+yrok6G_4+yrok6G_5+yrok6G_6

#######################################################################################################################



########################################7А##############################################################################



yrok7A_1 =("1 урок: "+str(sheet['J2'].value + ", " + "кабинет: ")+str(sheet['J3'].value)+'\n')
yrok7A_2 =("2 урок: "+str(sheet['J4'].value + ", " + "кабинет: ")+str(sheet['J5'].value)+'\n')
yrok7A_3 =("3 урок: "+str(sheet['J6'].value + ", " + "кабинет: ")+str(sheet['J7'].value)+'\n')
yrok7A_4 =("4 урок: "+str(sheet['J8'].value + ", " + "кабинет: ")+str(sheet['J9'].value)+'\n')
yrok7A_5 =("5 урок: "+str(sheet['J10'].value + ", " + "кабинет: ")+str(sheet['j11'].value)+'\n')
yrok7A_6 =("6 урок: "+str(sheet['J12'].value + ", " + "кабинет: ")+str(sheet['J13'].value)+'\n')


problem_7A = str(sheet['J12'].value)
problem_7A = len(problem_7A)
print("7A")
print(problem_7A)


if(problem_7A < 2):
    yrok7A_6=""



yrok7A =yrok7A_1+yrok7A_2+yrok7A_3+yrok7A_4+yrok7A_5+yrok7A_6

#######################################################################################################################



########################################7Б##############################################################################



yrok7B_1 =("1 урок: "+str(sheet['K2'].value + ", " + "кабинет: ")+str(sheet['K3'].value)+'\n')
yrok7B_2 =("2 урок: "+str(sheet['K4'].value + ", " + "кабинет: ")+str(sheet['K5'].value)+'\n')
yrok7B_3 =("3 урок: "+str(sheet['K6'].value + ", " + "кабинет: ")+str(sheet['K7'].value)+'\n')
yrok7B_4 =("4 урок: "+str(sheet['K8'].value + ", " + "кабинет: ")+str(sheet['K9'].value)+'\n')
yrok7B_5 =("5 урок: "+str(sheet['K10'].value + ", " + "кабинет: ")+str(sheet['K11'].value)+'\n')
yrok7B_6 =("6 урок: "+str(sheet['K12'].value + ", " + "кабинет: ")+str(sheet['K13'].value)+'\n')


problem_7B = str(sheet['J12'].value)
problem_7B = len(problem_7B)
print("7B")
print(problem_7B)


if(problem_7B < 2):
    yrok7B_6=""



yrok7B =yrok7B_1+yrok7B_2+yrok7B_3+yrok7B_4+yrok7B_5+yrok7B_6

#######################################################################################################################


########################################7В##############################################################################



yrok7V_1 =("1 урок: "+str(sheet['L2'].value + ", " + "кабинет: ")+str(sheet['J3'].value)+'\n')
yrok7V_2 =("2 урок: "+str(sheet['L4'].value + ", " + "кабинет: ")+str(sheet['J5'].value)+'\n')
yrok7V_3 =("3 урок: "+str(sheet['L6'].value + ", " + "кабинет: ")+str(sheet['J7'].value)+'\n')
yrok7V_4 =("4 урок: "+str(sheet['L8'].value + ", " + "кабинет: ")+str(sheet['J9'].value)+'\n')
yrok7V_5 =("5 урок: "+str(sheet['L10'].value + ", " + "кабинет: ")+str(sheet['j11'].value)+'\n')
yrok7V_6 =("6 урок: "+str(sheet['L12'].value + ", " + "кабинет: ")+str(sheet['J13'].value)+'\n')


problem_7V = str(sheet['L12'].value)
problem_7V = len(problem_7V)
print("7 В")
print(problem_7V)


if(problem_7V < 2):
    yrok7V_6=""



yrok7V =yrok7V_1+yrok7V_2+yrok7V_3+yrok7V_4+yrok7V_5+yrok7V_6

#######################################################################################################################




########################################7Г##############################################################################



yrok7G_1 =("1 урок: "+str(sheet['M2'].value + ", " + "кабинет: ")+str(sheet['J3'].value)+'\n')
yrok7G_2 =("2 урок: "+str(sheet['M4'].value + ", " + "кабинет: ")+str(sheet['J5'].value)+'\n')
yrok7G_3 =("3 урок: "+str(sheet['M6'].value + ", " + "кабинет: ")+str(sheet['J7'].value)+'\n')
yrok7G_4 =("4 урок: "+str(sheet['M8'].value + ", " + "кабинет: ")+str(sheet['J9'].value)+'\n')
yrok7G_5 =("5 урок: "+str(sheet['M10'].value + ", " + "кабинет: ")+str(sheet['j11'].value)+'\n')
yrok7G_6 =("6 урок: "+str(sheet['M12'].value + ", " + "кабинет: ")+str(sheet['J13'].value)+'\n')
yrok7G_7 = len(str(sheet['M14'].value))

if(yrok7G_7 >1):
    yrok7G_7 = ("7 урок: "+str(sheet['M14'].value + ", " + "кабинет: ")+str(sheet['M15'].value)+'\n')
else:
    yrok7G_7=""



problem_7G = str(sheet['M12'].value)
problem_7G = len(problem_7G)
print("7 Г")
print(problem_7G)


if(problem_7G < 2):
    yrok7G_6=""



yrok7G =yrok7G_1+yrok7G_2+yrok7G_3+yrok7G_4+yrok7G_5+yrok7G_6+yrok7G_7

#######################################################################################################################



########################################8A##############################################################################



yrok8A_1 =("1 урок: "+str(sheet['N2'].value + ", " + "кабинет: ")+str(sheet['N3'].value)+'\n')
yrok8A_2 =("2 урок: "+str(sheet['N4'].value + ", " + "кабинет: ")+str(sheet['N5'].value)+'\n')
yrok8A_3 =("3 урок: "+str(sheet['N6'].value + ", " + "кабинет: ")+str(sheet['N7'].value)+'\n')
yrok8A_4 =("4 урок: "+str(sheet['N8'].value + ", " + "кабинет: ")+str(sheet['N9'].value)+'\n')
yrok8A_5 =("5 урок: "+str(sheet['N10'].value + ", " + "кабинет: ")+str(sheet['N11'].value)+'\n')
yrok8A_6 =("6 урок: "+str(sheet['N12'].value + ", " + "кабинет: ")+str(sheet['N13'].value)+'\n')


problem_8A = str(sheet['N12'].value)
problem_8A = len(problem_8A)
print("8 A")
print(problem_8A)


if(problem_8A < 2):
    yrok8A_6=""



yrok8A =yrok8A_1+yrok8A_2+yrok8A_3+yrok8A_4+yrok8A_5+yrok8A_6

#######################################################################################################################



########################################8Б##############################################################################



yrok8B_1 =("1 урок: "+str(sheet['O2'].value + ", " + "кабинет: ")+str(sheet['O3'].value)+'\n')
yrok8B_2 =("2 урок: "+str(sheet['O4'].value + ", " + "кабинет: ")+str(sheet['O5'].value)+'\n')
yrok8B_3 =("3 урок: "+str(sheet['O6'].value + ", " + "кабинет: ")+str(sheet['O7'].value)+'\n')
yrok8B_4 =("4 урок: "+str(sheet['O8'].value + ", " + "кабинет: ")+str(sheet['O9'].value)+'\n')
yrok8B_5 =("5 урок: "+str(sheet['O10'].value + ", " + "кабинет: ")+str(sheet['O11'].value)+'\n')
yrok8B_6 =("6 урок: "+str(sheet['O12'].value + ", " + "кабинет: ")+str(sheet['O13'].value)+'\n')


problem_8B = str(sheet['O12'].value)
problem_8B = len(problem_8B)
print("8 Б")
print(problem_8B)


if(problem_8B < 2):
    yrok8B_6=""



yrok8B =yrok8B_1+yrok8B_2+yrok8B_3+yrok8B_4+yrok8B_5+yrok8B_6

#######################################################################################################################


########################################8В##############################################################################



yrok8V_1 =("1 урок: "+str(sheet['P2'].value + ", " + "кабинет: ")+str(sheet['P3'].value)+'\n')
yrok8V_2 =("2 урок: "+str(sheet['P4'].value + ", " + "кабинет: ")+str(sheet['P5'].value)+'\n')
yrok8V_3 =("3 урок: "+str(sheet['P6'].value + ", " + "кабинет: ")+str(sheet['P7'].value)+'\n')
yrok8V_4 =("4 урок: "+str(sheet['P8'].value + ", " + "кабинет: ")+str(sheet['P9'].value)+'\n')
yrok8V_5 =("5 урок: "+str(sheet['P10'].value + ", " + "кабинет: ")+str(sheet['P11'].value)+'\n')
yrok8V_6 =("6 урок: "+str(sheet['P12'].value + ", " + "кабинет: ")+str(sheet['P13'].value)+'\n')
yrok8V_7 = len(str(sheet['P12'].value))
if(yrok8V_7 >1):
    yrok8V_7 = (str(sheet['P12'].value))
else:
    yrok8V_7=""



problem_8V = str(sheet['N12'].value)
problem_8V = len(problem_8V)
if(problem_8V < 2):
    yrok8V_6=""
print("8 В")
print(problem_8V)





yrok8V =yrok8V_1+yrok8V_2+yrok8V_3+yrok8V_4+yrok8V_5+yrok8V_6

#######################################################################################################################



# Указываем токен

bot = telebot.TeleBot('1201504985:AAGMYqDdtcvzHVKwvEE-62Jh3v97yUGGp3w')

# Импортируем типы из модуля, чтобы создавать кнопки

from telebot import types

# Заготовки для трёх предложений



# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»



###########################################Привет#########################################################################
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я могу сказать, какие у тебя сегодня уроки🧠")
        bot.send_message(message.from_user.id, "Напиши свой класс, вместе с буквой (Например 5А)👨‍🎓")
########################################################################################################################



 ########################################5А##############################################################################
    if message.text == "5А" or message.text == "5 А" or message.text == "5а" or message.text == "5 а":


        bot.send_message(message.from_user.id, yrok5A)

 #######################################################################################################################




 ########################################5Б##############################################################################
    if message.text == "5Б" or message.text == "5 Б" or message.text == "5б" or message.text == "5 б":


        bot.send_message(message.from_user.id, yrok5B)

 #######################################################################################################################




 ########################################5В##############################################################################
    if message.text == "5В" or message.text == "5 В" or message.text == "5в" or message.text == "5 в":
            bot.send_message(message.from_user.id, yrok5V)

 ########################################5В##############################################################################



 ########################################5Г##############################################################################

    if message.text == "5Г" or message.text == "5 Г" or message.text == "5г" or message.text == "5 г":
        bot.send_message(message.from_user.id, yrok5G)
 #######################################################################################################################




 ########################################6А##############################################################################
    if message.text == "6А" or message.text == "6 А" or message.text == "6а" or message.text == "6 а":
        bot.send_message(message.from_user.id, yrok6A)
 #######################################################################################################################



 ########################################6Б##############################################################################
    if message.text == "6Б" or message.text == "6 Б" or message.text == "6б" or message.text == "6 б":
        bot.send_message(message.from_user.id, yrok6B)
 #######################################################################################################################



 ########################################6В##############################################################################
    if message.text == "6В" or message.text == "6 В" or message.text == "6в" or message.text == "6 в":
            bot.send_message(message.from_user.id, yrok6V)
 #######################################################################################################################




########################################6Г##############################################################################
    if message.text == "6Г" or message.text == "6 Г" or message.text == "6г" or message.text == "6 г":
        bot.send_message(message.from_user.id, yrok6G)
#######################################################################################################################




########################################7А##############################################################################
    if message.text == "7А" or message.text == "7 А" or message.text == "7а" or message.text == "7 а":
        bot.send_message(message.from_user.id, yrok7A)
#######################################################################################################################

    ########################################7Б##############################################################################
    if message.text == "7Б" or message.text == "7 Б" or message.text == "7б" or message.text == "7 б":
            bot.send_message(message.from_user.id, yrok7B)
    #######################################################################################################################



    ########################################7В##############################################################################
    if message.text == "7В" or message.text == "7 В" or message.text == "7в" or message.text == "7 в":
        bot.send_message(message.from_user.id, yrok7V)
    #######################################################################################################################




    ########################################7В##############################################################################
    if message.text == "7Г" or message.text == "7 Г" or message.text == "7г" or message.text == "7 г":
        bot.send_message(message.from_user.id, yrok7G)
    #######################################################################################################################

     ########################################7В##############################################################################
    if message.text == "8А" or message.text == "8 А" or message.text == "8а" or message.text == "8 а":
            bot.send_message(message.from_user.id, yrok8A)
        #######################################################################################################################



    ########################################7В##############################################################################
    if message.text == "8Б" or message.text == "8 Б" or message.text == "8б" or message.text == "8 б":
        bot.send_message(message.from_user.id, yrok8B)
    #######################################################################################################################

    ########################################7В##############################################################################
    if message.text == "8В" or message.text == "8 В" or message.text == "8в" or message.text == "8 в":
        bot.send_message(message.from_user.id, yrok8B)
    #######################################################################################################################

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")




#

bot.polling(none_stop=True, interval=0)
