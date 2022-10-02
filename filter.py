class Filter:
     def __intit__(self,string):
          self.string = string

     def filter(self):
          garbage = ['that', 'with', 'by', 'our', 'we', 'as', 'is','from', 'data', 'within', 'also', 'were', 'between', 'We', 'Which','', 'the', 'and', 'of', 'to', 'in', 'a', 'for','or', ',', 'than','another', 'method','on','K', 'm/s','results','at','The','this','et\xa0','This','shown', 'shows', ':','an','0', 'be','Space', '±','~', 'For','are','observed', 'was','In','km','cases', 'line', 'can','range', 'obtained', 'mean', '1','2','3','4','5','6','7','8','9','10','Materials', 'ProcessingNASA-Langley', 'has','al','Research', '\x0cAdvanced',]
          str_arr = self.string.split('  ')
          res = ' '
          for s in str_arr:
               if not s in garbage:
                    res += str+" "
          return res

     def filter_for(self):
          str_arr = self.string.split(',')
          res = ' '
          for s in str_arr:
               res += str+' '
          return res
