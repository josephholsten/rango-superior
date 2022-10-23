# Rango Superior

A collection of first-rank packages of go packages, available at:

  https://copr.fedorainfracloud.org/coprs/josephholsten/rango-superior/

## Why not just package go software acording to the existing Fedora/EPEL strategy?

Fedora packages of go software rely on RPM packages of every single dependency, particularly go library-only codebases. This leads to an explosion of dependencies, which must necessarily expand to match the versions also specified by the go module dependency specification. This strategy has certain benefits, especially if there are important reasons to track all dependency metadata and versions. If, for example, there are CVEs you must detect and mitigate. Or, should you intend to distribute these packages and need to prohibit certain licences or authors. That is, if your linux use cases are especially Enterprise.

Instead, rango-superior uses an alternative packaging scheme: we trust the authors of go tools to have tracked their dependencies in their source build process. We may even go so far as just to wrap a published binary for installation convenience.

## Can you include a package for my go tool?

Maybe? Most of the time it's best for a development team to maintain their own package. But if you'd like to maintain that package spec here, that's fine.
