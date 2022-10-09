from typing import List
import requests
import re
from registro_puerto import RegistroPuerto

class RegistroAlturaRio:
    url="https://contenidosweb.prefecturanaval.gob.ar/alturas/index.php"
    r = requests.get(url)

    codigo_html= r.text

    puertos_pattern= 'data-label=\\"Puerto:\\".*</th'
    rios_pattern= 'data-label=\\"Río:\\".*</td'
    ult_reg_pattern= 'data-label=\\"Ultimo\sRegistro:\\".*</td'
    fecha_hora_pattern= 'data-label=\\"Fecha\sHora:\\".*</td'
    estado_pattern= 'data-label=\\"Estado:\\".*</td'


    puertos = re.findall(puertos_pattern, codigo_html)
    rios = re.findall(rios_pattern,codigo_html)
    ult_regs = re.findall(ult_reg_pattern,codigo_html)
    fechas_horas = re.findall(fecha_hora_pattern,codigo_html)
    estados = re.findall(estado_pattern,codigo_html)

    def __init__(self) -> None:
        self._registro = []
        for i in range(0,RegistroAlturaRio.puertos.__len__()):
            self._registro.append(RegistroPuerto(
                RegistroAlturaRio.puertos[i][21:-4],
                RegistroAlturaRio.rios[i][18:-4],
                RegistroAlturaRio.ult_regs[i][46:-4],
                RegistroAlturaRio.fechas_horas[i][28:-8],
                RegistroAlturaRio.estados[i][21:-4]))

    def __str__(self) -> str:
        res = ""
        for elem in self._registro:
            res += "{elem}\n".format(elem=str(elem))
        return res

    def filtar_por_puerto(self, nombrePuerto : str) -> List:
        res = []
        for i in self._registro:
            if i._puerto == nombrePuerto:
                res.append(i)
        return res
    

    def filtar_por_rio(self, rio : str) -> List:
        res = []
        for i in self._registro:
            if i._rio == rio:
                res.append(i)
        return res
    

    def filtar_por_estado(self, estado : str) -> List:
        res = []
        for i in self._registro:
            if i._estado == estado:
                res.append(i)
        return res

    
    