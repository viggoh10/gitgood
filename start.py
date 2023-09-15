from donut import *
import time


if __name__ == "__main__":
    for i in range(screen_size):
          print()

    for _ in range(100):
        A += theta_spacing
        B += phi_spacing
        print("\033[1A"*(screen_size+1))  # Move cursor up one line
        pprint(render_frame(A, B))
        time.sleep(0.01)
