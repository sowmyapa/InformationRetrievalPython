================================================================================================================================
                                                  How to Execute
================================================================================================================================

1) Go inside the directory in terminal:
   ex : cd /Users/sowmyaparameshwara/college/InformationRetrievalPython/Assignment3
2) Type the following command :
   python3 index.py
3) You will be prompted to enter number of documents to be retrieved (k) :
   Ex : Enter number of documents to be retrieved
        10
4) Exact retrieval method output will be display.
   Ex : output for query :  suggestion made by president kennedy for a nato nuclear missile fleet manned by international crews .
        Document : 89
        Document : 254
        Document : 157
        Document : 247
        Document : 402
        Document : 1
        Document : 135
        Document : 418
        Document : 295
        Document : 38
5) You will be prompted to choose the relevance feedback method:
   Ex: Enter 1 for rocchio user feedback, 2 for psuedo-relevance, anything else to exit
       1
7) For rocchio user feedback, You will be prompted to Enter number of relevant documents :
   Ex : Enter number of relevant documents
        1
8) For rocchio user feedback, You will be prompted to enter relevant doc id(enter doc id from the above ) :
   Ex : Enter relevant docID
       89
9) For rocchio user feedback, You will be prompted to enter number of irrelevant documents :
   Ex : Enter number of irrelevant documents
        1
10) For rocchio user feedback, You will be prompted to enter irrelevant doc id(enter doc id from the above ) :
   Ex : Enter irrelevant docID
        402
