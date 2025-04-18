import reflex as rx

from rxconfig import config

class State(rx.State):
    """The app state."""
    ...

def index() -> rx.Component:
    # Mostrar "¡Hola Mundo!" en el centro de la página
    return rx.center(
        rx.text("¡Hola Mundo!")
    )

app = rx.App()
app.add_page(index)
