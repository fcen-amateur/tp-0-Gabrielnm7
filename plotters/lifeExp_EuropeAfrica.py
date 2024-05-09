import seaborn.objects as so
from gapminder import gapminder


def plot():
    datos_europa_africa = gapminder[(gapminder["continent"]=="Europe") 
                                    | (gapminder["continent"]=="Africa")]
    figura = (
        so.Plot(
            datos_europa_africa, 
            x = "lifeExp",
            color="continent"
        )
        .add(so.Bar()
             ,so.Hist())
        .label(
            title="Esperanza de vida en Europa y Africa",
            x="Esperanza de vida",
            color="Continente",
        )
    )
    return dict(
        descripcion="Histograma de la esperanza de vida en Europa y Africa",
        autor="Gabriel Nuñez Moreno",
        figura=figura,
    )
