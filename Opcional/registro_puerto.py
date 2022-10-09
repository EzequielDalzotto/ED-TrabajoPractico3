class RegistroPuerto:
    def __init__(self, puerto : str, rio : str, ult_reg : str, fecha_hora : str, estado : str) -> None:
        self._puerto = puerto
        self._rio = rio
        self._ult_reg = ult_reg
        self._fecha_hora = fecha_hora
        self._estado = estado

    def __str__(self) -> str:
        return f"Puerto: {self._puerto} Rio: {self._rio} Ultimo Registro: {self._ult_reg} Fecha Hora: {self._fecha_hora} Estado: {self._estado}"