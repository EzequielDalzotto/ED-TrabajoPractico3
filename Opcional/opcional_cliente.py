from registro_altura_rio import RegistroAlturaRio
from util import h2

registro = RegistroAlturaRio()

h2("Registro Completo")
print(registro)

h2("Puerto: Concordia")
for i in registro.filtar_por_puerto("CONCORDIA"):
    print(i)

h2("Rio: Uruguay")
for i in registro.filtar_por_rio("URUGUAY"):
    print(i)

h2("Estado: BAJA")
for i in registro.filtar_por_estado("BAJA"):
    print(i)