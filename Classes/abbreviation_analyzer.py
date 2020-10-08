from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.ReferentToken import ReferentToken
from pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
from pullenti.ner.core.GetTextAttr import GetTextAttr
from pullenti.ner.core.MiscHelper import MiscHelper
from pullenti.ner.uri.UriAnalyzer import UriAnalyzer
from pullenti.ner.uri.UriReferent import UriReferent
from pullenti.unisharp.Utils import Utils


class Abbreviation:
    def __init__(self,text):
        self.txt = text
        self.uri=[]
        self.uri_number=[]
    def get_abbreviation(self):
            with ProcessorService.create_processor()  as proc:
                ar = proc.process(SourceOfAnalysis(self.txt), None, None)
                number = 0
                t_i = 0
                t = ar.first_token
                t_previos = None
                first_pass2880 = True
                while True:
                    if first_pass2880:
                        first_pass2880 = False
                    else:
                        number += 1
                        t_i += 1
                        t_previos = t
                        t = t.next0_
                    if (not (t is not None)): break
                    if (t.get_referent() is not None):
                        continue
                    print(t)
                    if(len(t.get_source_text())>1):
                        if(str((t.get_source_text())).isupper()==True):
                            self.uri.append(t.get_source_text())
                            self.uri_number.append(number)

            return [self.uri,self.uri_number]

