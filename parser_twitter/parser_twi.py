"""Тут находятся основные функции парсинга твиттера"""

def reading_last_twit(arg):
    """
    Функция, которая принимает в себя respounse, конвертирует его в формат json,
    а потом возвращает строковый вид твита.
    Она хендлит ошибки, которые идут, по разным вариациям домашней странички.
    В зависимости, есть ли закрепленный твит, и если под последним есть добавления.
    """
    
    twi_json = arg.json()
    try:  # Если есть закрепленный и нет добавления к последнему твиту
        twi_json_items = twi_json['data']['user']['result']['timeline_v2']['timeline']['instructions']
        twi_json_items = twi_json_items[2]  
        twi_json_items = twi_json_items['entries']
        twi_json_items = twi_json_items[0]
        twi_json_items = twi_json_items['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
        return twi_json_items
    except IndexError:  # Если нет закрепленного
        twi_json_items = twi_json['data']['user']['result']['timeline_v2']['timeline']['instructions']
        twi_json_items = twi_json_items[1]  # Если нет закрепленного то тут будет [1]
        twi_json_items = twi_json_items['entries']
        twi_json_items = twi_json_items[0]
        twi_json_items = twi_json_items['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
        return twi_json_items
    except KeyError:  # Если есть закрепленный и есть добавление твитов то будет к последнему твиту
        twi_json_items = twi_json['data']['user']['result']['timeline_v2']['timeline']['instructions']
        twi_json_items = twi_json_items[2]  
        twi_json_items = twi_json_items['entries']
        twi_json_items = twi_json_items[0]
        twi_json_items = twi_json_items['content']['items']
        twi_json_items = twi_json_items[-1]
        twi_json_items = twi_json_items['item']['itemContent']['tweet_results']['result']['legacy']['full_text']
        return twi_json_items
      
def func_return_text(response, func_reading_twit):
    """Основная функция создающая текст. Её нужно импортировать в телеграм-бот."""
    
    respounse = response
    text_twit = func_reading_twit(respounse)
    return text_twit