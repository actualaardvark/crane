# This is a workaround taken from neon's personal configuration. It sources the nixpkgs
# version from `flake.lock` to avoid using channels.
let
  lock = (builtins.fromJSON (builtins.readFile ./flake.lock)).nodes.nixpkgs.locked;
in
  import (fetchTarball {
    url = "https://github.com/nixos-unstable/nixpkgs/archive/${lock.rev}.tar.gz";
    sha256 = lock.narHash;
  })
