- <a name="reportShadowedImports"></a> **reportShadowedImports** [boolean or string, optional]: Generate or suppress diagnostics for files that are overriding a module in the stdlib. The default value for this setting is `"none"`.

## Execution Environment Options
Pyright allows multiple execution environments to be defined for different portions of your source tree. For example, a subtree may be designed to run with different import search paths or a different version of the python interpreter than the rest of the source base.

The following settings can be specified for each execution environment.

- **root** [string, required]: Root path for the code that will execute within this execution environment.

- **extraPaths** [array of strings, optional]: Additional search paths (in addition to the root path) that will be used when searching for modules imported by files within this execution environment. If specified, this overrides the default extraPaths setting when resolving imports for files within this execution environment. Note that each files execution environment mapping is independent, so if file A is in one execution environment and imports a second file B within a second execution environment, any imports from B will use the extraPaths in the second execution environment.

- **pythonVersion** [string, optional]: The version of Python used for this execution environment. If not specified, the global `pythonVersion` setting is used instead.

- **pythonPlatform** [string, optional]: Specifies the target platform that will be used for this execution environment. If not specified, the global `pythonPlatform` setting is used instead.

In addition, any of the [type check diagnostics settings](configuration.md/type-check-diagnostics-settings) listed above can be specified. These settings act as overrides for the files in this execution environment.

## Sample Config File
The following is an example of a pyright config file:
```json
{
  "include": [
    "src"
  ],

  "exclude": [
    "**/node_modules",
    "**/__pycache__",
    "src/experimental",
    "src/typestubs"
  ],

  "ignore": [
    "src/oldstuff"
  ],

  "defineConstant": {
    "DEBUG": true
  },

  "stubPath": "src/stubs",

  "reportMissingImports": true,
  "reportMissingTypeStubs": false,

  "pythonVersion": "3.6",
  "pythonPlatform": "Linux",

  "executionEnvironments": [
    {
      "root": "src/web",
      "pythonVersion": "3.5",
      "pythonPlatform": "Windows",
      "extraPaths": [
        "src/service_libs"
      ]
    },
    {
      "root": "src/sdk",
      "pythonVersion": "3.0",
      "extraPaths": [
        "src/backend"
      ]
    },
    {
      "root": "src/tests",
      "extraPaths": [
        "src/tests/e2e",
        "src/sdk"
      ]
    },
    {
      "root": "src"
    }
  ]
}
```

## Sample pyproject.toml File
```toml
[tool.pyright]
include = ["src"]
exclude = ["**/node_modules",
    "**/__pycache__",
    "src/experimental",
    "src/typestubs"
]
ignore = ["src/oldstuff"]
defineConstant = { DEBUG = true }
stubPath = "src/stubs"

reportMissingImports = true
reportMissingTypeStubs = false

pythonVersion = "3.6"
pythonPlatform = "Linux"

executionEnvironments = [
  { root = "src/web", pythonVersion = "3.5", pythonPlatform = "Windows", extraPaths = [ "src/service_libs" ] },
  { root = "src/sdk", pythonVersion = "3.0", extraPaths = [ "src/backend" ] },
  { root = "src/tests", extraPaths = ["src/tests/e2e", "src/sdk" ]},
  { root = "src" }
]
```

## Diagnostic Settings Defaults

Each diagnostic setting has a default that is dictated by the specified type checking mode. The default for each rule can be overridden in the configuration file or settings. In strict type checking mode, overrides may only increase the strictness (e.g. increase the severity level from `"warning"` to `"error"`).

The following table lists the default severity levels for each diagnostic rule within each type checking mode (`"off"`, `"basic"`, `"standard"` and `"strict"`).

