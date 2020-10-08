import tkinter
import webbrowser
from tkinter import *
import pyperclip
import networkx as nx  # importing networkx package
import matplotlib.pyplot as plt # importing matplotlib package and pyplot is for displaying the graph on canvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk


from analyzer import analyzer




def do_analyz():

    txt = entry.get()
    #txt = pyperclip.paste()

    information = analyzer(txt)
    agent_label=Text(agent_canvas,wrap=WORD)
    agent_label.pack(side=BOTTOM,fill=Y,expand=1)
    txt=""
    first_token_0=True




    for i in information['data']['agents']:
        if first_token_0:
            first_token_0=False
            txt+=" " +str(i)+" "
        else:
            txt+=", "+str(i)+" "
    agent_label.insert(1.0, txt)
    txt=""

    action_label = Text(action_canvas,wrap=WORD)
    action_label.pack(side=BOTTOM,fill=Y,expand=1)
    first_token_0 = True
    for i in information['data']['actions']:
        if first_token_0:
            first_token_0 = False
            txt +=" " +str(i)+" "
        else:
            txt += ", " + str(i) + " "
    action_label.insert(1.0, txt)
    txt = ""

    atribute_label = Text(atribute_canvas,wrap=WORD)
    atribute_label.pack(side=BOTTOM,fill=Y,expand=1)
    first_token_0 = True
    for i in information['data']['atribute']:
        if first_token_0:
            first_token_0 = False
            txt +=" " +str(i)+" "
        else:
            txt += ", " + str(i) + " "
    atribute_label.insert(1.0, txt)
    txt = ""

    agents = information['data']['agents']
    actions = information['data']['actions']
    atribute = information['data']['atribute']
    numb_actions = information['number']['actions']
    numb_agents= information['number']['agents']
    numb_atribute= information['number']['atribute']

    edges=[]
    action_mass=[]
    for i in range(len(agents)-1):
        for k in range(len(actions)-1):
            if len(numb_actions)>1:
                if int(numb_actions[k])<int(numb_agents[i]):
                    for j in range(len(actions)-1):
                        if int(numb_atribute[j])<int(numb_actions[k]):
                            print(1)
                            action_mass.append(actions[k-1])
                            edges.append((agents[i-1],atribute[j]))
                            actions.pop(k)
                            numb_actions.pop(k)
                            numb_agents.pop(i-1)
                            agents.pop(i-1)
                            numb_atribute.pop(j)
                            atribute.pop(j)
                            k=0
                        elif actions.index(actions[k])==0:
                            print(2)
                            action_mass.append(actions[k])
                            edges.append((agents[i - 1], atribute[j]))
                            actions.pop(k)
                            numb_actions.pop(k )
                            numb_agents.pop(i - 1)
                            agents.pop(i - 1)
                            numb_atribute.pop(j)
                            atribute.pop(j)
                            k = 0
            elif len(numb_actions)==1:
                if int(numb_actions[0])<int(numb_agents[i]):
                    for j in range(len(actions)-1):
                        if int(numb_atribute[j])<int(numb_actions[0]):
                            print(3)
                            action_mass.append(actions[0])
                            edges.append((agents[i-1],atribute[j]))
                            actions.pop(0)
                            numb_actions.pop(0)
                            numb_agents.pop(i-1)
                            agents.pop(i-1)
                            numb_atribute.pop(j)
                            atribute.pop(j)
            else:break

    edges_labels={}
    for i in range(len(edges)):
        edges_labels[edges[i]]=action_mass[i]



    f = plt.figure(figsize=(5,5),dpi=70)
    #plt.subplot(122)
    plt.tight_layout()
    canvas = FigureCanvasTkAgg(f, graph_canvas)
    canvas.draw()
    G = nx.Graph()
    G.add_edges_from(edges)
    for i in agents:
        G.add_node(i,size=80,color='b')
    pos = nx.spring_layout(G)

    nx.draw(G, pos, edge_color='black', width=1, linewidths=3,
            node_size=80, node_color='b', alpha=1,
            labels={node: node for node in G.nodes()})
    nx.draw_networkx_edge_labels(G, pos, with_labels=True, edge_labels=edges_labels,
                                 font_color='red', font_weight='bold')
    canvas.get_tk_widget().pack(side=TOP,anchor=N, fill=BOTH, expand=1)

    toolbar=NavigationToolbar2Tk(canvas,graph_canvas)
    canvas._tkcanvas.pack(side=BOTTOM,anchor=N, fill=BOTH, expand=1)









root = Tk()


root.title("")

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 900
h = h - 400
root.geometry("1800x860+{}+{}".format(w,h))


entry_canvas = Canvas(root,width=50, height=50, bg='white')
entry_canvas.pack(side=TOP,fill=X,anchor=NW, expand=0)
i=0

graph_canvas = Canvas(root,width=50, height=50, bg='white')
graph_canvas.pack(fill=BOTH,side=TOP, expand=1)

agent_canvas = Canvas(root,width=50, height=50, bg='white')
agent_canvas.pack(fill=BOTH,side=LEFT, expand=1)
agent_label = Label(agent_canvas,text="Агенти:")
agent_label.pack(side=TOP,fill=X)

action_canvas = Canvas(root,width=50, height=50, bg='white')
action_canvas.pack(fill=BOTH,side=LEFT, expand=1)
action_label = Label(action_canvas,text="Дії:")
action_label.pack(side=TOP,fill=X)

atribute_canvas = Canvas(root,width=50, height=50, bg='white')
atribute_canvas.pack(fill=BOTH,side=LEFT, expand=1)
atribute_label = Label(atribute_canvas,text="Атрібути:")
atribute_label.pack(side=TOP,fill=X)


entry_label = Label(entry_canvas,text="Введіть текст:")
entry = Entry(entry_canvas)

entry_button = Button(entry_canvas,text ="прийняти",command=do_analyz)
entry_label.pack(side=TOP,fill=BOTH, expand=1)
entry.pack(side=TOP,fill=BOTH, expand=1)
entry_button.pack(side=BOTTOM,fill=BOTH,expand=1)



root.mainloop()

