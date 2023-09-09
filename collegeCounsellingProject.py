from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter as ttk
# importing the sqlite3 module as sql  
import sqlite3 as sql1

screen = Tk()

def reset():
    tname.set("")
    temail.set("")
    tage.set("")
    taddress.set("")

def register():
    username=tname.get()
    useremail=temail.get()
    userage=tage.get()
    useraddress=taddress.get()
    
    if(username==""):
        messagebox.showerror("STOP!!","please enter your Name")
    elif(useremail==""):
        messagebox.showerror("STOP!!"," please enter your email")
    elif(userage==""):
        messagebox.showerror("STOP!!","please enter your age")
    elif(useraddress==""):
        messagebox.showerror("STOP!!","please enter your address")
    else:
        screen2=ttk.Tk()
        screen2.title("Form")

    def reset():
        tschool_name.set("")
        tboard.set("")
        ttotal_marks.set("")
    
    def proceed():
        userschool_name=tschool_name.get()
        userboard=tboard.get()
        usertotal_marks=ttotal_marks.get()
    
        if(userschool_name==""):
            messagebox.showerror("STOP!!","please enter your school Name")
        elif(userboard==""):
            messagebox.showerror("STOP!!"," please enter your board")
        elif(usertotal_marks==""):
            messagebox.showerror("STOP!!","please enter your total marks of Intermediate")
        else:

            screen3=tk.Tk()
            screen3.title("college counselling")
            screen3.geometry("900x900")

        def per():
        
            tmarks = ttotal_marks.get()
            per=(int(tmarks)/500)*100
        
            if(per>=90):

                Label(screen3 ,text="Showing college's according to your percentage", font='cambria 20 bold',bg="purple", fg='white').pack(fill="both")
                Label(screen3 ,text="", font='cambria 3000 bold',bg="white", fg='white').pack(fill="both")

            # 1st psit
                Label(screen3 ,text='1. Pranveer Singh Institute of technology(PSIT)', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=70)
                Label(screen3 ,text='Address:-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=100)
                Label(screen3 ,text='Kanpur -Agra -delhi ,NH2, Bhauti ,Kanpur ,Uttar pradesh ,209305', font='cambria 11', fg='black',bg='white').place(x=100,y=100)
                Label(screen3 ,text='Ratings:-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=130)
                Label(screen3 ,text='8.2/10', font='cambria 11', fg='black',bg='white').place(x=100,y=130)

            # 2nd IITM   
                Label(screen3 ,text='2. Indraprashtha Institute of Technology and Management(IITM Delhi)', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=190)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=220)
                Label(screen3 ,text='d-21 ,Janakpuri Institution Area, Janakpuri, New Delhi 11058', font='cambria 11', fg='black',bg='white').place(x=100,y=220)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=250)
                Label(screen3 ,text='8.4/10', font='cambria 11', fg='black',bg='white').place(x=100,y=250)
                
            # 3rd ramswaroop
                Label(screen3 ,text='3. Shri Ramswaroop College Of Engineering and Management', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=300)
                Label(screen3 ,text='Address-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=324)
                Label(screen3 ,text='C-2/42, Service Rd, Lucknow,Uttar pradesh 226010', font='cambria 12', fg='black',bg='white').place(x=100,y=324)
                Label(screen3 ,text='Ratings-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=348)
                Label(screen3 ,text='8/10', font='cambria 12', fg='black',bg='white').place(x=100,y=348)

            # 4th babu_banarsi
                Label(screen3 ,text='4. Babu Banarsi Das University, Lucknow', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=405)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=435)
                Label(screen3 ,text='111, Faizabad Rd, Atif Vihar, Lucknow, Uttar pradesh 226028', font='cambria 11', fg='black',bg='white').place(x=100,y=435)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=465)
                Label(screen3 ,text='7.8/10', font='cambria 11', fg='black',bg='white').place(x=100,y=465)

            # 5th kanapur institute
                Label(screen3 ,text='5. Kanpur Institute of Technology', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=530)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=560)
                Label(screen3 ,text='A1, UPSIDC Industrial Area, Chakeri Ward, Rooma, Uttar Pradesh 208001', font='cambria 11', fg='black',bg='white').place(x=100,y=560)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=590)
                Label(screen3 ,text='7.2/10', font='cambria 11', fg='black',bg='white').place(x=100,y=590)

            elif(per>=85):

                Label(screen3 ,text="Showing college's according to your percentage", font='cambria 20 bold',bg="purple", fg='white').pack(fill="both")
                Label(screen3 ,text="", font='cambria 3000 bold',bg="white", fg='white').pack(fill="both")

            # 2nd IITM   
                Label(screen3 ,text=' Indraprashtha Institute of Technology and Management(IITM Delhi)', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=70)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=100)
                Label(screen3 ,text='d-21 ,Janakpuri Institution Area, Janakpuri, New Delhi 131558', font='cambria 11', fg='black',bg='white').place(x=100,y=100)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=130)
                Label(screen3 ,text='8.4/10', font='cambria 11', fg='black',bg='white').place(x=100,y=130)

            # 3rd ramswaroop
                Label(screen3 ,text='Shri Ramswaroop College Of Engineering and Management', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=190)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=220)
                Label(screen3 ,text='C-2/42, Service Rd, Lucknow,Uttar pradesh 226010', font='cambria 12', fg='black',bg='white').place(x=100,y=220)
                Label(screen3 ,text='Ratings-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=250)
                Label(screen3 ,text='8/10', font='cambria 12', fg='black',bg='white').place(x=100,y=250)

            # 4th babu_banarsi
                Label(screen3 ,text='Babu Banarsi Das University, Lucknow', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=300)
                Label(screen3 ,text='Address-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=324)
                Label(screen3 ,text='111, Faizabad Rd, Atif Vihar, Lucknow, Uttar pradesh 226028', font='cambria 12', fg='black',bg='white').place(x=100,y=324)
                Label(screen3 ,text='Ratings-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=348)
                Label(screen3 ,text='7.8/10', font='cambria 12', fg='black',bg='white').place(x=100,y=348)

            # 5th kanapur institute
                Label(screen3 ,text='Kanpur Institute of Technology', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=300)
                Label(screen3 ,text='Address-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=324)
                Label(screen3 ,text='A1, UPSIDC Industrial Area, Chakeri Ward, Rooma, Uttar Pradesh 208001', font='cambria 12', fg='black',bg='white').place(x=100,y=324)
                Label(screen3 ,text='Ratings-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=465)
                Label(screen3 ,text='7.2/10', font='cambria 12', fg='black',bg='white').place(x=100,y=465)

            # 6th csjmu
                Label(screen3 ,text='Chhatrapati Shahu Ji Maharaj University(CSJMU)', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=530)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black').place(x=300,y=560)
                Label(screen3 ,text='F7W8+QM7, Kanpur University, Kanpur, Uttar Pradesh 208024', font='cambria 11', fg='black').place(x=100,y=560)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black').place(x=30,y=590)
                Label(screen3 ,text='7/10', font='cambria 11', fg='black').place(x=100,y=590)

            elif(per>=80):

                Label(screen3 ,text="Showing college's according to your percentage", font='cambria 20 bold',bg="purple", fg='white').pack(fill="both")
                Label(screen3 ,text="", font='cambria 3000 bold',bg="white", fg='white').pack(fill="both")

            # 3rd ramswaroop
                Label(screen3 ,text='Shri Ramswaroop College Of Engineering and Management', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=70)
                Label(screen3 ,text='Address-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=100)
                Label(screen3 ,text='C-2/42, Service Rd, Lucknow,Uttar pradesh 226010', font='cambria 12', fg='black',bg='white').place(x=100,y=100)
                Label(screen3 ,text='Ratings-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=130)
                Label(screen3 ,text='8/10', font='cambria 12', fg='black',bg='white').place(x=100,y=130)

            # 4th babu_banarsi
                Label(screen3 ,text='Babu Banarsi Das University, Lucknow', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=190)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=220)
                Label(screen3 ,text='111, Faizabad Rd, Atif Vihar, Lucknow, Uttar pradesh 226028', font='cambria 11',bg='white', fg='black').place(x=100,y=220)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=250)
                Label(screen3 ,text='7.8/10', font='cambria 11', fg='black',bg='white').place(x=100,y=250)

            # 5th kanapur institute
                Label(screen3 ,text='Kanpur Institute of Technology', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=300)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=324)
                Label(screen3 ,text='A1, UPSIDC Industrial Area, Chakeri Ward, Rooma, Uttar Pradesh 208001', font='cambria 11', fg='black',bg='white').place(x=100,y=324)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=348)
                Label(screen3 ,text='7.2/10', font='cambria 11', fg='black',bg='white').place(x=100,y=348)

            # 6th csjmu
                Label(screen3 ,text='Chhatrapati Shahu Ji Maharaj University(CSJMU)', font='cambria 15 bold', fg='black').place(x=30,y=405)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=435)
                Label(screen3 ,text='F7W8+QM7, Kanpur University, Kanpur, Uttar Pradesh 208024', font='cambria 11', fg='black',bg='white').place(x=100,y=435)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=465)
                Label(screen3 ,text='7/10', font='cambria 11', fg='black',bg='white').place(x=100,y=465)

            # 7th ramaa
                Label(screen3 ,text='Rama University', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=530)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=560)
                Label(screen3 ,text='Mandhana, kanpur, uttar pradesh 209217', font='cambria 11', fg='black',bg='white').place(x=100,y=560)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=590)
                Label(screen3 ,text='7/10', font='cambria 11', fg='black',bg='white').place(x=100,y=590)

            elif(per>=70):

                Label(screen3 ,text="Showing college's according to your percentage", font='cambria 20 bold',bg="purple", fg='white').pack(fill="both")
                Label(screen3 ,text="", font='cambria 3000 bold',bg="white", fg='white').pack(fill="both")

            # 4th babu_banarsi
                Label(screen3 ,text='Babu Banarsi Das University, Lucknow', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=70)
                Label(screen3 ,text='Address-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=100)
                Label(screen3 ,text='111, Faizabad Rd, Atif Vihar, Lucknow, Uttar pradesh 226028', font='cambria 12', fg='black',bg='white').place(x=100,y=100)
                Label(screen3 ,text='Ratings-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=130)
                Label(screen3 ,text='7.8/10', font='cambria 12', fg='black',bg='white').place(x=100,y=130)

            # 5th kanapur institute
                Label(screen3 ,text='Kanpur Institute of Technology', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=190)
                Label(screen3 ,text='Address-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=220)
                Label(screen3 ,text='A1, UPSIDC Industrial Area, Chakeri Ward, Rooma, Uttar Pradesh 208001', font='cambria 12', fg='black',bg='white').place(x=100,y=220)
                Label(screen3 ,text='Ratings-', font='cambria 12 bold', fg='black',bg='white').place(x=30,y=250)
                Label(screen3 ,text='7.2/10', font='cambria 12', fg='black',bg='white').place(x=100,y=250)

            # 6th csjmu
                Label(screen3 ,text='Chhatrapati Shahu Ji Maharaj University(CSJMU)', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=300)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=324)
                Label(screen3 ,text='F7W8+QM7, Kanpur University, Kanpur, Uttar Pradesh 208024', font='cambria 11', fg='black',bg='white').place(x=100,y=324)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=348)
                Label(screen3 ,text='7/10', font='cambria 11', fg='black',bg='white').place(x=100,y=348)

            # 7th ramaa
                Label(screen3 ,text='Rama University', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=405)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=435)
                Label(screen3 ,text='Mandhana, kanpur, uttar pradesh 209217', font='cambria 11', fg='black',bg='white').place(x=100,y=435)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=465)
                Label(screen3 ,text='7/10', font='cambria 11', fg='black',bg='white').place(x=100,y=465)

            # 8th maharana
                Label(screen3 ,text='Maharana Pratap Engineering College', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=530)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=560)
                Label(screen3 ,text='Mandhana,Kothi, kanpur, uttar pradesh 209217', font='cambria 11', fg='black',bg='white').place(x=100,y=560)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=590)
                Label(screen3 ,text='7/10', font='cambria 11', fg='black',bg='white').place(x=100,y=590)

            elif(per>=60):

                Label(screen3 ,text="Showing college's according to your percentage", font='cambria 20 bold',bg="purple", fg='white').pack(fill="both")
                Label(screen3 ,text="", font='cambria 3000 bold',bg="white", fg='white').pack(fill="both")

            # 5th kanapur institute
                Label(screen3 ,text='Kanpur Institute of Technology', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=70)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=100)
                Label(screen3 ,text='A1, UPSIDC Industrial Area, Chakeri Ward, Rooma, Uttar Pradesh 208001', font='cambria 11',bg='white', fg='black').place(x=100,y=100)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=130)
                Label(screen3 ,text='7.2/10', font='cambria 11', fg='black',bg='white').place(x=100,y=130)

            # 6th csjmu
                Label(screen3 ,text='Chhatrapati Shahu Ji Maharaj University(CSJMU)', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=190)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=220)
                Label(screen3 ,text='F7W8+QM7, Kanpur University, Kanpur, Uttar Pradesh 208024', font='cambria 11', fg='black',bg='white').place(x=100,y=220)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=250)
                Label(screen3 ,text='7/10', font='cambria 11', fg='black',bg='white').place(x=100,y=250)

            # 7th ramaa
                Label(screen3 ,text='Rama University', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=300)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=324)
                Label(screen3 ,text='Mandhana, kanpur, uttar pradesh 209217', font='cambria 11', fg='black',bg='white').place(x=100,y=324)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=348)
                Label(screen3 ,text='7/10', font='cambria 11', fg='black',bg='white').place(x=100,y=348)

            # 8th maharana
                Label(screen3 ,text='Maharana Pratap Engineering College', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=405)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=435)
                Label(screen3 ,text='Mandhana,Kothi, kanpur, uttar pradesh 209217', font='cambria 11', fg='black',bg='white').place(x=100,y=435)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=465)
                Label(screen3 ,text='7/10', font='cambria 11', fg='black',bg='white').place(x=100,y=465)

            # 9th naraina
                Label(screen3 ,text=' Naraina Group Of Institution', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=530)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=560)
                Label(screen3 ,text='Ganga ganj, panki Kanpur,0208020', font='cambria 11', fg='black',bg='white').place(x=100,y=560)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=590)
                Label(screen3 ,text='6.1/10', font='cambria 11', fg='black',bg='white').place(x=100,y=590)

            elif(per>=50):
                
            # 6th csjmu
                Label(screen3 ,text='Chhatrapati Shahu Ji Maharaj University(CSJMU)', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=190)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=220)
                Label(screen3 ,text='F7W8+QM7, Kanpur University, Kanpur, Uttar Pradesh 208024', font='cambria 11', fg='black',bg='white').place(x=100,y=220)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=250)
                Label(screen3 ,text='7/10', font='cambria 11', fg='black',bg='white').place(x=100,y=250)

            # 7th ramaa
                Label(screen3 ,text='Rama University', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=300)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=324)
                Label(screen3 ,text='Mandhana, kanpur, uttar pradesh 209217', font='cambria 11', fg='black',bg='white').place(x=100,y=324)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=348)
                Label(screen3 ,text='7/10', font='cambria 11', fg='black',bg='white').place(x=100,y=348)

            # 8th maharana
                Label(screen3 ,text='Maharana Pratap Engineering College', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=405)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=435)
                Label(screen3 ,text='Mandhana,Kothi, kanpur, uttar pradesh 209217', font='cambria 11', fg='black',bg='white').place(x=100,y=435)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=465)
                Label(screen3 ,text='7/10', font='cambria 11', fg='black',bg='white').place(x=100,y=465)

            # 9th naraina
                Label(screen3 ,text='Naraina Group Of Institution', font='cambria 15 bold', fg='black',bg='white').place(x=30,y=530)
                Label(screen3 ,text='Address-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=560)
                Label(screen3 ,text='Ganga ganj, panki Kanpur,0208020', font='cambria 11', fg='black',bg='white').place(x=100,y=560)
                Label(screen3 ,text='Ratings-', font='cambria 11 bold', fg='black',bg='white').place(x=30,y=590)
                Label(screen3 ,text='6.1/10', font='cambria 11', fg='black',bg='white').place(x=100,y=590)

            # 10th Azad_institute
                Label(screen3 ,text='Azad Institute of Engineering and Technology', font='cambria 15 bold', fg='black').place(x=30,y=70)
                Label(screen3 ,text='Address-', font='cambria 12 bold', fg='black').place(x=30,y=315)
                Label(screen3 ,text='Bijnor Road Chandrawal, Via Bangla Bazar Road,near CRPF CAMP,Azad Puram, Lucknow, Uttar Pradesh 226002', font='cambria 12', fg='black').place(x=100,y=315)
                Label(screen3 ,text='Ratings-', font='cambria 12 bold', fg='black').place(x=30,y=130)
                Label(screen3 ,text='5.8/10', font='cambria 12', fg='black').place(x=100,y=590)
                
            else:
                Label(screen3 ,text='', font='cambria 2000', fg='black',bg='white').pack(fill='both')
                Label(screen3 ,text='SORRY..!!', font='cambria 20 bold', fg='black',bg='white').place(x=10,y=50)
                Label(screen3 ,text=' You are not eligible for any college', font='cambria 20 bold', fg='black',bg='white').place(x=80,y=80)

            Button(screen3, text="   Exit   ", font='cambria 14 bold',bg='ivory',fg='black', bd=2,command=screen3.destroy).place(x=800,y=530)
     
            
        per()

        screen2.destroy()
        #mainloop()

    def choose(value):
        Label(screen, text=value)
        label.pack()

#textbox
    global tschool_name    
    tschool_name= tk.StringVar(screen2)
    tboard=tk.StringVar(screen2)
    ttotal_marks=tk.IntVar(screen2)

    screen2.geometry("600x400")


    Label(screen2,text="Enter your detail's same as class 12th report card:", font="cambria 18 bold", bg='purple',fg='white').pack(fill="both")
    Label(screen2,text="", font="cambria 1000 bold", bg='lavender',fg='lavender').pack(fill="both")

#label
    Label(screen2, text='School Name', font='cambria 15 bold',bg='lavender').place(x=40,y=70)
    Label(screen2, text='Board', font='cambria 15 bold',bg='lavender').place(x=40,y=120)
    Label(screen2, text='Stream:-', font='cambria 15 bold',bg='lavender').place(x=40,y=170)
    var= StringVar()
    var.set('PCM')
    Radiobutton(screen2, text="PCM", variable=var,font="cambria 12 bold", value="PCM",bg='lavender',command=lambda :print(var.get())).place(x=130,y=200)
    Radiobutton(screen2, text="Comm+math", variable=var,font="cambria 12 bold", value="Comm.+maths",bg='lavender',command=lambda :print(var.get())).place(x=270,y=200)


    Label(screen2, text='Total marks',bg='lavender', font='cambria 15 bold').place(x=40,y=260)

    School_Name= Entry(screen2, font='10',textvariable=tschool_name, bd=2)
    School_Name.place(x=180,y=70)
    
    Board= Entry(screen2, font='10',textvariable=tboard, bd=2)
    Board.place(x=180,y=120)

    total_marks= Entry(screen2, font='10',textvariable=ttotal_marks, bd=2)
    total_marks.place(x=180,y=260)
                          
    Button(screen2, text="Reset", font='cambria 14 bold',bg='ivory',fg='black', bd=2, command=reset).place(x=350,y=330)
    Button(screen2, text="Process", font='cambria 14 bold',bg='ivory',fg='black', bd=2, command=proceed).place(x=480,y=330)
    Button(screen2, text="Exit", font='cambria 14 bold',bg='ivory',fg='black', bd=2,command=screen2.destroy).place(x=220,y=330)

    screen.destroy()

screen.title("Registration Form")
screen.geometry("600x400")

tname=StringVar()
temail=StringVar()
tage=IntVar()
taddress=StringVar()

Label(screen ,text='WELCOME TO OUR PAGE', font='cambria 23 bold', bg='purple', fg='white').pack(fill='both')
Label(screen ,text='WE WILL FIND BEST BCA/B.TECH COLLEGE FOR YOU', font='cambria 13 bold', bg='maroon', fg='white').pack(fill='both')
Label(screen ,text='Student registration panel', font='cambria 15 bold',bg='lavender', fg='black').pack(fill='both')
Label(screen ,text="", font='cambria 1000 bold', bg='lavender', fg='white').pack(fill='both')

#label define
Label(screen, text='Name',bg='lavender', font='cambria 15 bold').place(x=40, y=130)
Label(screen, text='Email',bg='lavender', font='cambria 15 bold').place(x=40, y=180)
Label(screen, text='Age',bg='lavender', font='cambria 15 bold').place(x=40, y=230)
Label(screen, text=' Gender ', font='cambria 15 bold',bg='lavender').place(x=230,y=230)
Label(screen, text='Address',bg='lavender', font='cambria 15 bold').place(x=40, y=280)

#text box
name = Entry(screen, font='10',textvariable=tname, bd = 2)
name.place(x=140,y=130)
email = Entry(screen, font='10',textvariable=temail, bd = 2)
email.place(x=140,y=180)
age = Entry(screen, font='5',textvariable=tage,width=5, bd = 2)
age.place(x=140,y=230)
address = Entry(screen, font='5',textvariable=taddress,width=25, bd = 2)
address.place(x=140,y=280)

listgender=StringVar(screen)
lists=["Male", "Female", "Other"]
listgender.set("Your Gender")
menu = OptionMenu(screen, listgender, *lists)
menu.place(x=320,  y=230, width=100)

#button
Button(screen, text="Reset", font='cambria 14 bold',bg='ivory',fg='black', bd=2 ,command=reset).place(x=370,y=340)
Button(screen, text="Exit", font='cambria 14 bold',bg='ivory',fg='black', bd=2,command=screen.destroy).place(x=260,y=340)
Button(screen, text='Register',command=register, font='cambria 14 bold',bg='ivory',fg='black', bd=2).place(x=480, y=340)
       
mainloop()
 

