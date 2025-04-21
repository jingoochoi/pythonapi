import tkinter as t
import requests,random
def translate(text, source="en", target="ko"):
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair={source}|{target}"
    response = requests.get(url)
    data = response.json()

    if 'responseData' in data:
        return data['responseData']['translatedText']
    else:
        return "번역 오류"
i=[17, 18, 19, 21, 22, 23, 24, 27]
n=random.choice(i)
r=requests.get(f'https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple&category={n}')
d=r.json()
q=d['results'][0]['question']
a=d['results'][0]['correct_answer']
ta=translate(q)
w=t.Tk()
w.title('quiz of trivia')
w.geometry('900x300')
w.update_idletasks()
window_width = w.winfo_width()
window_height = w.winfo_height()
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
w.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
l=t.Label(w,text=ta,cursor='hand2')
l.pack()
def click(e):
    la=t.Label(w,text=a)
    la.pack()
l.bind("<Button-1>",click)
w.mainloop()