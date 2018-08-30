# from tkinter import *
#
# class Application(Frame):
#     def __init__(self,master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()
#     def createWidgets(self):
#         self.helloLabel = Label(self,text='你好,world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self,text='退出',command=self.quit)
#         self.quitButton.pack()
# app = Application()
# app.master.title('好你,World!')
# app.mainloop()

# from tkinter import *
# import tkinter.messagebox as messagebox
# class Application(Frame):
#     def __init__(self,master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton=Button(self,text='Hello',command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello,%s' % name)
#
# app = Application()
# app.master.title('好你,World!')
# app.master.geometry('200x100')
# app.mainloop()

# import tkinter as tk
# window = tk.Tk()
# window.title('Tk-Window')
# window.geometry('200x200')
#
# def insert_point():
#     var = e.get()
#     t.insert("insert",var)
#
# def insert_end():
#     var = e.get()
#     t.insert("end",var)
#
# b1 = tk.Button(window,text="insert point",width=15,height=2,command=insert_point)
# b1.pack()
# b2 = tk.Button(window,text="insert end",command=insert_end)
# b2.pack()
# e = tk.Entry(window,show='')
# e.pack()
# t = tk.Text(window,height=2)
# t.pack()

# import tkinter as tk
# window = tk.Tk()
# window.title('Tk-Window')
# window.geometry('200x200')
#
# var1 = tk.StringVar()
# l = tk.Label(window,bg='green',width=4,textvariable=var1)
# l.pack()
#
# def print_s():
#     value = lb.get(lb.curselection())
#     var1.set(value)
#
# b1 = tk.Button(window,text="print_s",width=15,height=2,command=print_s)
# b1.pack()
# var2 = tk.StringVar()
# var2.set((11,22,33,44,55))
#
# lb = tk.Listbox(window,listvariable=var2)
# list_items  = [1,2,3,4]
# for item in list_items:
#     lb.insert('end',item)
# lb.insert(1, 'first')
# lb.delete(2)
# lb.pack()

# import tkinter as tk
# window = tk.Tk()
# window.title('Tk-Window')
# window.geometry('200x200')
#
# var1 = tk.StringVar()
# l = tk.Label(window,bg='green',text='empty')
# l.pack()
#
# def print_s():
#     l.config(text='you have select ' + var1.get())
#
# r1 = tk.Radiobutton(window,text='Option A',variable=var1,value='A',command=print_s)
# r1.pack()
#
# r2 = tk.Radiobutton(window,text='Option B',variable=var1,value='B',command=print_s)
# r2.pack()
#
# r3 = tk.Radiobutton(window,text='Option C',variable=var1,value='C',command=print_s)
# r3.pack()

# import tkinter as tk
# window = tk.Tk()
# window.title('Tk-Window')
# window.geometry('500x200')
#
# #var1 = tk.StringVar()
# l = tk.Label(window,bg='green',text='empty')
# l.pack()
#
#
# def print_s(v):
#     l.config(text='you have select: ' + v)
#
#
# s = tk.Scale(window,label='try me',from_=1,to=10,orient=tk.HORIZONTAL,
#              length=500,showvalue=0,tickinterval=1,resolution=0.01,command=print_s)
# s.pack()

# import tkinter as tk
# window = tk.Tk()
# window.title('Tk-Window')
# window.geometry('500x200')
#
# l = tk.Label(window,bg='green',text='empty')
# l.pack()
#
# def print_s():
#     global var1
#     if(var1.get()==0) & (var2.get() == 0):
#         l.config(text='i not love !')
#     elif(var1.get() == 1) & (var2.get() == 1):
#         l.config(text='i both love !')
#     elif (var1.get() == 1) & (var2.get() == 0):
#         l.config(text='i love python!')
#     else:
#         l.config(text='i love C++!')
#
# var1 = tk.IntVar()
# var2 = tk.IntVar()
# c1 = tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,command=print_s)
# c2 = tk.Checkbutton(window,text='C++    ',variable=var2,onvalue=1,offvalue=0,command=print_s)
# c1.pack()
# c2.pack()

# import tkinter as tk
# window = tk.Tk()
# window.title('Tk-Window')
# window.geometry('500x500')
#
# canvas = tk.Canvas(window,bg='red')
# image_file=tk.PhotoImage(file='CMS2.PNG',width=200,height=200)
# image = canvas.create_image(100,100,anchor='nw',image=image_file)
# x0,y0,y1,y1=50,50,80,80
# line = canvas.create_line(x0,y0,y1,y1)
# oval = canvas.create_oval(x0,y0,y1,y1,fill='blue')
# arc =canvas.create_arc(x0+30,y0+30,y1+30,y1+30,start=0,extent=170) #创建一个扇形
# rect = canvas.create_rectangle(100, 30, 100+20, 30+20)   #创建一个矩形
# canvas.pack()
#
# def moveit():
#     canvas.move(rect,0,2)
#
# b = tk.Button(window,text='move',command=moveit).pack()

