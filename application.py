import tkinter as tk
import requests
import time
from PIL import ImageTk, Image

def getweather(canvas):
    city=entry1.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=63e47eafe5df1dd993b360b69c16871d"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-21600))
    sunset =time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']-21600))
    final_info=condition +"\n"+str(temp)+"c"
    final_data="\n"+"Max Temp: "+str(max_temp)+"\n"+"Min Temp: "+str(min_temp)+"\n"+"\n"+"Pressure: "+str(pressure)+"\n"+"Humidity: "+str(humidity)+"\n"+"Wind: "+str(wind)+"\n"+"\n"+"Sunrise: "+sunrise+"\n"+"Sunset: "+sunset

    design="\n"+"@AMIT"
    label1.config(text=final_info)
    label2.config(text=final_data)
    label3.config(text=design,justify="left")

root=tk.Tk()
root.geometry("500x600")
root.configure(bg='#7CB9E8')

root.title("mosam ki jankari")

font_1=("poppins",20,"bold",)
font_2=("poppins",30,"bold")
font_3=("bison",10,"bold","italic")


entry1=tk.Entry(root,font=font_2,highlightthickness=8,bg="#7CB9E8",fg="#FFFDD0")
entry1.config(highlightcolor="#777B7E")
entry1.pack(pady=20)
entry1.focus()
entry1.bind('<Return>',getweather)

label1=tk.Label(root,font=font_2,bg="#7CB9E8",fg="#FFFDD0")
label1.pack()
label2=tk.Label(root,font=font_1,bg="#7CB9E8",fg="#FFFDD0")
label2.pack()
label3=tk.Label(root,font=font_3,bg="#7CB9E8",fg="#FFFDD0",anchor='w')
label3.pack()
root.mainloop()
