# MSRIT SIS API

This is a barebones api made to scrape the sis portal and fetch the data for a particular user.

The intention behind this project was to enable people to make their own rendition of the sis either as an app or webpage.

## Set up

The api is not deployed yet; thus to use it as is, we need to host the api locally.

`uvicorn api:app --reload` where api is the main python file. and app is the FastApi object.

this makes it so that any changes is reported by the system listening on the port deployed by the server. <br>
The base url might be of the type `http://127.0.0.1:8000/` where the port is 8000.

## docs

### fetch SIS portal details  `GET`

url: `baseURL/sis/`

Query Parameters:<br>
1. usn `Required` - type `str` 
2. dd `Required` - type `str`
3. mm `Required` - type `str`
4. yyyy `Required` - type `str`

> example url : <br>
`http://127.0.0.1:8000/sis?usn="1MS23CIXXX"&dd="0"&mm="0"&yyyy="2000"`

> One can also access the auto generated docs by FastApi at `http://127.0.0.1:8000/docs`

#### Response
```json
{
    "usn": "1MS23CIXXX",
    "section": "SEC A",
    "photo": "https://parents.msrit.edu/newparents/images/comprofiler/<STUDENT_SPECIFIC_URL>",
    "name": "John Doe",
    "sem": "SEM 0X",
    "lastUpdated": "19/11/2024",
    "courseData": [
        {
            "<courseCode>": [
                "<CourseName>",
                "<Attendance>"
            ]
        }
    ]
}
```

## Important
> A proper version of chromeDriver is needed to run the headless selenium browser instance. <br>
> It can be downloaded from [chromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) <br>
> Place it in the root folder

## modules used

1. [FastApi](https://pypi.org/project/fastapi/)
2. [uvicorn](https://pypi.org/project/uvicorn/)
3. [selenium](https://pypi.org/project/selenium/)
4. [pydantic](https://pypi.org/project/pydantic/)