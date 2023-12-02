import reflex as rx

def index() -> rx.Component:
    return rx.box(

    )

app = rx.App (


)

app.add_page (
    index,
    title="Calendario de Adviento 2023",
    description="Recibe tu regalo cada día"
)

app.compile()