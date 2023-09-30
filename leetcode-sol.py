import leetcode
import time
from collections import Counter

topic_to_accepted = Counter()
topic_to_total = Counter()
leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzc4MTAwNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjQ1MzUxODJiZmFmYTBlZjIwZmIzNzEzMWFiY2QzZjZiNjYyNmZhZjgiLCJpZCI6Mzc4MTAwNSwiZW1haWwiOiJvbWthci5rYXZpdGthcjk2QGdtYWlsLmNvbSIsInVzZXJuYW1lIjoidXNlcjE0NTFaIiwidXNlcl9zbHVnIjoidXNlcjE0NTFaIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL3VzZXIxNDUxWi9hdmF0YXJfMTYxMDQwOTA5Ni5wbmciLCJyZWZyZXNoZWRfYXQiOjE2OTYwNDI4NzUsImlwIjoiMjYwMzozMDI0OjE1MTg6YzcwMDo2Y2MyOmRiYzk6ZGI4NzphMmIxIiwiaWRlbnRpdHkiOiJkZjlmOWE4NDc0OTEyYWU2YWY5NjcxYzA1N2Q0ZjVmYSIsInNlc3Npb25faWQiOjQ3MDAzNDMwfQ.ugmyLXRV8jNcvQyP1F8Jnwp-tO5a5hwbm-6DwXvS6PA"
csrf_token = "xZczbejhRzye7FwuY20pUiUAuaHXpUurTnfiK27fuGWpsNzUkNNePaEyVvOE3LgJ"
configuration = leetcode.Configuration()
configuration.api_key["x-csrftoken"] = csrf_token
configuration.api_key["csrftoken"] = csrf_token
configuration.api_key["LEETCODE_SESSION"] = leetcode_session
configuration.api_key["Referer"] = "https://leetcode.com"
configuration.debug = False

api_instance =leetcode.DefaultApi(leetcode.ApiClient(configuration))
graphql_request = leetcode.GraphqlQuery(
query="""
     {
       question {
            questionId
            
            
         }
     }
     """,
variables=leetcode.GraphqlQueryVariables(),
)
print(api_instance.graphql_post(body=graphql_request))
api_response = api_instance.api_problems_topic_get(topic="algorithms")
api_response = api_instance.api_problems_topic_get(topic="algorithms")

slug_to_solved_status = {
    pair.stat.question__title_slug: True if pair.status == "ac" else False
    for pair in api_response.stat_status_pairs
}

#print(slug_to_solved_status)