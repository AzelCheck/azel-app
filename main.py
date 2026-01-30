from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0, 0, 0, 1)  # خلفية سوداء


def luhn_check(number):
    digits = [int(d) for d in number if d.isdigit()][::-1]
    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def card_type(number):
    if number.startswith("4"):
        return "Visa"
    if number[:2].isdigit() and 51 <= int(number[:2]) <= 55:
        return "MasterCard"
    if number[:4].isdigit() and 2221 <= int(number[:4]) <= 2720:
        return "MasterCard"
    return "Unknown"


class AzelUI(BoxLayout):
    def check(self, instance):
        num = self.input.text.replace(" ", "")
        if not num.isdigit():
            self.result.text = "[color=ff0000]رقم غير صالح[/color]"
            return

        ctype = card_type(num)
        luhn = luhn_check(num)
        length_ok = (len(num) in [13, 16, 19])

        if ctype != "Unknown" and luhn and length_ok:
            self.result.text = (
                f"[color=00ffcc]✔ صالح تقنيًا[/color]\n"
                f"Type: {ctype}"
            )
        else:
            self.result.text = (
                f"[color=ff3333]✖ غير صالح[/color]\n"
                f"Type: {ctype}"
            )


class AzelApp(App):
    def build(self):
        layout = AzelUI(orientation="vertical", padding=20, spacing=20)

        title = Label(
            text="[b][color=00ffcc]Azel Card Checker[/color][/b]",
            markup=True,
            font_size=32,
            size_hint=(1, 0.2)
        )

        layout.input = TextInput(
            hint_text="أدخل رقم البطاقة",
            font_size=22,
            foreground_color=(0, 1, 1, 1),
            background_color=(0, 0, 0, 1),
            multiline=False
        )

        btn = Button(
            text="CHECK",
            font_size=24,
            background_color=(0, 1, 0.8, 1),
            color=(0, 0, 0, 1)
        )
        btn.bind(on_press=layout.check)

        layout.result = Label(
            text="",
            markup=True,
            font_size=20
        )

        layout.add_widget(title)
        layout.add_widget(layout.input)
        layout.add_widget(btn)
        layout.add_widget(layout.result)

        return layout


if __name__ == "__main__":
    AzelApp().run()
      
