import json
import requests
import transliterate

#Обрабатывает прежде полученые данные, и формирует из их выходной результат для передачи в AMS систему
class Dump:
    def __init__(self, agents, agents_numb, atribute, atribute_numb, verb, verb_numb, point, money, money_numb, data, person, abbreviation, abbreviation_number):
        self.agents = agents
        self.agents_numb = agents_numb
        self.atribute = atribute
        self.attr_numb = atribute_numb
        self.action = verb
        self.action_numb = verb_numb
        self.points = point
        self.money = money
        self.money_numb = money_numb
        self.data = data
        self.person=person
        self.abbreviation=abbreviation
        self.abbreviation_number=abbreviation_number
        self.Supreme_keyword=['верховний суд',"вищий адмiнiстративний суд"]
        self.State_keyword=['окружний суд','адміністративний суд','апеляційний адміністративний суд','гу', 'головне управління']
        self.Tax_keyword=['компанiя', 'фiрма','ТОВ','ПФГ','Товариство з обмеженою відповідальністю']
        
    def to_result(self):

        for uri_index in reversed(self.abbreviation_number):
                for agent_index in reversed(self.agents_numb):

                    if(uri_index>agent_index):
                        a_tmp=self.agents[self.agents_numb.index(agent_index)]+' '+self.abbreviation[self.abbreviation_number.index(uri_index)]

                        self.agents.insert(self.agents_numb.index(agent_index),a_tmp)
                        self.agents.pop(self.agents_numb.index(agent_index)+1)

                        break
        tmp=''
        flag=True
        for i in self.agents:
            flag=True
            if(flag==True):
                for j in self.Supreme_keyword:
                    index=(i.lower()).find(j.lower())
                    if(index!=-1):

                        tmp+=i+'( {})'.format('SupremeCourt')+'\n'
                        flag=False
                        break
            if (flag == True):
                for j in self.State_keyword:
                    index = (i.lower()).find(j.lower())

                    if (index != -1):

                        tmp += i + '( {})'.format('StateAutority')+'\n'
                        flag = False
                        break
            if (flag == True):
                for j in self.Tax_keyword:
                    index = (i.lower()).find(j.lower())
                    if (index != -1):

                        tmp += i + '( {})'.format('TaxPayer')+'\n'
                        flag = False
                        break



        print(tmp)

