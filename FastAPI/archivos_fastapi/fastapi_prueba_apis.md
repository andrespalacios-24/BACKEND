# Prueba de APIs — Postman y Thunder Client

Fuentes: [Postman Docs](https://learning.postman.com/docs/introduction/overview/) · [Thunder Client Docs](https://github.com/rangav/thunder-client-support#readme) · [FastAPI - First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)

---

## 1. Por qué usar un cliente HTTP para probar APIs

Durante el desarrollo de un backend, necesitás verificar que cada endpoint responde correctamente antes de conectarlo a un frontend o a otro servicio. El navegador solo permite hacer peticiones GET escribiendo una URL. Para hacer peticiones POST, PUT, DELETE, o para enviar headers y cuerpos JSON, necesitás una herramienta específica.

Un **cliente HTTP** es esa herramienta. Permite construir cualquier tipo de petición, enviarla al servidor y examinar la respuesta completa: código de estado, headers y cuerpo.

Momento de uso: cada vez que definís un nuevo endpoint o modificás uno existente, lo probás con el cliente HTTP antes de avanzar.

---

## 2. Postman

Postman es la herramienta de prueba de APIs más usada en la industria. Es una aplicación de escritorio (también tiene versión web) con interfaz gráfica completa.

Descarga: [https://www.postman.com/downloads/](https://www.postman.com/downloads/)

### Instalación

Descargá el instalador desde el link de arriba. No requiere cuenta para uso básico local (podés saltear el login).

### Interfaz principal

Al abrir Postman, las áreas clave son:

| Área              | Para qué sirve                                              |
|-------------------|-------------------------------------------------------------|
| Barra superior    | Seleccionar método HTTP, escribir la URL y enviar          |
| Pestaña Params    | Agregar query parameters visualmente                        |
| Pestaña Headers   | Agregar headers (ej: `Content-Type`, `Authorization`)       |
| Pestaña Body      | Escribir el cuerpo de la petición (para POST, PUT)          |
| Panel inferior    | Ver la respuesta: código de estado, tiempo, headers y body  |
| Collections       | Guardar y organizar grupos de peticiones por proyecto       |

### Hacer una petición GET

1. Abrís una nueva pestaña (botón `+`).
2. Seleccionás el método `GET` en el selector de la izquierda.
3. Escribís la URL: `http://127.0.0.1:8000/`
4. Hacés clic en **Send**.
5. En el panel inferior aparece la respuesta.

```
Método: GET
URL:    http://127.0.0.1:8000/
```

Respuesta esperada (panel Body, pestaña Pretty):
```json
"Hola FastAPI!"
```

### Hacer una petición GET con query parameters

En lugar de escribir `?skip=0&limit=10` directo en la URL, podés usar la pestaña **Params**:

1. Abrís la pestaña **Params** debajo de la URL.
2. Agregás las claves y valores en la tabla.
3. Postman construye la URL automáticamente.

```
Método: GET
URL:    http://127.0.0.1:8000/items
Params: skip=0 / limit=10
```

### Hacer una petición POST con body JSON

1. Seleccionás el método `POST`.
2. Escribís la URL.
3. Abrís la pestaña **Body**.
4. Seleccionás **raw** y en el selector de formato elegís **JSON**.
5. Escribís el JSON del cuerpo.
6. Hacés clic en **Send**.

```
Método: POST
URL:    http://127.0.0.1:8000/users
Body (raw JSON):
{
    "nombre": "Andrés",
    "edad": 30
}
```

Postman agrega automáticamente el header `Content-Type: application/json` al seleccionar JSON.

### Leer la respuesta

El panel de respuesta muestra:

| Elemento         | Qué indica                                                  |
|------------------|-------------------------------------------------------------|
| Código de estado | `200 OK`, `201 Created`, `404 Not Found`, `422`, etc.       |
| Time             | Cuántos milisegundos tardó la respuesta                     |
| Size             | Tamaño del cuerpo de respuesta                              |
| Body → Pretty    | JSON formateado y con colores, fácil de leer                |
| Body → Raw       | Respuesta sin formato, exactamente como llegó               |
| Headers          | Headers que devolvió el servidor                            |

### Collections: organizar peticiones por proyecto

Una **Collection** es una carpeta donde guardás todas las peticiones de un proyecto. Así no tenés que reescribir las URLs cada vez.

Para crear una:
1. Panel izquierdo → **Collections** → botón `+`.
2. Nombrás la colección (ej: `FastAPI - Proyecto`).
3. Dentro podés crear carpetas por recurso (`/users`, `/products`, etc.).
4. Cada petición se guarda con nombre, método, URL, headers y body.

Referencia: [Postman - Sending Requests](https://learning.postman.com/docs/sending-requests/requests/) · [Postman - Collections](https://learning.postman.com/docs/collections/collections-overview/)

---

## 3. Thunder Client

Thunder Client es una extensión de VS Code que hace lo mismo que Postman pero dentro del editor. No requiere instalar nada externo ni abrir otra aplicación.

### Cuándo usar Thunder Client en lugar de Postman

| Situación                                      | Herramienta recomendada |
|------------------------------------------------|-------------------------|
| Pruebas rápidas sin salir de VS Code           | Thunder Client          |
| Proyectos en equipo con colecciones compartidas | Postman                 |
| Flujos de prueba complejos o automatizados     | Postman                 |
| Estás aprendiendo y querés simplicidad         | Thunder Client          |

Para el flujo de estudio actual, Thunder Client es suficiente y más cómodo.

### Instalación

1. En VS Code, abrís el panel de extensiones (`Ctrl+Shift+X`).
2. Buscás `Thunder Client`.
3. Instalás la extensión de **Rangav** (es la oficial).
4. Aparece el ícono del rayo en la barra lateral izquierda.

Documentación: [https://github.com/rangav/thunder-client-support](https://github.com/rangav/thunder-client-support)

### Interfaz

Al hacer clic en el ícono del rayo, se abre el panel con:

| Área          | Para qué sirve                                              |
|---------------|-------------------------------------------------------------|
| New Request   | Abre una petición nueva                                     |
| Collections   | Guarda y organiza peticiones (igual que Postman)            |
| Env           | Variables de entorno (ej: `base_url = http://127.0.0.1:8000`) |
| Activity      | Historial de peticiones recientes                           |

### Hacer una petición GET

1. Clic en **New Request**.
2. En el selector de método elegís `GET`.
3. Escribís la URL: `http://127.0.0.1:8000/`
4. Clic en **Send**.
5. La respuesta aparece en el panel derecho.

### Hacer una petición POST con body JSON

1. **New Request** → método `POST`.
2. URL del endpoint.
3. Pestaña **Body** → seleccionás **JSON**.
4. Escribís el cuerpo JSON.
5. **Send**.

```
Método: POST
URL:    http://127.0.0.1:8000/users
Body:
{
    "nombre": "Andrés",
    "edad": 30
}
```

### Variables de entorno

Si todos tus endpoints empiezan con `http://127.0.0.1:8000`, podés definir esa base como variable para no repetirla en cada petición.

1. Panel **Env** → **New Environment** → nombre: `local`.
2. Agregás variable: `base_url` = `http://127.0.0.1:8000`.
3. En las URLs usás `{{base_url}}/users`, `{{base_url}}/items`, etc.

Si el día de mañana el servidor cambia de puerto o dirección, cambiás solo la variable y todas las peticiones se actualizan.

---

## 4. Qué observar en cada respuesta

Independientemente de la herramienta, al probar un endpoint fijate siempre en:

### Código de estado

Es lo primero que indica si algo salió bien o mal.

```
200 OK               → respuesta exitosa
201 Created          → recurso creado (POST exitoso)
404 Not Found        → la ruta no existe o el recurso no se encontró
422 Unprocessable    → FastAPI rechazó los datos por tipo o formato incorrecto
500 Internal Error   → error no manejado en el código del servidor
```

Un `422` de FastAPI siempre viene acompañado de un cuerpo JSON que explica exactamente qué campo falló y por qué. Es el error más común durante el desarrollo.

Ejemplo de respuesta `422`:
```json
{
  "detail": [
    {
      "loc": ["query", "user_id"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

### Cuerpo de la respuesta (Body)

Verificás que la estructura del JSON devuelto es la esperada: que los campos existen, tienen los nombres correctos y los tipos correctos.

### Headers de la respuesta

FastAPI devuelve por defecto `content-type: application/json`. Si ves un tipo distinto, algo puede estar mal en el retorno.

### Tiempo de respuesta

En desarrollo local con datos de prueba, una respuesta debería tardar menos de 50ms. Si tarda más, puede haber un problema de lógica o una operación bloqueante.

---

## 5. Flujo de trabajo recomendado

```
1. Escribís o modificás un endpoint en main.py
2. Guardás el archivo (Ctrl+S) — uvicorn recarga automáticamente con --reload
3. Abrís Thunder Client (o Postman)
4. Construís la petición: método + URL + params/body si corresponde
5. Enviás y revisás: código de estado → body → estructura del JSON
6. Si hay error 422: revisás los tipos de parámetros en la función
7. Si hay error 500: revisás la terminal donde corre uvicorn — ahí está el traceback
8. Cuando el endpoint responde correctamente, avanzás al siguiente
```

El terminal donde corre uvicorn es tu aliado: cada petición que llega se imprime ahí con su método, ruta y código de respuesta. Los errores del servidor (`500`) muestran el traceback completo en esa terminal.

```
INFO:     127.0.0.1:PORT - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:PORT - "GET /url HTTP/1.1" 200 OK
INFO:     127.0.0.1:PORT - "POST /users HTTP/1.1" 422 Unprocessable Entity
```
