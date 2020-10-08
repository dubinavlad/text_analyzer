from Classes.analiz_test import Analize_test
from Classes.points_analizer import Point
from Classes.to_file import Dump_all
from pullenti.morph.MorphLang import MorphLang
import codecs
import transliterate
from pullenti.ner.Sdk import Sdk
from pullenti.unisharp.Misc import Stopwatch
from pullenti.ner.uri.UriAnalyzer import UriAnalyzer

from Classes.to_json import Dump
from Classes.to_env_description import Dump
from Classes.new_results import Dump
from Classes.data_analizer import Data
from Classes.person_analizer import Person
from Classes.organization_analizer import Organization
from Classes.keyword_analizer import Keyword
from Classes.verb_analizer import Verb
from Classes.attr_analizer import Attr
from Classes.money_analyzer import Money
from Classes.uri_analyzer import URI


def file_reader():
    fileObj = codecs.open("text.txt", "r", "utf_8_sig")
    txt = fileObj.read()
    fileObj.close()
    return txt


def analyzer(txt):

        actions = {'faiding': [],'NonFaiding':[]}
        action_nonefanding=[]
        agents = []
        agents_all =[]
        atribute = []
        agents_number=[]
        agents_number_all =[]
        actions_number={'faiding': [],'NonFaiding':[]}
        action_number_nonfanding=[]
        atribute_number=[]
        data = []
        data_number = []
        money=[]
        maney_number=[]
        tras_attr =[]
        tras_attr_numb =[]
        point = []
        person=[]

        tmp =""
        k=1
        t_previos = None

        sw = Stopwatch()
        Sdk.initialize(MorphLang.UA)
        sw.stop()



        data_analize = Data(txt).get_data()
        data = data_analize[0]
        data_number = data_analize[1]
        uri_analize=URI(txt).get_uri()
        uri=uri_analize[0]
        uri_number=uri_analize[1]
        person= Person(txt).get_Person()

        organization_analize = Organization(txt).get_Organization()
        agents = organization_analize[0]
        agents_number = organization_analize[2]
        agents_all = organization_analize[1]
        agents_number_all = organization_analize[3]

        verb_analize = Verb(txt).get_verb()

        actions = verb_analize[0]
        actions_number = verb_analize[1]

        action_nonefanding = verb_analize[2]
        action_number_nonfanding = verb_analize[3]

        keyword_analize= Keyword(txt,actions).get_keyword()
        atribute = keyword_analize[0]
        atribute_number = keyword_analize[1]



        point = Point(txt)
        point_tmp=point.analiz()

        attr_analize = Attr(txt,atribute).get_attr()
        tras_attr = attr_analize[0]
        tras_attr_numb= attr_analize[1]

        money_analize = Money(txt).get_money()
        money = money_analize[0]
        maney_number = money_analize[1]

        def action():

            for i in actions['faiding']:
                 actions_mass.append(i)

            for i in actions['NonFaiding']:
                actions_mass.append(i)

        #to_file =Dump_all(agents_all,agents_number_all,atribute,atribute_number,actions,actions_number,point_tmp,money,maney_number,data)
        #to_file.dump_to_file()
        #dum=Dump(agents_all,agents_number_all,action_nonefanding,action_number_nonfanding,tras_attr,tras_attr_numb,atribute, atribute_number,data,data_number,money,maney_number)
        #dum.tojson()
        #analize = Analize_test(agents_all,agents_number_all,atribute,atribute_number,actions,actions_number,point_tmp,money,maney_number,data, data_number)
        #analize.analize()
        new_results = Dump(agents,agents_number,tras_attr,tras_attr_numb,action_nonefanding,action_number_nonfanding,point,money,maney_number,data,person,uri,uri_number)
        new_results.to_result()
        #to_env= Dump(agents_all,agents_number_all,action_nonefanding,action_number_nonfanding,tras_attr,v,atribute, atribute_number,data,data_number,money,maney_number,point_tmp)
        #to_env.to_env_description()
        #trasa()
        actions_mass = []
        action()

        information = {'data': {'agents': agents, 'actions': actions_mass, 'atribute': atribute},'number':{'agents': agents_number, 'actions': actions_number, 'atribute': atribute_number}}
        return information