# import tkinter as tk
# window = tk.Tk()
# window.title('Tk-Window')
# window.geometry('500x500')
#
# l = tk.Label(window,bg='green',text='')
# l.pack()
#
# counter = 0
# def do_job():
#     global counter
#     l.config(text='do' + str(counter))
#     counter+=1
#
# menubar = tk.Menu(window)
# filemenu = tk.Menu(menubar,tearoff=0)
# menubar.add_cascade(label='File',menu=filemenu)
# filemenu.add_command(label='New',command=do_job)
# filemenu.add_command(label='Open',command=do_job)
# filemenu.add_command(label='Save',command=do_job)
# filemenu.add_separator()
# filemenu.add_command(label='Exit',command=window.quit)
#
# editmenu = tk.Menu(menubar,tearoff=0)
# menubar.add_cascade(label='Edit',menu=editmenu)
# editmenu.add_command(label='Cut',command=do_job)
# editmenu.add_command(label='Copy',command=do_job)
# editmenu.add_command(label='Paste',command=do_job)
#
# submenu = tk.Menu(filemenu)
# filemenu.add_cascade(label='Import',menu=submenu,underline=0)
# submenu.add_command(label='Submenu1',command=do_job)
#
# window.config(menu=menubar)

# import tkinter as tk
# window = tk.Tk()
# window.title('Tk-Window')
# window.geometry('300x200')
#
# tk.Label(window,bg='green',text='on the window').pack()
#
# frm = tk.Frame(window).pack()
# frm_l = tk.Frame(frm,)
# frm_r = tk.Frame(frm)
# frm_l.pack(side='left')
# frm_r.pack(side='right')
#
# tk.Label(frm_l,text='on the frm_l1').pack()
# tk.Label(frm_l,text='on the frm_l2').pack()
# tk.Label(frm_r,text='on the frm_r1').pack()

# from tkinter import messagebox
# import tkinter as tk
# window = tk.Tk()
# window.title('Tk-Window')
# window.geometry('300x200')
#
# def hit_me():
#     #tk.Messagebox.showinfo(title='Hello',message='aaoaaooooooooo')
#     tk.messagebox.showinfo(title='HI', message='Hello World')
#     tk.messagebox.showwarning(title='WR', message='warning')  # 提出警告对话窗
#     tk.messagebox.showerror(title='ER', message='404')  # 提出错误对话窗
#     tk.messagebox.askquestion(title='ask', message='yes or no')  # 询问选择对话窗
#     print(tk.messagebox.askquestion())  # 返回yes和no
#     print(tk.messagebox.askokcancel())  # 返回true和false
#     print(tk.messagebox.askyesno())  # 返回true和false
#     print(tk.messagebox.askretrycancel())  # 返回true和false
#
# tk.Button(window,text='hit me',command=hit_me).pack()


# import tkinter as tk
# window = tk.Tk()
# window.title('Tk-Window')
# window.geometry('300x200')
#
# # tk.Label(window,bg='green',text='on the window').pack(side='left')
# # tk.Label(window,bg='green',text='on the window').pack(side='right')
# # tk.Label(window,bg='green',text='on the window').pack(side='top')
# # tk.Label(window,bg='green',text='on the window').pack(side='bottom')
#
# # for i in range(4):
# #     for j in range(3):
# #         #tk.Label(window, bg='green', text='LDA').grid(row=i,column=j,ipadx=10,ipady=10)
# #         tk.Label(window, bg='green', text='LDA').grid(row=i,column=j,padx=10,pady=10)
#
# tk.Label(window, bg='green', text='LDA').place(x=10,y=100,anchor='sw')

import tkinter as tk
import pickle
from tkinter import messagebox
window = tk.Tk()
window.title('行之行-登录窗口')
window.geometry('450x300')

canvas = tk.Canvas(window,height=200,width=500)
image_file = tk.PhotoImage(file='3-01-02.gif')
image = canvas.create_image(0,0,anchor='nw',image = image_file)
canvas.pack(side='top')

tk.Label(window, text='User name:').place(x=50,y=150)
tk.Label(window, text='Password:').place(x=50,y=190)


var_usr_name = tk.StringVar()
var_usr_name.set('lda@actingtek.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb')as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo('Welcome', 'How are you? ' + usr_name)
        else:
            tk.messagebox.showerror(message='Error,your password is wrong,try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome', 'You have not sign up yet . Sign up today?')
        if is_sign_up:
            usr_sign_up()
def usr_sign_up():
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name =tk.StringVar()
    new_name.set('lda@actingtek.com')
    tk.Label(window_sign_up, text='User name:').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password:').place(x=10, y=50)
    entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_new_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm Password:').place(x=10, y=90)
    entry_new_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_new_pwd_confirm.place(x=150, y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_confirm_sign_up.place(x=150, y=130)


# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
# 定义一个`button`按钮，名为`Login`,触发命令为`usr_login`
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()
