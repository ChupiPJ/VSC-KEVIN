import pandas as pd
from data_analysis import data_analysis
from visualizations import plot_pie_internet, plot_boxplot_gender, plot_bar_gender, plot_bar_computer, plot_bar_school_type, plot_pie_low_strata
from data_loader import cargar_datos

def mostrar_menu():
    print("\n===== Menú de Análisis de Datos =====")
    print("1. Cargar y mostrar los primeros registros")
    print("2. Realizar análisis de la Generación E")
    print("3. Mostrar estadísticas descriptivas de PUNT_GLOBAL")
    print("4. Mostrar gráficos de barras")
    print("5. Salir")

def main():
    # Cargar los datos
    df = cargar_datos('bdd_choco.xlsx')
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            print("\nPrimeras filas del DataFrame cargado:")
            print(df.head())  # Muestra las primeras filas
        elif opcion == '2':
            print("\nRealizando análisis para la Generación E...")
            data_analysis(df)  # Llama a la función de análisis de datos
        elif opcion == '3':
            print("\nMostrando estadísticas descriptivas de PUNT_GLOBAL...")
            stats = df['PUNT_GLOBAL'].describe()
            print(stats)  # Muestra estadísticas descriptivas
        elif opcion == '4':
            print("\nGenerando gráficos de barras...")
            plot_pie_internet(df)  # Pie chart de tenencia de internet
            plot_boxplot_gender(df)  # Boxplot de género
            plot_bar_gender(df)  # Gráfico de barras por género
            plot_bar_computer(df)  # Gráfico de barras de estudiantes con computador
            plot_bar_school_type(df)  # Gráfico de barras por tipo de colegio
            plot_pie_low_strata(df)  # Gráfico de torta de estratos bajos
        elif opcion == '5':
            print("¡Hasta luego!")
            break  # Sale del ciclo y termina el programa
        else:
            print("\nOpción no válida. Por favor, elige una opción del menú.")

if __name__ == '__main__':
    main()
