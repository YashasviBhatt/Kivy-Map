from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

class QuestionApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        screen = Screen()
        layout = Builder.load_file('question.kv')
        screen.add_widget(layout)
        return screen


class Map(Screen):
    pass


if __name__ == '__main__':
    sm = ScreenManager()
    sm.add_widget(Map(name='Map'))
    QuestionApp().run()