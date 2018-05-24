import wikipedia

class RequestWikiApi:
    
    def __init__(self, request):
        self.request = request

    @property
    def summary_extr(self):
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

if __name__ == '__main__':
    req = [RequestWikiApi('louvre'), RequestWikiApi('wqewr'), RequestWikiApi('openclassroom')]
    for r in req:
        print('---------------------------')
        print(r.summary_extr)
