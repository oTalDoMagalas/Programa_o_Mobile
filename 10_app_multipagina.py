import flet as ft

def main(page: ft.Page):
    page.title = "App Multi-página"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO

    pagina_atual = "home"

    dados_usuario = {
        "nome": "Estudante Flet",
        "nivel": "Iniciante",
        "pontos": 150,
        "configuracoes": {
            "modo_escuro": False,
            "notificacoes": True,
            "som": True
        }
    }

    def mudar_pagina(nova_pagina):
        nonlocal pagina_atual
        pagina_atual = nova_pagina

        # Esconder todas as páginas
        conteudo_home.visible = False
        conteudo_perfil.visible = False
        conteudo_config.visible = False
        conteudo_sobre.visible = False

        # Mostrar a página selecionada
        if pagina_atual == "home":
            conteudo_home.visible = True
        elif pagina_atual == "perfil":
            conteudo_perfil.visible = True
        elif pagina_atual == "config":
            conteudo_config.visible = True
        elif pagina_atual == "sobre":
            conteudo_sobre.visible = True

        atualizar_barra_navegacao()
        page.update()

    def ir_home(e): mudar_pagina("home")
    def ir_perfil(e): mudar_pagina("perfil")
    def ir_config(e): mudar_pagina("config")
    def ir_sobre(e): mudar_pagina("sobre")

    cabecalho = ft.Container(
        content=ft.Text(
            "Meu App",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE
        ),
        bgcolor=ft.Colors.BLUE,
        padding=ft.padding.only(top=20, bottom=20),
        alignment=ft.alignment.center
    )

    def criar_item_navegacao(icone, label, pagina_nome, on_click_func):
        return ft.GestureDetector(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(icone, size=24, color=ft.Colors.GREY),
                        ft.Text(label, size=10, text_align=ft.TextAlign.CENTER, color=ft.Colors.GREY)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=4
                ),
                padding=ft.padding.symmetric(vertical=8, horizontal=16),
                border_radius=12,
                bgcolor=ft.Colors.TRANSPARENT,
                animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT)
            ),
            on_tap=on_click_func
        )

    item_home = criar_item_navegacao(ft.Icons.HOME, "Início", "home", ir_home)
    item_perfil = criar_item_navegacao(ft.Icons.PERSON, "Perfil", "perfil", ir_perfil)
    item_config = criar_item_navegacao(ft.Icons.SETTINGS, "Config", "config", ir_config)
    item_sobre = criar_item_navegacao(ft.Icons.INFO, "Sobre", "sobre", ir_sobre)

    def atualizar_barra_navegacao():
        itens = [
            (item_home, "home"),
            (item_perfil, "perfil"),
            (item_config, "config"),
            (item_sobre, "sobre")
        ]

        for item, pagina_nome in itens:
            container = item.content
            icone = container.content.controls[0]
            texto = container.content.controls[1]

            if pagina_atual == pagina_nome:
                container.bgcolor = ft.Colors.BLUE_50
                container.border = ft.border.all(2, ft.Colors.BLUE_200)
                icone.color = ft.Colors.BLUE
                texto.color = ft.Colors.BLUE
                texto.weight = ft.FontWeight.BOLD
            else:
                container.bgcolor = ft.Colors.TRANSPARENT
                container.border = None
                icone.color = ft.Colors.GREY
                texto.color = ft.Colors.GREY
                texto.weight = ft.FontWeight.NORMAL

    # Conteúdos das páginas
    conteudo_home = ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(ft.Icons.HOME, size=80, color=ft.Colors.BLUE),
                ft.Text("Bem-vindo ao App! 🎉", size=28, weight=ft.FontWeight.BOLD),
                ft.Text("Navegue pelas páginas usando a barra inferior", size=16, text_align=ft.TextAlign.CENTER),
                ft.Container(height=20),
                ft.Text("🎯 Toque nos ícones da barra para navegar!", size=14, color=ft.Colors.BLUE_600)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        padding=40,
        visible=True
    )

    def adicionar_pontos(e):
        dados_usuario["pontos"] += 10
        texto_pontos.value = f"Pontos: {dados_usuario['pontos']} ⭐"
        page.update()

    texto_pontos = ft.Text(f"Pontos: {dados_usuario['pontos']} ⭐", size=16)

    conteudo_perfil = ft.Container(
        content=ft.Column(
            controls=[
                ft.CircleAvatar(
                    content=ft.Icon(ft.Icons.PERSON, size=50, color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.BLUE,
                    radius=60
                ),
                ft.Text(dados_usuario["nome"], size=24, weight=ft.FontWeight.BOLD),
                ft.Text(f"Nível: {dados_usuario['nivel']}", size=16, color=ft.Colors.BLUE_600),
                texto_pontos,
                ft.Container(height=20),
                ft.ElevatedButton(
                    "Ganhar Pontos! 🎯",
                    on_click=adicionar_pontos,
                    bgcolor=ft.Colors.GREEN,
                    color=ft.Colors.WHITE
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        padding=40,
        visible=False
    )

    def alternar_modo_escuro(e):
        dados_usuario["configuracoes"]["modo_escuro"] = e.control.value

    def alternar_notificacoes(e):
        dados_usuario["configuracoes"]["notificacoes"] = e.control.value

    def alternar_som(e):
        dados_usuario["configuracoes"]["som"] = e.control.value

    conteudo_config = ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(ft.Icons.SETTINGS, size=60, color=ft.Colors.BLUE),
                ft.Text("Configurações ⚙️", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(height=20),
                ft.Switch(
                    label="Modo escuro",
                    value=dados_usuario["configuracoes"]["modo_escuro"],
                    on_change=alternar_modo_escuro
                ),
                ft.Switch(
                    label="Notificações",
                    value=dados_usuario["configuracoes"]["notificacoes"],
                    on_change=alternar_notificacoes
                ),
                ft.Container(height=30)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        padding=40,
        visible=False
    )

    conteudo_sobre = ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(ft.Icons.INFO, size=60, color=ft.Colors.BLUE),
                ft.Text("Sobre o App ℹ️", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(height=20),
                ft.Text("Versão: 1.0.0", size=16),
                ft.Text("Desenvolvido com Flet", size=16),
                ft.Text("Python + Interface Mobile", size=16),
                ft.Container(height=20),
                ft.Text(
                    "Este app demonstra navegação entre páginas, "
                    "gerenciamento de estado e interface completa!",
                    size=14,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.GREY_600
                ),
                ft.Container(height=30)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        padding=40,
        visible=False
    )

    # Container principal com stack para páginas
    conteudo_principal = ft.Container(
        content=ft.Column(
            controls=[
                cabecalho,
                ft.Container(
                    content=ft.Stack(
                        controls=[
                            conteudo_home,
                            conteudo_perfil,
                            conteudo_config,
                            conteudo_sobre
                        ]
                    ),
                    expand=True,
                    padding=ft.padding.only(bottom=90)
                )
            ],
            spacing=0
        ),
        expand=True
    )

    # Barra de navegação inferior
    barra_navegacao_inferior = ft.Container(
        content=ft.Row(
            controls=[item_home, item_perfil, item_config, item_sobre],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor=ft.Colors.WHITE,
        padding=ft.padding.only(top=12, bottom=20),
        border=ft.border.only(top=ft.border.BorderSide(1, ft.Colors.GREY_300)),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=10,
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
            offset=ft.Offset(0, -2)
        ),
        height=80
    )

    # Adiciona tudo na página
    page.add(
        ft.Column(
            controls=[
                conteudo_principal,
                barra_navegacao_inferior
            ],
            spacing=0,
            expand=True
        )
    )

    # Atualiza a barra para refletir o estado inicial
    atualizar_barra_navegacao()

ft.app(target=main)
