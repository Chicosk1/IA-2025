from api           import get_user_input
from scrapper      import get_cars_from_sources
from prompt_engine import analyze_cars
from formatter     import format_output

def main():
    local, valor = get_user_input()
    cars = get_cars_from_sources(local, valor)

    if "erro" in cars[0]:
        print(cars[0]["erro"])
        return

    recomendacao = analyze_cars(cars)
    format_output(cars, recomendacao)

if __name__ == "__main__":
    main()