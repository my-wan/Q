#!/usr/bin/python3.5
import configparser,subprocess,shlex,os,pwd
import tkinter.messagebox as msg
from tkinter import *
global cfgkey
global Par

Par=""
#~ ini=os.path.dirname(os.path.realpath(sys.argv[0]))+'/Q.cfg'

ini=os.path.expanduser('~')+"/.Q/Q.cfg"

cfg=configparser.ConfigParser()
cfg.optionxform=str
cfg.read(ini)
Arg="DEFAULT"

if len(sys.argv)>1:Arg=str(sys.argv[len(sys.argv)-1])

if os.path.isfile(Arg):
	Par=" "+Arg
	Arg=os.path.splitext(Arg)[1]
elif os.path.exists(Arg):Arg="Folder"

if not cfg.has_section(Arg):Arg="Other"

def getxy():
	mx=Q.winfo_pointerx()
	my=Q.winfo_pointery()
	gx=Q.winfo_reqwidth()
	gy=Q.winfo_reqheight()
	sx=Q.winfo_screenwidth()
	sy=Q.winfo_screenheight()
	if mx>sx-gx:mx=mx-gx
	if my>sy-gy:my=my-gy
	my=my-24
	return "+"+str(mx)+"+"+str(my)
	
def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    msg.showinfo("","gdhfgdhldfhg;lghdflaghf")

def xit(x):
	sys.exit()

def popup(e):
	cfgkey=e.widget.cget("text")
	#~ mnu.post(e.x_root,event.y_root)

def doit(e):
	global cfgkey
	cfgkey=e.widget.cget("text")
	cmdl=cfg[Arg][e.widget.cget("text")]
	wdir=os.path.dirname(cmdl)
	#~ subprocess.Popen(shlex.split(cmdl))
	#if len(Par)>1:cmdl=cmdl+Par
	try:subprocess.Popen(shlex.split(cmdl))
	except OSError as err:
		msg.showinfo(pwd.getpwuid(os.getuid()).pw_name+"@"+os.uname()[1]+":~$",cmdl+"\n\n"+str(err))
	xit(x)

Q=Tk()
Q.wm_title('Q')
#~ Q.resizable(0,0)
#~ Q.attributes('-topmost',1) #,"-type","desktop")
Q.attributes("-type",'menu')

#~ msg.showinfo('',Q.attributes("-type",'desktop'))
Q.attributes("-topmost",1)
Q.bind("<FocusOut>",xit)
#~ Q.attributes(106,True,'-topmost',True)


#~ self.protocol("WM_DELETE_WINDOW", "")




#~ -alpha, -topmost, -zoomed, -fullscreen, or -type
#[types]
#--dialog
#--popup
#--desktop -- under windows
#--dock  ------ no exit
#--toolbar --- has toolbar
#--menu ----- close only toolbar
#--utility
#--utility 
#--splash --- no exit
#--dialog
#--dropdown_menu
#--popup_menu
#--tooltip
#--notification
#--combo
#--dnd
#--normal



#~ _NET_WM_WINDOW_TYPE_DESKTOP, ATOM
#~ _NET_WM_WINDOW_TYPE_DOCK, ATOM
#~ _NET_WM_WINDOW_TYPE_TOOLBAR, ATOM
#~ _NET_WM_WINDOW_TYPE_MENU, ATOM
#~ _NET_WM_WINDOW_TYPE_UTILITY, ATOM
#~ _NET_WM_WINDOW_TYPE_SPLASH, ATOM
#~ _NET_WM_WINDOW_TYPE_DIALOG, ATOM
#~ _NET_WM_WINDOW_TYPE_DROPDOWN_MENU, ATOM
#~ _NET_WM_WINDOW_TYPE_POPUP_MENU, ATOM
#~ _NET_WM_WINDOW_TYPE_TOOLTIP, ATOM
#~ _NET_WM_WINDOW_TYPE_NOTIFICATION, ATOM
#~ _NET_WM_WINDOW_TYPE_COMBO, ATOM
#~ _NET_WM_WINDOW_TYPE_DND, ATOM
#~ _NET_WM_WINDOW_TYPE_NORMAL, ATOM


#~ desktop - Allows event binding but pops up under all other windows
#~ splash - no exit

#~ notification

def isuf():
	#~ if not Q.focus_get(): xit(0)
	#~ Q.focus_get()
	#~ Q.wm_withdraw()
	#~ Q.wm_deiconify
	Q.tkraise()
	#~ print('',Q.winfo_viewable())
	#~ Q.after(2000,isuf)
	#~ after(5000,'isuf')
    #~ def focus_get(self): #Return the widget which has currently the focus in the application. Use focus_displayof to allow working with several displays. Return None if application does not have the focus."""

	#~ pass
#~ focus(self, *args): #Set focus to the first item specified in ARGS."""
	
	
	

for i,x in enumerate(cfg[Arg]):
	lbl=Label(Q,relief='ridge',text=x,bg='lightgrey',fg='black',bd=2) #.grid(row=5,column=7,sticky=W+E+N+S)
	lbl.grid(row=i+1,sticky=W+E+N+S)
	lbl.bind("<ButtonRelease-1>",lambda e,i=i:doit(e))
	lbl.bind("<Button-3>",lambda e,i=i:popup(e))
	lbl.bind("<Button-1>",lambda e,i=i:e.widget.config(bg='lightblue',relief='ridge'))
	lbl.bind("<Enter>",lambda e,i=i:e.widget.config(bg='lightblue',relief='raised'))
	lbl.bind("<Leave>",lambda e,i=i:e.widget.config(bg='lightgrey',relief='ridge'))
Q.geometry(getxy())
Q.update()
Q.geometry(getxy())
Q.wm_resizable(0,0)
#~ Q.after(3000,isuf)
Q.mainloop()

#~ sudo dpkg -i /home/john/Desktop/ocs-url_3.0.0-0ubuntu1_amd64.deb




