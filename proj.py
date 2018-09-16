# -*- coding: utf-8 -*-

from graphviz import Digraph
from tkinter import filedialog
from tkinter import Frame
from tkinter import *
from PIL import Image
import sys
import tkinter.ttk as ttk
import tkinter as tk
import graphviz as gv
import PIL
import os
import ctypes
import networkx as nx
import matplotlib.pyplot as plt
import re
import time

class def_node:
    val=0
    succW=[]
    def __init__(self, val,succ):
        self.val=val
        self.succW=succ


def fenetre():
    root =tk.Tk()
    top = def_fenetre (root)
    root.mainloop()

class def_fenetre:
    
    g= gv.Digraph(format='png')
    gx=nx.DiGraph()
    gx1=nx.DiGraph()
    allNodes=[]
    allArcs=[]
    chemin =[]
    cout =0
    parcours = []
    a=0
    nodeObj = []
    nCible = object
    nCible1=object
    succ = []
    path = 0
    debA=""
    pathTmp=0
    visited=[]
    vist=[]
    cst=0
  
    def __init__(self, top=None):

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI Semibold} -size 9 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI Symbol} -size 9 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI Semilight} -size 9 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background= [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("555x575+451+66")
        top.title("Algorithmes de recherche")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.02, relheight=0.88, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#f1f5f5")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=535)

        self.b_visualiser = Button(self.Frame1,command=self.draw_graph)
        self.b_visualiser.place(relx=0.24, rely=0.14, height=34, width=187)
        self.b_visualiser.configure(activebackground="#d9d9d9")
        self.b_visualiser.configure(activeforeground="#000000")
        self.b_visualiser.configure(background="#f0f5f7")
        self.b_visualiser.configure(disabledforeground="#a3a3a3")
        self.b_visualiser.configure(font=font10)
        self.b_visualiser.configure(foreground="#000000")
        self.b_visualiser.configure(highlightbackground="#d9d9d9")
        self.b_visualiser.configure(highlightcolor="black")
        self.b_visualiser.configure(pady="0")
        self.b_visualiser.configure(text='''Visualiser le graphe''')

        self.champ_fileName = Entry(self.Frame1)
        self.champ_fileName.place(relx=0.43, rely=0.04, relheight=0.06
                , relwidth=0.55)
        self.champ_fileName.configure(background="white")
        self.champ_fileName.configure(disabledforeground="#a3a3a3")
        self.champ_fileName.configure(font="TkFixedFont")
        self.champ_fileName.configure(foreground="#000000")
        self.champ_fileName.configure(highlightbackground="#d9d9d9")
        self.champ_fileName.configure(highlightcolor="black")
        self.champ_fileName.configure(insertbackground="black")
        self.champ_fileName.configure(selectbackground="#c4c4c4")
        self.champ_fileName.configure(selectforeground="black")

        self.b_ajoutFichier = Button(self.Frame1,command=self.browsefunc)
        self.b_ajoutFichier.place(relx=0.04, rely=0.04, height=34, width=187)
        self.b_ajoutFichier.configure(activebackground="#d9d9d9")
        self.b_ajoutFichier.configure(activeforeground="#000000")
        self.b_ajoutFichier.configure(background="#f0f5f7")
        self.b_ajoutFichier.configure(disabledforeground="#a3a3a3")
        self.b_ajoutFichier.configure(font=font10)
        self.b_ajoutFichier.configure(foreground="#000000")
        self.b_ajoutFichier.configure(highlightbackground="#d9d9d9")
        self.b_ajoutFichier.configure(highlightcolor="black")
        self.b_ajoutFichier.configure(pady="0")
        self.b_ajoutFichier.configure(text='''Ajouter le fichier de description''')

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.04, rely=0.32, height=21, width=234)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ecf4f4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#9b0a64")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Appliquer un algorithme de recherche''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.04, rely=0.4, height=21, width=64)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ecf4f4")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#9b0a64")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Etat initial''')

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.04, rely=0.46, height=21, width=54)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ecf4f4")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font10)
        self.Label4.configure(foreground="#9b0a64")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Etat final''')

        self.Label6 = Label(self.Frame1)
        self.Label6.place(relx=0.04, rely=0.52, height=21, width=54)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#ecf4f4")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font10)
        self.Label6.configure(foreground="#9b0a64")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''limite''')

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.04, rely=0.59, height=21, width=137)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ecf4f4")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#9b0a64")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Algorithme de recherche''')

        self.entre_source = Entry(self.Frame1)
        self.entre_source.place(relx=0.19, rely=0.4, relheight=0.04,relwidth=0.08)
        self.entre_source.configure(background="white")
        self.entre_source.configure(disabledforeground="#a3a3a3")
        self.entre_source.configure(font="TkFixedFont")
        self.entre_source.configure(foreground="#000000")
        self.entre_source.configure(highlightbackground="#d9d9d9")
        self.entre_source.configure(highlightcolor="black")
        self.entre_source.configure(insertbackground="black")
        self.entre_source.configure(selectbackground="#c4c4c4")
        self.entre_source.configure(selectforeground="black")

        self.entre_end = Entry(self.Frame1)
        self.entre_end.place(relx=0.19, rely=0.46, relheight=0.04, relwidth=0.08)
        self.entre_end.configure(background="white")
        self.entre_end.configure(disabledforeground="#a3a3a3")
        self.entre_end.configure(font="TkFixedFont")
        self.entre_end.configure(foreground="#000000")
        self.entre_end.configure(highlightbackground="#d9d9d9")
        self.entre_end.configure(highlightcolor="black")
        self.entre_end.configure(insertbackground="black")
        self.entre_end.configure(selectbackground="#c4c4c4")
        self.entre_end.configure(selectforeground="black")

        self.entre_val = Entry(self.Frame1)
        self.entre_val.place(relx=0.19, rely=0.52, relheight=0.04, relwidth=0.08)
        self.entre_val.configure(background="white")
        self.entre_val.configure(disabledforeground="#a3a3a3")
        self.entre_val.configure(font="TkFixedFont")
        self.entre_val.configure(foreground="#000000")
        self.entre_val.configure(highlightbackground="#d9d9d9")
        self.entre_val.configure(highlightcolor="black")
        self.entre_val.configure(insertbackground="black")
        self.entre_val.configure(selectbackground="#c4c4c4")
        self.entre_val.configure(selectforeground="black")
        
        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.32, rely=0.59, relheight=0.04
                , relwidth=0.31)
        self.value_list = ["coût uniforme","En largeur d abrod","En profondeur d abord","En profondeur limitée itérative","A*","Meilleur d abord gloutonne","SMA",]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.bind("<<ComboboxSelected>>", self.choixAlgo)
        #self.TCombobox1.configure(textvariable=fenetre_support.algorithmes)
        self.TCombobox1.configure(takefocus="")

        
        self.resultat = Text(self.Frame1)
        self.resultat.grid(column=1,row=3)
        self.resultat.place(relx=0.04, rely=0.75, relheight=0.25, relwidth=0.44)
        self.resultat.configure(background="white")
        self.resultat.configure(font="TkTextFont")
        self.resultat.configure(foreground="black")
        self.resultat.configure(highlightbackground="#d9d9d9")
        self.resultat.configure(highlightcolor="black")
        self.resultat.configure(insertbackground="black")
        self.resultat.configure(selectbackground="#c4c4c4")
        self.resultat.configure(selectforeground="black")
        self.resultat.configure(undo="1")
        self.resultat.configure(width=234)
        self.resultat.configure(wrap=WORD)

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.04, rely=0.69, height=21, width=114)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#ecf4f4")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font11)
        self.Label5.configure(foreground="#9b0a64")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Résultat''')

        self.b_quitter = Button(top,command=top.destroy)
        self.b_quitter.place(relx=0.83, rely=0.92, height=34, width=67)
        self.b_quitter.configure(activebackground="#d9d9d9")
        self.b_quitter.configure(activeforeground="#000000")
        self.b_quitter.configure(background="#f0f5f7")
        self.b_quitter.configure(disabledforeground="#a3a3a3")
        self.b_quitter.configure(font=font10)
        self.b_quitter.configure(foreground="#000000")
        self.b_quitter.configure(highlightbackground="#d9d9d9")
        self.b_quitter.configure(highlightcolor="black")
        self.b_quitter.configure(pady="0")
        self.b_quitter.configure(text='''Quitter''')


    def browsefunc(self):
        filename = filedialog.askopenfilename()
        self.champ_fileName.insert(0,filename)

   

    def draw_graph(self):
        sp=[]
        self.extract_el(self.champ_fileName.get())
        for node in self.allNodes:
            self.g.node(node[0:node.index("(")],xlabel=node[node.index("(")+1:node.index(")")])
            self.gx.add_node(node)
        for arc in self.allArcs :
            sp=arc[1:-1].split(",")
            self.g.edge(sp[0],sp[1],label=sp[2])
            self.gx.add_edge(sp[0],sp[1],weight=int(sp[2]))
            
        filename = self.g.render(filename='img1')
        f = PIL.Image.open("img1.png")
        f.show()
        os.remove("img1.png")
        

    def extract_el(self,filename):
        tmp=[]
        tmp2=[]
        h=0
        sp=[]
        with open(filename, "r") as f :
            files = f.readlines()
            
        nodes=files[0]
        self.allNodes=nodes[3:-2].split(",")
        arcs=files[1]
        lArcs=arcs[3:-2]
        self.allArcs=lArcs.split(" ")

        for n in self.allNodes :
            for a in self.allArcs :
                sp=a[1:-1].split(",")
                if n[0:n.index('(')]==sp[0] : 
                    for k in self.allNodes :
                        if sp[1]==k[0:k.index('(')]:
                            h=k[k.index('=')+1:k.index(')')]
                            tmp.append((sp[1],sp[2],h))
          
                
            self.nodeObj.append(def_node(n[0],tmp))
            tmp=[]
            h=0
            
    def lenNode (self,n):
        for i in self.visited :
            print(i[0])
            if (n == i[0]) :
                return i[1]
        return 0

    def coutUniforme(self,debut,fin):
        mini=999
        val = 0

        for n in self.nodeObj :
            if n.val == debut :
                self.nCible=n
                self.parcours.append(debut)
                
        
        if len(self.nCible.succW)!=0 :
            val =self.lenNode(self.nCible.val)
            print(self.nCible.val)
            for i in self.nCible.succW :
                print(i)
                self.succ.append((i[0],int(i[1])+val ))


        for s in self.succ :
            print("les succ sont :")
            print(s)
            if int(s[1])< mini :
                mini = int(s[1])
                resultat = (s[0],s[1])
        print(resultat)
        print("resultat")
        print(resultat[0])
        self.visited.append(resultat)
                  
        self.succ.remove(resultat)
        if (resultat[0] == fin) :
            print("finn")
            self.chemin=nx.shortest_path(self.gx,self.debA,fin)
            self.cout=resultat[1]
            self.parcours.append(resultat[0])
        else :
            self.coutUniforme(resultat[0],fin)
        
    
                    
    def dfs_algo (self,debut,fin):
        parcours=list(nx.dfs_preorder_nodes(self.gx,debut))
        if fin in parcours:
            self.parcours=parcours[:parcours.index(fin)+1]
            self.chemin=nx.shortest_path(self.gx,debut,fin,1)
            self.cout=self.calcChemin(self.chemin)
            
    def bfs_algo (self,debut,fin):
        listbfs=list(nx.bfs_edges(self.gx,debut))
        nodeBfs = []
        nodeBfs.append((listbfs[0])[0])
        for c in listbfs :
            nodeBfs.append(c[1])
        print (nodeBfs)
        if fin in nodeBfs :
            self.parcours=nodeBfs[:nodeBfs.index(fin)+1]
            self.chemin=nx.shortest_path(self.gx,debut,fin,1)
            self.cout=self.calcChemin(self.chemin)

    def lenNodeA (self,n):
        for i in self.visited :
            if i[0] == n :
                for j in self.vist :
                    if i[0]==j[0]:
                        return j[1]
        return 0
            
            
    def aEtoile (self,debut,fin):
        val = 0
        mini=999
        rm=[]

        for n in self.nodeObj :
            if n.val == debut :
                self.nCible=n
                self.parcours.append(debut)
                
        if len(self.nCible.succW)!=0 :
            val =self.lenNodeA(self.nCible.val)
            for i in self.nCible.succW :
                self.succ.append((i[0],int(i[1])+int(i[2])+val))
                self.vist.append((i[0],int(i[1])+val))
        for s in self.succ :
            print(s)
            if int(s[1])< mini :
                mini = int(s[1])
                resultat = (s[0],s[1])
                
        self.visited.append(resultat)
        for t in self.succ :
            if resultat[0]==t[0] :
                rm.append(t)
            if t[0] in self.parcours :
                rm.append(t)
        self.succ = [x for x in self.succ if x not in rm]
        #self.succ.remove(resultat)
      
        if (resultat[0] == fin) :
            self.chemin=nx.shortest_path(self.gx,self.debA,fin)
            self.cout=resultat[1]
            self.parcours.append(resultat[0])
            self.succ=[]
            
        else :
            self.aEtoile(resultat[0],fin)        
    
    def gloutonne (self,debut,fin):
        val = 0
        mini=999
        rm=[]

        for n in self.nodeObj :
            if n.val == debut :
                self.nCible=n
                self.parcours.append(debut)
                
        if len(self.nCible.succW)!=0 :
            for i in self.nCible.succW :
                self.succ.append((i[0],int(i[2])))
        for s in self.succ :
            print(s)
            if int(s[1])< mini :
                mini = int(s[1])
                resultat = (s[0],s[1])
        for t in self.succ :
            if resultat[0]==t[0] :
                rm.append(t)
            if t[0] in self.parcours :
                rm.append(t)
        self.succ = [x for x in self.succ if x not in rm]
      
        if (resultat[0] == fin) :
            self.chemin=nx.shortest_path(self.gx,self.debA,fin)
            self.cout=resultat[1]
            self.parcours.append(resultat[0])
            self.succ=[]
            
        else :
            self.gloutonne(resultat[0],fin)

    def calcChemin(self,listC):
        l=len(listC)
        k=0
        v=[]
        valeur=0
        print(l)
        while k < l :
            for arc in self.allArcs :
                v=arc[1:-1].split(",")
                if listC[k]==v[0] and listC[k+1]==v[1] :
                    valeur+=int(v[2])
            k=k+1

        return valeur
                    
            

    def profondeurLimité(self,debut,fin):
        limite=int(self.entre_val.get())
        v=[]
        p=[]
        tmp=[]

        while (self.cst<limite):
            if self.a ==0 :
                for n in self.nodeObj :
                    if n.val == debut :
                        self.a=1
                        self.nCible=n
                        self.succ.append(n)
                        self.gx1.add_node(n.val)
            
            for j in self.succ:
                for a in self.allArcs :
                    v=a[1:-1].split(",")
                    for k in j.succW :
                        if j.val==v[0] and k[0]==v[1]:
                            self.gx1.add_node(j.val)
                            self.gx1.add_edge(j.val,k[0])
                            print("on a ajouté ")
                            print(j.val)
                            print(k[0])
                            
            p=list(nx.dfs_preorder_nodes(self.gx1,debut))
            print(p)
            print("nouvelle liste")
            self.cst+=1
            self.parcours.extend(p)

            for ajout in self.succ :
                for suc in ajout.succW :
                    for n in self.nodeObj :
                        if suc[0]==n.val :
                            tmp.append(n)
            self.succ=tmp
                   
            if fin in self.parcours :
                print("hhh")
                self.cst=limite
                self.parcours=self.parcours[:self.parcours.index(fin)+1]
                self.chemin=nx.shortest_path(self.gx,self.debA,fin)
                self.cout=self.calcChemin(self.chemin)
                self.succ=[]
                self.gx1.clear()

            else :
                self.profondeurLimité(debut,fin)


        
    def sma(self,debut,fin):
        v=[]
        p=[]
        tmp=[]
        
        if self.a ==0 :
            for n in self.nodeObj :
                if n.val == debut :
                    self.a=1
                    self.nCible=n
                    self.succ.append(n)
                    self.gx1.add_node(n.val)
        
        for j in self.succ:
            for a in self.allArcs :
                v=a[1:-1].split(",")
                for k in j.succW :
                    if j.val==v[0] and k[0]==v[1]:
                        self.gx1.add_node(j.val)
                        self.gx1.add_edge(j.val,k[0])
                        print("on a ajouté ")
                        
        p=list(nx.dfs_preorder_nodes(self.gx1,debut))
        print(p)
        print("nouvelle liste")
    
        self.parcours.extend(p)

        for ajout in self.succ :
            for suc in ajout.succW :
                for n in self.nodeObj :
                    if suc[0]==n.val :
                        tmp.append(n)
        self.succ=tmp
                                
        if fin in self.parcours :
            print("hhh")
            self.parcours=self.parcours[:self.parcours.index(fin)+1]
            self.chemin=nx.shortest_path(self.gx,self.debA,fin)
            self.cout=self.calcChemin(self.chemin)
            self.succ=[]
            self.gx1.clear()

        else :
            self.sma(debut,fin)
                    
        
    def choixAlgo(self,event):
        algo = self.TCombobox1.get()
        s=self.entre_source.get()
        e=self.entre_end.get()

        if self.TCombobox1.get()== "En profondeur d abord":
            start_time = time.time()
            self.resultat.delete('1.0', END)
            self.cout=0
            self.dfs_algo(s,e)
            
            
        if self.TCombobox1.get()== "En largeur d abrod":
            start_time = time.time()
            self.resultat.delete('1.0', END)
            self.bfs_algo(s,e)
        if self.TCombobox1.get()== "A*":
            start_time = time.time()
            self.parcours=[]
            self.visited=[]
            self.resultat.delete('1.0', END)
            self.debA=s
            self.cout=0
            self.aEtoile(s,e)
                            
        if self.TCombobox1.get()== "coût uniforme":
            start_time = time.time()
            self.resultat.delete('1.0', END)
            self.parcours=[]
            self.visited=[]
            self.cout=0
            self.debA=s
            self.coutUniforme(s,e)

        if self.TCombobox1.get()== "SMA":
            start_time = time.time()
            self.resultat.delete('1.0', END)
            self.parcours=[]
            self.visited=[]
            self.cout=0
            self.debA=s
            self.gx1.clear()
            self.sma(s,e)
        if self.TCombobox1.get()== "En profondeur limitée itérative":
            start_time = time.time()
            self.resultat.delete('1.0', END)
            self.parcours=[]
            self.visited=[]
            self.cout=0
            self.debA=s
            self.gx1.clear()
            self.profondeurLimité(s,e)

        if self.TCombobox1.get()== "Meilleur d abord gloutonne":
            start_time = time.time()
            self.resultat.delete('1.0', END)
            self.parcours=[]
            self.visited=[]
            self.cout=0
            self.debA=s
            self.gloutonne(s,e)

                
        self.resultat.insert(END," ".join(map(str, ["Parcours :", self.parcours,'\n\n'])))
        self.resultat.insert(END," ".join(map(str, ["Chemin :", self.chemin,'\n\n'])))
        self.resultat.insert(END," ".join(map(str, ["Cout : ", self.cout,'\n\n'])))
        self.resultat.insert(END," ".join(map(str, ["Temps d'execution : ","%.4f" %(time.time() - start_time),"secondes"])))    
        ch= self.resultat.get("1.0",END)
        fich = open('algoRecherche.txt','w')
        fich.write(str(ch))
        fich.close()
        ch=""
a=fenetre()











