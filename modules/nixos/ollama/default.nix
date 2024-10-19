{
  inputs,
  pkgs,
  ...
}: {
  disabledModules = [
    "services/misc/ollama.nix"
    "services/misc/open-webui.nix"
  ];
  imports = [
    "${inputs.master}/nixos/modules/services/misc/ollama.nix"
    "${inputs.stable}/nixos/modules/services/misc/open-webui.nix"
  ];

  # environment.systemPackages = [inputs.master.legacyPackages.${pkgs.system}.lsp-ai];

  services.ollama = {
    enable = true;
    acceleration = "rocm";
    # package = outputs.packages.${pkgs.system}.ollama;
    rocmOverrideGfx = "11.0.0";
    environmentVariables = {
      OLLAMA_KEEP_ALIVE = "15m";
    };
  };

  services.open-webui = {
    enable = true;
    port = 11111;
    openFirewall = true;
    environment = {
      OLLAMA_API_BASE_URL = "http://localhost:11434";
      WEBUI_AUTH = "False";
    };
    package = inputs.stable.legacyPackages.${pkgs.system}.open-webui;
  };
}
