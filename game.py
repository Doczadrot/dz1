import random




# Функция для перемешивания букв в слове    
def shuffle_word(input_word):  # Принимает слово, которое нужно перемешать
    # Преобразуем слово в список букв, чтобы можно было их перемешать
    word_letters = list(input_word)   
    # Используем функцию shuffle из модуля random для случайного перемешивания букв
    random.shuffle(word_letters)  
    # Собираем перемешанные буквы обратно в слово методом join
    mixed_word = ''.join(word_letters)  
    # Возвращаем перемешанное слово
    return mixed_word  

# Функция для получения имени игрока
def get_user_name():
    # Выводим приглашение ввести имя
    print("Введите ваше имя:") 
    # Получаем имя от пользователя через консоль
    name = input() 
    # Возвращаем введенное имя
    return name

# Функция для чтения слов из файла
def read_words():
    # Открываем файл words.txt для чтения в кодировке utf-8
    with open('words.txt', 'r', encoding='utf-8') as file:
        # Создаем пустой список для хранения слов
        words = [] 
        # Читаем файл построчно
        for line in file:
            # Добавляем каждое слово в список, удаляя лишние пробелы
            words.append(line.strip())
        # Возвращаем заполненный список слов
        return words 
def read_history():
    # Open history file to read scores
    with open('history.txt', 'r', encoding='utf-8') as file: # Открыла файл для чтения 
        scores = [] # создаем  списко результатов
        for line in file: # для каждой линии в файле.
            name, score = line.strip().split(':')
            scores.append((name, int(score))) 
    return scores

# Функция для записи результатов игрока в файл истории
# Принимает два параметра: имя игрока и его счет
def write_history(user_name, score):
    # Открываем файл history.txt в режиме добавления ('a' - append)
    # encoding='utf-8' позволяет записывать русские буквы
    with open('history.txt', 'a', encoding='utf-8') as file:
        # Записываем строку в формате "имя:счет" и добавляем перенос строки \n
        
        file.write(f'{user_name}:{score}\n')
    # Функция ничего не возвращает (можно убрать return None)
    return None



# Основная игровая функция
def play_game(words_list, user_name):
    # Счетчик очков игрока
    count = 0
    # Перебираем каждое слово из списка
    for word in words_list:
        # Получаем перемешанный вариант текущего слова
        mixed_word = shuffle_word(word)
        # Показываем игроку перемешанное слово
        print(f'Угадай слово {mixed_word}')
        # Получаем ответ игрока
        answer = input()
        # Сравниваем ответ с правильным словом (игнорируя регистр)
        if answer.lower() == word.lower():
            # Если угадал - поздравляем и начисляем очки
            print(f'Слово угадано! +10 очков {user_name}')
            count += 10
        else:
            # Если не угадал - показываем правильный ответ
            print(f"Неверно. Правильный ответ: {word}")
    # Возвращаем финальный счет
    return count


def get_statistics():
    try:
        with open('history.txt', 'r', encoding='utf-8') as file:
            scores = [] # cохраняем результат для того что бы читать
            for line in file:
                # Проверяем, что строка не пустая   
                if ':' in line:  # проверка на наличие символа ':' в строке
                    try:
                        sum_game = line.strip().split(':')  
                        scores.append((sum_game[0], int(sum_game[1])))
                    except (IndexError, ValueError):
                        continue
            total_games = len(scores) 
            max_score = max(score[1] for score in scores) if scores else 0
              
            return total_games, max_score 
    except FileNotFoundError:
        return 0, 0
            
            
# Основной код программы:

# Получаем имя игрока
user_name = get_user_name()
# Приветствуем игрока
print(f'привет {user_name} давайте поиграем!')

# Загружаем список слов из файла
words_list = read_words()
# Показываем загруженные слова

# Запускаем игру и сохраняем результат
final_count = play_game(words_list, user_name)
# Выводим финальный счет игрока
# Вызываем функцию записи истории, передавая имя игрока и его финальный счет
write_history(user_name, final_count)
print(f'Имя Игрока {user_name} счет {final_count}')

# Получаем и выводим статистику
total_games, max_score = get_statistics()
print(f'\nВсего игр сыграно: {total_games + 1}')  # +1 для учета текущей игры
print(f'Максимальный рекорд: {max(max_score, final_count)}')  # учитываем текущий результат


    

