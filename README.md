# Gender

Gender gives you the opportunity to see the gender and nationality of a name

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to get Gender's dependencies .

```bash
pip3 install sqlalchemy
git clone https://github.com/pipinstallpip/gender.git
```

## Usage

```python
from src import Gender

g = Gender()
print(g.ismale('Andrea')) #returns True
print(g.isfemale('Andrea')) #returns True
print(g.isunisex('Andrea')) #returns True

```

### Class methods

**Gender check**

- ismale(self, name: str) -> bool:
- isfemale(self, name: str) -> bool:
- isunisex(self, name: str) -> bool:

**Nationality check**

- isenglish(self, name: str) -> bool:
- isgerman(self, name: str) -> bool:
- isfrench(self, name: str) -> bool:
- isdutch(self, name: str) -> bool:
- isspanish(self, name: str) -> bool:
- isgreek(self, name: str) -> bool:
- isportoguese(self, name: str) -> bool:
- isicelandic(self, name: str) -> bool:
- isswedish(self, name: str) -> bool:
- isitalian(self, name: str) -> bool:
- isafrican(self, name: str) -> bool:
- isargentine(self, name: str) -> bool:
- isturkish(self, name: str) -> bool:
- isjapanese(self, name: str) -> bool:

**Extra**
- getfemalenames(self) -> list:
- getmalenames(self) -> list:
- getcountries(self, name: str) -> list:

## Data update
Manipulate the countries.sql and names.sql files to add data, then run the following command

```bash
cd data
python3 UpdateData.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT License

Copyright (c) 2020 pipinstallpip

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.