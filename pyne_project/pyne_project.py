import pynecone as pc

class State(pc.State):
    initial = 1

    def multiply(self):
        self.initial *= 2

    def divide(self):
        self.initial /= 2


def index():
    return pc.hstack(
        pc.button(
            "Multiply",
            color_scheme="blue",
            border_radius="1em",
            on_click=State.multiply,
        ),
        pc.text(State.initial, font_size="2em"),
        pc.button(
            "Divide",
            color_scheme="red",
            border_radius="1em",
            on_click=State.divide,
        ),
    )

app = pc.App(state=State)
app.add_page(index, title="Multiply and Divide App")
app.compile()
