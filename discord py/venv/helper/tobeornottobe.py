def tier_1_pos():
    tier_1_pos_word = [
        "like", "enjoy", "appreciate", "prefer", "admire", "respect", "consider", "value", 
        "approve", "support", "fond", "care", "accept", "interested", "inclined", "grateful", 
        "affection", "partial", "content", "delight", "happy", "cheer", "thankful", "comfortable", 
        "relish", "praise", "esteem", "fondness", "mildly", "glad", "satisfied", "calm", 
        "charmed", "please", "agree", "positive", "welcome", "acclaim", "commend", "delightful",
        "hopeful", "thrilled", "inspired", "nice", "grateful", "pleasant", "excited", "jovial", 
        "cheerful", "good", "suitable", "fun", "great", "contented", "savor", "heartwarming", 
        "uplifted", "successful", "upbeat", "affirmative", "lighthearted", "thank", "optimistic", 
        "eager", "joyful", "warm", "in favor", "blessed", "tickled", "lovely", "excited", "rejoice", 
        "blissful", "joyous", "positive feeling", "refreshing", "relieved", "beaming", "grinning", 
        "attentive", "satisfied", "glowing", "vibrant", "fulfilled", "genuine", "appreciated", 
        "mindful", "contented", "happy-go-lucky", "approving", 
        # Added words
        "affable", "cheery", "friendly", "cozy", "gentle", "compassionate", "hospitable", "jovial",
        "mellow", "positive", "reliable", "warm-hearted", "approving", "tolerant", "graceful",
        "agreeable", "kind-hearted", "welcoming", "cordial", "sociable", "grateful", "cheerful",
        "receptive", "uplifted", "balanced", 'lovely', 'kind', 'beautiful', 'special', 'motivated'
    ]
    return tier_1_pos_word

def tier_2_pos():
    tier_2_pos_word = [
        "favorite", "adore", "cherish", "treasure", "delight in", "relish", "devoted", 
        "passionate", "fascinated", "captivated", "enchanted", "hooked", "addicted", "obsessed", 
        "obsessed with", "mesmerized", "allured", "infatuated", "in love", "beloved", "dear", 
        "revered", "enthusiastic", "ecstatic", "crazy about", "devotion", "intense", "indulge", 
        "zealous", "ardent", "fervent", "genuine", "fondly", "flattered", "adulation", "exhilarated", 
        "exalted", "grateful", "eager", "energized", "fulfilled", "overjoyed", "smitten", "enamored", 
        "serene", "ecstatic", "ecstasy", "captivated", "over the moon", "bliss", "glorious", 
        "admiration", "reverence", "rave", "appreciation", "relished", "delightful", "enraptured", 
        "adoration", "fanatic", "endearment", "serenity", "glow", "genuinely", "glamorous", 
        "savor", "rich", "optimistic", "energetic", "marvelous", "stellar", "brilliant", 
        "outstanding", "tremendous", "stoked", "proud", "worthy", "favored", "goodness", 
        "splendid", "out of this world", "awesome", "wonderful", "positive feeling", 
        # Added words
        "adoring", "zestful", "enthusiastic", "ebullient", "joyous", "captivating", "exhilarating",
        "buoyant", "vibrant", "elevated", "sublime", "passionate", "effervescent", "sparkling",
        "blessed", "thriving", "intoxicating", "euphoric", "elated", "heavenly", "glimmering",
        "beaming", "radiant", "zealous", "inspired", 'brightened','thrilled', 'incredible'
    ]
    return tier_2_pos_word

def tier_3_pos():
    tier_3_pos_word = [
        "love", "adore", "worship", "idolize", "cherish deeply", "treasure", "irreplaceable", 
        "unconditional", "devote", "passion", "intensely", "obsessed with", "crazy about", 
        "exhilarated", "delirious", "extremely", "intoxicating", "blissfully", "overwhelming", 
        "enchanted", "maddening", "exalted", "infatuated", "fascinated beyond measure", 
        "blissful", "out of this world", "astonishing", "unbeatable", "addictive", "unparalleled", 
        "unimaginable", "paradise", "ecstatic", "euphoric", "enthralled", "indescribable", 
        "heavenly", "heaven-sent", "divine", "goddess", "dreamlike", "utopia", "incomparable", 
        "divinely inspired", "extraordinary", "outstanding", "epic", "magnificent", "perfect", 
        "flawless", "surreal", "ultimate", "ideal", "unbelievable", "immaculate", "splendid", 
        "perfected", "mind-blowing", "mesmerizing", "sublime", "elevated", "majestic", 
        "life-changing", "limitless", "over the top", "unreachable", "top-tier", "phenomenal", 
        "incredible", "magnificent", "unmatched", "superb", "thrilling", "powerful", 
        "mind-bending", "glorious", "glow", "sublime", "rare", "elite", "undeniable", 
        "angelic", "blessed", "epic", "inspired", 
        # Added words
        "transcendent", "overwhelmingly positive", "divine", "extraordinary", "epic", "miraculous",
        "unparalleled", "superlative", "celestial", "majestic", "unimaginable", "sublime",
        "ethereal", "incomparable", "limitless", "paradisiacal", "enlightened", "untouchable",
        "flawless", "heavenly", "glorious"
    ]
    return tier_3_pos_word


