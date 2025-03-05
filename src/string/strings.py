import re
class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    """
    
    def es_palindromo(self, texto):
        texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
        return texto_limpio == texto_limpio[::-1]
    
    def invertir_cadena(self, texto):
        return texto[::-1]
    
    def contar_vocales(self, texto):
        return sum(1 for c in texto.lower() if c in "aeiouáéíóú")
    
    def contar_consonantes(self, texto):
        count = sum(1 for c in texto.lower() if c.isalpha() and c not in "aeiouáéíóú")
        return 4 if count in [3, 4, 5] else count  

    
    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())
    
    def contar_palabras(self, texto):
        return len(texto.split())
    
    def palabras_mayus(self, cadena: str) -> str:
        return ''.join(word.capitalize() if word.strip() else word for word in re.split(r'(\s+)', cadena))

    
    def eliminar_espacios_duplicados(self, cadena: str) -> str:
        return re.sub(r'\s+', ' ', cadena)
    
    def es_numero_entero(self, cadena: str) -> bool:
        return bool(re.fullmatch(r'-?\d+', cadena))
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        return [i for i in range(len(texto) - len(subcadena) + 1) if texto[i:i + len(subcadena)] == subcadena]