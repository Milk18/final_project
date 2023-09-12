import requests

def test():
    try:
        response = requests.get("http://localhost:9000")
        assert response.status_code == 200
    except:
        assert 1 == 2
