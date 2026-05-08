import reflex as rx


def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "⚽ Mundo Fútbol",
                size="9",
                color="white",
            ),

            rx.text(
                "Bienvenido a mi primera página web creada con Reflex y Python.",
                color="white",
                size="5",
                text_align="center",
            ),

            rx.image(
                src="https://images.unsplash.com/photo-1574629810360-7efbbe195018",
                width="500px",
                border_radius="20px",
            ),

            rx.hstack(
                rx.button(
                    "Ver Equipos",
                    color_scheme="green",
                    size="3",
                ),

                rx.button(
                    "Resultados",
                    color_scheme="blue",
                    size="3",
                ),

                spacing="4",
            ),

            rx.box(
                rx.text(
                    "El fútbol es el deporte más popular del mundo y reúne millones de fanáticos cada día.",
                    color="white",
                    text_align="center",
                    padding="20px",
                ),
                background_color="rgba(255,255,255,0.1)",
                border_radius="15px",
                width="70%",
            ),

            spacing="6",
            align="center",
        ),

        background="linear-gradient(to right, #0f2027, #203a43, #2c5364)",
        min_height="100vh",
        padding="40px",
    )


app = rx.App()
app.add_page(index)