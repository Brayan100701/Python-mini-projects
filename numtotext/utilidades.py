class Translator:
    basics = {
        '0':['', '', ''],
        '1':['uno', 'diez', 'cien'],
        '2':['dos', 'veinte', 'doscientos'],
        '3':['tres', 'treinta', 'trescientos'],
        '4':['cuatro', 'cuarenta', 'cuatrocientos'],
        '5':['cinco', 'cincuenta', 'quinientos'],
        '6':['seis', 'sesenta', 'seiscientos'],
        '7':['siete', 'setenta', 'setecientos'],
        '8':['ocho', 'ochenta', 'ochocientos'],
        '9':['nueve', 'noventa', 'novecientos']
        }
    
    specials = {
        '10':'diez',
        '11':'once',
        '12':'doce',
        '13':'trece',
        '14':'catorce',
        '15':'quince'
    }
    
    def translate(self,num):
        if num != '0':
            num = '0'*(6-len(num)) + num
            translation = self.toWord(num[:3],'mil')
            translation += self.toWord(num[3:])
            return translation
        return 'cero'
    
    def toTens(self,n):
        if n not in Translator.specials:
            if n[1] != '0':
                match n[0]:
                    case '1':
                        temp = 'dieci'
                    case '2':
                        temp = 'veinti'
                    case _:
                        temp = Translator.basics[n[0]][1] + ' y ' if n[0]!='0' else ''
                return temp + Translator.basics[n[1]][0]    
            return Translator.basics[n[0]][1]
        return Translator.specials[n]
    
    def toHundreds(self,n):
        temp = Translator.basics[n][2]
        return temp+'to ' if n[0] == '1' else temp+' '
    
    def toWord(self, n, ad=''):
        temp = self.toHundreds(n[0]) + self.toTens(n[1:])
        return temp + f' {ad} ' if n != '000' else ''


def validate(text):
    try:
        return True if 0 <= int(text) <= 999999 else False
    except:
        return False