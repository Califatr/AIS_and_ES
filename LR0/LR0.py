# Импортировать необходимые библиотеки
import numpy as np
import matplotlib.pyplot as plt

# Задать данные о количестве продаж по 10 товарам в течение 12 месяцев (помесячно)
sales_data = np.array([
    [100, 110, 120, 105, 108, 112, 115, 118, 125, 130, 135, 140],
    [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135],
    [120, 125, 130, 140, 145, 150, 155, 160, 165, 170, 175, 180],
    [90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145],
    [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],
    [110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165],
    [95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],
    [75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130],
    [85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140],
    [105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160]
])

# Прогноз на следующий месяц (13-й месяц)
forecasted_sales = sales_data.mean(axis=1)

# Рассчитать оценку погрешности прогноза (sigma) для каждого товара
sigma = sales_data.std(axis=1)

# Определить уровень достоверности планирования для каждого товара


def reliability_level(x):
    if x < 1 * np.mean(sigma):
        return 'Красный'
    elif x < 2 * np.mean(sigma):
        return 'Желтый'
    elif x < 3 * np.mean(sigma):
        return 'Оранжевый'
    else:
        return 'Зеленый'


reliability_levels = [reliability_level(x) for x in sigma]

# Создать словарь для соответствия уровня достоверности цветам
color_mapping = {
    'Зеленый': 'g',
    'Желтый': 'y',
    'Оранжевый': 'orange',
    'Красный': 'r'
}

# Построить график продаж по месяцам
months = np.arange(1, 13)
plt.figure(figsize=(10, 6))
for i in range(10):
    plt.plot(months, sales_data[i], label=f"Товар {i + 1}")

# Визуализировать прогнозируемое значение на 13-й месяц на графиках продаж и цветом уровня достоверности
for i in range(10):
    plt.scatter(13, forecasted_sales[i], c=color_mapping[reliability_levels[i]],
                marker='o', label=f"Прогноз на 13 месяц (Товар {i + 1})")

plt.xlabel("Месяц")
plt.ylabel("Количество продаж")
plt.title("Продажи по месяцам для разных товаров с прогнозом на 13 месяц")
plt.legend()

# Создать гистограмму плана на 13-й месяц с цветом уровня достоверности
plt.figure(figsize=(10, 6))
bars = plt.bar(range(1, 11), forecasted_sales, tick_label=[
               f"Товар {i + 1}" for i in range(10)])
for i, bar in enumerate(bars):
    # Использовать цвета из словаря color_mapping
    bar.set_color(color_mapping[reliability_levels[i]])

# Визуализировать прогнозируемое значение на 13-й месяц на гистограмме плана и цветом уровня достоверности
for i in range(10):
    plt.text(
        i + 1, forecasted_sales[i], f"{forecasted_sales[i]:.2f}", ha='center', va='bottom')

plt.xlabel("Товар")
plt.ylabel("Прогноз продаж на 13 месяц")
plt.title("Прогноз продаж на 13 месяц для разных товаров с уровнем достоверности")

plt.show()
