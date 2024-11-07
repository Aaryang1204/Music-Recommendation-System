import random
import mysql.connector as sql
con=sql.connect(host='localhost',user='root',passwd='password@#1234',database='msr')
cur=con.cursor()
def gen_song_id():
  alpha='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
  num='1234567890'
  song_id=''
  song_id_temp=[]
  id_counter=0
  while(id_counter<=6):
    song_id_temp+=random.choice(alpha)
    song_id_temp+=random.choice(num) 
    id_counter+=1
  song_id=''.join(song_id_temp)
  return song_id
  
def gen_user_id():
  alpha='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
  num='1234567890'
  user_id=''
  user_id_temp=[]
  id_counter=0
  while(id_counter<=7):
    user_id_temp+=random.choice(alpha)
    user_id_temp+=random.choice(num)
    id_counter+=1
  user_id=''.join(user_id_temp)
  return user_id

def signup_user():
  user_name=str(input("Enter your Name:"))
  user_num=int(input("Enter your Mobile Number:"))
  user_pass=str(input("Enter a Password of length 8 with alphabets and nums and symbols:"))
  while(len(user_pass)<8):
    print("Re-enter password!\n")
    user_pass=str(input("Enter a Password of length 8 with alphabets and nums and symbols:"))
  user_id=gen_user_id()
  print("Your user ID is",user_id,"and password is",user_pass)
  if con.is_connected:
    cur.execute("insert into user_info values('{}','{}','{}','{}')".format(user_id,user_name,user_num,user_pass))
    print('Entry Successful!\n')
    con.commit()
    
  
  

def login_user():
  user_id=str(input("Enter your user ID:"))
  user_pass=str(input("Enter your password:"))
  if con.is_connected:
    cur.execute("select * from user_info where user_id='{}'".format(user_id))
    passw=cur.fetchall()
    for row in passw:
        if(row[3]==user_pass):
            print("\nLogin Successful!!")
            return 0
        else:
          print("User id or password is not valid")
          return 1
          con.commit()
  
def forgot_pass_user():
  user_name=str(input("Enter Your Name:"))
  user_num=int(input("Enter Your Mobile Number:"))
  user_pass=str(input("Enter the New Password of length 8 with alphabets and nums and symbols:"))
  while(len(user_pass)<8):
    print("Re-enter password\n")
    user_pass=str(input("Enter the New Password of length 8 with alphabets and nums and symbols:"))
  if con.is_connected:
    cur.execute("select user_name,user_mob from user_info where user_name='{}'".format(user_name)) 
    name=cur.fetchall()
    for row in name:
        if(row[0]==user_name and row[1]==user_num):
            cur.execute("update user_info set user_pass='{}' where user_mob='{}'".format(user_pass,user_num))
            print("Password changed")
        else:
          print("User not found")
    return 2
    con.commit()


def mood():
  mood_list=['Happy',"Sad","Party","Motivated","Romantic","Calm"]
  print(mood_list)
  user_mood=str(input("Enter your Mood from above list:"))
  while (user_mood not in mood_list):
    print(mood_list)
    user_mood=str(input("Enter your mood from above list:"))
  recommend(user_mood)

  
def song_entry():
  n=int(input("Enter the number of songs:"))
  sgen=input("Enter mood from HAPPY,SAD,PARTY,MOTIVATION,ROMANTIC,CALM:")
  if con.is_connected:
    i=1
    while (i<=n):
        print(i,"\n")
        i=i+1
        sname=input("Enter song name:")
        sart=input("Enter song artist:")
        sid=gen_song_id()
        print("Your ID:", sid)
        cur.execute("insert into song_data(song_name,song_artist,song_genre,song_id) values('{}','{}','{}','{}')".format(sname,sart,sgen,sid))
        print('Entry Successful!\n')
        con.commit()



def user_song_data(user_id_data):    
    cur.execute("create table {} (song_id varchar(20) NOT NULL PRIMARY KEY)".format(user_id_data))
    print("Table creataed")
    cur.execute("select * from song_data")
    data=cur.fetchall()
    #print("[Song Name]\t\t\t[Song Artist]\t\t\t[Song Genre]\t\t\t[Song ID]")
    for row in data:
        print("Song Name:",row[0])
        print("\nSong Artist:",row[1])
        print("\nSong Genre:",row[2])
        print("\nSong Id:",row[3])
        print("\n\n")
      #print(row[0],row[1],row[2],row[3],sep="\t\t\t")
    print("Enter any 5 songs name from list:")
    i=1
    while(i<=5):
      i+=1
      song=input("Enter song:")
      cur.execute("select song_id from song_data where song_name like '%{}%'".format(song))
      ids=cur.fetchall()
      for row in ids:
        cur.execute("insert into {} values ('{}')".format(user_id_data,row[0]))
    print("5 songs has been entered\n\n")
    con.commit()
  