def tier_1_neg():
    tier_1_neg_word = [
        "dislike", "not fond", "uninterested", "indifferent", "unconcerned", "avoid", "antagonistic", 
        "reject", "disapprove", "dismayed", "annoyed", "bored", "unpleasant", "irritated", "mildly upset", 
        "frustrated", "displeased", "unhappy", "unimpressed", "neglect", "indifferent", "resent", 
        "unmoved", "apathetic", "unwilling", "detest", "irksome", "unattractive", 
        "stale", "average", "mediocre", "unappealing", "discontented", "not thrilled", "apathetic", 
        "lackluster", "faintly", "underwhelmed", "uninspired", "unexcited", "cynical", "begrudge", 
        "distaste", "sour", "off-putting", "unpleasant", "nonchalant", "unsatisfied", "irksome", 
        "unpleased", "dissatisfied", "disengaged", "begrudging", "disheartened", "mild distaste", 
        "resigned", "grumble", "grumpy", "half-hearted", "disenchanted", "cool", "detachment", 
        "unimpressed", "apathetic"
        # Added words
        "aloof", "disinterested", "unbothered", "unexcited", "apathetic", "irritable", "disengaged", 
        "underwhelmed", "dissatisfied", "indifferent", "lackluster", "uninvolved", "unconcerned", 
        "dismissive", "apathetic", "bland", "unmoved", "not interested", "cold", "indifferent", 
        "uninspired", "unimpressed", "discontent", "sullen", "unfeeling", 'sad', 'uncomfortable', 'ugly'
    ]
    return tier_1_neg_word

def tier_2_neg():
    tier_2_neg_word = [
        "hate", "despise", "disgust", "detest", "revile", "resent", "intolerant", 
        "abhorrence", "repulsed", "offended", "offensive", "vile", "despised", "contempt", 
        "aversion", "disdain", "animosity", "disgusted", "unbearable", "sickened", "grossed out", 
        "intense dislike", "irritable", "loathing", "disdain", "grudge", "hostile", "antagonistic", 
        "intolerant", "discomfort", "seethe", "rage", "violent", "poisonous", "burning hatred", 
        "upset", "fury", "wrath", "inimical", "horrified", "disturbed", "incredible dislike", 
        "acrimony", "sharp distaste", "violent dislike", "unforgiving", "distressed", 
        "indignant", "unhappy", "grudge", "hatred", "harsh", "disgusting", "resentment", "revolt", 
        # Added words
        "fury", "revulsion", "scorn", "vengeful", "hostile", "bitter", "irate", "malice", "repulsion", 
        "abhorrent", "sickening", "fuming", "distasteful", "antagonistic", "repugnant", "displeasure", 
        "resentful", "venomous", "vindictive", "unforgiving", "infuriated", "bitterly angry", "scathing", 
        "despicable", "horrifying", "detestable", 'horrible', 'sickening', 'sick', 'grating', 'dilapidated'
    ]
    return tier_2_neg_word

