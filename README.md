<h1 style="text-align: center;">✨ easyhttp ✨</h1> 

<span style="text-align: center;">

 ![GitHub last commit](https://img.shields.io/github/last-commit/luisbrandino/easyhttp?style=flat-square)
 ![GitHub top language](https://img.shields.io/github/languages/top/luisbrandino/easyhttp?style=flat-square) ![GitHub](https://img.shields.io/github/license/luisbrandino/easyhttp?style=flat-square)

easyhttp is a simple HTTP server made for study purposes.

</span>

## 🚀 Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install easyhttp.

Simply run:

```bash
pip install easyhttp
```

## 💻 Quickstart

```python
import easyhttp

app = easyhttp.App()

def index(req, res):
    res.send('<h1>It\'s working!</h1>')

app.get('/', index)

app.listen(3000)
```

You can also use other HTTP methods:

```python
app.get('/', index_get)
app.post('/', index_post)
app.put('/', index_put)
app.delete('/', index_delete)
```

Specifying a public folder can be done as shown below:

```python
app.public('/public')
```

## 📜 License

[MIT](https://choosealicense.com/licenses/mit/)