11) For rocchio user feedback, new set of relevant documents will be displayed, followed by new query terms.
    Ex : Document : 89
         Document : 135
         Document : 157
         Document : 1
         Document : 254
         Document : 247
         Document : 228
         Document : 402
         Document : 148
         Document : 53
     {'allies': 2.55, 'nato': 4.9, 'deterrent': 3.0, 'old': 1.5, 'disarray': 0.75, 'haunt': 0.75, 'councils': 0.75, 'allied': 0.75, 'differences': 0.75, 'symptoms': 0.75, 'deep': 0.75, 'rooted': 0.75, 'disunity': 0.75, 'result': 0.75, 'military': 0.75, 'effectiveness': 0.75, 'secure': 0.75, 'nuclear': 4.3, 'shield': 0.75, 'european': 1.5, 'nations': 1.2, 'eager': 0.75, 'build': 3.0, 'conventional': 0.6, 'forces': 0.6, 'grown': 0.75, 'powerful': 0.75, 'prosperous': 0.75, 'europeans': 2.1, 'total': 0.6, 'control': 2.55, 'weapons': 2.1, 'foreseeable': 0.75, 'future': 0.75, 'dependence': 0.75, 'breeds': 0.75, 'mistrust': 0.75, 'charles': 0.6, 'de': 1.05, 'gaulle': 0.45, 'fear': 0.75, 'counted': 0.75, 'risk': 0.75, 'destruction': 0.75, 'cities': 0.75, 'russia': 0.6, 'attack': 0.75, 'western': 1.05, 'europe': 5.25, 'repeated': 0.75, 'assurances': 0.75, 'term': 0.75, 'strategic': 0.75, 'commitment': 0.75, 'heedless': 0.75, '400': 0.75, '000': 0.75, 'continent': 0.75, 'permanent': 1.5, 'hostage': 0.75, 'security': 1.5, 'neither': 0.75, 'france': 1.5, 'embryonic': 0.75, 'force': 5.25, 'frappe': 0.75, 'britain': 2.25, 'obsolete': 0.75, 'bomber': 0.75, 'strike': 1.5, 'carries': 0.75, 'sufficient': 0.75, 'punch': 0.75, 'deter': 0.75, 'alone': 0.75, 'defeat': 0.75, 'aggressor': 0.75, 'fine': 1.5, 'watches': 1.5, 'attempt': 0.75, 'soothe': 0.75, 'restiveness': 0.75, 'giving': 2.1, 'greater': 1.35, 'responsibility': 0.75, 'serious': 0.75, 'pitch': 0.75, 'share': 0.6, 'planning': 1.5, 'atomic': 3.0, '15member': 0.75, 'council': 0.75, 'paris': 1.2, 'president': 1.75, 'kennedy': 1.75, 'special': 0.75, 'envoy': 0.75, 'livingston': 0.75, 'merchant': 2.25, 'proposed': 0.6, 'creation': 0.75, 'multinational': 3.0, 'consisting': 0.75, 'fleet': 3.25, 'surface': 1.35, 'ships': 1.35, 'equipped': 0.75, 'polaris': 3.6, 'missile': 2.5, 'key': 1.5, 'provision': 0.75, 'plan': 2.1, 'multimanned': 0.75, 'crews': 3.1, 'drawn': 0.75, 'nation': 1.5, 'willing': 0.75, 'help': 0.75, 'foot': 0.75, 'bill': 0.75, 'cost': 1.5, 'international': 1.75, 'task': 0.75, '2': 0.6, 'billion': 0.75, '200': 0.75, 'missiles': 0.45, 'floating': 0.75, 'launch': 0.75, 'pads': 0.75, 'half': 0.75, 'money': 0.75, 'create': 0.75, 'submarine': 0.75, 'originally': 0.75, 'hastily': 0.75, 'suggested': 0.75, 'multi': 0.75, 'manned': 2.2, 'submarines': 2.25, 'logical': 0.75, 'progression': 0.75, 'independent': 0.75, 'subs': 0.75, 'agreed': 0.75, 'committed': 0.75, 'apart': 0.75, 'congress': 0.75, 'indicated': 0.75, 'dead': 0.75, 'components': 0.75, 'moreover': 0.75, 'naval': 2.25, 'hands': 0.75, 'aghast': 0.75, 'prospect': 1.5, 'manning': 0.75, 'mixed': 0.6, 'nationalities': 0.6, 'warned': 0.75, 'west': 2.85, 'german': 0.75, 'expert': 0.75, 'sub': 0.75, 'warfare': 0.6, 'room': 0.75, 'misunderstanding': 0.75, 'farce': 1.2, 'finger': 0.75, 'trigger': 0.75, 'new': 0.6, 'agrees': 0.75, 'participating': 0.75, 'ally': 0.75, 'equal': 0.75, 'veto': 0.75, 'argument': 0.75, 'provokes': 0.75, 'largely': 0.75, 'academic': 0.75, 'fingers': 0.75, 'unanimous': 0.75, 'believe': 0.6, 'want': 0.75, 'shoot': 0.75, 'sure': 0.75, 'major': 0.75, 'strategist': 0.75, 'considering': 0.75, 'semantics': 0.75, 'voting': 0.75, 'becomes': 0.75, 'irrelevant': 0.75, 'partners': 0.75, 'belgium': 0.75, 'italy': 0.75, 'greece': 0.75, 'netherlands': 0.75, 'turkey': 0.6, 'germany': 1.5, 'immediately': 0.75, 'receptive': 0.75, 'proposal': 1.5, 'expressed': 0.75, 'warmest': 0.75, 'interest': 0.75, 'british': 0.75, 'looked': 0.6, 'scheme': 0.75, 'mild': 0.75, 'benevolence': 0.75, 'wanted': 0.75, 'hear': 0.75, 'allowed': 0.75, 'price': 0.75, 'high': 0.75, 'payoff': 0.75, 'distant': 0.6, 'meanwhile': 0.75, 'fraction': 0.75, 'existing': 0.75, 'stockpile': 0.75, 'remain': 1.5, 'lock': 0.75, 'coldly': 0.75, 'received': 0.75, 'gaullist': 0.75, 'daily': 0.75, 'la': 1.5, 'dubbed': 0.75, 'multilateral': 0.45, 'multilaterale': 0.75, 'touted': 0.75, 'significant': 0.75, 'boost': 0.75, 'gibe': 0.75, 'justified': 0.75, 'joke': 0.75, 'flat': 0.75, 'jointly': 1.5, 'financed': 0.75, 'armada': 0.75, 'offer': 0.75, 'solid': 0.75, 'benefits': 0.75, 'arts': 1.5, 'course': 0.75, 'allow': 0.75, 'collaborate': 0.75, 'scratch': 0.75, 'targeting': 0.75, 'contingency': 0.75, 'satisfy': 0.75, 'acute': 0.75, 'desire': 0.75, 'knowhow': 0.75, 'thorough': 0.75, 'education': 0.75, 'complex': 0.75, 'technological': 0.75, 'financial': 0.75, 'realities': 0.75, 'sides': 0.75, 'provide': 0.45, 'substantial': 0.75, 'token': 0.75, 'determination': 0.75, 'defend': 0.75, 'ultimate': 0.75, 'weapon': 0.75, 'defense': 0.45, 'planner': 0.75, 'glue': 0.75, 'alliance': 0.75, 'prepared': 0.75, 'leave': 0.75, 'series': 0.75, 'briefings': 0.75, 'rome': 0.75, 'brussels': 0.75, 'bonn': 0.75, 'london': 0.75, 'diplomat': 0.75, 'pointed': 0.75, 'incentive': 0.75, 'participate': 0.75, 'contribute': 0.75, 'french': 0.30000000000000004, 'suggestion': 1.0}
