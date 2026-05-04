import tkinter as tk
from model import SmartModel
from utils import control_device

model = SmartModel()

def run_prediction():
    try:
        time = int(entry_time.get())
        temp = int(entry_temp.get())
        motion = int(entry_motion.get())

        action = model.predict(time, temp, motion)
        result = control_device(action)

        label_result.config(text=f"{action}\n{result}")

    except Exception as e:
        label_result.config(text="Invalid Input ❌")

# GUI
root = tk.Tk()
root.title("Smart Home Automation")
root.geometry("300x300")

tk.Label(root, text="Time (0-23)").pack()
entry_time = tk.Entry(root)
entry_time.pack()

tk.Label(root, text="Temperature").pack()
entry_temp = tk.Entry(root)
entry_temp.pack()

tk.Label(root, text="Motion (0/1)").pack()
entry_motion = tk.Entry(root)
entry_motion.pack()

tk.Button(root, text="Predict", command=run_prediction).pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()