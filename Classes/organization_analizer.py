from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.ReferentToken import ReferentToken
from pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
from pullenti.ner.core.GetTextAttr import GetTextAttr
from pullenti.ner.core.MiscHelper import MiscHelper
from pullenti.ner.org.OrganizationAnalyzer import OrganizationAnalyzer
from pullenti.ner.org.OrganizationReferent import OrganizationReferent
from pullenti.unisharp.Utils import Utils


class Organization:
    def __init__(self,text):
        self.txt = text
        self.agents=[]
        self.agents_number = []
        self.agents_all = []
        self.agents_number_all = []



    def get_Organization(self):
            with ProcessorService.create_specific_processor(OrganizationAnalyzer.ANALYZER_NAME) as proc:
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
                        kw = Utils.asObjectOrNull(t.get_referent(), OrganizationReferent)
                        if (kw is None):
                            continue
                        kwstr = MiscHelper.get_text_value_of_meta_token(Utils.asObjectOrNull(t, ReferentToken),
                                                                        Utils.valToEnum((
                                                                                            GetTextAttr.FIRSTNOUNGROUPTONOMINATIVESINGLE) | (
                                                                                            GetTextAttr.KEEPREGISTER),
                                                                                        GetTextAttr))
                        for i in [self.agents]:
                            if (kwstr != None):
                                if (str(kwstr).lower() not in str(i).lower()):
                                    self.agents.append(kwstr)
                                    self.agents_number.append(number)

                                self.agents_all.append(kwstr)
                                self.agents_number_all.append(number)

            return [self.agents,self.agents_all,self.agents_number,self.agents_number_all]