def main():
    movies = {}

    movies["Super Mario Bros. O Filme"] = {"villan": "Bowser", "age": 2023}
    movies["Star Wars Episode IV"] = {"villan": "Darth Vader", "age": 1977}
    movies["Harry Potter e a Pedra Filosofal"] = {"villan": "Lord Voldemort", "age": 2001}
    movies["Dragon Ball Super: Broly"] = {"villan": "Broly", "age": 2019}
    movies["Batman: O Cavaleiro das Trevas"] = {"villan": "Coringa", "age": 2008}

    for movie, info in movies.items():
        print(f"Filme: {movie}")
        print(f"Vilão: {info['villan']}")
        print(f"Ano de Lançamento: {info['age']}\n")

main()
