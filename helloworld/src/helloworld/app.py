"""
My first application
"""

import asyncio
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "Your name: ",
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.photo = toga.ImageView(style=Pack(height=300, padding=5))
        camera_button = toga.Button(
            "Take photo", 
            on_press=self.take_photo, 
            style=Pack(padding=5)
        )

        main_box.add(self.photo)
        main_box.add(camera_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def say_hello(self, widget, **kwargs):
        await asyncio.sleep(5)
        self.main_window.info_dialog(
            greeting(self.name_input.value),
            "Hi there!"
        )

    async def take_photo(self, widget, **kwargs):
        try:
            if not self.camera.has_permission:
                await self.camera.request_permission()

            image = await self.camera.take_photo()
            if image:
                self.photo.image = image
        except NotImplementedError:
            await self.main_window.info_dialog(
                "Oh no!",
                "The Camera API is not implemented on this platform",
            )
        except PermissionError:
            await self.main_window.info_dialog(
                "Oh no!",
                "You have not granted permission to take photos",
            )


def greeting(name):
    return f"Hello, {name or 'stranger'}"


def main():
    return HelloWorld()
