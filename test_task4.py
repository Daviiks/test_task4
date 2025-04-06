import pandas as pd

def task1():
    s1 = pd.Series(data=['1', 2, 3.1, 'hi!', 15, -52, 12.42, 'sb', 10.1, 98], index=range(6, 26, 2))
    print('Задание №1. Выбрать элементы с индексами 8 и 14, сложить их, и из полученного результата вычесть количество целочисленных элементов (имеющих тип int), ответ сохранить в переменную s2.')
    # Выбираем элементы с индексами 8 и 14
    selected_values = s1.loc[[8, 14]]
    print(f'{selected_values}')
    # Суммируем их
    sum_selected = pd.to_numeric(selected_values, errors='coerce').sum()
    print(f'Сумма элементов c индексами 8 и 14:  {sum_selected}')
    # Подсчитываем количество целочисленных элементов (int), исходя из исходных данных их всего 4.
    int_count = sum(isinstance(x, int) for x in s1)
    print(f'Всего целочисленных элементов: {int_count}')# Для наглядности процесса
    # Вычитаем количество целых чисел из суммы
    s2 = sum_selected - int_count
    return f'При вычитании суммы элементов и количества целлочисленных элементов получилось: {s2}'  # Результат: 13.0 (или 13, если привести к int)

def task2():
    # Загрузка данных
    tr_mcc_codes = pd.read_csv('tr_mcc_codes.csv', sep='\t')
    transactions = pd.read_csv('transactions.csv', sep=',', nrows=500000)
    print('Задание №2. Проверить содержимое созданных датафреймов')
    print("tr_mcc_codes preview:")
    print(tr_mcc_codes.head())
    print("tr_mcc_codes preview:")
    print(tr_mcc_codes.tail())
    print("\ntr_mcc_codes info:")
    print(tr_mcc_codes.info())
    print("transactions preview:")
    print(transactions.head())
    print("transactions preview:")
    print(transactions.tail())
    print("\ntransactions info:")
    print(transactions.info())

def task3():
    print('Задание №3. Рассчитать медиану суммы транзакций')
    # Загрузка данных
    transactions = pd.read_csv('transactions.csv', sep=',')
    print("Столбцы в transactions:", transactions.columns.tolist())
    # Удаляются дубликаты
    transactions_dedup = transactions.drop_duplicates(subset=['mcc_code', 'tr_type'], keep='last')
    # Сортировка по amount в порядке убывания
    transactions_sorted = transactions_dedup.sort_values('amount', ascending=False)
    # Рассчет медианы
    median_amount = transactions_sorted['amount'].median()
    # Информация для наглядности
    print(f"Исходное количество строк: {len(transactions)}")
    print(f"После удаления дубликатов: {len(transactions_dedup)}")
    print(f"Первые 5 строк после сортировки:\n{transactions_sorted.head()}")
    print(f"Медиана: {median_amount}")
    
    