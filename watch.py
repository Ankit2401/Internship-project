from cProfile import label
import tkinter as tk 
from time import strftime
from tkinter import font
import requests

root=tk.Tk()
root.title("DIGITAL CLOCK")
def get_weather(city):
    url = f"https://wttr.in/{'Agra'}?format=%t"
    try:
        response = requests.get(url)
        temperature = response.text.strip()
    except:
        temperature = "N/A"
    return temperature

def time():
    string=strftime('%H:%M:%S %p \n %D')
    temperature = get_weather("Agra") 
    label.config(text=f"{string} \nTemperature: {temperature}") 
    label.after(1000,time)

label= tk.Label(root,font=('calibri',40,'bold'),background='black',foreground='white')
label.pack(anchor='center')
time()
root.mainloop()    