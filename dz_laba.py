import wikipedia
from fastapi import FastAPI
from pydantic import BaseModel
from wikipedia import*

class SearchInput(BaseModel):
    spisok: list

class States(BaseModel):
    name: str

class Heading(BaseModel):
    heading: str

app = FastAPI(title="Grach")

@app.get("/search_all_headings/{request}", response_model = SearchInput)
def search_headings(request: str):
    wikipedia.set_lang("ru")
    return SearchInput(spisok=wikipedia.search(request))

@app.get("/search_with_count/", response_model = States)
def search_specific_article(request: str, sentences_number: str):
    wikipedia.set_lang("ru")
    return States(name=wikipedia.summary(request, sentences = sentences_number))

@app.post("/search_full_page", response_model = Heading)
def search_content(search_input: Heading):
    wikipedia.set_lang("ru")
    return Heading(heading=wikipedia.page(search_input.heading).content)