def tier_3_neg():
    tier_3_neg_word = [
        "loathe", "abhor", "despise deeply", "disgust beyond measure", "repelled", "revulsion", 
        "uncontrollable hate", "viciously", "extreme hate", "horrify", "devastatingly", "furious", 
        "irate", "seething", "blinding rage", "venomous", "detested", "furiously angry", 
        "extremely repulsive", "intensely intolerant", "destruction", "devouring hatred", 
        "deplorable", "hate-filled", "out of control hate", "fiery", "scorn", "vengeful", 
        "disgusting beyond belief", "atrocious", "inexcusable", "shocking", "disastrous", 
        "horrifying", "reprehensible", "bitter", "condemning", "apocalyptic", "hostile beyond reason", 
        "spiteful", "diabolical", "abhorrent", "extreme", "fuming", "gruesome", "wrathful", "hateful", 
        "horrific", "unforgiving", "despicable", "repugnant", "irreconcilable", "revengeful", 
        "scathing", "horrendous", "poisonous", "relentless", "disastrous", "monstrous", "bloodthirsty", 
        "demonic", "devastating", "devouring", "blistering", "flame", "intense loathing", "malice", 
        # Added words
        "unbearable", "scalding", "toxic", "disastrous", "abominable", "savage", "incensed", "destructive",
        "overwhelming hate", "excruciating", "devastating", "infernal", "vile", "demonizing", "sinister",
        "unquenchable", "dark", "relentless", "obliterating", "immensely harmful", "uncontrollable rage", 
        "frenzied hatred", "blistering", "anguish", "devilish", "vengeful", "deadly"
    ]
    return tier_3_neg_word


t1p = tier_1_pos()
t2p = tier_2_pos()
t3p = tier_3_pos()

t1n = tier_1_neg()
t2n = tier_2_neg()
t3n = tier_3_neg()

all_pos = t1p + t2p + t3p
all_neg = t1n + t2n + t3n

all_words = all_pos + all_neg

intensfier = ['fucking', 'bloody', 'hella', 'insanely', 'really', 'exteremely', 'very', 'so']
article = ['a', 'an', 'the']
possesive = ['my', 'his', 'her', 'its', 'their', 'our', 'your']

def IsEmpty(L):
    return L == []

def divider():
    print('-'*50)

def tone(sentence,ignore_intensifier=bool):
    score = 0
    pos_arr = []
    neg_arr = []

    if isinstance(sentence, list):    
        low = sentence
    else:
        low = sentence.split(' ')

    print(low)

    def IsIntensified(n):
        k = (low.index(n) - 1)
        if k >= 0:
            return low[k] in intensfier

    def intensity(i,score):
        n = 0

        if IsIntensified(i) and not ignore_intensifier:
                print(f'{i} is intensified')
                n = score
        else:
            if ignore_intensifier:
                print('intensifier is ignored')
            else:
                print(f'{i} is not intensified')
                n = 0
        return n
    
    def a_noun(n):
        k = (low.index(n) - 1)
        if k >= 0:
            
            return low[k] in article or low[k] in possesive

    for i in low:
        if i in t1p:
            intense = intensity(i, 1)

            pos_arr.append(i)

            if not a_noun(i):
                score += 1 + intense 
            else:
                print(f'{i} is a noun. thus ignored')
                score += 0

        elif i in t2p:
            intense = intensity(i, 2)

            pos_arr.append(i)
            
            if not a_noun(i):
                score += 2 + intense 
            else:
                print(f'{i} is a noun. thus ignored')
                score += 0

        elif i in t3p:
            intense = intensity(i, 3)

            pos_arr.append(i)

            if not a_noun(i):
                score += 3 + intense 
            else:
                print(f'{i} is a noun. thus ignored')
                score += 0

        elif i in t1n:
            intense = intensity(i, 1)

            neg_arr.append(i)

            if not a_noun(i):
                score -= 1 + intense 
            else:
                print(f'{i} is a noun. thus ignored')
                score += 0

        elif i in t2n:
            intense = intensity(i, 2)

            neg_arr.append(i)
            
            if not a_noun(i):
                score -= 2 + intense 
            else:
                print(f'{i} is a noun. thus ignored')
                score += 0

        elif i in t3n:
            intense = intensity(i, 3)

            neg_arr.append(i)

            if not a_noun(i):
                score -= 3 + intense 
            else:
                print(f'{i} is a noun. thus ignored')
                score += 0
    
    if  IsEmpty(pos_arr):
        print('no positive word')
    else:
        print(pos_arr)
    
    if  IsEmpty(neg_arr):
        print('no negative word')
    else:
        print(neg_arr)

    return score

def indicate(sentence, ignore_intensifier=False):
    """
    
    :param sentence: the sentence that you want the determine its sentiment score
    :param ignore_intensifier: if true, intensifier wont be calculated. defaults at false
    :return: score which is an integer

    """
    score = tone(sentence, ignore_intensifier)

    if score > 0:
        return 'positive', score
    elif score < 0:
        return 'negative', score
    else:
        return 'neutral', 0

    
# print(indicate('fucking beautiful fucking horrendous fucking insane fucking ugly fucking love',False))
# divider()
# print(indicate('you look so beautiful in white', True))
# divider()
# print(indicate(['i', 'like', 'you']))



