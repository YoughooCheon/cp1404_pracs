"""
function main():
    create a band named "Extreme"
    create musician nuno with name "Nuno Bettencourt"
    add two guitars to nuno's instruments:
        - "Washburn N4", 1990, 2499.95
        - "Takamine acoustic", 1986, 1200.0
    add nuno to the band

    add musician "Gary Cherone" to the band without instruments

    create musician pat with name "Pat Badger"
    add guitar "Mouradian CS-74 Bass", 2009, 1500.0 to pat
    add pat to the band

    create musician kevin with name "Kevin Figueiredo"
    add kevin to the band without instruments

    print "band (str)"
    print string representation of band
    print "band.play()"
    print result of band.play() method

main()
"""
from band import Band
from musician import Musician
from guitar import Guitar

def main():
    band = Band("Extreme")
    nuno = Musician("Nuno Bettencourt")
    nuno.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add(Guitar("Takamine acoustic", 1986, 1200.0))
    band.add(nuno)
    band.add(Musician("Gary Cherone"))
    pat = Musician("Pat Badger")
    pat.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.0))
    band.add(pat)
    kevin = Musician("Kevin Figueiredo")
    band.add(kevin)

    print("band (str)")
    print(band)
    print("band.play()")
    print(band.play())

main()
