import json

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import os
import time

URL = 'https://api.cyberconnect.dev/l2/'

class GqlClient:
    def __init__(self, auth_token, url=URL):

        if not auth_token:
            raise ValueError("Authorization token not found.")

        self.url = url
        self.headers = {
            "accept-encoding": "gzip, deflate, br, zstd",
            "origin": "https://cyber.co",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://cyber.co",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            'Content-Type': 'application/json',
            "authorization": auth_token
        }
        self.transport = RequestsHTTPTransport(url=self.url, headers=self.headers, use_json=True)
        self.client = Client(transport=self.transport, fetch_schema_from_transport=False)

    def sendGqlRequest(self, query_str, variables):
        query = gql(query_str)

        return self.client.execute(query, variables)

if __name__ == "__main__":
    # GraphQL endpoint
    # Instantiate the GraphQLClient
    auth_token_arr = ["YOUR_AUTH_TOKEN"]

    for auth_token in auth_token_arr:
        gql_client = GqlClient(auth_token)
        query_str = """
            mutation checkedIn {
              checkIn {
                status
              }
            }
            """
        variables = {}

        data = gql_client.sendGqlRequest(query_str, variables)
        print(json.dumps(data, indent=4))
        time.sleep(5)
