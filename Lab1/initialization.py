import glfw
from OpenGL.GL import *

def main():
    # Initialize GLFW
    if not glfw.init():
        print("Failed to initialize GLFW")
        return

    # Set GLFW window hints
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "OpenGL Window", None, None)
    if not window:
        glfw.terminate()
        print("Failed to create GLFW window")
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Main rendering loop
    while not glfw.window_should_close(window):
        # Clear the color buffer
        glClear(GL_COLOR_BUFFER_BIT)

        # Set the color to white
        glColor3f(1.0, 1.0, 1.0)

        # Draw your graphics here...

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
