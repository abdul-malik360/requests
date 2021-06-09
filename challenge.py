import requests
from tkinter import *
root = Tk()
root.title("Weather App")
root.geometry("550x550")
root.config(bg="#ffba08")

weather = StringVar()
cloud = StringVar()
location = StringVar()
city = StringVar()
temp = StringVar()
humid = StringVar()
wind = StringVar()
tzone = StringVar()
# label and entry for location
Label(root, text="Enter Location: ", font=50, height=5, width=25, bg="#ffba08", foreground="#03071e").place(x=20, y=20)
city_ent = Entry(root)
city_ent.place(x=100, y=100)





def check_weather():
    city_ent.get()
    params1 = {'units': 'Metric'}
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city_ent.get() +"&appid=9855a903510d5170456e11eb94f17a1b", params=params1)
    data = response.json()

    weather.set(data["weather"][0]["main"])
    cloud.set(data["weather"][0]["description"])
    location.set(data["sys"]["country"])
    temp.set(data["main"]["temp"])
    humid.set(data["main"]["humidity"])
    wind.set(data["wind"]["speed"])
    tzone.set(data["timezone"])
    temp_lab = Label(root, text="Temperature", font=30, height=2, bg="#ffba08", foreground="#03071e")
    temp_lab.place(x=20, y= 250)
    humid_lab = Label(root, text="Humidity", font=30, height=2, bg="#ffba08", foreground="#03071e")
    humid_lab.place(x=20, y= 300)
    wind_lab = Label(root, text="Wind Speed", font=30, height=2, bg="#ffba08", foreground="#03071e")
    wind_lab.place(x=20, y= 350)
    cloud_lab = Label(root, text="Cloud Cover", font=30, height=2, bg="#ffba08", foreground="#03071e")
    cloud_lab.place(x=20, y= 400)
    tzone_lab = Label(root, text="Time Zone", font=30, height=2, bg="#ffba08", foreground="#03071e")
    tzone_lab.place(x=20, y= 450)
    location_lab = Label(root, text="Country", font=30, height=2, bg="#ffba08", foreground="#03071e")
    location_lab.place(x=20, y=500)
    weather_lab = Label(root, text="Weather", font=30, height=2, bg="#ffba08", foreground="#03071e")
    weather_lab.place(x=20, y=200)

    weather_ans = Label(root, textvariable=weather, font=30, bg="#ffba08", height=2)
    weather_ans.place(x=150, y=200)
    weather_descript_ans = Label(root, textvariable=cloud, font=30, bg="#ffba08", height=2)
    weather_descript_ans.place(x=150, y=400)
    weather_location_ans = Label(root, textvariable=location, font=30, bg="#ffba08", height=2)
    weather_location_ans.place(x=150, y=500)
    weather_temp_ans = Label(root, textvariable=temp, font=30, bg="#ffba08", height=2)
    weather_temp_ans.place(x=150, y=250)
    weather_humid_ans = Label(root, textvariable=humid, font=30, bg="#ffba08", height=2)
    weather_humid_ans.place(x=150, y=300)
    weather_wind_ans = Label(root, textvariable=wind, font=30, bg="#ffba08", height=2)
    weather_wind_ans.place(x=150, y=350)
    weather_timezone_ans = Label(root, textvariable=tzone, font=30, bg="#ffba08", height=2)
    weather_timezone_ans.place(x=150, y=450)


check_btn = Button(root, command=check_weather, cursor="hand2", text="Check Weather", bg="#e85d04", font=2, foreground="#caf0f8", borderwidth=5, width=20)
check_btn.place(x=300, y=100)


def clear():
    weather.set(" ")
    cloud.set(" ")
    location.set(" ")
    temp.set(" ")
    humid.set(" ")
    wind.set(" ")
    tzone.set(" ")
    city_ent.delete(0, END)



clear_btn = Button(root, text="Clear", command=clear,  cursor="hand2", bg="#e85d04", font=2, foreground="#caf0f8", borderwidth=5)
clear_btn.place(x=390, y=250)

root.mainloop()
