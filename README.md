# resilver-orders

A synthetic test fixture (walk 102943). `orders` is a tiny Python package that depends on a toy HTTP
library, `platform-http`, which exists only as the two wheels under `ci/wheels/`.

It is here so that a software-maintenance tool can be exercised against a real code host.
The branch `renovate/platform-http-4.x` moves the package to version 4 of the toy library,
which renames a method and breaks a test; the tool is then asked to repair that pull request.

Nothing here is a real service, and nothing here is meant to be used.
