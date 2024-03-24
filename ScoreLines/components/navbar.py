import reflex as rx


def navbar():
    return rx.box(
        rx.flex(
            rx.box(
                rx.hstack(
                    rx.image(src='/score.jpg', width='60px'),  # favicon image
                    rx.text("ScoreLines Sport!",background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                    background_clip="text",
                    font_weight="bold",
                    font_size="2em",),       # additional text with white color for visibility
                    spacing="10px"
                ),
            ), rx.spacer(),

            rx.box(
                rx.hstack(
                    rx.input(placeholder="Search keyword"),
                    rx.button("Search"),
                ),
            ), rx.spacer(),

            rx.menu(
                rx.menu_button('menu', bg="#1D1D38", color="#000000", padding="10px"),  # Menu button with padding added
                rx.menu_list(
                    rx.menu_item(
                        rx.link('About', href='/home'),
                    ),
                    rx.menu_item('post')
                )
            ),

            justify_content = 'flex-start',
            align_items='center'
        ),
        bg="#000000",
        position="fixed",
        z_index="1",
        left="0px",
        width="100%", 
    )



def custom_component(image_name, url):
    return rx.box(
        rx.link(
            rx.box(
                rx.image(src=f"/{image_name}", height="auto", width="auto", max_height="100%", max_width="100%"),  # Adjusting the anonymous CSS Box model properties
                on_hover=rx.text("Hover Text"),
                border_radius="10px",
                height="150px",
                width="350px",
                border_color="neonblue",
                border_width="3px", 
                border_style="solid",
                style={
                    "display": "flex",
                    "justify_content": "center",
                    "align_items": "center",
                },  # Using CSS Flexbox for center alignment and maintaining aspect ratio
            ),
            href=url
        ),
        height="150px",
        width="350px",
        border_radius="10px",
        bg="#1D1D38",

    )
#     url: str


class State(rx.State):
    sidebar_open: bool = False

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

def sidebar():
    return rx.box(
        rx.menu(rx.vstack(
            rx.spacer(heigh='5px'), 
            rx.menu_button("Live",background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                background_clip="text",
                font_weight="bold",
                font_size="1em",), 
    
            rx.spacer(height='15px'),
            rx.menu_button("Playback", color='white',background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                background_clip="text",
                font_weight="bold",
                font_size="1em", ),
            rx.spacer(height='15px'),
            rx.menu_button("Teams",background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                background_clip="text",
                font_weight="bold",
                font_size="1em",  ),
            rx.spacer(height='15px'),
            rx.menu_button("Players",background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                background_clip="text",
                font_weight="bold",
                font_size="1em",), 
            rx.spacer(height='15px'),
            rx.menu_button("Tournamnets",background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                background_clip="text",
                font_weight="bold",
                font_size="1em",)
            
            
            )),



        background_color="#000000",
        position="fixed",
        left="0px",
        top="60px",
        height="calc(100% - 70px)",
        z_index="5",
        width=rx.cond(State.sidebar_open, "250px", "100px"),
        transition="width 0.5s",
        border_color="#1D1D38",
        border_width="3px", 
        border_style="solid",
    )

def button():
    return rx.button(
        ">>>",
        on_click=State.toggle_sidebar,
        position="absolute",
        left="-850px",
        top="500px",
        z_index="6",
        width=rx.cond(State.sidebar_open, "250px", "50px"),

        transition="width 0.5s"

    )
    
def sidebar_with_button():
    return rx.box(
        sidebar(),
        button(),
        position="relative"
    )


class Spline(rx.Component):
    """Spline component."""
    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: rx.Var[str] ="https://prod.spline.design/SC7zzZaANZ6KzAeU/scene.splinecode"
    is_default = True
    lib_dependencies: list[str] = ["@splinetool/runtime"]

spline = Spline.create()

def NavAndSide():
    return rx.container(
        rx.stack(navbar()),  sidebar_with_button(), 
        rx.spacer(height='120px'), 
    
    )
# url='url'
  # rx.flex(
        #             rx.responsive_grid(
        #                 custom_component("favicon.ico", "http://localhost:3000/video/"),
        #                 custom_component("favicon.ico", "http://localhost:3000/video/"),
        #                 custom_component("favicon.ico", "http://localhost:3000/video/"),
        #                 custom_component("favicon.ico", "http://localhost:3000/video/"),
        #                 custom_component("favicon.ico", "http://localhost:3000/video/"),
        #                 custom_component("favicon.ico", "http://localhost:3000/video/"),
        #                 custom_component("favicon.ico", "http://localhost:3000/video/"),

        #                 columns=[3],
        #                 spacing_x="370",
        #                 spacing_y="30"
        #                                 ),
        #   justify="center",
        #     width="120%"
        #         )