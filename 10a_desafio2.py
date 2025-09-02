import flet as ft

def main(page: ft.Page):
    page.title = "Gerador de Senhas"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO

    # Elementos da interface
    tamanho_senha = ft.TextField(
        label="Tamanho da senha",
        value="12",
        width=200,
        keyboard_type=ft.KeyboardType.NUMBER,
        text_align=ft.TextAlign.CENTER
    )

    incluir_maiusculas = ft.Checkbox(label="Incluir maiúsculas", value=True)
    incluir_minusculas = ft.Checkbox(label="Incluir minúsculas", value=True)
    incluir_numeros = ft.Checkbox(label="Incluir números", value=True)
    incluir_simbolos = ft.Checkbox(label="Incluir símbolos", value=True)

    senha_gerada = ft.TextField(
        label="Senha gerada",
        read_only=True,
        width=300,
        text_align=ft.TextAlign.CENTER,
        multiline=True,
        min_lines=2,
        max_lines=2,
        bgcolor=ft.Colors.WHITE  # 🔥 Fundo branco
    )

    def gerar_senha(e):
        import random
        import string

        comprimento = int(tamanho_senha.value)
        caracteres = ""
        if incluir_maiusculas.value: caracteres += string.ascii_uppercase
        if incluir_minusculas.value: caracteres += string.ascii_lowercase
        if incluir_numeros.value: caracteres += string.digits
        if incluir_simbolos.value: caracteres += string.punctuation

        if not caracteres:
            senha_gerada.value = "Selecione pelo menos uma opção!"
            senha_gerada.color = ft.Colors.RED
            page.update()
            return

        if comprimento <= 0:
            senha_gerada.value = "Tamanho inválido!"
            senha_gerada.color = ft.Colors.RED
            page.update()
            return

        senha = ''.join(random.choice(caracteres) for i in range(comprimento))
        senha_gerada.value = senha
        senha_gerada.color = ft.Colors.BLACK
        page.update()

    def copiar_senha(e):
        page.set_clipboard(senha_gerada.value)
        page.show_snack_bar(
            ft.SnackBar(ft.Text("Senha copiada para a área de transferência!"), open=True)
        )

    # Botões
    botao_gerar = ft.ElevatedButton(
        "Gerar Senha",
        on_click=gerar_senha,
        icon=ft.Icons.REFRESH,
        bgcolor=ft.Colors.BLUE_400,
        color=ft.Colors.WHITE,
        width=200
    )

    botao_copiar = ft.ElevatedButton(
        "Copiar Senha",
        on_click=copiar_senha,
        icon=ft.Icons.COPY,
        bgcolor=ft.Colors.GREY_400,
        color=ft.Colors.WHITE,
        width=200
    )

    # Layout principal
    layout_principal = ft.Column(
        [
            ft.Text("🔐 Gerador de Senhas", size=26, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Crie senhas fortes e seguras!",
                size=14,
                color=ft.Colors.GREY_600,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Container(height=20),
            tamanho_senha,
            ft.Text("Opções:", size=16, weight=ft.FontWeight.BOLD),
            incluir_maiusculas,
            incluir_minusculas,
            incluir_numeros,
            incluir_simbolos,
            ft.Row(
                [botao_gerar, botao_copiar],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            ft.Container(height=20),
            senha_gerada
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    page.add(layout_principal)

ft.app(target=main)
