def słownie(liczba: int, skala: str = 'długa', jeden: bool = True):
    '''
    Zamienia liczbę na zapis słowny w języku polskim.
    Obsługuje liczby w zakresie do 10^66-1 dla długiej skali oraz 10^36-1 dla krótkiej skali.
    Możliwe pominięcie słowa "jeden" przy potęgach tysiąca.
    '''


    if (skala == 'długa' and abs(liczba) >= 10 ** 66) or (skala == 'krótka' and abs(liczba) >= 10 ** 36):
        raise ValueError('Zbyt duża liczba.')

    jedności = ('', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć')
    naście = ('', 'jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście', 'osiemnaście','dziewiętnaście')
    dziesiątki = ('', 'dziesięć', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt','osiemdziesiąt', 'dziewięćdziesiąt')
    setki = ('', 'sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset')

    grupy = [  # kolejne potęgi tysiąca, z formami gramatycznymi
        ('', '', ''),
        ('tysiąc', 'tysiące', 'tysięcy'),
    ]

    przedrostki = ('mi', 'bi', 'try', 'kwadry', 'kwinty', 'seksty', 'septy', 'okty', 'nony', 'decy')
    for p in przedrostki:
        grupy.append((f'{p}lion', f'{p}liony', f'{p}lionów'))
        if skala == 'długa':
            grupy.append((f'{p}liard', f'{p}liardy', f'{p}liardów'))

    if liczba == 0:
        return 'zero'

    słowa = []
    znak = ''
    if liczba < 0:
        znak = 'minus'
        liczba = -liczba

    g = 0
    while liczba != 0:
        # Liczba jest dzielona na kolejne potęgi tysiąca, od największej.
        s = liczba % 1_000 // 100
        d = liczba % 100 // 10
        j = liczba % 10
        liczba //= 1_000

        if s == d == j == 0:  # brak elementów do nazwania
            g += 1
            continue

        if d == 1 and j > 0:  # łączymy dziesiątki i jedności w -naście
            n = j
            d = j = 0
        else:
            n = 0

        # wybór formy gramatycznej
        if j == 1 and s + d + n == 0:
            forma = 0
        elif 2 <= j <= 4:
            forma = 1
        else:
            forma = 2

        słowa = [setki[s], dziesiątki[d], naście[n], jedności[j] if jeden or g == 0 else '', grupy[g][forma]] + słowa
        g += 1

        słowa.insert(0, znak)
        return ' '.join(s for s in słowa if s)