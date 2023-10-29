# fire_incidents
# README - Cargar CSV a BigQuery con Apache Airflow

Este repositorio contiene un DAG de Apache Airflow que carga un archivo CSV desde Google Cloud Storage a BigQuery. Fue la manera más rápida y simple que se me ocurrió abordar el problema, y que se alineara con mi conocimiento previo. Por ello es que fue configurado bajo ciertos supuestos.

## Supuestos

- Considerando que los archivos CSV se actualizan diariamente, sería ideal que queden cargados en Google Cloud Storage.
- Los parámetros del archivo siguen siempre la misma estructura.

## Requisitos

- Apache Airflow configurado y en funcionamiento.
- Conexiones configuradas para Google Cloud Storage y BigQuery en Apache Airflow.

## Uso

1. Asegurar la configuración de Apache Airflow.

2. Personalizar el archivo `gcs_to_bigquery.py` con los detalles de su proyecto, como el nombre del bucket en Google Cloud Storage y la ubicación en BigQuery.

3. Colocar el archivo en la carpeta `dags` de tu instalación de Apache Airflow.

4. Ejecutar el DAG desde la interfaz de Apache Airflow o programa su ejecución según sea necesario.

## Particionamiento por Fecha (Pendiente)

- El DAG utilizaría `execution_date` de Apache Airflow como campo de partición en BigQuery, lo que crea una partición por cada ejecución del DAG, ayudando a optimizar el acceso a los datos en Bigquery.
