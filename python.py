import flet as ft
def login(user,password,page,footer):
    if user.value=="" or password.value=="":
        user.border_color='red'
        password.border_color='red'
        footer.value="error"
    elif user.value=="admin" and password.value=="admin":
        user.border_color=None
        password.border_color=None
        user.value=""
        password.value=""
        footer.value="login succesfull"
    else:

        user.value=""
        password.value=""
        footer.value="login failed"
        user.border_color='red'
        password.border_color='red'
        
    page.update()
    
    
def main(page:ft.Page):
    page.window_bgcolor='white'
    page.bgcolor='grey'
    page.horizontal_alignment='center'
    text=ft.Text(value="Login",size=30)
    user=ft.TextField(label="Enter your name")
    password=ft.TextField(label="Enetr password")
    dev=" devloped by izza kanwal"
    footer=ft.Text(value=dev)
    button=  ft.ElevatedButton(text="login",on_click=lambda _:login(user,password,page,footer))
    page.add(text,user,password,button,footer)
    
ft.app(target=main)