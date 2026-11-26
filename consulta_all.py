"""Consulta todas las clínicas y cuenta sus historias clínicas asociadas."""
from sqlalchemy import func
from configuracion import obtener_sesion
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

def consulta_all():
    session = obtener_sesion()
    try:
        print("\nCLÍNICAS Y NÚMERO DE HISTORIAS CLÍNICAS")
        clinicas = session.query(Clinica).order_by(Clinica.id).all()
        for clinica in clinicas:
            cantidad = (
                session.query(func.count(HistoriaClinica.id))
                .join(Veterinario, HistoriaClinica.veterinario_id == Veterinario.id)
                .join(Consultorio, Veterinario.consultorio_id == Consultorio.id)
                .filter(Consultorio.clinica_id == clinica.id)
                .scalar()
            )
            print(f"{clinica.nombre} ({clinica.ciudad}): {cantidad} historia(s) clínica(s)")
    finally:
        session.close()

if __name__ == "__main__":
    consulta_all()
