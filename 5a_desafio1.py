#  5a Desafio Digitação (Aqui)📚  ⚽ 🎵  🎮 👨‍🍳 🎨 ⚠️ ✨ 🧹 👤 
import flet as ft

def main(page: ft.Page):
    page.title = "Criador de Perfil"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20) # Padding superior para área segura
    page.scroll = ft.ScrollMode.AUTO

    # campos do formulário
    campo_nome = ft.TextField(label="Nome completo", width=300)
    campo_idade = ft.TextField(label="Idade", width=300, keyboard_type=ft.KeyboardType.NUMBER)

    dropdown_hobby = ft.Dropdown(
        label="Hobby favorito",
        width=300,
        options=[
            ft.dropdown.Option("Leitura 📚"),
            ft.dropdown.Option("Esportes ⚽"),
            ft.dropdown.Option("Música 🎵"),
            ft.dropdown.Option("Jogos 🎮"),
            ft.dropdown.Option("Culinária 🧑‍🍳"),
            ft.dropdown.Option("Arte 🎨")
        ]
    )

    # Área do perfil criado (inicialmente oculta)
    cartao_perfil = ft.Container(
        content=ft.Text("Preencha os dados acima"),
        bgcolor=ft.Colors.GREY_100,
        padding=30,
        border_radius=15,
        width=350,
        visible=False
    )

    def criar_perfil(evento):
        """
        Valida dados e cria o perfil visual
        """
        # Validações
        if not campo_nome.value or len(campo_nome.value) < 2:
            mostrar_erro("Nome deve ter pelo menos 2 caracteres")
            return

        if not campo_idade.value:
            mostrar_erro("Idade é obrigatória")
            return

        try:
            idade = int(campo_idade.value)
            if idade < 1 or idade > 120:
                mostrar_erro("Idade deve estar entre 1 e 120 anos")
                return
        except ValueError:
            mostrar_erro("Idade deve ser um número")
            return

        if not dropdown_hobby.value:
            mostrar_erro("Selecione um hobby")
            return

        # Criando o perfil visual
        criar_cartao_perfil()

    def mostrar_erro(mensagem):
        """
        Mostra mensagem de erro
        """
        cartao_perfil.content = ft.Column([
            ft.Icon(ft.Icons.ERROR, color=ft.Colors.RED, size=40),
            ft.Text(f"⚠️ {mensagem}", color=ft.Colors.RED, text_align=ft.TextAlign.CENTER)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        cartao_perfil.bgcolor = ft.Colors.RED_50
        cartao_perfil.visible = True
        page.update()

    def criar_cartao_perfil():
        """
        Cria o cartão visual do perfil
        """
        # Definindo categoria de Idade
        idade = int(campo_idade.value)
        if idade < 18:
            categoria = "Jovem"
            cor_icone = ft.Colors.GREEN
        elif idade < 60:
            categoria = "Adulto"
            cor_icone = ft.Colors.BLUE
        else:
            categoria = "Experiente"
            cor_icone = ft.Colors.PURPLE

        cartao_perfil.content = ft.Column([
            ft.Icon(ft.Icons.PERSON, size=60, color=cor_icone),
            ft.Text(f"{campo_nome.value}", weight=ft.FontWeight.BOLD),
            ft.Text(f"{idade} anos - ({categoria})", size=14, color=ft.Colors.GREY_600),
            ft.Text(f"Hobby: {dropdown_hobby.value}", size=14),
            ft.Container(
                content=ft.Text("Perfil criado! ✨", color=ft.Colors.WHITE),
                bgcolor=cor_icone,
                padding=10,
                border_radius=20
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)

        cartao_perfil.bgcolor = ft.Colors.WHITE
        cartao_perfil.visible = True
        page.update()

    def limpar_campos(evento):
        """
        Limpa todos os campos
        """
        campo_nome.value = ""
        campo_idade.value = ""
        dropdown_hobby.value = None
        cartao_perfil.visible = False
        page.update()

    # Botões
    linha_botoes = ft.Row([
        ft.ElevatedButton(
            "✨ Criar Perfil",
            on_click=criar_perfil,
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
            width=140
        ),
        ft.ElevatedButton(
            "🧹 Limpar",
            on_click=limpar_campos,
            bgcolor=ft.Colors.GREY,
            color=ft.Colors.WHITE,
            width=140
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER, spacing=20
    )

    # Layout principal
    layout_principal = ft.Column([
        ft.Text("Criador de Perfil", size=26, weight=ft.FontWeight.BOLD),
        ft.Text("Preencha seus dados para criar seu perfil personalizado!", size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
        ft.Container(height=20),
        campo_nome,
        campo_idade,
        dropdown_hobby,
        linha_botoes,
        ft.Container(height=20),
        cartao_perfil
    ],
    horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15
    )

    page.add(layout_principal)

ft.app(target=main)


