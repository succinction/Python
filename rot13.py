# from string import maketrans   # Required to call maketrans function.

# intab = "aeiou"
# outtab = "12345"
#
# str = "this is string example....wow!!!";
# print str.translate(trantab)

from string import ascii_letters


def cypher(word, rotate):
    # single =   "abcdefghijklmnopqrstuvwxyz"
    single = ascii_letters
    double = single + single
    rot = int(rotate) % 52
    rotated = double[rot:rot+52]
    intab = single
    outtab = rotated
    trantab = str.maketrans(intab, outtab)
    new_phrase = word.translate(trantab)
    print(new_phrase)
    return new_phrase

def decypher(word, rotate):
    # single =   "abcdefghijklmnopqrstuvwxyz"
    single = ascii_letters
    double = single + single
    rot = int(rotate) % 52
    rotated = double[rot:rot+52]
    intab = rotated
    outtab = single
    trantab = str.maketrans(intab, outtab)
    new_phrase = word.translate(trantab)
    print(new_phrase)

while True:
    rotation = input("Enter Cypher Rotation: ")
    cphr = input("Enter phrase for encryption: ")
    zfr = cypher(cphr, rotation)
    decypher(zfr, rotation)






# This is a puzzle! Here is a chart to help with your translation:
# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m