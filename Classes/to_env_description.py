import json
import requests
import transliterate

#Обрабатывает прежде полученые данные, и формирует из их выходной результат для передачи в AMS систему
class Dump:

    def __init__(self,agents_all,agents_number_all,action_nonefanding,action_number_nonfanding,tras_attr,tras_attr_numb,atribute, atribute_number,data,data_number,money,maney_number,points):
        self.trasa_atribute = None
        self.trasa_agent = None
        self.trasa_action = None
        self.trasa_data = None
        self.trasa_attr = None
        self.trasa_money = None
        self.trasa_point = None

        self.trasa_point=0
        self.trasa_point=points

        self.agent_i = 0
        self.trassa_agent_mass = agents_all
        self.trassa_agent_mass.reverse()

        self.trassa_agent_mass_numb = agents_number_all
        self.trassa_agent_mass_numb.reverse()

        self.action_i = 0
        self.trassa_action_mass = action_nonefanding
        self.trassa_action_mass_numb = action_number_nonfanding

        self.attr_i = 0
        self.trassa_attr_mass = tras_attr
        self.trassa_attr_mass.reverse()

        self.trassa_attr_mass_numb = tras_attr_numb
        self.trassa_attr_mass_numb.reverse()

        self.attribute_i = 0
        self.trassa_atribute = atribute
        self.trassa_atribute.reverse()

        self.trassa_atribute_number = atribute_number
        self.trassa_atribute_number.reverse()

        self.data_i = 0
        self.trassa_data_mass = data
        self.trassa_data_mass.reverse()

        self.trassa_data_mass_number = data_number
        self.trassa_data_mass_number.reverse()

        self.money_i = 0
        self.trassa_maney_mass = money
        self.trassa_maney_mass.reverse()

        self.trassa_maney_number = maney_number
        self.trassa_maney_number.reverse()



    def to_env_description(self):
        trasa_agent = ''
        trasa_action = ''
        trasa_pre_action = ''
        trasa_data=''
        trasa_money=''
        trasa_pre_maney=''
        trassa_midle_money=''
        trasa_atribute=''
        print(self.at)
        for i in self.trassa_action_mass_numb:

            self.action_i += 1
            for j in self.trassa_agent_mass_numb:
                self.agent_i += 1
                if i > j:
                    for a in self.trassa_atribute_number:
                        self.attribute_i += 1
                        try:

                            # if a > trassa_action_mass_numb[trassa_action_mass_numb.index(i) - 1]:

                            # for h in trassa_attr_mass_numb:
                            # attr_i+=1
                            # if j<h:

                            if self.trassa_data_mass_number:

                                for d in self.trassa_data_mass_number:
                                    self.data_i += 1
                                    if j > d:


                                        for m in self.trassa_maney_number:

                                            self.money_i += 1

                                            if j < m:
                                                print(0)

                                                if (len(self.trassa_action_mass_numb) > 0):

                                                    try:
                                                        trasa_agent = self.trassa_agent_mass[self.trassa_agent_mass_numb.index(j)]
                                                        self.trassa_agent_mass.pop(self.trassa_agent_mass_numb.index(j))
                                                        self.trassa_agent_mass_numb.pop(
                                                            self.trassa_agent_mass_numb.index(j))

                                                        trasa_action = self.trassa_action_mass[
                                                            self.trassa_action_mass_numb.index(i)]
                                                        trasa_pre_action = self.trassa_action_mass[
                                                            self.trassa_action_mass_numb.index(i) + 1]

                                                        self.trassa_action_mass.pop(self.trassa_action_mass_numb.index(i))
                                                        self.trassa_action_mass_numb.pop(self.trassa_action_mass_numb.index(i))

                                                        #  trasa_attr = trassa_attr_mass[trassa_attr_mass_numb.index(h)]
                                                        # trassa_attr_mass.pop(trassa_attr_mass_numb.index(h))
                                                        # trassa_attr_mass_numb.pop(
                                                        #     trassa_attr_mass_numb.index(h))

                                                        trasa_data = self.trassa_data_mass[self.trassa_data_mass_number.index(d)]
                                                        self.trassa_data_mass.pop(self.trassa_data_mass_number.index(d))
                                                        self.trassa_data_mass_number.pop(
                                                            self.trassa_data_mass_number.index(d))

                                                        trasa_money = self.trassa_maney_mass[
                                                            self.trassa_maney_number.index(
                                                                m)]

                                                        trasa_pre_maney = \
                                                            self.trassa_maney_mass[
                                                                self.trassa_maney_number.index(
                                                                    m) - 1]

                                                        trassa_midle_money = \
                                                            self.trassa_maney_mass[
                                                                self.trassa_maney_number.index(
                                                                    m) - 2]

                                                        self.trassa_maney_number.pop(
                                                            self.trassa_maney_number.index(
                                                                m) - 2)

                                                        self.trassa_maney_number.pop(
                                                            self.trassa_maney_number.index(
                                                                m) - 1)

                                                        self.trassa_maney_mass.pop(
                                                            self.trassa_maney_number.index(
                                                                m))

                                                        trasa_atribute = \
                                                            self.trassa_atribute[
                                                                self.trassa_atribute_number.index(
                                                                    a) + 1]
                                                        self.trassa_atribute.pop(self.trassa_atribute_number.index(a))


                                                    except ValueError:
                                                        print(1)
                                                        break
                            else:
                                for m in self.trassa_maney_number:
                                    self.money_i += 1
                                    print(j)
                                    print(m)
                                    if j < m:

                                        if (len(self.trassa_action_mass_numb) > 0):
                                            try:

                                                trasa_agent = self.trassa_agent_mass[self.trassa_agent_mass_numb.index(j)]

                                                self.trassa_agent_mass.pop(self.trassa_agent_mass_numb.index(j))
                                                self.trassa_agent_mass_numb.pop(
                                                    self.trassa_agent_mass_numb.index(j))

                                                trasa_action = self.trassa_action_mass[self.trassa_action_mass_numb.index(i)]
                                                trasa_pre_action = self.trassa_action_mass[
                                                    self.trassa_action_mass_numb.index(i) + 1]
                                                self.trassa_action_mass.pop(self.trassa_action_mass_numb.index(i))
                                                self.trassa_action_mass_numb.pop(self.trassa_action_mass_numb.index(i))

                                                # trasa_attr = trassa_attr_mass[trassa_attr_mass_numb.index(h)]
                                                # trassa_attr_mass.pop(trassa_attr_mass_numb.index(h))
                                                # trassa_attr_mass_numb.pop(
                                                # trassa_attr_mass_numb.index(h))

                                                # trasa_data = trassa_data_mass[trassa_data_mass_number.index(d)]
                                                # trassa_data_mass.pop(trassa_data_mass_number.index(d))

                                                trasa_money = self.trassa_maney_mass[self.trassa_maney_number.index(m)]

                                                trasa_pre_maney = self.trassa_maney_mass[self.trassa_maney_number.index(m) - 1]

                                                trassa_midle_money = self.trassa_maney_mass[self.trassa_maney_number.index(m) - 2]
                                                trassa_midle_money = trassa_midle_money.split(' ')
                                                trassa_midle_money = trassa_midle_money[0]
                                                #self.trassa_maney_number.pop(
                                                    #self.trassa_maney_number.index(m) - 2)

                                                #self.trassa_maney_number.pop(
                                                    #self.trassa_maney_number.index(m) - 1)

                                                #self.trassa_maney_mass.pop(
                                                    #self.trassa_maney_number.index(
                                                        #m))

                                                trasa_atribute = self.trassa_atribute[self.trassa_atribute_number.index(a) + 1]
                                                self.trassa_atribute.pop(self.trassa_atribute_number.index(a))


                                                with open('Classes/text_file/empty_file.json', 'r', encoding='utf-8')as fer:
                                                    json_file = json.loads(fer.read())

                                                json_file['model']['agentTypes'].append({"id": self.agent_i,
                                                                                         "name": transliterate.translit(
                                                                                             str(trasa_agent).replace(
                                                                                                 ' ', '_'),
                                                                                             language_code='uk',
                                                                                             reversed=True),
                                                                                         "description": "",
                                                                                         "attributes":
                                                                                             [{"id": self.money_i,
                                                                                               "name": transliterate.translit(
                                                                                                   "Податкове забов`язання".replace(
                                                                                                       ' ', '_'),
                                                                                                   language_code='uk',
                                                                                                   reversed=True),
                                                                                               "description": "",
                                                                                               "type": "real",
                                                                                               "body": {"input": [],
                                                                                                        "output": "undefined"}},
                                                                                              {"id": self.money_i + 1,
                                                                                               "name": transliterate.translit(
                                                                                                   "Штрафні санкції".replace(
                                                                                                       ' ', '_'),
                                                                                                   language_code='uk',
                                                                                                   reversed=True),
                                                                                               "description": "",
                                                                                               "type": "real",
                                                                                               "body": {"input": [],
                                                                                                        "output": "undefined"}}]})
                                                print(trasa_agent)
                                                json_file['model']['agents'].append({
                                                    "id": self.agent_i,
                                                    "name": transliterate.translit(
                                                        trasa_agent.lower().replace(' ', '_'), language_code='uk',
                                                        reversed=True),
                                                    "description": "",
                                                    "type": transliterate.translit(trasa_agent.replace(' ', '_'),
                                                                                   language_code='uk', reversed=True)
                                                })

                                                json_file['model']['actions'].append({
                                                    "id": self.action_i,
                                                    "name": transliterate.translit(trasa_action.replace(' ', '_'),
                                                                                   language_code='uk', reversed=True),
                                                    "description": "",
                                                    "msc": {"entities":
                                                                [{"id": self.agent_i,
                                                                  "text": transliterate.translit(
                                                                      trasa_agent.replace(' ', '_'), language_code='uk',
                                                                      reversed=True) + " " + transliterate.translit(
                                                                      trasa_agent.lower().replace(' ', '_'),
                                                                      language_code='uk', reversed=True)},
                                                                 {"id": 1, "text": "COURT court"}],
                                                            "elements": [{
                                                                "for": [
                                                                    0,
                                                                    1],
                                                                "text": "1"},
                                                                {
                                                                    "for": [
                                                                        0,
                                                                        1],
                                                                    "text": transliterate.translit(
                                                                        trasa_agent.lower().replace(' ', '_'),
                                                                        language_code='uk',
                                                                        reversed=True) + "." + transliterate.translit(
                                                                        trasa_action.replace(' ', '_'),
                                                                        language_code='uk',
                                                                        reversed=True) + "=" + trassa_midle_money + ";\ntov.Penalties=0"
                                                                }
                                                            ]

                                                            }})
                                                self.action_i += 1
                                                json_file['model'][
                                                    'actions'].append({
                                                    "id": self.action_i,
                                                    "name": transliterate.translit(
                                                        trasa_pre_action.replace(' ', '_'),
                                                        language_code='uk',
                                                        reversed=True),
                                                    "description": "",
                                                    "msc": {"entities": [
                                                        {"id": self.agent_i,
                                                         "text": transliterate.translit(trasa_agent.replace(' ', '_'),
                                                                                        language_code='uk',
                                                                                        reversed=True) + " " + transliterate.translit(
                                                             trasa_agent.lower().replace(' ', '_'), language_code='uk',
                                                             reversed=True)},
                                                        {"id": 1,
                                                         "text": "COURT court"}],
                                                        "elements": [
                                                            {"for": [0, 1],
                                                             "text": "1"},
                                                            {
                                                                "for": [0,
                                                                        1],
                                                                "text": "1"
                                                            }
                                                        ]}})
                                                json_file['model']['behavior'] = 'BO = ' + transliterate.translit(
                                                    trasa_action.replace(' ', '_'), language_code='uk',
                                                    reversed=True) + ' . ' + transliterate.translit(
                                                    trasa_pre_action.replace(' ', '_'), language_code='uk',
                                                    reversed=True) + " . Delta"
                                                json_file['model']['behaviors'].append(
                                                    {
                                                        "id": 1,
                                                        "name": "Bo",
                                                        "description": "",
                                                        "graph":
                                                            {
                                                                "vertices": [],
                                                                "edges": []
                                                            }
                                                    }
                                                )
                                                trasa_pre_maney = trasa_pre_maney.split(" ")
                                                trasa_pre_maney = trasa_pre_maney[0]

                                                trasa_money = trasa_money.split(" ")
                                                trasa_money = trasa_money[0]

                                                json_file['experiments'].append(
                                                    {"name": "default", "logicFormula":
                                                        {"body":
                                                             [
                                                                 "cycle == 1 &&\n{0}.Shtrafni_sanktsiyi == {1} &&\n{0}.Podatkove_zabovjazannja=={2} ".format(
                                                                     transliterate.translit(
                                                                         trasa_agent.replace(' ', '_'),
                                                                         language_code='uk', reversed=True),
                                                                     trasa_money, trasa_pre_maney)]}})

                                                self.action_i -= 1
                                                with open('Classes/text_file/trasa.json', 'a', encoding='utf-8')as f:
                                                    json.dump(json_file, f)
                                            except ValueError:
                                                print(1)
                                                break
                        except ValueError:
                            print(2)
                            break
        print(trasa_pre_action)
        print(trasa_action)

        tmp = 'environment(\n' \
              'types:obj(\nNil\n);\n'\
              'attributes:obj(\n Nil \n);\n' \
              'agent_types:obj(\n'
        atribute_tmp='{}:real'.format(transliterate.translit(self.trassa_atribute[0].replace(' ', '_'), language_code='uk', reversed=True))
        for i in range(len(self.trassa_atribute)):
            if(i+1<len(self.trassa_atribute)):
                atribute_tmp += ',{}:real'.format(transliterate.translit(self.trassa_atribute[i+1].replace(' ', '_'), language_code='uk', reversed=True))
        tmp+='{0}:obj({1}));\n'.format(transliterate.translit(trasa_agent.replace(' ', '_'), language_code='uk', reversed=True),atribute_tmp)
        tmp+='agents:obj(\n{}:obj(u)\n);\n'.format(transliterate.translit(trasa_agent.replace(' ', '_'), language_code='uk', reversed=True))
        tmp+= 'instances:(\nNil\n);\n' \
                  'axioms:obj(Nil);\n'
        tmp+='logic_formula:obj((u.{0} = {3}) && (u.{1} = {4}) && (u.{2}={5}));'.format(transliterate.translit("податкове зобов'язання".replace(' ', '_'), language_code='uk', reversed=True),
                                                                             transliterate.translit(
                                                                                 "основний платіж".replace(' ',
                                                                                                                  '_'),
                                                                                 language_code='uk', reversed=True),transliterate.translit(
                                                                                 "штрафні санкції".replace(' ',
                                                                                                                  '_'),
                                                                                 language_code='uk', reversed=True),trasa_pre_maney,trassa_midle_money,trasa_money)
        tmp+='reductions:(Nil);\n' \
                  'initial:env(\nobj(\nattributes:obj(Nil);\nagent_parameters:obj(Nil)\n' \
                  '),\nstate(\nNil\n)\n)\n);'

        with open("Classes/text_file/project.env_descript", 'w',
                      encoding='utf-8') as fd:
                fd.write(tmp + '\n')

        behp_tmp = 'B0 = {0}.{1}.Delta '.format(transliterate.translit(trasa_action.replace(' ', '_'), language_code='uk', reversed=True),
                                                transliterate.translit(trasa_pre_action.replace(' ', '_'), language_code='uk', reversed=True))

        with open("Classes/text_file/project.behp", 'w',
                      encoding='utf-8') as fd:
                fd.write(behp_tmp + '\n')
        act_tmp='{0}=(\n' \
                '(1)->\n' \
                '("{1} {0}")\n' \
                '(1)),\n' \
                '{2}=(\n' \
                '(1)->\n' \
                '("{1} {2}")\n' \
                '(1))\n'.format(transliterate.translit(trasa_action.replace(' ', '_'), language_code='uk', reversed=True),
                                transliterate.translit(trasa_agent.replace(' ', '_'), language_code='uk', reversed=True),
                                                transliterate.translit(trasa_pre_action.replace(' ', '_'), language_code='uk', reversed=True))
        with open("Classes/text_file/project.act", 'w',
                      encoding='utf-8') as fd:
                fd.write(act_tmp + '\n')

        final_file={
            'env_descript':tmp,
            'behp':behp_tmp,
            'act':act_tmp
        }

        print(final_file)
        url = 'http://localhost:5002/'


        x = requests.post(url, data=final_file)


        print(x.text)