# POST Request
import requests
 
url = "https://api.jobthai.com/v1/graphql"

body = """
mutation {

  searchJobs(filter: $searchJobsFilter, orderBy: $orderBy) {
    data {
      total
      data {
        id
        companyID
        jobTitle
        companyName
        companyLogo
        province {
          id
          name
        }
        district {
          id
          name
        }
        industrial {
          id
          name
        }
        disabledPerson {
          id
          name
        }
        country {
          id
          name
        }
        transitStations {
          id
          distance
          type
          name
        }
        isTopCompany
        workLocation
        salary
        urgent {
          id
          name
        }
        jobType {
          id
          name
        }
        province {
          id
          name
        }
        region {
          id
          name
        }
        tags
        updatedAt
      }
    }
  }
  
}
"""
 
response = requests.post(url=url, json={"query": body})
print("response status code: ", response.status_code)
if response.status_code == 200:
    print("response : ",response.content)