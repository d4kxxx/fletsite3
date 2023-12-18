from pytube import YouTube
import flet as ft
from time import sleep
import os





def main(page:ft.Page):
    #page.bgcolor="white"
    page.horizontal_alignment= "center"
    #page.theme_mode = ft.ThemeMode.LIGHT

    
    def video_download(e):
        down_progress.value ="Your File is Downloading Please Wait....."
        page.update()
        yt = YouTube(url.value)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        yt.download("~/Downloads")
        url.value =""
        down_progress.value =""   
        page.snack_bar.open = True
        page.update()
    def audio_download(e):
        down_progress.value ="Your File is Downloading Please Wait....."
        page.update()
        yt = YouTube(url.value)
        yt= yt.streams.filter(only_audio=True).first()
        out=yt.download("~/Downloads")
        base, ext = os.path.splitext(out) 
        new_file = base + '.mp3'
        os.rename(out, new_file) 
        url.value =""
        down_progress.value =""   
        page.snack_bar.open = True
        page.update()
    down_progress = ft.Text("")
    y_icon = ft.IconButton(icon=ft.icons.VIDEOCAM)
    f_icon = ft.IconButton(icon=ft.icons.FACEBOOK)
    t_icon = ft.IconButton(icon=ft.icons.TIKTOK)
    #title = ft.Text("Download YouTube Video & Audio", font_family="lucida", size=18, color="black", opacity=0.5)
    logo = ft.Container(content=ft.Image(src="logo2.png", width=600, height=200, fit=ft.ImageFit.CONTAIN))
    url = ft.TextField(label="Type The Video URL Here",width=800, border_color="orange")
    btn1 = ft.FloatingActionButton(icon=ft.icons.VIDEO_LIBRARY, text="Download Video", on_click=video_download)
    btn2 = ft.FloatingActionButton(icon=ft.icons.AUDIOTRACK, text="Download Audio", on_click=audio_download)
    page.snack_bar = ft.SnackBar(ft.Text(f"Download Finished, Your File Is Ready", size=18, color="black", text_align=ft.TextAlign.CENTER), bgcolor=ft.colors.SECONDARY)
    space_text= ft.Text()
    row1 = ft.Row(controls=[logo], alignment=ft.MainAxisAlignment.CENTER)
    row2 = ft.Row(controls=[url], alignment=ft.MainAxisAlignment.CENTER)
    row3 = ft.Row(controls=[btn1, btn2], alignment=ft.MainAxisAlignment.CENTER)
    row4 = ft.Row(controls=[down_progress], alignment=ft.MainAxisAlignment.CENTER)
    row5 = ft.Row(controls=[y_icon, f_icon, t_icon ], alignment=ft.MainAxisAlignment.CENTER)
    pb = ft.ProgressBar(width=400)
    
    page.add(row1, space_text,row5, row2,space_text, row3, space_text, row4)





ft.app(target=main, view= ft.WEB_BROWSER)

