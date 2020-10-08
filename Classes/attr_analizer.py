from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
from pullenti.ner.instrument.InstrumentAnalyzer import InstrumentAnalyzer
import re
# Запускает специфический процессор с InstrumentAnalyzer ,
# разбивает текст на соответствующие токены , после чего проверяем их на последовательность прилагательное, предлог , существительное чем будем являться Atribute
class Attr:
    def __init__(self,text,atribute):
        self.txt = text
        self.atribute = atribute
        self.tras_attr = []
        self.tras_attr_numb = []

    def get_attr(self):
        with ProcessorService.create_specific_processor(InstrumentAnalyzer.ANALYZER_NAME) as proc:
            ar = proc.process(SourceOfAnalysis(self.txt), None, None)
            t = ar.first_token
            f = False
            number = 0
            f_t = None
            f_t_previos = None
            t_previos = None
            first_pass = True
            while True:
                if first_pass:
                    first_pass = False
                else:
                    number += 1
                    t_previos = t
                    if (not (t is not None)): break
                    t = t.next0_

                if (not (t is not None)): break

                for i in self.atribute:
                    a_numb = number
                    a_t = t
                    a = False
                    while (a == False):
                        t_previos = t
                        number += 1
                        if (t is None): break
                        t = t.next0_
                        if (t is None): break
                        if (i in t.get_source_text()):
                            f_numb = number
                            f_t = t
                            f = False
                            while (f == False):
                                t_previos = t
                                number += 1
                                if (t is None):break
                                t = t.next0_
                                if (re.search(r'\bприлаг\b', str(t))):
                                    if (re.search(r'\bпредлог\b', str(t_previos))):
                                        if (re.search(r'\bсуществ\b', str(t.next0_))):
                                            tmp = str(t_previos.get_source_text()) + ' ' + str(
                                                t.get_source_text()) + ' ' + str((t.next0_).get_source_text())
                                            self.tras_attr.append(tmp)
                                            self.tras_attr_numb.append(number)
                                            f = True
                                            a = True
                                            t = f_t
                                            number = f_numb

                    if (not (t is not None)): break
                    t = t.next0_
                    number += 1
        return [self.tras_attr,self.tras_attr_numb]