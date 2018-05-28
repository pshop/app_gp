import wikipedia

class RequestWikiApi:
    
    def __init__(self, request):
        """
        request is a str that will be used in the method summary_extr 
        TESTED
        """
        self.request = str(request)

    @property
    def summary_extr(self):
        """ Returns the first three sentences of the wikipedia article of the str(request)
        argument, if Something goes wrong or API is Down, returns null """
        wikipedia.set_lang('fr')

        try :
            w_summ = wikipedia.summary(self.request, sentences=3, auto_suggest=True)
            return w_summ
        except wikipedia.exceptions.DisambiguationError as e:
            try :
                w_summ = wikipedia.summary(e.options[1], sentences=3, auto_suggest=True)
                return w_summ
            except wikipedia.exceptions.DisambiguationError:
                return None
        except (wikipedia.exceptions.PageError , ValueError):
            return None
