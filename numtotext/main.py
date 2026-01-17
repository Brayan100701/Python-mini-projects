import flet as ft
import utilidades

def main(page: ft.Page):
    def update_text(lbl_value, lbl_color):
        lbl_text.value = lbl_value
        lbl_text.color = lbl_color
        page.update()

    def convert(*_):
        if utilidades.validate(txt_number.value):
            update_text(translator.translate(str(txt_number.value)), 'White')
        else:
            update_text('La entrada no cumple con ser un numero entre 0 y 999999','Red')

    translator = utilidades.Translator()

    page.window.width = 400
    page.window.height = 280
    page.title = 'Traductor numero a texto'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    lbl_number = ft.Text(value='Ingresa el numero')
    txt_number = ft.TextField(value='0', width=150)
    btn_translate = ft.Button(text='Traducir a Texto', on_click=convert)
    lbl_text = ft.Text(value='')

    page.add(
        ft.Column(
            controls=[
                lbl_number,
                txt_number,
                btn_translate,
                lbl_text
            ]
        )
    )

    page.update()


if __name__ == '__main__':
    ft.app(main)
