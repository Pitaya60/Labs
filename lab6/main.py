import tkinter as tk
from rx import operators as ops
from rx.subject import Subject
import random

# Инициализация окна Tkinter
root = tk.Tk()
root.title("FRP Animation")

# Создание холста для отображения анимации
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Создание потока событий для изменения позиции круга
position_stream = Subject() # FRP

# Функция для обновления позиции круга на холсте; FRP function
def update_position(position):
    canvas.delete("circle")  # Удаление предыдущего круга
    x, y = position
    (canvas.create_oval
     (x - 10, y - 10, x + 10, y + 10,
      fill="blue", tags="circle"))  # Создание нового круга

# Изменения данных о позиции круга; FRP
position_data = position_stream.pipe(
    ops.map(lambda _: (random.randint(50, 350),
                       random.randint(50, 350))))

# Подписка на изменение позиции и обновление круга
position_data.subscribe(update_position) # FRP

# Функция, вызываемая при клике на холсте; FRP
def on_canvas_click(event):
    position_stream.on_next(event)

# Привязка функции к событию клика на холсте
canvas.bind("<Button-1>", on_canvas_click)

# Запуск главного цикла Tkinter
root.mainloop()
