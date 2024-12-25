students = [
    ["Алина",[5,4,5]],
    ["Борис",[3,3,4]],
    ["Вика",[5,5,4]]

]
for name in students:
    for numb in name:
        for max_numb in numb:
            for min_numb in numb:

              print(f"Имя ученика:{name}.Максимальная оценка {max_numb}")




