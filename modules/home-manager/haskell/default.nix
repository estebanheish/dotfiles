{pkgs, ...}: {
  home.packages = with pkgs; [
    (
      let
        haskellPkgs = ps:
          with ps; [
            brick
            aeson
            wreq
            QuickCheck
            regex-pcre
            matrix
            split
            #http-conduit
            #scalpel
            #cursor
            #http-conduit
          ];
      in (haskellPackages.ghcWithPackages haskellPkgs)
    )
    stack
    haskell-language-server
    # haskellPackages.ghcup
  ];
}
