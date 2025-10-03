import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet import ControlEvent

def main(page: ft.Page) -> None:
    page.title = 'SignIn'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.them_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    #Setup UI Elements
    text_username: TextField = TextField(label='Email:', text_align=ft.TextAlign.LEFT, width=300)
    button_submit: ElevatedButton = ElevatedButton(text='Sign in', width=100, disabled=True)

    def validate(e: ControlEvent) -> None:
        if all([text_username.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True

        page.update()

    def submit(e: ControlEvent) -> None:
        print('Username:', text_username.value)

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Welcome: {text_username.value}!', size=20)],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )



   
    text_username.on_change = validate
    button_submit.on_click = submit

    #render UI Elements
    page.add(
        Row(
            controls=[
                Column(
                    [text_username,
                    button_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

if __name__ == '__main__':
    ft.app(target=main)
        