# Sistema de gestión de clínicas veterinarias

Proyecto académico de la Unidad 3: acceso a bases de datos relacionales mediante ORM.

## Tecnologías
- Python 3
- SQLite
- SQLAlchemy ORM

## Archivos
- `configuracion.py`: conexión SQLite, activación de claves foráneas y sesiones.
- `crear_base_entidades.py`: entidades Clínica, Consultorio, Veterinario e HistoriaClinica y sus relaciones.
- `poblar_base.py`: carga de datos demostrativos sin duplicar registros.
- `consulta_all.py`: muestra todas las clínicas y cuenta sus historias clínicas.
- `consulta_filter.py`: ejemplos de `filter()`.
- `consulta_order_by.py`: ejemplos de `order_by()`.
- `consulta_or.py`: ejemplos de `or_()`.
- `consulta_and.py`: ejemplos de `and_()`.

## Instalación y ejecución
Abre una terminal en esta carpeta y ejecuta:

```bash
python -m pip install -r requirements.txt
python crear_base_entidades.py
python poblar_base.py
python consulta_all.py
python consulta_filter.py
python consulta_order_by.py
python consulta_or.py
python consulta_and.py
```

La base de datos `clinicas_veterinarias.db` se crea localmente en esta misma carpeta. Para repetir las pruebas desde cero, cierra los programas que la estén usando y elimina ese archivo; luego ejecuta nuevamente los comandos en el orden indicado.

## Datos de demostración
La carga inicial incorpora 3 clínicas, 6 consultorios, 6 veterinarios y 8 historias clínicas. El resultado esperado de `consulta_all.py` es: VetSalud Central = 3, Huellitas del Sur = 3 y AnimalCare = 2.

## Relaciones
- Clínica 1:N Consultorio.
- Consultorio 1:N Veterinario.
- Veterinario 1:N Historia clínica.

Las claves foráneas son obligatorias (`nullable=False`), y correo y licencia profesional son únicos.