12) Press 3 to exit rocchio iteration for this query. Anything else to proceed with next iteration.
13) For psuedo-relevance, after step 5, please choose option 2, the new relevant documents along with new query will be displayed.
    Ex: Document : 89
        Document : 157
        Document : 254
        Document : 135
        Document : 1
        Document : 247
        Document : 402
        Document : 228
        Document : 54
        Document : 148
        {'allies': 2.25, 'nato': 5.0, 'deterrent': 1.25, 'old': 0.75, 'disarray': 0.25, 'haunt': 0.25, 'councils': 0.5, 'allied': 1.25, 'differences': 0.25, 'symptoms': 0.25, 'deep': 0.25, 'rooted': 0.25, 'disunity': 0.25, 'result': 0.25, 'military': 1.0, 'effectiveness': 0.25, 'secure': 0.25, 'nuclear': 4.25, 'shield': 0.25, 'european': 0.75, 'nations': 0.75, 'eager': 0.25, 'build': 1.0, 'conventional': 0.25, 'forces': 0.5, 'grown': 0.25, 'powerful': 0.25, 'prosperous': 0.25, 'europeans': 1.0, 'total': 0.25, 'control': 1.25, 'weapons': 1.5, 'foreseeable': 0.25, 'future': 0.5, 'dependence': 0.25, 'breeds': 0.25, 'mistrust': 0.25, 'charles': 1.0, 'de': 2.25, 'gaulle': 1.5, 'fear': 0.25, 'counted': 0.25, 'risk': 0.25, 'destruction': 0.25, 'cities': 0.25, 'russia': 0.25, 'attack': 0.25, 'western': 1.0, 'europe': 3.25, 'repeated': 0.25, 'assurances': 0.25, 'term': 0.5, 'strategic': 0.25, 'commitment': 0.25, 'heedless': 0.25, '400': 0.25, '000': 0.25, 'continent': 0.25, 'permanent': 0.5, 'hostage': 0.25, 'security': 0.75, 'neither': 0.25, 'france': 2.25, 'embryonic': 0.25, 'force': 4.5, 'frappe': 0.5, 'britain': 2.0, 'obsolete': 0.25, 'bomber': 0.25, 'strike': 0.75, 'carries': 0.25, 'sufficient': 0.25, 'punch': 0.25, 'deter': 0.5, 'alone': 0.5, 'defeat': 0.25, 'aggressor': 0.25, 'fine': 0.5, 'watches': 0.5, 'attempt': 0.25, 'soothe': 0.25, 'restiveness': 0.25, 'giving': 0.75, 'greater': 0.75, 'responsibility': 0.75, 'serious': 0.25, 'pitch': 0.25, 'share': 0.5, 'planning': 0.75, 'atomic': 1.0, '15member': 0.25, 'council': 0.25, 'paris': 2.0, 'president': 1.5, 'kennedy': 1.5, 'special': 0.25, 'envoy': 0.25, 'livingston': 0.25, 'merchant': 0.75, 'proposed': 0.25, 'creation': 0.25, 'multinational': 1.0, 'consisting': 0.25, 'fleet': 2.75, 'surface': 1.0, 'ships': 0.5, 'equipped': 0.25, 'polaris': 3.0, 'missile': 2.0, 'key': 0.5, 'provision': 0.25, 'plan': 1.5, 'multimanned': 0.5, 'crews': 2.25, 'drawn': 0.25, 'nation': 0.5, 'willing': 0.5, 'help': 0.25, 'foot': 0.25, 'bill': 0.25, 'cost': 0.75, 'international': 1.25, 'task': 0.5, '2': 0.5, 'billion': 0.75, '200': 0.25, 'missiles': 0.75, 'floating': 0.25, 'launch': 0.25, 'pads': 0.25, 'half': 0.25, 'money': 0.75, 'create': 0.5, 'submarine': 0.75, 'originally': 0.25, 'hastily': 0.25, 'suggested': 0.25, 'multi': 0.25, 'manned': 2.0, 'submarines': 1.5, 'logical': 0.25, 'progression': 0.25, 'independent': 0.75, 'subs': 0.5, 'agreed': 0.5, 'committed': 1.0, 'apart': 0.25, 'congress': 0.25, 'indicated': 0.5, 'dead': 0.25, 'components': 0.25, 'moreover': 0.25, 'naval': 1.0, 'hands': 0.25, 'aghast': 0.25, 'prospect': 0.5, 'manning': 0.25, 'mixed': 0.75, 'nationalities': 0.25, 'warned': 0.25, 'west': 1.5, 'german': 1.25, 'expert': 0.25, 'sub': 0.25, 'warfare': 0.25, 'room': 0.25, 'misunderstanding': 0.25, 'farce': 0.5, 'finger': 0.25, 'trigger': 0.25, 'new': 0.5, 'agrees': 0.25, 'participating': 0.25, 'ally': 0.25, 'equal': 0.5, 'veto': 0.25, 'argument': 0.25, 'provokes': 0.25, 'largely': 0.25, 'academic': 0.25, 'fingers': 0.25, 'unanimous': 0.25, 'believe': 0.5, 'want': 0.25, 'shoot': 0.25, 'sure': 0.25, 'major': 0.25, 'strategist': 0.25, 'considering': 0.25, 'semantics': 0.25, 'voting': 0.25, 'becomes': 0.25, 'irrelevant': 0.25, 'partners': 0.5, 'belgium': 0.25, 'italy': 0.5, 'greece': 0.25, 'netherlands': 0.25, 'turkey': 0.25, 'germany': 1.25, 'immediately': 0.25, 'receptive': 0.25, 'proposal': 0.5, 'expressed': 0.5, 'warmest': 0.25, 'interest': 0.25, 'british': 2.0, 'looked': 0.25, 'scheme': 0.5, 'mild': 0.25, 'benevolence': 0.25, 'wanted': 0.25, 'hear': 0.25, 'allowed': 0.25, 'price': 0.25, 'high': 0.75, 'payoff': 0.25, 'distant': 0.25, 'meanwhile': 0.25, 'fraction': 0.25, 'existing': 0.25, 'stockpile': 0.25, 'remain': 0.5, 'lock': 0.25, 'coldly': 0.25, 'received': 0.25, 'gaullist': 0.5, 'daily': 0.25, 'la': 0.5, 'dubbed': 0.25, 'multilateral': 0.5, 'multilaterale': 0.25, 'touted': 0.25, 'significant': 0.25, 'boost': 0.25, 'gibe': 0.25, 'justified': 0.25, 'joke': 0.25, 'flat': 0.25, 'jointly': 0.5, 'financed': 0.25, 'armada': 0.25, 'offer': 1.0, 'solid': 0.25, 'benefits': 0.25, 'arts': 0.5, 'course': 1.0, 'allow': 0.25, 'collaborate': 0.25, 'scratch': 0.25, 'targeting': 0.25, 'contingency': 0.25, 'satisfy': 0.25, 'acute': 0.25, 'desire': 0.25, 'knowhow': 0.25, 'thorough': 0.25, 'education': 0.25, 'complex': 0.25, 'technological': 0.25, 'financial': 0.75, 'realities': 0.25, 'sides': 0.25, 'provide': 0.25, 'substantial': 0.5, 'token': 0.25, 'determination': 0.25, 'defend': 0.25, 'ultimate': 0.5, 'weapon': 0.25, 'defense': 1.25, 'planner': 0.25, 'glue': 0.25, 'alliance': 0.5, 'prepared': 0.25, 'leave': 0.25, 'series': 0.25, 'briefings': 0.25, 'rome': 0.25, 'brussels': 0.25, 'bonn': 0.25, 'london': 0.75, 'diplomat': 0.5, 'pointed': 0.5, 'incentive': 0.25, 'participate': 0.25, 'contribute': 0.25, 'french': 1.0, 'horse': 0.5, 'top': 0.5, 'officials': 1.0, 'listened': 0.25, 'politely': 0.25, 'navy': 0.25, 'argued': 0.5, 'merits': 0.25, 'firing': 0.25, 'britons': 0.25, 'real': 0.5, 'feelings': 0.25, 'mlf': 1.5, 'sardonic': 0.25, 'limerick': 0.25, 'rounds': 0.25, 'whitehall': 0.25, 'hooray': 0.25, 'multimixed': 0.25, 'yankee': 0.25, 'produces': 0.25, 'knight': 0.25, 'fight': 0.25, 'efforts': 0.25, 'sell': 0.25, 'ill': 0.25, 'concealed': 0.25, 'washington': 0.75, 'either': 0.25, 'privately': 0.25, 'pentagon': 0.5, 'considers': 0.25, 'gimmick': 0.5, 'postpone': 0.25, 'proliferation': 0.25, 'wants': 0.25, 'costs': 0.25, 'prevent': 0.25, 'delay': 0.25, 'monstrous': 0.5, 'nonsense': 0.5, 'charged': 0.25, 'halfhearted': 0.25, 'mission': 0.25, 'winning': 0.25, 'support': 0.5, '5': 0.25, 'admiral': 0.25, 'claude': 0.25, 'ricketts': 0.5, 'deputy': 0.25, 'chief': 0.25, 'operations': 0.25, 'doubled': 0.25, 'late': 0.25, 'multimixmaster': 0.25, 'strategically': 0.25, '25': 0.25, 'vessels': 0.25, 'cruising': 0.25, 'shallow': 0.25, 'coastal': 0.25, 'waters': 0.25, 'easily': 0.25, 'destroyed': 0.25, 'soviet': 0.25, 'aircraft': 0.5, 'additional': 0.25, 'system': 0.25, 'enhances': 0.25, 'credibility': 0.25, 'systems': 0.25, 'marshal': 0.25, 'sir': 0.25, 'john': 0.25, 'slessor': 0.25, 'state': 0.5, 'department': 0.25, 'main': 0.25, 'justification': 0.25, 'political': 0.5, 'aimed': 0.25, 'primarily': 0.25, 'satisfying': 0.25, 'demand': 0.5, 'voice': 0.25, 'germans': 0.25, 'pledged': 0.25, 'match': 0.25, 'shoulder': 0.25, '40': 0.25, 'backing': 0.25, 'drawing': 0.25, 'board': 0.25, 'building': 0.25, '1': 0.25, '1970': 0.5, 'reply': 0.25, 'afford': 0.25, 'pour': 0.25, 'anything': 0.25, 'theoretical': 0.25, 'telling': 0.25, 'objection': 0.25, 'project': 0.25, 'chip': 0.25, 'rest': 0.25, 'administration': 0.5, 'hopes': 0.5, 'nonetheless': 0.25, 'win': 0.5, 'certainly': 0.25, 'don': 0.25, 'explained': 0.25, 'ranking': 0.5, 'official': 0.5, 'satisfies': 0.25, 'think': 0.25, 'worth': 0.25, 'pursuing': 0.25, 'doesn': 0.25, 'merely': 0.25, 'obscured': 0.25, 'ought': 0.25, 'policy': 0.5, 'truly': 0.25, 'united': 0.25, 'full': 0.25, 'goal': 0.25, 'achieved': 0.25, 're': 0.25, 'speaking': 0.5, 'thaw': 0.25, 'cried': 0.25, 'headlines': 0.25, 'operation': 0.25, 'charm': 0.25, 'purred': 0.25, 'press': 0.25, 'news': 0.25, 'terms': 0.25, 'attend': 0.25, 'meeting': 0.75, 'south': 0.25, 'east': 0.25, 'asia': 0.25, 'treaty': 0.25, 'organization': 0.25, 'secretary': 0.75, 'dean': 0.25, 'rusk': 0.5, 'chatted': 0.25, 'cordially': 0.25, '35': 0.25, 'minutes': 0.25, 'counting': 0.25, 'translation': 0.25, 'foreign': 0.5, 'lord': 0.25, 'home': 0.25, 'minister': 0.25, 'maurice': 0.25, 'couve': 0.25, 'murville': 0.25, 'snubbing': 0.25, 'excluded': 0.25, 'common': 0.25, 'market': 0.25, 'january': 0.5, 'exchanged': 0.25, 'civilities': 0.25, 'elysee': 0.25, 'palace': 0.25, 'reception': 0.25, 'seato': 0.25, 'delegates': 0.25, 'countries': 0.5, 'le': 0.25, 'grand': 0.25, 'affably': 0.25, 'cooperation': 0.5, 'please': 0.25, 'progress': 0.25, 'skeptics': 0.25, 'noted': 0.25, 'government': 0.25, 'inclined': 0.25, 'talk': 0.25, 'practice': 0.25, 'indicating': 0.25, 'honor': 0.25, '15': 0.25, 'agreement': 0.5, 'accept': 0.25, 'controlled': 0.25, 'warheads': 0.25, 'based': 0.25, '100': 0.25, 'fighterbombers': 0.25, 'brusquely': 0.25, 'denied': 0.25, 'present': 0.5, 'plans': 0.5, 'concerning': 0.25, 'planes': 0.25, 'within': 0.25, 'daunted': 0.25, 'leaked': 0.25, 'wishful': 0.25, 'reports': 0.25, 'badly': 0.25, 'schedule': 0.75, 'beset': 0.25, 'evermounting': 0.25, 'technical': 0.25, 'problems': 0.25, 'hinted': 0.25, 'ready': 0.25, 'return': 0.25, 'fold': 0.25, 'retorted': 0.25, 'insisted': 0.25, '50': 0.25, 'mirage': 0.25, 'iv': 0.25, 'bombers': 0.5, 'service': 0.25, 'december': 0.25, '1965': 0.25, 'expects': 0.25, 'bomb': 0.25, 'ahead': 0.25, 'launching': 0.25, 'due': 0.25, '1968': 0.5, 'reason': 0.25, 'away': 0.25, 'aim': 0.25, 'independence': 0.25, 'presse': 0.25, 'greatly': 0.25, 'changed': 0.25, 'tone': 0.25, 'general': 0.5, 'rejected': 0.25, 'pushing': 0.25, 'enthusiasm': 0.25, 'enthusiastic': 0.25, 'rather': 0.25, 'sink': 0.25, 'excluding': 0.25, 'outline': 0.25, 'limited': 0.25, 'inter': 0.5, 'natocontrolled': 0.25, 'just': 0.25, 'session': 0.25, 'conferences': 0.25, 'attended': 0.25, 'mcnamara': 0.25, 'policymakers': 0.25, 'announced': 0.25, 'next': 0.25, 'ottawa': 0.25, 'detailed': 0.25, 'command': 0.25, 'structure': 0.25, 'integrate': 0.25, 'include': 0.25, 'planners': 0.25, 'dismissed': 0.25, 'proposals': 0.25, 'mere': 0.25, 'gimmickry': 0.25, 'clamoring': 0.25, 'role': 0.25, 'produced': 0.25, 'anxious': 0.25, 'cooperate': 0.25, 'remained': 0.25, 'stiffly': 0.25, 'aloof': 0.25, 'suggesting': 0.25, 'event': 0.25, 'war': 0.25, 'coordinated': 0.25, 'believed': 0.25, 'shown': 0.25, 'positive': 0.25, 'attitude': 0.25, 'gravely': 0.25, 'misjudged': 0.25, 'aims': 0.25, 'snapped': 0.25, 'crisis': 0.25, 'isn': 0.25, 'won': 0.25, 'suggestion': 1.0}
