class Carta:
    PALOS = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    VALORES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self, valor, palo):
        if valor not in self.VALORES or palo not in self.PALOS:
            raise ValueError("Valor o palo de carta inválido")
        self.valor = valor
        self.palo = palo
    
    def __repr__(self):
        return f"{self.valor} de {self.palo}"
    
    def valor_numerico(self):
        return self.VALORES.index(self.valor)

class Mano:
    CLASIFICACIONES = [
        'Carta Alta', 'Par', 'Dos Pares', 'Trío', 'Escalera', 
        'Color', 'Full House', 'Póker', 'Escalera de Color', 'Escalera Real'
    ]
    
    def __init__(self, cartas):
        if len(cartas) != 5:
            raise ValueError("Una mano debe tener exactamente 5 cartas")
        self.cartas = sorted(cartas, key=lambda x: x.valor_numerico(), reverse=True)
    
    def _contar_valores(self):
        conteo = {}
        for carta in self.cartas:
            conteo[carta.valor] = conteo.get(carta.valor, 0) + 1
        return conteo
    
    def _es_color(self):
        return len(set(carta.palo for carta in self.cartas)) == 1
    
    def _es_escalera(self):
        valores = [carta.valor_numerico() for carta in self.cartas]
        valores.sort()
        return (valores[-1] - valores[0] == 4) and (len(set(valores)) == 5)
    
    def evaluar_mano(self):
        conteo_valores = self._contar_valores()
        es_color = self._es_color()
        es_escalera = self._es_escalera()
        
        # Determinar la clasificación de la mano
        if es_color and es_escalera:
            return 'Escalera de Color' if self.cartas[0].valor == 'A' else 'Escalera de Color'
        
        if 4 in conteo_valores.values():
            return 'Póker'
        
        if sorted(conteo_valores.values()) == [2, 3]:
            return 'Full House'
        
        if es_color:
            return 'Color'
        
        if es_escalera:
            return 'Escalera'
        
        if 3 in conteo_valores.values():
            return 'Trío'
        
        if list(conteo_valores.values()).count(2) == 2:
            return 'Dos Pares'
        
        if 2 in conteo_valores.values():
            return 'Par'
        
        return 'Carta Alta'

def obtener_carta():
    while True:
        print("\nValores disponibles:", ', '.join(Carta.VALORES))
        print("Palos disponibles:", ', '.join(Carta.PALOS))
        
        valor = input("Ingrese el valor de la carta (2-10, J, Q, K, A): ").strip().upper()
        if valor == '10':
            valor = '10'
        
        palo = input("Ingrese el palo de la carta: ").strip().capitalize()
        
        try:
            return Carta(valor, palo)
        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo.")

def main():
    while True:
        print("\n--- Evaluador de Manos de Póker ---")
        print("1. Crear una mano")
        print("2. Salir")
        
        opcion = input("Elija una opción (1/2): ").strip()
        
        if opcion == '2':
            print("¡Gracias por usar el evaluador de manos de Póker!")
            break
        
        if opcion != '1':
            print("Opción inválida. Por favor, elija 1 o 2.")
            continue
        
        print("\nVamos a crear su mano. Recuerde, necesita 5 cartas.")
        cartas = []
        
        for i in range(5):
            print(f"\nCarta {i+1}:")
            carta = obtener_carta()
            cartas.append(carta)
        
        try:
            mano = Mano(cartas)
            print("\nSu mano:")
            for carta in mano.cartas:
                print(carta)
            
            clasificacion = mano.evaluar_mano()
            print(f"\n¡Tiene un {clasificacion}!")
        
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()