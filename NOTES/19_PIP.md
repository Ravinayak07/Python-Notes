# PIP:

- package Manager for modules and packages of python
- It is included by default from python version 3.4

> What is a Package?

- Contains all files that are needed for a module
- Modules are python code libraries that are included in project

> check pip is installed or not

- open cmd
- Navigate to the directory where python scripts are there
- Run the command:

```
C:\Users\ASUS\AppData\Local\Programs\Python\Python310\Scripts>pip --version
```

> Install PIP:

- Download and Install from [here](https://pypi.org/project/pip/)

> Steps to download a package:

- Lets download a package named "camelcase":
- open cmd
- Navigate to the directory where python scripts are there
- Run the command:

```
C:\Users\ASUS\AppData\Local\Programs\Python\Python310\Scripts>pip install camelcase
```

- Package Downloaded
- Now to use it in project, we need to import it

```py
import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))

#This method capitalizes the first letter of each word.

```

```
Lorem Ipsum Dolor Sit Amet
```

- For more packages, visit [here](https://pypi.org/)

> Uninstall Packages:

- Lets uninstall camelcase:

```
C:\Users\ASUS\AppData\Local\Programs\Python\Python310\Scripts>pip uninstall camelcase
```

> List Packages:

- To list all packages installed on your system:

```
C:\Users\ASUS\AppData\Local\Programs\Python\Python311\Scripts>pip list
```

```
Package                       Version
----------------------------- ---------
absl-py                       1.4.0
anyio                         3.6.2
argon2-cffi                   21.3.0
argon2-cffi-bindings          21.2.0
arrow                         1.2.3
asttokens                     2.2.1
astunparse                    1.6.3
async-generator               1.10
attrs                         22.2.0
backcall                      0.2.0
beautifulsoup4                4.11.2
bleach                        6.0.0
cachetools                    5.3.0
certifi                       2022.12.7
cffi                          1.15.1
charset-normalizer            3.1.0
click                         8.1.3
colorama                      0.4.6
comm                          0.1.2
contourpy                     1.0.7
cycler                        0.11.0
debugpy                       1.6.6
decorator                     5.1.1
defusedxml                    0.7.1
dm-tree                       0.1.8
editdistance                  0.6.2
exceptiongroup                1.1.1
executing                     1.2.0
fastjsonschema                2.16.3
Flask                         2.2.3
flatbuffers                   23.3.3
fonttools                     4.39.0
fqdn                          1.5.1
gast                          0.4.0
google-auth                   2.16.2
google-auth-oauthlib          0.4.6
google-pasta                  0.2.0
grpcio                        1.51.3
h11                           0.14.0
h5py                          3.8.0
idna                          3.4
imutils                       0.5.4
ipykernel                     6.21.3
ipython                       8.11.0
ipython-genutils              0.2.0
ipywidgets                    8.0.4
isoduration                   20.11.0
itsdangerous                  2.1.2
jax                           0.4.6
jedi                          0.18.2
Jinja2                        3.1.2
joblib                        1.2.0
jsonpointer                   2.3
jsonschema                    4.17.3
jupyter                       1.0.0
jupyter_client                8.0.3
jupyter-console               6.6.3
jupyter_core                  5.2.0
jupyter-events                0.6.3
jupyter_server                2.4.0
jupyter_server_terminals      0.4.4
jupyterlab-pygments           0.2.2
jupyterlab-widgets            3.0.5
keras                         2.12.0rc1
kiwisolver                    1.4.4
libclang                      15.0.6.1
lmdb                          1.4.1
Markdown                      3.4.1
MarkupSafe                    2.1.2
matplotlib                    3.7.1
matplotlib-inline             0.1.6
mistune                       2.0.5
nbclassic                     0.5.3
nbclient                      0.7.2
nbconvert                     7.2.10
nbformat                      5.7.3
nest-asyncio                  1.5.6
notebook                      6.5.3
notebook_shim                 0.2.2
numpy                         1.23.5
oauthlib                      3.2.2
opencv-python                 4.7.0.72
opt-einsum                    3.3.0
outcome                       1.2.0
packaging                     23.0
pandas                        1.5.3
pandocfilters                 1.5.0
parso                         0.8.3
path                          16.6.0
pickleshare                   0.7.5
Pillow                        9.4.0
pip                           23.1.2
platformdirs                  3.1.1
prometheus-client             0.16.0
prompt-toolkit                3.0.38
protobuf                      4.22.1
psutil                        5.9.4
pure-eval                     0.2.2
pyasn1                        0.4.8
pyasn1-modules                0.2.8
pycparser                     2.21
Pygments                      2.14.0
pyparsing                     3.0.9
pyrsistent                    0.19.3
PySocks                       1.7.1
python-dateutil               2.8.2
python-json-logger            2.0.7
pytz                          2022.7.1
pywin32                       305
pywinpty                      2.0.10
PyYAML                        6.0
pyzmq                         25.0.1
qtconsole                     5.4.1
QtPy                          2.3.0
requests                      2.28.2
requests-oauthlib             1.3.1
rfc3339-validator             0.1.4
rfc3986-validator             0.1.1
rsa                           4.9
scikit-learn                  1.2.2
scipy                         1.10.1
seaborn                       0.12.2
selenium                      4.8.3
Send2Trash                    1.8.0
setuptools                    65.5.0
six                           1.16.0
sniffio                       1.3.0
sortedcontainers              2.4.0
soupsieve                     2.4
stack-data                    0.6.2
tensorboard                   2.12.0
tensorboard-data-server       0.7.0
tensorboard-plugin-wit        1.8.1
tensorflow                    2.12.0rc1
tensorflow-estimator          2.12.0rc0
tensorflow-intel              2.12.0rc1
tensorflow-io-gcs-filesystem  0.31.0
tensorflow-model-optimization 0.7.3
termcolor                     2.2.0
terminado                     0.17.1
threadpoolctl                 3.1.0
tinycss2                      1.2.1
tornado                       6.2
traitlets                     5.9.0
trio                          0.22.0
trio-websocket                0.10.2
TwoCaptcha                    0.0.1
typing_extensions             4.5.0
uri-template                  1.2.0
urllib3                       1.26.15
wcwidth                       0.2.6
webcolors                     1.12
webencodings                  0.5.1
websocket-client              1.5.1
Werkzeug                      2.2.3
wheel                         0.40.0
widgetsnbextension            4.0.5
wrapt                         1.14.1
wsproto                       1.2.0
xgboost                       1.7.4
```