14) Press 3 to exit psuedo relevance feedback iteration for this query. Anything else to proceed with next iteration.

15) After processing all queries, it will ask if you wish to print dictionary (Enter 'y' if you wish to print else 'n'):
   Ex : Do you want to print dictionary (y/n)
        y
16) It outputs dictionary and asks if you wish to print docID to fileName mapping (Enter 'y' if you wish to print else 'n'):
   Ex : Do you want to print doc id to file name list (y/n)
        y
17) It outputs the docID to filename mapping.
18) Rerun the program, with command "python3 index.py", to run for a different relevance feedback type.

Please note :
1) In one run of the code you can run only relevance feedback method per query : User feedback or psuedo feedback.
2) Queries are picked from file : "/Users/sowmyaparameshwara/college/InformationRetrievalPython/Assignment3/queries.txt"
   new line is assumed as the delimiter across queries (Each line holds one query).

================================================================================================================================
                                                      Refer
================================================================================================================================

 1) Sample queries :
    queries.txt
 2) Output generated by my code :
    output.txt

================================================================================================================================
                                                    Index Structure
================================================================================================================================
           "{"term1": {"idf":1.0,
                    "docIDs":{
                              "1":{"wtd":1.3,
                                   "positions":[101,103,230]
                                   },
                              "15":{"wtd":1.2,
                                    "positions":[25,30]
                                   }
                              }
                   },
             "term2": {"idf":1.2,
                      "docIDs":{
                              "5":{"wtd":1.3,
                                   "positions":[101,103,230]
                                   },
                              "10":{"wtd":1.2,
                                    "positions":[25,30]
                                   }
                              }
                   }
            }

================================================================================================================================
