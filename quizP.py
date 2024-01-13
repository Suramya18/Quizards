import mysql.connector
from prettytable import PrettyTable
from tkinter import *
import tkinter as tk
import random

r=tk.Tk()
r.geometry('410x300')
r.config(bg='white')
r.title("QUIZARDS")

heading=Label(r,text="QUIZARDS",bg="green",fg="white",font=("ariel", 20, "bold"))
heading.grid(row=0,column=1)

count=0
c=0
name=""
n=random.randint(1,75)

d={1:["Where is Meenakshi Mandir situated ?",{1:'Madurai',2:'Chennai',3:'Thanjavur',4:'Kanchipuram'},1],2:["Who is called Gaurinandan ?",{1:'Shiv',2:'Ganesh',3:'Parvati',4:'Krishna'},2],3:["Hockey's National Association is ?",{1:'NHF',2:'BCCI',3:'IHA',4:'IHF'},1],4:["Who designed the Eiffel Tower ?",{1:'Gusto Eiffel',2:'Gustave Eiffel',3:'Arthur Eiffel',4:'Gustave Hugo'},1],5:["Which is the single largest internal organ by mass in human body ?",{1:'Stomach',2:'Liver',3:'Gall Bladder',4:'Large Intestine'},2],6:["Which of these is a non renewable resource of energy ?",{1:'Fossil Fuels',2:'Solar Energy',3:'Wind Energy',4:'Geothermal Energy'},1],7:["According to the Brahmananda Purana , which of these sages was born out of the anger of Lord Shiva ?",{1:'Vishwamitra',2:'Durvasa',3:'Kashyap',4:'Bhrigu'},2],8:["Which of these Chief Justices of India also served as in Acting President of India ?",{1:'Deepak Misra',2:'Mirza Hamidullah Beg',3:'Mohammed Hidayatullah',4:'K. Subbarao'},3],9:["Widal test is used to diagnose which of the following diseases ?",{1:'Polio',2:'Typhoid',3:'Hepatitis',4:'Cholera'},2],10:["According to Mahabharata , who among these was an incarnation of Chandra Dev's son, who was sent to the earth for only 16 years ?",{1:'Abhimanyu',2:'Ghatotkacha',3:'Parikhsit',4:'Pandu'},1],11:["Which of these persons has NOT walked on the moon ?",{1:'Charles Duke',2:'James A. Lovell',3:'Alan Bean',4:'Pete Conrad'},2],12:["With which of these cards would you associate the phrase 'AAM AADMI KA ADHIKAR' ?",{1:'Pan card',2:'Voter ID card',3:'Aadhar Card',4:'Rashan card'},3],13:["Which of these words or phrases was famously used in many of his dialogues by actor Praan ?",{1:'Khamosh',2:'Barkhurdaar',3:'Jaani',4:'Babumoshai'},2],14:["The Indian National Calendar is based on ?",{1:'Chritian Era',2:'Saka Era',3:'Vikram Era',4:'Hijii Era'},2],15:["Which of the following Muslim festivals is based on The Holy Quran ?",{1:'Id-Ul-Fitr',2:'Id-Al-Adha',3:'Ramadan',4:'Mailid-Al-Nabi'},1],16:["Which of the following pairs of country and its currency is NOT correct ?",{1:'North Korea - Won',2:'Bangladesh - Taka',3:'Saudi Arabia - Rial',4:'Japan - Yuan'},4],17:["Atlantis is the name of the space shuttle launched by ?",{1:'Britain',2:'India',3:'Australia',4:'America'},4],18:["Parliament of Iran is known as ?",{1:'Congress',2:'Quami Assembly',3:'Majilis',4:'Darul Awam'},3],19:["Which of the following former Soviet Central Asian Republic is a nuclear power state ?",{1:'Uzbekistan',2:'Kazakhstan',3:'Turkmenistan',4:'Tazakistan'},2],20:["The currency of Greece is ?",{1:'Lira',2:'Peseta',3:'Drachma',4:'Krone'},3],21:["Snakes that are active in daytime generally have round pupils. What about snakes that come out at night ?",{1:'Horizontal Pupils',2:'No pupils',3:'Vertical pupils',4:'Round Pupils'},3],22:["The large flightless bird is to be found in Africa. What is it ?",{1:'Ostrich',2:'Rhea',3:'Emu',4:'Emperor Penguin'},1],23:["The fastest animal on four legs is the cheetah. How fast can it run ?",{1:'400 km/h',2:'40 km/h',3:'110 km/h',4:'200 km/h'},4],24:["Who is considered the father of the Indian films ?",{1:'Prithviraj Kapoor',2:'Dadasaheb Phalke',3:'Raj Kapoor',4:'Amitabh Bachchan'},2],25:["Which of these has not acted in Devadas ?",{1:'Aishwarya Rai',2:'Jackie Shroff',3:'Shahrukh Khan',4:'Aamir Khan'},4],26:["The title track of Chameli Ki Shaadi was sung by ?",{1:'Anil Kapoor',2:'Amrita Singh',3:'Dilip Kumar',4:'Kishore Kumar'},1],27:["In Kal Ho Na Ho whom does Shahrukh Khan pretend to be married to ?",{1:'Dalnaaz Paul',2:'Simone Singh',3:'Sonali Bendre',4:'Preeti Zinta'},3],28:["How many times can you subtract 8 from 80 ?",{1:'3',2:'2',3:'1',4:'10'},3],29:["Humans and chimpanzees share roughly how much DNA ?",{1:'98.0%',2:'98.8%',3:'92.6%',4:'96.8%'},1],30:["Which of these is not a browser ?",{1:'Firefox',2:'Chrome',3:'Internet Explorer',4:'Facebook'},4],31:["What is that one thing that cannot be seen in daylight ?",{1:'Darkness',2:'Moon',3:'Sun',4:'Smoke'},1],32:["In the film Bala what does Balmukund Shukla struggle with ?",{1:'Greying Hair',2:'Premature Ageing',3:'Memory Loss',4:'Premature Baldness'},4],33:["Which of these scientists or inventors lost their life as a consequence of their own discovery ?",{1:'Ernest Rutherford',2:'Alfred Noble',3:'Marie Curie',4:'Nicola Tesla'},3],34:["Which two seas are connected by Suez canal ?",{1:'Caspian Sea & Black Sea',2:'Red Sea & Mediterranean Sea',3:'Adriatic Sea & Red Sea',4:'North Sea & Tyrannean Sea'},2],35:["Which of these cannot be same for two different persons ?",{1:'Fingerprints',2:'Skin colour',3:'Blood Group',4:'Eye colour'},1],36:["Rama and Krishna are a variety of which plant ?",{1:'Tulsi',2:'Money Plant',3:'Neem',4:'Curry leaves Plant'},1],37:["Which colour of the spectrum has the least wavelength ?",{1:'Red',2:'White',3:'Violet',4:'Yellow'},3],38:["Which mirror is used in headlights of cars ?",{1:'Concave Mirror',2:'Reflecting Mirror',3:'Spherical Mirror',4:'Convex Mirror'},4],39:["Which is the largest country in the world ?",{1:'China',2:'USA',3:'Canada',4:'Russia'},4],40:["Which of the following Satyagraha was NOT launched by Mahatama Gandhi ?",{1:'Kheda Satyagraha',2:'Champaran Satyagraha',3:'Vykom Satyagraha',4:'Ahemedabad Satyagraha'},3],41:["What element is denoted by the chemical symbol 'Sn' in the periodic table ?",{1:'Tin',2:'Antimony',3:'Stibium',4:'Selenium'},1],42:["Who was known as the king of bollywood music ?",{1:'Kishore Kumar',2:'Sachin Dev Burman',3:'Rahul Dev Burman',4:'Mohammad Rafi'},3],43:["As of 2020 which is the only bollywood movie to win 13 filmfare awards ?",{1:'Uri:The Surgical Strike',2:'Article 15',3:'Saand Ki Aankh',4:'Gully Boy'},4],44:["Which movie has become the first bollywood film to go plastic free ?",{1:'War',2:'Dream Girl',3:'Mission Mangal',4:'Coolie No.1'},4],45:["Which of the following movies has became the first bollywood film ever to release in Saudi Arabia ?",{1:'Padman',2:'Raazi',3:'Parmanu',4:'Gold'},4],46:["Who directed Dil Chahta Hai ?",{1:'Zoya Akhtar',2:'Aamir Khan',3:'Farhan Akhtar',4:'Reema Kagti'},3],47:["Which movie is this ground breaking line from : 'Teja Main Hoon, Mark Idhar Hai' ?",{1:'Hera Pheri',2:'Welcome',3:'Maine Pyaar Kiya',4:'Andaaz Apna Apna'},4],48:["In the movie Karthik calling Karthik who was actually calling Karthik ?",{1:'Deepika Padukone',2:'Karthik',3:'Shanaya',4:'Mira'},2],49:["In 3 Idiots what is Rancho's real name ?",{1:'Ranchodas Shyamaldas Chanchhad',2:'Chatur Ramalingam',3:'Phunsuk Wangdu',4:'Veeru Sahastrabuddhi'},3],50:['Pointing to a photograph of a boy Suresh said,"He is the son of the only son of my mother." How is Suresh related to the boy ?',{1:'Brother',2:'Uncle',3:'Cousin',4:'Father'},4],51:["What is the hottest continent on earth ?",{1:'Africa',2:'Asia',3:'Antarctica',4:'Europe'},1],52:["Who among the following was the first Governor-General of new dominions of India until June 1948 ?",{1:'General Dyer',2:'Lord Mountbatten',3:'Warren Hastings',4:'Sir John Simon'},3],53:["The famous quote 'a tryst with destiny' is given by ?",{1:'Jawaharlal Nehru',2:'Mahatama Gandhi',3:'Lal Bahadur Shashtri',4:'Indira Gandhi'},1],54:["The most commonly used bleaching agent is ?",{1:'Alcohol',2:'Carbon Dioxide',3:'Chlorine',4:'Sodium Chloride'},3],55:["The main use of salt in the diet is to ?",{1:'Make the taste of food better',2:'Reduce in small amounts the hydrochloric acid required for the digestion of food',3:'Ease the process of cooking',4:'Increase the solubility of food particles in water'},2],56:["Who wrote the introduction to the English translation of Rabindranath's Gitanjali ?",{1:'William Buttler Yeats',2:'Edgar Allen Poe',3:'Walt Whitman',4:'William Blake'},1],57:["The death anniversary of which of the following leaders is observed as Martyr's Day ?",{1:'Smt. Indira Gandhi',2:'Jawaharlal Nehru',3:'Mahatama Gandhi',4:'Lal Bahadur Shashtri'},4],58:["Who is the author of the epic 'Meghdoot' ?",{1:'Vishakadutta',2:'Valmiki',3:'Banabhatta',4:'Kalidas'},4],59:["World Health Day is observed on ?",{1:'April 7',2:'March 6',3:'March 15',4:'April 28'},1],60:["Which of the following is not a dance from Kerela ?",{1:'Kathakali',2:'Mohiniattam',3:'Otten Thullal',4:'Yakshagana'},4],61:["Pongal is a popular festival of which state ?",{1:'Karnataka',2:'Kerela',3:'Tamil Nadu',4:'Andhra Pradesh'},3],62:["Rath Yatra is a famous festival at ?",{1:'Ayodhya',2:'Mathura',3:'Dwarka',4:'Puri'},4],63:["Which one of the following is essentially a solo dance ?",{1:'Kuchipudi',2:'Kathak',3:'Manipuri',4:'Mohiniattam'},4],64:["Which city of India was the first to get affected by plague ?",{1:'Jaipur',2:'Bombay',3:'Surat',4:'Kanpur'},2],65:["Dogri is spoken in which of the following states ?",{1:'Bihar',2:'Orissa',3:'Assam',4:'Jammu & Kashmir'},4],66:["The value of π(pi) was first given by ?",{1:'Bhaskara',2:'Varahamihira',3:'Aryabhatta',4:'None of these'},3],67:["The National Open University is run by ?",{1:'CBSE',2:'UGC',3:'IGNOU',4:'NCERT'},2],68:["Field Marshal is the highest rank in ?",{1:'Army',2:'Navy',3:'Air Force',4:'Territorial Army'},1],69:["Delhi became capital of India in ?",{1:'1910',2:'1911',3:'1916',4:'1923'},2],70:["Name the first Spacecraft to visit the Solar System ?",{1:'Pioneer 10 & Pioneer 11',2:'Ranger 1 & Ranger 2',3:'Surveyor 6 & Surveyor 7',4:'Viking & Viking 2'},1],71:["Name NASA's Mars Exploration Rover Mission ?",{1:'Oppurtunity Rover',2:'Spirit Rover',3:'Sojourner Rover',4:'Curiosity Rover'},2],72:["Where is the headquarter of DRDO situated ?",{1:'New Delhi',2:'Odisha',3:'Karnataka',4:'Maharashtra'},4],73:["What is the full form of PSLV?",{1:'Polar Satellite Launch Vehicle',2:'Penumbra Satellite Launch Vehicle',3:'Polar Stationary Launch Vehicle',4:'Polar Satellite Locked Vehicle'},1],74:["What is the full form of GSLV?",{1:'Geosynchronous Satellite Launch Vehicle',2:'Geosynchronous Stationary Launch Vehicle',3:'Polar Satellite Launch Vehicle',4:'Polar Satellite Launch Instrument'},1],75:["Which city is known as the home of the World's Oldest Oil paintings ?",{1:'Paris',2:'Takamatsuzuka',3:'Sulawesi',4:'Bamiyan'},4]}


