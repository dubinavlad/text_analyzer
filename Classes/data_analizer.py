from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.ReferentToken import ReferentToken
from pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
from pullenti.ner.core.GetTextAttr import GetTextAttr
from pullenti.ner.core.MiscHelper import MiscHelper
from pullenti.ner.date.DateAnalyzer import DateAnalyzer
from pullenti.ner.date.DateReferent import DateReferent
from pullenti.unisharp.Utils import Utils

#Запускает специфический процессор с DateAnalyzer, разбивает текст на токены  из которых мы получаем дату и время
class Date:
    def __init__(self,text):
        self.txt = text
        self.data = []
        self.data_number=[]
    def get_data(self):
            with ProcessorService.create_specific_processor(DateAnalyzer.ANALYZER_NAME) as proc:
                ar = proc.process(SourceOfAnalysis(self.txt), None, None)
                t = ar.first_token
                number=0
                first_pass = True
                while True:
                    if first_pass:
                        first_pass = False
                    else:
                        number+=1
                        t = t.next0_
                    if (not (t is not None)): break
                    if (isinstance(t, ReferentToken)):
                        kw = Utils.asObjectOrNull(t.get_referent(), DateReferent)
                        if (kw is None):
                            continue
                        kwstr = MiscHelper.get_text_value_of_meta_token(Utils.asObjectOrNull(t, ReferentToken), Utils.valToEnum((GetTextAttr.NO) | (GetTextAttr.KEEPREGISTER), GetTextAttr))
                        self.data.append(kwstr)
                        self.data_number.append(number)
            return [self.data,self.data_number]
