"""Carga registros de demostración en las cuatro entidades."""
from datetime import date
from configuracion import obtener_sesion
from crear_base_entidades import (
    crear_tablas, Clinica, Consultorio, Veterinario, HistoriaClinica
)

def poblar_base():
    crear_tablas()
    session = obtener_sesion()
    try:
        # La carga es idempotente: no duplica los datos si se ejecuta otra vez.
        if session.query(Clinica).first():
            print("La base de datos ya contiene información; no se duplicaron registros.")
            return

        c1 = Clinica(nombre="VetSalud Central", direccion="Av. Amazonas y Naciones Unidas", ciudad="Quito", veterinario_responsable="Dra. Laura Mendoza")
        c2 = Clinica(nombre="Huellitas del Sur", direccion="Av. Loja y Remigio Crespo", ciudad="Cuenca", veterinario_responsable="Dr. Andrés Molina")
        c3 = Clinica(nombre="AnimalCare", direccion="Av. Francisco de Orellana", ciudad="Guayaquil", veterinario_responsable="Dra. Camila Torres")
        session.add_all([c1, c2, c3])
        session.flush()

        consultorios = [
            Consultorio(nombre="Consultorio 101", especialidad="Medicina general", clinica=c1),
            Consultorio(nombre="Consultorio 102", especialidad="Cirugía", clinica=c1),
            Consultorio(nombre="Consultorio 201", especialidad="Dermatología", clinica=c2),
            Consultorio(nombre="Consultorio 202", especialidad="Medicina general", clinica=c2),
            Consultorio(nombre="Consultorio 301", especialidad="Cirugía", clinica=c3),
            Consultorio(nombre="Consultorio 302", especialidad="Odontología veterinaria", clinica=c3),
        ]
        session.add_all(consultorios)
        session.flush()

        vets = [
            Veterinario(nombres="Daniela", apellidos="Paredes Ruiz", correo="daniela.paredes@vetsalud.ec", licencia="VET-001", consultorio=consultorios[0]),
            Veterinario(nombres="Roberto", apellidos="Salazar León", correo="roberto.salazar@vetsalud.ec", licencia="VET-002", consultorio=consultorios[1]),
            Veterinario(nombres="Mariana", apellidos="Cordero Vega", correo="mariana.cordero@huellitas.ec", licencia="VET-003", consultorio=consultorios[2]),
            Veterinario(nombres="Felipe", apellidos="Ortega Ruiz", correo="felipe.ortega@huellitas.ec", licencia="VET-004", consultorio=consultorios[3]),
            Veterinario(nombres="Valeria", apellidos="Sánchez Mora", correo="valeria.sanchez@animalcare.ec", licencia="VET-005", consultorio=consultorios[4]),
            Veterinario(nombres="Gabriel", apellidos="Vera López", correo="gabriel.vera@animalcare.ec", licencia="VET-006", consultorio=consultorios[5]),
        ]
        session.add_all(vets)
        session.flush()

        historias = [
            HistoriaClinica(fecha_atencion=date(2026, 10, 5), diagnostico="Gastroenteritis leve", tratamiento="Dieta blanda e hidratación", mascota="Max", veterinario=vets[0]),
            HistoriaClinica(fecha_atencion=date(2026, 10, 8), diagnostico="Otitis externa", tratamiento="Limpieza y gotas óticas", mascota="Luna", veterinario=vets[0]),
            HistoriaClinica(fecha_atencion=date(2026, 10, 10), diagnostico="Fractura de miembro posterior", tratamiento="Intervención quirúrgica", mascota="Rocky", veterinario=vets[1]),
            HistoriaClinica(fecha_atencion=date(2026, 10, 12), diagnostico="Dermatitis alérgica", tratamiento="Tratamiento dermatológico", mascota="Nala", veterinario=vets[2]),
            HistoriaClinica(fecha_atencion=date(2026, 10, 15), diagnostico="Infección respiratoria", tratamiento="Medicación y seguimiento", mascota="Toby", veterinario=vets[3]),
            HistoriaClinica(fecha_atencion=date(2026, 10, 18), diagnostico="Luxación de rótula", tratamiento="Evaluación y tratamiento quirúrgico", mascota="Milo", veterinario=vets[4]),
            HistoriaClinica(fecha_atencion=date(2026, 10, 20), diagnostico="Enfermedad periodontal", tratamiento="Limpieza dental veterinaria", mascota="Coco", veterinario=vets[5]),
            HistoriaClinica(fecha_atencion=date(2026, 10, 22), diagnostico="Control de vacunación", tratamiento="Aplicación de vacuna anual", mascota="Luna", veterinario=vets[3]),
        ]
        session.add_all(historias)
        session.commit()
        print("Carga completada: 3 clínicas, 6 consultorios, 6 veterinarios y 8 historias clínicas.")
    except Exception as error:
        session.rollback()
        print(f"No fue posible completar la carga: {error}")
        raise
    finally:
        session.close()

if __name__ == "__main__":
    poblar_base()