def history_input(user_id):
  h=s=p=m=r=c=0
  cur.execute("select * from {}".format(user_id))
  hist=cur.fetchall()
  for row in hist:
    cur.execute("select song_genre from song_data where song_id='{}'".format(row[0]))
    mod=cur.fetchall()
    for row1 in mod:
      
      if (row1[0]=="HAPPY"):
        h+=1
      elif(row1[0]=="SAD"):
        s+=1
      elif(row1[0]=="PARTY"):
        p+=1
      elif(row1[0]=="MOTIVATION"):
        m+=1
      elif(row1[0]=="ROMANTIC"):
        r+=1
      elif(row1[0]=="CALM"):
        c+=1
  b=max(h,s,p,m,r,c)
  if(b==h):
    mood="HAPPY"
  elif(b==s):
    mood="SAD"
  elif(b==p):
    mood="PARTY"
  elif(b==m):
    mood="MOTIVATION"
  elif(b==r):
    mood="ROMANTIC"
  elif(b==c):
    mood="CALM"
  return mood
  con.commit()

def recommend(mood):
  cur.execute("select song_name,song_artist from song_data where song_genre='{}'".format(mood))
  count=0
  print("Your mood:",mood,"\nSongs...\n")
  for i in cur:
    if (count!=4):
      print(i)
      count+=1
  con.commit()
  


def admin_login():
  admin_id=input("Enter Admin ID:")
  admin_pass=input("Enter the Password:")
  if con.is_connected:
    cur.execute("select * from admin_info where admin_id='{}'".format(admin_id))
    passw=cur.fetchall()
    for row in passw:
        if(row[1]==admin_pass):
            print("Login Sccessful")
            return 0
        else:
          print("User id or pass is not valid")
          return 1
    con.commit()

def del_song(song_id):
  cur.execute("delete from song_info where song_id={}".format(song_id))
  con.commit()
  print("Deleted")


def user_del(user_id):
  cur.execute("delete from user_info where user_id='{}'".format(user_id))
  print("Deleted")
  con.commit()


def hist_del(user_id):
  cur.execute("drop table {}".format(user_id))
  con.commit()
  print("deleted")


def new_song():
  song_entry()

def user_display():
  cur.execute("Select * from user_info")
  info=cur.fetchall()
  for row in info:
    print("\n\n")
    print("User ID:",row[0])
    print("User name:",row[1])
    print("User Mobile Number:",row[2])
    print("User Password:",row[3])
    print("\n\n")
  con.commit()


def display_song():
  cur.execute("select * from song_data")
  s_info=cur.fetchall()
  for row in s_info:
    print("Song Name:",row[0])
    print("\nSong Artist:",row[1])
    print("\nSong Genre:",row[2])
    print("\nSong Id:",row[3])
    print("\n\n")
    

def feedback(ids):
  print("Please enter your feedback:\n")
  fee=input("Enter Y, if you are satisfied with the recommendation!\nEnter N, if you are not satisfied with the recommendation!\nEnter:")
  cur.execute("insert into feedback values ('{}','{}')".format(ids,fee))
  con.commit()
  print("Feedback noted")
    










        
def main_func():
  if con.is_connected:
    print("\n\n******WELCOME TO MUSIC RECOMMENDATION SYSTEM******")
    print()
    print("SELECT YOUR ROLE \n1. For Admin \n2. For user")
    choice=int(input("Enter your choice:"))
    if(choice==1):
      al=admin_login()
      if(al==0):
        print("\n\n-------ADMIN PORTAL-------")
        print("1.User Information Display\n2.User Information Deletion\n3.User Songs History Deleteion\n4.Add New Songs\n5.Song Deletion\n6.Display Songs In Library\n")
        ac=int(input("Enter your choice:"))
        if(ac==1):
          user_display()
        elif(ac==2):
          user_id_del=input("Enter the user Id")
          user_del(user_id_del)
        elif(ac==3):
          user_hist_del=input("Enter the user ID:")
          hist_del(user_hist_del)
        elif(ac==4):
          new_song()
        elif(ac==5):
          song_id_del=input("Enter song id")
          del_song(song_id_del)
        elif(ac==6):
          display_song()
        else:
          print("Wrong input")
        ch0=input("\n\n\nEnter:\n1)Y if you want to continue\n2)N if you want to exit\n\n\n")
        while(ch0=='Y' or ch0=='y'):
            main_func()



    elif(choice==2):
      print("-------USER PORTAL-------")
      ch=int(input("Choose:\n1.For Signup\n2.For Login\n3.Forgot Password\nEnter your choice:"))
      if(ch==1):
          signup_user()
          ch0=int(input("\n\nDo you want recommendation of songs based on:\n1)Mood\n2)Songs from Library"))
          if (ch0==1):
              mood()
          elif(ch0==2):
              ids=input("\nEnter user ID:")
              user_song_data(ids)
              recommend(history_input(ids))
              feedback(ids)
          else:
              print("Wrong Input")
        
      elif(ch==2):
          au=login_user()
          if(au==1):
              exit
          else:
        
              print("\n-------LOGIN SUCCESSFUL-------\n")
              ids=input("\nEnter user ID:")
              ch0=int(input("\n\nDo you want recommendation of songs based on:\n1)Mood\n2)Songs from Library"))
              if (ch0==1):
                  mood()
              elif(ch0==2):
                  ids=input("\nEnter user ID:")
                  recommend(history_input(ids))
                  feedback(ids)
              else:
                  print("Wrong Input")
        
          

      elif(ch==3):
        fp=forgot_pass_user()
        if(fp==2):
          exit

      ch0=input("\n\n\nEnter:\n1)Y if you want to continue\n2)N if you want to exit\n\n\n")
      while(ch0=='Y' or ch0=='y'):
        main_func()
      


main_func()
















          
























      
    
