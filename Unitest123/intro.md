# `<span class="pre">unittest</span>` — Unit testing framework

**Source code:** [Lib/unittest/__init__.py](https://github.com/python/cpython/tree/3.12/Lib/unittest/__init__.py)

---

(If you are already familiar with the basic concepts of testing, you might want to skip to [the list of assert methods](https://docs.python.org/3/library/unittest.html#assert-methods).)

The [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

To achieve this, [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") supports some important concepts in an object-oriented way:

test fixtureA *test fixture* represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

test caseA *test case* is the individual unit of testing. It checks for a specific response to a particular set of inputs. [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") provides a base class, [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase"), which may be used to create new test cases.

test suiteA *test suite* is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

test runnerA *test runner* is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.

See also

Module [`<span class="pre">doctest</span>`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.")Another test-support module with a very different flavor.

[Simple Smalltalk Testing: With Patterns](https://web.archive.org/web/20150315073817/http://www.xprogramming.com/testfram.htm)Kent Beck’s original paper on testing frameworks using the pattern shared by [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.").

[pytest](https://docs.pytest.org/)Third-party unittest framework with a lighter-weight syntax for writing tests. For example, `<span class="pre">assert</span><span> </span><span class="pre">func(10)</span><span> </span><span class="pre">==</span><span> </span><span class="pre">42</span>`.

[The Python Testing Tools Taxonomy](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)An extensive list of Python testing tools including functional testing frameworks and mock object libraries.

[Testing in Python Mailing List](http://lists.idyll.org/listinfo/testing-in-python)A special-interest-group for discussion of testing, and testing tools, in Python.

The script `<span class="pre">Tools/unittestgui/unittestgui.py</span>` in the Python source distribution is a GUI tool for test discovery and execution. This is intended largely for ease of use for those new to unit testing. For production environments it is recommended that tests be driven by a continuous integration system such as [Buildbot](https://buildbot.net/), [Jenkins](https://www.jenkins.io/), [GitHub Actions](https://github.com/features/actions), or [AppVeyor](https://www.appveyor.com/).

## Basic example

The [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") module provides a rich set of tools for constructing and running tests. This section demonstrates that a small subset of the tools suffice to meet the needs of most users.

Here is a short script to test three string methods:

```
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

A testcase is created by subclassing [`<span class="pre">unittest.TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase"). The three individual tests are defined with methods whose names start with the letters `<span class="pre">test</span>`. This naming convention informs the test runner about which methods represent tests.

The crux of each test is a call to [`<span class="pre">assertEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual") to check for an expected result; [`<span class="pre">assertTrue()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue "unittest.TestCase.assertTrue") or [`<span class="pre">assertFalse()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse "unittest.TestCase.assertFalse") to verify a condition; or [`<span class="pre">assertRaises()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "unittest.TestCase.assertRaises") to verify that a specific exception gets raised. These methods are used instead of the [`<span class="pre">assert</span>`](https://docs.python.org/3/reference/simple_stmts.html#assert) statement so the test runner can accumulate all test results and produce a report.

The [`<span class="pre">setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") and [`<span class="pre">tearDown()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") methods allow you to define instructions that will be executed before and after each test method. They are covered in more detail in the section [Organizing test code](https://docs.python.org/3/library/unittest.html#organizing-tests).

The final block shows a simple way to run the tests. [`<span class="pre">unittest.main()</span>`](https://docs.python.org/3/library/unittest.html#unittest.main "unittest.main") provides a command-line interface to the test script. When run from the command line, the above script produces an output that looks like this:

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

Passing the `<span class="pre">-v</span>` option to your test script will instruct [`<span class="pre">unittest.main()</span>`](https://docs.python.org/3/library/unittest.html#unittest.main "unittest.main") to enable a higher level of verbosity, and produce the following output:

```
test_isupper (__main__.TestStringMethods.test_isupper) ... ok
test_split (__main__.TestStringMethods.test_split) ... ok
test_upper (__main__.TestStringMethods.test_upper) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

The above examples show the most commonly used [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") features which are sufficient to meet many everyday testing needs. The remainder of the documentation explores the full feature set from first principles.

**Changed in version 3.11:** The behavior of returning a value from a test method (other than the default `<span class="pre">None</span>` value), is now deprecated.

## Command-Line Interface

The unittest module can be used from the command line to run tests from modules, classes or even individual test methods:

```
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
```

You can pass in a list with any combination of module names, and fully qualified class or method names.

Test modules can be specified by file path as well:

```
python -m unittest tests/test_something.py
```

This allows you to use the shell filename completion to specify the test module. The file specified must still be importable as a module. The path is converted to a module name by removing the ‘.py’ and converting path separators into ‘.’. If you want to execute a test file that isn’t importable as a module you should execute the file directly instead.

You can run tests with more detail (higher verbosity) by passing in the -v flag:

```
python -m unittest -v test_module
```

When executed without arguments [Test Discovery](https://docs.python.org/3/library/unittest.html#unittest-test-discovery) is started:

```
python -m unittest
```

For a list of all the command-line options:

```
python -m unittest -h
```

**Changed in version 3.2:** In earlier versions it was only possible to run individual test methods and not modules or classes.

### Command-line options

**unittest** supports these command-line options:

-b**,** **--buffer**[](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-b "Link to this definition")The standard output and standard error streams are buffered during the test run. Output during a passing test is discarded. Output is echoed normally on test fail or error and is added to the failure messages.

-c**,** **--catch**[](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-c "Link to this definition")Control-C during the test run waits for the current test to end and then reports all the results so far. A second Control-C raises the normal [`<span class="pre">KeyboardInterrupt</span>`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt") exception.

See [Signal Handling](https://docs.python.org/3/library/unittest.html#signal-handling) for the functions that provide this functionality.

-f**,** **--failfast**[](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-f "Link to this definition")Stop the test run on the first error or failure.

-k[](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-k "Link to this definition")Only run test methods and classes that match the pattern or substring. This option may be used multiple times, in which case all test cases that match any of the given patterns are included.

Patterns that contain a wildcard character (`<span class="pre">*</span>`) are matched against the test name using [`<span class="pre">fnmatch.fnmatchcase()</span>`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "fnmatch.fnmatchcase"); otherwise simple case-sensitive substring matching is used.

Patterns are matched against the fully qualified test method name as imported by the test loader.

For example, `<span class="pre">-k</span><span> </span><span class="pre">foo</span>` matches `<span class="pre">foo_tests.SomeTest.test_something</span>`, `<span class="pre">bar_tests.SomeTest.test_foo</span>`, but not `<span class="pre">bar_tests.FooTest.test_something</span>`.

--locals[](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-locals "Link to this definition")Show local variables in tracebacks.

--durations **N**[](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-durations "Link to this definition")Show the N slowest test cases (N=0 for all).

**Added in version 3.2:** The command-line options `<span class="pre">-b</span>`, `<span class="pre">-c</span>` and `<span class="pre">-f</span>` were added.

**Added in version 3.5:** The command-line option `<span class="pre">--locals</span>`.

**Added in version 3.7:** The command-line option `<span class="pre">-k</span>`.

**Added in version 3.12:** The command-line option `<span class="pre">--durations</span>`.

The command line can also be used for test discovery, for running all of the tests in a project or just a subset.

## Test Discovery

**Added in version 3.2.**

Unittest supports simple test discovery. In order to be compatible with test discovery, all of the test files must be [modules](https://docs.python.org/3/tutorial/modules.html#tut-modules) or [packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) importable from the top-level directory of the project (this means that their filenames must be valid [identifiers](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)).

Test discovery is implemented in [`<span class="pre">TestLoader.discover()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.discover "unittest.TestLoader.discover"), but can also be used from the command line. The basic command-line usage is:

```
cd project_directory
python -m unittest discover
```

Note

 As a shortcut, `<span class="pre">python</span><span> </span><span class="pre">-m</span><span> </span><span class="pre">unittest</span>` is the equivalent of `<span class="pre">python</span><span> </span><span class="pre">-m</span><span> </span><span class="pre">unittest</span><span> </span><span class="pre">discover</span>`. If you want to pass arguments to test discovery the `<span class="pre">discover</span>` sub-command must be used explicitly.

The `<span class="pre">discover</span>` sub-command has the following options:

-v**,** **--verbose**[](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-v "Link to this definition")Verbose output

-s**,** **--start-directory** **directory**[](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-s "Link to this definition")Directory to start discovery (`<span class="pre">.</span>` default)

-p**,** **--pattern** **pattern**[](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-p "Link to this definition")Pattern to match test files (`<span class="pre">test*.py</span>` default)

-t**,** **--top-level-directory** **directory**[](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-t "Link to this definition")Top level directory of project (defaults to start directory)

The [`<span class="pre">-s</span>`](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-s), [`<span class="pre">-p</span>`](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-p), and [`<span class="pre">-t</span>`](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-t) options can be passed in as positional arguments in that order. The following two command lines are equivalent:

```
python -m unittest discover -s project_directory -p "*_test.py"
python -m unittest discover project_directory "*_test.py"
```

As well as being a path it is possible to pass a package name, for example `<span class="pre">myproject.subpackage.test</span>`, as the start directory. The package name you supply will then be imported and its location on the filesystem will be used as the start directory.

Caution

 Test discovery loads tests by importing them. Once test discovery has found all the test files from the start directory you specify it turns the paths into package names to import. For example `<span class="pre">foo/bar/baz.py</span>` will be imported as `<span class="pre">foo.bar.baz</span>`.

If you have a package installed globally and attempt test discovery on a different copy of the package then the import *could* happen from the wrong place. If this happens test discovery will warn you and exit.

If you supply the start directory as a package name rather than a path to a directory then discover assumes that whichever location it imports from is the location you intended, so you will not get the warning.

Test modules and packages can customize test loading and discovery by through the [load_tests protocol](https://docs.python.org/3/library/unittest.html#id1).

**Changed in version 3.4:** Test discovery supports [namespace packages](https://docs.python.org/3/glossary.html#term-namespace-package) for the start directory. Note that you need to specify the top level directory too (e.g. `<span class="pre">python</span><span> </span><span class="pre">-m</span><span> </span><span class="pre">unittest</span><span> </span><span class="pre">discover</span><span> </span><span class="pre">-s</span><span> </span><span class="pre">root/namespace</span><span> </span><span class="pre">-t</span><span> </span><span class="pre">root</span>`).

**Changed in version 3.11:** [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") dropped the [namespace packages](https://docs.python.org/3/glossary.html#term-namespace-package) support in Python 3.11. It has been broken since Python 3.7. Start directory and subdirectories containing tests must be regular package that have `<span class="pre">__init__.py</span>` file.

Directories containing start directory still can be a namespace package. In this case, you need to specify start directory as dotted package name, and target directory explicitly. For example:

```
# proj/  <-- current directory
#   namespace/
#     mypkg/
#       __init__.py
#       test_mypkg.py

python -m unittest discover -s namespace.mypkg -t .
```

## Organizing test code

The basic building blocks of unit testing are *test cases* — single scenarios that must be set up and checked for correctness. In [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python."), test cases are represented by [`<span class="pre">unittest.TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances. To make your own test cases you must write subclasses of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") or use [`<span class="pre">FunctionTestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.FunctionTestCase "unittest.FunctionTestCase").

The testing code of a [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instance should be entirely self contained, such that it can be run either in isolation or in arbitrary combination with any number of other test cases.

The simplest [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") subclass will simply implement a test method (i.e. a method whose name starts with `<span class="pre">test</span>`) in order to perform specific testing code:

```
import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))
```

Note that in order to test something, we use one of the [assert* methods](https://docs.python.org/3/library/unittest.html#assert-methods) provided by the [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") base class. If the test fails, an exception will be raised with an explanatory message, and [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") will identify the test case as a  *failure* . Any other exceptions will be treated as  *errors* .

Tests can be numerous, and their set-up can be repetitive. Luckily, we can factor out set-up code by implementing a method called [`<span class="pre">setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp"), which the testing framework will automatically call for every single test we run:

```
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
```

Note

 The order in which the various tests will be run is determined by sorting the test method names with respect to the built-in ordering for strings.

If the [`<span class="pre">setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") method raises an exception while the test is running, the framework will consider the test to have suffered an error, and the test method will not be executed.

Similarly, we can provide a [`<span class="pre">tearDown()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") method that tidies up after the test method has been run:

```
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
```

If [`<span class="pre">setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") succeeded, [`<span class="pre">tearDown()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") will be run whether the test method succeeded or not.

Such a working environment for the testing code is called a  *test fixture* . A new TestCase instance is created as a unique test fixture used to execute each individual test method. Thus [`<span class="pre">setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp"), [`<span class="pre">tearDown()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown"), and `<span class="pre">__init__()</span>` will be called once per test.

It is recommended that you use TestCase implementations to group tests together according to the features they test. [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") provides a mechanism for this: the  *test suite* , represented by [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.")’s [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") class. In most cases, calling [`<span class="pre">unittest.main()</span>`](https://docs.python.org/3/library/unittest.html#unittest.main "unittest.main") will do the right thing and collect all the module’s test cases for you and execute them.

However, should you want to customize the building of your test suite, you can do it yourself:

```
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

You can place the definitions of test cases and test suites in the same modules as the code they are to test (such as `<span class="pre">widget.py</span>`), but there are several advantages to placing the test code in a separate module, such as `<span class="pre">test_widget.py</span>`:

* The test module can be run standalone from the command line.
* The test code can more easily be separated from shipped code.
* There is less temptation to change test code to fit the code it tests without a good reason.
* Test code should be modified much less frequently than the code it tests.
* Tested code can be refactored more easily.
* Tests for modules written in C must be in separate modules anyway, so why not be consistent?
* If the testing strategy changes, there is no need to change the source code.

## Re-using old test code

Some users will find that they have existing test code that they would like to run from [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python."), without converting every old test function to a [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") subclass.

For this reason, [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") provides a [`<span class="pre">FunctionTestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.FunctionTestCase "unittest.FunctionTestCase") class. This subclass of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") can be used to wrap an existing test function. Set-up and tear-down functions can also be provided.

Given the following test function:

```
def testSomething():
    something = makeSomething()
    assert something.name is not None
    # ...
```

one can create an equivalent test case instance as follows, with optional set-up and tear-down methods:

```
testcase = unittest.FunctionTestCase(testSomething,
                                     setUp=makeSomethingDB,
                                     tearDown=deleteSomethingDB)
```

Note

 Even though [`<span class="pre">FunctionTestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.FunctionTestCase "unittest.FunctionTestCase") can be used to quickly convert an existing test base over to a [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.")-based system, this approach is not recommended. Taking the time to set up proper [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") subclasses will make future test refactorings infinitely easier.

In some cases, the existing tests may have been written using the [`<span class="pre">doctest</span>`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") module. If so, [`<span class="pre">doctest</span>`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") provides a `<span class="pre">DocTestSuite</span>` class that can automatically build [`<span class="pre">unittest.TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") instances from the existing [`<span class="pre">doctest</span>`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.")-based tests.

## Skipping tests and expected failures

**Added in version 3.1.**

Unittest supports skipping individual test methods and even whole classes of tests. In addition, it supports marking a test as an “expected failure,” a test that is broken and will fail, but shouldn’t be counted as a failure on a [`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult").

Skipping a test is simply a matter of using the [`<span class="pre">skip()</span>`](https://docs.python.org/3/library/unittest.html#unittest.skip "unittest.skip") [decorator](https://docs.python.org/3/glossary.html#term-decorator) or one of its conditional variants, calling [`<span class="pre">TestCase.skipTest()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.skipTest "unittest.TestCase.skipTest") within a [`<span class="pre">setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") or test method, or raising [`<span class="pre">SkipTest</span>`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") directly.

Basic skipping looks like this:

```
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass
```

This is the output of running the example above in verbose mode:

```
test_format (__main__.MyTestCase.test_format) ... skipped 'not supported in this library version'
test_nothing (__main__.MyTestCase.test_nothing) ... skipped 'demonstrating skipping'
test_maybe_skipped (__main__.MyTestCase.test_maybe_skipped) ... skipped 'external resource not available'
test_windows_support (__main__.MyTestCase.test_windows_support) ... skipped 'requires Windows'

----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK (skipped=4)
```

Classes can be skipped just like methods:

```
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
```

[`<span class="pre">TestCase.setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") can also skip the test. This is useful when a resource that needs to be set up is not available.

Expected failures use the [`<span class="pre">expectedFailure()</span>`](https://docs.python.org/3/library/unittest.html#unittest.expectedFailure "unittest.expectedFailure") decorator.

```
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
```

It’s easy to roll your own skipping decorators by making a decorator that calls [`<span class="pre">skip()</span>`](https://docs.python.org/3/library/unittest.html#unittest.skip "unittest.skip") on the test when it wants it to be skipped. This decorator skips the test unless the passed object has a certain attribute:

```
def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))
```

The following decorators and exception implement test skipping and expected failures:

@**unittest.**skip**(** *reason* **)**[](https://docs.python.org/3/library/unittest.html#unittest.skip "Link to this definition")Unconditionally skip the decorated test. *reason* should describe why the test is being skipped.

@**unittest.**skipIf**(** *condition* ,  *reason* **)**[](https://docs.python.org/3/library/unittest.html#unittest.skipIf "Link to this definition")Skip the decorated test if *condition* is true.

@**unittest.**skipUnless**(** *condition* ,  *reason* **)**[](https://docs.python.org/3/library/unittest.html#unittest.skipUnless "Link to this definition")Skip the decorated test unless *condition* is true.

@**unittest.**expectedFailure[](https://docs.python.org/3/library/unittest.html#unittest.expectedFailure "Link to this definition")Mark the test as an expected failure or error. If the test fails or errors in the test function itself (rather than in one of the *test fixture* methods) then it will be considered a success. If the test passes, it will be considered a failure.

*exception *unittest.**SkipTest**( *reason* **)**[](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "Link to this definition")This exception is raised to skip a test.

Usually you can use [`<span class="pre">TestCase.skipTest()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.skipTest "unittest.TestCase.skipTest") or one of the skipping decorators instead of raising this directly.

Skipped tests will not have [`<span class="pre">setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") or [`<span class="pre">tearDown()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") run around them. Skipped classes will not have [`<span class="pre">setUpClass()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass "unittest.TestCase.setUpClass") or [`<span class="pre">tearDownClass()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "unittest.TestCase.tearDownClass") run. Skipped modules will not have `<span class="pre">setUpModule()</span>` or `<span class="pre">tearDownModule()</span>` run.

## Distinguishing test iterations using subtests

**Added in version 3.4.**

When there are very small differences among your tests, for instance some parameters, unittest allows you to distinguish them inside the body of a test method using the [`<span class="pre">subTest()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.subTest "unittest.TestCase.subTest") context manager.

For example, the following test:

```
class NumbersTest(unittest.TestCase):

    def test_even(self):
"""
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
```

will produce the following output:

```
======================================================================
FAIL: test_even (__main__.NumbersTest.test_even) (i=1)
Test that numbers between 0 and 5 are all even.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 11, in test_even
    self.assertEqual(i % 2, 0)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1 != 0

======================================================================
FAIL: test_even (__main__.NumbersTest.test_even) (i=3)
Test that numbers between 0 and 5 are all even.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 11, in test_even
    self.assertEqual(i % 2, 0)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1 != 0

======================================================================
FAIL: test_even (__main__.NumbersTest.test_even) (i=5)
Test that numbers between 0 and 5 are all even.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 11, in test_even
    self.assertEqual(i % 2, 0)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1 != 0
```

Without using a subtest, execution would stop after the first failure, and the error would be less easy to diagnose because the value of `<span class="pre">i</span>` wouldn’t be displayed:

```
======================================================================
FAIL: test_even (__main__.NumbersTest.test_even)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 32, in test_even
    self.assertEqual(i % 2, 0)
AssertionError: 1 != 0
```

## Classes and functions

This section describes in depth the API of [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.").

### Test cases

*class *unittest.**TestCase**( *methodName**=**'runTest'* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase "Link to this definition")Instances of the [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") class represent the logical test units in the [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") universe. This class is intended to be used as a base class, with specific tests being implemented by concrete subclasses. This class implements the interface needed by the test runner to allow it to drive the tests, and methods that the test code can use to check for and report various kinds of failure.

Each instance of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") will run a single base method: the method named  *methodName* . In most uses of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase"), you will neither change the *methodName* nor reimplement the default `<span class="pre">runTest()</span>` method.

**Changed in version 3.2:** [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") can be instantiated successfully without providing a  *methodName* . This makes it easier to experiment with [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") from the interactive interpreter.

[`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances provide three groups of methods: one group used to run the test, another used by the test implementation to check conditions and report failures, and some inquiry methods allowing information about the test itself to be gathered.

Methods in the first group (running the test) are:

setUp**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "Link to this definition")Method called to prepare the test fixture. This is called immediately before calling the test method; other than [`<span class="pre">AssertionError</span>`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") or [`<span class="pre">SkipTest</span>`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest"), any exception raised by this method will be considered an error rather than a test failure. The default implementation does nothing.

tearDown**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "Link to this definition")Method called immediately after the test method has been called and the result recorded. This is called even if the test method raised an exception, so the implementation in subclasses may need to be particularly careful about checking internal state. Any exception, other than [`<span class="pre">AssertionError</span>`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") or [`<span class="pre">SkipTest</span>`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest"), raised by this method will be considered an additional error rather than a test failure (thus increasing the total number of reported errors). This method will only be called if the [`<span class="pre">setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") succeeds, regardless of the outcome of the test method. The default implementation does nothing.

setUpClass**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass "Link to this definition")A class method called before tests in an individual class are run. `<span class="pre">setUpClass</span>` is called with the class as the only argument and must be decorated as a [`<span class="pre">classmethod()</span>`](https://docs.python.org/3/library/functions.html#classmethod "classmethod"):

```
@classmethod
def setUpClass(cls):
    ...
```

See [Class and Module Fixtures](https://docs.python.org/3/library/unittest.html#class-and-module-fixtures) for more details.

**Added in version 3.2.**

tearDownClass**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "Link to this definition")A class method called after tests in an individual class have run. `<span class="pre">tearDownClass</span>` is called with the class as the only argument and must be decorated as a [`<span class="pre">classmethod()</span>`](https://docs.python.org/3/library/functions.html#classmethod "classmethod"):

```
@classmethod
def tearDownClass(cls):
    ...
```

See [Class and Module Fixtures](https://docs.python.org/3/library/unittest.html#class-and-module-fixtures) for more details.

**Added in version 3.2.**

run**(** *result**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.run "Link to this definition")Run the test, collecting the result into the [`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") object passed as  *result* . If *result* is omitted or `<span class="pre">None</span>`, a temporary result object is created (by calling the [`<span class="pre">defaultTestResult()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.defaultTestResult "unittest.TestCase.defaultTestResult") method) and used. The result object is returned to [`<span class="pre">run()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.run "unittest.TestCase.run")’s caller.

The same effect may be had by simply calling the [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instance.

**Changed in version 3.3:** Previous versions of `<span class="pre">run</span>` did not return the result. Neither did calling an instance.

skipTest**(** *reason* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.skipTest "Link to this definition")Calling this during a test method or [`<span class="pre">setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") skips the current test. See [Skipping tests and expected failures](https://docs.python.org/3/library/unittest.html#unittest-skipping) for more information.

**Added in version 3.1.**

subTest**(** *msg**=**None* ,  ***params* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.subTest "Link to this definition")Return a context manager which executes the enclosed code block as a subtest. *msg* and *params* are optional, arbitrary values which are displayed whenever a subtest fails, allowing you to identify them clearly.

A test case can contain any number of subtest declarations, and they can be arbitrarily nested.

See [Distinguishing test iterations using subtests](https://docs.python.org/3/library/unittest.html#subtests) for more information.

**Added in version 3.4.**

debug**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug "Link to this definition")Run the test without collecting the result. This allows exceptions raised by the test to be propagated to the caller, and can be used to support running tests under a debugger.

The [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") class provides several assert methods to check for and report failures. The following table lists the most commonly used methods (see the tables below for more assert methods):



* `assertEqual(a, b)` checks that `a == b`
* `assertNotEqual(a, b)` checks that `a != b`
* `assertTrue(x)` checks that `bool(x) is True`
* `assertFalse(x)` checks that `bool(x) is False`
* `assertIs(a, b)` checks that `a is b`
* `assertIsNot(a, b)` checks that `a is not b`
* `assertIsNone(x)` checks that `x is None`
* `assertIsNotNone(x)` checks that `x is not None`
* `assertIn(a, b)` checks that `a in b`
* `assertNotIn(a, b)` checks that `a not in b`
* `assertIsInstance(a, b)` checks that `isinstance(a, b)`
* `assertNotIsInstance(a, b)` checks that `not isinstance(a, b`)

| Method                                                                                                                                                                                                                   | Checks that                                                                                                                                                     | New in |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| [`<span class="pre">assertEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual")                         | `<span class="pre">a</span><span> </span><span class="pre">==</span><span> </span><span class="pre">b</span>`                                               |        |
| [`<span class="pre">assertNotEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual "unittest.TestCase.assertNotEqual")                | `<span class="pre">a</span><span> </span><span class="pre">!=</span><span> </span><span class="pre">b</span>`                                               |        |
| [`<span class="pre">assertTrue(x)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue "unittest.TestCase.assertTrue")                                                                      | `<span class="pre">bool(x)</span><span> </span><span class="pre">is</span><span> </span><span class="pre">True</span>`                                      |        |
| [`<span class="pre">assertFalse(x)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse "unittest.TestCase.assertFalse")                                                                   | `<span class="pre">bool(x)</span><span> </span><span class="pre">is</span><span> </span><span class="pre">False</span>`                                     |        |
| [`<span class="pre">assertIs(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs "unittest.TestCase.assertIs")                                  | `<span class="pre">a</span><span> </span><span class="pre">is</span><span> </span><span class="pre">b</span>`                                               | 3.1    |
| [`<span class="pre">assertIsNot(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot "unittest.TestCase.assertIsNot")                         | `<span class="pre">a</span><span> </span><span class="pre">is</span><span> </span><span class="pre">not</span><span> </span><span class="pre">b</span>`    | 3.1    |
| [`<span class="pre">assertIsNone(x)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone "unittest.TestCase.assertIsNone")                                                                | `<span class="pre">x</span><span> </span><span class="pre">is</span><span> </span><span class="pre">None</span>`                                            | 3.1    |
| [`<span class="pre">assertIsNotNone(x)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone "unittest.TestCase.assertIsNotNone")                                                       | `<span class="pre">x</span><span> </span><span class="pre">is</span><span> </span><span class="pre">not</span><span> </span><span class="pre">None</span>` | 3.1    |
| [`<span class="pre">assertIn(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn "unittest.TestCase.assertIn")                                  | `<span class="pre">a</span><span> </span><span class="pre">in</span><span> </span><span class="pre">b</span>`                                               | 3.1    |
| [`<span class="pre">assertNotIn(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIn "unittest.TestCase.assertNotIn")                         | `<span class="pre">a</span><span> </span><span class="pre">not</span><span> </span><span class="pre">in</span><span> </span><span class="pre">b</span>`    | 3.1    |
| [`<span class="pre">assertIsInstance(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance "unittest.TestCase.assertIsInstance")          | `<span class="pre">isinstance(a,</span><span> </span><span class="pre">b)</span>`                                                                            | 3.2    |
| [`<span class="pre">assertNotIsInstance(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance "unittest.TestCase.assertNotIsInstance") | `<span class="pre">not</span><span> </span><span class="pre">isinstance(a,</span><span> </span><span class="pre">b)</span>`                                 | 3.2    |

All the assert methods accept a *msg* argument that, if specified, is used as the error message on failure (see also [`<span class="pre">longMessage</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.longMessage "unittest.TestCase.longMessage")). Note that the *msg* keyword argument can be passed to [`<span class="pre">assertRaises()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "unittest.TestCase.assertRaises"), [`<span class="pre">assertRaisesRegex()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex "unittest.TestCase.assertRaisesRegex"), [`<span class="pre">assertWarns()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "unittest.TestCase.assertWarns"), [`<span class="pre">assertWarnsRegex()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex "unittest.TestCase.assertWarnsRegex") only when they are used as a context manager.

assertEqual**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "Link to this definition")Test that *first* and *second* are equal. If the values do not compare equal, the test will fail.

In addition, if *first* and *second* are the exact same type and one of list, tuple, dict, set, frozenset or str or any type that a subclass registers with [`<span class="pre">addTypeEqualityFunc()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addTypeEqualityFunc "unittest.TestCase.addTypeEqualityFunc") the type-specific equality function will be called in order to generate a more useful default error message (see also the [list of type-specific methods](https://docs.python.org/3/library/unittest.html#type-specific-methods)).

**Changed in version 3.1:** Added the automatic calling of type-specific equality function.

**Changed in version 3.2:** [`<span class="pre">assertMultiLineEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual "unittest.TestCase.assertMultiLineEqual") added as the default type equality function for comparing strings.

assertNotEqual**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual "Link to this definition")Test that *first* and *second* are not equal. If the values do compare equal, the test will fail.

assertTrue**(** *expr* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue "Link to this definition")assertFalse**(** *expr* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse "Link to this definition")Test that *expr* is true (or false).

Note that this is equivalent to `<span class="pre">bool(expr)</span><span> </span><span class="pre">is</span><span> </span><span class="pre">True</span>` and not to `<span class="pre">expr</span><span> </span><span class="pre">is</span><span> </span><span class="pre">True</span>` (use `<span class="pre">assertIs(expr,</span><span> </span><span class="pre">True)</span>` for the latter). This method should also be avoided when more specific methods are available (e.g. `<span class="pre">assertEqual(a,</span><span> </span><span class="pre">b)</span>` instead of `<span class="pre">assertTrue(a</span><span> </span><span class="pre">==</span><span> </span><span class="pre">b)</span>`), because they provide a better error message in case of failure.

assertIs**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs "Link to this definition")assertIsNot**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot "Link to this definition")Test that *first* and *second* are (or are not) the same object.

**Added in version 3.1.**

assertIsNone**(** *expr* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone "Link to this definition")assertIsNotNone**(** *expr* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone "Link to this definition")Test that *expr* is (or is not) `<span class="pre">None</span>`.

**Added in version 3.1.**

assertIn**(** *member* ,  *container* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn "Link to this definition")assertNotIn**(** *member* ,  *container* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIn "Link to this definition")Test that *member* is (or is not) in  *container* .

**Added in version 3.1.**

assertIsInstance**(** *obj* ,  *cls* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance "Link to this definition")assertNotIsInstance**(** *obj* ,  *cls* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance "Link to this definition")Test that *obj* is (or is not) an instance of *cls* (which can be a class or a tuple of classes, as supported by [`<span class="pre">isinstance()</span>`](https://docs.python.org/3/library/functions.html#isinstance "isinstance")). To check for the exact type, use [`<span class="pre">assertIs(type(obj),</span><span> </span><span class="pre">cls)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs "unittest.TestCase.assertIs").

**Added in version 3.2.**

It is also possible to check the production of exceptions, warnings, and log messages using the following methods:


* `assertRaises(exc, fun, *args, **kwds)` checks that `fun(*args, **kwds)` raises `exc`
* `assertRaisesRegex(exc, r, fun, *args, **kwds)` checks that `fun(*args, **kwds)` raises `exc` and the message matches regex `r`
* `assertWarns(warn, fun, *args, **kwds)` checks that `fun(*args, **kwds)` raises `warn`
* `assertWarnsRegex(warn, r, fun, *args, **kwds)` checks that `fun(*args, **kwds)` raises `warn` and the message matches regex `r`
* `assertLogs(logger, level)` checks that the `with` block logs on `logger` with minimum `level`
* `assertNoLogs(logger, level)` checks that the `with` block does not log on `logger` with minimum `level`

| Method                                                                                                                                                                                                                                                                                                                                                        | Checks that                                                                                                                                | New in |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| [`<span class="pre">assertRaises(exc,</span><span> </span><span class="pre">fun,</span><span> </span><span class="pre">*args,</span><span> </span><span class="pre">**kwds)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "unittest.TestCase.assertRaises")                                                          | `<span class="pre">fun(*args,</span><span> </span><span class="pre">**kwds)</span>` raises *exc*                                      |        |
| [`<span class="pre">assertRaisesRegex(exc,</span><span> </span><span class="pre">r,</span><span> </span><span class="pre">fun,</span><span> </span><span class="pre">*args,</span><span> </span><span class="pre">**kwds)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex "unittest.TestCase.assertRaisesRegex") | `<span class="pre">fun(*args,</span><span> </span><span class="pre">**kwds)</span>` raises *exc* and the message matches regex *r*  | 3.1    |
| [`<span class="pre">assertWarns(warn,</span><span> </span><span class="pre">fun,</span><span> </span><span class="pre">*args,</span><span> </span><span class="pre">**kwds)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "unittest.TestCase.assertWarns")                                                            | `<span class="pre">fun(*args,</span><span> </span><span class="pre">**kwds)</span>` raises *warn*                                     | 3.2    |
| [`<span class="pre">assertWarnsRegex(warn,</span><span> </span><span class="pre">r,</span><span> </span><span class="pre">fun,</span><span> </span><span class="pre">*args,</span><span> </span><span class="pre">**kwds)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex "unittest.TestCase.assertWarnsRegex")   | `<span class="pre">fun(*args,</span><span> </span><span class="pre">**kwds)</span>` raises *warn* and the message matches regex *r* | 3.2    |
| [`<span class="pre">assertLogs(logger,</span><span> </span><span class="pre">level)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLogs "unittest.TestCase.assertLogs")                                                                                                                                                        | The `<span class="pre">with</span>` block logs on *logger* with minimum *level*                                                      | 3.4    |
| [`<span class="pre">assertNoLogs(logger,</span><span> </span><span class="pre">level)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNoLogs "unittest.TestCase.assertNoLogs")                                                                                                                                                  | The `<span class="pre">with</span>` block does not log on*logger* with minimum *level*                                               | 3.10   |

assertRaises**(** *exception* ,  *callable* ,  ****args*** ,  ***kwds* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "Link to this definition")assertRaises**(** *exception* ,  *** ,  *msg**=**None* **)**Test that an exception is raised when *callable* is called with any positional or keyword arguments that are also passed to [`<span class="pre">assertRaises()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "unittest.TestCase.assertRaises"). The test passes if *exception* is raised, is an error if another exception is raised, or fails if no exception is raised. To catch any of a group of exceptions, a tuple containing the exception classes may be passed as  *exception* .

If only the *exception* and possibly the *msg* arguments are given, return a context manager so that the code under test can be written inline rather than as a function:

```
with self.assertRaises(SomeException):
    do_something()
```

When used as a context manager, [`<span class="pre">assertRaises()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "unittest.TestCase.assertRaises") accepts the additional keyword argument  *msg* .

The context manager will store the caught exception object in its `<span class="pre">exception</span>` attribute. This can be useful if the intention is to perform additional checks on the exception raised:

```
with self.assertRaises(SomeException) as cm:
    do_something()

the_exception = cm.exception
self.assertEqual(the_exception.error_code, 3)
```

**Changed in version 3.1:** Added the ability to use [`<span class="pre">assertRaises()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "unittest.TestCase.assertRaises") as a context manager.

**Changed in version 3.2:** Added the `<span class="pre">exception</span>` attribute.

**Changed in version 3.3:** Added the *msg* keyword argument when used as a context manager.

assertRaisesRegex**(** *exception* ,  *regex* ,  *callable* ,  ****args*** ,  ***kwds* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex "Link to this definition")assertRaisesRegex**(** *exception* ,  *regex* ,  *** ,  *msg**=**None* **)**Like [`<span class="pre">assertRaises()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "unittest.TestCase.assertRaises") but also tests that *regex* matches on the string representation of the raised exception. *regex* may be a regular expression object or a string containing a regular expression suitable for use by [`<span class="pre">re.search()</span>`](https://docs.python.org/3/library/re.html#re.search "re.search"). Examples:

```
self.assertRaisesRegex(ValueError, "invalid literal for.*XYZ'$",
                       int, 'XYZ')
```

or:

```
with self.assertRaisesRegex(ValueError, 'literal'):
   int('XYZ')
```

**Added in version 3.1:** Added under the name `<span class="pre">assertRaisesRegexp</span>`.

**Changed in version 3.2:** Renamed to [`<span class="pre">assertRaisesRegex()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex "unittest.TestCase.assertRaisesRegex").

**Changed in version 3.3:** Added the *msg* keyword argument when used as a context manager.

assertWarns**(** *warning* ,  *callable* ,  ****args*** ,  ***kwds* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "Link to this definition")assertWarns**(** *warning* ,  *** ,  *msg**=**None* **)**Test that a warning is triggered when *callable* is called with any positional or keyword arguments that are also passed to [`<span class="pre">assertWarns()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "unittest.TestCase.assertWarns"). The test passes if *warning* is triggered and fails if it isn’t. Any exception is an error. To catch any of a group of warnings, a tuple containing the warning classes may be passed as  *warnings* .

If only the *warning* and possibly the *msg* arguments are given, return a context manager so that the code under test can be written inline rather than as a function:

```
with self.assertWarns(SomeWarning):
    do_something()
```

When used as a context manager, [`<span class="pre">assertWarns()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "unittest.TestCase.assertWarns") accepts the additional keyword argument  *msg* .

The context manager will store the caught warning object in its `<span class="pre">warning</span>` attribute, and the source line which triggered the warnings in the `<span class="pre">filename</span>` and `<span class="pre">lineno</span>` attributes. This can be useful if the intention is to perform additional checks on the warning caught:

```
with self.assertWarns(SomeWarning) as cm:
    do_something()

self.assertIn('myfile.py', cm.filename)
self.assertEqual(320, cm.lineno)
```

This method works regardless of the warning filters in place when it is called.

**Added in version 3.2.**

**Changed in version 3.3:** Added the *msg* keyword argument when used as a context manager.

assertWarnsRegex**(** *warning* ,  *regex* ,  *callable* ,  ****args*** ,  ***kwds* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex "Link to this definition")assertWarnsRegex**(** *warning* ,  *regex* ,  *** ,  *msg**=**None* **)**Like [`<span class="pre">assertWarns()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "unittest.TestCase.assertWarns") but also tests that *regex* matches on the message of the triggered warning. *regex* may be a regular expression object or a string containing a regular expression suitable for use by [`<span class="pre">re.search()</span>`](https://docs.python.org/3/library/re.html#re.search "re.search"). Example:

```
self.assertWarnsRegex(DeprecationWarning,
                      r'legacy_function\(\) is deprecated',
                      legacy_function, 'XYZ')
```

or:

```
with self.assertWarnsRegex(RuntimeWarning, 'unsafe frobnicating'):
    frobnicate('/etc/passwd')
```

**Added in version 3.2.**

**Changed in version 3.3:** Added the *msg* keyword argument when used as a context manager.

assertLogs**(** *logger**=**None* ,  *level**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLogs "Link to this definition")A context manager to test that at least one message is logged on the *logger* or one of its children, with at least the given  *level* .

If given, *logger* should be a [`<span class="pre">logging.Logger</span>`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") object or a [`<span class="pre">str</span>`](https://docs.python.org/3/library/stdtypes.html#str "str") giving the name of a logger. The default is the root logger, which will catch all messages that were not blocked by a non-propagating descendent logger.

If given, *level* should be either a numeric logging level or its string equivalent (for example either `<span class="pre">"ERROR"</span>` or [`<span class="pre">logging.ERROR</span>`](https://docs.python.org/3/library/logging.html#logging.ERROR "logging.ERROR")). The default is [`<span class="pre">logging.INFO</span>`](https://docs.python.org/3/library/logging.html#logging.INFO "logging.INFO").

The test passes if at least one message emitted inside the `<span class="pre">with</span>` block matches the *logger* and *level* conditions, otherwise it fails.

The object returned by the context manager is a recording helper which keeps tracks of the matching log messages. It has two attributes:

records[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.records "Link to this definition")A list of [`<span class="pre">logging.LogRecord</span>`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") objects of the matching log messages.

output[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.output "Link to this definition")A list of [`<span class="pre">str</span>`](https://docs.python.org/3/library/stdtypes.html#str "str") objects with the formatted output of matching messages.

Example:

```
with self.assertLogs('foo', level='INFO') as cm:
    logging.getLogger('foo').info('first message')
    logging.getLogger('foo.bar').error('second message')
self.assertEqual(cm.output, ['INFO:foo:first message',
                             'ERROR:foo.bar:second message'])
```

**Added in version 3.4.**

assertNoLogs**(** *logger**=**None* ,  *level**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNoLogs "Link to this definition")A context manager to test that no messages are logged on the *logger* or one of its children, with at least the given  *level* .

If given, *logger* should be a [`<span class="pre">logging.Logger</span>`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") object or a [`<span class="pre">str</span>`](https://docs.python.org/3/library/stdtypes.html#str "str") giving the name of a logger. The default is the root logger, which will catch all messages.

If given, *level* should be either a numeric logging level or its string equivalent (for example either `<span class="pre">"ERROR"</span>` or [`<span class="pre">logging.ERROR</span>`](https://docs.python.org/3/library/logging.html#logging.ERROR "logging.ERROR")). The default is [`<span class="pre">logging.INFO</span>`](https://docs.python.org/3/library/logging.html#logging.INFO "logging.INFO").

Unlike [`<span class="pre">assertLogs()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLogs "unittest.TestCase.assertLogs"), nothing will be returned by the context manager.

**Added in version 3.10.**

There are also other methods used to perform more specific checks, such as:

| Method                                                                                                                                                                                                                      | Checks that                                                                                                                                                          | New in |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| [`<span class="pre">assertAlmostEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual "unittest.TestCase.assertAlmostEqual")          | `<span class="pre">round(a-b,</span><span> </span><span class="pre">7)</span><span> </span><span class="pre">==</span><span> </span><span class="pre">0</span>` |        |
| [`<span class="pre">assertNotAlmostEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual "unittest.TestCase.assertNotAlmostEqual") | `<span class="pre">round(a-b,</span><span> </span><span class="pre">7)</span><span> </span><span class="pre">!=</span><span> </span><span class="pre">0</span>` |        |
| [`<span class="pre">assertGreater(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreater "unittest.TestCase.assertGreater")                      | `<span class="pre">a</span><span> </span><span class="pre">></span><span> </span><span class="pre">b</span>`                                                     | 3.1    |
| [`<span class="pre">assertGreaterEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreaterEqual "unittest.TestCase.assertGreaterEqual")       | `<span class="pre">a</span><span> </span><span class="pre">>=</span><span> </span><span class="pre">b</span>`                                                    | 3.1    |
| [`<span class="pre">assertLess(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLess "unittest.TestCase.assertLess")                               | `<span class="pre">a</span><span> </span><span class="pre"><</span><span> </span><span class="pre">b</span>`                                                     | 3.1    |
| [`<span class="pre">assertLessEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLessEqual "unittest.TestCase.assertLessEqual")                | `<span class="pre">a</span><span> </span><span class="pre"><=</span><span> </span><span class="pre">b</span>`                                                    | 3.1    |
| [`<span class="pre">assertRegex(s,</span><span> </span><span class="pre">r)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegex "unittest.TestCase.assertRegex")                            | `<span class="pre">r.search(s)</span>`                                                                                                                             | 3.1    |
| [`<span class="pre">assertNotRegex(s,</span><span> </span><span class="pre">r)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotRegex "unittest.TestCase.assertNotRegex")                   | `<span class="pre">not</span><span> </span><span class="pre">r.search(s)</span>`                                                                                  | 3.2    |
| [`<span class="pre">assertCountEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertCountEqual "unittest.TestCase.assertCountEqual")             | *a* and *b* have the same elements in the same number, regardless of their order.                                                                                | 3.2    |

assertAlmostEqual**(** *first* ,  *second* ,  *places**=**7* ,  *msg**=**None* ,  *delta**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual "Link to this definition")assertNotAlmostEqual**(** *first* ,  *second* ,  *places**=**7* ,  *msg**=**None* ,  *delta**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual "Link to this definition")Test that *first* and *second* are approximately (or not approximately) equal by computing the difference, rounding to the given number of decimal *places* (default 7), and comparing to zero. Note that these methods round the values to the given number of *decimal places* (i.e. like the [`<span class="pre">round()</span>`](https://docs.python.org/3/library/functions.html#round "round") function) and not  *significant digits* .

If *delta* is supplied instead of *places* then the difference between *first* and *second* must be less or equal to (or greater than)  *delta* .

Supplying both *delta* and *places* raises a [`<span class="pre">TypeError</span>`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").

**Changed in version 3.2:** [`<span class="pre">assertAlmostEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual "unittest.TestCase.assertAlmostEqual") automatically considers almost equal objects that compare equal. [`<span class="pre">assertNotAlmostEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual "unittest.TestCase.assertNotAlmostEqual") automatically fails if the objects compare equal. Added the *delta* keyword argument.

assertGreater**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreater "Link to this definition")assertGreaterEqual**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreaterEqual "Link to this definition")assertLess**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLess "Link to this definition")assertLessEqual**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLessEqual "Link to this definition")Test that *first* is respectively >, >=, < or <= than *second* depending on the method name. If not, the test will fail:

**>>>**

```
>>> self.assertGreaterEqual(3, 4)
AssertionError: "3" unexpectedly not greater than or equal to "4"
```

**Added in version 3.1.**

assertRegex**(** *text* ,  *regex* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegex "Link to this definition")assertNotRegex**(** *text* ,  *regex* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotRegex "Link to this definition")Test that a *regex* search matches (or does not match)  *text* . In case of failure, the error message will include the pattern and the *text* (or the pattern and the part of *text* that unexpectedly matched). *regex* may be a regular expression object or a string containing a regular expression suitable for use by [`<span class="pre">re.search()</span>`](https://docs.python.org/3/library/re.html#re.search "re.search").

**Added in version 3.1:** Added under the name `<span class="pre">assertRegexpMatches</span>`.

**Changed in version 3.2:** The method `<span class="pre">assertRegexpMatches()</span>` has been renamed to [`<span class="pre">assertRegex()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegex "unittest.TestCase.assertRegex").

**Added in version 3.2:** [`<span class="pre">assertNotRegex()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotRegex "unittest.TestCase.assertNotRegex").

assertCountEqual**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertCountEqual "Link to this definition")Test that sequence *first* contains the same elements as  *second* , regardless of their order. When they don’t, an error message listing the differences between the sequences will be generated.

Duplicate elements are *not* ignored when comparing *first* and  *second* . It verifies whether each element has the same count in both sequences. Equivalent to: `<span class="pre">assertEqual(Counter(list(first)),</span><span> </span><span class="pre">Counter(list(second)))</span>` but works with sequences of unhashable objects as well.

**Added in version 3.2.**

The [`<span class="pre">assertEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual") method dispatches the equality check for objects of the same type to different type-specific methods. These methods are already implemented for most of the built-in types, but it’s also possible to register new methods using [`<span class="pre">addTypeEqualityFunc()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addTypeEqualityFunc "unittest.TestCase.addTypeEqualityFunc"):

addTypeEqualityFunc**(** *typeobj* ,  *function* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addTypeEqualityFunc "Link to this definition")Registers a type-specific method called by [`<span class="pre">assertEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual") to check if two objects of exactly the same *typeobj* (not subclasses) compare equal. *function* must take two positional arguments and a third msg=None keyword argument just as [`<span class="pre">assertEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual") does. It must raise [`<span class="pre">self.failureException(msg)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.failureException "unittest.TestCase.failureException") when inequality between the first two parameters is detected – possibly providing useful information and explaining the inequalities in details in the error message.

**Added in version 3.1.**

The list of type-specific methods automatically used by [`<span class="pre">assertEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual") are summarized in the following table. Note that it’s usually not necessary to invoke these methods directly.

| Method                                                                                                                                                                                                                      | Used to compare    | New in |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------ |
| [`<span class="pre">assertMultiLineEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual "unittest.TestCase.assertMultiLineEqual") | strings            | 3.1    |
| [`<span class="pre">assertSequenceEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSequenceEqual "unittest.TestCase.assertSequenceEqual")    | sequences          | 3.1    |
| [`<span class="pre">assertListEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual "unittest.TestCase.assertListEqual")                | lists              | 3.1    |
| [`<span class="pre">assertTupleEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual "unittest.TestCase.assertTupleEqual")             | tuples             | 3.1    |
| [`<span class="pre">assertSetEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSetEqual "unittest.TestCase.assertSetEqual")                   | sets or frozensets | 3.1    |
| [`<span class="pre">assertDictEqual(a,</span><span> </span><span class="pre">b)</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictEqual "unittest.TestCase.assertDictEqual")                | dicts              | 3.1    |

assertMultiLineEqual**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual "Link to this definition")Test that the multiline string *first* is equal to the string  *second* . When not equal a diff of the two strings highlighting the differences will be included in the error message. This method is used by default when comparing strings with [`<span class="pre">assertEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual").

**Added in version 3.1.**

assertSequenceEqual**(** *first* ,  *second* ,  *msg**=**None* ,  *seq_type**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSequenceEqual "Link to this definition")Tests that two sequences are equal. If a *seq_type* is supplied, both *first* and *second* must be instances of *seq_type* or a failure will be raised. If the sequences are different an error message is constructed that shows the difference between the two.

This method is not called directly by [`<span class="pre">assertEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual"), but it’s used to implement [`<span class="pre">assertListEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual "unittest.TestCase.assertListEqual") and [`<span class="pre">assertTupleEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual "unittest.TestCase.assertTupleEqual").

**Added in version 3.1.**

assertListEqual**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual "Link to this definition")assertTupleEqual**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual "Link to this definition")Tests that two lists or tuples are equal. If not, an error message is constructed that shows only the differences between the two. An error is also raised if either of the parameters are of the wrong type. These methods are used by default when comparing lists or tuples with [`<span class="pre">assertEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual").

**Added in version 3.1.**

assertSetEqual**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSetEqual "Link to this definition")Tests that two sets are equal. If not, an error message is constructed that lists the differences between the sets. This method is used by default when comparing sets or frozensets with [`<span class="pre">assertEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual").

Fails if either of *first* or *second* does not have a `<span class="pre">set.difference()</span>` method.

**Added in version 3.1.**

assertDictEqual**(** *first* ,  *second* ,  *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictEqual "Link to this definition")Test that two dictionaries are equal. If not, an error message is constructed that shows the differences in the dictionaries. This method will be used by default to compare dictionaries in calls to [`<span class="pre">assertEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual").

**Added in version 3.1.**

Finally the [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") provides the following methods and attributes:

fail**(** *msg**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.fail "Link to this definition")Signals a test failure unconditionally, with *msg* or `<span class="pre">None</span>` for the error message.

failureException[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.failureException "Link to this definition")This class attribute gives the exception raised by the test method. If a test framework needs to use a specialized exception, possibly to carry additional information, it must subclass this exception in order to “play fair” with the framework. The initial value of this attribute is [`<span class="pre">AssertionError</span>`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError").

longMessage[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.longMessage "Link to this definition")This class attribute determines what happens when a custom failure message is passed as the msg argument to an assertXYY call that fails. `<span class="pre">True</span>` is the default value. In this case, the custom message is appended to the end of the standard failure message. When set to `<span class="pre">False</span>`, the custom message replaces the standard message.

The class setting can be overridden in individual test methods by assigning an instance attribute, self.longMessage, to `<span class="pre">True</span>` or `<span class="pre">False</span>` before calling the assert methods.

The class setting gets reset before each test call.

**Added in version 3.1.**

maxDiff[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.maxDiff "Link to this definition")This attribute controls the maximum length of diffs output by assert methods that report diffs on failure. It defaults to 80*8 characters. Assert methods affected by this attribute are [`<span class="pre">assertSequenceEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSequenceEqual "unittest.TestCase.assertSequenceEqual") (including all the sequence comparison methods that delegate to it), [`<span class="pre">assertDictEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictEqual "unittest.TestCase.assertDictEqual") and [`<span class="pre">assertMultiLineEqual()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual "unittest.TestCase.assertMultiLineEqual").

Setting `<span class="pre">maxDiff</span>` to `<span class="pre">None</span>` means that there is no maximum length of diffs.

**Added in version 3.2.**

Testing frameworks can use the following methods to collect information on the test:

countTestCases**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.countTestCases "Link to this definition")Return the number of tests represented by this test object. For [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances, this will always be `<span class="pre">1</span>`.

defaultTestResult**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.defaultTestResult "Link to this definition")Return an instance of the test result class that should be used for this test case class (if no other result instance is provided to the [`<span class="pre">run()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.run "unittest.TestCase.run") method).

For [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances, this will always be an instance of [`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult"); subclasses of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") should override this as necessary.

id**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.id "Link to this definition")Return a string identifying the specific test case. This is usually the full name of the test method, including the module and class name.

shortDescription**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.shortDescription "Link to this definition")Returns a description of the test, or `<span class="pre">None</span>` if no description has been provided. The default implementation of this method returns the first line of the test method’s docstring, if available, or `<span class="pre">None</span>`.

**Changed in version 3.1:** In 3.1 this was changed to add the test name to the short description even in the presence of a docstring. This caused compatibility issues with unittest extensions and adding the test name was moved to the [`<span class="pre">TextTestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TextTestResult "unittest.TextTestResult") in Python 3.2.

addCleanup**(** *function* ,  */* ,  ****args*** ,  ***kwargs* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addCleanup "Link to this definition")Add a function to be called after [`<span class="pre">tearDown()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") to cleanup resources used during the test. Functions will be called in reverse order to the order they are added (LIFO). They are called with any arguments and keyword arguments passed into [`<span class="pre">addCleanup()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addCleanup "unittest.TestCase.addCleanup") when they are added.

If [`<span class="pre">setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") fails, meaning that [`<span class="pre">tearDown()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") is not called, then any cleanup functions added will still be called.

**Added in version 3.1.**

enterContext**(** *cm* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.enterContext "Link to this definition")Enter the supplied [context manager](https://docs.python.org/3/glossary.html#term-context-manager). If successful, also add its [`<span class="pre">__exit__()</span>`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__") method as a cleanup function by [`<span class="pre">addCleanup()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addCleanup "unittest.TestCase.addCleanup") and return the result of the [`<span class="pre">__enter__()</span>`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__") method.

**Added in version 3.11.**

doCleanups**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.doCleanups "Link to this definition")This method is called unconditionally after [`<span class="pre">tearDown()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown"), or after [`<span class="pre">setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") if [`<span class="pre">setUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") raises an exception.

It is responsible for calling all the cleanup functions added by [`<span class="pre">addCleanup()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addCleanup "unittest.TestCase.addCleanup"). If you need cleanup functions to be called *prior* to [`<span class="pre">tearDown()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") then you can call [`<span class="pre">doCleanups()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.doCleanups "unittest.TestCase.doCleanups") yourself.

[`<span class="pre">doCleanups()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.doCleanups "unittest.TestCase.doCleanups") pops methods off the stack of cleanup functions one at a time, so it can be called at any time.

**Added in version 3.1.**

*classmethod *addClassCleanup**(** *function* ,  */* ,  ****args*** ,  ***kwargs* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addClassCleanup "Link to this definition")Add a function to be called after [`<span class="pre">tearDownClass()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "unittest.TestCase.tearDownClass") to cleanup resources used during the test class. Functions will be called in reverse order to the order they are added (LIFO). They are called with any arguments and keyword arguments passed into [`<span class="pre">addClassCleanup()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addClassCleanup "unittest.TestCase.addClassCleanup") when they are added.

If [`<span class="pre">setUpClass()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass "unittest.TestCase.setUpClass") fails, meaning that [`<span class="pre">tearDownClass()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "unittest.TestCase.tearDownClass") is not called, then any cleanup functions added will still be called.

**Added in version 3.8.**

*classmethod *enterClassContext**(** *cm* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.enterClassContext "Link to this definition")Enter the supplied [context manager](https://docs.python.org/3/glossary.html#term-context-manager). If successful, also add its [`<span class="pre">__exit__()</span>`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__") method as a cleanup function by [`<span class="pre">addClassCleanup()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addClassCleanup "unittest.TestCase.addClassCleanup") and return the result of the [`<span class="pre">__enter__()</span>`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__") method.

**Added in version 3.11.**

*classmethod *doClassCleanups**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestCase.doClassCleanups "Link to this definition")This method is called unconditionally after [`<span class="pre">tearDownClass()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "unittest.TestCase.tearDownClass"), or after [`<span class="pre">setUpClass()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass "unittest.TestCase.setUpClass") if [`<span class="pre">setUpClass()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass "unittest.TestCase.setUpClass") raises an exception.

It is responsible for calling all the cleanup functions added by [`<span class="pre">addClassCleanup()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addClassCleanup "unittest.TestCase.addClassCleanup"). If you need cleanup functions to be called *prior* to [`<span class="pre">tearDownClass()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "unittest.TestCase.tearDownClass") then you can call [`<span class="pre">doClassCleanups()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.doClassCleanups "unittest.TestCase.doClassCleanups") yourself.

[`<span class="pre">doClassCleanups()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.doClassCleanups "unittest.TestCase.doClassCleanups") pops methods off the stack of cleanup functions one at a time, so it can be called at any time.

**Added in version 3.8.**

*class *unittest.**IsolatedAsyncioTestCase**( *methodName**=**'runTest'* **)**[](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase "Link to this definition")This class provides an API similar to [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") and also accepts coroutines as test functions.

**Added in version 3.8.**

*coroutine *asyncSetUp**(**)[](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.asyncSetUp "Link to this definition")Method called to prepare the test fixture. This is called after `<span class="pre">setUp()</span>`. This is called immediately before calling the test method; other than [`<span class="pre">AssertionError</span>`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") or [`<span class="pre">SkipTest</span>`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest"), any exception raised by this method will be considered an error rather than a test failure. The default implementation does nothing.

*coroutine *asyncTearDown**(**)[](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.asyncTearDown "Link to this definition")Method called immediately after the test method has been called and the result recorded. This is called before `<span class="pre">tearDown()</span>`. This is called even if the test method raised an exception, so the implementation in subclasses may need to be particularly careful about checking internal state. Any exception, other than [`<span class="pre">AssertionError</span>`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") or [`<span class="pre">SkipTest</span>`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest"), raised by this method will be considered an additional error rather than a test failure (thus increasing the total number of reported errors). This method will only be called if the [`<span class="pre">asyncSetUp()</span>`](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.asyncSetUp "unittest.IsolatedAsyncioTestCase.asyncSetUp") succeeds, regardless of the outcome of the test method. The default implementation does nothing.

addAsyncCleanup**(** *function* ,  */* ,  ****args*** ,  ***kwargs* **)**[](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.addAsyncCleanup "Link to this definition")This method accepts a coroutine that can be used as a cleanup function.

*coroutine *enterAsyncContext**(** *cm* **)**[](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.enterAsyncContext "Link to this definition")Enter the supplied [asynchronous context manager](https://docs.python.org/3/glossary.html#term-asynchronous-context-manager). If successful, also add its [`<span class="pre">__aexit__()</span>`](https://docs.python.org/3/reference/datamodel.html#object.__aexit__ "object.__aexit__") method as a cleanup function by [`<span class="pre">addAsyncCleanup()</span>`](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.addAsyncCleanup "unittest.IsolatedAsyncioTestCase.addAsyncCleanup") and return the result of the [`<span class="pre">__aenter__()</span>`](https://docs.python.org/3/reference/datamodel.html#object.__aenter__ "object.__aenter__") method.

**Added in version 3.11.**

run**(** *result**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.run "Link to this definition")Sets up a new event loop to run the test, collecting the result into the [`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") object passed as  *result* . If *result* is omitted or `<span class="pre">None</span>`, a temporary result object is created (by calling the `<span class="pre">defaultTestResult()</span>` method) and used. The result object is returned to [`<span class="pre">run()</span>`](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.run "unittest.IsolatedAsyncioTestCase.run")’s caller. At the end of the test all the tasks in the event loop are cancelled.

An example illustrating the order:

```
from unittest import IsolatedAsyncioTestCase

events = []


class Test(IsolatedAsyncioTestCase):


    def setUp(self):
        events.append("setUp")

    async def asyncSetUp(self):
        self._async_connection = await AsyncConnection()
        events.append("asyncSetUp")

    async def test_response(self):
        events.append("test_response")
        response = await self._async_connection.get("https://example.com")
        self.assertEqual(response.status_code, 200)
        self.addAsyncCleanup(self.on_cleanup)

    def tearDown(self):
        events.append("tearDown")

    async def asyncTearDown(self):
        await self._async_connection.close()
        events.append("asyncTearDown")

    async def on_cleanup(self):
        events.append("cleanup")

if __name__ == "__main__":
    unittest.main()
```

After running the test, `<span class="pre">events</span>` would contain `<span class="pre">["setUp",</span><span> </span><span class="pre">"asyncSetUp",</span><span> </span><span class="pre">"test_response",</span><span> </span><span class="pre">"asyncTearDown",</span><span> </span><span class="pre">"tearDown",</span><span> </span><span class="pre">"cleanup"]</span>`.

*class *unittest.**FunctionTestCase**( *testFunc* ,  *setUp**=**None* ,  *tearDown**=**None* ,  *description**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.FunctionTestCase "Link to this definition")This class implements the portion of the [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") interface which allows the test runner to drive the test, but does not provide the methods which test code can use to check and report errors. This is used to create test cases using legacy test code, allowing it to be integrated into a [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.")-based test framework.

### Grouping tests

*class *unittest.**TestSuite**( *tests**=**()* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "Link to this definition")This class represents an aggregation of individual test cases and test suites. The class presents the interface needed by the test runner to allow it to be run as any other test case. Running a [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") instance is the same as iterating over the suite, running each test individually.

If *tests* is given, it must be an iterable of individual test cases or other test suites that will be used to build the suite initially. Additional methods are provided to add test cases and suites to the collection later on.

[`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") objects behave much like [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") objects, except they do not actually implement a test. Instead, they are used to aggregate tests into groups of tests that should be run together. Some additional methods are available to add tests to [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") instances:

addTest**(** *test* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.addTest "Link to this definition")Add a [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") or [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") to the suite.

addTests**(** *tests* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.addTests "Link to this definition")Add all the tests from an iterable of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") and [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") instances to this test suite.

This is equivalent to iterating over  *tests* , calling [`<span class="pre">addTest()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.addTest "unittest.TestSuite.addTest") for each element.

[`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") shares the following methods with [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase"):

run**(** *result* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.run "Link to this definition")Run the tests associated with this suite, collecting the result into the test result object passed as  *result* . Note that unlike [`<span class="pre">TestCase.run()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.run "unittest.TestCase.run"), [`<span class="pre">TestSuite.run()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.run "unittest.TestSuite.run") requires the result object to be passed in.

debug**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.debug "Link to this definition")Run the tests associated with this suite without collecting the result. This allows exceptions raised by the test to be propagated to the caller and can be used to support running tests under a debugger.

countTestCases**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.countTestCases "Link to this definition")Return the number of tests represented by this test object, including all individual tests and sub-suites.

__iter__**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.__iter__ "Link to this definition")Tests grouped by a [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") are always accessed by iteration. Subclasses can lazily provide tests by overriding `<span class="pre">__iter__()</span>`. Note that this method may be called several times on a single suite (for example when counting tests or comparing for equality) so the tests returned by repeated iterations before [`<span class="pre">TestSuite.run()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.run "unittest.TestSuite.run") must be the same for each call iteration. After [`<span class="pre">TestSuite.run()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.run "unittest.TestSuite.run"), callers should not rely on the tests returned by this method unless the caller uses a subclass that overrides `<span class="pre">TestSuite._removeTestAtIndex()</span>` to preserve test references.

**Changed in version 3.2:** In earlier versions the [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") accessed tests directly rather than through iteration, so overriding `<span class="pre">__iter__()</span>` wasn’t sufficient for providing tests.

**Changed in version 3.4:** In earlier versions the [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") held references to each [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") after [`<span class="pre">TestSuite.run()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.run "unittest.TestSuite.run"). Subclasses can restore that behavior by overriding `<span class="pre">TestSuite._removeTestAtIndex()</span>`.

In the typical usage of a [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") object, the [`<span class="pre">run()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.run "unittest.TestSuite.run") method is invoked by a `<span class="pre">TestRunner</span>` rather than by the end-user test harness.

### Loading and running tests

*class *unittest.**TestLoader**[](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "Link to this definition")The [`<span class="pre">TestLoader</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") class is used to create test suites from classes and modules. Normally, there is no need to create an instance of this class; the [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") module provides an instance that can be shared as [`<span class="pre">unittest.defaultTestLoader</span>`](https://docs.python.org/3/library/unittest.html#unittest.defaultTestLoader "unittest.defaultTestLoader"). Using a subclass or instance, however, allows customization of some configurable properties.

[`<span class="pre">TestLoader</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") objects have the following attributes:

errors[](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.errors "Link to this definition")A list of the non-fatal errors encountered while loading tests. Not reset by the loader at any point. Fatal errors are signalled by the relevant method raising an exception to the caller. Non-fatal errors are also indicated by a synthetic test that will raise the original error when run.

**Added in version 3.5.**

[`<span class="pre">TestLoader</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") objects have the following methods:

loadTestsFromTestCase**(** *testCaseClass* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromTestCase "Link to this definition")Return a suite of all test cases contained in the [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")-derived `<span class="pre">testCaseClass</span>`.

A test case instance is created for each method named by [`<span class="pre">getTestCaseNames()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.getTestCaseNames "unittest.TestLoader.getTestCaseNames"). By default these are the method names beginning with `<span class="pre">test</span>`. If [`<span class="pre">getTestCaseNames()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.getTestCaseNames "unittest.TestLoader.getTestCaseNames") returns no methods, but the `<span class="pre">runTest()</span>` method is implemented, a single test case is created for that method instead.

loadTestsFromModule**(** *module* ,  *** ,  *pattern**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromModule "Link to this definition")Return a suite of all test cases contained in the given module. This method searches *module* for classes derived from [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") and creates an instance of the class for each test method defined for the class.

Note

 While using a hierarchy of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")-derived classes can be convenient in sharing fixtures and helper functions, defining test methods on base classes that are not intended to be instantiated directly does not play well with this method. Doing so, however, can be useful when the fixtures are different and defined in subclasses.

If a module provides a `<span class="pre">load_tests</span>` function it will be called to load the tests. This allows modules to customize test loading. This is the [load_tests protocol](https://docs.python.org/3/library/unittest.html#id1). The *pattern* argument is passed as the third argument to `<span class="pre">load_tests</span>`.

**Changed in version 3.2:** Support for `<span class="pre">load_tests</span>` added.

**Changed in version 3.5:** Support for a keyword-only argument *pattern* has been added.

**Changed in version 3.12:** The undocumented and unofficial *use_load_tests* parameter has been removed.

loadTestsFromName**(** *name* ,  *module**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromName "Link to this definition")Return a suite of all test cases given a string specifier.

The specifier *name* is a “dotted name” that may resolve either to a module, a test case class, a test method within a test case class, a [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") instance, or a callable object which returns a [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") or [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") instance. These checks are applied in the order listed here; that is, a method on a possible test case class will be picked up as “a test method within a test case class”, rather than “a callable object”.

For example, if you have a module `<span class="pre">SampleTests</span>` containing a [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")-derived class `<span class="pre">SampleTestCase</span>` with three test methods (`<span class="pre">test_one()</span>`, `<span class="pre">test_two()</span>`, and `<span class="pre">test_three()</span>`), the specifier `<span class="pre">'SampleTests.SampleTestCase'</span>` would cause this method to return a suite which will run all three test methods. Using the specifier `<span class="pre">'SampleTests.SampleTestCase.test_two'</span>` would cause it to return a test suite which will run only the `<span class="pre">test_two()</span>` test method. The specifier can refer to modules and packages which have not been imported; they will be imported as a side-effect.

The method optionally resolves *name* relative to the given  *module* .

**Changed in version 3.5:** If an [`<span class="pre">ImportError</span>`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") or [`<span class="pre">AttributeError</span>`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") occurs while traversing *name* then a synthetic test that raises that error when run will be returned. These errors are included in the errors accumulated by self.errors.

loadTestsFromNames**(** *names* ,  *module**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromNames "Link to this definition")Similar to [`<span class="pre">loadTestsFromName()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromName "unittest.TestLoader.loadTestsFromName"), but takes a sequence of names rather than a single name. The return value is a test suite which supports all the tests defined for each name.

getTestCaseNames**(** *testCaseClass* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.getTestCaseNames "Link to this definition")Return a sorted sequence of method names found within  *testCaseClass* ; this should be a subclass of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase").

discover**(** *start_dir* ,  *pattern**=**'test*.py'* ,  *top_level_dir**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.discover "Link to this definition")Find all the test modules by recursing into subdirectories from the specified start directory, and return a TestSuite object containing them. Only test files that match *pattern* will be loaded. (Using shell style pattern matching.) Only module names that are importable (i.e. are valid Python identifiers) will be loaded.

All test modules must be importable from the top level of the project. If the start directory is not the top level directory then *top_level_dir* must be specified separately.

If importing a module fails, for example due to a syntax error, then this will be recorded as a single error and discovery will continue. If the import failure is due to [`<span class="pre">SkipTest</span>`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") being raised, it will be recorded as a skip instead of an error.

If a package (a directory containing a file named `<span class="pre">__init__.py</span>`) is found, the package will be checked for a `<span class="pre">load_tests</span>` function. If this exists then it will be called `<span class="pre">package.load_tests(loader,</span><span> </span><span class="pre">tests,</span><span> </span><span class="pre">pattern)</span>`. Test discovery takes care to ensure that a package is only checked for tests once during an invocation, even if the load_tests function itself calls `<span class="pre">loader.discover</span>`.

If `<span class="pre">load_tests</span>` exists then discovery does *not* recurse into the package, `<span class="pre">load_tests</span>` is responsible for loading all tests in the package.

The pattern is deliberately not stored as a loader attribute so that packages can continue discovery themselves.

*top_level_dir* is stored internally, and used as a default to any nested calls to `<span class="pre">discover()</span>`. That is, if a package’s `<span class="pre">load_tests</span>` calls `<span class="pre">loader.discover()</span>`, it does not need to pass this argument.

*start_dir* can be a dotted module name as well as a directory.

**Added in version 3.2.**

**Changed in version 3.4:** Modules that raise [`<span class="pre">SkipTest</span>`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") on import are recorded as skips, not errors.

**Changed in version 3.4:** *start_dir* can be a [namespace packages](https://docs.python.org/3/glossary.html#term-namespace-package).

**Changed in version 3.4:** Paths are sorted before being imported so that execution order is the same even if the underlying file system’s ordering is not dependent on file name.

**Changed in version 3.5:** Found packages are now checked for `<span class="pre">load_tests</span>` regardless of whether their path matches  *pattern* , because it is impossible for a package name to match the default pattern.

**Changed in version 3.11:** *start_dir* can not be a [namespace packages](https://docs.python.org/3/glossary.html#term-namespace-package). It has been broken since Python 3.7 and Python 3.11 officially remove it.

**Changed in version 3.12.4:** *top_level_dir* is only stored for the duration of *discover* call.

The following attributes of a [`<span class="pre">TestLoader</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") can be configured either by subclassing or assignment on an instance:

testMethodPrefix[](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.testMethodPrefix "Link to this definition")String giving the prefix of method names which will be interpreted as test methods. The default value is `<span class="pre">'test'</span>`.

This affects [`<span class="pre">getTestCaseNames()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.getTestCaseNames "unittest.TestLoader.getTestCaseNames") and all the `<span class="pre">loadTestsFrom*</span>` methods.

sortTestMethodsUsing[](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.sortTestMethodsUsing "Link to this definition")Function to be used to compare method names when sorting them in [`<span class="pre">getTestCaseNames()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.getTestCaseNames "unittest.TestLoader.getTestCaseNames") and all the `<span class="pre">loadTestsFrom*</span>` methods.

suiteClass[](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.suiteClass "Link to this definition")Callable object that constructs a test suite from a list of tests. No methods on the resulting object are needed. The default value is the [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") class.

This affects all the `<span class="pre">loadTestsFrom*</span>` methods.

testNamePatterns[](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.testNamePatterns "Link to this definition")List of Unix shell-style wildcard test name patterns that test methods have to match to be included in test suites (see `<span class="pre">-k</span>` option).

If this attribute is not `<span class="pre">None</span>` (the default), all test methods to be included in test suites must match one of the patterns in this list. Note that matches are always performed using [`<span class="pre">fnmatch.fnmatchcase()</span>`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "fnmatch.fnmatchcase"), so unlike patterns passed to the `<span class="pre">-k</span>` option, simple substring patterns will have to be converted using `<span class="pre">*</span>` wildcards.

This affects all the `<span class="pre">loadTestsFrom*</span>` methods.

**Added in version 3.7.**

*class *unittest.**TestResult**[](https://docs.python.org/3/library/unittest.html#unittest.TestResult "Link to this definition")This class is used to compile information about which tests have succeeded and which have failed.

A [`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") object stores the results of a set of tests. The [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") and [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") classes ensure that results are properly recorded; test authors do not need to worry about recording the outcome of tests.

Testing frameworks built on top of [`<span class="pre">unittest</span>`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") may want access to the [`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") object generated by running a set of tests for reporting purposes; a [`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") instance is returned by the `<span class="pre">TestRunner.run()</span>` method for this purpose.

[`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") instances have the following attributes that will be of interest when inspecting the results of running a set of tests:

errors[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.errors "Link to this definition")A list containing 2-tuples of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances and strings holding formatted tracebacks. Each tuple represents a test which raised an unexpected exception.

failures[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.failures "Link to this definition")A list containing 2-tuples of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances and strings holding formatted tracebacks. Each tuple represents a test where a failure was explicitly signalled using the [assert* methods](https://docs.python.org/3/library/unittest.html#assert-methods).

skipped[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.skipped "Link to this definition")A list containing 2-tuples of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances and strings holding the reason for skipping the test.

**Added in version 3.1.**

expectedFailures[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.expectedFailures "Link to this definition")A list containing 2-tuples of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances and strings holding formatted tracebacks. Each tuple represents an expected failure or error of the test case.

unexpectedSuccesses[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.unexpectedSuccesses "Link to this definition")A list containing [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances that were marked as expected failures, but succeeded.

collectedDurations[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.collectedDurations "Link to this definition")A list containing 2-tuples of test case names and floats representing the elapsed time of each test which was run.

**Added in version 3.12.**

shouldStop[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.shouldStop "Link to this definition")Set to `<span class="pre">True</span>` when the execution of tests should stop by [`<span class="pre">stop()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stop "unittest.TestResult.stop").

testsRun[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.testsRun "Link to this definition")The total number of tests run so far.

buffer[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.buffer "Link to this definition")If set to true, `<span class="pre">sys.stdout</span>` and `<span class="pre">sys.stderr</span>` will be buffered in between [`<span class="pre">startTest()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.startTest "unittest.TestResult.startTest") and [`<span class="pre">stopTest()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stopTest "unittest.TestResult.stopTest") being called. Collected output will only be echoed onto the real `<span class="pre">sys.stdout</span>` and `<span class="pre">sys.stderr</span>` if the test fails or errors. Any output is also attached to the failure / error message.

**Added in version 3.2.**

failfast[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.failfast "Link to this definition")If set to true [`<span class="pre">stop()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stop "unittest.TestResult.stop") will be called on the first failure or error, halting the test run.

**Added in version 3.2.**

tb_locals[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.tb_locals "Link to this definition")If set to true then local variables will be shown in tracebacks.

**Added in version 3.5.**

wasSuccessful**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.wasSuccessful "Link to this definition")Return `<span class="pre">True</span>` if all tests run so far have passed, otherwise returns `<span class="pre">False</span>`.

**Changed in version 3.4:** Returns `<span class="pre">False</span>` if there were any [`<span class="pre">unexpectedSuccesses</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.unexpectedSuccesses "unittest.TestResult.unexpectedSuccesses") from tests marked with the [`<span class="pre">expectedFailure()</span>`](https://docs.python.org/3/library/unittest.html#unittest.expectedFailure "unittest.expectedFailure") decorator.

stop**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stop "Link to this definition")This method can be called to signal that the set of tests being run should be aborted by setting the [`<span class="pre">shouldStop</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.shouldStop "unittest.TestResult.shouldStop") attribute to `<span class="pre">True</span>`. `<span class="pre">TestRunner</span>` objects should respect this flag and return without running any additional tests.

For example, this feature is used by the [`<span class="pre">TextTestRunner</span>`](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner "unittest.TextTestRunner") class to stop the test framework when the user signals an interrupt from the keyboard. Interactive tools which provide `<span class="pre">TestRunner</span>` implementations can use this in a similar manner.

The following methods of the [`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") class are used to maintain the internal data structures, and may be extended in subclasses to support additional reporting requirements. This is particularly useful in building tools which support interactive reporting while tests are being run.

startTest**(** *test* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.startTest "Link to this definition")Called when the test case *test* is about to be run.

stopTest**(** *test* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stopTest "Link to this definition")Called after the test case *test* has been executed, regardless of the outcome.

startTestRun**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.startTestRun "Link to this definition")Called once before any tests are executed.

**Added in version 3.1.**

stopTestRun**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stopTestRun "Link to this definition")Called once after all tests are executed.

**Added in version 3.1.**

addError**(** *test* ,  *err* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addError "Link to this definition")Called when the test case *test* raises an unexpected exception. *err* is a tuple of the form returned by [`<span class="pre">sys.exc_info()</span>`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info"): `<span class="pre">(type,</span><span> </span><span class="pre">value,</span><span> </span><span class="pre">traceback)</span>`.

The default implementation appends a tuple `<span class="pre">(test,</span><span> </span><span class="pre">formatted_err)</span>` to the instance’s [`<span class="pre">errors</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.errors "unittest.TestResult.errors") attribute, where *formatted_err* is a formatted traceback derived from  *err* .

addFailure**(** *test* ,  *err* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addFailure "Link to this definition")Called when the test case *test* signals a failure. *err* is a tuple of the form returned by [`<span class="pre">sys.exc_info()</span>`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info"): `<span class="pre">(type,</span><span> </span><span class="pre">value,</span><span> </span><span class="pre">traceback)</span>`.

The default implementation appends a tuple `<span class="pre">(test,</span><span> </span><span class="pre">formatted_err)</span>` to the instance’s [`<span class="pre">failures</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.failures "unittest.TestResult.failures") attribute, where *formatted_err* is a formatted traceback derived from  *err* .

addSuccess**(** *test* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addSuccess "Link to this definition")Called when the test case *test* succeeds.

The default implementation does nothing.

addSkip**(** *test* ,  *reason* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addSkip "Link to this definition")Called when the test case *test* is skipped. *reason* is the reason the test gave for skipping.

The default implementation appends a tuple `<span class="pre">(test,</span><span> </span><span class="pre">reason)</span>` to the instance’s [`<span class="pre">skipped</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.skipped "unittest.TestResult.skipped") attribute.

addExpectedFailure**(** *test* ,  *err* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addExpectedFailure "Link to this definition")Called when the test case *test* fails or errors, but was marked with the [`<span class="pre">expectedFailure()</span>`](https://docs.python.org/3/library/unittest.html#unittest.expectedFailure "unittest.expectedFailure") decorator.

The default implementation appends a tuple `<span class="pre">(test,</span><span> </span><span class="pre">formatted_err)</span>` to the instance’s [`<span class="pre">expectedFailures</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.expectedFailures "unittest.TestResult.expectedFailures") attribute, where *formatted_err* is a formatted traceback derived from  *err* .

addUnexpectedSuccess**(** *test* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addUnexpectedSuccess "Link to this definition")Called when the test case *test* was marked with the [`<span class="pre">expectedFailure()</span>`](https://docs.python.org/3/library/unittest.html#unittest.expectedFailure "unittest.expectedFailure") decorator, but succeeded.

The default implementation appends the test to the instance’s [`<span class="pre">unexpectedSuccesses</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.unexpectedSuccesses "unittest.TestResult.unexpectedSuccesses") attribute.

addSubTest**(** *test* ,  *subtest* ,  *outcome* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addSubTest "Link to this definition")Called when a subtest finishes. *test* is the test case corresponding to the test method. *subtest* is a custom [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instance describing the subtest.

If *outcome* is [`<span class="pre">None</span>`](https://docs.python.org/3/library/constants.html#None "None"), the subtest succeeded. Otherwise, it failed with an exception where *outcome* is a tuple of the form returned by [`<span class="pre">sys.exc_info()</span>`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info"): `<span class="pre">(type,</span><span> </span><span class="pre">value,</span><span> </span><span class="pre">traceback)</span>`.

The default implementation does nothing when the outcome is a success, and records subtest failures as normal failures.

**Added in version 3.4.**

addDuration**(** *test* ,  *elapsed* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addDuration "Link to this definition")Called when the test case finishes. *elapsed* is the time represented in seconds, and it includes the execution of cleanup functions.

**Added in version 3.12.**

*class *unittest.**TextTestResult**( *stream* ,  *descriptions* ,  *verbosity* ,  *** ,  *durations**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TextTestResult "Link to this definition")A concrete implementation of [`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") used by the [`<span class="pre">TextTestRunner</span>`](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner "unittest.TextTestRunner"). Subclasses should accept `<span class="pre">**kwargs</span>` to ensure compatibility as the interface changes.

**Added in version 3.2.**

**Changed in version 3.12:** Added the *durations* keyword parameter.

unittest.**defaultTestLoader**[](https://docs.python.org/3/library/unittest.html#unittest.defaultTestLoader "Link to this definition")Instance of the [`<span class="pre">TestLoader</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") class intended to be shared. If no customization of the [`<span class="pre">TestLoader</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") is needed, this instance can be used instead of repeatedly creating new instances.

*class *unittest.**TextTestRunner**( *stream**=**None* ,  *descriptions**=**True* ,  *verbosity**=**1* ,  *failfast**=**False* ,  *buffer**=**False* ,  *resultclass**=**None* ,  *warnings**=**None* ,  *** ,  *tb_locals**=**False* ,  *durations**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner "Link to this definition")A basic test runner implementation that outputs results to a stream. If *stream* is `<span class="pre">None</span>`, the default, [`<span class="pre">sys.stderr</span>`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") is used as the output stream. This class has a few configurable parameters, but is essentially very simple. Graphical applications which run test suites should provide alternate implementations. Such implementations should accept `<span class="pre">**kwargs</span>` as the interface to construct runners changes when features are added to unittest.

By default this runner shows [`<span class="pre">DeprecationWarning</span>`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning"), [`<span class="pre">PendingDeprecationWarning</span>`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning"), [`<span class="pre">ResourceWarning</span>`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning") and [`<span class="pre">ImportWarning</span>`](https://docs.python.org/3/library/exceptions.html#ImportWarning "ImportWarning") even if they are [ignored by default](https://docs.python.org/3/library/warnings.html#warning-ignored). This behavior can be overridden using Python’s `<span class="pre">-Wd</span>` or `<span class="pre">-Wa</span>` options (see [Warning control](https://docs.python.org/3/using/cmdline.html#using-on-warnings)) and leaving *warnings* to `<span class="pre">None</span>`.

**Changed in version 3.2:** Added the *warnings* parameter.

**Changed in version 3.2:** The default stream is set to [`<span class="pre">sys.stderr</span>`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") at instantiation time rather than import time.

**Changed in version 3.5:** Added the *tb_locals* parameter.

**Changed in version 3.12:** Added the *durations* parameter.

_makeResult**(**)[](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner._makeResult "Link to this definition")This method returns the instance of `<span class="pre">TestResult</span>` used by [`<span class="pre">run()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner.run "unittest.TextTestRunner.run"). It is not intended to be called directly, but can be overridden in subclasses to provide a custom `<span class="pre">TestResult</span>`.

`<span class="pre">_makeResult()</span>` instantiates the class or callable passed in the `<span class="pre">TextTestRunner</span>` constructor as the `<span class="pre">resultclass</span>` argument. It defaults to [`<span class="pre">TextTestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TextTestResult "unittest.TextTestResult") if no `<span class="pre">resultclass</span>` is provided. The result class is instantiated with the following arguments:

```
stream, descriptions, verbosity
```

run**(** *test* **)**[](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner.run "Link to this definition")This method is the main public interface to the `<span class="pre">TextTestRunner</span>`. This method takes a [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") or [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instance. A [`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") is created by calling [`<span class="pre">_makeResult()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner._makeResult "unittest.TextTestRunner._makeResult") and the test(s) are run and the results printed to stdout.

unittest.**main**( *module**=**'__main__'* ,  *defaultTest**=**None* ,  *argv**=**None* ,  *testRunner**=**None* ,  *testLoader**=**unittest.defaultTestLoader* ,  *exit**=**True* ,  *verbosity**=**1* ,  *failfast**=**None* ,  *catchbreak**=**None* ,  *buffer**=**None* ,  *warnings**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.main "Link to this definition")A command-line program that loads a set of tests from *module* and runs them; this is primarily for making test modules conveniently executable. The simplest use for this function is to include the following line at the end of a test script:

```
if __name__ == '__main__':
    unittest.main()
```

You can run tests with more detailed information by passing in the verbosity argument:

```
if __name__ == '__main__':
    unittest.main(verbosity=2)
```

The *defaultTest* argument is either the name of a single test or an iterable of test names to run if no test names are specified via  *argv* . If not specified or `<span class="pre">None</span>` and no test names are provided via  *argv* , all tests found in *module* are run.

The *argv* argument can be a list of options passed to the program, with the first element being the program name. If not specified or `<span class="pre">None</span>`, the values of [`<span class="pre">sys.argv</span>`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv") are used.

The *testRunner* argument can either be a test runner class or an already created instance of it. By default `<span class="pre">main</span>` calls [`<span class="pre">sys.exit()</span>`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit") with an exit code indicating success (0) or failure (1) of the tests run. An exit code of 5 indicates that no tests were run or skipped.

The *testLoader* argument has to be a [`<span class="pre">TestLoader</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") instance, and defaults to [`<span class="pre">defaultTestLoader</span>`](https://docs.python.org/3/library/unittest.html#unittest.defaultTestLoader "unittest.defaultTestLoader").

`<span class="pre">main</span>` supports being used from the interactive interpreter by passing in the argument `<span class="pre">exit=False</span>`. This displays the result on standard output without calling [`<span class="pre">sys.exit()</span>`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit"):

**>>>**

```
>>> from unittest import main
>>> main(module='test_module', exit=False)
```

The  *failfast* , *catchbreak* and *buffer* parameters have the same effect as the same-name [command-line options](https://docs.python.org/3/library/unittest.html#command-line-options).

The *warnings* argument specifies the [warning filter](https://docs.python.org/3/library/warnings.html#warning-filter) that should be used while running the tests. If it’s not specified, it will remain `<span class="pre">None</span>` if a `<span class="pre">-W</span>` option is passed to **python** (see [Warning control](https://docs.python.org/3/using/cmdline.html#using-on-warnings)), otherwise it will be set to `<span class="pre">'default'</span>`.

Calling `<span class="pre">main</span>` actually returns an instance of the `<span class="pre">TestProgram</span>` class. This stores the result of the tests run as the `<span class="pre">result</span>` attribute.

**Changed in version 3.1:** The *exit* parameter was added.

**Changed in version 3.2:** The  *verbosity* ,  *failfast* ,  *catchbreak* , *buffer* and *warnings* parameters were added.

**Changed in version 3.4:** The *defaultTest* parameter was changed to also accept an iterable of test names.

#### load_tests Protocol

**Added in version 3.2.**

Modules or packages can customize how tests are loaded from them during normal test runs or test discovery by implementing a function called `<span class="pre">load_tests</span>`.

If a test module defines `<span class="pre">load_tests</span>` it will be called by [`<span class="pre">TestLoader.loadTestsFromModule()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromModule "unittest.TestLoader.loadTestsFromModule") with the following arguments:

```
load_tests(loader, standard_tests, pattern)
```

where *pattern* is passed straight through from `<span class="pre">loadTestsFromModule</span>`. It defaults to `<span class="pre">None</span>`.

It should return a [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite").

*loader* is the instance of [`<span class="pre">TestLoader</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") doing the loading. *standard_tests* are the tests that would be loaded by default from the module. It is common for test modules to only want to add or remove tests from the standard set of tests. The third argument is used when loading packages as part of test discovery.

A typical `<span class="pre">load_tests</span>` function that loads tests from a specific set of [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") classes may look like:

```
test_cases = (TestCase1, TestCase2, TestCase3)

def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite
```

If discovery is started in a directory containing a package, either from the command line or by calling [`<span class="pre">TestLoader.discover()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.discover "unittest.TestLoader.discover"), then the package `<span class="pre">__init__.py</span>` will be checked for `<span class="pre">load_tests</span>`. If that function does not exist, discovery will recurse into the package as though it were just another directory. Otherwise, discovery of the package’s tests will be left up to `<span class="pre">load_tests</span>` which is called with the following arguments:

```
load_tests(loader, standard_tests, pattern)
```

This should return a [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") representing all the tests from the package. (`<span class="pre">standard_tests</span>` will only contain tests collected from `<span class="pre">__init__.py</span>`.)

Because the pattern is passed into `<span class="pre">load_tests</span>` the package is free to continue (and potentially modify) test discovery. A ‘do nothing’ `<span class="pre">load_tests</span>` function for a test package would look like:

```
def load_tests(loader, standard_tests, pattern):
    # top level directory cached on loader instance
    this_dir = os.path.dirname(__file__)
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
    standard_tests.addTests(package_tests)
    return standard_tests
```

**Changed in version 3.5:** Discovery no longer checks package names for matching *pattern* due to the impossibility of package names matching the default pattern.

## Class and Module Fixtures

Class and module level fixtures are implemented in [`<span class="pre">TestSuite</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite"). When the test suite encounters a test from a new class then `<span class="pre">tearDownClass()</span>` from the previous class (if there is one) is called, followed by `<span class="pre">setUpClass()</span>` from the new class.

Similarly if a test is from a different module from the previous test then `<span class="pre">tearDownModule</span>` from the previous module is run, followed by `<span class="pre">setUpModule</span>` from the new module.

After all the tests have run the final `<span class="pre">tearDownClass</span>` and `<span class="pre">tearDownModule</span>` are run.

Note that shared fixtures do not play well with [potential] features like test parallelization and they break test isolation. They should be used with care.

The default ordering of tests created by the unittest test loaders is to group all tests from the same modules and classes together. This will lead to `<span class="pre">setUpClass</span>` / `<span class="pre">setUpModule</span>` (etc) being called exactly once per class and module. If you randomize the order, so that tests from different modules and classes are adjacent to each other, then these shared fixture functions may be called multiple times in a single test run.

Shared fixtures are not intended to work with suites with non-standard ordering. A `<span class="pre">BaseTestSuite</span>` still exists for frameworks that don’t want to support shared fixtures.

If there are any exceptions raised during one of the shared fixture functions the test is reported as an error. Because there is no corresponding test instance an `<span class="pre">_ErrorHolder</span>` object (that has the same interface as a [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")) is created to represent the error. If you are just using the standard unittest test runner then this detail doesn’t matter, but if you are a framework author it may be relevant.

### setUpClass and tearDownClass

These must be implemented as class methods:

```
import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._connection = createExpensiveConnectionObject()

    @classmethod
    def tearDownClass(cls):
        cls._connection.destroy()
```

If you want the `<span class="pre">setUpClass</span>` and `<span class="pre">tearDownClass</span>` on base classes called then you must call up to them yourself. The implementations in [`<span class="pre">TestCase</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") are empty.

If an exception is raised during a `<span class="pre">setUpClass</span>` then the tests in the class are not run and the `<span class="pre">tearDownClass</span>` is not run. Skipped classes will not have `<span class="pre">setUpClass</span>` or `<span class="pre">tearDownClass</span>` run. If the exception is a [`<span class="pre">SkipTest</span>`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") exception then the class will be reported as having been skipped instead of as an error.

### setUpModule and tearDownModule

These should be implemented as functions:

```
def setUpModule():
    createConnection()

def tearDownModule():
    closeConnection()
```

If an exception is raised in a `<span class="pre">setUpModule</span>` then none of the tests in the module will be run and the `<span class="pre">tearDownModule</span>` will not be run. If the exception is a [`<span class="pre">SkipTest</span>`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") exception then the module will be reported as having been skipped instead of as an error.

To add cleanup code that must be run even in the case of an exception, use `<span class="pre">addModuleCleanup</span>`:

unittest.**addModuleCleanup**( *function* ,  */* ,  ****args*** ,  ***kwargs* **)**[](https://docs.python.org/3/library/unittest.html#unittest.addModuleCleanup "Link to this definition")Add a function to be called after `<span class="pre">tearDownModule()</span>` to cleanup resources used during the test class. Functions will be called in reverse order to the order they are added (LIFO). They are called with any arguments and keyword arguments passed into [`<span class="pre">addModuleCleanup()</span>`](https://docs.python.org/3/library/unittest.html#unittest.addModuleCleanup "unittest.addModuleCleanup") when they are added.

If `<span class="pre">setUpModule()</span>` fails, meaning that `<span class="pre">tearDownModule()</span>` is not called, then any cleanup functions added will still be called.

**Added in version 3.8.**

*classmethod *unittest.**enterModuleContext**( *cm* **)**[](https://docs.python.org/3/library/unittest.html#unittest.enterModuleContext "Link to this definition")Enter the supplied [context manager](https://docs.python.org/3/glossary.html#term-context-manager). If successful, also add its [`<span class="pre">__exit__()</span>`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__") method as a cleanup function by [`<span class="pre">addModuleCleanup()</span>`](https://docs.python.org/3/library/unittest.html#unittest.addModuleCleanup "unittest.addModuleCleanup") and return the result of the [`<span class="pre">__enter__()</span>`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__") method.

**Added in version 3.11.**

unittest.**doModuleCleanups**(**)**[](https://docs.python.org/3/library/unittest.html#unittest.doModuleCleanups "Link to this definition")This function is called unconditionally after `<span class="pre">tearDownModule()</span>`, or after `<span class="pre">setUpModule()</span>` if `<span class="pre">setUpModule()</span>` raises an exception.

It is responsible for calling all the cleanup functions added by [`<span class="pre">addModuleCleanup()</span>`](https://docs.python.org/3/library/unittest.html#unittest.addModuleCleanup "unittest.addModuleCleanup"). If you need cleanup functions to be called *prior* to `<span class="pre">tearDownModule()</span>` then you can call [`<span class="pre">doModuleCleanups()</span>`](https://docs.python.org/3/library/unittest.html#unittest.doModuleCleanups "unittest.doModuleCleanups") yourself.

[`<span class="pre">doModuleCleanups()</span>`](https://docs.python.org/3/library/unittest.html#unittest.doModuleCleanups "unittest.doModuleCleanups") pops methods off the stack of cleanup functions one at a time, so it can be called at any time.

**Added in version 3.8.**

## Signal Handling

**Added in version 3.2.**

The [`<span class="pre">-c/--catch</span>`](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-c) command-line option to unittest, along with the `<span class="pre">catchbreak</span>` parameter to [`<span class="pre">unittest.main()</span>`](https://docs.python.org/3/library/unittest.html#unittest.main "unittest.main"), provide more friendly handling of control-C during a test run. With catch break behavior enabled control-C will allow the currently running test to complete, and the test run will then end and report all the results so far. A second control-c will raise a [`<span class="pre">KeyboardInterrupt</span>`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt") in the usual way.

The control-c handling signal handler attempts to remain compatible with code or tests that install their own [`<span class="pre">signal.SIGINT</span>`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT") handler. If the `<span class="pre">unittest</span>` handler is called but *isn’t* the installed [`<span class="pre">signal.SIGINT</span>`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT") handler, i.e. it has been replaced by the system under test and delegated to, then it calls the default handler. This will normally be the expected behavior by code that replaces an installed handler and delegates to it. For individual tests that need `<span class="pre">unittest</span>` control-c handling disabled the [`<span class="pre">removeHandler()</span>`](https://docs.python.org/3/library/unittest.html#unittest.removeHandler "unittest.removeHandler") decorator can be used.

There are a few utility functions for framework authors to enable control-c handling functionality within test frameworks.

unittest.**installHandler**(**)**[](https://docs.python.org/3/library/unittest.html#unittest.installHandler "Link to this definition")Install the control-c handler. When a [`<span class="pre">signal.SIGINT</span>`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT") is received (usually in response to the user pressing control-c) all registered results have [`<span class="pre">stop()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stop "unittest.TestResult.stop") called.

unittest.**registerResult**( *result* **)**[](https://docs.python.org/3/library/unittest.html#unittest.registerResult "Link to this definition")Register a [`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") object for control-c handling. Registering a result stores a weak reference to it, so it doesn’t prevent the result from being garbage collected.

Registering a [`<span class="pre">TestResult</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") object has no side-effects if control-c handling is not enabled, so test frameworks can unconditionally register all results they create independently of whether or not handling is enabled.

unittest.**removeResult**( *result* **)**[](https://docs.python.org/3/library/unittest.html#unittest.removeResult "Link to this definition")Remove a registered result. Once a result has been removed then [`<span class="pre">stop()</span>`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stop "unittest.TestResult.stop") will no longer be called on that result object in response to a control-c.

unittest.**removeHandler**( *function**=**None* **)**[](https://docs.python.org/3/library/unittest.html#unittest.removeHandler "Link to this definition")When called without arguments this function removes the control-c handler if it has been installed. This function can also be used as a test decorator to temporarily remove the handler while the test is being executed:

```
@unittest.removeHandler
def test_signal_handling(self):
```
