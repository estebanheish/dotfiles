{user, ...}: {
  programs.nh = {
    enable = true;
    clean.enable = true;
    flake = "/home/${user}/.dots";
  };
}
