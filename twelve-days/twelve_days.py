PRESENTS = { 1: 'and a Partridge in a Pear Tree', 2: 'two Turtle Doves', 3: 'three French Hens', 4: 'four Calling Birds', 5: 'five Gold Rings', 6: 'six Geese-a-Laying', 7: 'seven Swans-a-Swimming', 8: 'eight Maids-a-Milking', 9: 'nine Ladies Dancing', 10: 'ten Lords-a-Leaping', 11: 'eleven Pipers Piping', 12: 'twelve Drummers Drumming'}

DAYS = { 1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth'}

        

          

def verse(day_number):
    day = DAYS[day_number]

    if day_number == 1:
        presents = 'a Partridge in a Pear Tree'
    else:
        presents = ', '.join([PRESENTS[x] for x in range(day_number, 0, -1)])

    return f"On the {day} day of Christmas my true love gave to me: {presents}."

def recite(start, end):
    return [verse(x) for x in range(start, end+1)]