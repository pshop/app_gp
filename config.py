import os

class Config():
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

class ConfigGoogle():
    private_key = 'AIzaSyD9OHJRmPNC4QXz_fKRLLHepBpIOA0v8-I'

    PLACES_API_ARGS = {
        "query": None,
        "key": private_key
    }
    PLACES_API_BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    PLACES_NEAR_API_ARGS = {
        "key" : private_key,
        "location": None,
        "keyword": None,
        "rankby":"distance"
    }
    PLACES_NEAR_BASE_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    AUTOCOMP_API_ARGS = {
        "key" : private_key,
        "input" : None,
        "location":None
    }

    AUTOCOMP_BASE_URL = "https://maps.googleapis.com/maps/api/place/autocomplete/json"

    LOCATE_API_KEY = {
        "key":'AIzaSyA1fMrD5e0vqYGT2CKp9NbI7QhDBFlfxBg'
    }
    LOCATE_API_BASE_URL = "https://www.googleapis.com/geolocation/v1/geolocate"



class ConfigParser():
    STOP_WORDS = ["a","stp","hasard", "où", "sais","adresse", "grandpybot", "grandpy", "papy", "vieux", "connait", "connais", "parler",
                  "entendu", "hello", "bonjour", "salut", "abord", "GrandpyBot", "absolument", "afin", "ah",
                  "ai", "aie", "ailleurs", "ainsi", "ait", "allaient", "allo", "allons", "allô", "alors",
                  "anterieur", "anterieure", "anterieures", "apres", "après", "as", "assez", "attendu", "au",
                  "aucun", "aucune", "aujourd", "aujourd'hui", "aupres", "auquel", "aura", "auraient",
                  "aurait", "auront", "aussi", "autre", "autrefois", "autrement", "autres", "autrui", "aux",
                  "auxquelles", "auxquels", "avaient", "avais", "avait", "avant", "avec", "avoir", "avons",
                  "ayant", "b", "bah", "bas", "basee", "bat", "beau", "beaucoup", "bien", "bigre", "boum",
                  "bravo", "brrr", "c", "car", "ce", "ceci", "cela", "celle", "celle-ci", "celle-là", "celles",
                  "celles-ci", "celles-là", "celui", "celui-ci", "celui-là", "cent", "cependant", "certain",
                  "certaine", "certaines", "certains", "certes", "ces", "cet", "cette", "ceux", "ceux-ci",
                  "ceux-là", "chacun", "chacune", "chaque", "cher", "chers", "chez", "chiche", "chut", "chère",
                  "chères", "ci", "cinq", "cinquantaine", "cinquante", "cinquantième", "cinquième", "clac",
                  "clic", "combien", "comme", "comment", "comparable", "comparables", "compris", "concernant",
                  "contre", "couic", "crac", "d", "da", "dans", "de", "debout", "dedans", "dehors", "deja",
                  "delà", "depuis", "dernier", "derniere", "derriere", "derrière", "des", "desormais",
                  "desquelles", "desquels", "dessous", "dessus", "deux", "deuxième", "deuxièmement", "devant",
                  "devers", "devra", "different", "differentes", "differents", "différent", "différente",
                  "différentes", "différents", "dire", "directe", "directement", "dit", "dite", "dits",
                  "divers", "diverse", "diverses", "dix", "dix-huit", "dix-neuf", "dix-sept", "dixième",
                  "doit", "doivent", "donc", "dont", "douze", "douzième", "dring", "du", "duquel", "durant",
                  "dès", "désormais", "e", "effet", "egale", "egalement", "egales", "eh", "elle", "elle-même",
                  "elles", "elles-mêmes", "en", "encore", "enfin", "entre", "envers", "environ", "es", "est",
                  "et", "etant", "etc", "etre", "eu", "euh", "eux", "eux-mêmes", "exactement", "excepté",
                  "extenso", "exterieur", "f", "fais", "faisaient", "faisant", "fait", "façon", "feront", "fi",
                  "flac", "floc", "font", "g", "gens", "h", "ha", "hein", "hem", "hep", "hi", "ho", "holà",
                  "hop", "hormis", "hors", "hou", "houp", "hue", "hui", "huit", "huitième", "hum", "hurrah",
                  "hé", "hélas", "i", "il", "ils", "importe", "j", "je", "jusqu", "jusque", "juste", "k", "l",
                  'la', "laisser", "laquelle", "las", "le", "lequel", "les", "lesquelles", "lesquels", "leur",
                  "leurs", "longtemps", "lors", "lorsque", "lui", "lui-meme", "lui-même", "là", "lès", "m",
                  "ma", "maint", "maintenant", "mais", "malgre", "malgré", "maximale", "me", "meme", "memes",
                  "merci", "mes", "mien", "mienne", "miennes", "miens", "mille", "mince", "minimale", "moi",
                  "moi-meme", "moi-même", "moindres", "moins", "mon", "moyennant", "multiple", "multiples",
                  "même", "mêmes", "n", "na", "naturel", "naturelle", "naturelles", "ne", "neanmoins",
                  "necessaire", "necessairement", "neuf", "neuvième", "ni", "nombreuses", "nombreux", "non",
                  "nos", "notamment", "notre", "nous", "nous-mêmes", "nouveau", "nul", "néanmoins", "nôtre",
                  "nôtres", "o", "oh", "ohé", "ollé", "olé", "on", "ont", "onze", "onzième", "ore", "ou",
                  "ouf", "ouias", "oust", "ouste", "outre", "ouvert", "ouverte", "ouverts", "o|", "où", "p",
                  "paf", "pan", "par", "parce", "parfois", "parle", "parlent", "parler", "parmi", "parseme",
                  "partant", "particulier", "particulière", "particulièrement", "pas", "passé", "pendant",
                  "pense", "permet", "personne", "peu", "peut", "peuvent", "peux", "pff", "pfft", "pfut",
                  "pif", "pire", "plein", "plouf", "plus", "plusieurs", "plutôt", "possessif", "possessifs",
                  "possible", "possibles", "pouah", "pour", "pourquoi", "pourrais", "pourrait", "pouvait",
                  "prealable", "precisement", "premier", "première", "premièrement", "pres", "probable",
                  "probante", "procedant", "proche", "près", "psitt", "pu", "puis", "puisque", "pur", "pure",
                  "q", "qu", "quand", "quant", "quant-à-soi", "quanta", "quarante", "quatorze", "quatre",
                  "quatre-vingt", "quatrième", "quatrièmement", "que", "quel", "quelconque", "quelle",
                  "quelles", "quelqu'un", "quelque", "quelques", "quels", "qui", "quiconque", "quinze", "quoi",
                  "quoique", "r", "rare", "rarement", "rares", "relative", "relativement", "remarquable",
                  "rend", "rendre", "restant", "reste", "restent", "restrictif", "retour", "revoici",
                  "revoilà", "rien", "s", "sa", "sacrebleu", "sait", "sans", "sapristi", "sauf", "se", "sein",
                  "seize", "selon", "semblable", "semblaient", "semble", "semblent", "sent", "sept",
                  "septième", "sera", "seraient", "serait", "seront", "ses", "seul", "seule", "seulement",
                  "si", "sien", "sienne", "siennes", "siens", "sinon", "six", "sixième", "soi", "soi-même",
                  "soit", "soixante", "son", "sont", "sous", "souvent", "specifique", "specifiques",
                  "speculatif", "stop", "strictement", "subtiles", "suffisant", "suffisante", "suffit", "suis",
                  "suit", "suivant", "suivante", "suivantes", "suivants", "suivre", "superpose", "sur",
                  "surtout", "t", "ta", "tac", "tant", "tardive", "te", "tel", "telle", "tellement", "telles",
                  "tels", "tenant", "tend", "tenir", "tente", "tes", "tic", "tien", "tienne", "tiennes",
                  "tiens", "toc", "toi", "toi-même", "ton", "touchant", "toujours", "tous", "tout", "toute",
                  "toutefois", "toutes", "treize", "trente", "tres", "trois", "troisième", "troisièmement",
                  "trop", "très", "tsoin", "tsouin", "tu", "té", "u", "un", "une", "unes", "uniformement",
                  "unique", "uniques", "uns", "v", "va", "vais", "vas", "vers", "via", "vif", "vifs", "vingt",
                  "vivat", "vive", "vives", "vlan", "voici", "voilà", "vont", "vos", "votre", "vous",
                  "vous-mêmes", "vu", "vé", "vôtre", "vôtres", "w", "x", "y", "z", "zut", "à", "â", "ça", "ès",
                  "étaient", "étais", "était", "étant", "été", "être", "ô"]

