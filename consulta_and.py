"""Ejemplos de consultas con AND lógico usando and_()."""
from sqlalchemy import and_
from configuracion import obtener_sesion
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

def consulta_and():
    session = obtener_sesion()
    try:
        print("\nCLÍNICA DE CUENCA CON NOMBRE HUELLITAS DEL SUR")
        for x in session.query(Clinica).filter(and_(Clinica.ciudad == "Cuenca", Clinica.nombre == "Huellitas del Sur")).all():
            print(x.nombre, x.ciudad)

        print("\nCONSULTORIOS DE CIRUGÍA EN LA CLÍNICA 1")
        for x in session.query(Consultorio).filter(and_(Consultorio.especialidad == "Cirugía", Consultorio.clinica_id == 1)).all():
            print(x.nombre, x.especialidad, "Clínica:", x.clinica_id)

        print("\nVETERINARIA DANIELA PAREDES RUIZ")
        for x in session.query(Veterinario).filter(and_(Veterinario.nombres == "Daniela", Veterinario.apellidos == "Paredes Ruiz")).all():
            print(x.nombres, x.apellidos, x.correo)

        print("\nHISTORIA DE LUNA CON DIAGNÓSTICO DE OTITIS EXTERNA")
        for x in session.query(HistoriaClinica).filter(and_(HistoriaClinica.mascota == "Luna", HistoriaClinica.diagnostico == "Otitis externa")).all():
            print(x.mascota, x.diagnostico, x.tratamiento)
    finally:
        session.close()

if __name__ == "__main__":
    consulta_and()
