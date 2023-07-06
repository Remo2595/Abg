#  Copyright (C) 2023-present Abishnoi6 <https://github.com/Abishnoi69>
#
#  This file is part of Abg.
#
#  Abg is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Abg is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Abg.  If not, see <http://www.gnu.org/licenses/>.

# ===================================================================

import re
from sys import argv

from compiler.api import compiler as api_compiler
from compiler.errors import compiler as errors_compiler
from setuptools import find_packages, setup

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open("Abg/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

if len(argv) > 1 and argv[1] in ["bdist_wheel", "install", "develop"]:
    api_compiler.start()
    errors_compiler.start()

setup(
    name="Abg",
    version=version,
    description="Telegram bot helpers, A add-on for Pyrogram",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Abishnoi69/Abg",
    download_url="https://github.com/Abishnoi69/Abg/releases/latest",
    author="Abishnoi",
    author_email="Abishnoi@Abg.org",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    keywords="telegram bot chat messenger mtproto api client library python conversation keyboard userbot patch botapi https",
    project_urls={
        "Tracker": "https://github.com/Abishnoi69/Abg/issues",
        "Community": "https://t.me/AbgPY",
        "Source": "https://github.com/Abishnoi69/Abg",
        "Documentation": "https://github.com/Abishnoi69/Abg/tree/master/doce",
    },
    python_requires="~=3.7",
    package_data={
        "Abg": ["py.typed"],
    },
    packages=find_packages(exclude=["compiler*", "tests*"]),
    zip_safe=False,
    install_requires=requires,
)
