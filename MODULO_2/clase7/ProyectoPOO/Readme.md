# Sistema de Veterinaria

Este proyecto implementa un sistema de gestión para una clínica veterinaria. Permite registrar clientes, registrar mascotas, programar citas, actualizar y consultar el historial de las mascotas.

---

## Clases

### `Persona` (Abstracta)
Clase base para representar una persona (cliente o veterinario).

**Atributos:**
- `nombre` : str
- `contacto` : str
- `direccion` : str

**Métodos:**
- `mostrar_informacion()` : Método abstracto que devuelve la información de la persona.

---

### `Cliente` (Hereda de `Persona`)
Representa un cliente de la veterinaria.

**Atributos:**
- `mascotas` : Lista de objetos `Mascota`

**Métodos:**
- `agregar_mascota(mascota)` : Agrega una mascota al cliente.
- `mostrar_informacion()` : Devuelve un string con la información del cliente.

---

### `Mascota` (Abstracta)
Clase base para representar una mascota.

**Atributos:**
- `nombre` : str
- `especie` : str
- `raza` : str
- `edad` : int
- `historial_citas` : lista de objetos `Cita`

**Métodos:**
- `agregar_al_historial(detalles_servicio)` : Método abstracto, agrega un registro de cita.
- `obtener_historial()` : Método abstracto, devuelve el historial de citas.

---

### `RegistroMascota` (Hereda de `Mascota`)
Implementación concreta de la clase `Mascota`.

**Métodos:**
- `agregar_al_historial(detalles_servicio)` : Agrega una cita al historial.
- `obtener_historial()` : Devuelve todas las citas registradas.

---

### `Cita` (Abstracta)
Representa una cita veterinaria.

**Atributos:**
- `fecha` : str (formato `AAAA-MM-DD`)
- `hora` : str (formato `HH:MM`)
- `servicio` : str (consulta, vacunación, etc.)
- `veterinario` : str

**Métodos:**
- `actualizar(**kwargs)` : Método abstracto para actualizar los datos de la cita.

---

### `CitaMascota` (Hereda de `Cita`)
Implementación concreta de la clase `Cita`.

**Métodos:**
- `actualizar(**kwargs)` : Permite actualizar cualquiera de los atributos de la cita.

---

### `SistemaVeterinaria`
Clase principal que maneja la lógica del sistema.

**Atributos:**
- `clientes` : Lista de objetos `Cliente`

**Métodos:**
1. `registrar_cliente()` : Pide los datos de un cliente y lo agrega al sistema.
2. `registrar_mascota()` : Pide los datos de una mascota y la asocia a un cliente existente.
3. `programar_cita()` : Registra una nueva cita para una mascota.
4. `ActualizaCita()` : Permite modificar los detalles de una cita existente.
5. `consultar_Cita()` : Muestra todas las citas registradas de una mascota.
6. `Iniciar()` : Muestra el menú principal y permite seleccionar las opciones.

---

## Uso del sistema

1. Ejecuta el archivo principal (`python nombre_del_archivo.py`).
2. Selecciona una opción del menú.
3. Ingresa los datos solicitados según la operación.

---

## Notas técnicas

- El sistema utiliza **clases abstractas** para definir la estructura de `Persona`, `Mascota` y `Cita`.
- Se aplica **herencia** al implementar `Cliente`, `RegistroMascota` y `CitaMascota`.
- Se aplica **polimorfismo** en el método `actualizar()` de las citas.
- El historial de cada mascota se mantiene en la lista `historial_citas`.

---

