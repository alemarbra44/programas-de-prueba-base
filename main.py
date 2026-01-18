import pygame
import asyncio # <--- 1. Importante: Necesario para la web

async def main(): # <--- 2. juego debe estar dentro de función "async"
    #async: en python permite ejecutar funciones sin 
    # interrumpir la funcion principal, o sea en paralelo
    #  https://youtu.be/dEvUiYIfLPw?si=RiFFAQsvaxXEqjuZ

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mi Juego Web")
    
    # 1. CARGAR RECURSOS (Imágenes y Sonidos)
    # Importante: Siempre usa la ruta 'assets/nombre_archivo'
    try:
        personaje = pygame.image.load("assets/imagen_personaje.png")
        personaje_rect = personaje.get_rect(center=(400, 300))
        sonido = pygame.mixer.Sound("assets/sonido_clic.wav")
    except:
        # Esto crea un cuadro rojo si no encuentra la imagen
        personaje = pygame.Surface((100, 100))
        personaje.fill("red")
        personaje_rect = personaje.get_rect(center=(400, 300))

    # 2. CONFIGURAR TEXTO
    fuente = pygame.font.SysFont("Arial", 36)
    mensaje = "¡Toca al personaje!"

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # 3. DETECTAR TOQUE EN EL PERSONAJE
            if event.type == pygame.MOUSEBUTTONDOWN:
                if personaje_rect.collidepoint(event.pos):
                    mensaje = "¡Lo tocaste!"
                    try: sonido.play() # Reproduce sonido
                    except: pass

        # --- DIBUJO ---
        screen.fill("bisque") # Fondo
        
        # Dibujar imagen
        screen.blit(personaje, personaje_rect)
        
        # Dibujar texto
        texto_render = fuente.render(mensaje, True, (0, 0, 0))
        screen.blit(texto_render, (20, 20))
        
        pygame.display.flip()

        # --- MANTENER VIVO EL NAVEGADOR ---
        clock.tick(60) # Limita a 60 FPS
        await asyncio.sleep(0) # <--- 3. ESTA ES LA LÍNEA MÁGICA
        # Esta línea le dice al navegador: "Ya terminé este cuadro, 
        # puedes procesar otras cosas y luego regresas a mí".

# 4. Forma especial de arrancar el juego:
asyncio.run(main())