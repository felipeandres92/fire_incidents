import airflow
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime

# DAG
with airflow.DAG(
    'csv_to_bigquery',
    schedule_interval="5 4 * * *",
    start_date=datetime(2023, 10, 27),
    catchup=False,
) as dag:
    # GSC to BQ Operator
    load_csv = GCSToBigQueryOperator(
    task_id="gcs_to_bigquery",
    bucket='fperez-b5a2d04a-2b62-4189-93d3-4d306fae211b',
    source_objects=['Fire_Incidents_20231026.csv'], #probar borrar gs
    destination_project_dataset_table='mythic-chalice-403320.fire_incidents.fire_incidents_data',
    schema_fields=[{'name': 'Incident_Number', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'Exposure_Number', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'ID', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'Address', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Incident_Date', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Call_Number', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'Alarm_DtTm', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Arrival_DtTm', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Close_DtTm', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'City', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'zipcode', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Battalion', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Station_Area', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Box', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Suppression_Units', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'Suppression_Personnel', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'EMS_Units', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'EMS_Personnel', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'Other_Units', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'Other_Personnel', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'First_Unit_On_Scene', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Estimated_Property_Loss', 'type':'FLOAT', 'mode': 'NULLABLE'},{'name': 'Estimated_Contents_Loss', 'type':'FLOAT', 'mode': 'NULLABLE'},{'name': 'Fire_Fatalities', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'Fire_Injuries', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'Civilian_Fatalities', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'Civilian_Injuries', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'Number_of_Alarms', 'type':'INTEGER', 'mode': 'NULLABLE'},{'name': 'Primary_Situation', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Mutual_Aid', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Action_Taken_Primary', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Action_Taken_Secondary', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Action_Taken_Other', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Detector_Alerted_Occupants', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Property_Use', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Area_of_Fire_Origin', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Ignition_Cause', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Ignition_Factor_Primary', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Ignition_Factor_Secondary', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Heat_Source', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Item_First_Ignited', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Human_Factors_Associated_Ignition', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Structure_Type', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Structure_Status', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Floor_of_Fire_Origin', 'type':'FLOAT', 'mode': 'NULLABLE'},{'name': 'Fire_Spread', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'No_Flame_Spead', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'N_floors_minimum_damage', 'type':'FLOAT', 'mode': 'NULLABLE'},{'name': 'N_floors_significant_damage', 'type':'FLOAT', 'mode': 'NULLABLE'},{'name': 'N_floors_heavy_damage', 'type':'FLOAT', 'mode': 'NULLABLE'},{'name': 'N_floors_extreme_damage', 'type':'FLOAT', 'mode': 'NULLABLE'},{'name': 'Detectors_Present', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Detector_Type', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Detector_Operation', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Detector_Effectiveness', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Detector_Failure_Reason', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'AES_Present', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'AES_Type', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'AES_Perfomance', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'AES_Failure_Reason', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'Number_of_Sprinkler_Heads_Operating', 'type':'FLOAT', 'mode': 'NULLABLE'},{'name': 'Supervisor_District', 'type':'FLOAT', 'mode': 'NULLABLE'},{'name': 'neighborhood_district', 'type':'STRING', 'mode': 'NULLABLE'},{'name': 'poINTEGER', 'type':'STRING', 'mode': 'NULLABLE'}],
    write_disposition="WRITE_TRUNCATE",
)

load_csv