def start():
    global name
    r.geometry('985x400')
    name=mystring.get()
    user.destroy()
    userE.destroy()
    st.destroy()
    global count
    lc=Label(r,text="",padx=20,pady=20,state=DISABLED,bg='white',font=("ariel", 9, "bold"))
    lc.grid(row=6,column=0,columnspan=3)

    def correct():
        global c
        c+=1
        lc.config(state=NORMAL,text="Wohoo! CORRECT")
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
    
    def wrong():
        global n
        lc.config(state=NORMAL,text="Oops! The correct answer is "+d[n][1][d[n][2]])
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)

    l=[]

    l.append(n)
    count+=1

    l1=Label(r,text=d[n][0],padx=0,pady=5,bg='black',fg='white',width=105,font=("ariel", 11, "bold"))
    l1.grid(row=1,column=0,padx=20,columnspan=3,pady=3)
    b1=Button(r,text=d[n][1][1],padx=1,pady=5,command=wrong,bg='black',fg='white',font=("ariel", 10,'bold'))
    b1.grid(row=2,column=0,columnspan=3,pady=3)
    b2=Button(r,text=d[n][1][2],padx=1,pady=5,command=wrong,bg='black',fg='white',font=("ariel", 10,'bold'))
    b2.grid(row=3,column=0,columnspan=3,pady=3)
    b3=Button(r,text=d[n][1][3],padx=1,pady=5,command=wrong,bg='black',fg='white',font=("ariel", 10,'bold'))
    b3.grid(row=4,column=0,columnspan=3,pady=3)
    b4=Button(r,text=d[n][1][4],padx=1,pady=5,command=wrong,bg='black',fg='white',font=("ariel", 10,'bold'))
    b4.grid(row=5,column=0,columnspan=3,pady=3)

    if d[n][1][1]==d[n][1][d[n][2]]:
        b1.config(command=correct)
    
    elif d[n][1][2]==d[n][1][d[n][2]]:
        b2.config(command=correct)

    elif d[n][1][3]==d[n][1][d[n][2]]:
        b3.config(command=correct)
    
    elif d[n][1][4]==d[n][1][d[n][2]]:
        b4.config(command=correct)

    def changeQ():
        global count
        global n
        count+=1
        b1.config(command=wrong,state=NORMAL)
        b2.config(command=wrong,state=NORMAL)
        b3.config(command=wrong,state=NORMAL)
        b4.config(command=wrong,state=NORMAL)
        lc.config(text='',state=DISABLED)
        n=random.randint(1,75)
        if n not in l:
            l.append(n)
            l1.config(text=d[n][0])
            b1.config(text=d[n][1][1])
            b2.config(text=d[n][1][2])
            b3.config(text=d[n][1][3])
            b4.config(text=d[n][1][4])
            if d[n][1][1]==d[n][1][d[n][2]]:
                b1.config(command=correct)
    
            elif d[n][1][2]==d[n][1][d[n][2]]:
                b2.config(command=correct)

            elif d[n][1][3]==d[n][1][d[n][2]]:
                b3.config(command=correct)
    
            elif d[n][1][4]==d[n][1][d[n][2]]:
                b4.config(command=correct)
        else:
            count-=1
            changeQ()

    def close():
        sqlI()
        leaderboard()
        r.destroy()

    
    def nextButton():
        if count<=12:
            changeQ()
        else:
            r.geometry('410x300')
            lc.destroy()
            l1.config(text='SCORE : '+str(c)+'/12',padx=5,pady=5,width=15,font=("ariel", 30, "bold"),bg='lightgreen',fg='black')
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            nextB.destroy()
            q.destroy()
            cl=Button(r,text='Close',command=close,width=10,padx=3,pady=3,activebackground='red')
            cl.grid(row=8,column=0)
        
          
    nextB=Button(r,text='Next',command=nextButton,width=20,padx=3,pady=3,activebackground='green')
    nextB.grid(row=8,column=2)

    def quitB():
        sqlI()
        leaderboard()
        r.destroy()

    q=Button(r,text='Quit',command=quitB,width=20,padx=3,pady=3,activebackground='red')
    q.grid(row=8,column=0)

