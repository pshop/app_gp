import wikipedia

class RequestWikiApi:
    
    def __init__(self, request):
        self.request = request

    @property
    def wiki_sum(self):

        wikipedia.set_lang('fr')
        search = wikipedia.search(self.request)

        try:
            summary = wikipedia.summary(search[0])
        except IndexError:
            return False

        splited_sum = summary.split('.')
        wiki_sum = ''
        i = 0

        for sentence in splited_sum:
            if i < 3:
                wiki_sum += sentence + '.'
                i += 1
            else:
                break

        return wiki_sum





if __name__ == '__main__':
    wikipedia.set_lang('fr')
    search = wikipedia.search('sdfgsdfg')
    summary = wikipedia.summary(search[0])
    splited_sum = summary.split('.')
    wiki_sum = ''
    i = 0
    for sentence in splited_sum:
        if i < 3:
            wiki_sum += sentence + '.'
            i += 1
        else:
            break
    print(wiki_sum)
