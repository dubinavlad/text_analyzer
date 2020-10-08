from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.ReferentToken import ReferentToken
from pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
from pullenti.ner.core.GetTextAttr import GetTextAttr
from pullenti.ner.core.MiscHelper import MiscHelper
from pullenti.ner.keyword.KeywordAnalyzer import KeywordAnalyzer
from pullenti.ner.keyword.KeywordReferent import KeywordReferent
from pullenti.unisharp.Utils import Utils

#Запускает специфический процессор с KeywordAnalyzer, разбивает текст на токены  из которых мы получаем Atribute, Actions и номера токенов в тексте
class Keyword:
    def __init__(self,text,actions):
        self.txt = text
        self.atribute = []
        self.atribute_number = []
        self.actions = actions

    def get_keyword(self):
            with ProcessorService.create_specific_processor(KeywordAnalyzer.ANALYZER_NAME) as proc:
                ar = proc.process(SourceOfAnalysis(self.txt), None, None)
                t = ar.first_token
                number = 0
                t_previos = None
                t_n = None
                kwstr_previos = None
                first_pass2881 = True
                while True:
                    if first_pass2881:
                        first_pass2881 = False
                    else:

                        number += 1
                        t_previos = t
                        t = t.next0_
                    if (not (t is not None)): break

                    if (isinstance(t, ReferentToken)):
                        kw = Utils.asObjectOrNull(t.get_referent(), KeywordReferent)
                        if (kw is None):
                            continue
                        if (t_previos is not None):
                            kwstr_previos = MiscHelper.get_text_value_of_meta_token(
                                Utils.asObjectOrNull(t_previos, ReferentToken),
                                Utils.valToEnum((
                                                    GetTextAttr.NO) | (
                                                    GetTextAttr.KEEPREGISTER),
                                                GetTextAttr))
                        t_previos = t
                        kwstr = MiscHelper.get_text_value_of_meta_token(Utils.asObjectOrNull(t, ReferentToken),
                                                                        Utils.valToEnum((
                                                                                            GetTextAttr.NO) | (
                                                                                            GetTextAttr.KEEPREGISTER),
                                                                                        GetTextAttr))

                        if (kwstr_previos != None):
                            for i in [self.actions['NonFaiding']]:
                                if (str(kwstr_previos).lower() in str(i).lower()):
                                    kwstr = MiscHelper.get_text_value_of_meta_token(
                                        Utils.asObjectOrNull(t, ReferentToken),
                                        Utils.valToEnum((
                                                            GetTextAttr.NO) | (
                                                            GetTextAttr.KEEPREGISTER),

                                                        GetTextAttr))
                                    self.atribute.append(kwstr)
                                    self.atribute_number.append(number)
            return [self.atribute,self.atribute_number]