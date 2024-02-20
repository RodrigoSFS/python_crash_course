class NumeroRomano:
    def __init__(self, valor):
        self.valor = valor

    def para_romano(self):

        decimais_romanos = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        for k, v in decimais_romanos.items():
            print(v, end=" ")

        print()

        mil = 0
        novecentos = 0
        quinhentos = 0
        quatrocentos = 0
        cem = 0
        noventa = 0
        cinquenta = 0
        quarenta = 0
        dez = 0
        nove = 0
        cinco = 0
        quatro = 0
        um = 0

        while self.valor > 0:
            if self.valor >= 1000:
                mil = self.valor // 1000
                self.valor = self.valor % 1000
            if self.valor >= 900:
                novecentos = self.valor // 900
                self.valor = self.valor % 900
            if self.valor >= 500:
                quinhentos = self.valor // 500
                self.valor = self.valor % 500
            if self.valor >= 400:
                quatrocentos = self.valor // 400
                self.valor = self.valor % 400
            if self.valor >= 100:
                cem = self.valor // 100
                self.valor = self.valor % 100
            if self.valor >= 90:
                noventa = self.valor // 90
                self.valor = self.valor % 90
            if self.valor >= 50:
                cinquenta = self.valor // 50
                self.valor = self.valor % 50
            if self.valor >= 40:
                quarenta = self.valor // 40
                self.valor = self.valor % 40
            if self.valor >= 10:
                dez = self.valor // 10
                self.valor = self.valor % 10
            if self.valor >= 9:
                nove = self.valor // 9
                self.valor = self.valor % 9
            if self.valor >= 5:
                cinco = self.valor // 5
                self.valor = self.valor % 5
            if self.valor >= 4:
                quatro = self.valor // 4
                self.valor = self.valor % 4
            if self.valor >= 1:
                um = self.valor // 1
                self.valor = self.valor % 1

        resultado = (
            um,
            quatro,
            cinco,
            nove,
            dez,
            quarenta,
            cinquenta,
            noventa,
            cem,
            quatrocentos,
            quinhentos,
            novecentos,
            mil,
        )

        numero_em_romano = (
            decimais_romanos[1000] * mil
            + decimais_romanos[900] * novecentos
            + decimais_romanos[500] * quinhentos
            + decimais_romanos[400] * quatrocentos
            + decimais_romanos[100] * cem
            + decimais_romanos[90] * noventa
            + decimais_romanos[50] * cinquenta
            + decimais_romanos[40] * quarenta
            + decimais_romanos[10] * dez
            + decimais_romanos[9] * nove
            + decimais_romanos[5] * cinco
            + decimais_romanos[4] * quatro
            + decimais_romanos[1] * um
        )

        print(resultado)

        return numero_em_romano

    def para_decimal(self):
        romanos_decimais = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        valor = self.valor.upper()

        soma = 0
        i = 0

        while i < len(valor):
            if i < len(valor) - 1:
                if valor[i] == "C" and valor[i + 1] == "M":
                    soma += 900
                    i += 2 
                elif valor[i] == "C" and valor[i + 1] == "D":
                    soma += 400
                    i += 2
                elif valor[i] == "X" and valor[i + 1] == "C":
                    soma += 90
                    i += 2
                elif valor[i] == "X" and valor[i + 1] == "L":
                    soma += 40
                    i += 2
                elif valor[i] == "I" and valor[i + 1] == "X":
                    soma += 9
                    i += 2
                elif valor[i] == "I" and valor[i + 1] == "V":
                    soma += 4
                    i += 2
                else:
                    soma += romanos_decimais[valor[i]]
                    i += 1
            else:
                soma += romanos_decimais[valor[i]]
                i += 1
            
        return soma

    @classmethod
    def de_romano(cls, romano):
        novo_objeto = cls(romano)
        return novo_objeto
