import pygame



def get_keyboard_inputs():
    keys = pygame.key.get_pressed()

    return {

        1 : {
            "movement_x" : int(keys[pygame.K_d]) - int(keys[pygame.K_a]),
            "movement_y" : int(keys[pygame.K_s]) - int(keys[pygame.K_w]),
            "button_a" : keys[pygame.K_q],
            "button_b" : keys[pygame.K_e]
        }
        
    }

