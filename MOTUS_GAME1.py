# coding=utf-8
# Créé par admin, le 29/03/2020 en Python 3.2

from random import randrange
import sqlite3
from tkinter import *  # importation du module tkinter permettant de créer des fenêtre et placer des objets
import time
def raise_frame(frame): 
    frame.tkraise()
root=Tk()
root.title('MOTUS GAME')
window=Frame(root)
login_window=Frame(root)
signup_window=Frame(root)
fenetre=Frame(root)

from tkinter.messagebox import *  # boîte de dialogue

#fenetre.title("MOTUS")  # Titre de la fenêtre
Proposition = StringVar()

lettres_trouvees = ['.', '.', '.', '.', '.', '.', '.', '.']
mot = ''
lettres_trouvees = []
coups = 0


def choix_mot():
    global lettres_trouvees

    # compléter ci-dessous

    mots = ['ACCAPARA', 'FOUIRIEZ', 'SURLIEES', 'VACILLES', 'DISSONES', 'ACTIVITE', 'IRONIQUE', 'VERDIRAI', 'INTACTES',
            'ALOURDIT', 'HUCHAMES', 'INCISIVE', 'SOUFRIEZ', 'REQUETAT',
            'TYPHLITE', 'OBVIATES', 'EMETTRAS', 'REGISTRA', 'DEBACHEZ', 'TEILLEUR', 'FAILLENT', 'DEPRISAS', 'ADONNENT',
            'AHURIRAS', 'NICKELLE', 'TAILLEES', 'SHETLAND', 'REALESER',
            'CARIIONS', 'COMBINEE', 'EPULIDES', 'FILLETTE', 'WESTERNS', 'PETUNERA', 'IMPOSIEZ', 'FLIPPENT', 'RETISSEE',
            'FILATEUR', 'GAMBETTE', 'TENEUSES', 'GRANDEUR', 'LOUFERAS',
            'PATERENT', 'BERNIONS', 'REGAGNES', 'PLUCHONS', 'BAGARRAS', 'MOCASSIN', 'MONETISA', 'PIQUIONS', 'OPOPANAX',
            'VRAIMENT', 'DESISTEZ', 'RASSASIE', 'DELASSAI', 'GROSSIER',
            'RONGERAI', 'OUTRASSE', 'LIMONAIT', 'SACCULES', 'EGRENENT', 'ZEUZERES', 'PROUVAIT', 'ENROUERA', 'LOUVATES',
            'CLAPSANT', 'ACCEPTES', 'PIFFIONS', 'TEMOIGNE', 'HULULENT',
            'EDENTANT', 'RECENTRE', 'BRIDGIEZ', 'DEFERAIS', 'DEMOLIES', 'CAPSULES', 'PARIAGES', 'EMBRELEE', 'LICTEURS',
            'DEMANDEZ', 'ASTRAKAN', 'ETRIQUAT', 'CONCILIA', 'FIGERIEZ',
            'DENIGRER', 'CACATOES', 'ENCUVERA', 'FRONCEES', 'CARRARES', 'EPAULONS', 'INNOMEES', 'PERDURAI', 'PECHERAI',
            'SUCCEDAI', 'ABHORRES', 'REIFIAIT', 'SOLIDAGE', 'LIARDERA',
            'TRACASSE', 'CENSIERS', 'DILAPIDE', 'VOUSOYEE', 'ISOLABLE', 'MOULATES', 'CAMBRIEZ', 'RANIMEES', 'DEVANCEZ',
            'REPINCES', 'ORGUEILS', 'PATISSAT', 'INSTAURE', 'DEPLOYEZ',
            'SIONISTE', 'TREPANES', 'ESSOREES', 'REPERCAS', 'RELOGEES', 'ARCONNAS', 'SURGIRAI', 'ATTRAPER', 'ENCOMBRA',
            'ARROSAIT', 'SURVOLAT', 'TROUPIER', 'PERCATES', 'REVASSES',
            'MYROXYLE', 'RECULEES', 'REFORMER', 'CLABOTER', 'AMORCAIT', 'HATERAIS', 'GAINAGES', 'PERCAGES', 'LEGUATES',
            'HERBIONS', 'RIGOLEUR', 'EXCLUAIS', 'EDULCORA', 'STRIPAGE',
            'IMMOTIVE', 'EPILAMES', 'COUDRAIE', 'ENLIGNER', 'ECOUTENT', 'RECUSERA', 'ENVOLIEZ', 'POIVRIER', 'PIVOTANT',
            'DENOTANT']

    # compléter ci-dessous
    hazard = randrange(0, len(mots))
    mot ='RECULEES'
    #mots[hazard]
    lettres_trouvees = ['.', '.', '.', '.', '.', '.', '.', '.']
    return (mot)


