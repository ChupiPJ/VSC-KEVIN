import matplotlib.pyplot as plt

def filter_generation_e(df):
    return df[
        (df['ESTU_GENERACION-E'] == 'GENERACION E - GRATUIDAD') &
        (df['COLE_NATURALEZA'].isin(['OFICIAL', 'MIXTO'])) &
        (df['EDAD'] < 18)
    ]

def calculate_statistics(df, column):
    return df[column].describe()

def plot_pie_internet(ax, df):
    df['FAMI_TIENEINTERNET'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#66b3ff', '#ff6666'], ax=ax)
    ax.set_title('Distribución de estudiantes según tenencia de internet')
    ax.set_ylabel('')

def plot_boxplot_gender(ax, df):
    df.boxplot(column='PUNT_GLOBAL', by='ESTU_GENERO', patch_artist=True, 
               boxprops=dict(facecolor='skyblue', color='blue'), ax=ax)
    ax.set_title('Distribución de Puntajes Globales por Género')
    ax.set_xlabel('Género')
    ax.set_ylabel('Puntaje Global')

def plot_bar_gender(ax, df):
    avg_by_gender = df.groupby('ESTU_GENERO')['PUNT_GLOBAL'].mean()
    avg_by_gender.plot(kind='bar', color='skyblue', edgecolor='blue', ax=ax)
    ax.set_title('Promedio de Puntajes Globales por Género')
    ax.set_xlabel('Género')
    ax.set_ylabel('Promedio de Puntaje Global')

def plot_bar_computer(ax, df):
    df['FAMI_TIENECOMPUTADOR'].value_counts().plot(kind='bar', color=['#66b3ff', '#ff6666'], ax=ax)
    ax.set_title('Distribución de estudiantes con computador')
    ax.set_xlabel('Tiene computador')
    ax.set_ylabel('Cantidad de estudiantes')

def plot_bar_school_type(ax, df):
    avg_by_school = df.groupby('COLE_NATURALEZA')['PUNT_GLOBAL'].mean()
    avg_by_school.plot(kind='bar', color='lightgreen', edgecolor='green', ax=ax)
    ax.set_title('Promedio de Puntajes Globales por Tipo de Colegio')
    ax.set_xlabel('Tipo de Colegio')
    ax.set_ylabel('Promedio de Puntaje Global')

def plot_pie_low_strata(ax, df):
    low_strata = df['FAMI_ESTRATOVIVIENDA'].isin([1, 2]).sum()
    total = len(df)
    ax.pie([low_strata, total - low_strata], labels=['Estrato Bajo', 'Otros'], autopct='%1.1f%%', 
            colors=['#66b3ff', '#ff6666'])
    ax.set_title('Distribución de estudiantes en estratos bajos')

def data_analysis(df):
    # Crear una figura con subgráficos
    fig, axs = plt.subplots(3, 2, figsize=(15, 12))  # 3 filas, 2 columnas de gráficos

    filtered_df = filter_generation_e(df)
    print('Estudiantes filtrados:')
    print(filtered_df)

    # Llamar a las funciones de visualización y pasarles los ejes correspondientes
    plot_pie_internet(axs[0, 0], filtered_df)
    plot_boxplot_gender(axs[0, 1], df)
    plot_bar_gender(axs[1, 0], df)
    plot_bar_computer(axs[1, 1], df)
    plot_bar_school_type(axs[2, 0], df)
    plot_pie_low_strata(axs[2, 1], df)

    # Ajustar los espacios entre los subgráficos
    plt.tight_layout()
    plt.show()