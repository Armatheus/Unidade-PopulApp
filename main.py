from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 0
        MDCard:
            id:espaco_texto
            elevation: 0
            md_bg_color: 0,0.5,0,0
            
            MDTextField:
                id: data
                hint_text: 'Cole a mensagem'
                icon_left: 'hammer-sickle'
                
                helper_text: "Verifique se há '#' ou emojis em seu texto!"
                helper_text_mode: "on_error"

                pos_hint: {'center_x':.5, 'center_y':.5}
                size_hint_x: .5
                size_hint_y: 1
                mode: "fill"
                width: 250
                multiline: True
                
        MDCard:
            id:espaco_botao
            size_hint_y: .15

            elevation: 0
            md_bg_color: 0,0,1,0

            MDBoxLayout:
                pos_hint: {'center_y':.5}
                padding: 15
                spacing: 10

                MDRectangleFlatIconButton:
                    icon: 'content-copy'
                    text: 'Copiar fórmula'
                    pos_hint: {'center_y':.5}
                    on_press: app.get_data() 
'''


class App(MDApp):
    Window.size = (300,600)

    def build(self):
        self.novoTexto = False
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)
    
    def get_data(self):
        texto = self.root.ids.data.text
        print(texto.split())
        if limparMensagem(texto) == False:
            self.root.ids.data.error = True
        else:
            self.novoTexto = criarMensagem(texto)
            self.copy()
    
    def copy(self):
        print(self.novoTexto)
        try: Clipboard.copy(self.novoTexto)
        except: self.root.ids.data.error = True

def limparMensagem(texto):
    for x in texto:
        if x == '#': return False
    else: return True

def criarMensagem(texto):
    str = ''
    ciclo = False
    for x in texto.split():
        if ciclo: str = str+f'+{x}'
        else:     
            str = f"{x}"
            ciclo = True
    print(str)
    novo = "=CONCATENAR(\"https://wa.me/+\";REGEXREPLACE(TO_TEXT(A3);\"[+\(\)\- ]\";\"\");\"?text="+str+"\")"
    return novo

App().run()