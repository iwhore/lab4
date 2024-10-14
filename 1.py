deposit = 25000  # Внесок у гривнях
ua_percent = 11.5 / 100  # Відсотки у гривнях
usd_interest = 4 / 100  # Відсотки у доларах
usd_to_ua = 27  # Початковий курс долара
future_usd_to_ua = 28.6  # Прогнозований курс через рік

# сума через рік
final_uah = deposit * (1 + ua_percent)

# переводимо
usd_deposit = deposit / usd_to_ua
final_usd_in_uah = (usd_deposit * (1 + usd_interest)) * future_usd_to_ua

if final_uah > final_usd_in_uah:
    print(f"Вигідніше зробити внесок у гривнях. Сума через рік: {final_uah:.2f} грн")
else:
    print(f"Вигідніше зробити внесок у доларах. Сума через рік: {final_usd_in_uah:.2f} грн")