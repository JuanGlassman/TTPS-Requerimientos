from estudios.models import Estudio
from datetime import date

estudio = ""

def crear():
    # Crear un nuevo estudio
    estudio = Estudio.objects.create(
        id_interno="1234_APE_NOM",
        paciente=14,
        fecha=date.today(),
        tipo_estudio="Ejemplo"
    )

def avanzar():
    # Avanzar al siguiente estado
    estudio.avanzar_estado()
    print(estudio)

def cancelar():
    # Cancelar el estudio
    estudio.cancelar()
    print(estudio)