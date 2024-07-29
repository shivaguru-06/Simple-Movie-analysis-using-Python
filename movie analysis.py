import pandas as pd
import matplotlib.pyplot as plt
kollywood={"Movie_Name":["Kushi","Allai","Annathe","Vettaikaran","Kadhal Kottai","Enthiran","PooveUnakkagha","Kadhal Mannan","Kaala","Ghilli","Amarkalam","Paadaiyappa","Their","Vaali","Mannan","Thirupachi","Kandukonden Kandukonden","Chandramukhi","Mersal","Dheena","Muthu","Master","Citizen","Arunachalam","Kaththi","Villan","Annamalai","Sivakasi","Billa","Padikadhavan"],
'Hero Name':["Vijay","Ajith","Rajini","Vijay","Ajith","Rajini","Vijay","Ajith","Rajini","Vijay","Ajith","Rajini","Vijay","Ajith","Rajini","Vijay","Ajith","Rajini","Vijay","Ajith","Rajini","Vijay","Ajith","Rajini","Vijay","Ajith","Rajini","Vijay","Ajith","Rajini"]}
user={'gener':["Romance","Romance","Action","Action","Romance","Scifi","Romance","Romance","Drama","Action","Romance","Romance","Thriller","Thriller","Romance","Action","Romance","Horror","Action","Romance","Musical","Thriller","Thriller","Comedy","Action","Sentimental","Drama","Action","Gangster","Drama"],
'Heroine Name':['Jothika','Yamuna','Nayanthara','Anushka','Devayani','Iswrya Rai','Sangetha Madhavan','Radhika','Maanu','Trisha','Shalini','RamyaKrishanan','Samantha','Simran','Viyashanthi','Trisha','Iswarya Rai','Jothika','Kajal','Laila','Meena','Malavika Mohanan','Meena','Soundarya','Samnatha','Meena','Kushbu','Asin','Nayantharan','Ambhika'],
"Director Name":['SJ Surya','Vasanth','Siva','Babu Sivan','Agathiyan','Shankar','Rajiv Prasad','Saran','Pa Ranjith','Dharani','Saran','K SRavikumar','Atlee','SJ Surya','P Vasu','Perarasu','Suresh Menon','P Vasu','Atlle','A R Murgadoss','K S Ravikaumar','Logeshkanagajan','Saravana Subhash','Sundra C ','A R Murgadoss','K S Ravikumar','Suresh Krishana','Peraarsu','vishnuvardan','Rajshekar'],
"IMDB":[8,7.6,4.4,7,7.6,7.1,8.7,8.1,6.2,8,8,8.2,7.4,7,7.2,6.3,6,7.2,7.8,7.2,7.6,7.8,7.2,7.4,8.1,7.1,7.7,8.4,8,7.2]}
gener_df=pd.DataFrame(kollywood,index=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130])
user_df=pd.DataFrame(user,index=["kamala","srinithi","ram","kamala","sita","mithun","mala","ravi","sam",
         "kithi","charan","ravi","isai","lalitha","joesna","kamala","kithi","hari","moni","mala","madhu",
         "amru","som","mala","srinithi","lalitha","ganesh","banu","privy","leekla"])
#Details of movie
print("MOVIE ANALYSIS")
df=1
if df<5:
    print('Hello viewers')

df=int(input("Enter your choice:"))

if df==1:
    print(pd.DataFrame(kollywood))

df=int(input("Enter your choice:"))
if df==2:
    print(pd.DataFrame(user))



import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as pd

#Top IMDB rating of 10 movies
pd=1
if pd<20:
    print('Top IMDB rating of 10 movies')
    
pd=int(input("Enter your choice:"))

if pd==1:
    IMDB=[8,7.6,4.4,7,7.8,7.1,7.2,7.9,6.2,8]
    Movie_name=["Kushi","Allai","Annathe","kavalan","Mersal","Enthiran","Dheena","Master","Kaala","Ghilli"]
    plt.bar(Movie_name,IMDB,color=['red','blue','green','orange','cyan','purple','pink','yellow','grey','gold'])
    plt.ylabel("IMDB RATINGS")
    plt.xlabel("Movie_name")
    plt.title("Top IMDB rating of 10 movies")
    plt.show()

    pd=int(input("Enter your choice:"))
    

else:
    print("TO KNOW ABOUT THE HEROES DETAILS")

ch=1
if ch<18:
    

        
    print("MOVIE ANALYSIS")
 
    print(" 1. WELCOME TO MOVIE BUS")
    print(" 2. DISPLAY KOLLYWOOD MOVIES")
    print(" 3. TO FIND NO OF MOVIES ACTED BY HEROS")
    print(" 4. TO KNOW ABOUT RATING OF VIJAY MOVIES")
    print(" 5. TO KNOW ABOUT RATING OF AJITH MOVIES")
    print(" 6. TO KNOW ABOUT RATING OF RAJINI MOVIES")

ch=int(input("Enter your choice:"))
if ch==2:
    print("!!WELCOME TO MOVIE BUS!!")
    print("To know about movies name and actors")
    print("**start**")

    ch=int(input("Enter your choice:"))

#No of movies acted
    
if ch==3:
    a=['Vijay','Ajith','Rajini']
    b=[65,60,169]
    plt.plot(a,b,marker='*')
    plt.grid()
    plt.show()
    

    ch=int(input("Enter your choice:"))
    

#No of rated movies of vijay
if ch==4:    
    rating=["Blockbuster","Hit","Average","Flop"]
    no=[10,16,15,23]
    plt.pie(no,labels=rating,autopct="%5.2f%%")
    plt.title("Vijay")
    plt.show()
    

    ch=int(input("Enter your choice:"))

    
    
#No of rated movies of Ajith
    
if ch==5:
    rating=["Blockbuster","Hit","Average","Flop"]
    no=[4,9,8,25]
    plt.pie(no,labels=rating,autopct="%5.2f%%")
    plt.title("Ajith")
    plt.show()


    ch=int(input("Enter your choice:"))
    
#No of rated movies of rajini
   
if ch==6:
    rating=["Blockbuster","Hit","Average","Flop"]
    no=[19,74,50,30]
    plt.pie(no,labels=rating,autopct="%5.2f%%")
    plt.title("Rajini")
    plt.show()

    ch=int(input("Enter your choice:"))
    
if ch>6:
     print("Thankyou for watching movies")
     print("Visit again")
     print("!! HAVE A NICE DAY !!")

    
    
    
    


    













   
     
        


        
    
    
