# This sample verifies that the use of a bound TypeVar defined
# by a generic class is not used inappropriately.

from typing import Any, Generic, TypeVar


class Bar:
    ...


_T = TypeVar("_T", bound=Bar)


class Foo(Generic[_T]):
    def func1(self, a: _T):
        pass

    def func2(self):
        x: int = 3
        # This should generate an error
        self.func1(x)

        y = Bar()
        self.func1(y)

        z: Any = 3
        self.func1(z)
