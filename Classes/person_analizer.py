from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.ReferentToken import ReferentToken
from pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
from pullenti.ner.core.GetTextAttr import GetTextAttr
from pullenti.ner.core.MiscHelper import MiscHelper
from pullenti.ner.person.PersonAnalyzer import PersonAnalyzer
from pullenti.ner.person.PersonReferent import PersonReferent
from pullenti.unisharp.Utils import Utils

#Запускает специфический процессор с PersonAnalyzer, разбивает текст на токены  из которых мы получаем имена , а также должности если они привязаны к имени
class Person:
    def __init__(self,text):
        self.txt = text
        self.person=[]
    def get_Person(self):
            with ProcessorService.create_specific_processor(PersonAnalyzer.ANALYZER_NAME) as proc:
                ar = proc.process(SourceOfAnalysis(self.txt), None, None)
                t = ar.first_token
                first_pass = True
                while True:
                    if first_pass:
                        first_pass = False
                    else:
                        t = t.next0_
                    if (not (t is not None)): break
                    if (isinstance(t, ReferentToken)):
                        kw = Utils.asObjectOrNull(t.get_referent(), PersonReferent)
                        if (kw is None):
                            continue
                        kwstr = MiscHelper.get_text_value_of_meta_token(Utils.asObjectOrNull(t, ReferentToken),
                                                                        Utils.valToEnum((
                                                                                            GetTextAttr.FIRSTNOUNGROUPTONOMINATIVESINGLE) | (
                                                                                            GetTextAttr.KEEPREGISTER),
                                                                                        GetTextAttr))
                        self.person.append(kwstr)

            return self.person