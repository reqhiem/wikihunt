from db.connection import get_postgresql_connection


def search_engine(query):
    connection = get_postgresql_connection()
    cur = connection.cursor()

    query = f"""
            SELECT DISTINCT
                t.id,
                t.clean_title,
                t.url,
                h.hash,
                t.pr_score
            FROM
                (
                    SELECT
                        SPLIT_PART(unnest(hashes), ':', 1) AS hash
                    FROM
                        iindex
                    WHERE
                        word LIKE '%{query}%'
                ) AS h
            JOIN
                hashes_urls_titles AS t
            ON
                h.hash = t.hash
            ORDER BY
                t.pr_score DESC;
        """
    cur.execute(query)
    results = cur.fetchall()

    # contrunt a list of dictionaries with the results with values: id, title, url, hash
    results = [
        {
            "id": result[0],
            "title": result[1],
            "url": result[2],
            "hash": result[3],
        }
        for result in results
    ]

    cur.close()
    connection.close()

    return results
