import requests
from tkinter import *
root = Tk()
root.title("Weather App")
root.geometry("900x900")
root.config(bg="#ffba08")

weather = StringVar()
descript = StringVar()
location= StringVar()
city = StringVar()
temp = StringVar
# label and entry for location
Label(root, text="Enter Location: ", font=50, height=5, width=25, bg="#ffba08", foreground="#03071e").place(x=20, y=20)
city_ent = Entry(root)
city_ent.place(x=100, y=100)

Label(root, text="Temperature", font=30, height=2, bg="#ffba08", foreground="#03071e").place(x=20, y= 250)
Label(root, text="Humidity", font=30, height=2, bg="#ffba08", foreground="#03071e").place(x=20, y= 300)
Label(root, text="Wind Speed", font=30, height=2, bg="#ffba08", foreground="#03071e").place(x=20, y= 350)
Label(root, text="Cloud Cover", font=30, height=2, bg="#ffba08", foreground="#03071e").place(x=20, y= 400)
Label(root, text="Description", font=30, height=2, bg="#ffba08", foreground="#03071e").place(x=20, y= 450)
Label(root, text="Country", font=30, height=2, bg="#ffba08", foreground="#03071e").place(x=20, y=500)
Label(root, text="Main", font=30, height=2, bg="#ffba08", foreground="#03071e").place(x=20, y=550)
Label(root, text="Weather", font=30, height=2, bg="#ffba08", foreground="#03071e").place(x=20, y=200)

weather_ans = Label(root, textvariable=weather, font=30, bg="#ffba08", height=2).place(x=150, y=200)
weather_descript_ans = Label(root, textvariable=descript, font=30, bg="#ffba08", height=2)
weather_descript_ans.place(x=150, y=450)
weather_location_ans = Label(root, textvariable=location, font=30, bg="#ffba08", height=2)
weather_location_ans.place(x=150, y=500)
weather_temp_ans = Label(root, textvariable=temp, font=30, bg="#ffba08", height=2)
weather_temp_ans.place(x=150, y=250)


def check_weather():
    city_ent.get()
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city_ent.get() +"&appid=9855a903510d5170456e11eb94f17a1b")
    data = response.json()
    weather.set(data["weather"][0]["main"])
    descript.set(data["weather"][0]["description"])
    location.set(data["sys"]["country"])
    temp.set(data["weather"]["temp"])





check_btn = Button(root, command=check_weather, cursor="hand2", text="Check Weather", bg="#e85d04", font=2, foreground="#caf0f8", borderwidth=5, width=20)
check_btn.place(x=300, y=100)



root.mainloop()
