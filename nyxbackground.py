################
#### nyx
import os
import pygame
import random
import sys
from PIL import Image

# Inicializar pygame
pygame.init()

# Configuración de la pantalla "aqui cambiar de acuerdo a la resolucion de su monitor"
screen_width, screen_height = 1366, 770

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("NyxF3r")

# Colores y fuentes
background_color = (208, 247, 128)  #color de fondo principal
head_text_color = (0, 250, 0) #color de la primera letra
head_background_color = (0, 0, 0) #color de fondo de la primera letra
#el texto es degrado empieza de negro a gris
trail_start_color = (0, 0, 0) #color del texto negro 
trail_end_color = (64, 64, 64) #color de texto gris al final

# Nombre de la fuente instalada en el sistema
font_name = "AcPlus_ToshibaTxL1_8x16"  # Nombre de la fuente sin la extensión .ttf
font_size = 24

# Cargar la fuente desde el sistema
font = pygame.font.SysFont(font_name, font_size)

# Si la fuente no está disponible, pygame.sysfont devuelve una fuente predeterminada.
if not font:
    print("Fuente no encontrada en el sistema. Usando fuente predeterminada.")
    font = pygame.font.SysFont("Arial", font_size)  # Usar fuente predeterminada como respaldo

# Clase para manejar GIF animados
class AnimatedGIF:
    def __init__(self, filepath):
        self.frames = []
        self.load_gif(filepath)
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()

    def load_gif(self, filepath):
        try:
            pil_image = Image.open(filepath)
            for frame in range(pil_image.n_frames):
                pil_image.seek(frame)
                # Convertir a modo RGBA para evitar fondo blanco
                frame_surface = pygame.image.fromstring(
                    pil_image.convert("RGBA").tobytes(), pil_image.size, "RGBA"
                )
                self.frames.append(frame_surface)
        except Exception as e:
            print(f"Error al cargar GIF: {e}")
            sys.exit()

    def get_current_frame(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:  # Cambiar frame cada 100ms
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = now
        return self.frames[self.current_frame]

# Clase para manejar PNG estáticos
class StaticImage:
    def __init__(self, filepath):
        self.image = pygame.image.load(filepath).convert_alpha()

    def get_current_frame(self):
        return self.image

# Cargar imagen (puede ser PNG o GIF y debe estar en la misma carpeta donde esta el archivo python)
image_file = "skull.gif"  # Cambia esta imagen si decides usar PNG o GIF, la imagen debe estar en el mismo archivo
animation = None

if image_file.endswith(".gif"):
    animation = AnimatedGIF(image_file)
elif image_file.endswith(".png"):
    animation = StaticImage(image_file)
else:
    print("Formato no soportado. Usa PNG o GIF.")
    pygame.quit()
    sys.exit()

# Clase para las columnas animadas
class MatrixColumn:
    def __init__(self, x_position):
        self.x = x_position
        self.y = random.randint(0, screen_height)
        self.speed = random.uniform(1, 80)  #Velocidad algunos 1 o 80
        self.char = 'ô'  #caracter de la primera letra pueden reemplazar por una letra o icono hacknerdfont
        self.trail_length = random.randint(10, 30)
        self.trail = [random.choice('01') for _ in range(self.trail_length)]
        self.in_front = random.choice([True, False])

    def update(self):
        self.y -= self.speed
        if self.y < -self.trail_length * font.size(" ")[1]:
            self.y = screen_height
            self.trail = [random.choice('01') for _ in range(self.trail_length)]
            self.in_front = random.choice([True, False])

    def update_trail(self):
        self.trail = [random.choice('01') for _ in range(self.trail_length)]

    def draw(self):
        head_width, head_height = font.size(self.char)
        head_rect = pygame.Rect(self.x, self.y, head_width, head_height)
        pygame.draw.rect(screen, head_background_color, head_rect)
        head_surface = font.render(self.char, True, head_text_color)
        screen.blit(head_surface, (self.x, self.y))

        for i, trail_char in enumerate(self.trail):
            color_ratio = i / self.trail_length
            trail_color = (
                int(trail_start_color[0] * (1 - color_ratio) + trail_end_color[0] * color_ratio),
                int(trail_start_color[1] * (1 - color_ratio) + trail_end_color[1] * color_ratio),
                int(trail_start_color[2] * (1 - color_ratio) + trail_end_color[2] * color_ratio),
            )
            alpha_text = max(255 - (i * 25), 0)
            trail_surface = font.render(trail_char, True, trail_color)
            trail_surface.set_alpha(alpha_text)
            trail_y_position = self.y + (i + 1) * font.size(" ")[1] * 0.8
            screen.blit(trail_surface, (self.x, trail_y_position))

# Crear las columnas
column_spacing = font.size(" ")[0] * 1
columns = [MatrixColumn(x * column_spacing) for x in range(screen_width // int(column_spacing))]

# Crea carpeta para guardar los frames
frames_folder = "frames"
if not os.path.exists(frames_folder):
    os.makedirs(frames_folder)

# Variables para animación
clock = pygame.time.Clock()
frame_count = 0  # Contador de frames

# Variables para posicionar el GIF/PNG
x_offset = 20  # Mueve horizontalmente (positivo: derecha, negativo: izquierda)
y_offset = 100  # Mueve verticalmente (positivo: abajo, negativo: arriba)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rellenar fondo
    screen.fill(background_color)

    # Dibujar columnas detrás de las imágenes
    for column in columns:
        if not column.in_front:
            column.update()
            column.update_trail()
            column.draw()

    # Dibujar la animación actual con nueva posición
    if animation:
        frame = animation.get_current_frame()
        x_position = ((screen_width - frame.get_width()) // 2) + x_offset
        y_position = ((screen_height - frame.get_height()) // 2) + y_offset
        screen.blit(frame, (x_position, y_position))

    # Dibujar columnas frente a las imágenes
    for column in columns:
        if column.in_front:
            column.update()
            column.update_trail()
            column.draw()

    # Guardar el frame como imagen   "esto hace que guarde imagenes de la animacion python para poner de fondo de pantalla"
    #frame_path = os.path.join(frames_folder, f"frame_{frame_count:04d}.png")
    #pygame.image.save(screen, frame_path)
    #frame_count += 1

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(10)
