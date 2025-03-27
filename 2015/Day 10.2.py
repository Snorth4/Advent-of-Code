class ElementInfo:
    def __init__(self, atomic_number, decays_into: list[str], sequence: str):
        self.atomic_number = atomic_number
        self.decays_into = decays_into
        self.sequence = sequence
        self.n = len(sequence)

PeriodicTable = {"H"  : ElementInfo( 1, ["H"],                          "22"),
                 "He" : ElementInfo( 2, ["Hf", "Pa", "H", "Ca", "Li"], "13112221133211322112211213322112"),
                 "Li" : ElementInfo( 3, ["He"],                       "312211322212221121123222112"),
                 "Be" : ElementInfo( 4, ["Ge", "Ca", "Li"],          "111312211312113221133211322112211213322112"),
                 "B"  : ElementInfo( 5, ["Be"],                     "1321132122211322212221121123222112"),
                 "C"  : ElementInfo( 6, ["B"],                     "3113112211322112211213322112"),
                 "N"  : ElementInfo( 7, ["C"],                    "111312212221121123222112"),
                 "O"  : ElementInfo( 8, ["N"],                   "132112211213322112"),
                 "F"  : ElementInfo( 9, ["O"],                  "31121123222112"),
                 "Ne" : ElementInfo(10, ["F"],                 "111213322112"),
                 "Na" : ElementInfo(11, ["Ne"],               "123222112"),
                 "Mg" : ElementInfo(12, ["Pm", "Na"],         "3113322112"),
                 "Al" : ElementInfo(13, ["Mg"],                "1113222112"),
                 "Si" : ElementInfo(14, ["Al"],                 "1322112"),
                 "P"  : ElementInfo(15, ["Ho", "Si"],            "311311222112"),
                 "S"  : ElementInfo(16, ["P"],                    "1113122112"),
                 "Cl" : ElementInfo(17, ["S"],                     "132112"),
                 "Ar" : ElementInfo(18, ["Cl"],                     "3112"),
                 "K"  : ElementInfo(19, ["Ar"],                      "1112"),
                 "Ca" : ElementInfo(20, ["K"],                        "12"),
                 "Sc" : ElementInfo(21, ["Ho", "Pa", "H", "Ca", "Co"], "3113112221133112"),
                 "Ti" : ElementInfo(22, ["Sc"],                         "11131221131112"),
                 "V"  : ElementInfo(23, ["Ti"],                          "13211312"),
                 "Cr" : ElementInfo(24, ["V"],                            "31132"),
                 "Mn" : ElementInfo(25, ["Cr", "Si"],                      "111311222112"),
                 "Fe" : ElementInfo(26, ["Mn"],                             "13122112"),
                 "Co" : ElementInfo(27, ["Fe"],                              "32112"),
                 "Ni" : ElementInfo(28, ["Zn", "Co"],                         "11133112"),
                 "Cu" : ElementInfo(29, ["Ni"],                                "131112"),
                 "Zn" : ElementInfo(30, ["Cu"],                                "312"),
                 "Ga" : ElementInfo(31, ["Eu", "Ca", "Ac", "H", "Ca", "Zn"],  "13221133122211332"),
                 "Ge" : ElementInfo(32, ["Ho", "Ga"],                        "31131122211311122113222"),
                 "As" : ElementInfo(33, ["Ge", "Na"],                       "11131221131211322113322112"),
                 "Se" : ElementInfo(34, ["As"],                            "13211321222113222112"),
                 "Br" : ElementInfo(35, ["Se"],                           "3113112211322112"),
                 "Kr" : ElementInfo(36, ["Br"],                          "11131221222112"),
                 "Rb" : ElementInfo(37, ["Kr"],                         "1321122112"),
                 "Sr" : ElementInfo(38, ["Rb"],                        "3112112"),
                 "Y"  : ElementInfo(39, ["Sr", "U"],                  "1112133"),
                 "Zr" : ElementInfo(40, ["Y", "H", "Ca", "Tc"],      "12322211331222113112211"),
                 "Nb" : ElementInfo(41, ["Er", "Zr"],               "1113122113322113111221131221"),
                 "Mo" : ElementInfo(42, ["Nb"],                    "13211322211312113211"),
                 "Tc" : ElementInfo(43, ["Mo"],                   "311322113212221"),
                 "Ru" : ElementInfo(44, ["Eu", "Ca", "Tc"],      "132211331222113112211"),
                 "Rh" : ElementInfo(45, ["Ho", "Ru"],           "311311222113111221131221"),
                 "Pd" : ElementInfo(46, ["Rh"],                "111312211312113211"),
                 "Ag" : ElementInfo(47, ["Pd"],               "132113212221"),
                 "Cd" : ElementInfo(48, ["Ag"],              "3113112211"),
                 "In" : ElementInfo(49, ["Cd"],             "11131221"),
                 "Sn" : ElementInfo(50, ["In"],            "13211"),
                 "Sb" : ElementInfo(51, ["Pm", "Sn"],      "3112221"),
                 "Te" : ElementInfo(52, ["Eu", "Ca", "Sb"], "1322113312211"),
                 "I"  : ElementInfo(53, ["Ho", "Te"],        "311311222113111221"),
                 "Xe" : ElementInfo(54, ["I"],                "11131221131211"),
                 "Cs" : ElementInfo(55, ["Xe"],                "13211321"),
                 "Ba" : ElementInfo(56, ["Cs"],                 "311311"),
                 "La" : ElementInfo(57, ["Ba"],                  "11131"),
                 "Ce" : ElementInfo(58, ["La", "H", "Ca", "Co"], "1321133112"),
                 "Pr" : ElementInfo(59, ["Ce"],                  "31131112"),
                 "Nd" : ElementInfo(60, ["Pr"],                 "111312"),
                 "Pm" : ElementInfo(61, ["Nd"],                "132"),
                 "Sm" : ElementInfo(62, ["Pm", "Ca", "Zn"],   "311332"),
                 "Eu" : ElementInfo(63, ["Sm"],              "1113222"),
                 "Gd" : ElementInfo(64, ["Eu", "Ca", "Co"],  "13221133112"),
                 "Tb" : ElementInfo(65, ["Ho", "Gd"],         "3113112221131112"),
                 "Dy" : ElementInfo(66, ["Tb"],                "111312211312"),
                 "Ho" : ElementInfo(67, ["Dy"],                 "1321132"),
                 "Er" : ElementInfo(68, ["Ho", "Pm"],            "311311222"),
                 "Tm" : ElementInfo(69, ["Er", "Ca", "Co"],       "11131221133112"),
                 "Yb" : ElementInfo(70, ["Tm"],                    "1321131112"),
                 "Lu" : ElementInfo(71, ["Yb"],                     "311312"),
                 "Hf" : ElementInfo(72, ["Lu"],                      "11132"),
                 "Ta" : ElementInfo(73, ["Hf", "Pa", "H", "Ca", "W"], "13112221133211322112211213322113"),
                 "W"  : ElementInfo(74, ["Ta"],                       "312211322212221121123222113"),
                 "Re" : ElementInfo(75, ["Ge", "Ca", "W"],           "111312211312113221133211322112211213322113"),
                 "Os" : ElementInfo(76, ["Re"],                     "1321132122211322212221121123222113"),
                 "Ir" : ElementInfo(77, ["Os"],                    "3113112211322112211213322113"),
                 "Pt" : ElementInfo(78, ["Ir"],                   "111312212221121123222113"),
                 "Au" : ElementInfo(79, ["Pt"],                  "132112211213322113"),
                 "Hg" : ElementInfo(80, ["Au"],                 "31121123222113"),
                 "Tl" : ElementInfo(81, ["Hg"],                "111213322113"),
                 "Pb" : ElementInfo(82, ["Tl"],               "123222113"),
                 "Bi" : ElementInfo(83, ["Pm", "Pb"],         "3113322113"),
                 "Po" : ElementInfo(84, ["Bi"],                "1113222113"),
                 "At" : ElementInfo(85, ["Po"],                 "1322113"),
                 "Rn" : ElementInfo(86, ["Ho", "At"],            "311311222113"),
                 "Fr" : ElementInfo(87, ["Rn"],                   "1113122113"),
                 "Ra" : ElementInfo(88, ["Fr"],                    "132113"),
                 "Ac" : ElementInfo(89, ["Ra"],                     "3113"),
                 "Th" : ElementInfo(90, ["Ac"],                      "1113"),
                 "Pa" : ElementInfo(91, ["Th"],                       "13"),
                 "U"  : ElementInfo(92, ["Pa"],                        "3"),
                 "Np" : ElementInfo(93, ["Hf", "Pa", "H", "Ca", "Pu"],  "1311222113321132211221121332211n"),
                 "Pu" : ElementInfo(94, ["Np"],                          "31221132221222112112322211n")}

