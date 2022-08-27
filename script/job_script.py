import requests
import pandas as pd

# Created this function to help get the content from a website. If you are going to reuse a block of code maybe you should make it a function

url = "https://countrycode.org/"


def get_url(url):
    response = requests.get(url).content
    return response


site_url = get_url(url)
table = pd.read_html(site_url)

table_df = pd.DataFrame(table[-2])


def country_head(df):
    return df.head()


def country_tail(df):
    return df.tail()


def country_sample(df):
    return df.sample(5)


print(country_tail(table_df))
print(country_head(table_df))
print(country_sample(table_df))