def code_couleur(coul, prop):
    global coups
    global mot
    lettre = StringVar()
    bgcoul = '#00F'
    bgora = '#FFA500'
    bgver = '#0F0'
    bgcol = ''
    col = 0

    for i in range(len(coul)):
        ch1=prop[0:i+1]
        ch2=mot[0:i+1]
        if (coul[i] == '1'):
            lettre =prop[i]
            bgcol = bgver
            print(bgcol)
            print(lettre)
            e = Label(fenetre, text=lettre, background=bgcol, font=(60, 40), foreground='#FFF')
            e.grid(row=coups, column=i, columnspan=1, sticky=E + W, ipadx=10, ipady=10, padx=1, pady=1)
        elif (coul[i] == '2'): #and ch1.count(prop[i])<=mot.count(prop[i])):
            lettre = prop[i]
            bgcol = bgora
            e = Label(fenetre, text=lettre, background=bgcol, font=(60, 40), foreground='#FFF')
            e.grid(row=coups, column=i, columnspan=1, sticky=E + W, ipadx=10, ipady=10, padx=1, pady=1)
        else:
            lettre = prop[i]
            bgcol = bgcoul
            e = Label(fenetre, text=lettre, background=bgcol, font=(60, 40), foreground='#FFF')
            e.grid(row=coups, column=i, columnspan=1, sticky=E + W, ipadx=10, ipady=10, padx=1, pady=1)
                 
    coups+=1
        

def placer_lettres(coups, lettres, coul):
    col = 0
    # Placer votre code ci-dessous
    """coul=position_lettres(lettres)
    code_couleur(coul, lettres)"""


    for i in range(len(lettres)):
        e = Label(fenetre, text=lettres[i], background=coul,
                  font=(60, 40), foreground='#FFF')
        e.grid(row=coups, column=i, columnspan=1, sticky=E + W, ipadx=10, ipady=10, padx=1, pady=1)
        """ col = col + 1"""

    coups = coups + 1