def getName(e):
    print(e.widget.get())

user=Label(r,text="Enter name",padx=5,pady=5,font=("ariel", 15, "bold"))
user.grid(row=1,column=0)
mystring=tk.StringVar(r)
userE=Entry(r,textvariable=mystring,border=3,font=("ariel", 15, "bold"))
userE.grid(row=1,column=1,padx=20,pady=20)
userE.focus()
st=Button(r,text='Start',command=start,font=("ariel", 9, "bold"),activebackground='green')
st.grid(row=2,column=1,columnspan=2)

def leaderboard():
    l=[]
    mydb=mysql.connector.connect(host="localhost",user="root",password="ccdeeghnppq",database="QUIZP")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT DISTINCT(name),MAX(score) FROM PLAYERS GROUP BY name ORDER BY score DESC")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        l.append(list(x))
    table=PrettyTable(["Name","Score"])
    for rec in l:
        table.add_row(rec)
    print(table)
        


def sqlI():
    global name
    global c
    mydb=mysql.connector.connect(host="localhost",user="root",password="ccdeeghnppq",database="QUIZP")
    mycursor=mydb.cursor()
    insert_stmt=("INSERT INTO PLAYERS VALUES (%s,%s)")
    insert_data=(name.title(),c)
    try:
        mycursor.execute(insert_stmt,insert_data)
        mydb.commit()
    except:
        mydb.rollback()
    mydb.close()
    

r.mainloop()
