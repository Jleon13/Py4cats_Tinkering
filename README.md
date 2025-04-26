# Proyecto de Simulación de Atenuación Atmosférica con Py4CAtS

Este proyecto utiliza Py4CAtS para realizar simulaciones de la transmisión radiativa atmosférica mediante la lectura de datos espectrales y atmosféricos. Se implementan secciones transversales, profundidades ópticas y simulaciones de radiación a través de notebooks interactivos.

## 1. Requisitos Previos

- [Conda](https://docs.conda.io/en/latest/miniconda.html) o [Anaconda](https://www.anaconda.com/products/distribution).
- Acceso a internet para descargar el paquete Py4CAtS y otros datos necesarios.
- Python (>=3.10).

## 2. Crear y Activar el Entorno

Desde una terminal, ejecuta los siguientes comandos para crear y activar un entorno llamado `standoff`:

```sh
conda create -n standoff python=3.10.16 -y
conda activate standoff
```

## 3. Instalar Py4CAtS

Con el entorno activado, instala Py4CAtS utilizando el archivo wheel:

```sh
pip install https://atmos.eoc.dlr.de/tools/Py4CAtS/py4cats-4.0.0-py3-none-any.whl
```

Este comando instalará Py4CAtS junto a sus dependencias (como IPython, matplotlib, numpy, scipy, etc.).

## 4. Archivos y Datos Necesarios

Para el correcto funcionamiento del proyecto, asegúrate de tener los siguientes archivos organizados en la siguiente estructura:

- **Archivo de parámetros de líneas:**
  - `680HIT86b.par`  
    (Contiene parámetros espectrales usados por la función `higstract` para leer las líneas espectrales).

- **Datos atmosféricos:**
  - `data_and_doc/data/atmos/20/mls.xy`  
    (Perfil atmosférico leído por la función `atmRead`).

  - Opcionalmente, otros niveles o archivos atmosféricos (p. ej. `mlw.xy`) conforme a la simulación.

- **Archivos de líneas espectrales:**
  - Se encuentran en `data_and_doc/data/lines/` y se utilizan mediante las funciones `atlas`, `lbl2xs`, `lbl2od`, entre otras.

- **Documentación y Datos Adicionales:**
  - Se recomienda descargar y desempaquetar el archivo `data_and_doc.tgz` (si se incluye en el proyecto) para acceder a ejemplos, documentación y datos complementarios.
  
  Para desempaquetarlo:
  
  ```sh
  tar xfvz data_and_doc.tgz
  ```

## 5. Uso del Proyecto

El proyecto se puede ejecutar a través de notebooks interactivos (por ejemplo, `forward.ipynb` y otros notebooks) en Visual Studio Code o Jupyter.

### Ejecución:

1. **Abrir el Notebook:**
   - Inicia Visual Studio Code o Jupyter Notebook.
   - Abre el notebook `forward.ipynb`.

2. **Ejecutar Secciones:**
   - El notebook está organizado en secciones:
     - **Importación de Librerías:** Se importan funciones de Py4CAtS para la simulación.
     - **Lectura de Datos:** Se define el rango espectral y se leen los archivos de parámetros (`680HIT86b.par`) y del perfil atmosférico (`mls.xy`).
     - **Visualización de Datos:** Funciones como `atmPlot`, `atlas`, `xsPlot`, `odPlot` y `riPlot` muestran los gráficos de la simulación.
     - **Cálculos de Sección Cruzada y Profundidad Óptica:** Se utiliza `lbl2xs` para obtener la sección cruzada, utilizando valores escalares o perfiles según la configuración.
     - **Cálculos de la Radiancia** Se utiliza `dod2ri` para obtener la radiación a partir de la profundidad óptica


## 6. Notas Adicionales

- Para mayor información y ejemplos de uso, consulta la documentación en el directorio `doc` o en la página oficial: [Py4CAtS Home-page](https://atmos.eoc.dlr.de/tools/Py4CAtS/index.html).

Con estos pasos ya estarás listo para empezar a trabajar con las simulaciones de atenuación atmosférica utilizando Py4CAtS.

¡Disfruta explorando las capacidades de modelado atmosférico!