import transliterate

#Обрабатывает прежде полученые данные, и формирует из их выходной результат для передачи в AMS систему
class Dump_all:
    def __init__(self,agents,agents_numb,atribute,atribute_numb,verb,verb_numb,point,money,money_numb,data):
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
    def dump_to_file(self):
        for i in self.ag_numb:
            tmp = '\n'+ transliterate.translit(
                str(self.agents[self.ag_numb.index(i)]).replace(
                    ' ', '_'),
                language_code='uk',
                reversed=True)+ ' - '

            for j in self.attr_numb:
                if (i<j):
                    tmp+= transliterate.translit(
                        str(self.atribute[self.attr_numb.index(j)]).replace(
                            ' ', '_'),
                        language_code='uk',
                        reversed=True) +', '
                self.atribute.pop(self.attr_numb.index(j))
                self.attr_numb.pop(self.attr_numb.index(j))
            with open('Dump.txt','a',encoding='utf-8') as f:
                f.write(str(tmp)+"\n")

        with open('Dump.txt', 'a', encoding='utf-8') as f:
            f.write(str(transliterate.translit(
                        str(self.action['faiding']).replace(
                            ' ', '_'),
                        language_code='uk',
                        reversed=True)+", "+transliterate.translit(
                        str(self.action['NonFaiding']).replace(
                            ' ', '_'),
                        language_code='uk',
                        reversed=True)+'\n' ))


        self.atribute.reverse()
        self.attr_numb.reverse()
        self.money.reverse()
        self.money_numb.reverse()
        tmp_string = ''


        tmp_string += transliterate.translit(
            str("судового збору").replace(
                 ' ', '_'),
             language_code='uk',
            reversed=True) +" = "+ transliterate.translit(
                            str(self.money[0]).replace(
                                ' ', '_'),
                            language_code='uk',
                            reversed=True) + "\n"
        self.money.pop(0)
        self.money_numb.pop(0)

        for i in self.money_numb:
            index_i = self.money_numb.index(i)
            for j in self.attr_numb:
                index_j = self.attr_numb.index(j)
                if j<i:
                    with open('Dump.txt', 'a', encoding='utf-8') as f:
                        f.write(str(transliterate.translit(
                            str(self.atribute[self.attr_numb.index(j)]).replace(
                                ' ', '_'),
                            language_code='uk',
                            reversed=True) +" = "+transliterate.translit(
                            str( self.money[self.money_numb.index(i)]).replace(
                                ' ', '_'),
                            language_code='uk',
                            reversed=True) +'\n'))
                self.atribute.pop(self.attr_numb.index(j))
                self.attr_numb.pop(self.attr_numb.index(j))
            self.money.pop(self.money_numb.index(i))
            self.money_numb.pop(self.money_numb.index(i))

        self.money.reverse()

        tmp_string +=   transliterate.translit(
                            str("штрафні санкції").replace(
                                ' ', '_'),
                            language_code='uk',
                            reversed=True)+" = "+transliterate.translit(
                            str(self.money[0]).replace(
                                ' ', '_'),
                            language_code='uk',
                            reversed=True) + "\n"
        tmp_string += transliterate.translit(
            str("штрафні санкції").replace(
                ' ', '_'),
            language_code='uk',
            reversed=True) +" = "+ transliterate.translit(
                            str(self.money[1]).replace(
                                ' ', '_'),
                            language_code='uk',
                            reversed=True) + "\n"
        #tmp_string += transliterate.translit(
          #  str("судового збору").replace(
           #     ' ', '_'),
           # language_code='uk',
            #reversed=True) + self.money[2] + "\n"

        with open('Dump.txt', 'a', encoding='utf-8') as f:
            f.write(str(tmp_string)+'\n'+transliterate.translit(
                            str(self.points).replace(
                                ' ', '_'),
                            language_code='uk',
                            reversed=True)+'\n'+transliterate.translit(
                            str(self.data).replace(
                                ' ', '_'),
                            language_code='uk',
                            reversed=True))



