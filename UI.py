import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet import ControlEvent

def main(page: ft.Page) -> None:
    page.title = 'SignIn'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT  # Fixed typo
    page.window_width = 400
    page.window_height = 600
    page.window_resizable = False

    # Setup UI Elements for login
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
        
        # Clear the login screen
        page.clean()
        
        # Create inventory items list
        items_list = Column(spacing=10)
        
        # Input fields for adding items
        item_name_field = TextField(label='Item Name:', width=250)
        item_quantity_field = TextField(label='Quantity:', width=250, keyboard_type=ft.KeyboardType.NUMBER)
        
        def add_item(e: ControlEvent) -> None:
            if item_name_field.value and item_quantity_field.value:
                # Create a new item row
                new_item = Row(
                    controls=[
                        Text(f"{item_name_field.value} - Qty: {item_quantity_field.value}", size=16),
                        ElevatedButton(
                            text="Remove",
                            on_click=lambda e: remove_item(new_item),
                            bgcolor=ft.Colors.RED_400,
                            color=ft.Colors.WHITE
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
                items_list.controls.append(new_item)
                
                # Clear the input fields
                item_name_field.value = ""
                item_quantity_field.value = ""
                page.update()
        
        def remove_item(item_row):
            items_list.controls.remove(item_row)
            page.update()
        
        add_button = ElevatedButton(
            text='Add Item',
            width=250,
            on_click=add_item
        )
        
        # Create the inventory UI
        inv_title = Text(
            "Inventory",
            size=30,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.LEFT,
        )
        
        welcome_text = Text(
            value=f'Welcome: {text_username.value}!',
            size=20,
            weight=ft.FontWeight.W_500
        )
        
        main_container = ft.Container(
            content=Column(
                [
                    welcome_text,
                    ft.Divider(height=20),
                    inv_title,
                    ft.Divider(),
                    item_name_field,
                    item_quantity_field,
                    add_button,
                    ft.Divider(height=20),
                    Text("Your Items:", size=18, weight=ft.FontWeight.BOLD),
                    items_list,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                scroll=ft.ScrollMode.AUTO
            ),
            expand=True,
            padding=20,
            border_radius=10,
            bgcolor=ft.Colors.TRANSPARENT,
            width=350
        )
        
        page.add(main_container)
        page.update()

    text_username.on_change = validate
    button_submit.on_click = submit

    # Render login UI Elements
    page.add(
        Row(
            controls=[
                Column(
                    [text_username, button_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

if __name__ == '__main__':
    ft.app(target=main)

#GPT made the remove and add item functionalities. Did just about everything else.