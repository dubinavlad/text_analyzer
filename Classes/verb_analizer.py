from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
from pullenti.ner.core.VerbPhraseHelper import VerbPhraseHelper

#Запускает стандартный процессор , разбивает текст на токены  и производит прверку того что текстовый токен является глаголом,также производит проверку на то что глагол не входит в словарь ошибочных слов
class Verb:
    def __init__(self,text):
        self.txt = text
        self.actions = {'faiding': [],'NonFaiding':[]}
        self.actions_number = {'faiding': [], 'NonFaiding': []}
        self.action_nonefanding = []
        self.action_number_nonfanding = []


    def get_verb(self):
            with ProcessorService.create_processor() as proc:

                ar = proc.process(SourceOfAnalysis(self.txt), None, None)
                number = 0
                t_i=0
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

                    verb = VerbPhraseHelper.try_parse(t, False)

                    if (verb is None):
                        continue

                    with open('Classes/text_file/words.txt', 'r', encoding='utf-8') as f:
                        text = f.read()
                    text.split(',')
                    if t_i< len(text):

                        if verb.get_source_text() not in text[t_i]:

                            if ((t.next0_).get_source_text() == ':'):
                                self.actions['faiding'].append(verb.get_source_text())
                                self.actions_number['faiding'].append(number)
                            else:
                                self.actions['NonFaiding'].append(verb.get_source_text())
                                self.action_nonefanding.append(verb.get_source_text())
                                self.actions_number['NonFaiding'].append(number)
                                self.action_number_nonfanding.append(number)
                    else:
                        if ((t.next0_).get_source_text() == ':'):
                            self.actions['faiding'].append(verb.get_source_text())
                            self.actions_number['faiding'].append(number)
                        else:
                            self.actions['NonFaiding'].append(verb.get_source_text())
                            self.action_nonefanding.append(verb.get_source_text())
                            self.actions_number['NonFaiding'].append(number)
                            self.action_number_nonfanding.append(number)

                    t = verb.end_token

            return [self.actions,self.actions_number,self.action_nonefanding,self.action_number_nonfanding]

