from google.cloud import bigquery


def run_query():
    # Construct a BigQuery client object.
    # client = bigquery.Client("inspiring-bee-398116")
    client = bigquery.Client.from_service_account_json('sa_key.json')

    # client
    table = client.get_table("inspiring-bee-398116.testing_dataset.Ger_table")

    query = """
        INSERT testing_dataset.Ger_table VALUES(ART99,20019,11,2023-09-19,200)
    """
    rows_to_insert = [("ART99", 20019, 11, "2023-09-19", 200)]

    query_job = client.insert_rows(table, rows_to_insert)

    # query_job = client.query(query)  # Make an API request.
    # query_job.begin()

    # print("The query data:")
    # for row in query_job:
    #     # Row values can be accessed by field name or index.
    #     print("name={}, count={}".format(row[0], row["total_people"]))


# from google.cloud import bigquery
# client = bigquery.Client(project='PROJECT_ID')
# query = "SELECT...."
# dataset = client.dataset('dataset')
# table = dataset.table(name='table')
# job = client.run_async_query('my-job', query)
# job.destination = table
# job.write_disposition= 'WRITE_TRUNCATE'
# job.begin()

if __name__ == "__main__":
    run_query()
