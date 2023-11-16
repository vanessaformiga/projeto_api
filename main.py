from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def inicializando_projeto():
    return "Inicializando a Biblioteca de Livros"

@app.get("/livros")
def listar_livros():
    
    listar_livros = {
    "livros": [
        {
            "id": "01",
            "titulo": "Orgulho e Preconceito",
            "autor": "Jane Austen"
        },
        {
            "id": "02",
            "titulo": "Boa Noite",
            "autor": "Pan Gonçalves"
        }
    ]
    }
    return {"listar_livros":listar_livros}

@app.get("/livro/id/01")
def exibindo_livros():
          return {
          "livros": [
          {
          "id": "01",
          "titulo": "Orgulho e Preconceito",
          "autor": "jane Austen"
                              
          }
          ]

          }

@app.get("/livro/id/02")
def exibindo_livros():
          return {
          "livros": [
                    {
                    
                    "id": "02",
                    "titulo": "Boa Noite",
                    "autor": "Pan Gonçalves"
                    
                    }
          ]

           }


class LivroCreateRequest:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

