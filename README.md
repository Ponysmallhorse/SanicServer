Server that uses Sanic web server to run.

To run server, install dependencies from **_requirements.txt_**, and run command **"python -m server"** from project root folder.

Application has two endpoints:

- POST /auth - to authenticate users. Return jwt token that user must append to request as Bearer Token in order to access protected endpoints
- POST(protected) /normalize - Returns normalized json object from json objects list: [{"name": "n1", "strVal": "v1"}, {"name": "n2", "anyVal": "v2}] returns {"n1": "v1", "n2", "v2"}
