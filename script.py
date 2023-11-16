from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Classe Pydantic para modelar os dados do livro
class Livro(BaseModel):
    id: str
    titulo: str
    autor: str

# Lista de livros de exemplo (inicialmente contém um livro)
livros = [
    
    {
        "id": "01",
        "titulo": "Orgulho e Preconceito",
        "autor": "Jane Austen"
    }, 
    {
        "id": "02",
        "titulo": "Boa Noite",
        "autor": "Pan Gonçalves"
    },

    {
        "id": "03",
        "titulo": "1984",
        "autor": "George Orwell"
    }, 

    {
        "id": "04",
        "titulo": "O diário de anne frank",
        "autor": "Anne Frank"
    }, 

    {
        "id": "05",
        "titulo": "Como eu era antes de você",
        "autor": "Jojo Moyes"
    }

]

# Endpoint principal da página
@app.get("/")
def exibir_livros():
    return {"Welcome a Api of Books"}

# Endpoint para exibir a lista de livros (método GET)
@app.get("/livros")
def exibir_livros():
    return {"Listando os livros"}

# Endpoint para exibir a lista de livros (método GET)
@app.get("/livro/")
def exibir_livros():
    return {"livros": livros}

# Endpoint para exibir um item por vez da lista de livros de acordo com o id informado
@app.get('/livro/id/{item_id}')
def get_item(item_id: str):
    # Procura o item com base no item_id
    item = next((livro for livro in livros if livro["id"] == item_id), None)

    if item:
          return item
    else:
         return {'message': 'Livro não encontrado'}, 404
    
# Endpoint para criar um novo livro (método POST)
@app.post("/livro/")
def criar_livro(livro: Livro):
    ids = [int(livro["id"]) for livro in livros]
    novo_id = str(max(ids) + 1) if ids else "01"
    novo_livro = Livro(id=novo_id, titulo=livro.titulo, autor=livro.autor)
    livros.append(novo_livro.dict())
    return novo_livro

#Endpoint para atuaizar o id

@app.put('/livro/id/{item_id}')
def put_item(item_id: str, new_id: str):
    livro_encontrado = None
    for index, livro_item in enumerate(livros):
        if livro_item["id"] == item_id:
            livro_encontrado = livro_item
            livro_encontrado["id"] = new_id # update the book's ID
            break
    if livro_encontrado:
        return {'message': 'ID do livro atualizado'}
    else:
         raise HTTPException(status_code=404, detail='Livro não encontrado')
    

#Endpoint para deleta um item da lista de acordo com o id
@app.delete('/livro/id/{item_id}')
def deletar_item(item_id: str):
    livro_encontrado = None
    for livro in livros:
        if livro["id"] == item_id:
            livro_encontrado = livro
            break

    if livro_encontrado:
        livros.remove(livro_encontrado)
        return {'message': 'Livro excluído'}
    else:
        return {'message': 'Livro não encontrado'}, 404
    