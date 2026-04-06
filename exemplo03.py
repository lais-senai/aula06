import flet as ft

def main(page: ft.Page):
    page.acroll = ft.ScrollMode.AUTO
    
    page.add(
        ft.Image(
            src="images/paisagem.png",
            width=200,
            height=200,
            border_radius=10,
        ),
    
        ft.Container(
            content=ft.Text("Paisagem", color=ft.Colors.WHITE, size=32),
            image=ft.DecorationImage(
            src="images/paisagem.png",
            fit=ft.BoxFit.COVER
        ),
        bgcolor=ft.Colors.BLUE,
        width=300,
        height=600,
        alignment=ft.Alignment(0,0),
    )
)
    

        
ft.run(main)