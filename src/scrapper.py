def get_cars_from_sources(local, valor):
    carros = [
        { "site": "Webmotors"     , "modelo": "Honda Civic 2018"   , "preco": 70000, "local": "Pato Branco"       },
        { "site": "SóCarrão"      , "modelo": "Toyota Corolla 2017", "preco": 68000, "local": "Francisco Beltrão" },
        { "site": "FB Marketplace", "modelo": "Fiat Argo 2020"     , "preco": 72000, "local": "Pato Branco"       },
        { "site": "Webmotors"     , "modelo": "VW Gol 2016"        , "preco": 45000, "local": "Vitorino"          },
        { "site": "SóCarrão"      , "modelo": "Chevrolet Onix 2019", "preco": 69000, "local": "Pato Branco"       },
    ]

    valor_max = int(valor)
    filtrados = [c for c in carros if c["preco"] <= valor_max and local.lower() in c["local"].lower()]

    if not filtrados:
        return [{"erro": "Nenhum carro encontrado com esses critérios."}]
    return filtrados