def look_and_say_sequence(string: str) -> str:

    prev, curr, next = "", "", ""
    symbol_counter: int = 0
    sequence: str = ""
    n = len(string)

    for i in range(n):
        prev = string[i-1:i]
        curr = string[i:i+1]
        next = string[i+1:i+2]

        if i == 0:
            prev == ""
        if i == n - 1:
            next == ""
        
        if   prev == curr == next:
            symbol_counter += 1

        elif prev == curr != next:
            symbol_counter += 1
            sequence = f"{sequence}{symbol_counter}{curr}"
            
        elif prev != curr == next:
            symbol_counter = 1

        elif prev != curr != next:
            symbol_counter = 1
            sequence = f"{sequence}{symbol_counter}{curr}"

    return sequence
        
def look_and_say_length(string: str, num_iterations: int) -> int:

    output = 0
    curr_list = []
    next_list = []

    if num_iterations > 0:
        valid = False
    else:
        valid = True
        output = len(string)

    while not valid:

        for element in PeriodicTable:

            if string == PeriodicTable[element].sequence: # Could use some work...

                curr_list = [element]
                valid = True
                break
        
        if not valid:
            string = look_and_say_sequence(string)

    for _ in range(num_iterations):
        next_list = []
        for curr_element in curr_list:
            for next_element in PeriodicTable[curr_element].decays_into:
                next_list.append(next_element)
        
        curr_list = next_list
    
    for element in curr_list:
        output += PeriodicTable[element].n
    
    return output

def main():
    print("Input:")

    number = str(input())
    num_iterations = 50

    print(f"Length of {num_iterations} iterations: {look_and_say_length(number, num_iterations)}")

if __name__ == "__main__":
    main()
