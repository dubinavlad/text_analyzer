import transliterate


class Analize_test:
    def __init__(self,agents,agents_numb,atribute,atribute_numb,verb,verb_numb,point,money,money_numb,data,data_numb):
        self.agents = agents
        self.ag_numb = agents_numb
        self.atribute = atribute
        self.attr_numb = atribute_numb
        self.action = verb
        self.action_numb = verb_numb
        self.points = point
        self.money = money
        self.money_numb = money_numb
        self.data = data
        self.data_numb=data_numb

    def analize(self):
        tmp = ''
        data = 0
        attr=''
        for i in self.ag_numb:
            for j in self.action_numb['NonFaiding']:
                if j<i:
                    for d in self.data_numb:
                        if d < i :
                            data = self.data[self.data_numb.index(d)]
                    for a in self.attr_numb:
                        if a<i and a>j:
                            attr = self.atribute[self.attr_numb.index(a)]
                    tmp+="Agent obj(\n" +  self.agents[self.ag_numb.index(i)-1] +"\n"+ self.agents[self.ag_numb.index(i)]+"\n)\n" + 'Action(\n'+self.action['NonFaiding'][self.action_numb['NonFaiding'].index(j) ]+\
                        '\n)\n'+'DATE:['+str(data)+']\n'+ 'Type_Massage: '+attr+" \n"+self.agents[self.ag_numb.index(i)-1] + " "+self.action['NonFaiding'][self.action_numb['NonFaiding'].index(j) ]+ ' -> ' +self.agents[self.ag_numb.index(i)]

        with open('analize_result.txt','w',encoding='utf-8') as f:
            f.write(tmp)
