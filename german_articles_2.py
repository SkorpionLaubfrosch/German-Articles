import re

def german():
    word = input('Enter your word: ')
    if word.isalpha():
        word = word.lower()
        matched_vowels = re.search(r'\b[bcdfghjklmnpqrstvwxz]*[aeiouy]{6,}', word)
        if not matched_vowels:
            matched_consonants = re.search(r'\b[aeiouybcdfghjklmnpqrstvwxz]*[bcdfghjklmnpqrstvwxz]{6,}', word)
            if not matched_consonants:
                #print('запускаем функцию')
                word = word.title()
                lentgh = len(word)

                one_letter = word[lentgh-1:lentgh]
                two_letters = word[lentgh-2:lentgh]
                three_letters = word[lentgh-3:lentgh]
                four_letters = word[lentgh-4:lentgh]
                five_letters = word[lentgh-5:lentgh]
                six_letters = word[lentgh-6:lentgh]
            
                masculine_two = {'er', 'or', 'är', 'ar'}
                masculine_three = {'ler', 'ner', 'ent', 'ant', 'ist', 'eur', 'iur'}
                masculine_four = {'ling'}
                masculine_five = {'ismus'}
            
                feminine_one = {'t'}
                feminine_two = {'in', 'ei', 'ur', 'ät'}
                feminine_three = {'ung', 'tät', 'tur', 'ion', 'anz', 'enz'}
                feminine_four = {'heit', 'keit', 'tion'} 
                feminine_six = {'schaft'}

                neutral_two = {'um'}
                neutral_tree = {'nis', 'sal', 'sel', 'tum', 'ium', 'iat'}
                neutral_four = {'chen', 'lein', 'ment'}

                if three_letters in neutral_tree or four_letters in neutral_four:
                    print('Das {}'.format(word))
                elif two_letters in masculine_two or three_letters in masculine_three or four_letters in masculine_four or five_letters in masculine_five:
                    print('Der {}'.format(word))
                elif two_letters in {'el', 'al', 'en', 'at'}:
                    print('Der {} или Das {}'.format(word, word))
                elif one_letter in feminine_one or two_letters in feminine_two or three_letters in feminine_three or four_letters in feminine_four or six_letters in feminine_six:
                    print('Die {}'.format(word))
                elif one_letter in {'e'}:
                    print('Der {} или Die {}'.format(word, word))
                else:
                    print('ошибка. это слово нельзя определить по суффиксу, нужно решение для этого')
            else:
                print('много согласных подряд, нет')
        else:
            print('много гласных подряд, нет')
    else:
        print('its not a word')
       
german()
