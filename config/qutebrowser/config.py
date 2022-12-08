config.load_autoconfig()

c.colors.webpage.darkmode.enabled = True
c.colors.webpage.preferred_color_scheme = "dark"
c.fonts.default_family = "Ubuntu"
c.fonts.statusbar = "bold"
c.fonts.tabs.selected = "bold"
c.fonts.tabs.unselected = "bold"
c.fonts.web.family.standard = "Ubuntu"
c.tabs.favicons.scale = 1
c.tabs.indicator.width = 1
c.zoom.default = 150

c.url.searchengines["amazon"] = "https://www.amazon.es/s?k={}"
c.url.searchengines["aw"] = "https://wiki.archlinux.org/?search={}"
c.url.searchengines["g"] = "https://www.google.com/search?hl=en&q={}"
c.url.searchengines[
    "np"
] = "https://search.nixos.org/packages?channel=unstable&from=0&size=50&sort=relevance&query={}"
c.url.searchengines["nw"] = "https://nixos.wiki/?search={}"
c.url.searchengines["w"] = "https://en.wikipedia.org/wiki/?search={}"
c.url.searchengines["y"] = "https://www.youtube.com/results?search_query={}"

base00 = "#101419"
base01 = "#252A30"
base02 = "#3A3F46"
base03 = "#636972"
base04 = "#8D949E"
base05 = "#b6beca"
base06 = "#BDC4CF"
base07 = "#C3C9D3"
base08 = "#e05f65"
base09 = "#f08e48"
base0A = "#f1cf8a"
base0B = "#78dba9"
base0C = "#74bee9"
base0D = "#70a5eb"
base0E = "#c68aee"
base0F = "#1c252c"
focus = "#78dba9"

c.colors.completion.category.bg = focus
c.colors.completion.category.border.bottom = base00
c.colors.completion.category.border.top = base00
c.colors.completion.category.fg = base00
c.colors.completion.even.bg = base00
c.colors.completion.fg = base05
c.colors.completion.item.selected.bg = base02
c.colors.completion.item.selected.border.bottom = base02
c.colors.completion.item.selected.border.top = base02
c.colors.completion.item.selected.fg = base05
c.colors.completion.item.selected.match.fg = base05
c.colors.completion.match.fg = base09
c.colors.completion.odd.bg = base00
c.colors.completion.scrollbar.bg = base00
c.colors.completion.scrollbar.fg = base05
c.colors.contextmenu.disabled.bg = base01
c.colors.contextmenu.disabled.fg = base04
c.colors.contextmenu.menu.bg = base00
c.colors.contextmenu.menu.fg = base05
c.colors.contextmenu.selected.bg = base02
c.colors.contextmenu.selected.fg = base05
c.colors.downloads.bar.bg = base00
c.colors.downloads.error.fg = base08
c.colors.downloads.start.bg = focus
c.colors.downloads.start.fg = base00
c.colors.downloads.stop.bg = base0C
c.colors.downloads.stop.fg = base00
c.colors.hints.bg = base0A
c.colors.hints.fg = base00
c.colors.hints.match.fg = base05
c.colors.keyhint.bg = base00
c.colors.keyhint.fg = base05
c.colors.keyhint.suffix.fg = base05
c.colors.messages.error.bg = base08
c.colors.messages.error.border = base08
c.colors.messages.error.fg = base00
c.colors.messages.info.bg = base00
c.colors.messages.info.border = base00
c.colors.messages.info.fg = base05
c.colors.messages.warning.bg = base0E
c.colors.messages.warning.border = base0E
c.colors.messages.warning.fg = base00
c.colors.prompts.bg = base00
c.colors.prompts.border = base00
c.colors.prompts.fg = base05
c.colors.prompts.selected.bg = base02
c.colors.prompts.selected.fg = base05
c.colors.statusbar.caret.bg = base00
c.colors.statusbar.caret.fg = focus
c.colors.statusbar.caret.selection.bg = base00
c.colors.statusbar.caret.selection.fg = focus
c.colors.statusbar.command.bg = base01
c.colors.statusbar.command.fg = base05
c.colors.statusbar.command.private.bg = base01
c.colors.statusbar.command.private.fg = base0E
c.colors.statusbar.insert.bg = base00
c.colors.statusbar.insert.fg = base0C
c.colors.statusbar.normal.bg = base00
c.colors.statusbar.normal.fg = base05
c.colors.statusbar.passthrough.bg = base00
c.colors.statusbar.passthrough.fg = base0A
c.colors.statusbar.private.bg = base00
c.colors.statusbar.private.fg = base0E
c.colors.statusbar.progress.bg = focus
c.colors.statusbar.url.error.fg = base08
c.colors.statusbar.url.fg = base05
c.colors.statusbar.url.hover.fg = base09
c.colors.statusbar.url.success.http.fg = base0B
c.colors.statusbar.url.success.https.fg = base0B
c.colors.statusbar.url.warn.fg = base0E
c.colors.tabs.bar.bg = base00
c.colors.tabs.even.bg = base00
c.colors.tabs.even.fg = base05
c.colors.tabs.indicator.error = base08
c.colors.tabs.indicator.start = focus
c.colors.tabs.indicator.stop = base0C
c.colors.tabs.odd.bg = base00
c.colors.tabs.odd.fg = base05
c.colors.tabs.pinned.even.bg = base0B
c.colors.tabs.pinned.even.fg = base00
c.colors.tabs.pinned.odd.bg = base0B
c.colors.tabs.pinned.odd.fg = base00
c.colors.tabs.pinned.selected.even.bg = base02
c.colors.tabs.pinned.selected.even.fg = base05
c.colors.tabs.pinned.selected.odd.bg = base02
c.colors.tabs.pinned.selected.odd.fg = base05
c.colors.tabs.selected.even.bg = focus
c.colors.tabs.selected.even.fg = base00
c.colors.tabs.selected.odd.bg = focus
c.colors.tabs.selected.odd.fg = base00
c.colors.webpage.bg = base00
