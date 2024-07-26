import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to animate a moving shape
def animate_shape(shape, motion_style):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)
    
    # Define the initial position and velocity of the shape
    if shape == 'rectangle':
        rect = plt.Rectangle((1, 5), 2, 1, color='b')
        ax.add_patch(rect)
        obj = rect
        obj.velocity = [0.5, 0]  # Only x-direction movement for linear and bounce
    elif shape == 'circle':
        circle = plt.Circle((1, 5), 0.5, color='b')
        ax.add_patch(circle)
        obj = circle
        obj.velocity = [0.5, 0]  # Only x-direction movement for linear and bounce
    else:
        print("Invalid shape type.")
        return
    
    # Define the animation update function
    def update(frame):
        if motion_style == 'linear':
            # Linear motion (constant velocity)
            if shape == 'rectangle':
                obj.set_xy((1 + frame * 0.5, 5))  # Move along x-axis
            elif shape == 'circle':
                obj.center = (1 + frame * 0.5, 5)
        elif motion_style == 'bounce':
            # Bouncing motion (reverses direction at boundaries)
            if shape == 'rectangle':
                x, y = obj.get_xy()
                if x + obj.get_width() >= 10 or x <= 0:
                    obj.velocity[0] *= -1
                obj.set_xy((x + obj.velocity[0], y))
            elif shape == 'circle':
                x, y = obj.center
                if x + obj.radius >= 10 or x - obj.radius <= 0:
                    obj.velocity[0] *= -1
                obj.center = (x + obj.velocity[0], y)
        return obj,
    
    ani = animation.FuncAnimation(fig, update, frames=20, interval=100, blit=True)
    plt.show()

# Main function to prompt user for animation parameters
def main():
    # Prompt user for the type of shape (rectangle or circle)
    shape_type = input("Enter shape type (rectangle or circle): ").lower()
    # Prompt user for the animation style (linear or bounce)
    motion_style = input("Enter motion style (linear or bounce): ").lower()
    # Validate user input and start animation
    if shape_type in ['rectangle', 'circle'] and motion_style in ['linear', 'bounce']:
        animate_shape(shape_type, motion_style)
    else:
        print("Invalid input. Please choose a valid shape type (rectangle or circle) and motion style (linear or bounce).")

if __name__ == "__main__":
    main()
