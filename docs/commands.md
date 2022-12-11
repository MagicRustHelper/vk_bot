# Описание команд бота

Команды начинаются с префикса `.` или `/`. Все команды бота не чувствительны к языку. Например команда `/bans` или `.ифты` это одно и тоже.

## Команды для всех

## /checks
Синтаксис: /checks  
Другие варианты команды: проверки, сруслы  
**Описание**: Выводит количество проверок модераторов за рабочий месяц (с 10 числа текущего месяца по 9 число следующего месяца)

## /stats
**Синтаксис**: /stats [КД=10.0]  
*Другие варианты команды*: ыефеы, стата  
**Описание**: Выводит игроков со статиской больше указанного КД  
**Параметры**:
* КД - Значение КД, по умолчанию 10.0. Можно указаывать в виде числа с точкой. Например: 5.6

## /new
**Синтаксис**: /new  
*Другие варианты команды*: туц, новые  
**Описание**: Выводит список новых игроков (Зашли менее 7 дней назад) со статистикой больше 1.0. 

## /bans
**Синтаксис**: /bans [количество дней с бана=30d]  
*Другие варианты команды*: ифты, баны  
**Описание**: Выводит список игроков, которые были забанены в последние указанное количество дней.
**Параметры**:
* количество дней с бана - количество дней с бана, по умолчанию 30 дней
  * Указывать виде значения в днях, неделях, месяцах или годах. Например: 30d, 2w, 1m, 1y

**!NOTE!**: Команда работает медленно, да и в целом пока работает очень плохо.



