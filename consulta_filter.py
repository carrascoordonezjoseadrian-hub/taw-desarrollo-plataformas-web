"""Ejemplos de filter() aplicados a las cuatro entidades."""
from configuracion import obtener_sesion
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

def consulta_filter():
    session = obtener_sesion()
    try:
        print("\nFILTER: clínicas de Quito")
        for x in session.query(Clinica).filter(Clinica.ciudad == "Quito").all():
            print(x.nombre, x.ciudad)

        print("\nFILTER: consultorios de Cirugía")
        for x in session.query(Consultorio).filter(Consultorio.especialidad == "Cirugía").all():
            print(x.nombre, x.especialidad)

        print("\nFILTER: veterinario con licencia VET-001")
        for x in session.query(Veterinario).filter(Veterinario.licencia == "VET-001").all():
            print(x.nombres, x.apellidos, x.licencia)

        print("\nFILTER: historias clínicas de Luna")
        for x in session.query(HistoriaClinica).filter(HistoriaClinica.mascota == "Luna").all():
            print(x.fecha_atencion, x.diagnostico)
    finally:
        session.close()

if __name__ == "__main__":
    consulta_filter()
