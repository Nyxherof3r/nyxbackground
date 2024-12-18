# NyxBackground

Este proyecto utiliza Python y Pygame para crear una animación personalizada en tu escritorio. Sigue los pasos a continuación para configurar el entorno y ejecutar el script.

---

## ⚙️ Pasos de instalación

### 1. Clonar este repositorio
Primero, clona el repositorio en tu equipo local usando el siguiente comando:
```
git clone https://github.com/Nyxherof3r/nyxbackground.git
```
### 2. Crear la carpeta de destino
Copia el contenido del repositorio en la carpeta ~/scripts/nyxbackground. Puedes crear esta carpeta ejecutando:
```
mkdir -p ~/scripts/nyxbackground
```
Luego, copia todo el contenido del repositorio a esa carpeta:
```
cp -r nyxbackground/* ~/scripts/nyxbackground/
```
### 3. Crear un entorno virtual
Navega a la carpeta donde está el archivo Python y crea un entorno virtual:
```
cd ~/scripts/nyxbackground
python3 -m venv env
```
Activa el entorno virtual:
En Linux/Mac:
```
source env/bin/activate
```
### 4. Instalar las dependencias
Con el entorno virtual activado, instala las dependencias necesarias:
```
pip install pygame pillow
```
### 5. Ejecutar el script
Finalmente, ejecuta el script desde la misma carpeta para probar la animación:
```
python nyxbackground.py
```
---
## 📂 Estructura del proyecto
````
nyxbackground/
├── nyxbackground.py       # Script principal
├── frames/                # Carpeta donde se guardan los frames generados
├── skull.gif              # Archivo de ejemplo para el GIF animado
└── requirements.txt       # Dependencias del proyecto
````
## 🛠️ Notas
- Asegúrate de tener Python 3 instalado en tu sistema.
- Si experimentas algún problema al ejecutar el script, verifica la ruta del archivo de fuente o del GIF animado.
