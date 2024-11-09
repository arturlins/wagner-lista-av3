from os import system
from config.db import start_connection

def search_games():
    system('cls')
    conn = start_connection()
    cursor = conn.cursor()
    search = input("Digite a palavra que você quer pesquisar: ")
    sql = f"SELECT titulo, subtitulo FROM jogos WHERE titulo ILIKE '%{search}%' OR subtitulo ILIKE '%{search}%'"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:    
        print(f"Resultados encontrados em '{search}': ")
        for row in result:
            titulo, subtitulo = row
            print(f"Título: {titulo}: {subtitulo}")
    else:
        system('cls')
        print(f"Nenhum jogo encontrado em '{search}'")
        
def list_games():
    system('cls')
    conn = start_connection()
    cursor = conn.cursor()
    sql = "SELECT titulo, subtitulo FROM jogos ORDER BY titulo;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Lista de todos os jogos em ordem alfabética: ")
    for row in result:
       titulo, subtitulo = row
       print(f"Título: {titulo}")

def search_k_games():
    system('cls')
    conn = start_connection()
    cursor = conn.cursor()
    sql = f"SELECT titulo, subtitulo FROM jogos WHERE titulo ILIKE '%k%' OR subtitulo ILIKE '%k%'"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:    
        print(f"Resultados encontrados em 'k': ")
        for row in result:
            titulo, subtitulo = row
            print(f"Título: {titulo}: {subtitulo}")
    else:
        print(f"Nenhum jogo encontrado em 'k'")