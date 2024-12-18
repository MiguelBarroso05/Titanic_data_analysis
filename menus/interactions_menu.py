import threading
import time
import sys
import os

def clean():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')


def press_any_key_with_animation():
    """
    Displays 'Press any key to continue...' with an animated boat on the same lines.
    """
    stop_animation = [False] 
    boat_frames = [
        "  ~    ~    ~    ~    🚤  ~    ~    ~    ~",
        "    ~    ~    ~    ~   🚤  ~    ~    ~    ~",
        " ~    ~    ~    ~    ~ 🚤   ~    ~    ~    ~",
        "    ~    ~    ~    ~   🚤  ~    ~    ~    ~",
    ]

    def boat_animation():
        first_interaction = False
        dots = 0

        while not stop_animation[0]:
            # Limpa apenas as duas últimas linhas usando escape sequences depois de ter sido chamado e iterado pelo menos 1 vez
            if first_interaction:
                sys.stdout.write("\033[F\033[K" * 2)  # Sobe 2 linhas e limpa
                sys.stdout.flush()
            else: 
                first_interaction = True

            # Mensagem fixa
            print(f"Press any key to continue{'.' * (dots % 4)}")
            print(boat_frames[dots % len(boat_frames)])
            dots += 1
            time.sleep(0.3) 

    print("\n")
    animation_thread = threading.Thread(target=boat_animation)
    animation_thread.start()

    try:
        input()
    finally:
        stop_animation[0] = True  # Sinaliza para parar a animação
        animation_thread.join()  # Garante que a thread termina
        print("\033[F\033[K" * 2, end="")  # Limpa as linhas finais após parar
        