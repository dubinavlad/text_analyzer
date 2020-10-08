from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.ReferentToken import ReferentToken
from pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
from pullenti.ner.core.GetTextAttr import GetTextAttr
from pullenti.ner.core.MiscHelper import MiscHelper
from pullenti.ner.money.MoneyAnalyzer import MoneyAnalyzer
from pullenti.ner.money.MoneyReferent import MoneyReferent
from pullenti.unisharp.Utils import Utils


class Money:
    def __init__(self,text):
        self.txt=text
        self.money=[]
        self.money_number = []

    def get_money(self):
        with ProcessorService.create_specific_processor(MoneyAnalyzer.ANALYZER_NAME) as proc:
            ar = proc.process(SourceOfAnalysis(self.txt), None, None)
            t = ar.first_token
            number = 0
            first_pass = True
            while True:
                if first_pass:
                    first_pass = False
                else:
                    number += 1
                    t = t.next0_
                if (not (t is not None)): break
                if (isinstance(t, ReferentToken)):
                    kw = Utils.asObjectOrNull(t.get_referent(), MoneyReferent)
                    if (kw is None):
                        continue
                    kwstr = MiscHelper.get_text_value_of_meta_token(Utils.asObjectOrNull(t, ReferentToken),
                                                                    Utils.valToEnum(
                                                                        (GetTextAttr.NO) | (GetTextAttr.KEEPREGISTER),
                                                                        GetTextAttr))
                    self.money.append(kwstr)
                    self.money_number.append(number)
        return [self.money,self.money_number]