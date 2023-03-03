from ganttouchthis import BacklogItem, Date, Gantt, Priority, Project, Task

zero_date = Date(2023, 3, 1)
g = Gantt()
g.add_project(
    name="Python лучшие инструменты и практики",
    tasks="17,A",
    priority=Priority.CRITICAL,
    groups={"python"},
    start=zero_date,
    end=zero_date + 60,
    cluster=2,
)
g.add_project(
    name="Robust Python",
    tasks="24",
    priority=Priority.HIGH,
    groups={"python"},
    start=zero_date + 3,
    end=zero_date + 90,
    cluster=1,
)
g.add_project(
    name="Python Programming with Design Patterns",
    tasks="13",
    priority=Priority.HIGH,
    groups={"python", "design_patterns"},
    start=zero_date + 30,
    end=zero_date + 70,
    cluster=1,
)
g.add_project(
    name="Python Standard Library",
    tasks="Introduction,Built-in Functions,Built-in Constants,Built-in Types,Built-in Exceptions,string,re,difflib,textwrap,unicodedata,stringprep,readline,rlcompleter,struct,codecs,datetime,zoneinfo,calendar,collections,collections.abc,heapq,bisect,array,weakref,types,copy,pprint,reprlib,enum,graphlib,numbers,math,cmath,decimal,fractions,random,statistics,itertools,functools,operator,pathlib,os.path,fileinput,stat,filecmp,tempfile,glob,fnmatch,linecache,shutil,pickle,copyreg,shelve,marshal,dbm,sqlite3,zlib,gzip,bz2,lzma,zipfile,tarfile,csv,configparser,tomllib,netrc,plistlib,hashlib,hmac,secrets,os,io,time,argparse,getopt,logging,logging.config,logging.handlers,getpass,curses,curses.textpad,curses.ascii,curses.panel,platform,errno,ctypes,threading,multiprocessing,multiprocessing.shared_memory,The concurrent package,concurrent.futures,subprocess,sched,queue,contextvars,_thread,asyncio,socket,ssl,select,selectors,signal,mmap,email,json,mailbox,mimetypes,base64,binascii,quopri,html,html.parser,html.entities,XML Processing Modules,xml.etree.ElementTree,xml.dom,xml.dom.minidom,xml.dom.pulldom,xml.sax,xml.sax.handler,xml.sax.saxutils,xml.sax.xmlreader,xml.parsers.expat,webbrowser,wsgiref,urllib,urllib.request,urllib.response,urllib.parse,urllib.error,urllib.robotparser,http,http.client,ftplib,poplib,imaplib,smtplib,uuid,socketserver,http.server,http.cookies,http.cookiejar,xmlrpc,xmlrpc.client,xmlrpc.server,ipaddress,wave,colorsys,gettext,locale,turtle,cmd,shlex,tkinter,tkinter.colorchooser,tkinter.font,Tkinter Dialogs,tkinter.messagebox,tkinter.scrolledtext,tkinter.dnd,tkinter.ttk,tkinter.tix,IDLE,typing,pydoc,Python Development Mode,Effects of the Python Development Mode,ResourceWarning Example,Bad file descriptor error example,doctest,unittest,unittest.mock,unittest.mock,2to3,test,test.support,test.support.socket_helper,test.support.script_helper,test.support.bytecode_helper,test.support.threading_helper,test.support.os_helper,test.support.import_helper,test.support.warnings_helper,Audit events table,bdb,faulthandler,pdb,The Python Profilers,timeit,trace,tracemalloc,distutils,ensurepip,venv,zipapp,sys,sysconfig,builtins,__main__,warnings,dataclasses,contextlib,abc,atexit,traceback,__future__,gc,inspect,site,code,codeop,zipimport,pkgutil,modulefinder,runpy,importlib,importlib.resources – Resources,Deprecated functions,importlib.resources.abc – Abstract base classes for resources,Using importlib.metadata,The initialization of the sys.path module search path,ast,symtable,token,keyword,tokenize,tabnanny,pyclbr,py_compile,compileall,dis,pickletools,msvcrt,winreg,winsound,posix,pwd,grp,termios,tty,pty,fcntl,resource,syslog,aifc,asynchat,asyncore,audioop,cgi,cgitb,chunk,crypt,imghdr,imp,mailcap,msilib,nis,nntplib,optparse,ossaudiodev,pipes,smtpd,sndhdr,spwd,sunau,telnetlib,uu,xdrlib,Security Considerations",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 1,
    interval=3,
    cluster=2,
)
g.add_project(
    name="How to use C from Python? - #9",
    tasks="1",
    priority=Priority.WISH,
    groups={"python", "c"},
    start=zero_date + 15,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Mastering Python Design Patterns",
    tasks="16",
    priority=Priority.WISH,
    groups={"python", "design_patterns"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Design Patterns in Python",
    tasks="8",
    priority=Priority.WISH,
    groups={"python", "design_patterns"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python FAQs",
    tasks="1",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Elementary Math for Computer Science with Python.pdf",
    tasks="8,A",
    priority=Priority.WISH,
    groups={"math", "python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="C and Python Applications.pdf",
    tasks="6,A",
    priority=Priority.WISH,
    groups={"c", "python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python. The True Book.pdf",
    tasks="8",
    priority=Priority.HIGH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python Concurrency with asyncio.pdf",
    tasks="14",
    priority=Priority.WISH,
    groups={"python", "async", "concurrency"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Une introduction à Python 3.pdf",
    tasks="9,J",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Профессиональная разработка на Python.pdf",
    tasks="12",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Programming in Python. An Interdisciplinary Approach.pdf",
    tasks="4,B",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="CPython Internals.pdf",
    tasks="17",
    priority=Priority.WISH,
    groups={"python", "c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Fast numerical computations with Cython.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"python", "c"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Cython: The Best of Both Worlds.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"python", "c"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Изучаем Python, том 2.pdf",
    tasks="26-41,D",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="A functional start to computing with Python.pdf",
    tasks="32",
    priority=Priority.WISH,
    groups={"python", "functional"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Effective Python.pdf",
    tasks="10",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Классические задачи Computer Science на языке Python",
    tasks="10",
    priority=Priority.WISH,
    groups={"cs", "alg", "python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Fluent Python (2e).pdf",
    tasks="24",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Fluent Python (2015).pdf",
    tasks="21,B",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python Fluente (2015).pdf",
    tasks="21,B",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Functional Programming in Python.pdf",
    tasks="4",
    priority=Priority.WISH,
    groups={"python", "functional"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Секреты Python Pro.pdf",
    tasks="11,A",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Inside the Python Virtual Machine.pdf",
    tasks="12",
    priority=Priority.WISH,
    groups={"python", "python_low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Чистый Python.pdf",
    tasks="9",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Путь Python.pdf",
    tasks="13",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn More Python 3 the Hard Way.pdf",
    tasks="0-52",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn Python 3 the Hard Way",
    tasks="0-52,B",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Advanced Python Development.pdf",
    tasks="12",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mastering Python for Web. A Beginner's Guide.pdf",
    tasks="6",
    priority=Priority.WISH,
    groups={"python", "web"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Full Speed Python.pdf",
    tasks="12",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Serious Python.pdf",
    tasks="13",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Паттерны разработки на Python. TDD, DDD и событийно-ориентированная архитектура.pdf",
    tasks="14,A,B,C,D,E",
    priority=Priority.WISH,
    groups={"python", "design_patterns"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Beyond the Basic Stuff with Python. Best Practices.pdf",
    tasks="17",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://pybind11.readthedocs.io/en/latest/",
    tasks="19",
    priority=Priority.WISH,
    groups={"python", "c++", "python_low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Стандартная библиотека Python 3.pdf",
    tasks="19,A,B,C",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Python Book.pdf",
    tasks="20",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://book.pythontips.com/en/latest/index.html",
    tasks="27",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python. Сборник упражнений.pdf",
    tasks="16",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Exploring CPython's Internals - Python Developer's Guide",
    tasks="10",
    priority=Priority.WISH,
    groups={"python", "python_low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python, например.pdf",
    tasks="24",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Three Keys to Leveling up Your Python.pdf",
    tasks="3",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Простой Python (2021).pdf",
    tasks="22,A5",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python. Das umfassende Handbuch",
    tasks="40,A",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn Python Programing.pdf",
    tasks="15",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Основы Python (2021).pdf",
    tasks="21,A",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python Glossary",
    tasks="1",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Как устроен Python. Гид для разработчиков, программистов и интересующихся [2019] Харрисон",
    tasks="27,B",
    priority=Priority.WISH,
    groups={"python", "python_low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Advanced Guide to Python 3 Programming",
    tasks="41",
    priority=Priority.HIGH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Advanced Python Programming.pdf",
    tasks="23",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python Developer’s Guide",
    tasks="20",
    priority=Priority.WISH,
    groups={"python", "python_lowlevel"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python/C API",
    tasks="96",
    priority=Priority.WISH,
    groups={"python", "c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Clean Code in Python.pdf",
    tasks="10",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="40 Algorithms Every Programmer Should Know (Python).pdf",
    tasks="40",
    priority=Priority.WISH,
    groups={"python", "alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Practical Cryptography in Python. Learning Correct Cryptography by Example.pdf",
    tasks="8",
    priority=Priority.WISH,
    groups={"crypto", "python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Bash Pocket Reference. Help for Power Users and Sys Admins.pdf",
    tasks="18",
    priority=Priority.WISH,
    groups={"shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Udemy C++ Masterclass",
    tasks="699",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=7,
)
g.add_project(
    name="Cherno C++ Playlist",
    tasks="100",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="C++. Das umfassende Handbuch",
    tasks="31,A",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Programming Principles and Practice Using C++",
    tasks="17",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Beginning C++17.pdf",
    tasks="0-19",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Beginning C++20.pdf",
    tasks="0-21",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Schrödinger programmiert C++",
    tasks="18",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Data Structures and Algorithms in Cpp.pdf",
    tasks="14,A",
    priority=Priority.WISH,
    groups={"c++", "dsa", "alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://www.learncpp.com/",
    tasks="23,C",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Here's An Easier Way to Understand Pointer Math in C/C++ Programming - YouTube",
    tasks="1",
    priority=Priority.WISH,
    groups={"c", "c++"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="C++ на примерах.pdf",
    tasks="14,A",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Cpp for Mathematicians.pdf",
    tasks="15,C",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Accelerated C++.pdf",
    tasks="0-16,B",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="C++ by Dissection",
    tasks="11,D",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Beginning Cpp Programming.pdf",
    tasks="10",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="How Linux Works. What Every Superuser Should Know.pdf",
    tasks="17",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Введение в язык Си++.pdf",
    tasks="6",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools",
    tasks="1",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="C++ Tutorial 2021 - YouTube",
    tasks="1",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Язык программирование C++. Полное руководство.pdf",
    tasks="20,A",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://vcpkg.io/en/index.html",
    tasks="1",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Lecture: Modern C++ (Summer 2018, Uni Bonn)",
    tasks="0-9",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Rook's Guide to Cpp.pdf",
    tasks="23",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Уроки програмування на С++ для початківців / aCode",
    tasks="267",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Hands-On Machine Learning with Cpp.pdf",
    tasks="13",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Modern CMake for Cpp.pdf",
    tasks="12,A",
    priority=Priority.WISH,
    groups={"c++", "cmake"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="C++ Cheatsheets",
    link="https://hackingcpp.com/cpp/cheat_sheets.html",
    tasks="Algorithms,Views,Containers,Randomness,Utilities,Language,Libraries,Design,Engineering,Terminology",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="C++20 Recipes.pdf",
    tasks="14",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="CMake Cookbook",
    tasks="15",
    priority=Priority.WISH,
    groups={"cmake", "c", "c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Система построения проектов CMake.pdf",
    tasks="3",
    priority=Priority.WISH,
    groups={"c", "c++", "cmake"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Professional CMake. A Practical Guide.pdf",
    tasks="28",
    priority=Priority.WISH,
    groups={"cmake", "c", "c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="C++ - das Übungsbuch",
    tasks="29,A",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Professional C++",
    tasks="34A,B,C,D",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://github.com/pdeitel/CPlusPlus20ForProgrammers",
    tasks="20",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Modern Parallel Programming with C++ and Assembly Language",
    tasks="19,A,B",
    priority=Priority.WISH,
    groups={"c++", "low_level", "parallel"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Touch of Class",
    tasks="19,A,B,C,D,E",
    priority=Priority.WISH,
    groups={"oop", "c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="An Introduction to GCC. For the GNU Compilers GCC and G++",
    tasks="13,A,B",
    priority=Priority.WISH,
    groups={"c", "c++", "compiler"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="C++20 for Programmers",
    tasks="10",
    priority=Priority.WISH,
    groups={"c++"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Foundations of Programming Languages.pdf",
    tasks="9",
    priority=Priority.WISH,
    groups={"proglang"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn Computer Vision Using OpenCV. With Deep Learning CNNs and RNNs",
    tasks="6",
    priority=Priority.WISH,
    groups={"cv", "opencv", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Linguae per carmina",
    tasks="300",
    priority=Priority.WISH,
    groups={"ls", "multilingual"},
    start=zero_date + 306,
    interval=3,
)
g.add_project(
    name="Everything You Need to Ace Computer Science and Coding.pdf",
    tasks="39",
    priority=Priority.WISH,
    groups={"cs_gen"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP01) Speech and Language Processing (2023).pdf",
    tasks="26,C",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP02) Speech and Language Processing (2008).djvu",
    tasks="25",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Cómo piensa el mundo: Una historia global de la filosofía",
    tasks="28",
    priority=Priority.MEDIUM_LOW,
    groups={"philo"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="LingoDeer",
    tasks="44",
    priority=Priority.LOW,
    groups={"ls"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Fusha to Shami",
    tasks="33",
    priority=Priority.WISH,
    groups={"ar"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://uk.wikipedia.org/wiki/Обробка_природної_мови",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="NLP04) Deep Learning for NLP and Speech Recognition",
    tasks="13,L",
    priority=Priority.WISH,
    groups={"nlp", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Digital Electronics",
    tasks="12",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP03) NLP (Eisenstein)",
    tasks="19,B",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Машинное обучение без лишних слов.pdf",
    tasks="11",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Dual Numbers",
    link="https://www.youtube.com/watch?v=ceaNqdHdqtg",
    tasks="1",
    priority=Priority.WISH,
    groups={"dl", "math"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Об'єктно-орієнтоване програмування",
    tasks="18,A",
    priority=Priority.WISH,
    groups={"oop"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Cogneethi -  Evolution Of Object Detection Networks",
    tasks="134",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=4,
)
g.add_project(
    name="NLP Wikipedia",
    tasks="105",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Gemalte Wörter",
    tasks="214",
    priority=Priority.LOW,
    groups={"ls", "zh"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Open Data Structures",
    tasks="14",
    priority=Priority.WISH,
    groups={"dsa"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Computer Science of TeX and LaTeX.pdf",
    tasks="7",
    priority=Priority.WISH,
    groups={"cs", "tex"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Transfer Learning for Natural Language Processing.pdf",
    tasks="11,B",
    priority=Priority.WISH,
    groups={"nlp", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Code and Data for the Social Sciences. A Practitioner's Guide.pdf",
    tasks="8,A",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Healthy Programmer",
    tasks="12,A2",
    priority=Priority.CRITICAL,
    groups={"prog", "meta"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="A Programmer's Guide to Computer Science. Volume I.pdf",
    tasks="14,B",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Julia Docs",
    tasks="108",
    priority=Priority.WISH,
    groups={"julia"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="How Software Works",
    tasks="9",
    priority=Priority.HIGHER,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP09) NLP and CL II (Kurdi)",
    tasks="4",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP07) Advanced Natural Language Processing with TensorFlow 2.pdf",
    tasks="16",
    priority=Priority.WISH,
    groups={"nlp", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Дискретная математика для программистов.pdf",
    tasks="9",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP18) Taming Text.pdf",
    tasks="9",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://www.gnu.org/software/bash/manual/",
    tasks="14",
    priority=Priority.WISH,
    groups={"bash"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP13) Practical Natural Language Processing.pdf",
    tasks="11",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Willensfreiheit",
    tasks="8",
    priority=Priority.WISH,
    groups={"free_will"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Das Handwerk der Freiheit",
    tasks="11,A",
    priority=Priority.WISH,
    groups={"free_will"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="HOG paper",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Detecting Faces (Viola Jones Algorithm) - Computerphile",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="ML Algorithms.jpg",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Git Cheat Sheet",
    tasks="1",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Page Segmentation for Historical Handwritten Documents Using Fully Convolutional Networks.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://uk.wikipedia.org/wiki/Інформатика#Штучний_інтелект",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml", "uk"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="The Gospel of John in Greek and Latin",
    tasks="21",
    priority=Priority.WISH,
    groups={"la", "grc"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Modern C for Absolute Beginners",
    tasks="47,E",
    priority=Priority.WISH,
    groups={"c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Algorithmic Thinking. A Problem Based Introduction.pdf",
    tasks="8,C",
    priority=Priority.WISH,
    groups={"alg", "c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="C Programming. A Self-Teaching Introduction.pdf",
    tasks="5,E",
    priority=Priority.WISH,
    groups={"c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="100 примеров на Си.djvu",
    tasks="100",
    priority=Priority.WISH,
    groups={"c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="C Programming for Dummies.pdf",
    tasks="7",
    priority=Priority.WISH,
    groups={"c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Smaller C.pdf",
    tasks="7",
    priority=Priority.WISH,
    groups={"c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The C Programming Language 2e",
    tasks="7,C",
    priority=Priority.WISH,
    groups={"c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Linux Command Line",
    tasks="36",
    priority=Priority.WISH,
    groups={"shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Head First Design Patterns.pdf",
    tasks="14",
    priority=Priority.WISH,
    groups={"design_patterns"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP14) Transformers for Natural Language Processing.pdf",
    tasks="12",
    priority=Priority.WISH,
    groups={"transformer", "nlp", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mythos Determinismus",
    tasks="8",
    priority=Priority.WISH,
    groups={"free_will"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Шаблоны и практика глубокого обучения.pdf",
    tasks="14",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Использование Docker.pdf",
    tasks="13",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Computing with Data",
    tasks="15",
    priority=Priority.WISH,
    groups={"ds", "cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Шаблоны и практика глубокого обучения.pdf",
    tasks="14",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://sites.google.com/view/datascience-cheat-sheets",
    tasks="9,D",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Neural Networks and Deep Learning",
    tasks="9,A",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introductory Mathematics: Algebra and Analysis (Smith)",
    tasks="8",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Clean Code (IT).pdf",
    tasks="17,C",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Clean Code. A Handbook of Agile Software Craftsmanship.pdf",
    tasks="17,C",
    priority=Priority.WISH,
    groups={"agile", "management"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="MIT DL Course",
    tasks="8",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Computer Organization. An Under the Hood Look at Hardware and x86-64 Assembly.pdf",
    tasks="21",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Україна - не Росія",
    tasks="30",
    priority=Priority.WISH,
    groups={"uk"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Computer Science Illuminated",
    tasks="18",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Computer Science - A Very Short Introduction",
    tasks="8",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="A Concise Introduction to ML (Faul)",
    tasks="9,A",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Encyclopedia of Machine Learning and Data Mining.pdf",
    tasks="8",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Machine Learning (Mitchell)",
    tasks="13,A",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Intro to Github",
    tasks="1",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Математика для Data Science [2021] Миронов, Минеева",
    tasks="6",
    priority=Priority.WISH,
    groups={"math", "ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP00) Natural Language Processing with Transformers.pdf",
    tasks="11",
    priority=Priority.WISH,
    groups={"transformer", "nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Building your Mouseless Development Environment",
    tasks="25",
    priority=Priority.WISH,
    groups={"prog", "setup"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Computing with Data",
    tasks="15",
    priority=Priority.WISH,
    groups={"ds", "cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Missing Semester of Your CS Education",
    tasks="14",
    priority=Priority.WISH,
    groups={"prog", "setup"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Computing Handbook. Computer science and software engineering.pdf",
    tasks="93",
    priority=Priority.WISH,
    groups={"cs", "prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="All the Math You Missed",
    tasks="16,A",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="ML Spider Diagram RU.jpg",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Taxonomy of Principal Distances.jpg",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml", "math"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Linux intern",
    tasks="17",
    priority=Priority.WISH,
    groups={"linux", "low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="zsh Docs",
    tasks="26,A6",
    priority=Priority.WISH,
    groups={"shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Embeddings in Natural Language Processing",
    tasks="9",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Art of Clean Code.pdf",
    tasks="0-9",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Code Craft - The Practice of Writing Excellent Code.pdf",
    tasks="24,A",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Softwareengineering - Wie entwickelt man Software",
    tasks="75",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Гид по Computer Science.pdf",
    tasks="35,B",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="3Blue1Brown Essence of Linear Algebra & Calculus & Neural Networks",
    tasks="32",
    priority=Priority.WISH,
    groups={"math", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Foundations of Mathematics (Ian Stewart)",
    tasks="16,A",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Modern Vim.pdf",
    tasks="7,A",
    priority=Priority.WISH,
    groups={"vim"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Обработка естественного языка в действии.pdf",
    tasks="13,A6",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP12) NLP in Action.pdf",
    tasks="13",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Week 12 – Practicum: Attention and the Transformer",
    tasks="1",
    priority=Priority.WISH,
    groups={"dl", "nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Git Tutorial",
    tasks="1",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Programming Languages. Principles and Paradigms",
    tasks="13",
    priority=Priority.WISH,
    groups={"proglang"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Das illustrierte Kompendium der Philosophie",
    tasks="5",
    priority=Priority.WISH,
    groups={"philo"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Techtiefen",
    tasks="36",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Самоучитель украинского языка",
    tasks="50,A",
    priority=Priority.WISH,
    groups={"uk"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Bin ich mein Gehirn?",
    tasks="14",
    priority=Priority.WISH,
    groups={"neuro", "free_will"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Design Patterns (Lasater).pdf",
    tasks="4",
    priority=Priority.WISH,
    groups={"design_patterns"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introducción al sistema operativo GNU/Linux.pdf",
    tasks="0-7,A",
    priority=Priority.WISH,
    groups={"linux"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Das lateinische Basisvokabular",
    tasks="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z",
    priority=Priority.WISH,
    groups={"la"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Griechische Grammatik (Bornemann)",
    tasks="1.I,1.II,1.III,2.I,2.II,2.III,2.IV,2.V,2.VI.A,2.VI.B,2.VI.C,3.I,3.II,3.III,A.1,A.2,R.1,R.2,R.3",
    priority=Priority.WISH,
    groups={"grc"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Refactoring.pdf",
    tasks="12",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Dive into Deep Learning",
    tasks="20",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn Vim Tonight",
    tasks="18",
    priority=Priority.WISH,
    groups={"vim"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Code (Petzold)",
    tasks="25",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Код.pdf",
    tasks="25",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn Git Branching",
    tasks="1",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Bert",
    tasks="1",
    priority=Priority.WISH,
    groups={"transformer", "nlp", "dl"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Injecting fairness into machine-learning models",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Handbook of Linear Algebra",
    tasks="98",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Pattern Recognition and Machine Learning (Bishop)",
    tasks="14,E",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP15) Audio Processing and Speech Recognition. Concepts, Techniques and Research Overviews.pdf",
    tasks="5",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Алгоритмы обработки текста. 125 задач с решениями.pdf",
    tasks="125",
    priority=Priority.WISH,
    groups={"nlp", "alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP26) Real-World Natural Language Processing.pdf",
    tasks="11",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="TF Certificate Handbook.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"dl", "tf"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://towardsdatascience.com/ai-papers-to-read-in-2022-c6edd4302247",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml", "dl"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Sigmoid and Logit function | Logical Intuitions",
    tasks="1",
    priority=Priority.WISH,
    groups={"dl", "math"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Ingeniería del software.pdf",
    tasks="32",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Computer Systems - A Programmer's Perspective",
    tasks="12",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn TensorFlow 2.0.pdf",
    tasks="6",
    priority=Priority.WISH,
    groups={"dl", "tf"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Programming Logic and Design, Comprehensive.pdf",
    tasks="14,D",
    priority=Priority.WISH,
    groups={"prog", "cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Lilian Weng Blog",
    tasks="35",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Наш творчий мозок.pdf",
    tasks="31",
    priority=Priority.WISH,
    groups={"neuro"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="An Introduction To Programs",
    tasks="1",
    priority=Priority.WISH,
    groups={"prog", "cs"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Lecture notes: Literature search and scientific reading",
    tasks="1",
    priority=Priority.WISH,
    groups={"misc"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="C32 | SIFT | Scale Invariant Feature Transform | Computer Vision | Object detection | EvODN - YouTube",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Modern C",
    tasks="19,A",
    priority=Priority.WISH,
    groups={"c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mastering C Pointers.pdf",
    tasks="10",
    priority=Priority.WISH,
    groups={"c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Язык Си для начинающих",
    link="https://www.youtube.com/playlist?list=PL0lO_mIqDDFX2VcYQrDzrvYpzMVNexrp0",
    tasks="9",
    priority=Priority.WISH,
    groups={"c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Си на примерах. Практика",
    tasks="13",
    priority=Priority.WISH,
    groups={"c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Effective C",
    tasks="0-11",
    priority=Priority.WISH,
    groups={"c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Transformers Video",
    link="https://www.youtube.com/watch?v=XSSTuhyAmnI",
    tasks="1",
    priority=Priority.WISH,
    groups={"transformer", "dl"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Заблуждения и антишаблоны, относящиеся к devops.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Open letter",
    link="http://assets.press.princeton.edu/chapters/s10825.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Handbook of Mathematics",
    tasks="28,A",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP08) NLP and CL I (Kurdi)",
    tasks="4",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Programming from the Ground Up.pdf",
    tasks="13,A,B,C,D,E,F,G,H,I",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP10) Neural Network Methods for NLP.pdf",
    tasks="21",
    priority=Priority.WISH,
    groups={"nlp", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="LPP 13-16",
    tasks="27",
    priority=Priority.WISH,
    groups={"language_study", "multi"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Грокаем глубокое обучение.pdf",
    tasks="16",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Notation Sheet",
    link="https://nthu-datalab.github.io/ml/slides/Notation.pdf?fbclid=IwAR0kYjO13sIR4JvN8VVBrgXBH8e9wlE1TGBv_YC6wuAzyCFved5TC4gCqc8",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Deep Learning. A Comprehensive Overview.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="nand2tetris",
    tasks="12",
    priority=Priority.WISH,
    groups={"low_level", "compiler"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://sebastianraschka.com/faq/docs/logistic-why-sigmoid.html",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml", "math"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="First Year in Code",
    tasks="0-22,C",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Intro to Deep Learning (Skansi)",
    tasks="11",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn Bash the Hard Way.pdf",
    tasks="4",
    priority=Priority.WISH,
    groups={"shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP-01) Applied Natural Language Processing in the Enterprise.pdf",
    tasks="12",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Align LPP",
    tasks="27",
    priority=Priority.WISH,
    groups={"language_study", "multi"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Reinforcement Learning. An Introduction",
    tasks="17",
    priority=Priority.WISH,
    groups={"rl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="But How Do It Know. The Basic Principles of Computers for Everyone.pdf",
    tasks="10",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Современные методы обработки естественного языка.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Обработка естественного языка.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Cambridge NLP Notes.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Attention is All You Need",
    tasks="1",
    priority=Priority.WISH,
    groups={"transformer", "dl"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Conditional Random Fields : Data Science Concepts - YouTube",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml", "nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Linguistique computationnelle. Entre sciences cognitives et traitement automatique des langues.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Deep Learning for Amharic Text-Image Recognition: Algorithm, Dataset and Application",
    tasks="1",
    priority=Priority.WISH,
    groups={"dl", "nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://euler.stephan-brumme.com/",
    tasks="200",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Ukrainian. A Comprehensive Grammar",
    tasks="8",
    priority=Priority.WISH,
    groups={"uk"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Регулярные выражения.pdf",
    tasks="10",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Concise Computer Vision.pdf",
    tasks="10",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Programmer's Brain. What Every Programmer Needs.pdf",
    tasks="13",
    priority=Priority.HIGHER,
    groups={"prog", "meta"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Machine Learning Solutions Architect Handbook.pdf",
    tasks="12",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Linux in a Nutshell.pdf",
    tasks="15",
    priority=Priority.WISH,
    groups={"linux"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn to Program with Assembly",
    tasks="19,A11",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Читаемый код.pdf",
    tasks="15",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Linux Philosophy for SysAdmins.pdf",
    tasks="26",
    priority=Priority.WISH,
    groups={"linux"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Secret Life of Programs. Understand Computers, Craft Better Code.pdf",
    tasks="0-15",
    priority=Priority.WISH,
    groups={"low_level", "cs", "prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Машинное обучение. Паттерны проектирования.pdf",
    tasks="I,II,30,VIII",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Der freie Wille",
    tasks="8,A",
    priority=Priority.WISH,
    groups={"free_will"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learning the Vi and Vim Editors",
    tasks="17,A,B,C,D",
    priority=Priority.WISH,
    groups={"vim"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Dialogues Project",
    tasks="12",
    priority=Priority.WISH,
    groups={"language_study", "multi"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python Tutorial",
    tasks="16",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Изучаем Python, том 1.pdf",
    tasks="25,A",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Test-Driven Development with Python.pdf",
    tasks="26,A10",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Functional Python Programming. Discover the power of functional programming, generator functions, lazy evaluation, the built-in itertools library, and monads.pdf",
    tasks="16",
    priority=Priority.WISH,
    groups={"python", "functional"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python Language Reference",
    tasks="10,A,B",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://docs.python.org/3/extending/",
    tasks="5",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python HOWTOs",
    tasks="16",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Functional Programming in Python (2019)",
    tasks="13",
    priority=Priority.WISH,
    groups={"python", "functional"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Flask Framework Cookbook.pdf",
    tasks="13",
    priority=Priority.WISH,
    groups={"python", "web"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Optimizing Visual Studio Code for Python Development",
    tasks="5",
    priority=Priority.WISH,
    groups={"vscode", "python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Python. Экспресс-курс",
    tasks="42,A,B",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Coder’s Apprentice. Learning Programming with Python 3",
    tasks="27,A,B,C,D,E,F",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://python-patterns.guide/",
    tasks="74",
    priority=Priority.WISH,
    groups={"python", "design_patterns"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Visual Studio Code for Python Programmers",
    tasks="12",
    priority=Priority.WISH,
    groups={"vscode"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mastering Vim",
    tasks="21",
    priority=Priority.WISH,
    groups={"vim"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Big Data PT.pdf",
    tasks="6",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Object-oriented vs Functional Programming.pdf",
    tasks="40",
    priority=Priority.WISH,
    groups={"oop", "functional"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Numbers and Functions: Steps into Analysis (Burn)",
    tasks="12,A3",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Computer Science Distilled",
    tasks="9,A,B,C,D",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Теоретический минимум по Computer Science",
    tasks="8,A0-A4",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP Overview",
    tasks="9",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Agile (PT).pdf",
    tasks="8",
    priority=Priority.WISH,
    groups={"agile", "management"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Elements of Computing Systems (2e)",
    tasks="13,A5",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Машинное обучение. Карманный справочник.pdf",
    tasks="19",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Bewusstsein und freier Wille",
    tasks="19",
    priority=Priority.WISH,
    groups={"free_will"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Computer Vision Algorithms and Applications.pdf",
    tasks="15,A,B,C",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Neural Networks and Deep Learning (Michael Nielsen)",
    tasks="6,A",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Missing README.pdf",
    tasks="14",
    priority=Priority.HIGHER,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Simple Explanation of LSTM | Deep Learning Tutorial 36 (Tensorflow, Keras & Python) - YouTube",
    tasks="1",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Logique, Linguistique et Informatique.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://uk.wikipedia.org/wiki/Машинне_навчання",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Page Segmentation of Historical Document Images  with Convolutional Autoencoders.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Git Handbook",
    link="https://www.freecodecamp.org/news/the-essential-git-handbook-a1cf77ed11b5/",
    tasks="1",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Make list of top 1000 Chinese characters, all input codes, constituent radicals, character combinations, pronunciations, eventually example phrases",
    tasks="1000",
    priority=Priority.WISH,
    groups={"zh"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=10,
)
g.add_project(
    name="Word2Vec",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Computer Science. An Interdisciplinary Approach.pdf",
    tasks="7,C",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Advanced Deep Learning with TensorFlow 2 and Keras.pdf",
    tasks="13",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="ix Developer - Sichere Software entwickeln",
    tasks="6",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Metric and Topological Spaces (Sutherland)",
    tasks="17",
    priority=Priority.WISH,
    groups={"math", "topo"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Nano Docs",
    tasks="10",
    priority=Priority.WISH,
    groups={"prog_misc"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Cogneethi - Classical CV - HOG and SIFT intuitions",
    tasks="15",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Nano Cheatsheet",
    tasks="1",
    priority=Priority.WISH,
    groups={"prog_misc"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Computational Linguistics and Deep Learning.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp", "dl"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Elmo",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp", "dl"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Reviewing Pull Requests",
    tasks="1",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Computerlinguistik und Sprachtechnologie.pdf",
    tasks="6",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/bash",
    tasks="89",
    priority=Priority.WISH,
    groups={"bash"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Ich denke, also will ich: Philosophie des freien Willens",
    tasks="5",
    priority=Priority.WISH,
    groups={"free_will"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Computers: A History",
    link="https://www.youtube.com/watch?v=OwQ9DFeJysw&list=PLU3TaPgchJtRANwKajkQyUIrRYGthyl7t&index=4",
    tasks="1",
    priority=Priority.WISH,
    groups={"cs", "history"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="The Future of Computer Security",
    link="https://www.youtube.com/watch?v=sJvLyccxIJY&list=PLU3TaPgchJtRANwKajkQyUIrRYGthyl7t&index=6",
    tasks="1",
    priority=Priority.WISH,
    groups={"cs", "crypto"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Чистый Agile. Основы гибкости.pdf",
    tasks="8",
    priority=Priority.WISH,
    groups={"agile", "management"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Software Development, Design, and Coding.pdf",
    tasks="19",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Software Engineering. Grundlagen, Menschen, Prozesse, Techniken.epub",
    tasks="26",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Scrum. Революционный метод управления проектами.pdf",
    tasks="0-9,A,B",
    priority=Priority.WISH,
    groups={"agile", "management"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Pro bash programming: scripting the GNU/Linux shell",
    tasks="15,A",
    priority=Priority.WISH,
    groups={"shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Сценарии командной оболочки.pdf",
    tasks="15,B",
    priority=Priority.WISH,
    groups={"shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Real-World Kanban.pdf",
    tasks="5,A",
    priority=Priority.WISH,
    groups={"kanban", "management"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://towardsdatascience.com/xgboost-an-intuitive-explanation-88eb32a48eff",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="ML Algorithms List.jpg",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Why do linear SVMs trained on HOG features perform so well?",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="MMOD paper",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Genealogy of Programming Languages.pdf",
    tasks="1",
    priority=Priority.WISH,
    groups={"proglang"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Мозок - це ми.pdf",
    tasks="24",
    priority=Priority.WISH,
    groups={"neuro"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Прекрасный, опасный, кибербезопасный мир.pdf",
    tasks="11",
    priority=Priority.WISH,
    groups={"crypto"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Automated Machine Learning in Action.pdf",
    tasks="9",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Regression Cheatsheet.jpg",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Networks: The Internet and Beyond",
    tasks="1",
    priority=Priority.WISH,
    groups={"web"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="How I Read a Paper: Facebook's DETR (Video Tutorial)",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv", "meta"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="DETR: End-to-End Object Detection with Transformers | Paper Explained",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="DETR: End-to-End Object Detection with Transformers (Paper Explained)",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="DETR Paper arXiv Repo PwC",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="DETR - End to end object detection with transformers (ECCV2020)",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Data: The Past, the Present and the Future",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="CV3DST - Transformers and DETR",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="[Code] How to use Facebook's DETR object detection algorithm in Python (Full Tutorial)",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Emacs Tour",
    tasks="1",
    priority=Priority.WISH,
    groups={"prog_misc"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Ali Baba",
    tasks="9",
    priority=Priority.WISH,
    groups={"ar"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Software Engineering.pdf",
    tasks="25",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Consolidate Learning Scripts & Keyboards and Carácteres y radicales chinos and HSK",
    tasks="1",
    priority=Priority.WISH,
    groups={"language_study"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://en.wikipedia.org/wiki/Template:Design_Patterns_patterns",
    tasks="Abstract factory,Builder,Factory method,Prototype,Singleton,Adapter,Bridge,Composite,Decorator,Facade,Flyweight,Proxy,Chain of responsibility,Command,Interpreter,Iterator,Mediator,Memento,Observer,State,Strategy,Template method,Visitor,Active object,Balking,Binding properties,Double-checked locking,Event-based asynchronous,Guarded suspension,Join,Lock,Monitor,Proactor,Reactor,Read write lock,Scheduler,Thread pool,Thread-local storage,Front controller,Interceptor,MVC,ADR,ECS,n-tier,Specification,Publish–subscribe,Naked objects,Service locator,Active record,Identity map,Data access object,Data transfer object,Inversion of control,Model 2,Broker,Blackboard,Business delegate,Composite entity,Dependency injection,Intercepting filter,Lazy loading,Mock object,Null object,Object pool,Servant,Twin,Type tunnel,Method chaining,Delegation,Anti-pattern,Architectural pattern",
    priority=Priority.WISH,
    groups={"design_patterns"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Элементарное введение в высшую математику.pdf",
    tasks="19",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Computing Systems (Elahi)",
    tasks="10",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Программист-фанатик.pdf",
    tasks="0-5,A",
    priority=Priority.WISH,
    groups={"management", "meta"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Ich denke zu viel",
    tasks="11",
    priority=Priority.WISH,
    groups={"neuro", "psycho"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Вища математика I. Підручник у 2 частинах.pdf",
    tasks="13",
    priority=Priority.WISH,
    groups={"math", "uk"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Episode 10: Deep Neural Networks in Julia with Flux.jl",
    tasks="1",
    priority=Priority.WISH,
    groups={"julia", "dl"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://zsh.sourceforge.io/Guide/zshguide.html",
    tasks="7,A",
    priority=Priority.WISH,
    groups={"shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Street Coder.pdf",
    tasks="9",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Code Complete - A Practical Handbook of Software Construction.pdf",
    tasks="35",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Data Science Design Manual",
    tasks="13",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Практическая статистика для специалистов Data Science.pdf",
    tasks="7",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="GEB 2-3, 5-8",
    tasks="0-20",
    priority=Priority.WISH,
    groups={"misc", "language_study", "multi"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Programming Languages. Programming in C, C++, Scheme, Prolog, g, C#, and SOA",
    tasks="6,A,B,C",
    priority=Priority.WISH,
    groups={"proglang"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Assembly Programming and Computer Architecture for Software Engineers",
    tasks="12,A,B,C,D,E,F,G,H,I",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Computer Science: A Very Short Introduction",
    tasks="8",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Handbook of Data Structures and Applications",
    tasks="67",
    priority=Priority.WISH,
    groups={"dsa"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Encyclopedia of Algorithms",
    tasks="645",
    priority=Priority.WISH,
    groups={"dsa", "alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mastering ML with Python in Six Steps",
    tasks="6",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://numpy.org/doc/stable/reference/c-api/index.html",
    tasks="1",
    priority=Priority.WISH,
    groups={"python", "c"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Самоучитель Python",
    tasks="32",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Mathematical Thinking (Devlin)",
    tasks="4,A",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Разработка конвейеров машинного обучения",
    tasks="0-15,A,B,C",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Tacitus Germania",
    tasks="46",
    priority=Priority.WISH,
    groups={"la"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="write clustering section of ML Cheatsheet & make PR",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Write Great Code 2",
    tasks="17,A",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Write Great Code 1",
    tasks="16,A,B",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Soft Skills",
    tasks="71",
    priority=Priority.WISH,
    groups={"meta"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="O Programador Pragmático",
    tasks="47,A,B",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introducción a los Patrones de Diseño",
    tasks="31",
    priority=Priority.WISH,
    groups={"design_patterns"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Идеальный программист. Как стать профессионалом разработки ПО",
    tasks="0-14,A",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Visual Studio Code. End-To-End...",
    tasks="10",
    priority=Priority.WISH,
    groups={"vscode"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Visual Studio Code Distilled",
    tasks="11",
    priority=Priority.WISH,
    groups={"vscode"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Микросервисы и контейнеры Docker",
    tasks="13,A,B,C",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Совершенный код. Мастер-класс",
    tasks="34,A",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Assimil Hindi",
    tasks="53",
    priority=Priority.WISH,
    groups={"hi"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Cogneethi - Convolutional Neural Networks Basics & Intuitions",
    tasks="17",
    priority=Priority.WISH,
    groups={"cv", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Программирование Cloud Native. Микросервисы, Docker и Kubernetes",
    tasks="0-9",
    priority=Priority.WISH,
    groups={"docker", "kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/vimscript",
    tasks="20",
    priority=Priority.WISH,
    groups={"vim"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Hacking APIs Breaking Web Application Programming Interfaces",
    tasks="16,A,B",
    priority=Priority.WISH,
    groups={"web", "crypto"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Algorithm Design Manual",
    tasks="19",
    priority=Priority.WISH,
    groups={"alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="sed & awk 101 Hacks",
    tasks="13",
    priority=Priority.WISH,
    groups={"shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="GNU sed. Awesome Stream Editor",
    tasks="15",
    priority=Priority.WISH,
    groups={"shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Algorithms",
    tasks="0-35",
    priority=Priority.WISH,
    groups={"alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="First Course in Algorithms through Puzzles",
    tasks="8",
    priority=Priority.WISH,
    groups={"alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Effective awk Programming. Universal Text Processing and Pattern Matching",
    tasks="16,A,B,C",
    priority=Priority.WISH,
    groups={"shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learning Shell Scripting with zsh",
    tasks="6",
    priority=Priority.WISH,
    groups={"shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Sed & Awk",
    tasks="13,A,B,C",
    priority=Priority.WISH,
    groups={"shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Object-Oriented Thought Process",
    tasks="13,A,B,C",
    priority=Priority.WISH,
    groups={"oop"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn Git the Hard Way",
    tasks="25",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Git Essentials",
    tasks="7",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="How Open Source Ate Software",
    tasks="8",
    priority=Priority.WISH,
    groups={"meta", "prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mastering Git. A Beginner's Guide",
    tasks="8",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Practical Git",
    tasks="9",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Advanced Git",
    tasks="11",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Git Version Control Cookbook",
    tasks="12",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Git. Практическое руководство",
    tasks="12",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Professional Git",
    tasks="15",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Beginning Git and Github",
    tasks="19",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="GitHub for Dummies",
    tasks="20",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn Git in a Month of Lunches",
    tasks="20",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mastering Git",
    tasks="22",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Git Notes for Professionals",
    tasks="61",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Git Succinctly",
    tasks="0-7",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Git - Book",
    tasks="10,A3",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Git для профессионального программиста",
    tasks="10A,B,C",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Head First Git",
    tasks="8,A",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Pro Git",
    tasks="9,A",
    priority=Priority.WISH,
    groups={"git"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Чистая архитектура. Искусство разработки программного обеспечения",
    tasks="34",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Kubernetes Book",
    tasks="16,A",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Consciousness: A Very Short Introduction",
    tasks="8",
    priority=Priority.WISH,
    groups={"neuro", "philo"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="What Kind of Computation Is Cognition?",
    tasks="1",
    priority=Priority.WISH,
    groups={"cs", "philo"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Manim tutorial | Introduction: What is Manim?",
    tasks="1",
    priority=Priority.WISH,
    groups={"manim"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Make Videos Like 3Blue1Brown | Manim",
    tasks="1",
    priority=Priority.WISH,
    groups={"manim"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="How 3 Blue 1 Brown makes animations  | Manim Tutorial",
    tasks="1",
    priority=Priority.WISH,
    groups={"manim"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Advice for using Manim | Grant Sanderson and Lex Fridman",
    tasks="1",
    priority=Priority.WISH,
    groups={"manim"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="An Introduction to Information Retrieval",
    tasks="21",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="An Introduction to Language (Fromkin)",
    tasks="10",
    priority=Priority.WISH,
    groups={"ling"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="CRC Handbook of NLP (2010)",
    tasks="26",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="A Practical Introduction to Phonetics",
    tasks="11,A",
    priority=Priority.WISH,
    groups={"ling", "phon"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Acoustic Phonetics",
    tasks="10,A",
    priority=Priority.WISH,
    groups={"ling", "phon"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Articulatory Phonetics",
    tasks="39",
    priority=Priority.WISH,
    groups={"ling", "phon"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Cambridge Handbook of Formal Semantics",
    tasks="25",
    priority=Priority.WISH,
    groups={"ling", "semantics"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Comprehensive Articulatory Phonetics",
    tasks="36,A",
    priority=Priority.WISH,
    groups={"ling", "phon"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Dictionary of Linguistics and Phonetics",
    tasks="9",
    priority=Priority.WISH,
    groups={"ling", "phon"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Elements of Acoustical Phonetics",
    tasks="11",
    priority=Priority.WISH,
    groups={"ling", "phon"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Elements of Formal Semantics",
    tasks="7",
    priority=Priority.WISH,
    groups={"ling", "semantics"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Embedding of Semantic Predications",
    tasks="1",
    priority=Priority.WISH,
    groups={"ling", "semantics"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Linguistic Fundamentals for NLP",
    tasks="103",
    priority=Priority.WISH,
    groups={"ling", "nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="A Novel Method of Extracting Topological Features from Word Embeddings",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp", "topo"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Essentials of Linguistics (Anderson)",
    tasks="87",
    priority=Priority.WISH,
    groups={"ling"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="go through https://cs-k.it/master/lecture/Grundlagen-der-Automatischen-Spracherkennung.html",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Head First Data Analysis",
    tasks="13,A3",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Artificial Intelligence",
    tasks="15",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Language (Yule)",
    tasks="20,A",
    priority=Priority.WISH,
    groups={"ling"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Langage naturel (résumé)",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Mathematical Linguistics",
    tasks="10",
    priority=Priority.WISH,
    groups={"ling", "math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mathematics of Language",
    tasks="21,A2",
    priority=Priority.WISH,
    groups={"ling", "math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="АВТОМАТИЧЕСКАЯ ОБРАБОТКА ТЕКСТОВ. ЗАДАЧИ, ПОДХОДЫ,  РЕСУРСЫ",
    tasks="1",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="NLP06) Natural Language Processing with PyTorch",
    tasks="9",
    priority=Priority.WISH,
    groups={"nlp", "pytorch"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP06) Знакомство с PyTorch",
    tasks="9",
    priority=Priority.WISH,
    groups={"nlp", "pytorch"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Oxford Handbook of CL and NLP (2010)",
    tasks="22",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP20) Oxford Handbook of Computational Linguistics",
    tasks="38,A",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP25) Speech and Audio Signal Processing. Processing and Perception of Speech and Music",
    tasks="42",
    priority=Priority.WISH,
    groups={"nlp", "sp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP17) Text-to-Speech Synthesis",
    tasks="18,A4",
    priority=Priority.WISH,
    groups={"nlp", "sp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP16) Automatic Speech Recognition - A Deep Learning Approach",
    tasks="15",
    priority=Priority.WISH,
    groups={"nlp", "sp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP21) Handbook of Computational Linguistics and Natural Language Processing",
    tasks="22",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP22) Spoken Language Processing",
    tasks="13",
    priority=Priority.WISH,
    groups={"nlp", "sp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP19) Applied Text Analysis with Python",
    tasks="12,A",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP23) Text Mining with R. a Tidy Approach",
    tasks="9",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Psycholinguistics - The Key Concepts",
    tasks="13",
    priority=Priority.WISH,
    groups={"ling", "neuro"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Routledge Handbook of Semantics",
    tasks="29",
    priority=Priority.WISH,
    groups={"nlp", "semantics"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Using Praat for Linguistic Research (Styler)",
    tasks="13",
    priority=Priority.WISH,
    groups={"ling", "phon"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP11) Deep Learning in Natural Language Processing",
    tasks="11",
    priority=Priority.WISH,
    groups={"nlp", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP24) Text Mining in Practice with R",
    tasks="9",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="NLP05) Foundations of Statistical Natural Language Processing",
    tasks="16",
    priority=Priority.WISH,
    groups={"nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Sounds of the World's Languages",
    tasks="11",
    priority=Priority.WISH,
    groups={"ling", "phon"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Document Image Analysis. Current Trends and Challenges in Graphics Recognition",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://github.com/doc-analysis",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Rich feature hierarchies for accurate object detection and semantic segmentation",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Fast R-CNN",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Fast R-CNN Slides",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Faster R-CNN. Towards Real-Time Object Detection with Region Proposal Networks",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Mask R-CNN",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Mask RCNN - How it Works - Intuition Tutorial | OpenCV Python | Computer Vision 2020",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://learnopencv.com/create-snapchat-instagram-filters-using-mediapipe/",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://learnopencv.com/deep-learning-based-object-detection-using-yolov3-with-opencv-python-c/",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://www.learnopencv.com/wp-content/uploads/2020/05/Computer-Vision-Resources",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Mask RCNN - How it Works - Intuition Tutorial | OpenCV Python | Computer Vision 2020",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Vision Transformer in PyTorch",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Advanced Computer Vision with Python - Full Course",
    tasks="14",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Artificial Intelligence Programming with Python",
    tasks="12",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://omdena.com/blog/computer-vision-projects-github/",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Lecture 11 | Detection and Segmentation",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="DETR: End-to-End Object Detection with Transformers (Paper Explained)",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://learnopencv.com/deep-learning-based-text-recognition-ocr-using-tesseract-and-opencv/",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://learnopencv.com/multi-person-pose-estimation-in-opencv-using-openpose/",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://homepages.inf.ed.ac.uk/rbf/HIPR2/guidecon.htm",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Lecture 11 | Detection and Segmentation",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Vision Transformer in PyTorch",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://www.width.ai/post/facial-detection-and-recognition-with-dlib",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://learnopencv.com/convolutional-neural-network-based-image-colorization-using-opencv/",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://github.com/spmallick/learnopencv/blob/master/README.md?ck_subscriber_id=1680684172",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Fast R-CNN Slides",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="DETR: End-to-End Object Detection with Transformers (Paper Explained)",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Computer Vision. A Reference Guide",
    tasks="321",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Wikipedia Computer Vision",
    tasks="31",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Hands-On Computer Vision with Julia ",
    tasks="8",
    priority=Priority.WISH,
    groups={"cv", "julia"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Convolutional Neural Networks (Course 4 of the Deep Learning Specialization)",
    tasks="42",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mastering Computer Vision with TensorFlow 2.x",
    tasks="12",
    priority=Priority.WISH,
    groups={"cv", "tf", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="OCR with OpenCV, Tesseract, and Python",
    tasks="21",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Practical Machine Learning for Computer Vision",
    tasks="12",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learning OpenCV 4 Computer Vision with Python 3",
    tasks="10,A",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Lecture Collection | Convolutional Neural Networks for Visual Recognition (Spring 2017)",
    tasks="16",
    priority=Priority.WISH,
    groups={"cv", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="OCR with OpenCV, Tesseract, and Python - Intro to OCR",
    tasks="20",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Learning for Vision Systems",
    tasks="10",
    priority=Priority.WISH,
    groups={"cv", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Learning in Computer Vision",
    tasks="11",
    priority=Priority.WISH,
    groups={"cv", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Domain Adaptation in Computer Vision with Deep Learning",
    tasks="13",
    priority=Priority.WISH,
    groups={"cv", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Handbook of Image Processing and Computer Vision. Volume 1. From Energy to Image",
    tasks="9",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="PyTorch Computer Vision Cookbook",
    tasks="10",
    priority=Priority.WISH,
    groups={"cv", "pytorch"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="TensorFlow 2.0 Computer Vision Cookbook",
    tasks="12",
    priority=Priority.WISH,
    groups={"cv", "tf"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Биологическое и компьютерное зрение",
    tasks="10",
    priority=Priority.WISH,
    groups={"cv"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Practical Docker with Python",
    tasks="7",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Docker Handbook",
    tasks="10",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Descomplicando o Docker",
    tasks="12",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mastering Docker",
    tasks="13",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="BIOS.djvu",
    tasks="15",
    priority=Priority.WISH,
    groups={"os", "linux", "low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn Docker in a Month of Lunches",
    tasks="22",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Docker Succinctly",
    tasks="9",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Desconstruindo a Web",
    tasks="10",
    priority=Priority.WISH,
    groups={"web"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Docker in Action",
    tasks="13",
    priority=Priority.HIGHER,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Aprendizaje Docker",
    tasks="37",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Docker на практике",
    tasks="16,A,B",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Docker in Practice",
    tasks="16,A,B,C",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Docker Deep Dive",
    tasks="17,A,B,C",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Docker para Desenvolvedores",
    tasks="25,A",
    priority=Priority.WISH,
    groups={"docker"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Scrum Shortcuts without Cutting Corners",
    tasks="10",
    priority=Priority.WISH,
    groups={"agile", "management"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The GNU Make Book",
    tasks="6",
    priority=Priority.WISH,
    groups={"make", "prog_misc"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="A Course in Formal Languages, Automata, and Groups (Chiswell)",
    tasks="5,A",
    priority=Priority.WISH,
    groups={"compiler", "cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Sistemas computacionales",
    tasks="13",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://justinmeiners.github.io/lc3-vm/",
    tasks="15",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Category Theory for Computing Science",
    tasks="16",
    priority=Priority.WISH,
    groups={"cs", "functional", "math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://makefiletutorial.com/",
    tasks="1",
    priority=Priority.HIGHER,
    groups={"make"},
    start=zero_date - 1,
    interval=1,
    cluster=1,
)
g.add_project(
    name="GNU Make Manual",
    tasks="16,A,B,C,D,E,F",
    priority=Priority.WISH,
    groups={"make"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Rust Book",
    tasks="20,a,B,C,D,E,F",
    priority=Priority.WISH,
    groups={"rust"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Logic Circuits and Logic Design with VHDL",
    tasks="13,A,B",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Grundkurs Codierung Verschlüsselung, Kompression und Fehlerbeseitigung",
    tasks="6,a,B",
    priority=Priority.WISH,
    groups={"crypto"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Linux Kernel in a Nutshell",
    tasks="11,A,B",
    priority=Priority.WISH,
    groups={"low_level", "systems", "os"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Low-Level Programming",
    tasks="22",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Web Development for Beginners",
    tasks="23",
    priority=Priority.WISH,
    groups={"web"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Компиляторы",
    tasks="12,A9",
    priority=Priority.WISH,
    groups={"compiler"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Ensamblador",
    tasks="5",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Kryptologie Eine Einführung in die Wissenschaft vom Verschlüsseln, Verbergen und Verheimlichen",
    tasks="6",
    priority=Priority.WISH,
    groups={"crypto"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Scientific Computing. A Historical Perspective",
    tasks="6",
    priority=Priority.WISH,
    groups={"cs", "history"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Bases de datos",
    tasks="7",
    priority=Priority.WISH,
    groups={"db"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="How to Design, Build, & Program Your Own Working Computer System",
    tasks="8",
    priority=Priority.WISH,
    groups={"cs", "low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Cryptography Algorithms",
    tasks="9",
    priority=Priority.WISH,
    groups={"crypto"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Fundamentos físicos de la informática",
    tasks="9",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Exploring the Early Digital",
    tasks="10",
    priority=Priority.WISH,
    groups={"cs", "history"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="How Cybersecurity Really Works",
    tasks="10",
    priority=Priority.WISH,
    groups={"crypto"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="PostgreSQL. Основы языка SQL",
    tasks="10",
    priority=Priority.WISH,
    groups={"db"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Programming with POSIX threads",
    tasks="10",
    priority=Priority.WISH,
    groups={"low_level", "concurrency"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Beginning PostgresQL on the Cloud",
    tasks="12",
    priority=Priority.WISH,
    groups={"db"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Scala Book",
    tasks="12",
    priority=Priority.WISH,
    groups={"scala"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Real-World Cryptography",
    tasks="16",
    priority=Priority.WISH,
    groups={"crypto"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="An Introduction to Formal Languages and Automata",
    tasks="14,A,B",
    priority=Priority.WISH,
    groups={"cs", "compiler"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Основы технологий баз данных",
    tasks="22,A",
    priority=Priority.WISH,
    groups={"db"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Digital Computer Electronics",
    tasks="24,A",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Прикладная криптография",
    tasks="25,A9",
    priority=Priority.WISH,
    groups={"crypto"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Happy Learn Haskell",
    tasks="23",
    priority=Priority.WISH,
    groups={"haskell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Five Lines of Code",
    tasks="0-14",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Haskell Report",
    tasks="0-40",
    priority=Priority.WISH,
    groups={"haskell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Assembly Language Step-by-Step. Programming with Linux",
    tasks="13,A,B",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="How to Build a Working Digital Computer",
    tasks="7,A",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Essentials of Programming Languages",
    tasks="9,A,B",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Intro to Automata Theory, Languages, and Computation (Hopcroft)",
    tasks="14",
    priority=Priority.WISH,
    groups={"compiler", "cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Lenguaje ensamblador y programación para IBM PC y compatibles",
    tasks="15",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mastering MySQL for Web. A Beginner's Guide",
    tasks="6",
    priority=Priority.WISH,
    groups={"db", "web"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Tour of Scala",
    link="https://docs.scala-lang.org/tour/tour-of-scala.html",
    tasks="1",
    priority=Priority.WISH,
    groups={"scala"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="UNIX Network Programming, Volume 1. The Sockets Networking API",
    link="https://github.com/sqm2050/wiki/blob/master/Books/c%26programme/UNIX%20Network%20Programming%2C%20Volume%201%2C%20Third%20Edition%2C%20The%20Sockets%20Networking%20API.pdf",
    tasks="31,A5",
    priority=Priority.WISH,
    groups={"prog_misc", "low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Web Security for Developers",
    tasks="18",
    priority=Priority.WISH,
    groups={"web", "crypto"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Yet Another Haskell Tutorial",
    tasks="10,A,B,C",
    priority=Priority.WISH,
    groups={"haskell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Алгебраические основы криптографии",
    tasks="7",
    priority=Priority.WISH,
    groups={"crypto", "math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Scalability Patterns",
    tasks="6",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Algorithms, Languages, Automata, and Compilers",
    tasks="11",
    priority=Priority.WISH,
    groups={"alg", "compiler", "cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Refactoring at Scale",
    tasks="11",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Art of Assembly Language Programming",
    tasks="12",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Програмування мовою асемблера. Навчальний посібник",
    tasks="12",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Scalability Rules",
    tasks="13",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Secure by Design",
    tasks="14",
    priority=Priority.WISH,
    groups={"prog", "crypto"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Annotated Turing",
    tasks="18",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Art of 64-Bit Assembly",
    tasks="16,A,B,C,D,E",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="GNU Emacs Manual",
    tasks="24",
    priority=Priority.WISH,
    groups={"prog_misc"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Профессиональное программирование на ассемблере x64 с расширениями",
    tasks="0-16",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Программирование на ассемблере х64. От начального уровня до профессионального",
    tasks="0-43",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Code Reading. The Open Source Perspective",
    tasks="11,A,B,C,D,E",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Алгоритмы и модели вычисления",
    tasks="6",
    priority=Priority.WISH,
    groups={"alg", "cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Изучение сложных систем с помощью Python",
    tasks="12",
    priority=Priority.WISH,
    groups={"python" "ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Математические основы информатики",
    tasks="6,A",
    priority=Priority.WISH,
    groups={"math", "cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Сетевые технологии. Основы веб дизайна",
    tasks="3",
    priority=Priority.WISH,
    groups={"web"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Assembler Lernen - Tutorial Deutsch",
    tasks="18",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Fundamentals of Computer Architecture and Design",
    tasks="8,A",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="1400 задач по программированию",
    tasks="14,A,B,C",
    priority=Priority.WISH,
    groups={"prog", "alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Compiler Design",
    tasks="11",
    priority=Priority.WISH,
    groups={"compiler"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Kubernetes Succinctly",
    tasks="9",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Cloud Native DevOps with Kubernetes (2019)",
    tasks="12",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Kubernetes – An Enterprise Guide",
    tasks="14",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Cloud Native DevOps with Kubernetes",
    tasks="16",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Kubernetes лучшие практики",
    tasks="18",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn Kubernetes in a Month of Lunches",
    tasks="22,A,B,C,D",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Kubernetes Patterns",
    tasks="25,A",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Networking and Kubernetes",
    tasks="6",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Diving Deep into Kubernetes Networking",
    tasks="9",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="97 Etudes RU",
    tasks="97",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learn Helm",
    tasks="9",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learning Helm",
    tasks="8",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Linux в действии",
    tasks="16",
    priority=Priority.WISH,
    groups={"linux"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Seriously Good Software",
    tasks="9",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Scala Programming Projects",
    tasks="11",
    priority=Priority.WISH,
    groups={"scala"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Scala Design Patterns",
    tasks="12",
    priority=Priority.WISH,
    groups={"scala"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mastering RabbitMQ",
    tasks="11",
    priority=Priority.WISH,
    groups={"kubernetes"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Betriebssysteme (zweisprachig)",
    tasks="10,A",
    priority=Priority.WISH,
    groups={"low_level", "os"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to the Theory of Formal Languages and Automata (Levelt)",
    tasks="9,A",
    priority=Priority.WISH,
    groups={"cs", "compiler"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learning Algorithms Through Programming and Puzzle Solving",
    tasks="9,A",
    priority=Priority.WISH,
    groups={"alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Грокаем алгоритмы",
    tasks="11",
    priority=Priority.WISH,
    groups={"alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Объектно-ориентированный подход",
    tasks="12",
    priority=Priority.WISH,
    groups={"oop"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Real-Time Operating Systems Book 1. The Theory",
    tasks="13",
    priority=Priority.WISH,
    groups={"os", "low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Cloud Computing (Ruparelia)",
    tasks="12",
    priority=Priority.WISH,
    groups={"cloud"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Cloud Computing Theory and Practice",
    tasks="13",
    priority=Priority.WISH,
    groups={"cloud"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Implementing Programming Languages. An Introduction to Compilers and Interpreters",
    tasks="8,A,B,C,D",
    priority=Priority.WISH,
    groups={"proglang", "compiler"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="О криптографии всерьез",
    tasks="14",
    priority=Priority.WISH,
    groups={"crypto"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Handbuch für Softwareentwickler",
    tasks="20",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Алгоритмы. Построение и анализ",
    tasks="35,A4",
    priority=Priority.WISH,
    groups={"alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Foundations of Computer Science",
    tasks="14",
    priority=Priority.WISH,
    groups={"cs"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Arquitectura de computadores",
    tasks="10,A,B,C,D,E",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to the Design and Analysis of Algorithms",
    tasks="13,A,B",
    priority=Priority.WISH,
    groups={"alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Алгоритмы для начинающих",
    tasks="16",
    priority=Priority.WISH,
    groups={"alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/video_galleries/lecture-videos/",
    tasks="23",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Linux API. Исчерпывающее руководство",
    tasks="60",
    priority=Priority.WISH,
    groups={"linux", "low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Algorithmen und Datenstrukturen (Sedgewick 2014)",
    tasks="6",
    priority=Priority.WISH,
    groups={"dsa", "alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Compilers (Aho et al. 2E)",
    tasks="12,A,B",
    priority=Priority.WISH,
    groups={"compiler"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Linguaggi di Programmazione",
    tasks="16",
    priority=Priority.WISH,
    groups={"proglang"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Algoritmi. Lo spirito dell'informatica",
    tasks="17",
    priority=Priority.WISH,
    groups={"alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Types and Programming Languages",
    tasks="32,A,B",
    priority=Priority.WISH,
    groups={"proglang"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Algorytmy, struktury danych i techniki programowania",
    tasks="14,A,B,C",
    priority=Priority.WISH,
    groups={"dsa", "alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Operating System - YouTube",
    tasks="29",
    priority=Priority.WISH,
    groups={"os", "low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Structure and Interpretation of Computer Programs",
    tasks="5",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Programming Languages. Principles and Paradigms (Noonan and Tucker)",
    tasks="18",
    priority=Priority.WISH,
    groups={"proglang"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="CS 377 Spring '14: Operating Systems - YouTube",
    tasks="23",
    priority=Priority.WISH,
    groups={"os"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Compiladores y interpretes",
    tasks="10",
    priority=Priority.WISH,
    groups={"compiler"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Compiladores 2e",
    tasks="12,A,B",
    priority=Priority.WISH,
    groups={"compiler"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Compilers",
    tasks="0-37,A,B,C,D,E,F",
    priority=Priority.WISH,
    groups={"compiler"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Computer Systems (Elahi)",
    tasks="10,A",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Inside the Machine - An Illustrated Guide",
    tasks="12",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Fundamentals of Software Architecture",
    tasks="24",
    priority=Priority.WISH,
    groups={"prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Electronic Digital System Fundamentals",
    tasks="11,A,B,C",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Графовые алгоритмы",
    tasks="8",
    priority=Priority.WISH,
    groups={"alg"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Processor Microarchitecture",
    tasks="8",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Вычислительные системы и ассемблер.djvu",
    tasks="7",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Введение в рекурсивное программирование",
    tasks="12",
    priority=Priority.WISH,
    groups={"alg", "prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Structured Computer Organization",
    tasks="9,A,B,C",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Человеческий фактор успешные проекты и команды",
    tasks="26",
    priority=Priority.WISH,
    groups={"management", "prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/x86-64-assembly/",
    tasks="17",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Arquitetura e organização de computadores (Stallings)",
    tasks="21,A,B,C",
    priority=Priority.WISH,
    groups={"low_level"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Advanced Topics in Types and Programming Languages",
    tasks="10",
    priority=Priority.WISH,
    groups={"proglang"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/lua",
    tasks="82",
    priority=Priority.WISH,
    groups={"lua"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/ocaml",
    tasks="44",
    priority=Priority.LOW,
    groups={"ocaml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/wasm",
    tasks="21",
    priority=Priority.WISH,
    groups={"wasm"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/kotlin",
    tasks="85",
    priority=Priority.WISH,
    groups={"kotlin"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/haskell",
    tasks="96",
    priority=Priority.WISH,
    groups={"haskell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="ix Developer - Machine Learning",
    tasks="10",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Modern C Quick Syntax Reference",
    tasks="10",
    priority=Priority.WISH,
    groups={"c"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="A survey of transformers",
    tasks="10",
    priority=Priority.WISH,
    groups={"transformer", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Transformers for Machine Learning. A Deep Dive",
    tasks="10",
    priority=Priority.WISH,
    groups={"transformer", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Вища математика II. Підручник у 2 частинах",
    tasks="9",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Artin - Algebra",
    tasks="14,A",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Algebra, Topology, Differential Calculus, and Optimization Theory for Computer Science and Machine Learning",
    tasks="17,A,B,C",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Pure Mathematics for Beginners. A Rigorous Introduction to Logic, Set Theory, Abstract Algebra, Number Theory, Real Analysis, Topology, Complex Analysis, and Linear Algebra",
    tasks="16",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="ACME: Foundations of Applied Mathematics, Volume 2. Algorithms, Approximation, Optimization",
    tasks="17,A",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="ACME: Labs I",
    tasks="18",
    priority=Priority.WISH,
    groups={"math", "ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="ACME: Labs II",
    tasks="21",
    priority=Priority.WISH,
    groups={"math", "ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="ACME: Data Science Essentials →",
    tasks="16",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="ACME: Foundations of Applied Mathematics, Volume 1. Mathematical Analysis",
    tasks="15,A,B,C,D",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="ACME: Python Essentials",
    tasks="11",
    priority=Priority.WISH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="ACME: README",
    tasks="1",
    priority=Priority.WISH,
    groups={"math", "ds"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="PyTorch Recipes",
    tasks="7",
    priority=Priority.WISH,
    groups={"dl", "pytorch"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Глубокое обучение",
    tasks="20",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="PyTorch Deep Learning Hands-On",
    tasks="8",
    priority=Priority.WISH,
    groups={"pytorch"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Foundations Of Data Science (2020)",
    tasks="12",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Hands-On Machine Learning with Scikit-Learn and TensorFlow",
    tasks="19,A7",
    priority=Priority.WISH,
    groups={"ml", "tf", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Learning with TensorFlow 2 and Keras",
    tasks="16",
    priority=Priority.WISH,
    groups={"dl", "tf"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Learning. From Basics to Practice. Volume 1 (Glassner 2022)",
    tasks="30",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Learning. From Basics to Practice. Volume 2 (Glassner 2022)",
    tasks="30",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Machine Learning (Alpaydin 4e)",
    tasks="20,A,B",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learning Deep Learning",
    tasks="18,A10",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Основы искусственного интеллекта в примерах на Python",
    tasks="8,A",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The TensorFlow Workshop",
    tasks="11",
    priority=Priority.WISH,
    groups={"tf"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Programming Machine Learning. From Coding to Deep Learning",
    tasks="20,A2",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Applied Deep Learning with TensorFlow 2",
    tasks="20,A2",
    priority=Priority.WISH,
    groups={"tf"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Artificial Intelligence with Python. Your complete guide to building intelligent apps using Python 3.x and TensorFlow 2",
    tasks="23",
    priority=Priority.WISH,
    groups={"ml", "tf"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Machine Learning mit Python",
    tasks="18",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Generative Deep Learning",
    tasks="10",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Learning with PyTorch",
    tasks="15",
    priority=Priority.WISH,
    groups={"pytorch", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Mastering PyTorch",
    tasks="14",
    priority=Priority.WISH,
    groups={"pytorch", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Learning with Python. Learn Best Practices of Deep Learning Models with PyTorch",
    tasks="8",
    priority=Priority.WISH,
    groups={"pytorch", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="AI and Machine Learning for Coders",
    tasks="20",
    priority=Priority.WISH,
    groups={"pytorch", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="PyTorch Artificial Intelligence Fundamentals",
    tasks="8",
    priority=Priority.WISH,
    groups={"pytorch", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Deep Learning with PyTorch Workshop",
    tasks="6",
    priority=Priority.WISH,
    groups={"pytorch", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Inside Deep Learning",
    tasks="14",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://github.com/yunjey/pytorch-tutorial",
    tasks="14",
    priority=Priority.WISH,
    groups={"pytorch", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="TensorFlow 2 Pocket Reference: Building and Deploying Machine Learning Models",
    tasks="10",
    priority=Priority.WISH,
    groups={"tf", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Developing Analytic Talent",
    tasks="8",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Machine Learning Bookcamp",
    tasks="9",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Machine Learning (Flach)",
    tasks="12,A2",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Machine Learning Refined",
    tasks="14,A,B,C",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Machine Learning. An Algorithmic Perspective",
    tasks="18,A4",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="scikit-learn Cookbook",
    tasks="12",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="An Overview of Statistical Learning Theory",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Deep Learning Approaches for Low-Resource Natural Language Processing",
    tasks="10",
    priority=Priority.WISH,
    groups={"nlp", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Statistical Learning Theory Notes (Liang)",
    tasks="7,A",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learning from Data",
    link="https://work.caltech.edu/telecourse",
    tasks="18",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Introduction to Applied Linear Algebra Julia Companion",
    link="https://web.stanford.edu/~boyd/vmls/vmls-julia-companion.pdf",
    tasks="19,A",
    priority=Priority.WISH,
    groups={"math", "ds", "julia"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Statistics with Julia",
    tasks="10,A,B,C",
    priority=Priority.WISH,
    groups={"julia", "ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Julia for Data Science",
    tasks="11",
    priority=Priority.WISH,
    groups={"julia", "ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Flux.jl Docs",
    tasks="25",
    priority=Priority.WISH,
    groups={"julia", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Data Science. Concepts and Practice",
    tasks="15",
    priority=Priority.MEDIUM_HIGH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Data Science at the Command Line",
    tasks="10,A",
    priority=Priority.WISH,
    groups={"ds", "shell"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Doing Data Science",
    tasks="16",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="DL Technical Intro",
    tasks="3-7",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Антология машинного обучения. Важнейшие исследования в области ИИ.epub",
    tasks="18",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Крупномасштабное машинное обучение вместе с Python",
    tasks="9,A",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Building Machine Learning Pipelines",
    tasks="15,A,B,C",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Data science для карьериста",
    tasks="16",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Data Science Handbook (Shan et al.)",
    tasks="25",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Data Science Handbook (Cady)",
    tasks="25",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Pragmatic AI",
    tasks="11,A,B",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Learning (Goodfellow et al., 2016)",
    tasks="20",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Elements of Statistical Learning",
    tasks="18",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Machine Learning (Alpaydin 2020)",
    tasks="8,A",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Algorithms for Data Science",
    tasks="12,A,B",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Handbook of Data Intensive Computing",
    tasks="30",
    priority=Priority.LOWER,
    groups={"ds", "prog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Data Mining (Aggarwal)",
    tasks="20",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Understanding Complex Datasets",
    tasks="10,A",
    priority=Priority.WISH,
    groups={"ds", "ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Spark: The Definitive Guide (Chambers & Zaharia)",
    tasks="33",
    priority=Priority.WISH,
    groups={"ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Using MPI: Portable Parallel Programming with the Message-Passing Interface by (Gropp, Lusk, and Skjellum)",
    tasks="10,A,B,C",
    priority=Priority.WISH,
    groups={"hpc"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Programming Massively Parallel Processors (Kirk and Hwu)",
    tasks="21,A,B",
    priority=Priority.WISH,
    groups={"hpc"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="CUDA for Engineers (Storti & Yurtoglu)",
    tasks="9,A,B,C,D",
    priority=Priority.WISH,
    groups={"hpc"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Fundamentals of Machine Learning for Predictive Data Analysis",
    tasks="14,A,B,C,D",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Probabilistic Machine Learning. Advanced Topics - Supplementary Materials",
    tasks="36",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Probabilistic Machine Learning. Advanced Topics",
    tasks="36",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Kaggle Book",
    tasks="14",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Data Clustering",
    tasks="24",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Practical Machine Learning. A New Look at Anomaly Detection",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Practical Machine Learning. Innovations in Recommendation",
    tasks="1",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Анализ данных в науке и технике",
    tasks="12,A",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Как вытащить из данных максимум. Навыки аналитики для неспециалистов",
    tasks="11",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Разработка беспилотных транспортных средств",
    tasks="11,A",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Глубокое обучение с подкреплением на Python. OpenAI Gym и TensorFlow для профи",
    tasks="13",
    priority=Priority.WISH,
    groups={"dl", "tf"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Глубокое обучение с подкреплением",
    tasks="17,A,B",
    priority=Priority.WISH,
    groups={"rl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Reinforcement Learning. Das umfassende Praxis-Handbuch",
    tasks="25",
    priority=Priority.WISH,
    groups={"rl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Алгоритмы обучения с подкреплением на Python",
    tasks="13",
    priority=Priority.WISH,
    groups={"rl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Learning for Robot Perception and Cognition",
    tasks="21",
    priority=Priority.WISH,
    groups={"rl", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="R Deep Learning. Essentials",
    tasks="11",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Scaling Up Machine Learning. Parallel and Distributed Approaches",
    tasks="21",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Машинное обучение: алгоритмы для бизнеса",
    tasks="22,A,B,C",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Machine Learning and Data Science Blueprints for Finance",
    tasks="10",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Artificial Intelligence (Norvig)",
    tasks="28,A,B",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Linear Algebra and Learning from Data",
    tasks="I.1,I.2,I.3,I.4,I.5,I.6,I.7,I.8,I.9,I.10,I.11,I.12,II.1,II.2,II.3,II.4,III.1,III.2,III.3,III.4,III.5,IV.1,IV.2,IV.3,IV.4,IV.5,IV.6,IV.7,IV.8,IV.9,IV.10,V.1,V.2,V.3,V.4,V.5,V.6,VI.1,VI.2,VI.3,VI.4,VI.5,VII.1,VII.2,VII.3,VII.4,VII.5,A,B,C,D",
    priority=Priority.WISH,
    groups={"ml", "math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Aprender Noruego",
    tasks="5-36",
    priority=Priority.WISH,
    groups={"no"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="> 100 frases positivas + cumplidos - Noruego + Español - (Hablante nativo)",
    tasks="100",
    priority=Priority.WISH,
    groups={"no"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Imparare 200 frasi in Cinese",
    tasks="200",
    priority=Priority.WISH,
    groups={"zh"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="(2024) Word Translation Graph Project",
    tasks="1",
    priority=Priority.WISH,
    groups={"language_study", "multi"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="(2024) Modismos diversos (borrador)",
    tasks="1",
    priority=Priority.WISH,
    groups={"language_study", "multi"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="(2024) Database of Figurative Language",
    tasks="1",
    priority=Priority.WISH,
    groups={"language_study", "multi"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Argot - review and plan",
    tasks="1",
    priority=Priority.WISH,
    groups={"language_study", "multi"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="(2024)Wikiquote",
    tasks="1",
    priority=Priority.WISH,
    groups={"language_study", "multi"},
    start=Date(2024, 1, 1),
    interval=1,
    cluster=1,
)
g.add_project(
    name="Parallel Translations Projects - review & plan",
    tasks="1",
    priority=Priority.WISH,
    groups={"language_study", "multi"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Proverbs Project - review and plan",
    tasks="1",
    priority=Priority.WISH,
    groups={"language_study", "multi"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://zh.wikipedia.org/wiki/深度学习",
    tasks="1",
    priority=Priority.WISH,
    groups={"zh"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="https://zh.wikipedia.org/wiki/计算机科学",
    tasks="1",
    priority=Priority.WISH,
    groups={"zh"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="> Aprender Idiomas con Chris",
    tasks="1",
    priority=Priority.WISH,
    groups={"language_study", "multi"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Assimil Ancient Greek",
    tasks="50,A",
    priority=Priority.WISH,
    groups={"grc"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Assimil HI",
    tasks="53",
    priority=Priority.WISH,
    groups={"hi"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="> Assimil HR",
    tasks="50",
    priority=Priority.WISH,
    groups={"hr"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="> Assimil PL",
    tasks="1",
    priority=Priority.WISH,
    groups={"pl"},
    start=Date(2024, 1, 1),
    interval=1,
    cluster=1,
)
g.add_project(
    name="> Assimil ZH",
    tasks="101",
    priority=Priority.WISH,
    groups={"zh"},
    start=Date(2023, 3, 1) + 90,
    end=Date(2023, 3, 1) + 150,
    cluster=1,
)
g.add_project(
    name="> Build Your Arabic Vocabulary",
    tasks="16",
    priority=Priority.WISH,
    groups={"ar"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="> https://archive.org/details/AssimilArabicWithEase",
    tasks="41",
    priority=Priority.WISH,
    groups={"ar"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="(2024) Modismos diversos (borrador)",
    tasks="1",
    priority=Priority.WISH,
    groups={"language_study", "multi"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="(2024) Assimil NL",
    tasks="1",
    priority=Priority.WISH,
    groups={"nl"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="200 frases - Télugu - Español",
    tasks="200",
    priority=Priority.WISH,
    groups={"hi"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="R in a Nutshell",
    tasks="26,A",
    priority=Priority.WISH,
    groups={"r"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="The Art of R Programming",
    tasks="16,A,B",
    priority=Priority.WISH,
    groups={"r"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Systems Programming in Unix/Linux",
    tasks="14",
    priority=Priority.WISH,
    groups={"linux", "low_level", "os"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Learning (Aggarwal)",
    tasks="10",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Learning Perl the Hard Way",
    tasks="6",
    priority=Priority.WISH,
    groups={"perl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/prolog",
    tasks="19",
    priority=Priority.WISH,
    groups={"prolog"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/perl5",
    tasks="62",
    priority=Priority.WISH,
    groups={"perl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/rust",
    tasks="103",
    priority=Priority.WISH,
    groups={"rust"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Data Science with Julia",
    tasks="7,A,B,C,D,E",
    priority=Priority.WISH,
    groups={"julia"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Artificial Intelligence, Machine Learning, and Deep Learning (Campesato)",
    tasks="6,A,B,C",
    priority=Priority.WISH,
    groups={"ml", "dl", "tf"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Learning in Natural Language Processing",
    tasks="11,A",
    priority=Priority.WISH,
    groups={"dl", "nlp"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Machine Learning: A Bayesian and Optimization Perspective",
    tasks="19,A,B,C",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Linear Algebra and Optimization for Machine Learning: A Textbook",
    tasks="11",
    priority=Priority.WISH,
    groups={"ml", "math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Alebra, Topology, Differential Calculus, and Optimization Theory for Computer Science and Machine Learning",
    tasks="56,A,B,C",
    priority=Priority.WISH,
    groups={"math"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Machine Learning: A Probabilistic Perspective",
    tasks="28,A",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Probabilistic Machine Learning: An Introduction",
    tasks="23,A",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Deep Learning. A Visual Approach (Glassner)",
    tasks="23",
    priority=Priority.WISH,
    groups={"dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Getting Started with Artificial Intelligence",
    tasks="7",
    priority=Priority.WISH,
    groups={"ml"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Beginning Perl Programming",
    tasks="14",
    priority=Priority.WISH,
    groups={"perl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Beginning Rust",
    tasks="24",
    priority=Priority.WISH,
    groups={"rust"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Why Flux? The Elegant Julia Machine Learning Library",
    tasks="1",
    priority=Priority.WISH,
    groups={"julia", "dl"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Intro to Applied Linear Algebra",
    tasks="19,A,B,C,D",
    link="https://web.stanford.edu/~boyd/vmls/vmls.pdf",
    priority=Priority.WISH,
    groups={"math", "ds"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Однострочники Python лаконичный и содержательный код",
    tasks="6",
    priority=Priority.HIGH,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Architcture Patterns with Python",
    tasks="13,A,B,C,D,E",
    priority=Priority.HIGHER,
    groups={"python", "design_patterns"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Efektywny Python 59 sposobow na lepszy kod",
    tasks="59",
    priority=Priority.HIGHER,
    groups={"python"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Programming Rust. Fast, Safe Systems Development",
    tasks="23",
    priority=Priority.HIGHER,
    groups={"rust"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Программирование на Rust. Официальный гайд от команды разработчиков",
    tasks="20,A5",
    priority=Priority.HIGHER,
    groups={"rust"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Java и OpenCV",
    tasks="5",
    priority=Priority.WISH,
    groups={"cv", "java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Программирование на Java для начинающих.pdf",
    tasks="0-18",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://www.analyticsinsight.net/top-10-java-projects-that-beginners-should-master-in-2022/",
    tasks="1",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Sams Teach Yourself Java in 24 Hours.pdf",
    tasks="24,E",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Fundamentals of Java Programming.pdf",
    tasks="19",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Grundkurs Java",
    tasks="33,D",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Java Succinctly Part 1.pdf",
    tasks="9,A",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Neural Network Programming with Java.pdf",
    tasks="9,B",
    priority=Priority.MEDIUM_HIGH,
    groups={"java", "dl"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Core Java Cheatsheet.pdf",
    tasks="1",
    priority=Priority.HIGH,
    groups={"java"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Learning Java.pdf",
    tasks="13,B",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Програмування на Java",
    link="https://www.youtube.com/playlist?list=PLxxPga8YS0l7Bory4_a9RHhg7NAQiCyrq",
    tasks="87",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=3,
)
g.add_project(
    name="Курс Java з нуля Українською",
    link="https://www.youtube.com/playlist?list=PLOlyZEVllXBGFYKIpet7KdkWnhQ7JpNXS",
    tasks="5",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Head First Java.pdf",
    tasks="9,A",
    priority=Priority.MEDIUM_LOW,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Легкий способ выучить Java.pdf",
    tasks="11,A",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Hands-On Software Engineering with Java.pdf",
    tasks="15",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://www.geeksforgeeks.org/image-processing-in-java-changing-orientation-of-image/?ref=rp",
    tasks="1",
    priority=Priority.WISH,
    groups={"cv", "java"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="JTextPro: A Java-based Text Processing Toolkit",
    tasks="1",
    priority=Priority.WISH,
    groups={"java", "nlp"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="JWebPro: A Java-based Web Processing Toolkit",
    tasks="1",
    priority=Priority.WISH,
    groups={"java", "web"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Learn Java the Hard Way",
    tasks="0-58",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    interval=1,
    cluster=1,
)
g.add_project(
    name="Классические задачи Computer Science на языке Java",
    tasks="10",
    priority=Priority.WISH,
    groups={"cs", "alg", "java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Interactive Object-Oriented Programming with Java.pdf",
    tasks="16,C",
    priority=Priority.MEDIUM_HIGH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Core Java SE 9 for the Impatient.pdf",
    tasks="15",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="https://exercism.org/tracks/java",
    tasks="132",
    priority=Priority.MEDIUM_HIGH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Think Java (2e).pdf",
    tasks="17,D",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Java для всех.pdf",
    tasks="13,B",
    priority=Priority.WISH,
    groups={"java"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)
g.add_project(
    name="Eloquent JavaScript",
    tasks="21",
    priority=Priority.WISH,
    groups={"javascript"},
    start=zero_date + 306,
    end=zero_date + 396,
    cluster=1,
)

g.backlog.extend(
    [
        BacklogItem(
            name="Creative Projects for Rust Programmers (https://libgen.is/book/index.php?md5=69F202277193C9C7FD9495F17BFA0944)",
            tasks="",
            groups={"Language Study"},
        ),
        BacklogItem(name="HelloChinese", tasks="", groups={"Language Study"}),
        BacklogItem(
            name="Deep Learning from First Principles In Vectorized Python R and Octave", tasks="", groups={""}
        ),
        BacklogItem(name="Guide to NumPy (2006)", tasks="", groups={"python", "c"}),
        BacklogItem(name="https://exercism.org/tracks/python", tasks="", groups={""}),
        BacklogItem(name="Tiny Python Projects", tasks="", groups={""}),
        BacklogItem(name="Автоматизация рутинных задач с помощью Python", tasks="", groups={""}),
        BacklogItem(name="Python. Сборник упражнений", tasks="", groups={""}),
        BacklogItem(name="Python. Книга рецептов", tasks="", groups={""}),
        BacklogItem(name="Python. Разработка на основе тестирования", tasks="", groups={""}),
        BacklogItem(name="Machine Learning - An Applied Mathematics Introduction", tasks="", groups={""}),
        BacklogItem(name="Introduction to Statistical Learning", tasks="", groups={""}),
        BacklogItem(name="INTO_IT: C Programmieren trainieren! - YouTube", tasks="", groups={""}),
        BacklogItem(name="Le langage C", tasks="", groups={""}),
        BacklogItem(name="Mastering C++ Programming Language", tasks="", groups={""}),
        BacklogItem(name="Programmieren in C - YouTube C Tutorials Deutsch", tasks="", groups={""}),
        BacklogItem(name="Sams Teach Yourself C++ in One Hour a Day (2022)", tasks="", groups={""}),
        BacklogItem(name="The C++ Standard Library. A Tutorial and Reference", tasks="", groups={""}),
        BacklogItem(name="https://exercism.org/tracks/cpp", tasks="", groups={""}),
        BacklogItem(name="Conceitos de computação com o essencial de C++", tasks="", groups={""}),
        BacklogItem(name="C++. Lernen und professionell anwenden", tasks="", groups={""}),
        BacklogItem(name="Экстремальный Си", tasks="", groups={""}),
        BacklogItem(name="Экстремальный Си", tasks="", groups={""}),
        BacklogItem(name="The C++ Programming Language", tasks="", groups={""}),
        BacklogItem(name="100 algoritmos C++", tasks="", groups={""}),
        BacklogItem(name="Algoritmos em Linguagem C", tasks="", groups={""}),
        BacklogItem(name="Решение задач на современном C++", tasks="", groups={""}),
        BacklogItem(name="Cpp Notes for Professionals", tasks="", groups={""}),
        BacklogItem(name="Cpp Programming. Program Design Including Data Structures", tasks="", groups={""}),
        BacklogItem(name="Design Patterns in Modern C++", tasks="", groups={""}),
        BacklogItem(name="Design Patterns in Modern C++20", tasks="", groups={""}),
        BacklogItem(name="Hands-On Design Patterns with Cpp", tasks="", groups={""}),
        BacklogItem(name="Il linguaggio C (Deitel)", tasks="", groups={""}),
        BacklogItem(name="Open Data Structures (in C++)", tasks="", groups={""}),
        BacklogItem(name="Programming Principles and Practices C++", tasks="", groups={""}),
        BacklogItem(name="Думай как программист - C++", tasks="", groups={""}),
        BacklogItem(name="C++ для профи", tasks="", groups={""}),
        BacklogItem(name="Guide to Competitive Programming", tasks="", groups={""}),
        BacklogItem(name="C – kurz & gut", tasks="", groups={""}),
        BacklogItem(name="Clean C++", tasks="", groups={""}),
        BacklogItem(name="Оптимизация программ на C++", tasks="", groups={""}),
        BacklogItem(name="Функциональное программирование на языке C++", tasks="", groups={""}),
        BacklogItem(name="Алгоритмические трюки для программистов", tasks="", groups={""}),
        BacklogItem(
            name="Beautiful Cpp. 30 Core Guidelines for Writing Clean, Safe, and Fast Code", tasks="", groups={""}
        ),
        BacklogItem(name="Inteligencia artificial avanzada", tasks="", groups={""}),
        BacklogItem(name="C und Linux", tasks="", groups={""}),
        BacklogItem(name="Data Structures and Algorithm  Analysis in C++", tasks="", groups={""}),
        BacklogItem(name="Effective C++ (140)", tasks="", groups={""}),
        BacklogItem(name="Effective Modern C++", tasks="", groups={""}),
        BacklogItem(name="Expert C++", tasks="", groups={""}),
        BacklogItem(name="Practical C++ Design", tasks="", groups={""}),
        BacklogItem(name="Programación en C, C++, Java y UML", tasks="", groups={""}),
        BacklogItem(name="Software Architecture with C++", tasks="", groups={""}),
        BacklogItem(name="String Algorithms in C", tasks="", groups={""}),
        BacklogItem(name="Безопасное программирование на C и C++", tasks="", groups={""}),
        BacklogItem(name="Introduction to Programming in Java. An Interdisciplinary Approach", tasks="", groups={""}),
        BacklogItem(name="Java Cookbook", tasks="", groups={"java"}),
        BacklogItem(name="Java for Data Science", tasks="", groups={"java"}),
        BacklogItem(name="Java Programming (Farrell)", tasks="", groups={"java"}),
        BacklogItem(name="Java Programming. From The Ground Up", tasks="", groups={"java"}),
        BacklogItem(name="Java для начинающих", tasks="", groups={"java"}),
        BacklogItem(name="Java полное руководство", tasks="", groups={"java"}),
        BacklogItem(name="Java. A Beginner's Guide", tasks="", groups={"java"}),
        BacklogItem(name="Java. Справочник разработчика", tasks="", groups={"java"}),
        BacklogItem(name="Java.djvu", tasks="", groups={"java"}),
        BacklogItem(name="Mastering Java. A Beginner's Guide", tasks="", groups={"java"}),
        BacklogItem(
            name="Mastering Java. An Effective Project Based Approach (including Web)", tasks="", groups={"java"}
        ),
        BacklogItem(name="Введение в объектно-ориентированный дизайн с Java", tasks="", groups={"java"}),
        BacklogItem(name="Джава. Решение практических задач", tasks="", groups={"java"}),
        BacklogItem(name="Java Pocket Guide", tasks="", groups={"java"}),
        BacklogItem(name="Java by Comparison. Become a Java Craftsman in 70 Examples", tasks="", groups={"java"}),
        BacklogItem(name="Java Succinctly Part 2", tasks="", groups={"java"}),
        BacklogItem(
            name="Java and the Java Virtual Machine Definition, Verification, Validation",
            tasks="",
            groups={"java", "jvm"},
        ),
        BacklogItem(name="Java Virtual Machine", tasks="", groups={"java", "jvm"}),
        BacklogItem(name="Modern Java in Action", tasks="", groups={"java"}),
        BacklogItem(
            name="Principles of Computer Organization and Assembly Language Using the JavaTM Virtual Machine",
            tasks="",
            groups={"java", "jvm"},
        ),
        BacklogItem(name="Programming for the Java Virtual Machine", tasks="", groups={"java", "jvm"}),
        BacklogItem(name="The Java® Virtual Machine Specification", tasks="", groups={"java", "jvm"}),
        BacklogItem(name="Well-Grounded Java Developer", tasks="", groups={"java"}),
        BacklogItem(name="Система модулей Java", tasks="", groups={"java"}),
        BacklogItem(name="Современный Java 2020", tasks="", groups={"java"}),
        BacklogItem(
            name="Объектно-ориентированное программирование на Java. Платформа Java SE",
            tasks="",
            groups={"java", "jvm"},
        ),
        BacklogItem(name="Структуры данных и алгоритмы Java", tasks="", groups={"java"}),
        BacklogItem(name="Decompiling Java", tasks="", groups={"java", "jvm"}),
        BacklogItem(
            name="Avrim Blum and Tom Mitchell: Combining Labeled and Unlabeled Data with Co-Training, 1998.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="John Lafferty, Andrew McCallum, Fernando C.N. Pereira: Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data, ICML 2001.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Charles Sutton, Andrew McCallum. An Introduction to Conditional Random Fields for Relational Learning.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Kamal Nigam, et al.: Text Classification from Labeled and Unlabeled Documents using EM. Machine Learning, 1999.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="“A simple framework for contrastive learning of visual representations.”", tasks="", groups={""}
        ),
        BacklogItem(name="Kevin Knight: Bayesian Inference with Tears, 2009.", tasks="", groups={""}),
        BacklogItem(
            name="Marco Tulio Ribeiro et al.: “Why Should I Trust You?”: Explaining the Predictions of Any Classifier, KDD 2016.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Marco Tulio Ribeiro et al.: Beyond Accuracy: Behavioral Testing of NLP Models with CheckList, ACL 2020.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Richard Socher, et al.: Dynamic Pooling and Unfolding Recursive Autoencoders for Paraphrase Detection, NIPS 2011.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="“Efficientnet: Rethinking model scaling for convolutional neural networks.”", tasks="", groups={""}
        ),
        BacklogItem(
            name="Ronan Collobert et al.: Natural Language Processing (almost) from Scratch, J. of Machine Learning Research, 2011.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Richard Socher, et al.: Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank, EMNLP 2013.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Xiang Zhang, Junbo Zhao, and Yann LeCun: Character-level Convolutional Networks for Text Classification, NIPS 2015.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Yoon Kim: Convolutional Neural Networks for Sentence Classification, 2014.", tasks="", groups={""}
        ),
        BacklogItem(
            name="“Pushing the limits of narrow precision inferencing at cloud scale with microsoft floating point.”",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Christopher Olah: Understanding LSTM Networks, 2015.", tasks="", groups={""}),
        BacklogItem(
            name="Matthew E. Peters, et al.: Deep contextualized word representations, 2018.", tasks="", groups={""}
        ),
        BacklogItem(
            name="Jacob Devlin, et al.: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding, 2018.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Yihan Liu et al. RoBERTa: A Robustly Optimized BERT Pretraining Approach, 2020.",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="“AdderNet: Do we really need multiplications in deep learning?.”", tasks="", groups={""}),
        BacklogItem(
            name="Peter F Brown, et al.: Class-Based n-gram Models of Natural Language, 1992.", tasks="", groups={""}
        ),
        BacklogItem(
            name="Tomas Mikolov, et al.: Efficient Estimation of Word Representations in Vector Space, 2013.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Tomas Mikolov, et al.: Distributed Representations of Words and Phrases and their Compositionality, NIPS 2013.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Quoc V. Le and Tomas Mikolov: Distributed Representations of Sentences and Documents, 2014.",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="“Alias-free generative adversarial networks.”", tasks="", groups={""}),
        BacklogItem(
            name="Jeffrey Pennington, et al.: GloVe: Global Vectors for Word Representation, 2014.",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Ryan Kiros, et al.: Skip-Thought Vectors, 2015.", tasks="", groups={""}),
        BacklogItem(
            name="Piotr Bojanowski, et al.: Enriching Word Vectors with Subword Information, 2017.",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Daniel Cer et al.: Universal Sentence Encoder, 2018.", tasks="", groups={""}),
        BacklogItem(name="“Transparency and reproducibility in artificial intelligence.”", tasks="", groups={""}),
        BacklogItem(name="Thomas Hofmann: Probabilistic Latent Semantic Indexing, SIGIR 1999.", tasks="", groups={""}),
        BacklogItem(
            name="David Blei, Andrew Y. Ng, and Michael I. Jordan: Latent Dirichlet Allocation, J. Machine Learning Research, 2003.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Joshua Goodman: A bit of progress in language modeling, MSR Technical Report, 2001.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Stanley F. Chen and Joshua Goodman: An Empirical Study of Smoothing Techniques for Language Modeling, ACL 2006.",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="“On the Measure of Intelligence.”", tasks="", groups={""}),
        BacklogItem(
            name="Yee Whye Teh: A Hierarchical Bayesian Language Model based on Pitman-Yor Processes, COLING/ACL 2006.",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Yee Whye Teh: A Bayesian interpretation of Interpolated Kneser-Ney, 2006.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Yoshua Bengio, et al.: A Neural Probabilistic Language Model, J. of Machine Learning Research, 2003.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Andrej Karpathy: The Unreasonable Effectiveness of Recurrent Neural Networks, 2015.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(name="Why do linear SVMs trained on HOG features perform so well?", tasks="", groups={"Papers"}),
        BacklogItem(
            name="Yoon Kim, et al.: Character-Aware Neural Language Models, 2015.", tasks="", groups={"Papers"}
        ),
        BacklogItem(
            name="Alec Radford, et al.: Language Models are Unsupervised Multitask Learners, 2018.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Donald Hindle and Mats Rooth. Structural Ambiguity and Lexical Relations, Computational Linguistics, 1993.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Adwait Ratnaparkhi: A Maximum Entropy Model for Part-Of-Speech Tagging, EMNLP 1996.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Eugene Charniak: A Maximum-Entropy-Inspired Parser, NAACL 2000.", tasks="", groups={"Papers"}
        ),
        BacklogItem(
            name="Michael Collins: Discriminative Training Methods for Hidden Markov Models: Theory and Experiments with Perceptron Algorithms, EMNLP 2002.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Dan Klein and Christopher Manning: Accurate Unlexicalized Parsing, ACL 2003.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Dan Klein and Christopher Manning: Corpus-Based Induction of Syntactic Structure: Models of Dependency and Constituency, ACL 2004.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Joakim Nivre and Mario Scholz: Deterministic Dependency Parsing of English Text, COLING 2004.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Ryan McDonald et al.: Non-Projective Dependency Parsing using Spanning-Tree Algorithms, EMNLP 2005.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Daniel Andor et al.: Globally Normalized Transition-Based Neural Networks, 2016.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(name="Oriol Vinyals, et al.: Grammar as a Foreign Language, 2015.", tasks="", groups={"Papers"}),
        BacklogItem(
            name="Marti A. Hearst: Automatic Acquisition of Hyponyms from Large Text Corpora, COLING 1992.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Collins and Singer: Unsupervised Models for Named Entity Classification, EMNLP 1999.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Patrick Pantel and Dekang Lin, Discovering Word Senses from Text, SIGKDD, 2002.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Mike Mintz et al.: Distant supervision for relation extraction without labeled data, ACL 2009.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Zhiheng Huang et al.: Bidirectional LSTM-CRF Models for Sequence Tagging, 2015.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Xuezhe Ma and Eduard Hovy: End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF, ACL 2016.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Peter F. Brown et al.: A Statistical Approach to Machine Translation, Computational Linguistics, 1990.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Kevin Knight, Graehl Jonathan. Machine Transliteration. Computational Linguistics, 1992.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Dekai Wu: Inversion Transduction Grammars and the Bilingual Parsing of Parallel Corpora, Computational Linguistics, 1997.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(name="Kevin Knight: A Statistical MT Tutorial Workbook, 1999.", tasks="", groups={"Papers"}),
        BacklogItem(
            name="Kishore Papineni, et al.: BLEU: a Method for Automatic Evaluation of Machine Translation, ACL 2002.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Philipp Koehn, Franz J Och, and Daniel Marcu: Statistical Phrase-Based Translation, NAACL 2003.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Philip Resnik and Noah A. Smith: The Web as a Parallel Corpus, Computational Linguistics, 2003.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Franz J Och and Hermann Ney: The Alignment-Template Approach to Statistical Machine Translation, Computational Linguistics, 2004.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="David Chiang. A Hierarchical Phrase-Based Model for Statistical Machine Translation, ACL 2005.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Ilya Sutskever, Oriol Vinyals, and Quoc V. Le: Sequence to Sequence Learning with Neural Networks, NIPS 2014.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(name="Oriol Vinyals, Quoc Le: A Neural Conversation Model, 2015.", tasks="", groups={"Papers"}),
        BacklogItem(
            name="Dzmitry Bahdanau, et al.: Neural Machine Translation by Jointly Learning to Align and Translate, 2014.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Minh-Thang Luong, et al.: Effective Approaches to Attention-based Neural Machine Translation, 2015.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Rico Sennrich et al.: Neural Machine Translation of Rare Words with Subword Units. ACL 2016.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Yonghui Wu, et al.: Google’s Neural Machine Translation System: Bridging the Gap between Human and Machine Translation, 2016.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Melvin Johnson, et al.: Google’s Multilingual Neural Machine Translation System: Enabling Zero-Shot Translation, 2016.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Jonas Gehring, et al.: Convolutional Sequence to Sequence Learning, 2017.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(name="Ashish Vaswani, et al.: Attention Is All You Need, 2017.", tasks="", groups={"Papers"}),
        BacklogItem(
            name="Vincent Ng: Supervised Noun Phrase Coreference Research: The First Fifteen Years, ACL 2010.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Kenton Lee at al.: End-to-end Neural Coreference Resolution, EMNLP 2017.", tasks="", groups={"Papers"}
        ),
        BacklogItem(
            name="Kevin Knight and Daniel Marcu: Summarization beyond sentence extraction. Artificial Intelligence 139, 2002.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="James Clarke and Mirella Lapata: Modeling Compression with Discourse Constraints. EMNLP-CONLL 2007.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Ryan McDonald: A Study of Global Inference Algorithms in Multi-Document Summarization, ECIR 2007.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Wen-tau Yih et al.: Multi-Document Summarization by Maximizing Informative Content-Words. IJCAI 2007.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Alexander M Rush, et al.: A Neural Attention Model for Sentence Summarization. EMNLP 2015.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Abigail See et al.: Get To The Point: Summarization with Pointer-Generator Networks. ACL 2017.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Pranav Rajpurkar et al.: SQuAD: 100,000+ Questions for Machine Comprehension of Text. EMNLP 2015.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Minjoon Soo et al.: Bi-Directional Attention Flow for Machine Comprehension. ICLR 2015.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Jiwei Li, et al.: Deep Reinforcement Learning for Dialogue Generation, EMNLP 2016.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Marc’Aurelio Ranzato et al.: Sequence Level Training with Recurrent Neural Networks. ICLR 2016.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Samuel R Bowman et al.: Generating sentences from a continuous space, CoNLL 2016.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(
            name="Lantao Yu, et al.: SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient, AAAI 2017.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(name="CoNLL-X shared task on multilingual dependency parsing.", tasks="", groups={"Papers"}),
        BacklogItem(
            name="Coarse-to-fine n-best parsing and MaxEnt discriminative reranking.", tasks="", groups={"Papers"}
        ),
        BacklogItem(
            name="The CoNLL-2010 shared task: learning to detect hedges and their scope in natural language text.",
            tasks="",
            groups={"Papers"},
        ),
        BacklogItem(name="WordNet: An electronic lexical database. 1998.", tasks="", groups={"Papers"}),
        BacklogItem(name="Accurate unlexicalized parsing.", tasks="", groups={"Papers"}),
        BacklogItem(name="Automatic retrieval and clustering of similar words.", tasks="", groups={"Papers"}),
        BacklogItem(
            name="Building a large annotated corpus of English: The Penn Treebank.", tasks="", groups={"Papers"}
        ),
        BacklogItem(name="The proposition bank: An annotated corpus of semantic roles.", tasks="", groups={"Papers"}),
        BacklogItem(
            name="BLEU: a method for automatic evaluation of machine translation.", tasks="", groups={"Papers"}
        ),
        BacklogItem(name="Improved Inference for Unlexicalized Parsing.", tasks="", groups={"Papers"}),
        BacklogItem(name="3Blue1Brown Differential Equations", tasks="", groups={""}),
        BacklogItem(name="Mathematik", tasks="", groups={""}),
        BacklogItem(name="Principles of Mathematical Analysis (Rudin)", tasks="", groups={""}),
        BacklogItem(name="Videos: Socratica Abstract Algebra Playlist", tasks="", groups={""}),
        BacklogItem(name="Linear Algebra Done Right (Axler)", tasks="", groups={""}),
        BacklogItem(name="Linear Algebra (Insel, Freidberg, Spence - problems)", tasks="", groups={""}),
        BacklogItem(name="Videos: Sheldon Axler’s Playlist", tasks="", groups={""}),
        BacklogItem(name="Introduction to Linear Algebra, Fourth Edition by Gilbert Strang", tasks="", groups={""}),
        BacklogItem(name="Basic Linear Algebra (Blyth & Robertson)", tasks="", groups={""}),
        BacklogItem(
            name="MIT Open Courseware Video Lectures - Linear Algebra by Gilbert Strang", tasks="", groups={""}
        ),
        BacklogItem(name="Geometry by Roger Fenn", tasks="", groups={""}),
        BacklogItem(name="Metric Spaces (O'Searcoid)", tasks="", groups={""}),
        BacklogItem(name="Measure, Integral and Probability (Capinski & Kopp, 2E)", tasks="", groups={""}),
        BacklogItem(name="MIT OCW Measure and Integration", tasks="", groups={""}),
        BacklogItem(name="A First Course in Probability (Ross)", tasks="", groups={""}),
        BacklogItem(name="Schaum's Outline of Probability and Statistics", tasks="", groups={""}),
        BacklogItem(name="Probability and Statistics by Example: Volume 1 (Suhov & Kelbert)", tasks="", groups={""}),
        BacklogItem(name="Statistical Inference (Casella & Berger)", tasks="", groups={""}),
        BacklogItem(name="Real Analysis: Lectures by Professor Francis Su", tasks="", groups={""}),
        BacklogItem(name="Understanding Analysis (Abbott)", tasks="", groups={""}),
        BacklogItem(name="Videos: MAT137 Playlist", tasks="", groups={""}),
        BacklogItem(name="Real Analysis (Howie)", tasks="", groups={""}),
        BacklogItem(name="Topology through Inquiry (Su & Starbird)", tasks="", groups={""}),
        BacklogItem(name="Essential Topology (Crossley)", tasks="", groups={""}),
        BacklogItem(name="Videos: WhyBMaths", tasks="", groups={""}),
        BacklogItem(name="Foundations of Applied Mathematics", tasks="", groups={""}),
        BacklogItem(
            name="https://pnp.mathematik.uni-stuttgart.de/igt/eiserm/lehre/Lineare-Algebra/", tasks="", groups={""}
        ),
        BacklogItem(name="Vector Calculus (Matthews)", tasks="", groups={""}),
        BacklogItem(name="3Blue1Brown Neural Networks", tasks="", groups={""}),
        BacklogItem(name="Statistical Rethinking 2022", tasks="", groups={""}),
        BacklogItem(name="Measure Theory and Probability (MathematicalMonk)", tasks="", groups={""}),
        BacklogItem(name="Mathematical Tripos examination questions in IB Statistics", tasks="", groups={""}),
        BacklogItem(
            name="Div, Grad, Curl, and All That: An Informal Text on Vector Calculus (Schey)", tasks="", groups={""}
        ),
        BacklogItem(name="MIT OCW Multivariable Calculus", tasks="", groups={""}),
        BacklogItem(name="Think Bayes. Bayesian Statistics in Python", tasks="", groups={""}),
        BacklogItem(name="Think stats", tasks="", groups={""}),
        BacklogItem(name="Байесовская статистика", tasks="", groups={""}),
        BacklogItem(name="Classic Algebra by P.M. Cohn", tasks="", groups={""}),
        BacklogItem(
            name="Matlab - A Practical Introduction to Programming and Problem Solving (Attaway 3E)",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Online Notes: MAT327 Course Notes", tasks="", groups={""}),
        BacklogItem(name="Problems: MAT 327 Course Problems", tasks="", groups={""}),
        BacklogItem(name="Videos: Point Set Topology Playlist", tasks="", groups={""}),
        BacklogItem(name="Algebraic Topology Playlist", tasks="", groups={""}),
        BacklogItem(
            name="Concrete Abstract Algebra: From Numbers to Gröbner Bases by N. Lauritzen", tasks="", groups={""}
        ),
        BacklogItem(name="Contemporary Abstract Algebra (Gallian)", tasks="", groups={""}),
        BacklogItem(name="Introduction to Manifolds (Tu, for rigor)", tasks="", groups={""}),
        BacklogItem(name="Groups (Jordan & Jordan)", tasks="", groups={""}),
        BacklogItem(name="Schaum's Outline of Group Theory (Baumslag & Chandle)", tasks="", groups={""}),
        BacklogItem(name="Groups, Rings and Fields (Wallace)", tasks="", groups={""}),
        BacklogItem(name="Online Notes: MAT327 Course Notes <>", tasks="", groups={""}),
        BacklogItem(
            name="Elementary Differential Equations and Boundary Value Problems (Boyce & DiPrima)",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="MIT Open CourseWare Video Lectures - Differential Equations by Arthur Mattuck", tasks="", groups={""}
        ),
        BacklogItem(
            name="Stability, Instability and Chaos: An Introduction to the Theory of Nonlinear Differential Equations (Glendinning)",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Differential Equations with Boundary Value Problems (Zill & Cullen)", tasks="", groups={""}),
        BacklogItem(name="An Introduction to Ordinary Differential Equations (Robinson)", tasks="", groups={""}),
        BacklogItem(name="Visual Complex Analysis (Needham, for intuition)", tasks="", groups={""}),
        BacklogItem(name="Analysis of a Complex Kind (Petra Bonfert-Taylor)", tasks="", groups={""}),
        BacklogItem(name="A Geometric Approach to Differential Forms (Bachman, for intuition)", tasks="", groups={""}),
        BacklogItem(name="Differential Equations", tasks="", groups={""}),
        BacklogItem(
            name="Ordinary Differential Equations: Analysis, Qualitative Theory and Control (Logemann & Ryan)",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Scalar, Vector, and Matrix Mathematics", tasks="", groups={""}),
        BacklogItem(name="Machine Learning Engineering in Action", tasks="", groups={""}),
        BacklogItem(name="Machine Learning Engineering with MLFlow (Hank and (Elsie)", tasks="", groups={""}),
        BacklogItem(name="Machine Learning Engineering", tasks="", groups={""}),
        BacklogItem(name="Параллельные и высокопроизводительные вычисления", tasks="", groups={""}),
        BacklogItem(name="Deep Learning Illustrated", tasks="", groups={""}),
        BacklogItem(name="Deep Learning for Coders with Fastai and PyTorch", tasks="", groups={""}),
        BacklogItem(name="Machine Learning Hands-on for Developers and Technical Professionals", tasks="", groups={""}),
        BacklogItem(name="Mastering Machine Learning Algorithms", tasks="", groups={""}),
        BacklogItem(name="Transfer Learning", tasks="", groups={""}),
        BacklogItem(name="Math for Deep Learning. What You Need to Know", tasks="", groups={""}),
        BacklogItem(name="Thoughtful Machine Learning with Python", tasks="", groups={""}),
        BacklogItem(name="Глубокое обучение в картинках", tasks="", groups={""}),
        BacklogItem(name="Redes neuronales & deep learning", tasks="", groups={""}),
        BacklogItem(name="Data Scientists at Work", tasks="", groups={""}),
        BacklogItem(name="Машинное обучение с участием человека", tasks="", groups={""}),
        BacklogItem(name="GPT-2", tasks="", groups={""}),
        BacklogItem(name="“Tabular data: Deep learning is not all you need.”", tasks="", groups={""}),
        BacklogItem(name="Universal Language Model Fine-tuning for Text Classification", tasks="", groups={""}),
        BacklogItem(name="Improving Language Understanding by Generative Pre-Training", tasks="", groups={""}),
        BacklogItem(name="Learning an Executable Neural Semantic Parser", tasks="", groups={""}),
        BacklogItem(name="https://blog.codinghorror.com/recommended-reading-for-developers/", tasks="", groups={""}),
        BacklogItem(name="200 frases - Noruego - Español", tasks="", groups={""}),
        BacklogItem(name="Aprender yidis", tasks="", groups={""}),
        BacklogItem(name="Colloquial Arabic (Levantine)", tasks="", groups={""}),
        BacklogItem(name="Full-Stack Python Security", tasks="", groups={""}),
        BacklogItem(name="Modern Python Cookbook", tasks="", groups={""}),
        BacklogItem(name="Linux Bible", tasks="", groups={""}),
        BacklogItem(
            name="The TCP,IP Guide. A Comprehensive, Illustrated Internet Protocols Reference", tasks="", groups={""}
        ),
        BacklogItem(name="Программирование GPU при помощи Python и CUDA", tasks="", groups={""}),
        BacklogItem(name="Deep Learning with PyTorch Step-by-Step", tasks="", groups={""}),
        BacklogItem(
            name="Neural Networks https://www.youtube.com/watch?v=CqOfi41LfDw&list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="PyTorch Pocket Reference", tasks="", groups={""}),
        BacklogItem(name="PyTorch Basics for Absolute Beginners.epub", tasks="", groups={""}),
        BacklogItem(name="The Supervised Learning Workshop", tasks="", groups={""}),
        BacklogItem(name="Глубокое обучение 1 (Гласснер)", tasks="", groups={""}),
        BacklogItem(name="Глубокое обучение 2 (Гласснер)", tasks="", groups={""}),
        BacklogItem(name="Data science from Scratch 2e", tasks="", groups={""}),
        BacklogItem(
            name="Hands-On Python Deep Learning for the Web. Integrating neural network architectures to build smart web apps with Flask, Django, and TensorFlow",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Еще более эффективный Agile", tasks="", groups={""}),
        BacklogItem(name="Карьера программиста", tasks="", groups={""}),
        BacklogItem(name="Mathematics for Machine Learning", tasks="", groups={""}),
        BacklogItem(name="“A ConvNet for the 2020s.”", tasks="", groups={""}),
        BacklogItem(name="Unsupervised Compositionality Prediction of Nominal Compounds", tasks="", groups={""}),
        BacklogItem(
            name="Automatic Inference of Sound Correspondence Patterns across Multiple Languages", tasks="", groups={""}
        ),
        BacklogItem(
            name="A Sequential Matching Framework for Multi-Turn Response Selection in Retrieval-Based Chatbots",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Parsing Chinese Sentences with Grammatical Relations", tasks="", groups={""}),
        BacklogItem(name="300 verbos + Leer y escuchar: - Noruego + Español", tasks="", groups={""}),
        BacklogItem(name="Modern Cpp Tutorial", tasks="", groups={""}),
        BacklogItem(name="Программирование на С", tasks="", groups={""}),
        BacklogItem(name="Программирование на языке Cpp", tasks="", groups={""}),
        BacklogItem(name="Hands-On Machine Learning with C++", tasks="", groups={""}),
        BacklogItem(name="C++ українською", tasks="", groups={""}),
        BacklogItem(name="Cpp for Lazy Programmers", tasks="", groups={""}),
        BacklogItem(name="Cpp20 for Programmers", tasks="", groups={""}),
        BacklogItem(name="Discovering Modern C++", tasks="", groups={""}),
        BacklogItem(name="Exploring C++20", tasks="", groups={""}),
        BacklogItem(name="Corso di informatica 1. Linguaggio C e Cpp", tasks="", groups={""}),
        BacklogItem(name="Corso di informatica 2. Linguaggio C e Cpp", tasks="", groups={""}),
        BacklogItem(name="Tour of C++", tasks="", groups={""}),
        BacklogItem(name="A Book on C", tasks="", groups={""}),
        BacklogItem(name="The C++ Workshop", tasks="", groups={""}),
        BacklogItem(name="Computational Thinking | MIT 18.S191/6.S083 Spring 2021", tasks="", groups={""}),
        BacklogItem(name="Computational Thinking | MIT 18.S191/6.S083 Spring 2023", tasks="", groups={""}),
        BacklogItem(name="Data Science with Julia", tasks="", groups={""}),
        BacklogItem(
            name="Julia - Bit by Bit: Programming for Beginners (Undergraduate Topics in Computer Science)",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Julia 1.0 Programming Dynamic and High-Performance Programming to Build Fast Scientific Applications.epub",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Julia 1.7", tasks="", groups={""}),
        BacklogItem(name="Julia Express", tasks="", groups={""}),
        BacklogItem(name="Julia for Data Science", tasks="", groups={""}),
        BacklogItem(name="Julia for R Programmers", tasks="", groups={""}),
        BacklogItem(name="Julia Language. A Concise Tutorial", tasks="", groups={""}),
        BacklogItem(name="Julia Programming Projects", tasks="", groups={""}),
        BacklogItem(name="Julia", tasks="", groups={""}),
        BacklogItem(name="Learn Julia by building a number guessing game!", tasks="", groups={""}),
        BacklogItem(name="Learning Julia", tasks="", groups={""}),
        BacklogItem(name="Mastering Julia", tasks="", groups={""}),
        BacklogItem(name="Statistics with Julia", tasks="", groups={""}),
        BacklogItem(name="Осваиваем язык Julia", tasks="", groups={""}),
        BacklogItem(name="https://exercism.org/tracks/julia", tasks="", groups={""}),
        BacklogItem(name="https://docs.python.org/3/library/ctypes.html", tasks="", groups={""}),
        BacklogItem(name="Physics", tasks="", groups={""}),
        BacklogItem(name="PoissonNote.dvi - PoissonNote", tasks="", groups={""}),
        BacklogItem(name="Proof of existence and proof of uniqueness of determinant", tasks="", groups={""}),
        BacklogItem(
            name="Prove 8 statements in the key theorem of LA (All the Math You Missed, 1.6)", tasks="", groups={""}
        ),
        BacklogItem(name="Operating system for beginners || Operating system basics - YouTube", tasks="", groups={""}),
        BacklogItem(name="https://wiki.archlinux.org/title/Installation_guide", tasks="", groups={""}),
        BacklogItem(
            name="https://linux-audit.com/elf-binaries-on-linux-understanding-and-analysis/", tasks="", groups={""}
        ),
        BacklogItem(
            name="April 9 -  Comparing Programming Languages Part 3 - C, Rust, Java, Kotlin, Go, JS/TS, Python, and Ruby  (12 mins)",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="March 29 -  Comparing Programming Languages Part 2 - Memory Management and Concurrency  (10 mins)",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="March 26 -  Comparing Programming Languages Part 1 - Compilers and Type-Systems  (10 mins)",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="Compilers: Innovation from the Bottom-Up—Viral Shah & Keno Fischer on TechLifeSkills w/Tanmay Ep. 20",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="On Mathematical Maturity (1) Thomas Garrity - YouTube", tasks="", groups={""}),
        BacklogItem(name="Fast Inverse Square Root — A Quake III Algorithm - YouTube", tasks="", groups={""}),
        BacklogItem(
            name="Operating System Full Course | Operating System Tutorials for Beginners - YouTube",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Assembler #1 Hello-World zur Maschinensprache", tasks="", groups={""}),
        BacklogItem(name="Assembler #2 Wie speichert man eine Konsoleneingabe?", tasks="", groups={""}),
        BacklogItem(name="Operating Systems: Crash Course Computer Science #18 - YouTube", tasks="", groups={""}),
        BacklogItem(
            name="Operating System Full Course || Operating System for IT Support - YouTube", tasks="", groups={""}
        ),
        BacklogItem(name="https://www.youtube.com/watch?v=jAGIuobLp60", tasks="", groups={""}),
        BacklogItem(name="https://www.youtube.com/watch?v=LFKZLXVO-Dg", tasks="", groups={""}),
        BacklogItem(name="Neural Network from scratch-part 1 | AI Summer", tasks="", groups={""}),
        BacklogItem(name="https://contentlab.io/c-neural-network-in-a-weekend/", tasks="", groups={""}),
        BacklogItem(
            name="That unbelievable function that can compute EVERYTHING! An Adventure in Discrete Mathematics - YouTube",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="We're Building Computers Wrong - YouTube", tasks="", groups={""}),
        BacklogItem(
            name="https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c10/",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Turingmaschinen - YouTube", tasks="", groups={""}),
        BacklogItem(name="https://github.com/0xAX/asm", tasks="", groups={""}),
        BacklogItem(name="https://cs.lmu.edu/~ray/notes/nasmtutorial/", tasks="", groups={""}),
        BacklogItem(name="1000 Linux Questions & Answers", tasks="", groups={""}),
        BacklogItem(
            name="https://booking.ai/theres-more-to-experimentation-than-a-b-223fba846876", tasks="", groups={""}
        ),
        BacklogItem(name="http://www.norvig.com/design-patterns/design-patterns", tasks="", groups={""}),
        BacklogItem(name="So you want to write an interpreter?", tasks="", groups={""}),
        BacklogItem(name="WebAssembly (WASM) verdrängt Docker?! // deutsch", tasks="", groups={""}),
        BacklogItem(name="https://fuchsia.dev/", tasks="", groups={""}),
        BacklogItem(
            name="https://medium.com/@brianwill/unix-userland-should-be-replaced-5605fe47cac0", tasks="", groups={""}
        ),
        BacklogItem(name="https://medium.com/@brianwill", tasks="", groups={""}),
        BacklogItem(
            name="https://pilvinen.github.io/notes-on-why-oop-is-bad-and-how-to-solve-it.html", tasks="", groups={""}
        ),
        BacklogItem(name="https://developer.ibm.com/articles/l-gas-nasm/", tasks="", groups={""}),
        BacklogItem(name="Games RL", tasks="", groups={""}),
        BacklogItem(name="What Happens when I Press a Key?", tasks="", groups={""}),
        BacklogItem(name="AES", tasks="", groups={""}),
        BacklogItem(name="OOP", tasks="", groups={""}),
        BacklogItem(name="Why Rust?", tasks="", groups={""}),
        BacklogItem(name="Railroad", tasks="", groups={""}),
        BacklogItem(name="Was sind Monaden? Funktionale Programmierung", tasks="", groups={""}),
        BacklogItem(
            name="Why would a python programmer learn rust when there are no jobs in it", tasks="", groups={""}
        ),
        BacklogItem(name="https://github.com/gnulinuxpro/infra/", tasks="", groups={""}),
        BacklogItem(name="RabbitMQ Crash Course", tasks="", groups={""}),
        BacklogItem(
            name="RabbitMQ Introduction | RabbitMQ Tutorial for Beginners | What is RabbitMQ | RabbitMQ Message Broker",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Configuration as Code in Bamboo - Atlassian Summit Europe 2017", tasks="", groups={""}),
        BacklogItem(name="https://www.freecodecamp.org/news/the-docker-handbook/", tasks="", groups={""}),
        BacklogItem(
            name="Microservices Architecture Design Patterns | 10 Design Principles | 26 Design Patterns 🔥 🔥 🔥 - YouTube",
            tasks="",
            groups={""},
        ),
        BacklogItem(
            name="10 Architecture Patterns Used In Enterprise Software Development Today - YouTube",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="10 Design Patterns Explained in 10 Minutes - YouTube", tasks="", groups={""}),
        BacklogItem(name="RabbitMQ Crash Course - YouTube", tasks="", groups={""}),
        BacklogItem(name="Microservice APIs: With examples in Python (MEAP v10)", tasks="", groups={""}),
        BacklogItem(name="RabbitMQ in 5 minutes", tasks="", groups={""}),
        BacklogItem(name="https://www.youtube.com/watch?v=fl_AelgaWKE", tasks="", groups={""}),
        BacklogItem(name="Learn Docker in 7 Easy Steps - Full Beginner's Tutorial - YouTube", tasks="", groups={""}),
        BacklogItem(
            name="The 50 Most Popular Linux & Terminal Commands - Full Course for Beginners - YouTube",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Docker Tutorial #1 - Warum ihr Docker braucht! - YouTube", tasks="", groups={""}),
        BacklogItem(name="Cloud Computing. Concepts and Technologies.epub", tasks="", groups={""}),
        BacklogItem(name="Cloud Native Python", tasks="", groups={""}),
        BacklogItem(
            name="Generic Pipelines Using Docker. The DevOps Guide to Building Reusable, Platform Agnostic CI_CD",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="Hands-On RESTful Python Web Services", tasks="", groups={""}),
        BacklogItem(name="Practical Web Scraping for Data Scientists", tasks="", groups={""}),
        BacklogItem(name="Python и DevOps", tasks="", groups={""}),
        BacklogItem(name="Python. Непрерывная интеграция и доставка", tasks="", groups={""}),
        BacklogItem(name="RabbitMQ Essentials", tasks="", groups={""}),
        BacklogItem(name="RabbitMQ in Depth", tasks="", groups={""}),
        BacklogItem(
            name="Web API Development with Python. A Beginner's Guide using Flask and FastAPI", tasks="", groups={""}
        ),
        BacklogItem(
            name="Облачные архитектуры разработка устойчивых и экономичных облачных приложений", tasks="", groups={""}
        ),
        BacklogItem(name="От монолита к микросервисам", tasks="", groups={""}),
        BacklogItem(
            name="Networks, Crowds, and Markets: Reasoning about a Highly Connected World", tasks="", groups={""}
        ),
        BacklogItem(name="Learning at Lambert Labs", tasks="", groups={""}),
        BacklogItem(name="LaTeX 2e for class and package writers", tasks="", groups={""}),
        BacklogItem(
            name="LaTeX Users Guide and Reference Manual. A Document Preparation System (Lamport)",
            tasks="",
            groups={""},
        ),
        BacklogItem(name="TeX by Topic, A TeXnician's Reference", tasks="", groups={""}),
        BacklogItem(name="The TeXbook", tasks="", groups={""}),
        BacklogItem(name="Algorithms for Decision Making", tasks="", groups={""}),
        BacklogItem(name="Angewandte Mathematik 1 mit MATLAB und Julia", tasks="", groups={""}),
        BacklogItem(name="Angewandte Mathematik 2 mit MATLAB und Julia", tasks="", groups={""}),
        BacklogItem(name="Beginning Julia Programming for Engineers and Scientists", tasks="", groups={""}),
        BacklogItem(name="Foundation Dynamic Web Pages with Python", tasks="", groups={""}),
        BacklogItem(name="Getting Started with Julia Programming", tasks="", groups={""}),
        BacklogItem(name="Hands-on Design Patterns and Best Practices with Julia", tasks="", groups={""}),
        BacklogItem(name="https://julia.quantecon.org/intro.html", tasks="", groups={""}),
        BacklogItem(name="https://pnp.mathematik.uni-stuttgart.de/igt/eiserm/lehre/Topolywood/", tasks="", groups={""}),
        BacklogItem(name="Open Data Structures (in Java)", tasks="", groups={""}),
        BacklogItem(name="Seven Languages in Seven Weeks", tasks="", groups={""}),
        BacklogItem(name="Seven More Languages in Seven Weeks", tasks="", groups={""}),
        BacklogItem(name="Understanding Cryptography", tasks="", groups={""}),
        BacklogItem(name="ГЕОМЕТРИЯ В КАРТИНКАХ", tasks="", groups={""}),
        BacklogItem(name="Коротко о языке программирования Julia", tasks="", groups={""}),
        BacklogItem(name="Шпаргалки для начинающего верстальщика HTML CSS", tasks="", groups={""}),
        BacklogItem(
            name="ЯЗЫК ПРОГРАММИРОВАНИЯ МАТЕМАТИЧЕСКИХ ВЫЧИСЛЕНИЙ JULIA. БАЗОВОЕ РУКОВОДСТВО", tasks="", groups={""}
        ),
        BacklogItem(name="https://exercism.org/tracks/scala", tasks="", groups={""}),
        BacklogItem(name="https://exercism.org/tracks/go", tasks="", groups={""}),
        BacklogItem(name="ACOUSTIC PARAMETERS VERSUS PHONETIC FEATURES IN ASR", tasks="", groups={""}),
        BacklogItem(name="https://exercism.org/tracks/scheme", tasks="", groups={""}),
        BacklogItem(name="https://exercism.org/tracks/fortran", tasks="", groups={""}),
        BacklogItem(name="Modern Fortran", tasks="", groups={""}),
        BacklogItem(name="Das Gehirn", tasks="", groups={""}),
        BacklogItem(name="Kognitive Neurowissenschaften", tasks="", groups={""}),
        BacklogItem(name="Neurobiologie", tasks="", groups={""}),
        BacklogItem(name="Neuromythologie", tasks="", groups={""}),
        BacklogItem(name="Psycholinguistik - Neurolinguistik", tasks="", groups={""}),
        BacklogItem(name="Мозг, познание, разум I", tasks="", groups={""}),
        BacklogItem(name="Мозг, познание, разум II", tasks="", groups={""}),
        BacklogItem(name="Fascism: A Very Short Introduction", tasks="", groups={""}),
        BacklogItem(name="Free Will: A Very Short Introduction", tasks="", groups={""}),
        BacklogItem(name="Freedom Regained: The Possibility of Free Will", tasks="", groups={""}),
        BacklogItem(name="Gehirn und Geist Spezial", tasks="", groups={""}),
        BacklogItem(name="German Philosophy: A Very Short Introduction (Elsie)", tasks="", groups={""}),
        BacklogItem(name="History: A Very Short Introduction (Elsie)", tasks="", groups={""}),
        BacklogItem(name="Kant & Co. im Interview", tasks="", groups={""}),
        BacklogItem(name="Motherland: a philosophical history of Russia", tasks="", groups={""}),
        BacklogItem(name="The Palgrave Handbook of the Psychology of Sexuality and Gender", tasks="", groups={""}),
        BacklogItem(name="The Philosophy of Sex", tasks="", groups={""}),
        BacklogItem(name="Кухня Робинсона.djvu", tasks="", groups={""}),
        BacklogItem(name="Один на один с природой", tasks="", groups={""}),
        BacklogItem(name="Проста фізика.epub", tasks="", groups={""}),
        BacklogItem(name="Lehrbuch Kognitive Neurowissenschaften", tasks="", groups={""}),
        BacklogItem(name="Мозг, познание, разум", tasks="", groups={""}),
        BacklogItem(name="Философия DevOps", tasks="", groups={""}),
        BacklogItem(name="Осваиваем Kubernetes", tasks="", groups={""}),
        BacklogItem(name="Социальная инженерия и социальные хакеры", tasks="", groups={""}),
        BacklogItem(name="Субстанция мышления", tasks="", groups={""}),
        BacklogItem(name="МАТЕМАТИЧЕСКАЯ ЛОГИКА И ТЕОРИЯ АЛГОРИТМОВ", tasks="", groups={""}),
        BacklogItem(name="Программирование. Python. C++. Часть 1.djvu", tasks="", groups={""}),
        BacklogItem(name="Программирование. Python. C++. Часть 2.djvu", tasks="", groups={""}),
        BacklogItem(name="Программирование. Python. C++. Часть 3.djvu", tasks="", groups={""}),
        BacklogItem(name="Программирование. Python. C++. Часть 4.djvu", tasks="", groups={""}),
        BacklogItem(name="50 Shades of JavaScript", tasks="", groups={"javascript"}),
        BacklogItem(name="Aprendendo JavaScript", tasks="", groups={"javascript"}),
        BacklogItem(name="Beginning Topology", tasks="", groups={""}),
        BacklogItem(name="ES6 и не только", tasks="", groups={""}),
        BacklogItem(name="GNU Linux programación de sistemas", tasks="", groups={""}),
        BacklogItem(name="Hands-On System Programming with Linux", tasks="", groups={""}),
        BacklogItem(name="Introduction to Topology", tasks="", groups={""}),
        BacklogItem(name="Intuitive Concepts in Elementary Topology", tasks="", groups={""}),
        BacklogItem(name="JavaScript Succinctly", tasks="", groups={"javascript"}),
        BacklogItem(name="JavaScript для детей", tasks="", groups={"javascript"}),
        BacklogItem(name="JavaScript для профессиональных веб-разработчиков", tasks="", groups={"javascript"}),
        BacklogItem(name="JavaScript на примерах", tasks="", groups={"javascript"}),
        BacklogItem(name="JavaScript с нуля 2021", tasks="", groups={"javascript"}),
        BacklogItem(name="JavaScript. The Definitive Guide", tasks="", groups={"javascript"}),
        BacklogItem(name="JavaScript. Полное руководство", tasks="", groups={"javascript"}),
        BacklogItem(name="Professional JavaScript for Web Developers, 4th Edition", tasks="", groups={"javascript"}),
        BacklogItem(name="https://exercism.org/tracks/javascript", tasks="", groups={"javascript"}),
        BacklogItem(name="Rediscovering JavaScript", tasks="", groups={"javascript"}),
        BacklogItem(name="Познакомьтесь, JavaScript 2е (Симпсон)", tasks="", groups={"javascript"}),
        BacklogItem(name="The JavaScript Way", tasks="", groups={"javascript"}),
        BacklogItem(name="Topologie 2020", tasks="", groups={""}),
        BacklogItem(name="Topology Illustrated", tasks="", groups={""}),
        BacklogItem(name="Topology: A Very Short Introduction (Elsie)", tasks="", groups={""}),
        BacklogItem(name="TypeScript ES", tasks="", groups={""}),
        BacklogItem(name="Understanding Topology. A Practical Introduction", tasks="", groups={""}),
        BacklogItem(name="WebAssembly в действии", tasks="", groups={""}),
        BacklogItem(name="Искусство WebAssembly", tasks="", groups={""}),
        BacklogItem(name="Математика в огне", tasks="", groups={""}),
        BacklogItem(name="Наглядный CSS", tasks="", groups={""}),
        BacklogItem(name="Отзывчивый дизайн на HTML5 и CSS3 для любых устройств 3е", tasks="", groups={""}),
        BacklogItem(name="Программируй & типизируй", tasks="", groups={""}),
        BacklogItem(name="Разработка веб-приложений", tasks="", groups={""}),
        BacklogItem(name="ТОПОЛОГІЯ МНОГОВИДІВ", tasks="", groups={""}),
        BacklogItem(name="https://exercism.org/tracks/r", tasks="", groups={""}),
        BacklogItem(name="Numerical Methods in Science and Engineering", tasks="", groups={""}),
        BacklogItem(name="Cassandra. The Definitive Guide", tasks="", groups={""}),
        BacklogItem(name="Graph Databases", tasks="", groups={""}),
        BacklogItem(name="Hadoop. The Definitive Guide", tasks="", groups={""}),
        BacklogItem(name="High Performance Spark", tasks="", groups={""}),
        BacklogItem(name="Learning Spark", tasks="", groups={""}),
        BacklogItem(name="Practical Machine Learning with H2O", tasks="", groups={""}),
        BacklogItem(name="Time Series Databases", tasks="", groups={""}),
        BacklogItem(name="An introduction to language processing with Perl and Prolog", tasks="", groups={""}),
        BacklogItem(name="An Overview of Lexical Semantics", tasks="", groups={""}),
        BacklogItem(name="Analytical Methods for Interpretable Ultradense Word Embeddings", tasks="", groups={""}),
        BacklogItem(name="Kotlin в действии", tasks="", groups={""}),
        BacklogItem(name="Android Slides", tasks="", groups={""}),
        BacklogItem(name="Kotlin for Android App Development", tasks="", groups={""}),
        BacklogItem(name="Practical Android. 14 Complete Projects", tasks="", groups={""}),
        BacklogItem(name="https://exercism.org/tracks/racket", tasks="", groups={""}),
        BacklogItem(name="https://exercism.org/tracks/elixir", tasks="", groups={""}),
        BacklogItem(name="https://exercism.org/tracks/erlang", tasks="", groups={""}),
        BacklogItem(name="Practical Deep Learning for Cloud, Mobile, & Edge", tasks="", groups={""}),
        BacklogItem(name="Understanding Machine Learning", tasks="", groups={""}),
        BacklogItem(name="Foundations of Machine Learning", tasks="", groups={""}),
        BacklogItem(name="Foundaions of Machine Learning", tasks="", groups={""}),
        BacklogItem(name="Introduction to Machine Learning (Alpaydin)", tasks="", groups={""}),
        BacklogItem(name="Inteligencia artificial", tasks="", groups={""}),
        BacklogItem(name="Python Machine Learning Blueprints", tasks="", groups={""}),
        BacklogItem(name="Python и наука о данных", tasks="", groups={""}),
    ]
)
