import matplotlib.pyplot as plt

def plot_pie_internet(df):
    # Pie chart de tenencia de internet
    df['FAMI_TIENEINTERNET'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#66b3ff', '#ff6666'])
    plt.title('Distribución de estudiantes según tenencia de internet')
    plt.ylabel('')
    plt.show()

def plot_boxplot_gender(df):
    # Boxplot de PUNT_GLOBAL por Género
    plt.figure(figsize=(8, 6))
    df.boxplot(column='PUNT_GLOBAL', by='ESTU_GENERO', patch_artist=True,
               boxprops=dict(facecolor='skyblue', color='blue'))
    plt.title('Distribución de Puntajes Globales por Género')
    plt.suptitle('')
    plt.xlabel('Género')
    plt.ylabel('Puntaje Global')
    plt.show()

def plot_bar_gender(df):
    # Gráfico de barras del promedio de PUNT_GLOBAL por género
    avg_by_gender = df.groupby('ESTU_GENERO')['PUNT_GLOBAL'].mean()
    avg_by_gender.plot(kind='bar', color='skyblue', edgecolor='blue')
    plt.title('Promedio de Puntajes Globales por Género')
    plt.xlabel('Género')
    plt.ylabel('Promedio de Puntaje Global')
    plt.xticks(rotation=0)
    plt.show()

def plot_bar_computer(df):
    # Gráfico de barras de estudiantes con computador
    df['FAMI_TIENECOMPUTADOR'].value_counts().plot(kind='bar', color=['#66b3ff', '#ff6666'])
    plt.title('Distribución de estudiantes con computador')
    plt.xlabel('Tiene computador')
    plt.ylabel('Cantidad de estudiantes')
    plt.xticks(rotation=0)
    plt.show()

def plot_bar_school_type(df):
    # Gráfico de barras del promedio de puntajes por tipo de colegio
    avg_by_school = df.groupby('COLE_NATURALEZA')['PUNT_GLOBAL'].mean()
    avg_by_school.plot(kind='bar', color='lightgreen', edgecolor='green')
    plt.title('Promedio de Puntajes Globales por Tipo de Colegio')
    plt.xlabel('Tipo de Colegio')
    plt.ylabel('Promedio de Puntaje Global')
    plt.xticks(rotation=0)
    plt.show()

def plot_pie_low_strata(df):
    # Gráfico de torta mostrando la distribución de estudiantes en estratos bajos
    low_strata = df['FAMI_ESTRATOVIVIENDA'].isin([1, 2]).sum()
    total = len(df)
    plt.pie([low_strata, total - low_strata], labels=['Estrato Bajo', 'Otros'], autopct='%1.1f%%', 
            colors=['#66b3ff', '#ff6666'])
    plt.title('Distribución de estudiantes en estratos bajos')
    plt.show()
