# package-rs

Rust reference package: the `game-kit` contract, a CLI example, tests, and
crate release notes.

## Layout

| Path | Holds |
| --- | --- |
| `src/lib.rs` | publishable crate |
| `tests/` | contract tests |
| `examples/cli.rs` | full CLI example |
| `docs/` | usage and release notes |

## Build

```bash
cargo test --all
cargo build --examples
```
