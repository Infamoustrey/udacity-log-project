#!/usr/bin/env python3


import psycopg2

most_popular_articles = """
    select
        '"' || title || '"',
        (select count(id)
            from log
            where log.path
            like '%' || articles.slug || '%'
        ) as views
    from articles
    order by views desc
    limit 3
"""

most_popular_authors = """
    select
        name,
        (select count(log.id)
        from articles, log
        where log.path like '%' || articles.slug || '%') as views
    from authors
    order by views desc
    limit 3
"""

days_errors_above_one_percent = """
    select
        time::date,
        round(
            count(case when status <> '200 OK' then 1 end)::decimal
            /
            count(id) * 100
            , 1
        )
    from log
    group by time::date
    having round(
        count(case when status <> '200 OK' then 1 end)::decimal
        /
        count(id) * 100
        , 1
        ) >= 1
"""


def connect():
    # Attempt DB Connection
    return psycopg2.connect("dbname=news")


def query_db(query):
    # Execute Query and return results
    cur = connect().cursor()
    cur.execute(query)
    return cur.fetchall()


def print_results(results):
    for row in results:
        print(' - '.join(map(str, row)))


# Print Most Popular Articles
print("Most Popular Articles: ")
print_results(query_db(most_popular_articles))

print('\n')

# Print Most Popular Authors
print("Most Popular Authors: ")
print_results(query_db(most_popular_authors))

print('\n')

# Print Days Where Errors Exceeded 1%
print("Days where errors exceeded 1% of requests: ")
print_results(query_db(days_errors_above_one_percent))
