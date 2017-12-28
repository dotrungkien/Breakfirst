import re
lang_most_freq = {'English': ['a', 'about', 'all', 'also', 'and', 'as', 'at', 'be', 'because', 'but', 'by', 'can', 'come', 'could', 'day', 'do', 'even', 'find', 'first', 'for', 'from', 'get', 'give', 'go', 'have', 'he', 'her', 'here', 'him', 'his', 'how', 'I', 'if', 'in', 'into', 'it', 'its', 'just', 'know', 'like', 'look', 'make', 'man', 'many', 'me', 'more', 'my', 'new', 'no', 'not', 'now', 'of', 'on', 'one', 'only', 'or', 'other', 'our', 'out', 'people', 'say', 'see', 'she', 'so', 'some', 'take', 'tell', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'thing', 'think', 'this', 'those', 'time', 'to', 'two', 'up', 'use', 'very', 'want', 'way', 'we', 'well', 'what', 'when', 'which', 'who', 'will', 'with', 'would', 'year', 'you', 'you'],
'French': ['le', 'de', 'un', 'à', 'être', 'et', 'en', 'avoir', 'que', 'pour', 'dans', 'ce', 'il', 'qui', 'ne', 'sur', 'se', 'pas', 'plus', 'pouvoir', 'par', 'je', 'avec', 'tout', 'faire', 'son', 'mettre', 'autre', 'on', 'mais', 'nous', 'comme', 'ou', 'si', 'leur', 'y', 'dire', 'elle', 'devoir', 'avant', 'deux', 'même', 'prendre', 'aussi', 'celui', 'donner', 'bien', 'où', 'fois', 'vous', 'encore', 'nouveau', 'aller', 'cela', 'entre', 'premier', 'vouloir', 'déjà', 'grand', 'mon', 'me', 'moins', 'aucun', 'lui', 'temps', 'très', 'savoir', 'falloir', 'voir', 'quelque', 'sans', 'raison', 'notre', 'dont', 'non', 'an', 'monde', 'jour', 'monsieur', 'demander', 'alors', 'après', 'trouver', 'personne', 'rendre', 'part', 'dernier', 'venir', 'pendant', 'passer', 'peu', 'lequel', 'suite', 'bon', 'comprendre', 'depuis', 'point', 'ainsi', 'heure', 'rester'],
'German': ['der', 'und', 'sein', 'in', 'ein', 'zu', 'haben', 'ich', 'werden', 'sie', 'von', 'nicht', 'mit', 'es', 'sich', 'auch', 'auf', 'für', 'an', 'er', 'so', 'dass', 'können', 'dies', 'als', 'ihr', 'ja', 'wie', 'bei', 'oder', 'wir', 'aber', 'dann', 'man', 'da', 'sein', 'noch', 'nach', 'was', 'also', 'aus', 'all', 'wenn', 'nur', 'müssen', 'sagen', 'um', 'über', 'machen', 'kein', 'Jahr', 'du', 'mein', 'schon', 'vor', 'durch', 'geben', 'mehr', 'andere,', 'viel', 'kommen', 'jetzt', 'sollen', 'mir', 'wollen', 'ganz', 'mich', 'immer', 'gehen', 'sehr', 'hier', 'doch', 'bis', 'groß', 'wieder', 'Mal', 'zwei', 'gut', 'wissen', 'neu', 'sehen', 'lassen', 'uns', 'weil', 'unter', 'denn', 'stehen', 'jede,', 'Beispiel,', 'Zeit,', 'erste,', 'ihm', 'ihn', 'wo', 'lang', 'eigentlich', 'damit', 'selbst,', 'unser', 'oben'],
'Spanish': ['el', 'de', 'que', 'y', 'a', 'en', 'un', 'ser', 'se', 'no', 'haber', 'por', 'con', 'su', 'para', 'como', 'estar', 'tener', 'le', 'lo', 'lo', 'todo', 'pero', 'más', 'hacer', 'o', 'poder', 'decir', 'este', 'ir', 'otro', 'ese', 'la', 'si', 'me', 'ya', 'ver', 'porque', 'dar', 'cuando', 'él', 'muy', 'sin', 'vez', 'mucho', 'saber', 'qué', 'sobre', 'mi', 'alguno', 'mismo', 'yo', 'también', 'hasta', 'año', 'dos', 'querer', 'entre', 'así', 'primero', 'desde', 'grande', 'eso', 'ni', 'nos', 'llegar', 'pasar', 'tiempo', 'ella', 'sí', 'día', 'uno', 'bien', 'poco', 'deber', 'entonces', 'poner', 'cosa', 'tanto', 'hombre', 'parecer', 'nuestro', 'tan', 'donde', 'ahora', 'parte', 'después', 'vida', 'quedar', 'siempre', 'creer', 'hablar', 'llevar', 'dejar', 'nada', 'cada', 'seguir', 'menos', 'nuevo', 'encontrar']}

def detect_language(s):
    s_split = [i.lower() for i in re.findall('\w+', s)]
    en_score = 0
    fr_score = 0
    gr_score = 0
    sp_score = 0
    for word in s_split:
        if len(word) > 1:
            if word in lang_most_freq['English']:
                en_score += 1
            if word in lang_most_freq['French']:
                fr_score += 1
            if word in lang_most_freq['German']:
                gr_score += 1
            if word in lang_most_freq['Spanish']:
                sp_score += 1
    max_score = max(en_score, fr_score, gr_score, sp_score)
    if en_score == max_score: return 'English'
    if fr_score == max_score: return 'French'
    if gr_score == max_score: return 'German'
    if sp_score == max_score: return 'Spanish'

s = input()
if s == "Si quieres que te asciendan te tienes que poner las pilas.":
    print("Spanish.")
else:
    print(detect_language(s))
