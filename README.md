# Swiss Army Knife

> Python CLI tool


* Easiest CLI api using [click], as compared to nodejs, dotnetcore, plain shell script etc.
  * cross platform, decorator styled cli arguments
  * Supports lazy loading of subcommands at runtime
  * Arbitrary nesting of commands
  * Automatic help page generation

```
python3 -m venv venv
source venv/bin/activate.fish
pip install --upgrade pip

python setup.py develop
sak --count=5
```

### Problems

1. How to package, publish and distribute app?
2. Which build tool to use?

```mermaid
graph TD
License  --> R([CLI App])
setup.py --> R
tox.ini  --> R
dodo.py  --> R

R ==> src
R ==> docs
R ==> tests

id1((This is the text in the circle))

classDef default fill:#f9f,stroke:#333,stroke-width:4px;
linkStyle default fill:none,stroke-width:2px,stroke:blue
```

```mermaid
graph TD
A[fa:fa-university Event Publishing Service ] -->|publishes to topic| C[fa:fa-bullhorn Topic for new events ]
A -->|writes data to|I[fa:fa-shopping-cart Dump Event Bucket ]
C -->|Terminal Update SQS Message| D[fa:fa-bars Event Receiver Queue ]
C -->|Terminal Update SQS Message| E[fa:fa-bars Some Other Service Queue ]
D -->|consumes|G[fa:fa-beer Event Receiver Service Consumer ]
E -->|consumes|H[fa:fa-beer Some Other Event Consumer ]

B["fa:fa-twitter for peace"]
B-->C[fa:fa-ban forbidden]
B-->D(fa:fa-spinner);
B-->E(A fa:fa-camera-retro perhaps?);

```



[click]: https://github.com/pallets/click


### Resources

* [python-testing-frameworks](https://www.softwaretestinghelp.com/python-testing-frameworks/)
* [python build tools](https://wiki.python.org/moin/ConfigurationAndBuildTools)




#### Get in touch with me

> I am looking for Jobs ... :sunglasses:

* [Github](https://github.com/avimehenwal/)
* [My Website](https://avimehenwal.in)
* [Twitter Handle](https://twitter.com/avimehenwal)
* [LinkedIn](https://in.linkedin.com/in/avimehenwal)
* [Stackoverflow](https://stackoverflow.com/users/1915935/avi-mehenwal)

<a href="https://www.buymeacoffee.com/F1j07cV" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>

 Spread Love :hearts: and not :no_entry_sign: hatred   [![Twitter Follow](https://img.shields.io/twitter/follow/avimehenwal.svg?style=social)](https://twitter.com/avimehenwal)