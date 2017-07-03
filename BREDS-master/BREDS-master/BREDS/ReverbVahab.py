import fileinput
import io
from io import StringIO
#from numpy import StringIO
import nltk

from nltk import pos_tag, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag.mapping import map_tag
#from nltk.tokenize import PunktWordTokenizer



class ReverbVahab(object):
    def __init__(self):
        self.lmtzr = WordNetLemmatizer()
        self.aux_verbs = ['be']

    @staticmethod
    def extract_reverb_patterns(text):

        text_tokens = word_tokenize(text)
        tags_ptb = pos_tag(text_tokens)
        tags = []
        for t in tags_ptb:
            tag = map_tag('en-ptb', 'universal', t[1])
            tags.append((t[0], tag))

        patterns = []
        patterns_tags = []
        i = 0
        limit = len(tags)-1
        while i <= limit:
            tmp = io.StringIO()
            tmp_tags = []

            # a ReVerb pattern always starts with a verb
            if tags[i][1] == 'VERB':
                tmp.write(tags[i][0]+' ')
                t = (tags[i][0], tags[i][1])
                tmp_tags.append(t)
                i += 1

                # V = verb particle? adv? (also capture auxiliary verbs)
                while i <= limit and tags[i][1] in ['VERB', 'PRT', 'ADV']:
                    tmp.write(tags[i][0]+' ')
                    t = (tags[i][0], tags[i][1])
                    tmp_tags.append(t)
                    i += 1

                # W = (noun | adj | adv | pron | det)
                while i <= limit and tags[i][1] in ['NOUN', 'ADJ', 'ADV',
                                                    'PRON', 'DET']:
                    tmp.write(tags[i][0]+' ')
                    t = (tags[i][0], tags[i][1])
                    tmp_tags.append(t)
                    i += 1

                # P = (prep | particle | inf. marker)
                while i <= limit and tags[i][1] in ['ADP', 'PRT']:
                    tmp.write(tags[i][0]+' ')
                    t = (tags[i][0], tags[i][1])
                    tmp_tags.append(t)
                    i += 1
                # add the build pattern to the list collected patterns
                patterns.append(tmp.getvalue())
                patterns_tags.append(tmp_tags)
            i += 1

        return patterns, patterns_tags


    @staticmethod
    def extract_reverb_patterns_tagged_ptb(tagged_text):
        """
        Extract ReVerb relational patterns
        http://homes.cs.washington.edu/~afader/bib_pdf/emnlp11.pdf
        """

        # The pattern limits the relation to be a verb (e.g., invented),
        # a verb followed immediately by a preposition (e.g., located in),
        # or a verb followed by nouns, adjectives, or adverbs ending in a
        # preposition (e.g., has an atomic weight of).

        # V | V P | V W*P
        # V = verb particle? adv?
        # W = (noun | adj | adv | pron | det)
        # P = (prep | particle | inf. marker)

        patterns = []
        patterns_tags = []
        i = 0
        limit = len(tagged_text)-1
        tags = tagged_text

        verb = ['VB', 'VBD', 'VBD|VBN', 'VBG', 'VBG|NN', 'VBN', 'VBP',
                'VBP|TO', 'VBZ', 'VP']
        adverb = ['RB', 'RBR', 'RBS', 'RB|RP', 'RB|VBG', 'WRB']
        particule = ['POS', 'PRT', 'TO', 'RP']
        noun = ['NN', 'NNP', 'NNPS', 'NNS', 'NN|NNS', 'NN|SYM', 'NN|VBG', 'NP']
        adjectiv = ['JJ', 'JJR', 'JJRJR', 'JJS', 'JJ|RB', 'JJ|VBG']
        pronoun = ['WP', 'WP$', 'PRP', 'PRP$', 'PRP|VBP']
        determiner = ['DT', 'EX', 'PDT', 'WDT']
        adp = ['IN', 'IN|RP']

        # TODO: detect negations
        # ('rejected', 'VBD'), ('a', 'DT'), ('takeover', 'NN')

        while i <= limit:
            tmp = io.StringIO()# opens an "in memory" text file object like tmp = open("myfile.txt", "r", encoding="utf-8")
            #fileName="myfile"+str(i)+".txt"
            vahab_file = open("myfile.txt", "w", encoding="utf-8")#instead of temp just for vahab / not be an inmemory file to debuge
            #all vahab_file file operation is added by vahab to this class
            tmp_tags = []

            # a ReVerb pattern always starts with a verb
            # tags list element forms are ('rejected', 'VBD') then tags[i][1]='VBD' & tags[i][0]='rejected'
            if tags[i][1] in verb:

                tmp.write(tags[i][0]+' ')
                vahab_file.write(tags[i][0]+' ')
                t = (tags[i][0], tags[i][1])
                print(t)
                tmp_tags.append(t)
                i += 1 # token baad az verb dar list tags ra check mikonad ke harf, esm, sefat, .. kodam ast

                # V = verb particle? adv? (also capture auxiliary verbs)
                while i <= limit and (tags[i][1] in verb or tags[i][1] in adverb or tags[i][1] in particule):
                    tmp.write(tags[i][0]+' ')
                    vahab_file.write(tags[i][0] + ' ')
                    t = (tags[i][0], tags[i][1])
                    print(t)
                    tmp_tags.append(t)
                    i += 1

                # W = (noun | adj | adv | pron | det)
                while i <= limit and (tags[i][1] in noun or tags[i][1] in adjectiv or tags[i][1] in adverb or
                                      tags[i][1] in pronoun or tags[i][1] in determiner):
                    tmp.write(tags[i][0]+' ')
                    vahab_file.write(tags[i][0] + ' ')
                    t = (tags[i][0], tags[i][1])
                    print(t)
                    tmp_tags.append(t)
                    i += 1

                # P = (prep | particle | inf. marker)
                while i <= limit and (tags[i][1] in adp or tags[i][1] in particule):
                    tmp.write(tags[i][0]+' ')
                    vahab_file.write(tags[i][0] + ' ')
                    t = (tags[i][0], tags[i][1])
                    print(t)
                    tmp_tags.append(t)
                    i += 1

                # add the build pattern to the list collected patterns
                patterns.append(tmp.getvalue())
                print("tmp.getvalue()=\n",tmp.getvalue())
                patterns_tags.append(tmp_tags)
            i += 1

        # Finally, if the pattern matches multiple adjacent sequences, we merge
        # them into a single relation phrase (e.g.,wants to extend).
        #
        # This refinement enables the model to readily handle relation phrases
        # containing multiple verbs.

        merged_patterns_tags = [
            item for sublist in patterns_tags for item in sublist
            ]
        return merged_patterns_tags

    @staticmethod
    def extract_reverb_patterns_ptb(text):
        """
        Extract ReVerb relational patterns
        http://homes.cs.washington.edu/~afader/bib_pdf/emnlp11.pdf
        """

        # The pattern limits the relation to be a verb (e.g., invented),
        # a verb followed immediately by a preposition (e.g., located in),
        # or a verb followed by nouns, adjectives, or adverbs ending in a
        # preposition (e.g., has an atomic weight of).

        # V | V P | V W*P
        # V = verb particle? adv?
        # W = (noun | adj | adv | pron | det)
        # P = (prep | particle | inf. marker)

        # split text into tokens
        #text_tokens  vahab has changed

        text_tokens = nltk.tokenize.punkt.PunktWordTokenizer().tokenize(text)

        # tag the sentence, using the default NTLK English tagger
        # POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
        tags_ptb = pos_tag(text_tokens)
        patterns = []
        patterns_tags = []
        i = 0
        limit = len(tags_ptb)-1
        tags = tags_ptb

        verb = ['VB', 'VBD', 'VBD|VBN', 'VBG', 'VBG|NN', 'VBN', 'VBP',
                'VBP|TO', 'VBZ', 'VP']
        adverb = ['RB', 'RBR', 'RBS', 'RB|RP', 'RB|VBG', 'WRB']
        particule = ['POS', 'PRT', 'TO', 'RP']
        noun = ['NN', 'NNP', 'NNPS', 'NNS', 'NN|NNS', 'NN|SYM', 'NN|VBG', 'NP']
        adjectiv = ['JJ', 'JJR', 'JJRJR', 'JJS', 'JJ|RB', 'JJ|VBG']
        pronoun = ['WP', 'WP$', 'PRP', 'PRP$', 'PRP|VBP']
        determiner = ['DT', 'EX', 'PDT', 'WDT']
        adp = ['IN', 'IN|RP']

        # match is chosen.

        while i <= limit:
            tmp = StringIO.StringIO()
            tmp_tags = []

            # a ReVerb pattern always starts with a verb
            if tags[i][1] in verb:
                tmp.write(tags[i][0]+' ')
                t = (tags[i][0], tags[i][1])
                tmp_tags.append(t)
                i += 1

                # V = verb particle? adv? (also capture auxiliary verbs)
                while i <= limit and (tags[i][1] in verb or tags[i][1] in adverb or tags[i][1] in particule):
                    tmp.write(tags[i][0]+' ')
                    t = (tags[i][0], tags[i][1])
                    tmp_tags.append(t)
                    i += 1

                # W = (noun | adj | adv | pron | det)
                while i <= limit and (tags[i][1] in noun or tags[i][1] in adjectiv or tags[i][1] in adverb or
                                      tags[i][1] in pronoun or tags[i][1] in determiner):
                    tmp.write(tags[i][0]+' ')
                    t = (tags[i][0], tags[i][1])
                    tmp_tags.append(t)
                    i += 1

                # P = (prep | particle | inf. marker)
                while i <= limit and (tags[i][1] in adp or tags[i][1] in particule):
                    tmp.write(tags[i][0]+' ')
                    t = (tags[i][0], tags[i][1])
                    tmp_tags.append(t)
                    i += 1

                # add the build pattern to the list collected patterns
                patterns.append(tmp.getvalue())
                patterns_tags.append(tmp_tags)
            i += 1

        # Finally, if the pattern matches multiple adjacent sequences, we merge
        # them into a single relation phrase (e.g.,wants to extend).
        # This refinement enables the model to readily handle relation
        # phrases containing multiple verbs.

        merged_patterns_tags = [
            item for sublist in patterns_tags for item in sublist
            ]
        return merged_patterns_tags

    def detect_passive_voice(self, pattern):
        passive_voice = False

        # TODO: there more complex exceptions, adjectives or adverbs in between
        # (to be) + (adj|adv) + past_verb + by
        # to be + past verb + by

        if len(pattern) >= 3:
            if pattern[0][1].startswith('V'):
                verb = self.lmtzr.lemmatize(pattern[0][0], 'v')
                if verb in self.aux_verbs:
                    if (pattern[1][1] == 'VBN' or pattern[1][1] == 'VBD') \
                            and pattern[-1][0] == 'by':
                        passive_voice = True

                    # past verb + by
                    elif (pattern[-2][1] == 'VBN' or pattern[-2][1] == 'VBD') \
                            and pattern[-1][0] == 'by':
                        passive_voice = True

                # past verb + by
                elif (pattern[-2][1] == 'VBN' or pattern[-2][1] == 'VBD') \
                        and pattern[-1][0] == 'by':
                        passive_voice = True

        # past verb + by
        elif len(pattern) >= 2:
            if (pattern[-2][1] == 'VBN' or pattern[-2][1] == 'VBD') \
                    and pattern[-1][0] == 'by':
                passive_voice = True

        return passive_voice


def main():
    reverb = ReverbVahab()
    line="The 2016 election represented the president Donald Trump's greatest triumph, his life's work: Proving that all the elites who mocked him or said he couldn't do something were mistaken all along. They had to eat their words. He was right. Everyone else was wrong. The end."
    tokens = word_tokenize(line.strip())
    print(tokens)
    tokens_tagged = pos_tag(tokens)
    for token in tokens_tagged:
        print(token[1])
    print(tokens_tagged)
    print("patternTag=\n")
    pattern_tags = reverb.extract_reverb_patterns_tagged_ptb(tokens_tagged)
    print(pattern_tags)
    if reverb.detect_passive_voice(pattern_tags):
        print("Passive Voice: True")
    else:
        print("Passive Voice: False")
    print("\n")

if __name__ == "__main__":
    main()