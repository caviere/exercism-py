
              

template = {1: ['house that Jack built.'], 2: ['malt ', 'lay in'], 3: ['rat ', 'ate'], 4: ['cat ', 'killed'], 5: ['dog ', 'worried'], 6: ['cow with the crumpled horn ', 'tossed'], 7: ['maiden all forlorn ', 'milked'], 8: ['man all tattered and torn ', 'kissed'], 9: ['priest all shaven and shorn ', 'married'], 10: ['rooster that crowed in the morn ', 'woke'],  11: ['farmer sowing his corn ', 'kept'], 12: ['horse and the hound and the horn ', 'belonged to'], 'this': 'This is the {}', 'that': 'that {} the {}'}

def recite(start_verse, end_verse, previous=None):
    index = start_verse
    verse = ''
    verse += template['this'].format(template[index][0])
    index -= 1
    while index > 0:
        verse += template['that'].format(template[index + 1][1], template[index][0])
        index -= 1
    if previous:
        previous.append(verse)
    else:
        previous = [verse]
    if start_verse == end_verse:
        return previous
    else:
        return recite(start_verse + 1, end_verse, previous)


        

          