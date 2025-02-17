{pkgs ? (import ./nixpkgs.nix) {}}: {
  default = pkgs.mkShell {
    NIX_CONFIG = "experimental-features = nix-command flakes"; # Likely unnescessary
    nativeBuildInputs = with pkgs; [
      python313
      python313Packages.pip
      python313Packages.numpy
      python313Packages.opencv4
      python313Packages.pillow
    ];
  };
}
