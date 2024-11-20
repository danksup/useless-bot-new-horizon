def simple_word_match_algorithm(word, target):
    score = 0

    for i in word:
        if i in target:
            score += 0.1
        else:
            score -= 0.08
    
    delta_len = abs(len(word) - len(target))

    if word == target:
        score += 100
    elif len(word) != len(target):
        score -= delta_len * 0.05
    else:
        score += 0.1
    return score

def suggest_word(word, word_dict):
    best_score = 0
    best_match = None

    for i in word_dict:
        score = simple_word_match_algorithm(word, i)
        # print(f'{score} for {word} to {i}')
        if score > best_score:
            best_score = score
            best_match = i

    if best_score >= 0.2:
        return f'invalid command. did you mean `{best_match}`?'
    else:
        return 'invalid command'

