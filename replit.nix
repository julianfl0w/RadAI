{ pkgs }: {
  deps = [
    pkgs.python39Packages.poetry
    pkgs.python39Packages.pip
    pkgs.sudo
    pkgs.qtile
  ];
}