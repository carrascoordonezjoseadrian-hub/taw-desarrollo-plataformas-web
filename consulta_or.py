"""Ejemplos de consultas con OR lógico usando or_()."""
from sqlalchemy import or_
from configuracion import obtener_sesion
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

def consulta_or():
    session = obtener_sesion()
    try:
        print("\nCLÍNICAS DE QUITO O GUAYAQUIL")
        for x in session.query(Clinica).filter(or_(Clinica.ciudad == "Quito", Clinica.ciudad == "Guayaquil")).all():
            print(x.nombre, x.ciudad)

        print("\nCONSULTORIOS DE CIRUGÍA U ODONTOLOGÍA")
        for x in session.query(Consultorio).filter(or_(Consultorio.especialidad == "Cirugía", Consultorio.especialidad == "Odontología veterinaria")).all():
            print(x.nombre, x.especialidad)

        print("\nVETERINARIOS CON LICENCIA VET-001 O VET-003")
        for x in session.query(Veterinario).filter(or_(Veterinario.licencia == "VET-001", Veterinario.licencia == "VET-003")).all():
            print(x.nombres, x.apellidos, x.licencia)

        print("\nHISTORIAS DE LAS MASCOTAS MAX O LUNA")
        for x in session.query(HistoriaClinica).filter(or_(HistoriaClinica.mascota == "Max", HistoriaClinica.mascota == "Luna")).all():
            print(x.mascota, x.diagnostico)
    finally:
        session.close()

if __name__ == "__main__":
    consulta_or()
