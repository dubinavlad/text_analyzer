from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
from pullenti.ner.keyword.KeywordAnalyzer import KeywordAnalyzer
import re


class Point:
    def __init__(self,text):
        self.points = []
        self.point_string = ''
        self.txt=text

    def analiz(self):
        with ProcessorService.create_specific_processor(KeywordAnalyzer.ANALYZER_NAME) as proc:
            ar = proc.process(SourceOfAnalysis(self.txt), None, None)
            t = ar.first_token
            number = 0
            point_string = ''
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
                if (t != None):
                    if str(t.get_source_text())[0] == '.':
                        continue
                    if (re.search(r'\bП\b', str(t))) or (re.search(r'\bСТ\b', str(t))):

                        if (len(str(t.get_source_text())) < 13 and len(str(t.get_source_text())) > 0):
                            print(t.get_source_text())
                            if (t.next0_ is not None):
                                t_n = t.next0_


                            point_string += str(t.get_source_text())
                        else:
                            tmp = str(t.get_source_text()).split('ст.')
                            if len(tmp) > 1:
                                tmp[1] = 'ст.' + tmp[1]
                                tmp2 = str(tmp[0]).split('п.')[1:]
                                print(tmp2)

                                if len(tmp2) > 0:
                                    time_str = ''
                                    count = 0
                                    for i in tmp2:
                                        if (re.search(r'\d+', i)):
                                            for j in tmp2:
                                                time_str += 'п.'
                                                count += 1
                                                if j == i:
                                                    time_str += i
                                                    self.points.append(time_str)
                                                    time_str = ''
                                                    break
                                        tmp2 = tmp2[count:]

                                self.points.append(tmp[1])

                                continue
                            tmp = str(t.get_source_text()).split('п.')[1:]
                            if len(tmp) > 1:
                                time_str = ''
                                count = 0
                                for i in tmp:
                                    if (re.search(r'\d+', i)):
                                        for j in tmp:
                                            time_str += 'п.'
                                            count += 1
                                            if j == i:
                                                time_str += i
                                                self.points.append(time_str)
                                                time_str = ''
                                                break
                                    tmp2 = tmp2[count:]

                    if (str(t.get_source_text()) in "."):
                        if (t.next0_ is not None):
                            if (t.next0_ is not None):
                                t_n = t.next0_
                            if (re.search(r'\bП\b', str(t_n))) or (re.search(r'\bСТ\b', str(t_n))):
                                point_string += str(t.get_source_text())
                            else:
                                point_string += str(t.get_source_text()) + str(t_n.get_source_text())

                    if (re.search(r'\d+', str(t.get_source_text()))):

                        if (re.search(r'\bП\b', str(t.next0_))):
                            if (point_string != ''):
                                self.points.append(point_string)

                            point_string = ""
                        if (re.search(r'\bСТ\b', str(t.next0_))):

                            if (point_string != ''):
                                self.points.append(point_string)

                            point_string = ""
                        if (re.search(r'\bТА\b', str(t.next0_))):
                            if (point_string != ''):
                                self.points.append(point_string)

                            point_string = ""
                    if (t.get_source_text() == ';'):
                        if (point_string != ''):
                            self.points.append(point_string)

                        point_string = ""
                    if (t.get_source_text() == ','):
                        if (point_string != ''):
                            self.points.append(point_string)

                        point_string = ""

                    if (t.next0_ is None):
                        if (point_string != ''):
                            self.points.append(point_string)

                        point_string = ""

                with open("point.txt", 'a',
                          encoding='utf-8') as fd:
                    fd.write(str(self.points))
        return str(self.points)