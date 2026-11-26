"""Ejemplos de ordenamiento ascendente y descendente con order_by()."""
from configuracion import obtener_sesion
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

def consulta_order_by():
    session = obtener_sesion()
    try:
        print("\nCLÍNICAS ORDENADAS POR NOMBRE")
        for x in session.query(Clinica).order_by(Clinica.nombre.asc()).all():
            print(x.nombre)

        print("\nCONSULTORIOS ORDENADOS POR ESPECIALIDAD")
        for x in session.query(Consultorio).order_by(Consultorio.especialidad.asc()).all():
            print(x.especialidad, "-", x.nombre)

        print("\nVETERINARIOS ORDENADOS POR APELLIDO")
        for x in session.query(Veterinario).order_by(Veterinario.apellidos.asc()).all():
            print(x.apellidos, x.nombres)

        print("\nHISTORIAS CLÍNICAS: MÁS RECIENTES PRIMERO")
        for x in session.query(HistoriaClinica).order_by(HistoriaClinica.fecha_atencion.desc()).all():
            print(x.fecha_atencion, x.mascota, x.diagnostico)
    finally:
        session.close()

if __name__ == "__main__":
    consulta_order_by()
