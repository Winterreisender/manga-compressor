import shutil
import os
import flet as ft


def compress_folder(input_dir,output_dir):
    assert(os.path.exists(input_dir))
    for filename in os.listdir(input_dir):
        print(filename)
    

def main(page: ft.Page):
    page.title = "Manga"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()

    # State
    pictures = []

    # Images
    images = ft.Row(expand=1, wrap=True, scroll="always")
    page.add(images)

    # File Picker
    def update_pictures(v):
        pictures = v
        for picture in pictures:
            images.controls.append(
                ft.Column([
                ft.Image(
                    src=picture.path,
                    width=200,
                    height=150,
                    fit=ft.ImageFit.NONE,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Text(f'{round(picture.size/1024,1)} KB'),
                ft.Text(picture.name)
                ])
            )
        page.update()
    file_picker = ft.FilePicker(on_result=lambda e: update_pictures(e.files))
    page.overlay.append(ft.FilePicker(ref=file_picker))
    page.add(file_picker)

    # Pick File Button
    def on_pick_clicked(e):
        file_picker.pick_files(allow_multiple=True)
    page.add(
        ft.ElevatedButton("添加图片",on_click=on_pick_clicked)
    )

    page.update()
    return

    images = ft.Row(expand=1, wrap=False, scroll="always")

    for picture in []:
        images.controls.append(
            ft.Image(
                src=picture.path,
                width=200,
                height=150,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    
    page.add(images)
    page.update()


if __name__ == '__main__':
    print("hello")
    ft.app(target=main)
