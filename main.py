from wordfreq import word_frequency

CONTROL_MULTIPLY = 10 # Adjust lower to include more common words like a and the
EXCLUDE = set('!"#$%&\()*+,-./:;<=>?@[]^_`{|}~')


def word_list(filename):
    num_words = 0
    word_occurrence_map = {}
    with open(filename) as file:
        for line in file.readlines():
            formatted = ''.join(char for char in line if char not in EXCLUDE).strip('\n').lower()
            words = formatted.split(' ')
            for word in words:
                if word == '' or word == "'":
                    continue
                num_words += 1
                if word in word_occurrence_map.keys():
                    word_occurrence_map[word] += 1
                else:
                    word_occurrence_map[word] = 1

    # for word_occurrence in sorted(word_occurrence_map.items(), key=lambda x: x[1], reverse=True):
    #     print(f'{word_occurrence[0]}: {word_occurrence[1]}')

    results = {}
    for key in word_occurrence_map.keys():
        word_freq = word_occurrence_map[key]/num_words * 100  # Percent in text
        word_freq_control = word_frequency(key, 'en', wordlist='small') * 100  # Percent in english
        # print(key, word_freq, word_freq_control)
        results[key] = float(word_freq - CONTROL_MULTIPLY*word_freq_control)

    results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    # print(results)

    return '\n\n' + filename + '\n' + ', '.join([item[0] for item in results][:30]) + '\n\n'
