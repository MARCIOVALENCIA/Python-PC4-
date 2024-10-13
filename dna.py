import csv
import sys

# Función para encontrar la mayor cantidad de repeticiones consecutivas de un STR en la secuencia de ADN
def longest_match(sequence, subsequence):
    longest_run = 0
    subseq_len = len(subsequence)
    seq_len = len(sequence)

    # Recorrer la secuencia para encontrar el STR más largo
    for i in range(seq_len):
        count = 0
        while sequence[i:i + subseq_len] == subsequence:
            count += 1
            i += subseq_len
        
        longest_run = max(longest_run, count)
    
    return longest_run

# Verifica si se proporcionaron los argumentos correctos
if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    sys.exit(1)

# Cargar la base de datos de ADN desde el archivo CSV
database = []
with open(sys.argv[1], 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convertir los valores STR de la persona de string a enteros
        for key in row:
            if key != 'name':
                row[key] = int(row[key])
        database.append(row)

# Leer la secuencia de ADN desde el archivo de texto
with open(sys.argv[2], 'r') as file:
    dna_sequence = file.read()

# Extraer los nombres de los STR (los encabezados del archivo CSV)
str_names = list(database[0].keys())[1:]

# Contar la cantidad de repeticiones consecutivas más largas de cada STR en la secuencia de ADN
str_counts = {}
for str_name in str_names:
    str_counts[str_name] = longest_match(dna_sequence, str_name)

# Comparar los STR contados con cada persona en la base de datos
for person in database:
    match = True
    for str_name in str_names:
        if person[str_name] != str_counts[str_name]:
            match = False
            break

    if match:
        print(person["name"])
        sys.exit(0)

# Si no se encontró una coincidencia
print("No match")
