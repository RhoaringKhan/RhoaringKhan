import reflex as rx
from .components.navbar import *
import os
''''
every page needs to have a def NAME(): function in order to be a callable

Prop > properties, added to components

''' 



style = {
 "background_color": "darkgrey"
}

def index():
    return rx.container(
        navbar(),
        
    )

def about():

    return  rx.vstack(
        rx.box(
            rx.container( NavAndSide(),
            rx.flex(
                    rx.responsive_grid(
                        custom_component("soccer1.png", "http://localhost:3000/video/"),
                        custom_component("soccer2.jpg", "http://localhost:3000/video/"),
                        custom_component("soccer3.jpg", "http://localhost:3000/video/"),
                        custom_component("soccer4.jpg", "http://localhost:3000/video/"),

                        custom_component("soccer1.png", "http://localhost:3000/video/"),
                        custom_component("soccer2.jpg", "http://localhost:3000/video/"),
                        custom_component("soccer3.jpg", "http://localhost:3000/video/"),
                        custom_component("soccer4.jpg", "http://localhost:3000/video/"),

                        custom_component("soccer1.png", "http://localhost:3000/video/"),
                        custom_component("soccer2.jpg", "http://localhost:3000/video/"),
                        custom_component("soccer3.jpg", "http://localhost:3000/video/"),
                        custom_component("soccer4.jpg", "http://localhost:3000/video/"),

                        custom_component("soccer1.png", "http://localhost:3000/video/"),
                        custom_component("soccer2.jpg", "http://localhost:3000/video/"),
                        custom_component("soccer3.jpg", "http://localhost:3000/video/"),
                        custom_component("soccer4.jpg", "http://localhost:3000/video/"),

                        custom_component("soccer1.png", "http://localhost:3000/video/"),
                        custom_component("soccer2.jpg", "http://localhost:3000/video/"),
                        custom_component("soccer3.jpg", "http://localhost:3000/video/"),
                        custom_component("soccer4.jpg", "http://localhost:3000/video/"),


                        columns=[4],
                        spacing_x="370",
                        spacing_y="30",
                                        ),
          justify="center",
            width="120%",

                ) ),
            style={
                "position": "fixed",
                "width": "100%",
                "top": "0px",
                "z_index": "5",
            }
        ),
        rx.box(
            Spline(),
            style={
                "position": "fixed",
                "width": "100%",
                "height": "100%",
                "z_index": "1",
            },
        ),
    )





'''
you must also add the page with the add_page(NAME)
'''
@rx.page(route="/video")
def video_page():
    return rx.vstack(
        rx.box(
                    rx.container( NavAndSide(),
                    rx.flex(
                                    rx.video(
                                    url="/video.mp4",
                                    controls=True,
                                            ),
                            justify="center",
                                width="120%",
                                )),
            style={
                "position": "fixed",
                "width": "100%",
                "top": "0px",
                "z_index": "5",
            }
        ),
        rx.box(
            Spline(),
            style={
                "position": "fixed",
                "width": "100%",
                "height": "100%",
                "z_index": "1",
            },
        ),
    )
    

app = rx.App(style=style)

app.add_page(about, route='/home')
app.add_page(video_page, route="/video")
app.compile()