def position_lettres(mot_choisi):
    global lettres_trouvees
    global mot
    placement = ['.', '.', '.', '.', '.', '.', '.', '.']
    place = ''
    test = True
    # implanter votre code ci-dessous
    lettres_trouvees=['.', '.', '.', '.', '.', '.', '.', '.']
    for i in range(len(mot)):    
        test=False
        for y in range(len(mot)):
            if mot_choisi[i] == mot[y] and i == y :
                test = True
                placement[y] ='1'
                lettres_trouvees[y] = mot_choisi[i]
                print(lettres_trouvees)
    
    
    for i in range(len(mot_choisi)):

        j = 0;
        test = False
        test2 = False
        while mot_choisi[i] != mot[j] and test == False and j < len(mot_choisi) - 1:
            j += 1
            # lettres_trouvees[i] = mot_choisi[i]
            for y in range(len(mot)):
                if mot_choisi[i] == mot[y] and i == y :
                   test = True
                   #placement = placement + '1'
                   #lettres_trouvees[i] = mot_choisi[i]
                   #print(lettres_trouvees)"""
        if (mot!= mot_choisi):
            j = 0
            while mot_choisi[i] != mot[j] and  j < len(mot_choisi) - 1:
                j += 1
            if (mot_choisi[i] == mot[j] and i != j and mot.count(mot[j])>lettres_trouvees.count(mot_choisi[i]) and placement[i]=='.' ):#mot.count(mot[j])>mot_choisi[0:i+1].count(mot_choisi[i])):
                print(mot.count(mot[j]))
                lettres_trouvees[i] = mot_choisi[i]
                print(lettres_trouvees)
                
                #test2 = True
                placement[i] ='2'
            if (placement[i]=='.' ):
                placement[i] =  '3'
                #lettres_trouvees[i] = mot_choisi[i]
    #for i in range(len(mot)):    
        #test=False
        p=len(mot)
        for y in range(len(mot),0):
            p=p-1
            if(mot_choisi.count(mot_choisi[p])>mot.count(mot_choisi[p]) and placement[p]=='2'):
                """a=mot_choisi.count(mot_choisi[i])
                b=mot.count(mot_choisi[i])
                s=a-b"""
                placement[p]='3'
                """for z in range(s):
                    if(mot_choisi.count(mot_choisi[i])>mot.count(mot_choisi[i]) and placement[i]=='2'):
                        
                    for p in range(len(mot)):"""
                      
                
                
    return (placement)



def Verification():
    global mot
    global coups
    global lettre_trouvees
    global caract 
    caract=['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n','A',
            'Z','E','R','T','Y','U','I','O','P','Q','S','D','F','G','H','J','K','L','M','W','X','C','V','B','N']
    choix = Proposition.get().upper()  # récupère la proposition dans le champ entry
    
    test=False
    u=0
    while(test==False and u<8):
        if(( choix[u]  not in caract)and (u<8)):
            test=True
            #showwarning('Erreur', "le mot doit contenir des lettres")
        u+=1
    
    if len(choix) != 8:  # vérifie si le mot contien 8 lettres
        print(len(choix))
        showwarning('Erreur', "le mot ne contient pas 8 lettres")
    elif (test==True):
        showwarning('Erreur', "le mot doit contenir des lettres")
    else:
        ch= position_lettres(choix)  # récupère la position des lettres
        #print(pl)
        print(len(choix))
        print(choix)
        bgcol = ''
        pl=''
        code_couleur(ch, choix)
        #placer_lettres(coups, choix, pl)
        for t in range(len(ch)):
           pl=pl+ch[t];  
                        
        if pl == '11111111' or coups == 6:  # traitement perdu ou gagné
            if pl == '11111111':
                r = askquestion('Résultat', 'Bravo vous avez trouvé.\nVoulez-vous recommencer ?')
            else:
                placer_lettres(coups, mot, '#F00')
                r = askquestion('Résultat', 'Désolé, le mot à trouver était : ' + mot + '.\nVoulez-vous recommencer ?')

            if r == 'no':
                root.destroy()
                
            else:
                coups = 0
                mot = choix_mot()
                init_jeu()
        Proposition.set('')
    #placer_lettres(coups, choix, '#00F')



def init_jeu():

    global lettres_trouvees
    global Proposition
    global Proposition
    couleur = ('#00F')  # couleur bleue
    col = 0

    # Placer votre code ci-dessous
    for i in range(8):

        # implanter votre code ici
        for j in range(8):
            if (i < 7):
                e = Label(fenetre, text='.', background=couleur, font=(60, 40), foreground='#FFF')
                e.grid(row=i, column=j, columnspan=1, sticky=E + W, ipadx=20, ipady=10, padx=1, pady=1)
            else:
                Champ = Entry(fenetre, font=(None, 20), textvariable=Proposition)
                Champ.focus_set()
                Champ.grid(row=9, column=0, columnspan=6, pady=10, padx=10)
                Bouton = Button(fenetre, font=(None, 12), text='Valider', command=Verification)
                Bouton.grid(row=9, column=6, columnspan=2, pady=10, padx=20, sticky=E + W)