| Diagnostic Rule                           | Off        | Basic      | Standard   | Strict     |
| :---------------------------------------- | :--------- | :--------- | :--------- | :--------- |
| analyzeUnannotatedFunctions               | true       | true       | true       | true       |
| strictParameterNoneValue                  | true       | true       | true       | true       |
| enableTypeIgnoreComments                  | true       | true       | true       | true       |
| disableBytesTypePromotions                | false      | false      | false      | true       |
| strictListInference                       | false      | false      | false      | true       |
| strictDictionaryInference                 | false      | false      | false      | true       |
| strictSetInference                        | false      | false      | false      | true       |
| deprecateTypingAliases                    | false      | false      | false      | false      |
| enableExperimentalFeatures                | false      | false      | false      | false      |
| reportMissingTypeStubs                    | "none"     | "none"     | "none"     | "error"    |
| reportMissingModuleSource                 | "warning"  | "warning"  | "warning"  | "warning"  |
| reportInvalidTypeForm                     | "warning"  | "error"    | "error"    | "error"    |
| reportMissingImports                      | "warning"  | "error"    | "error"    | "error"    |
| reportUndefinedVariable                   | "warning"  | "error"    | "error"    | "error"    |
| reportAssertAlwaysTrue                    | "none"     | "warning"  | "warning"  | "error"    |
| reportInvalidStringEscapeSequence         | "none"     | "warning"  | "warning"  | "error"    |
| reportInvalidTypeVarUse                   | "none"     | "warning"  | "warning"  | "error"    |
| reportSelfClsParameterName                | "none"     | "warning"  | "warning"  | "error"    |
| reportUnsupportedDunderAll                | "none"     | "warning"  | "warning"  | "error"    |
| reportUnusedExpression                    | "none"     | "warning"  | "warning"  | "error"    |
| reportWildcardImportFromLibrary           | "none"     | "warning"  | "warning"  | "error"    |
| reportAbstractUsage                       | "none"     | "error"    | "error"    | "error"    |
| reportArgumentType                        | "none"     | "error"    | "error"    | "error"    |
| reportAssertTypeFailure                   | "none"     | "error"    | "error"    | "error"    |
| reportAssignmentType                      | "none"     | "error"    | "error"    | "error"    |
| reportAttributeAccessIssue                | "none"     | "error"    | "error"    | "error"    |
| reportCallIssue                           | "none"     | "error"    | "error"    | "error"    |
| reportGeneralTypeIssues                   | "none"     | "error"    | "error"    | "error"    |
| reportInconsistentOverload                | "none"     | "error"    | "error"    | "error"    |
| reportIndexIssue                          | "none"     | "error"    | "error"    | "error"    |
| reportInvalidTypeArguments                | "none"     | "error"    | "error"    | "error"    |
| reportNoOverloadImplementation            | "none"     | "error"    | "error"    | "error"    |
| reportOperatorIssue                       | "none"     | "error"    | "error"    | "error"    |
| reportOptionalSubscript                   | "none"     | "error"    | "error"    | "error"    |
| reportOptionalMemberAccess                | "none"     | "error"    | "error"    | "error"    |
| reportOptionalCall                        | "none"     | "error"    | "error"    | "error"    |
| reportOptionalIterable                    | "none"     | "error"    | "error"    | "error"    |
| reportOptionalContextManager              | "none"     | "error"    | "error"    | "error"    |
| reportOptionalOperand                     | "none"     | "error"    | "error"    | "error"    |
| reportRedeclaration                       | "none"     | "error"    | "error"    | "error"    |
| reportReturnType                          | "none"     | "error"    | "error"    | "error"    |
| reportTypedDictNotRequiredAccess          | "none"     | "error"    | "error"    | "error"    |
| reportPrivateImportUsage                  | "none"     | "error"    | "error"    | "error"    |
| reportUnboundVariable                     | "none"     | "error"    | "error"    | "error"    |
| reportUnhashable                          | "none"     | "error"    | "error"    | "error"    |
| reportUnusedCoroutine                     | "none"     | "error"    | "error"    | "error"    |
| reportUnusedExcept                        | "none"     | "error"    | "error"    | "error"    |
| reportFunctionMemberAccess                | "none"     | "none"     | "error"    | "error"    |
| reportIncompatibleMethodOverride          | "none"     | "none"     | "error"    | "error"    |
| reportIncompatibleVariableOverride        | "none"     | "none"     | "error"    | "error"    |
| reportOverlappingOverload                 | "none"     | "none"     | "error"    | "error"    |
| reportPossiblyUnboundVariable             | "none"     | "none"     | "error"    | "error"    |
| reportConstantRedefinition                | "none"     | "none"     | "none"     | "error"    |
| reportDeprecated                          | "none"     | "none"     | "none"     | "error"    |
| reportDuplicateImport                     | "none"     | "none"     | "none"     | "error"    |
| reportIncompleteStub                      | "none"     | "none"     | "none"     | "error"    |
| reportInconsistentConstructor             | "none"     | "none"     | "none"     | "error"    |
| reportInvalidStubStatement                | "none"     | "none"     | "none"     | "error"    |
| reportMatchNotExhaustive                  | "none"     | "none"     | "none"     | "error"    |
| reportMissingParameterType                | "none"     | "none"     | "none"     | "error"    |
| reportMissingTypeArgument                 | "none"     | "none"     | "none"     | "error"    |
| reportPrivateUsage                        | "none"     | "none"     | "none"     | "error"    |
| reportTypeCommentUsage                    | "none"     | "none"     | "none"     | "error"    |
| reportUnknownArgumentType                 | "none"     | "none"     | "none"     | "error"    |
| reportUnknownLambdaType                   | "none"     | "none"     | "none"     | "error"    |
| reportUnknownMemberType                   | "none"     | "none"     | "none"     | "error"    |
| reportUnknownParameterType                | "none"     | "none"     | "none"     | "error"    |
| reportUnknownVariableType                 | "none"     | "none"     | "none"     | "error"    |
| reportUnnecessaryCast                     | "none"     | "none"     | "none"     | "error"    |
| reportUnnecessaryComparison               | "none"     | "none"     | "none"     | "error"    |
| reportUnnecessaryContains                 | "none"     | "none"     | "none"     | "error"    |
| reportUnnecessaryIsInstance               | "none"     | "none"     | "none"     | "error"    |
| reportUnusedClass                         | "none"     | "none"     | "none"     | "error"    |
| reportUnusedImport                        | "none"     | "none"     | "none"     | "error"    |
| reportUnusedFunction                      | "none"     | "none"     | "none"     | "error"    |
| reportUnusedVariable                      | "none"     | "none"     | "none"     | "error"    |
| reportUntypedBaseClass                    | "none"     | "none"     | "none"     | "error"    |
| reportUntypedClassDecorator               | "none"     | "none"     | "none"     | "error"    |
| reportUntypedFunctionDecorator            | "none"     | "none"     | "none"     | "error"    |
| reportUntypedNamedTuple                   | "none"     | "none"     | "none"     | "error"    |
| reportCallInDefaultInitializer            | "none"     | "none"     | "none"     | "none"     |
| reportImplicitOverride                    | "none"     | "none"     | "none"     | "none"     |
| reportImplicitStringConcatenation         | "none"     | "none"     | "none"     | "none"     |
| reportImportCycles                        | "none"     | "none"     | "none"     | "none"     |
| reportMissingSuperCall                    | "none"     | "none"     | "none"     | "none"     |
| reportPropertyTypeMismatch                | "none"     | "none"     | "none"     | "none"     |
| reportShadowedImports                     | "none"     | "none"     | "none"     | "none"     |
| reportUninitializedInstanceVariable       | "none"     | "none"     | "none"     | "none"     |
| reportUnnecessaryTypeIgnoreComment        | "none"     | "none"     | "none"     | "none"     |
| reportUnusedCallResult                    | "none"     | "none"     | "none"     | "none"     |


## Locale Configuration

Pyright provides diagnostic messages that are translated to multiple languages. By default, pyright uses the default locale of the operating system. You can override the desired locale through the use of one of the following environment variables, listed in priority order.

```
LC_ALL="de"
LC_MESSAGES="en-us"
LANG="zh-cn"
LANGUAGE="fr"
```

When running in VS Code, the IDE's locale takes precedence. Setting these environment variables applies only when using pyright outside of VS code.
