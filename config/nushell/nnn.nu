let cfgHome = ($env | default $"($env.HOME)/.config" XDG_CONFIG_HOME | get XDG_CONFIG_HOME)
let-env NNN_TMPFILE = $"($cfgHome)/nnn/.lastd"

def-env ncd [...x] {
  # Launch nnn. Add desired flags after `^nnn`, ex: `^nnn -eda ($x | str join)`
  ^nnn ($x | str join)
  let newpath = (
    if ($env.NNN_TMPFILE | path exists) {
      let newpath = (open $env.NNN_TMPFILE | parse 'cd "{nnnpath}"').0.nnnpath
      ^rm -f $env.NNN_TMPFILE
      echo $newpath
    } else {
      pwd
    }
  )
  cd $newpath
}