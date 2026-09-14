Nous allons vérifier que Vim est installé.

Pour cela, ouvrez un terminal et tapez la commande suivante:
```console
vim --version
```

Si Vim est installé vous devriez avoir quelque chose comme ça qui s'affiche:
```console
VIM - Vi IMproved 8.1 (2018 May 18, compiled Mar 19 2020 13:12:18)
Included patches: 1-875, 878, 884, 948, 1046, 1365-1368, 1382, 1401
Modified by team+vim@tracker.debian.org
Compiled by team+vim@tracker.debian.org
Huge version without GUI.  Features included (+) or not (-):
+acl               +extra_search      +mouse_netterm     +tag_old_static
+arabic            +farsi             +mouse_sgr         -tag_any_white
+autocmd           +file_in_path      -mouse_sysmouse    -tcl
+autochdir         +find_in_path      +mouse_urxvt       +termguicolors
-autoservername    +float             +mouse_xterm       +terminal
-balloon_eval      +folding           +multi_byte        +terminfo
+balloon_eval_term -footer            +multi_lang        +termresponse
-browse            +fork()            -mzscheme          +textobjects
++builtin_terms    +gettext           +netbeans_intg     +textprop
+byte_offset       -hangul_input      +num64             +timers
+channel           +iconv             +packages          +title
+cindent           +insert_expand     +path_extra        -toolbar
-clientserver      +job               -perl              +user_commands
-clipboard         +jumplist          +persistent_undo   +vartabs
+cmdline_compl     +keymap            +postscript        +vertsplit
+cmdline_hist      +lambda            +printer           +virtualedit
+cmdline_info      +langmap           +profile           +visual
+comments          +libcall           -python            +visualextra
+conceal           +linebreak         +python3           +viminfo
+cryptv            +lispindent        +quickfix          +vreplace
+cscope            +listcmds          +reltime           +wildignore
+cursorbind        +localmap          +rightleft         +wildmenu
+cursorshape       -lua               -ruby              +windows
+dialog_con        +menu              +scrollbind        +writebackup
+diff              +mksession         +signs             -X11
+digraphs          +modify_fname      +smartindent       -xfontset
-dnd               +mouse             +startuptime       -xim
-ebcdic            -mouseshape        +statusline        -xpm
+emacs_tags        +mouse_dec         -sun_workshop      -xsmp
+eval              +mouse_gpm         +syntax            -xterm_clipboard
+ex_extra          -mouse_jsbterm     +tag_binary        -xterm_save
   system vimrc file: "$VIM/vimrc"
     user vimrc file: "$HOME/.vimrc"
 2nd user vimrc file: "~/.vim/vimrc"
      user exrc file: "$HOME/.exrc"
       defaults file: "$VIMRUNTIME/defaults.vim"
  fall-back for $VIM: "/usr/share/vim"
Compilation: gcc -c -I. -Iproto -DHAVE_CONFIG_H   -Wdate-time  -g -O2 -fdebug-prefix-map=/build/vim-ETdSYz/vim-8.1.0875=. -fstack-protector-strong -Wformat -Werror=format-security -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1       
Linking: gcc   -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-z,now -Wl,--as-needed -o vim        -lm -ltinfo -lnsl  -lselinux  -lacl -lattr -lgpm -ldl     -L/usr/lib/python3.7/config-3.7m-x86_64-linux-gnu -lpython3.7m -lcrypt -lpthread -ldl -lutil -lm 
```

Cela fait beaucoup d'informations, mais la première ligne nous donne la version de Vim installé (ici Vim 8.1).

Dans le cas où vim n'était pas installé la commande devrait vous renvoyer une erreur de ce type:
```console
command not found: vim
```
Auquel cas je vous invite à recommencer l'étape d'installation.