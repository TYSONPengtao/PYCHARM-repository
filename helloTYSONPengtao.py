import tkinter
top=tkinter.Tk()
top.geometry("300x450+100+100")
top.wm_title("彭涛编辑器")
main_m=tkinter.Menu(top)
item=tkinter.Menu(main_m,tearoff=0)
for  i in ["New file","Open","Open Mudule","Recent Files","Class browser","path browser"]:
    item.add_checkbutton(label=i)
item.add_separator()
for i in ["Save","save as","save copy as"]:
    item.add_radiobutton(label=i)
item.add_separator()
item.add_radiobutton(label="print window",accelerator="Ctrl+p")
item.add_separator()
item.add_radiobutton(label="close",accelerator="alt+F4")
item.add_radiobutton(label="exit",accelerator="ctrl+Q")
main_m.add_cascade(label="file",menu=item)
top["menu"]=main_m
top.mainloop()