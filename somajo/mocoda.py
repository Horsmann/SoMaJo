#!/usr/bin/env python3

# A few customizations in tokenization for the mocoda project
# This changes are kept intentionally in a separated file

import collections
import random
import re

class MoCoDa(object):
    
    def __init__(self):
        self.standalone = re.compile("^(\.{1,2})$|^(\?{1,2})$|^(!{1,2})$|^(\+{1,2})|^(-{1,2})$")
    
    def refineTokenization(self, somojaTokenization):
        out = []
    # Two punctuation marks should be separated three or more form a single token
        for i in range(0, len(somojaTokenization)):
            tok = somojaTokenization[i]
            if self.standalone.match(tok):
                for c in tok:
                    out.append(c)
                continue
                 	
            out.append(tok)
    

        return out
    #return list(tokens)


