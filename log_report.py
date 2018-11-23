#!/usr/bin/env python3


import psycopg2

most_popular_articles = """
    select
        '"' || title || '"',
        count(log.id) as views
    from articles
    join log on log.path like '%' || articles.slug
    where log.status = '200 OK'
    group by title
    order by views desc
    limit 3
"""

most_popular_authors = """
    select
        name,
        count(log.id) as views
    from authors
    join articles on articles.author = authors.id
    join log on log.path like '%' || articles.slug
    group by name
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
        ) AS percentage
    from log
    group by time::date
    having percentage >= 1
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

# # Print Most Popular Authors
print("Most Popular Authors: ")
print_results(query_db(most_popular_authors))

print('\n')

# # # Print Days Where Errors Exceeded 1%
print("Days where errors exceeded 1% of requests: ")
print_results(query_db(days_errors_above_one_percent))