def signup():
    def signup_database():
        conn=sqlite3.connect("1.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text, password text)")
        cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
        l4=Label(signup_window,text="account created",font="times 15")
        l4.grid(row=6,column=2)
        conn.commit()
        conn.close()

    l1 = Label(signup_window, text="user name", font="times 20")
    l1.grid(row=1, column=1)
    l2 = Label(signup_window, text="user email", font="times 20")
    l2.grid(row=2, column=1)
    l3 = Label(signup_window, text="user password", font="times 20")
    l3.grid(row=3, column=1)

    name_text = StringVar()
    e1 = Entry(signup_window, textvariable=name_text)
    e1.grid(row=1,column=2)
    email_text = StringVar()
    e2 = Entry(signup_window, textvariable=email_text)
    e2.grid(row=2,column=2)
    password_text = StringVar()
    e3 = Entry(signup_window, textvariable=password_text)
    e3.grid(row=3,column=2)

    b1 = Button(signup_window, text="SignUp", width=20, command=signup_database)
    b1.grid(row=4, column=2)

    #l1.grid(row=1,column=1)

    #l2.grid(row=2,column=1)

    #l3.grid(row=3,column=1)
"""l1=Label(signup_window,text="user name",font="times 20").pack()
name_text = StringVar()
e1 = Entry(signup_window, textvariable=name_text).pack()
    #e1.grid(row=1, column=2)
l2=Label(signup_window,text="user email",font="times 20").pack()
email_text = StringVar()
e2 = Entry(signup_window, textvariable=email_text).pack()
    #e2.grid(row=2, column=2)
l3=Label(signup_window,text="user password",font="times 20").pack()
password_text = StringVar()
e3 = Entry(signup_window, textvariable=password_text).pack()
    #e3.grid(row=3, column=2)

b1 = Button(signup_window, text="signup", width=20, command=lambda:signup_database()).pack()
    #b1.grid(row=4, column=2)
"""
signup()


def login():

    # b1.grid(row=4, column=2)
    # login_window.mainloop()
    def login_database():
        conn=sqlite3.connect("1.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM test WHERE (email=? OR name=?) AND password=?",(e1.get(),e1.get(),e2.get()))
        row=cur.fetchall()
        conn.close()
        print(row)
        if row!=[]:
            #user_name=row[0][1]
            #l3.config(text="user name found with name: "+user_name)
            init_jeu()
            raise_frame(fenetre)
            
            fenetre.mainloop()
        else:
            l3.config(text="user not found ")

    l1 = Label(login_window, text="email", font="times 20")
    l1.grid(row=1, column=1)
    l2 = Label(login_window, text="password", font="times 20")
    l2.grid(row=2, column=1)
    l3 = Label(login_window, font="times 20")
    l3.grid(row=5, column=2)

    email_text = StringVar()
    e1 = Entry(login_window, textvariable=email_text)
    e1.grid(row=1, column=2)
    password_text = StringVar()
    e2 = Entry(login_window, textvariable=password_text)
    e2.grid(row=2, column=2)

    b1 = Button(login_window, text="login", width=20, command=login_database)
    b1.grid(row=4, column=2)





login()

for frame in (window, login_window,signup_window,fenetre):
    frame.grid(row=0, column=0, sticky='news')






# Programme principal
mot = ''
lettre_trouvees = []
coups = 0
Proposition = StringVar()
mot = choix_mot()
print(mot)


l1=Label(window,text="Motus Game",font="times 20").pack()
#l1.grid(row=1,column=2,columnspan=2)

b1=Button(window,text="login",width=20,command=lambda:raise_frame(login_window)).pack()
#b1.grid(row=2,column=2)

b2=Button(window,text="signup",width=20,command=lambda:raise_frame(signup_window)).pack()
#b2.grid(row=2,column=3)

raise_frame(window)

root.mainloop()