class ConfigGrandpy:
    missunderstood = [
        "Oulala je me fais vieux, je n'ai pas compris la question.",
        "Qu'entends tu exactement par tartine de nutella ?",
        "Ma mémoire me joue des tours, je ne me souviens plus.",
        "N'hésite pas à parler plus fort pour que je comprenne.",
        "Si c'était la question, oui je vais bien, merci :)",
        "N'hésite pas à simplifier ta question au maximum, j'ai un petit cerveau."
    ]

    wiki_no_result = [
        "C'est amusant parce que je savais quelque chose là dessus mais j'ai oublié",
        "Ma mémoire me joue des tours... De quoi on parlait déjà ?",
        "Et à propos de cacahuètes j'ai une superbe histoire à te raconter. Ah non."
    ]

    intro_wiki = [
        "Oh et j'ai une superbe histoire à propos de ça, écoute :<br>",
        "Ecoute ce que j'ai à te dire là dessus et tu comprendras pourquoi on m'appelle wikipiedia :<br>",
        "J'ai fait un exposé là dessus quand j'étais en sixième, l'intro donnait ça :<br>"
    ]
    intro_address = [
         "Mon petit, si mes souvenirs sont bons, c'est à cette adresse:<br>",
         "Tu as grandis depuis la dernière fois non ?<br>L'adresse c'est ",
         "Je veux bien de donner l'adresse mais tu restes manger un part de tarte.<br>Ok ? Alors c'est "
    ]

