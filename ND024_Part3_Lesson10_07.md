# Lesson 10.7 Extending Your Editor

Sublime doesn't have a built in plug in repository so the first thing we'll need to do is install package control.

Run this in Sublime's terminal ctrl+`:
```
import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

Bring up Sublime's Command Palette: `ctrl+shift+P`
Seclect `Package Control: Install Package`

Plugins to Install
- Emmet - Extends and improves Sublime's built in text snippets.
- Sidebar Enhancements - Extends the right-click menu.
- Color Picker - Press Ctrl+Shift+C to bring up the color picker.
- Color Highlighter - It'll give us a preview of the color.

- - -
Next up: [Quiz: Using the Palette](ND024_Part3_Lesson10_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
